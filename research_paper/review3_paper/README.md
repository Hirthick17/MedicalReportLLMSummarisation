# Review 3 reference paper (AI-assisted draft)

`main.pdf` is a complete IEEE-format draft that shows the structure, content and evidence the Review 3
paper needs. It is a **reference for the team**: rewrite it in your own words before submitting.

## Build

    tectonic main.tex          # local (installed in miniconda: C:\Users\hirth\miniconda3\Library\bin\tectonic.exe)

or upload this folder to Overleaf (IEEEtran is built in).

## Where every number comes from

| paper part | source | regenerate with |
|---|---|---|
| Tables `aci.tex`, `mts.tex` (comparison with published systems) | our predictions re-scored with the official MEDIQA-Chat ROUGE + `research_paper/published_results.md` | `python scripts/official_rouge.py <pred dir>` then `python scripts/make_paper_tables.py` |
| Table `factuality.tex`, figure `factuality.png` | `reports/eval_review3/<system>/per_item.jsonl` | `python -m src.eval.run_eval --run <run> --system <sys> --label <label> --out reports/eval_review3 --bertscore` |
| Table `verifier.tex` | `<pred dir>/factcond_verified/verifier_stats.json` | `python scripts/run_verifier.py <B dir> <C dir>` |
| Verifier calibration numbers | `reports/eval_review3/verifier_calibration.md` | `python scripts/calibrate_verifier.py` |
| Published numbers | `research_paper/published_results.md` (copied from the PDFs in `research_paper/pdfs/`) | — |
| Literature survey | the PDFs in `research_paper/pdfs/` (`MANIFEST.md` lists what downloaded) | `python scripts/fetch_papers.py` |
| Generation run (systems A and B) | Kaggle kernel `hirthick17/medsum-review3-infer`, prompts dataset `hirthick17/medsum-review3-prompts` | `python scripts/build_review3_prompts.py`, then push `kaggle/review3/` |

## Before you submit

- Rewrite every section in your own words; keep the numbers exactly as in the tables.
- Read each surveyed paper (at least abstract, method, results) before you describe it.
- Remove the red "reference draft" footnote on the title.
- The 102 papers in `research_paper/pdfs/MANIFEST.md` → "Not downloaded" need library access if you want to cite them.
