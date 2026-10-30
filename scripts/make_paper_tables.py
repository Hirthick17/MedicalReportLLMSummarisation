#!/usr/bin/env python
"""Generate the result tables and figure of the Review 3 paper from the evaluation outputs.

    python scripts/make_paper_tables.py

Reads   <pred dir>/official_rouge.json        (scripts/official_rouge.py, MEDIQA-Chat ROUGE)
        reports/eval_review3/<label>/per_item.jsonl   (src/eval/run_eval.py, factuality + BERTScore)
        <C pred dir>/verifier_stats.json       (scripts/run_verifier.py)
Writes  research_paper/review3_paper/tables/{aci,mts,factuality,verifier}.tex, figures/factuality.png,
        reports/eval_review3/summary.json and summary.md (the numbers the paper text quotes).
Published numbers are copied from research_paper/published_results.md (sources and pages there).
"""
import json
import statistics
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUTS = ROOT.parent / "medsum-fact" / "outputs"
PRED = {
    "sft1024": OUTS / "kaggle_review3_sft/outputs/review3_sft/predictions/sft_1024",
    "sftfact": OUTS / "kaggle_review3_sft/outputs/review3_sft/predictions/sft_factcond",
    "zeroshot": OUTS / "kaggle_review3/outputs/review3/predictions/zeroshot_base",
    "factcond": OUTS / "kaggle_review3/outputs/review3/predictions/factcond_base",
    "verified": OUTS / "kaggle_review3/outputs/review3/predictions/factcond_verified",
}
NAME = {"sft1024": "SFT (QLoRA)", "sftfact": "SFT + Fact table", "zeroshot": "A. Zero-shot", "factcond": "B. + Fact table", "verified": "C. + Verifier (FaCTS)"}
EVAL = ROOT / "reports" / "eval_review3"
PAPER = ROOT / "research_paper" / "review3_paper"

ACI_PUB = [  # MEDIQA-Chat 2023 overview, Table 7 (ACI-Bench test 1, full notes)
    ("WangLab~\\cite{giorgi2023wanglab}", "GPT-4 ICL", 0.6141, 0.3288, 0.3815, 0.5515),
    ("Cadence~\\cite{sharma2023cadence}", "BART FT", 0.5297, 0.2500, 0.2979, 0.4663),
    ("iuteam1~\\cite{abacha2023overview}", "LSG-BART FT", 0.5268, 0.2622, 0.3060, 0.4976),
    ("GersteinLab~\\cite{abacha2023overview}", "GPT-3", 0.5008, 0.2506, 0.3282, 0.4668),
    ("Calvados~\\cite{abacha2023overview}", "LongT5 FT", 0.4307, 0.2017, 0.2394, 0.3861),
    ("Yim et al.~\\cite{yim2023aci}", "BART+SAMSum, by division", 0.5346, 0.2508, None, None),   # Table 6; R-L not comparable
    ("Organisers~\\cite{abacha2023overview}", "GPT-4 0-shot", 0.5176, 0.2258, 0.3029, 0.4256),
    ("Organisers~\\cite{abacha2023overview}", "ChatGPT 0-shot", 0.4744, 0.1901, 0.2711, 0.3902),
]
MTS_PUB = [  # same overview, Table 6 (MTS-Dialog test 1, 200 items)
    ("WangLab~\\cite{giorgi2023wanglab}", "GPT-4 ICL", 0.4466, 0.2282, 0.3837),
    ("Cadence~\\cite{sharma2023cadence}", "BART FT", 0.4303, 0.2078, 0.3642),
    ("GersteinLab~\\cite{abacha2023overview}", "FT + ICL", 0.4011, 0.2147, 0.3322),
    ("Calvados~\\cite{abacha2023overview}", "LongT5 FT", 0.3946, 0.1864, 0.3321),
    ("Care4Lang~\\cite{abacha2023overview}", "LM FT", 0.3581, 0.1650, 0.2890),
    ("Organisers~\\cite{abacha2023overview}", "GPT-4 0-shot", 0.3071, 0.1283, 0.2365),
    ("Organisers~\\cite{abacha2023overview}", "ChatGPT 0-shot", 0.3032, 0.1209, 0.2420),
]
MTS400_PUB = [  # Lyu et al., Table 4 (MTS-Dialog, 400 test items)
    ("Lyu et al.~\\cite{lyu2024}", "GatorTronGPT-20B PT", 0.3628, 0.1549, 0.3472),
    ("Lyu et al.~\\cite{lyu2024}", "T5-Large FT", 0.3425, 0.1465, 0.3368),
]
DATASETS = {"aci_bench": "ACI-Bench (120)", "mts_dialog": "MTS-Dialog (400)"}


