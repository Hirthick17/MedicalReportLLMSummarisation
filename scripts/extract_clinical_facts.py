#!/usr/bin/env python
"""
Run the rule-based Clinical Fact Extractor over every processed split (Person 1, Review 2).

For each record in data/processed/<dataset>/<split>.jsonl the extractor is applied to the source
dialogue (kind=dialogue) and to the reference note (kind=note; MTS-Dialog notes get the section from
metadata.section_header). Output, one line per record:

  data/processed/facts/<dataset>_<split>.jsonl
    {"id", "dataset", "split",
     "source_facts": [Fact...], "target_facts": [Fact...],
     "source_summary": {...counts...}, "target_summary": {...counts...}}

plus
  data/interim/cfe_stats.json          corpus-level statistics (facts / doc, negation rate, category mix,
                                       source->reference fact retention, run time)
  reports/data_audit/cfe_stats.md      the same as a table
  reports/data_audit/cfe_samples.md    N randomly chosen records rendered fact-by-fact for manual checking

Usage:
  python scripts/extract_clinical_facts.py                 # all splits
  python scripts/extract_clinical_facts.py --only aci_bench
  python scripts/extract_clinical_facts.py --samples 8 --seed 7
"""

from __future__ import annotations

import argparse
import collections
import json
import random
import sys
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

from src.cfe import CATEGORIES, extract_facts, facts_to_dicts, summarize  # noqa: E402
from src.cfe.lexicon import MTS_SECTION_MAP  # noqa: E402

PROCESSED = ROOT / "data" / "processed"
FACTS = PROCESSED / "facts"
INTERIM = ROOT / "data" / "interim"
REPORT = ROOT / "reports" / "data_audit"
SPLITS = {
    "aci_bench": ["train", "validation", "test_taskB_1", "test_taskC_2", "test_taskC_3"],
    "mts_dialog": ["train", "validation", "test_chat_2023", "test_sum_2023"],
    "dialogue_soap": ["train", "validation", "test"],
}


def canon_set(facts, cats=None):
    return {(f["category"], f["canonical"], f["polarity"]) for f in facts if cats is None or f["category"] in cats}


