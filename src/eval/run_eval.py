#!/usr/bin/env python
"""
Evaluate a baseline run (Person 3, Review 2): ROUGE-1/2/L, BERTScore, length / degeneration
diagnostics and the factuality checks, per test split, with tables, graphs and example errors.

  python -m src.eval.run_eval --run outputs/kaggle/outputs/baseline_qlora_llama31_8b --label run3_rep1.2_ngram6
  python -m src.eval.run_eval --run outputs/kaggle_run1_old_decoding/outputs/baseline_qlora_llama31_8b --label run1_rep1.1
  python -m src.eval.run_eval --run ... --label ... --bertscore            # adds BERTScore (CPU: ~15-25 min for 770 items)
  python -m src.eval.run_eval --compare                                     # comparison tables + plots over every label found

Input:  <run>/predictions/baseline_qlora/*.jsonl (+ predictions/val_check.jsonl, predictions/zeroshot_base/val_check.jsonl)
        in the REVIEW2_BASELINE.md §8.3 schema.
Output: reports/eval_baseline/<label>/
          per_item.jsonl      every metric and every flagged entity for every prediction
          metrics.json        per-split aggregates (mean / std / n; truncation and degeneration counts)
          metrics.md          the same as tables
          examples.md         worst / best items and one example per error type, with the text
          figures/*.png       ROUGE-L per split, factuality rates per split, length-ratio histogram, error-type counts
        reports/eval_baseline/comparison.md + figures/  (with --compare)
"""

from __future__ import annotations

import argparse
import collections
import glob
import json
import statistics
import sys
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent.parent
sys.path.insert(0, str(ROOT))

from src.cfe import extract_facts  # noqa: E402
from src.cfe.lexicon import MTS_SECTION_MAP  # noqa: E402
from src.eval.factuality import check_factuality  # noqa: E402
from src.eval.metrics import bertscore_batch, length_stats, rouge_scores  # noqa: E402

OUT = ROOT / "reports" / "eval_baseline"
SPLIT_ORDER = ["aci_bench_test_taskB_1", "aci_bench_test_taskC_2", "aci_bench_test_taskC_3",
               "mts_dialog_test_chat_2023", "mts_dialog_test_sum_2023", "dialogue_soap_test", "val_check", "zeroshot_base/val_check"]
HEADLINE = SPLIT_ORDER[:5]
RATE_KEYS = ["rouge1", "rouge2", "rougeL", "rougeLsum", "bertscore_f1", "length_ratio", "hallucination_rate", "hallucination_rate_strict",
             "negation_flip_rate", "negation_flip_rate_vs_source", "numerical_consistency", "clinical_coverage", "clinical_coverage_important",
             "coverage_symptom", "coverage_medical_history", "coverage_diagnosis", "coverage_medication", "coverage_investigation"]
# test items whose source dialogue also appears (as a different section target) in baseline_train — data audit §3
FLAGGED_TEST_IDS = {"mts_dialog_test_chat_2023_96", "mts_dialog_test_sum_2023_78"}


def load_jsonl(p: Path) -> list[dict]:
    with p.open(encoding="utf-8") as fh:
        return [json.loads(l) for l in fh if l.strip()]


def mean_std(xs):
    xs = [x for x in xs if x is not None]
    if not xs:
        return {"mean": None, "std": None, "n": 0}
    return {"mean": statistics.fmean(xs), "std": statistics.pstdev(xs) if len(xs) > 1 else 0.0, "n": len(xs)}


def fmt(x, nd=1, scale=100):
    return "—" if x is None else f"{x * scale:.{nd}f}"


