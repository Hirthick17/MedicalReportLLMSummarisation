#!/usr/bin/env python
"""ROUGE exactly as the MEDIQA-Chat 2023 evaluation script computes it, for comparison with published results.

The official script (abachaa/MEDIQA-Chat-2023/scripts/evaluate_summarization.py) calls Hugging Face
evaluate.load('rouge') with use_aggregator=False and averages per item. That is rouge_score with
use_stemmer=False; rougeLsum splits sentences on newlines.

    python scripts/official_rouge.py <predictions_dir> [<predictions_dir> ...]
        each dir holds <split>.jsonl files with `prediction` and `reference_summary`
-> prints a table and writes official_rouge.json next to each dir.
"""
import json
import statistics
import sys
from pathlib import Path

from rouge_score import rouge_scorer

TYPES = ["rouge1", "rouge2", "rougeL", "rougeLsum"]
SCORER = rouge_scorer.RougeScorer(TYPES, use_stemmer=False)


def score_file(path: Path) -> dict:
    rows = [json.loads(l) for l in path.open(encoding="utf-8") if l.strip()]
    per = [SCORER.score(r["reference_summary"], r["prediction"]) for r in rows]
    return {"n": len(rows), **{t: statistics.fmean(p[t].fmeasure for p in per) for t in TYPES}}


def main():
    for d in map(Path, sys.argv[1:]):
        res = {f.stem: score_file(f) for f in sorted(d.glob("*.jsonl"))}
        mts = [res[s] for s in ("mts_dialog_test_chat_2023", "mts_dialog_test_sum_2023") if s in res]
        if len(mts) == 2:   # pooled 400-item MTS-Dialog test (Lyu et al. setting)
            n = mts[0]["n"] + mts[1]["n"]
            res["mts_dialog_test_all"] = {"n": n, **{t: (mts[0][t] * mts[0]["n"] + mts[1][t] * mts[1]["n"]) / n for t in TYPES}}
        (d / "official_rouge.json").write_text(json.dumps(res, indent=2), encoding="utf-8")
        print(f"\n{d}")
        for k, v in res.items():
            print(f"  {k:28s} n={v['n']:3d}  " + "  ".join(f"{t}={v[t]:.4f}" for t in TYPES))


if __name__ == "__main__":
    main()