def render(rec: dict, facts: list[dict], label: str, clip: int = 700) -> list[str]:
    txt = rec["source_dialogue"] if label == "source" else rec["target_summary"]
    lines = [f"**{label}** ({len(txt.split())} words, {len(facts)} facts)", "", "```", txt[:clip] + ("…" if len(txt) > clip else ""), "```", "",
             "| category | text | canonical | polarity | certainty | temporality | who | section/speaker | value |", "|---|---|---|---|---|---|---|---|---|"]
    for f in facts:
        val = " ".join(str(x) for x in (f.get("value"), f.get("unit"), f.get("frequency"), f.get("route")) if x)
        lines.append(f"| {f['category']} | {f['text']} | {f['canonical']} | {f['polarity']} | {f['certainty']} | {f['temporality']} | {f['experiencer']} | {f.get('section') or f.get('speaker') or ''} | {val} |")
    return lines + [""]


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--only", default="")
    ap.add_argument("--samples", type=int, default=6)
    ap.add_argument("--seed", type=int, default=42)
    a = ap.parse_args()
    only = {k.strip() for k in a.only.split(",") if k.strip()}
    FACTS.mkdir(parents=True, exist_ok=True)
    INTERIM.mkdir(parents=True, exist_ok=True)
    REPORT.mkdir(parents=True, exist_ok=True)
    rng = random.Random(a.seed)

    stats: dict = {"generated": time.strftime("%Y-%m-%d %H:%M"), "categories": CATEGORIES, "splits": {}}
    samples_md = ["# CFE samples for manual validation", "", f"{a.samples} random records per corpus (seed {a.seed}). Each fact row is one assertion; "
                  "check polarity (negation), category and the value columns. Mark errors in the margin.", ""]
    t_all = time.time()
    for ds, splits in SPLITS.items():
        if only and ds not in only:
            continue
        corpus_samples = []
        for sp in splits:
            path = PROCESSED / ds / f"{sp}.jsonl"
            if not path.exists():
                continue
            recs = [json.loads(l) for l in path.open(encoding="utf-8") if l.strip()]
            t0 = time.time()
            agg = {"n": len(recs), "src_facts": 0, "tgt_facts": 0, "src_neg": 0, "tgt_neg": 0, "src_unc": 0,
                   "src_cat": collections.Counter(), "tgt_cat": collections.Counter(), "tgt_neg_cat": collections.Counter(),
                   "retained": 0, "tgt_total_for_retention": 0, "tgt_not_in_src": 0, "dosage_with_drug": 0, "dosage_total": 0,
                   "docs_no_src_facts": 0, "docs_no_tgt_facts": 0}
            with (FACTS / f"{ds}_{sp}.jsonl").open("w", encoding="utf-8") as out:
                for r in recs:
                    section = MTS_SECTION_MAP.get(r.get("metadata", {}).get("section_header", ""), None) if ds == "mts_dialog" else None
                    sf = extract_facts(r["source_dialogue"], kind="dialogue")
                    tf = extract_facts(r["target_summary"], kind="note", default_section=section)
                    sfd, tfd = facts_to_dicts(sf), facts_to_dicts(tf)
                    ss, ts = summarize(sf), summarize(tf)
                    out.write(json.dumps({"id": r["id"], "dataset": ds, "split": sp, "source_facts": sfd, "target_facts": tfd,
                                          "source_summary": ss, "target_summary": ts}, ensure_ascii=False) + "\n")
                    agg["src_facts"] += ss["n_facts"]; agg["tgt_facts"] += ts["n_facts"]
                    agg["src_neg"] += ss["n_negated"]; agg["tgt_neg"] += ts["n_negated"]; agg["src_unc"] += ss["n_uncertain"]
                    agg["src_cat"].update(ss["by_category"]); agg["tgt_cat"].update(ts["by_category"]); agg["tgt_neg_cat"].update(ts["negated_by_category"])
                    agg["docs_no_src_facts"] += ss["n_facts"] == 0; agg["docs_no_tgt_facts"] += ts["n_facts"] == 0
                    # how many reference-note facts (entity level, polarity-agnostic) are also found in the dialogue?
                    core = ("symptom", "medical_history", "diagnosis", "medication", "investigation")
                    s_ent = {f["canonical"] for f in sfd if f["category"] in core}
                    t_ent = {f["canonical"] for f in tfd if f["category"] in core}
                    agg["retained"] += len(t_ent & s_ent); agg["tgt_total_for_retention"] += len(t_ent); agg["tgt_not_in_src"] += len(t_ent - s_ent)
                    agg["dosage_total"] += sum(1 for f in tfd if f["category"] == "dosage")
                    agg["dosage_with_drug"] += sum(1 for f in tfd if f["category"] == "dosage" and f.get("drug"))
                    if sp in ("validation", "test", "test_taskB_1", "test_chat_2023"):
                        corpus_samples.append((r, sfd, tfd))
            dt = time.time() - t0
            n = max(1, len(recs))
            entry = {
                "n": len(recs), "seconds": round(dt, 1), "ms_per_record": round(1000 * dt / n, 1),
                "source_facts_per_doc": round(agg["src_facts"] / n, 1), "target_facts_per_doc": round(agg["tgt_facts"] / n, 1),
                "source_negation_rate": round(agg["src_neg"] / max(1, agg["src_facts"]), 3), "target_negation_rate": round(agg["tgt_neg"] / max(1, agg["tgt_facts"]), 3),
                "source_uncertain_rate": round(agg["src_unc"] / max(1, agg["src_facts"]), 3),
                "source_by_category": dict(agg["src_cat"]), "target_by_category": dict(agg["tgt_cat"]), "target_negated_by_category": dict(agg["tgt_neg_cat"]),
                "reference_entities_found_in_source": round(agg["retained"] / max(1, agg["tgt_total_for_retention"]), 3),
                "reference_entities_not_in_source": agg["tgt_not_in_src"],
                "dosage_facts_linked_to_drug": round(agg["dosage_with_drug"] / max(1, agg["dosage_total"]), 3),
                "docs_without_source_facts": agg["docs_no_src_facts"], "docs_without_target_facts": agg["docs_no_tgt_facts"],
            }
            stats["splits"][f"{ds}/{sp}"] = entry
            print(f"  {ds:14s} {sp:16s} n={len(recs):5d} src {entry['source_facts_per_doc']:5.1f}/doc  tgt {entry['target_facts_per_doc']:5.1f}/doc  "
                  f"neg(tgt) {entry['target_negation_rate']:.2f}  ref∩src {entry['reference_entities_found_in_source']:.2f}  {entry['ms_per_record']} ms/rec")
        rng.shuffle(corpus_samples)
        for r, sfd, tfd in corpus_samples[: a.samples]:
            samples_md += [f"## {r['id']}", ""] + render(r, sfd, "source") + render(r, tfd, "reference")

    stats["total_seconds"] = round(time.time() - t_all, 1)
    (INTERIM / "cfe_stats.json").write_text(json.dumps(stats, indent=2), encoding="utf-8")
    md = ["# Clinical fact extraction — corpus statistics", "", f"Generated {stats['generated']}; total {stats['total_seconds']} s on CPU.", "",
          "| split | n | src facts/doc | ref facts/doc | ref negation rate | src uncertain rate | ref entities found in src | dosage→drug link | ms/rec |",
          "|---|---|---|---|---|---|---|---|---|"]
    for k, e in stats["splits"].items():
        md.append(f"| {k} | {e['n']} | {e['source_facts_per_doc']} | {e['target_facts_per_doc']} | {e['target_negation_rate']} | {e['source_uncertain_rate']} | "
                  f"{e['reference_entities_found_in_source']} | {e['dosage_facts_linked_to_drug']} | {e['ms_per_record']} |")
    md += ["", "## Category mix in the reference notes (all splits)", "", "| split | " + " | ".join(CATEGORIES) + " |", "|---|" + "---|" * len(CATEGORIES)]
    for k, e in stats["splits"].items():
        md.append(f"| {k} | " + " | ".join(str(e["target_by_category"].get(c, 0)) for c in CATEGORIES) + " |")
    (REPORT / "cfe_stats.md").write_text("\n".join(md), encoding="utf-8")
    (REPORT / "cfe_samples.md").write_text("\n".join(samples_md), encoding="utf-8")
    print(f"\nfacts -> {FACTS}\nstats -> {INTERIM / 'cfe_stats.json'}, {REPORT / 'cfe_stats.md'}, samples -> {REPORT / 'cfe_samples.md'}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