def evaluate_run(run: Path, label: str, use_bertscore: bool, limit: int | None, bertscore_cache: Path | None = None,
                 system: str = "baseline_qlora") -> dict:
    pred_dir = run / "predictions"
    files = {Path(p).stem: Path(p) for p in glob.glob(str(pred_dir / system / "*.jsonl"))}
    if system == "baseline_qlora" and (pred_dir / "val_check.jsonl").exists():
        files["val_check"] = pred_dir / "val_check.jsonl"
    if system == "baseline_qlora" and (pred_dir / "zeroshot_base" / "val_check.jsonl").exists():
        files["zeroshot_base/val_check"] = pred_dir / "zeroshot_base" / "val_check.jsonl"
    if not files:
        sys.exit(f"no prediction files under {pred_dir}")
    out = OUT / label
    (out / "figures").mkdir(parents=True, exist_ok=True)
    cfg = json.loads((run / "training_config.json").read_text(encoding="utf-8")) if (run / "training_config.json").exists() else {}

    per_item: list[dict] = []
    cache_bs: dict[tuple[str, str], float] = {}
    if bertscore_cache and bertscore_cache.exists():      # BERTScore does not depend on the fact extractor: reuse it
        for it in load_jsonl(bertscore_cache):
            if it.get("bertscore_f1") is not None:
                cache_bs[(it["split"], it["id"])] = it["bertscore_f1"]
        print(f"[{label}] reusing {len(cache_bs)} cached BERTScore values from {bertscore_cache}")
    t0 = time.time()
    for split in [s for s in SPLIT_ORDER if s in files] + [s for s in files if s not in SPLIT_ORDER]:
        rows = load_jsonl(files[split])
        if limit:
            rows = rows[:limit]
        print(f"[{label}] {split}: {len(rows)} items", flush=True)
        cache: dict[str, dict] = {}
        for r in rows:
            section = MTS_SECTION_MAP.get((r.get("metadata") or {}).get("section_header", ""), None) if r["dataset"] == "mts_dialog" else None
            key = r["id"]
            if key not in cache:   # source / reference facts are the same for every system on this item
                cache[key] = {"source": extract_facts(r["source_dialogue"], kind="dialogue"),
                              "reference": extract_facts(r["reference_summary"], kind="note", default_section=section)}
            item = {"id": r["id"], "dataset": r["dataset"], "split": split, "system": r.get("system"), "truncated": bool(r.get("truncated")),
                    "generated_tokens": r.get("generated_tokens"), "prompt_tokens": r.get("prompt_tokens"), "flagged_near_dup": r["id"] in FLAGGED_TEST_IDS,
                    "decoding": r.get("decoding")}
            item.update(rouge_scores(r["prediction"], r["reference_summary"]))
            item.update(length_stats(r["prediction"], r["reference_summary"]))
            item.update(check_factuality(r["source_dialogue"], r["reference_summary"], r["prediction"], r["dataset"], section, facts=cache[key]))
            per_item.append(item)
        if cache_bs and all((split, r["id"]) in cache_bs for r in rows):
            for it in per_item:
                if it["split"] == split:
                    it["bertscore_f1"] = cache_bs[(split, it["id"])]
        elif use_bertscore:
            idx = [i for i, it in enumerate(per_item) if it["split"] == split]
            f1 = bertscore_batch([rows[j]["prediction"] for j in range(len(idx))], [rows[j]["reference_summary"] for j in range(len(idx))])
            for i, v in zip(idx, f1):
                per_item[i]["bertscore_f1"] = v
        print(f"    done ({time.time() - t0:.0f} s elapsed)", flush=True)

    with (out / "per_item.jsonl").open("w", encoding="utf-8") as fh:
        for it in per_item:
            fh.write(json.dumps(it, ensure_ascii=False) + "\n")

    # ---- aggregate
    agg: dict = {"label": label, "run": str(run), "generated": time.strftime("%Y-%m-%d %H:%M"), "bertscore": use_bertscore,
                 "decoding": cfg.get("decoding") or (per_item[0].get("decoding") if per_item else None),
                 "training": {k: cfg.get("training", {}).get(k) for k in ("max_steps", "steps", "best_step", "best_eval_loss", "epochs_completed")} if cfg else None,
                 "splits": {}}
    for split in [s for s in SPLIT_ORDER if any(it["split"] == s for it in per_item)]:
        items = [it for it in per_item if it["split"] == split]
        e = {"n": len(items), "truncated": sum(it["truncated"] for it in items), "degenerate": sum(it["degenerate"] for it in items),
             "items_with_incorrect_diagnosis": sum(1 for it in items if it["incorrect_diagnosis"]),
             "items_with_incorrect_medication": sum(1 for it in items if it["incorrect_medication"]),
             "items_with_dosage_mismatch": sum(1 for it in items if it["dosage_mismatch"]),
             "items_with_negation_flip": sum(1 for it in items if it["negation_flips"]),
             "items_with_numerical_error": sum(1 for it in items if it["unsupported_numbers"]),
             "items_with_missing_diagnosis": sum(1 for it in items if it["missing_diagnosis"]),
             "items_with_missing_medication": sum(1 for it in items if it["missing_medication"]),
             "total_incorrect_diagnoses": sum(len(it["incorrect_diagnosis"]) for it in items),
             "total_incorrect_medications": sum(len(it["incorrect_medication"]) for it in items),
             "total_dosage_mismatches": sum(len(it["dosage_mismatch"]) for it in items),
             "total_negation_flips": sum(len(it["negation_flips"]) for it in items),
             "total_unsupported_numbers": sum(len(it["unsupported_numbers"]) for it in items),
             "total_unsupported_entities": sum(len(it["unsupported_vs_source"]) for it in items),
             "total_pred_entities": sum(it["n_pred_entities"] for it in items),
             "micro_hallucination_rate": (sum(len(it["unsupported_vs_source"]) for it in items) / max(1, sum(it["n_pred_entities"] for it in items))),
             "micro_negation_flip_rate": (sum(len(it["negation_flips"]) for it in items) / max(1, sum(it["n_shared_with_reference"] for it in items))),
             "micro_numerical_consistency": 1 - (sum(len(it["unsupported_numbers"]) for it in items) / max(1, sum(it["n_pred_numbers"] for it in items))),
             "micro_clinical_coverage": (sum(round(it["clinical_coverage"] * it["n_ref_entities"]) for it in items if it["clinical_coverage"] is not None) / max(1, sum(it["n_ref_entities"] for it in items))),
             }
        for k in RATE_KEYS:
            e[k] = mean_std([it.get(k) for it in items])
        non_trunc = [it for it in items if not it["truncated"] and not it["degenerate"]]
        e["rougeL_excluding_degenerate"] = mean_std([it["rougeL"] for it in non_trunc])
        e["hallucination_rate_excluding_degenerate"] = mean_std([it["hallucination_rate"] for it in non_trunc])
        agg["splits"][split] = e
    agg["headline"] = {k: mean_std([it[k] for it in per_item if it["split"] in HEADLINE]) for k in ("rougeL", "hallucination_rate", "negation_flip_rate", "numerical_consistency", "clinical_coverage")}
    (out / "metrics.json").write_text(json.dumps(agg, indent=2), encoding="utf-8")
    write_tables(agg, out / "metrics.md", label)
    write_examples(per_item, out / "examples.md", label, files)
    try:
        plot_run(agg, per_item, out / "figures", label)
    except Exception as e:  # noqa: BLE001
        print("plots skipped:", e)
    print(f"[{label}] -> {out}  ({time.time() - t0:.0f} s)")
    return agg