def load_jsonl(p):
    return [json.loads(l) for l in Path(p).open(encoding="utf-8") if l.strip()]


def mean(xs):
    xs = [x for x in xs if x is not None]
    return statistics.fmean(xs) if xs else None


def f(x, nd=3):
    return "--" if x is None else f"{x:.{nd}f}"


def bold_max(vals):
    best = max(v for v in vals if v is not None)
    return [("\\textbf{" + f(v) + "}") if v == best else f(v) for v in vals]


def main():
    rouge = {k: json.loads((d / "official_rouge.json").read_text()) for k, d in PRED.items() if (d / "official_rouge.json").exists()}
    items = {k: load_jsonl(EVAL / k / "per_item.jsonl") for k in PRED if (EVAL / k / "per_item.jsonl").exists()}
    systems = [k for k in PRED if k in rouge and k in items]
    summary = {"systems": systems, "rouge": rouge, "factuality": {}, "verifier": None}
    tab = PAPER / "tables"
    tab.mkdir(parents=True, exist_ok=True)

    # ---- Dataset 1: ACI-Bench test 1 vs published
    rows = [(n, m, *v) for n, m, *v in ACI_PUB] + \
           [(f"Ours: {NAME[k]}", "Llama-3.1-8B", *(rouge[k]["aci_bench_test_taskB_1"][t] for t in ("rouge1", "rouge2", "rougeL", "rougeLsum"))) for k in systems]
    cols = list(zip(*[r[2:] for r in rows]))
    cols = [bold_max(c) for c in cols]
    body = [f"{r[0]} & {r[1]} & " + " & ".join(c[i] for c in cols) + "\\\\" + ("\\midrule" if i == len(ACI_PUB) - 1 else "")
            for i, r in enumerate(rows)]
    (tab / "aci.tex").write_text("\n".join([
        "\\begin{table}[t]", "\\centering",
        "\\caption{Dataset 1 --- ACI-Bench test 1 (40 full notes, MEDIQA-Chat 2023 Task B). ROUGE F1, official scoring. "
        "Published rows from~\\cite{abacha2023overview}.}\\label{tab:aci}",
        "\\scriptsize", "\\setlength{\\tabcolsep}{2.5pt}", "\\resizebox{\\columnwidth}{!}{\\begin{tabular}{@{}llrrrr@{}}", "\\toprule",
        "System & Method & R-1 & R-2 & R-L & R-Lsum\\\\", "\\midrule", *body, "\\bottomrule", "\\end{tabular}}", "\\end{table}"]) + "\n", encoding="utf-8")

    # ---- Dataset 2: MTS-Dialog test 1 vs published, and all 400 vs Lyu et al.
    def mts_block(pub, split):
        rows = [(n, m, *v) for n, m, *v in pub] + \
               [(f"Ours: {NAME[k]}", "Llama-3.1-8B", *(rouge[k][split][t] for t in ("rouge1", "rouge2", "rougeL"))) for k in systems]
        cols = [bold_max(c) for c in zip(*[r[2:] for r in rows])]
        return [f"{r[0]} & {r[1]} & " + " & ".join(c[i] for c in cols) + "\\\\" + ("\\midrule" if i == len(pub) - 1 else "")
                for i, r in enumerate(rows)]
    (tab / "mts.tex").write_text("\n".join([
        "\\begin{table}[t]", "\\centering",
        "\\caption{Dataset 2 --- MTS-Dialog. Top: test 1 (200, MEDIQA-Chat 2023 Task A~\\cite{abacha2023overview}). "
        "Bottom: both test sets (400) vs.~\\cite{lyu2024}. ROUGE F1, official scoring.}\\label{tab:mts}",
        "\\scriptsize", "\\setlength{\\tabcolsep}{2.5pt}", "\\resizebox{\\columnwidth}{!}{\\begin{tabular}{@{}llrrr@{}}", "\\toprule",
        "System & Method & R-1 & R-2 & R-L\\\\", "\\midrule",
        "\\multicolumn{5}{@{}l}{\\emph{Test 1 (200)}}\\\\", *mts_block(MTS_PUB, "mts_dialog_test_chat_2023"), "\\midrule",
        "\\multicolumn{5}{@{}l}{\\emph{Test 1 + 2 (400)}}\\\\", *mts_block(MTS400_PUB, "mts_dialog_test_all"),
        "\\bottomrule", "\\end{tabular}}", "\\end{table}"]) + "\n", encoding="utf-8")

    # ---- factuality per dataset (pooled over that dataset's test splits)
    keys = ["rougeL", "bertscore_f1", "hallucination_rate", "negation_flip_rate", "numerical_consistency", "clinical_coverage"]
    for ds in DATASETS:
        summary["factuality"][ds] = {}
        for k in systems:
            its = [it for it in items[k] if it["dataset"] == ds and it["split"].startswith(ds + "_test")]   # test splits only
            m = {key: mean([it.get(key) for it in its]) for key in keys}
            p = 1 - m["hallucination_rate"] if m["hallucination_rate"] is not None else None
            r = m["clinical_coverage"]
            m |= {"n": len(its), "fact_precision": p, "fact_recall": r, "fact_f1": 2 * p * r / (p + r) if p and r else None,
                  "degenerate": sum(1 for it in its if it.get("degenerate")), "truncated": sum(1 for it in its if it.get("truncated")),
                  "empty": sum(1 for it in its if not it.get("pred_words"))}
            summary["factuality"][ds][k] = m
    lines = []
    for ds, label in DATASETS.items():
        lines.append(f"\\multicolumn{{10}}{{@{{}}l}}{{\\emph{{{label}}}}}\\\\")
        for k in systems:
            m = summary["factuality"][ds][k]
            pct = lambda x: "--" if x is None else f"{100 * x:.1f}"
            lines.append(f"{NAME[k]} & {pct(m['rougeL'])} & {f(m['bertscore_f1'], 3)} & {pct(m['hallucination_rate'])} & "
                         f"{pct(m['negation_flip_rate'])} & {pct(m['numerical_consistency'])} & {pct(m['clinical_coverage'])} & "
                         f"{pct(m['fact_precision'])} & {pct(m['fact_recall'])} & {pct(m['fact_f1'])}\\\\")
        lines.append("\\midrule")
    (tab / "factuality.tex").write_text("\n".join([
        "\\begin{table*}[t]", "\\centering",
        "\\caption{Clinical factuality on all test items of each dataset (per-item means, \\%). R-L uses stemming; BERTScore "
        "= roberta-large, rescaled. Halluc.\\ and Neg.\\ flip: lower is better. $P_f=1-$Halluc., $R_f=$ Coverage.}\\label{tab:fact}",
        "\\footnotesize", "\\resizebox{\\textwidth}{!}{\\begin{tabular}{@{}lrrrrrrrrr@{}}", "\\toprule",
        "System & R-L & BERTScore & Halluc.$\\downarrow$ & Neg.\\ flip$\\downarrow$ & Num.\\ cons. & Coverage & $P_f$ & $R_f$ & $F1_f$\\\\",
        "\\midrule", *lines[:-1], "\\bottomrule", "\\end{tabular}}", "\\end{table*}"]) + "\n", encoding="utf-8")

    # ---- verifier statistics
    vs_path = PRED["verified"] / "verifier_stats.json"
    if vs_path.exists():
        vs = json.loads(vs_path.read_text())
        summary["verifier"] = vs
        rows = []
        for ds, label in DATASETS.items():
            sp = [s for name, s in vs["splits"].items() if name.startswith(ds)]
            n = sum(s["sentences_checked"] for s in sp)
            rows.append(f"{label} & {sum(s['items'] for s in sp)} & {n} & " +
                        " & ".join(f"{100 * sum(s[c] for s in sp) / max(1, n):.1f}" for c in ("green", "yellow", "red")) +
                        f" & {sum(s['items_emptied'] for s in sp)}\\\\")
        (tab / "verifier.tex").write_text("\n".join([
            "\\begin{table}[t]", "\\centering",
            "\\caption{Verifier verdicts on system B notes (share of checked sentences, \\%). Red sentences are dropped.}\\label{tab:ver}",
            "\\scriptsize", "\\setlength{\\tabcolsep}{3pt}", "\\resizebox{\\columnwidth}{!}{\\begin{tabular}{@{}lrrrrrr@{}}", "\\toprule",
            "Dataset & Notes & Sent. & Green & Yellow & Red & Emptied\\\\", "\\midrule", *rows,
            "\\bottomrule", "\\end{tabular}}", "\\end{table}"]) + "\n", encoding="utf-8")

    # ---- figure
    try:
        import matplotlib
        matplotlib.use("Agg")
        import matplotlib.pyplot as plt
        fig, axes = plt.subplots(1, 2, figsize=(7, 2.8), dpi=200)
        colors = ["#8a8f98", "#c9a227", "#4c78a8", "#f58518", "#54a24b"]
        for ax, (ds, label) in zip(axes, DATASETS.items()):
            metrics = [("hallucination_rate", "Halluc."), ("clinical_coverage", "Coverage"), ("fact_f1", "Fact F1")]
            w = 0.8 / len(systems)
            for j, k in enumerate(systems):
                vals = [100 * (summary["factuality"][ds][k][m] or 0) for m, _ in metrics]
                ax.bar([i + j * w for i in range(len(metrics))], vals, w, label=NAME[k], color=colors[j % len(colors)])
            ax.set_xticks([i + w * (len(systems) - 1) / 2 for i in range(len(metrics))], [t for _, t in metrics], fontsize=7)
            ax.set_title(label, fontsize=8)
            ax.set_ylim(0, 100)
            ax.tick_params(labelsize=7)
            ax.spines[["top", "right"]].set_visible(False)
        axes[0].set_ylabel("%", fontsize=7)
        handles, labels = axes[0].get_legend_handles_labels()
        fig.legend(handles, labels, fontsize=6.5, frameon=False, loc="lower center", ncol=len(systems))
        fig.tight_layout(rect=(0, 0.08, 1, 1))
        (PAPER / "figures").mkdir(exist_ok=True)
        fig.savefig(PAPER / "figures" / "factuality.png")
    except Exception as e:  # noqa: BLE001
        print("figure skipped:", e)

    EVAL.mkdir(parents=True, exist_ok=True)
    (EVAL / "summary.json").write_text(json.dumps(summary, indent=2), encoding="utf-8")
    md = ["# Review 3 results summary", "", "Generated by `scripts/make_paper_tables.py`.", "",
          "## Official ROUGE (MEDIQA-Chat scoring)", "", "| system | split | n | R-1 | R-2 | R-L | R-Lsum |", "|---|---|---|---|---|---|---|"]
    for k in systems:
        for s, v in rouge[k].items():
            md.append(f"| {NAME[k]} | {s} | {v['n']} | {f(v['rouge1'], 4)} | {f(v['rouge2'], 4)} | {f(v['rougeL'], 4)} | {f(v['rougeLsum'], 4)} |")
    md += ["", "## Factuality (per dataset, all test items)", "",
           "| dataset | system | n | R-L | BERTScore | halluc. | neg. flip | num. cons. | coverage | P_f | R_f | F1_f | degenerate | truncated | empty |",
           "|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|"]
    for ds in DATASETS:
        for k in systems:
            m = summary["factuality"][ds][k]
            md.append(f"| {ds} | {NAME[k]} | {m['n']} | " + " | ".join(f(m[x]) for x in ("rougeL", "bertscore_f1", "hallucination_rate", "negation_flip_rate",
                      "numerical_consistency", "clinical_coverage", "fact_precision", "fact_recall", "fact_f1")) +
                      f" | {m['degenerate']} | {m['truncated']} | {m['empty']} |")
    (EVAL / "summary.md").write_text("\n".join(md) + "\n", encoding="utf-8")
    print("\n".join(md))


if __name__ == "__main__":
    main()
