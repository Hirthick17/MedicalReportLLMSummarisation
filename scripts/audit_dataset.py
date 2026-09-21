#!/usr/bin/env python
"""
Data-quality audit of the processed corpora (Person 1, Review 2).

Reads data/processed/<dataset>/<split>.jsonl (from import_datasets.py) and the baseline mix
(baseline_train/val.jsonl from make_baseline_split.py) and reports, per corpus and split:

  1. schema / missing fields / unusable samples (empty, too short, target == source, non-text)
  2. exact duplicates (normalized text) within a split and across splits
  3. near-duplicates (64-bit SimHash over 3-word shingles, Hamming distance <= 3)
  4. leakage: id overlap and exact / near-duplicate source dialogues between train|val and test
  5. length distributions in words and in Llama-3.1 tokens (prompt as rendered by the training
     chat template), the share of examples over the 4,096-token training window, and what
     happens to them ("lengthy conversation" policy)
  6. speaker-turn statistics for the dialogues, section-header coverage for the notes

Outputs (reports/data_audit/):
  data_audit.json   every number below, machine-readable
  data_audit.md     the human-readable report used in docs/PERSON1_DATA_PIPELINE.md
  length_hist.png   token-length histograms per corpus
  near_duplicates.jsonl   the pairs found (ids + similarity), for inspection

Usage:
  python scripts/audit_dataset.py                    # everything
  python scripts/audit_dataset.py --no-tokens        # skip the tokenizer (fast, words only)
  python scripts/audit_dataset.py --tokenizer outputs/kaggle/outputs/baseline_qlora_llama31_8b/final
"""

from __future__ import annotations

import argparse
import collections
import hashlib
import json
import re
import sys
import time
from pathlib import Path

import numpy as np

ROOT = Path(__file__).resolve().parent.parent
PROCESSED = ROOT / "data" / "processed"
OUT = ROOT / "reports" / "data_audit"
MAX_SEQ_LEN = 4096          # kernel A training window (REVIEW2_BASELINE.md §4.3)
MIN_WORDS_SRC, MIN_WORDS_TGT = 5, 2

SPLITS = {
    "aci_bench": ["train", "validation", "test_taskB_1", "test_taskC_2", "test_taskC_3"],
    "mts_dialog": ["train", "validation", "test_chat_2023", "test_sum_2023"],
    "dialogue_soap": ["train", "validation", "test"],
}
TEST = {("aci_bench", s) for s in SPLITS["aci_bench"][2:]} | {("mts_dialog", s) for s in SPLITS["mts_dialog"][2:]} | {("dialogue_soap", "test")}

# the baseline prompt (REVIEW2_BASELINE.md §4.2) — replicated here so the token audit measures what the trainer saw
SYSTEM = ("You are a clinical documentation assistant. Given the transcript of a doctor-patient consultation, "
          "write the clinical note. Include only information stated in the transcript.")
TASK = {
    "aci_bench": "Write a complete clinical note with the sections: HISTORY OF PRESENT ILLNESS, PHYSICAL EXAM, RESULTS, ASSESSMENT AND PLAN.",
    "dialogue_soap": "Write a SOAP note with the sections: Subjective, Objective, Assessment, Plan.",
    "mts_dialog": "Write the {section_header} section of the clinical note.",
}


def load(path: Path) -> list[dict]:
    if not path.exists():
        return []
    with path.open(encoding="utf-8") as fh:
        return [json.loads(l) for l in fh if l.strip()]


def norm(t: str) -> str:
    return re.sub(r"\s+", " ", t).strip().lower()


def shingles(t: str, k: int = 3) -> list[str]:
    w = re.findall(r"[a-z0-9']+", t.lower())
    return [" ".join(w[i:i + k]) for i in range(max(1, len(w) - k + 1))]


def simhash(t: str) -> int:
    v = np.zeros(64)
    for sh in shingles(t):
        h = int.from_bytes(hashlib.blake2b(sh.encode(), digest_size=8).digest(), "little")
        for b in range(64):
            v[b] += 1 if (h >> b) & 1 else -1
    return sum(1 << b for b in range(64) if v[b] > 0)