def write_tables(agg: dict, path: Path, label: str) -> None:
    md = [f"# Evaluation — {label}", "", f"Run: `{agg['run']}`  ·  generated {agg['generated']}  ·  decoding: `{json.dumps(agg['decoding'])}`", ""]
    if agg.get("training"):
        md += [f"Training: `{json.dumps(agg['training'])}`", ""]
    md += ["## Standard metrics (mean over items, ×100; ROUGE F1 with stemming; BERTScore F1 rescaled)", "",
           "| split | n | ROUGE-1 | ROUGE-2 | ROUGE-L | ROUGE-Lsum | BERTScore | len ratio | truncated | degenerate | ROUGE-L excl. degenerate |",
           "|---|---|---|---|---|---|---|---|---|---|---|"]
    for s, e in agg["splits"].items():
        md.append(f"| {s} | {e['n']} | {fmt(e['rouge1']['mean'])} | {fmt(e['rouge2']['mean'])} | **{fmt(e['rougeL']['mean'])}** | {fmt(e['rougeLsum']['mean'])} | "
                  f"{fmt(e['bertscore_f1']['mean'])} | {fmt(e['length_ratio']['mean'], 2, 1)} | {e['truncated']} | {e['degenerate']} | {fmt(e['rougeL_excluding_degenerate']['mean'])} (n={e['rougeL_excluding_degenerate']['n']}) |")
    md += ["", "## Factuality (mean of per-item rates ×100; micro = pooled over all entities of the split)", "",
           "| split | n | hallucination ↓ | halluc. strict ↓ | micro halluc. ↓ | negation-flip ↓ | micro neg-flip ↓ | numerical consistency ↑ | micro num. ↑ | clinical coverage ↑ | coverage (important) ↑ | micro coverage ↑ |",
           "|---|---|---|---|---|---|---|---|---|---|---|---|"]
    for s, e in agg["splits"].items():
        md.append(f"| {s} | {e['n']} | **{fmt(e['hallucination_rate']['mean'])}** | {fmt(e['hallucination_rate_strict']['mean'])} | {fmt(e['micro_hallucination_rate'])} | "
                  f"**{fmt(e['negation_flip_rate']['mean'])}** | {fmt(e['micro_negation_flip_rate'])} | **{fmt(e['numerical_consistency']['mean'])}** | {fmt(e['micro_numerical_consistency'])} | "
                  f"**{fmt(e['clinical_coverage']['mean'])}** | {fmt(e['clinical_coverage_important']['mean'])} | {fmt(e['micro_clinical_coverage'])} |")
    md += ["", "## Coverage by category (×100, mean per item)", "", "| split | symptom | medical history | diagnosis | medication | investigation |", "|---|---|---|---|---|---|"]
    for s, e in agg["splits"].items():
        md.append(f"| {s} | {fmt(e['coverage_symptom']['mean'])} | {fmt(e['coverage_medical_history']['mean'])} | {fmt(e['coverage_diagnosis']['mean'])} | {fmt(e['coverage_medication']['mean'])} | {fmt(e['coverage_investigation']['mean'])} |")
    md += ["", "## Error counts (items affected / total occurrences)", "",
           "| split | n | hallucinated entities | incorrect diagnosis | missing diagnosis | incorrect medication | missing medication | dosage mismatch | negation flips | numerical errors |",
           "|---|---|---|---|---|---|---|---|---|---|"]
    for s, e in agg["splits"].items():
        md.append(f"| {s} | {e['n']} | {e['total_unsupported_entities']} / {e['total_pred_entities']} pred. entities | {e['items_with_incorrect_diagnosis']} / {e['total_incorrect_diagnoses']} | "
                  f"{e['items_with_missing_diagnosis']} | {e['items_with_incorrect_medication']} / {e['total_incorrect_medications']} | {e['items_with_missing_medication']} | "
                  f"{e['items_with_dosage_mismatch']} / {e['total_dosage_mismatches']} | {e['items_with_negation_flip']} / {e['total_negation_flips']} | {e['items_with_numerical_error']} / {e['total_unsupported_numbers']} |")
    h = agg["headline"]
    md += ["", "## Headline (five official test splits pooled, item mean ×100)", "",
           f"ROUGE-L **{fmt(h['rougeL']['mean'])}** · hallucination rate **{fmt(h['hallucination_rate']['mean'])}** · negation-flip rate **{fmt(h['negation_flip_rate']['mean'])}** · "
           f"numerical consistency **{fmt(h['numerical_consistency']['mean'])}** · clinical coverage **{fmt(h['clinical_coverage']['mean'])}** (n = {h['rougeL']['n']})", ""]
    path.write_text("\n".join(md), encoding="utf-8")


