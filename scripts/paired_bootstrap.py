#!/usr/bin/env python
"""Paired bootstrap 95% confidence intervals for differences between systems (same test items).

    python scripts/paired_bootstrap.py
-> reports/eval_review3/significance.json / .md, research_paper/review3_paper/tables/significance.tex
"""
import json
import random
import statistics
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
EVAL = ROOT / "reports" / "eval_review3"
PAIRS = [("zeroshot", "sft1024", "SFT $-$ A"), ("sft1024", "sftfact", "SFT+F $-$ SFT"), ("zeroshot", "factcond", "B $-$ A"), ("factcond", "verified", "C $-$ B")]
METRICS = [("hallucination_rate", "Halluc."), ("negation_flip_rate", "Neg.\\ flip"), ("numerical_consistency", "Num.\\ cons."),
           ("clinical_coverage", "Coverage"), ("rougeL", "R-L")]
DATASETS = {"aci_bench": "ACI-Bench", "mts_dialog": "MTS-Dialog"}
B = 10000


def per_item(label):
    rows = [json.loads(l) for l in (EVAL / label / "per_item.jsonl").open(encoding="utf-8")]
    return {(r["split"], r["id"]): r for r in rows if r["split"].startswith(("aci_bench_test", "mts_dialog_test"))}


def main():
    rng = random.Random(42)
    data = {k: per_item(k) for k in ("sft1024", "sftfact", "zeroshot", "factcond", "verified")}
    out, tex = {}, []
    for ds, ds_name in DATASETS.items():
        for base, other, name in PAIRS:
            row = []
            for m, _ in METRICS:
                keys = [k for k in data[base] if k[0].startswith(ds) and k in data[other]
                        and data[base][k].get(m) is not None and data[other][k].get(m) is not None]
                d = [data[other][k][m] - data[base][k][m] for k in keys]
                boots = sorted(statistics.fmean(rng.choices(d, k=len(d))) for _ in range(B))
                lo, hi = boots[int(0.025 * B)], boots[int(0.975 * B)]
                res = {"n": len(d), "diff": statistics.fmean(d), "ci95": [lo, hi], "significant": lo > 0 or hi < 0}
                out.setdefault(ds, {}).setdefault(name, {})[m] = res
                row.append(f"{100 * res['diff']:+.1f}" + ("$^{*}$" if res["significant"] else ""))
            tex.append(f"{ds_name} & {name} & " + " & ".join(row) + "\\\\")
        tex.append("\\midrule")
    (EVAL / "significance.json").write_text(json.dumps(out, indent=2), encoding="utf-8")
    md = ["# Paired bootstrap (10,000 resamples), difference in percentage points, 95% CI", ""]
    for ds, comps in out.items():
        for name, ms in comps.items():
            md.append(f"- **{ds} {name.replace('$-$', '-')}**: " + "; ".join(
                f"{m} {100 * r['diff']:+.1f} [{100 * r['ci95'][0]:+.1f}, {100 * r['ci95'][1]:+.1f}] (n={r['n']}){' *' if r['significant'] else ''}"
                for m, r in ms.items()))
    (EVAL / "significance.md").write_text("\n".join(md) + "\n", encoding="utf-8")
    (ROOT / "research_paper" / "review3_paper" / "tables" / "significance.tex").write_text("\n".join([
        "\\begin{table}[t]", "\\centering",
        "\\caption{Paired differences in percentage points (per-item means). $^{*}$: 95\\% paired bootstrap interval "
        "excludes 0 (10{,}000 resamples).}\\label{tab:sig}",
        "\\scriptsize", "\\setlength{\\tabcolsep}{2.5pt}", "\\resizebox{\\columnwidth}{!}{\\begin{tabular}{@{}llrrrrr@{}}", "\\toprule",
        "Dataset & Comparison & " + " & ".join(n for _, n in METRICS) + "\\\\", "\\midrule", *tex[:-1],
        "\\bottomrule", "\\end{tabular}}", "\\end{table}"]) + "\n", encoding="utf-8")
    print("\n".join(md))


if __name__ == "__main__":
    main()