def hamming(a: int, b: int) -> int:
    return bin(a ^ b).count("1")


def near_dup_pairs(items: list[tuple[str, int]], max_dist: int = 3) -> list[tuple[str, str, int]]:
    """Banded SimHash: candidates share one of four 16-bit bands, then verify by Hamming distance."""
    pairs, seen = [], set()
    for band in range(4):
        buckets: dict[int, list[tuple[str, int]]] = collections.defaultdict(list)
        for id_, h in items:
            buckets[(h >> (16 * band)) & 0xFFFF].append((id_, h))
        for bucket in buckets.values():
            if len(bucket) < 2 or len(bucket) > 400:
                continue
            for i in range(len(bucket)):
                for j in range(i + 1, len(bucket)):
                    a, b = bucket[i], bucket[j]
                    key = (a[0], b[0]) if a[0] < b[0] else (b[0], a[0])
                    if key in seen:
                        continue
                    d = hamming(a[1], b[1])
                    if d <= max_dist:
                        seen.add(key)
                        pairs.append((key[0], key[1], d))
    return pairs


def pct(x, q=(50, 90, 95, 99, 100)):
    if len(x) == 0:
        return {}
    return {f"p{p}": int(np.percentile(x, p)) for p in q}


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--tokenizer", default=str(ROOT / "outputs/kaggle/outputs/baseline_qlora_llama31_8b/final"))
    ap.add_argument("--no-tokens", action="store_true")
    ap.add_argument("--out", default=str(OUT))
    a = ap.parse_args()
    out = Path(a.out)
    out.mkdir(parents=True, exist_ok=True)
    t0 = time.time()

    tok = None
    if not a.no_tokens:
        try:
            from transformers import AutoTokenizer
            tok = AutoTokenizer.from_pretrained(a.tokenizer)
            tmpl = Path(a.tokenizer) / "chat_template.jinja"          # newer transformers save the template as a file
            if not getattr(tok, "chat_template", None) and tmpl.exists():
                tok.chat_template = tmpl.read_text(encoding="utf-8")
            print(f"tokenizer loaded from {a.tokenizer} (vocab {len(tok)})")
        except Exception as e:  # noqa: BLE001
            print(f"tokenizer unavailable ({e}); word counts only")

    def n_tokens(rec: dict) -> tuple[int, int]:
        instr = TASK[rec["dataset"]].format(**rec.get("metadata", {}))
        msgs = [{"role": "system", "content": SYSTEM}, {"role": "user", "content": f"{instr}\n\nTRANSCRIPT:\n{rec['source_dialogue']}"}]
        p = tok.apply_chat_template(msgs, tokenize=True, add_generation_prompt=True)
        if not isinstance(p, list):
            p = list(p["input_ids"])
        t = tok(rec["target_summary"], add_special_tokens=False)["input_ids"]
        return len(p), len(t) + 1

    report: dict = {"generated": time.strftime("%Y-%m-%d %H:%M"), "max_seq_len": MAX_SEQ_LEN, "corpora": {}, "leakage": {}, "baseline_mix": {}}
    all_recs: dict[tuple[str, str], list[dict]] = {}
    md = ["# Data audit — processed corpora", "", f"Generated {report['generated']}. Training window {MAX_SEQ_LEN} tokens.", ""]

    # ---- 1–2, 5–6: per split
    md += ["## 1. Records, unusable samples, duplicates, lengths", "",
           "| corpus | split | n | unusable | exact dup (within) | src words p50/p95/max | tgt words p50/p95/max | prompt tok p50/p95/max | total tok p50/p99/max | > 4096 tok |",
           "|---|---|---|---|---|---|---|---|---|---|"]
    fig_data = {}
    for ds, splits in SPLITS.items():
        report["corpora"][ds] = {}
        for sp in splits:
            recs = load(PROCESSED / ds / f"{sp}.jsonl")
            all_recs[(ds, sp)] = recs
            if not recs:
                continue
            missing = [r["id"] for r in recs if not all(k in r for k in ("id", "dataset", "split", "source_dialogue", "target_summary"))]
            unusable = {"empty_source": [], "empty_target": [], "short_source": [], "short_target": [], "target_equals_source": [], "non_text": []}
            for r in recs:
                s, t = r["source_dialogue"], r["target_summary"]
                if not s.strip():
                    unusable["empty_source"].append(r["id"])
                elif len(s.split()) < MIN_WORDS_SRC:
                    unusable["short_source"].append(r["id"])
                if not t.strip():
                    unusable["empty_target"].append(r["id"])
                elif len(t.split()) < MIN_WORDS_TGT:
                    unusable["short_target"].append(r["id"])
                if norm(s) == norm(t):
                    unusable["target_equals_source"].append(r["id"])
                if re.search(r"[\x00-\x08\x0b\x0c\x0e-\x1f]", s + t):
                    unusable["non_text"].append(r["id"])
            src_c = collections.Counter(norm(r["source_dialogue"]) for r in recs)
            pair_c = collections.Counter(norm(r["source_dialogue"]) + "||" + norm(r["target_summary"]) for r in recs)
            dup_src = sum(n - 1 for n in src_c.values() if n > 1)
            dup_pair = sum(n - 1 for n in pair_c.values() if n > 1)
            id_dup = len(recs) - len({r["id"] for r in recs})
            sw = np.array([len(r["source_dialogue"].split()) for r in recs])
            tw = np.array([len(r["target_summary"].split()) for r in recs])
            entry = {
                "n": len(recs), "missing_fields": missing, "unusable": {k: v for k, v in unusable.items()},
                "n_unusable": len({x for v in unusable.values() for x in v}),
                "duplicate_ids": id_dup, "exact_duplicate_sources": dup_src, "exact_duplicate_pairs": dup_pair,
                "source_words": {**pct(sw), "mean": float(sw.mean())}, "target_words": {**pct(tw), "mean": float(tw.mean())},
                "compression_ratio_words": float(np.median(tw / np.maximum(sw, 1))),
            }
            if ds != "dialogue_soap" or True:
                turns = [len(re.findall(r"(?m)^\s*(?:\[(?:doctor|patient)[^\]]*\]|(?:doctor|patient)\s*:)", r["source_dialogue"], re.I)) for r in recs]
                entry["dialogue_turns"] = {**pct(np.array(turns)), "mean": float(np.mean(turns))}
            if ds == "mts_dialog":
                entry["section_headers"] = dict(collections.Counter(r["metadata"].get("section_header") for r in recs))
            if ds == "aci_bench":
                heads = collections.Counter()
                for r in recs:
                    for h in re.findall(r"(?m)^([A-Z][A-Z /&]{3,40})\s*$", r["target_summary"]):
                        heads[h.strip()] += 1
                entry["note_headers"] = dict(heads.most_common(12))
            if tok is not None:
                pt, tt = zip(*(n_tokens(r) for r in recs))
                pt, tt = np.array(pt), np.array(tt)
                tot = pt + tt
                entry["prompt_tokens"] = pct(pt)
                entry["target_tokens"] = pct(tt)
                entry["total_tokens"] = pct(tot)
                entry["over_max_seq_len"] = int((tot > MAX_SEQ_LEN).sum())
                entry["over_max_seq_len_ids"] = [r["id"] for r, x in zip(recs, tot) if x > MAX_SEQ_LEN][:20]
                entry["prompt_share"] = float((pt / tot).mean())
                fig_data[(ds, sp)] = tot
            report["corpora"][ds][sp] = entry
            f = lambda d, keys=("p50", "p95", "p100"): "/".join(str(d.get(k, "-")) for k in keys)
            md.append(f"| {ds} | {sp} | {len(recs)} | {entry['n_unusable']} | {dup_src} | {f(entry['source_words'])} | {f(entry['target_words'])} | "
                      f"{f(entry.get('prompt_tokens', {}))} | {f(entry.get('total_tokens', {}), ('p50', 'p99', 'p100'))} | {entry.get('over_max_seq_len', '-')} |")
            print(f"  {ds:14s} {sp:16s} n={len(recs):5d} unusable={entry['n_unusable']} dup={dup_src} "
                  f"tok p50/p99/max={f(entry.get('total_tokens', {}), ('p50','p99','p100'))} >{MAX_SEQ_LEN}={entry.get('over_max_seq_len','-')}")

    # ---- 3: near-duplicates within and across splits of a corpus
    md += ["", "## 2. Near-duplicates (SimHash, 3-word shingles, Hamming ≤ 3)", "", "| corpus | pairs within a split | pairs across splits | pairs involving a test split |", "|---|---|---|---|"]
    nd_out = (out / "near_duplicates.jsonl").open("w", encoding="utf-8")
    report["near_duplicates"] = {}
    for ds, splits in SPLITS.items():
        items, where = [], {}
        for sp in splits:
            for r in all_recs[(ds, sp)]:
                items.append((r["id"], simhash(r["source_dialogue"])))
                where[r["id"]] = sp
        pairs = near_dup_pairs(items)
        within = sum(1 for a, b, _ in pairs if where[a] == where[b])
        across = len(pairs) - within
        test_inv = sum(1 for a, b, _ in pairs if ((ds, where[a]) in TEST) != ((ds, where[b]) in TEST))
        report["near_duplicates"][ds] = {"pairs": len(pairs), "within_split": within, "across_splits": across, "train_or_val_vs_test": test_inv}
        for a_, b_, d in pairs:
            nd_out.write(json.dumps({"dataset": ds, "id_a": a_, "split_a": where[a_], "id_b": b_, "split_b": where[b_], "hamming": d}) + "\n")
        md.append(f"| {ds} | {within} | {across} | {test_inv} |")
        print(f"  near-dup {ds}: {len(pairs)} pairs (within {within}, across {across}, vs test {test_inv})")
    nd_out.close()

    # ---- 4: leakage between the baseline mix and every test split
    train = load(PROCESSED / "baseline_train.jsonl")
    val = load(PROCESSED / "baseline_val.jsonl")
    manifest = json.loads((PROCESSED / "train_manifest.json").read_text(encoding="utf-8")) if (PROCESSED / "train_manifest.json").exists() else {}
    tests = [r for k, recs in all_recs.items() if k in TEST for r in recs]
    tr_ids, va_ids, te_ids = {r["id"] for r in train}, {r["id"] for r in val}, {r["id"] for r in tests}
    te_src = {norm(r["source_dialogue"]): r["id"] for r in tests}
    te_tgt = {norm(r["target_summary"]): r["id"] for r in tests}
    exact_src = [(r["id"], te_src[norm(r["source_dialogue"])]) for r in train + val if norm(r["source_dialogue"]) in te_src]
    exact_tgt = [(r["id"], te_tgt[norm(r["target_summary"])]) for r in train + val if norm(r["target_summary"]) in te_tgt]
    nd = near_dup_pairs([(r["id"], simhash(r["source_dialogue"])) for r in train + val + tests])
    mix_ids = tr_ids | va_ids
    nd_leak = [(a_, b_, d) for a_, b_, d in nd if (a_ in mix_ids) != (b_ in mix_ids)]
    sha = lambda p: hashlib.sha256(p.read_bytes()).hexdigest() if p.exists() else None
    report["leakage"] = {
        "id_overlap_train_val": len(tr_ids & va_ids), "id_overlap_train_test": len(tr_ids & te_ids), "id_overlap_val_test": len(va_ids & te_ids),
        "exact_source_overlap_mix_vs_test": exact_src, "exact_target_overlap_mix_vs_test": exact_tgt,
        "near_duplicate_source_mix_vs_test": [{"mix_id": a_ if a_ in mix_ids else b_, "test_id": b_ if a_ in mix_ids else a_, "hamming": d} for a_, b_, d in nd_leak],
        "manifest_sha_train_matches": sha(PROCESSED / "baseline_train.jsonl") == manifest.get("train", {}).get("sha256"),
        "manifest_sha_val_matches": sha(PROCESSED / "baseline_val.jsonl") == manifest.get("val", {}).get("sha256"),
        "dropped_by_make_baseline_split": manifest.get("leakage_check", {}).get("dropped_for_verbatim_overlap_with_test", []),
        "status": "passed" if not (tr_ids & te_ids or va_ids & te_ids or tr_ids & va_ids or exact_src) else "FAILED",
    }
    report["baseline_mix"] = {"train": {"n": len(train), "mix": dict(collections.Counter(r["dataset"] for r in train))},
                              "val": {"n": len(val), "mix": dict(collections.Counter(r["dataset"] for r in val))},
                              "test": {f"{ds}/{sp}": len(all_recs[(ds, sp)]) for (ds, sp) in sorted(TEST)}}
    if tok is not None and train:
        tot = np.array([sum(n_tokens(r)) for r in train])
        report["baseline_mix"]["train"]["total_tokens"] = pct(tot)
        report["baseline_mix"]["train"]["over_max_seq_len"] = int((tot > MAX_SEQ_LEN).sum())
        report["baseline_mix"]["train"]["over_max_seq_len_ids"] = [r["id"] for r, x in zip(train, tot) if x > MAX_SEQ_LEN]
        fig_data[("baseline", "train")] = tot
    L = report["leakage"]
    md += ["", "## 3. Leakage checks (baseline_train + baseline_val vs. the six test splits)", "",
           f"- id overlap train/val: {L['id_overlap_train_val']}, train/test: {L['id_overlap_train_test']}, val/test: {L['id_overlap_val_test']}",
           f"- exact source-dialogue overlap with test: {len(exact_src)} (after make_baseline_split.py dropped {len(L['dropped_by_make_baseline_split'])}: {L['dropped_by_make_baseline_split']})",
           f"- exact target-note overlap with test: {len(exact_tgt)} {exact_tgt[:5] if exact_tgt else ''}",
           f"- near-duplicate source dialogues (mix vs test, Hamming ≤ 3): {len(nd_leak)}",
           f"- train_manifest.json SHA-256 matches on disk: train={L['manifest_sha_train_matches']}, val={L['manifest_sha_val_matches']}",
           f"- **status: {L['status']}**", "",
           "## 4. Baseline mix", "", f"- train: {report['baseline_mix']['train']}", f"- val: {report['baseline_mix']['val']}", f"- test: {report['baseline_mix']['test']}", ""]

    # ---- 5: lengthy conversations policy
    md += ["## 5. Lengthy conversations", "",
           f"The training window is {MAX_SEQ_LEN} tokens (prompt + note). Kernel A *drops* any example whose rendered "
           "length exceeds it rather than truncating (truncating a note teaches the model to stop early; truncating a "
           "transcript removes facts the note still asserts). At inference the prompt-only limit is the base model's "
           "128k context, so no test conversation is cut. Counts of dropped examples per split are in the table above "
           "(`> 4096 tok`).", ""]

    # ---- figure
    try:
        import matplotlib
        matplotlib.use("Agg")
        import matplotlib.pyplot as plt
        keys = [k for k in fig_data if k[1] in ("train", "test", "test_taskB_1", "test_chat_2023")]
        fig, ax = plt.subplots(1, 1, figsize=(9, 4.5))
        for k in keys:
            ax.hist(fig_data[k], bins=60, alpha=0.45, label=f"{k[0]}/{k[1]} (n={len(fig_data[k])})")
        ax.axvline(MAX_SEQ_LEN, color="k", ls="--", lw=1, label=f"max_seq_len={MAX_SEQ_LEN}")
        ax.set_xlabel("prompt + note tokens (Llama-3.1 tokenizer, training template)")
        ax.set_ylabel("examples")
        ax.set_yscale("log")
        ax.legend(fontsize=8)
        ax.set_title("Token-length distribution per corpus")
        fig.tight_layout()
        fig.savefig(out / "length_hist.png", dpi=150)
        md.append("![token length histogram](length_hist.png)\n")
    except Exception as e:  # noqa: BLE001
        print("plot skipped:", e)

    (out / "data_audit.json").write_text(json.dumps(report, indent=2), encoding="utf-8")
    (out / "data_audit.md").write_text("\n".join(md), encoding="utf-8")
    print(f"\nleakage status: {L['status']}   ->  {out / 'data_audit.md'}   ({time.time() - t0:.0f} s)")
    return 0 if L["status"] == "passed" else 1


if __name__ == "__main__":
    raise SystemExit(main())