def _clip(t: str, n: int = 900) -> str:
    t = t.replace("\r", "")
    return t if len(t) <= n else t[:n] + " …"


def write_examples(per_item: list[dict], path: Path, label: str, files: dict[str, Path]) -> None:
    texts: dict[str, dict] = {}
    for split, p in files.items():
        for r in load_jsonl(p):
            texts[(split, r["id"])] = r
    md = [f"# Example errors — {label}", "", "Each block shows the transcript excerpt, the reference note, the generated note and the flags raised by the factuality checker.", ""]

    def block(title: str, it: dict, why: str) -> list[str]:
        r = texts[(it["split"], it["id"])]
        lines = [f"## {title}: `{it['id']}`", "", f"*{why}*", "",
                 f"ROUGE-L {it['rougeL'] * 100:.1f} · length ratio {it['length_ratio']:.2f} · truncated {it['truncated']} · degenerate {it['degenerate']} · "
                 f"hallucination {fmt(it['hallucination_rate'])} · negation-flip {fmt(it['negation_flip_rate'])} · numerical consistency {fmt(it['numerical_consistency'])} · coverage {fmt(it['clinical_coverage'])}", "",
                 "**Transcript (excerpt)**", "", "```", _clip(r["source_dialogue"], 700), "```", "",
                 "**Reference note**", "", "```", _clip(r["reference_summary"], 900), "```", "",
                 "**Generated note**", "", "```", _clip(r["prediction"], 1100), "```", "",
                 f"- unsupported entities (vs. transcript): {', '.join(it['unsupported_vs_source'][:20]) or '—'}",
                 f"- incorrect diagnosis: {', '.join(it['incorrect_diagnosis']) or '—'}  ·  missing diagnosis: {', '.join(it['missing_diagnosis']) or '—'}",
                 f"- incorrect medication: {', '.join(it['incorrect_medication']) or '—'}  ·  missing medication: {', '.join(it['missing_medication']) or '—'}",
                 f"- dosage mismatch: {json.dumps(it['dosage_mismatch']) if it['dosage_mismatch'] else '—'}",
                 f"- negation flips (vs. reference): {', '.join(it['negation_flips']) or '—'}",
                 f"- unsupported numbers: {', '.join(it['unsupported_numbers'][:15]) or '—'}",
                 f"- missing information: {json.dumps({k: v[:6] for k, v in it['missing_by_category'].items() if v})}", ""]
        return lines

    for split in [s for s in SPLIT_ORDER if any(it["split"] == s for it in per_item)]:
        items = [it for it in per_item if it["split"] == split]
        md.append(f"# Split: {split}\n")
        ranked = sorted(items, key=lambda it: it["rougeL"])
        md += block("Best ROUGE-L", ranked[-1], "highest ROUGE-L in the split")
        md += block("Worst ROUGE-L", ranked[0], "lowest ROUGE-L in the split")
        picks = [("Hallucination example", lambda it: len(it["unsupported_vs_source"]) > 0 and not it["degenerate"], lambda it: -len(it["unsupported_vs_source"])),
                 ("Incorrect diagnosis example", lambda it: it["incorrect_diagnosis"], lambda it: -len(it["incorrect_diagnosis"])),
                 ("Incorrect medication / dosage example", lambda it: it["incorrect_medication"] or it["dosage_mismatch"], lambda it: -(len(it["incorrect_medication"]) + len(it["dosage_mismatch"]))),
                 ("Negation error example", lambda it: it["negation_flips"], lambda it: -len(it["negation_flips"])),
                 ("Numerical error example", lambda it: it["unsupported_numbers"], lambda it: -len(it["unsupported_numbers"])),
                 ("Missing information example", lambda it: it["clinical_coverage"] is not None and it["n_ref_entities"] >= 5, lambda it: it["clinical_coverage"]),
                 ("Degenerate output example", lambda it: it["degenerate"], lambda it: -it["longest_comma_list"])]
        for title, cond, key in picks:
            cand = sorted([it for it in items if cond(it)], key=key)
            if cand:
                md += block(title, cand[0], title.lower())
    path.write_text("\n".join(md), encoding="utf-8")


def plot_run(agg: dict, per_item: list[dict], fig_dir: Path, label: str) -> None:
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    import numpy as np
    splits = list(agg["splits"])
    short = [s.replace("aci_bench_test_", "ACI ").replace("mts_dialog_test_", "MTS ").replace("dialogue_soap_test", "SOAP test").replace("zeroshot_base/val_check", "zero-shot val").replace("val_check", "adapter val") for s in splits]
    x = np.arange(len(splits))
    # 1. ROUGE
    fig, ax = plt.subplots(figsize=(10, 4))
    for i, k in enumerate(("rouge1", "rouge2", "rougeL")):
        ax.bar(x + (i - 1) * 0.27, [agg["splits"][s][k]["mean"] * 100 for s in splits], 0.27, label=k.upper().replace("ROUGE", "ROUGE-"))
    ax.set_xticks(x, short, rotation=20, ha="right", fontsize=8); ax.set_ylabel("F1 × 100"); ax.set_title(f"ROUGE per split — {label}"); ax.legend(); fig.tight_layout()
    fig.savefig(fig_dir / "rouge_per_split.png", dpi=150); plt.close(fig)
    # 2. factuality
    fig, ax = plt.subplots(figsize=(10, 4))
    keys = [("hallucination_rate", "hallucination ↓"), ("negation_flip_rate", "negation flip ↓"), ("numerical_consistency", "numerical consistency ↑"), ("clinical_coverage", "clinical coverage ↑")]
    for i, (k, lab) in enumerate(keys):
        vals = [(agg["splits"][s][k]["mean"] or 0) * 100 for s in splits]
        ax.bar(x + (i - 1.5) * 0.2, vals, 0.2, label=lab)
    ax.set_xticks(x, short, rotation=20, ha="right", fontsize=8); ax.set_ylabel("rate × 100"); ax.set_title(f"Factuality per split — {label}"); ax.legend(fontsize=8); fig.tight_layout()
    fig.savefig(fig_dir / "factuality_per_split.png", dpi=150); plt.close(fig)
    # 3. length ratio hist
    fig, ax = plt.subplots(figsize=(8, 4))
    for ds in ("aci_bench", "mts_dialog", "dialogue_soap"):
        v = [min(it["length_ratio"], 5) for it in per_item if it["dataset"] == ds and it["split"] in HEADLINE + ["dialogue_soap_test"]]
        if v:
            ax.hist(v, bins=40, alpha=0.5, label=f"{ds} (n={len(v)})")
    ax.axvline(1.0, color="k", ls="--", lw=1); ax.set_xlabel("generated / reference length (words, clipped at 5)"); ax.set_ylabel("items"); ax.legend(); ax.set_title(f"Length ratio — {label}"); fig.tight_layout()
    fig.savefig(fig_dir / "length_ratio_hist.png", dpi=150); plt.close(fig)
    # 4. error type counts (items affected) on the headline splits
    fig, ax = plt.subplots(figsize=(8, 4))
    cats = [("items_with_incorrect_diagnosis", "incorrect dx"), ("items_with_missing_diagnosis", "missing dx"), ("items_with_incorrect_medication", "incorrect med"),
            ("items_with_missing_medication", "missing med"), ("items_with_dosage_mismatch", "dosage mismatch"), ("items_with_negation_flip", "negation flip"),
            ("items_with_numerical_error", "numerical error"), ("degenerate", "degenerate output")]
    n_head = sum(agg["splits"][s]["n"] for s in splits if s in HEADLINE)
    vals = [100 * sum(agg["splits"][s][k] for s in splits if s in HEADLINE) / max(1, n_head) for k, _ in cats]
    ax.barh([lab for _, lab in cats], vals); ax.set_xlabel(f"% of headline test items affected (n={n_head})"); ax.set_title(f"Error types — {label}"); fig.tight_layout()
    fig.savefig(fig_dir / "error_types.png", dpi=150); plt.close(fig)
    # 5. ROUGE-L vs hallucination scatter
    fig, ax = plt.subplots(figsize=(6, 4.5))
    for ds, mk in (("aci_bench", "o"), ("mts_dialog", "^"), ("dialogue_soap", "s")):
        pts = [(it["rougeL"] * 100, it["hallucination_rate"] * 100) for it in per_item if it["dataset"] == ds and it["hallucination_rate"] is not None and it["split"] != "zeroshot_base/val_check"]
        if pts:
            ax.scatter(*zip(*pts), s=10, alpha=0.5, marker=mk, label=ds)
    ax.set_xlabel("ROUGE-L × 100"); ax.set_ylabel("hallucination rate × 100"); ax.legend(); ax.set_title(f"ROUGE-L vs hallucination — {label}"); fig.tight_layout()
    fig.savefig(fig_dir / "rougeL_vs_hallucination.png", dpi=150); plt.close(fig)


def compare() -> None:
    runs = {}
    for p in sorted(OUT.glob("*/metrics.json")):
        runs[p.parent.name] = json.loads(p.read_text(encoding="utf-8"))
    if not runs:
        sys.exit("nothing to compare")
    md = ["# Baseline comparison across runs / decoding configurations", "", "All numbers ×100, item means. Runs:", ""]
    for lab, a in runs.items():
        md.append(f"- **{lab}**: `{a['run']}` · decoding `{json.dumps(a['decoding'])}`")
    md.append("")
    keys = [("rougeL", "ROUGE-L ↑"), ("bertscore_f1", "BERTScore ↑"), ("hallucination_rate", "hallucination ↓"), ("negation_flip_rate", "negation-flip ↓"),
            ("numerical_consistency", "numerical consistency ↑"), ("clinical_coverage", "clinical coverage ↑"), ("length_ratio", "length ratio")]
    for k, title in keys:
        md += [f"## {title}", "", "| split | " + " | ".join(runs) + " |", "|---|" + "---|" * len(runs)]
        for s in SPLIT_ORDER:
            if not any(s in a["splits"] for a in runs.values()):
                continue
            cells = []
            for a in runs.values():
                e = a["splits"].get(s)
                cells.append("—" if e is None else (fmt(e[k]["mean"], 2, 1) if k == "length_ratio" else fmt(e[k]["mean"])))
            md.append(f"| {s} | " + " | ".join(cells) + " |")
        md.append("")
    md += ["## Truncated / degenerate outputs", "", "| split | " + " | ".join(f"{r} trunc / degen" for r in runs) + " |", "|---|" + "---|" * len(runs)]
    for s in SPLIT_ORDER:
        if not any(s in a["splits"] for a in runs.values()):
            continue
        md.append(f"| {s} | " + " | ".join("—" if s not in a["splits"] else f"{a['splits'][s]['truncated']} / {a['splits'][s]['degenerate']} (n={a['splits'][s]['n']})" for a in runs.values()) + " |")
    (OUT / "comparison.md").write_text("\n".join(md), encoding="utf-8")
    try:
        import matplotlib
        matplotlib.use("Agg")
        import matplotlib.pyplot as plt
        import numpy as np
        (OUT / "figures").mkdir(exist_ok=True)
        for k, title, fname in (("rougeL", "ROUGE-L × 100", "compare_rougeL.png"), ("hallucination_rate", "hallucination rate × 100", "compare_hallucination.png"),
                                ("clinical_coverage", "clinical coverage × 100", "compare_coverage.png"), ("negation_flip_rate", "negation-flip rate × 100", "compare_negflip.png")):
            splits = [s for s in SPLIT_ORDER[:6] if any(s in a["splits"] for a in runs.values())]
            x = np.arange(len(splits)); w = 0.8 / len(runs)
            fig, ax = plt.subplots(figsize=(10, 4))
            for i, (lab, a) in enumerate(runs.items()):
                ax.bar(x + (i - (len(runs) - 1) / 2) * w, [((a["splits"].get(s) or {}).get(k, {}).get("mean") or 0) * 100 for s in splits], w, label=lab)
            ax.set_xticks(x, [s.replace("aci_bench_test_", "ACI ").replace("mts_dialog_test_", "MTS ").replace("dialogue_soap_test", "SOAP") for s in splits], rotation=15, ha="right", fontsize=8)
            ax.set_ylabel(title); ax.set_title(title + " by run"); ax.legend(fontsize=8); fig.tight_layout(); fig.savefig(OUT / "figures" / fname, dpi=150); plt.close(fig)
    except Exception as e:  # noqa: BLE001
        print("comparison plots skipped:", e)
    print(f"-> {OUT / 'comparison.md'}")


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--run")
    ap.add_argument("--label")
    ap.add_argument("--bertscore", action="store_true")
    ap.add_argument("--bertscore-cache", default=None, help="per_item.jsonl of an earlier evaluation of the same predictions; its BERTScore values are reused")
    ap.add_argument("--limit", type=int, default=None, help="evaluate only the first N items per split (smoke test)")
    ap.add_argument("--compare", action="store_true")
    ap.add_argument("--system", default="baseline_qlora", help="predictions/<system>/ folder to evaluate")
    ap.add_argument("--out", default=None, help="report root (default reports/eval_baseline)")
    a = ap.parse_args()
    if a.out:
        global OUT
        OUT = Path(a.out)
    if a.run:
        evaluate_run(Path(a.run), a.label or Path(a.run).name, a.bertscore, a.limit, Path(a.bertscore_cache) if a.bertscore_cache else None,
                     a.system)
    if a.compare or not a.run:
        compare()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
