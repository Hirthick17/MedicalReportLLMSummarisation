# medsum-fact — FaCTS

Fact-Constrained, Traceable Summarization of clinical text.
BCSE306L mini-project (DA1 · DA2 · DA3).

Start with **[docs/REVIEW2_SUMMARY.md](docs/REVIEW2_SUMMARY.md)** — the one-page overview of what
Review 2 delivered, the key numbers and where everything is. Then, per role:

- **[docs/PERSON1_DATA_PIPELINE.md](docs/PERSON1_DATA_PIPELINE.md)** — datasets, cleaning, standard
  schema, duplicates / leakage / length audit, train-val-test preparation, the clinical fact extractor
  (`src/cfe/`) and the facts dataset.
- **[docs/PERSON2_MODEL_TRAINING.md](docs/PERSON2_MODEL_TRAINING.md)** — model choice, environment,
  4-bit QLoRA, the training run, issues solved, testing, generation, saved artefacts, handoff.
  Procedure and troubleshooting in full: **[REVIEW2_BASELINE.md](REVIEW2_BASELINE.md)**; run history:
  **[STATUS.md](STATUS.md)**.
- **[docs/PERSON3_EVALUATION.md](docs/PERSON3_EVALUATION.md)** — ROUGE / BERTScore, the factuality
  checker (`src/eval/`), results tables, figures, example errors, preliminary conclusions.
- **[MODEL_PLAN.md](MODEL_PLAN.md)** — the full FaCTS design (Review 3 target).

### Review 3 (this version)

The Review 3 paper is **[research_paper/review3_paper/main.pdf](research_paper/review3_paper/main.pdf)**
(LaTeX sources and tables in the same folder; how each number is produced: its `README.md`).
This version of the code covers SFT training and testing on ACI-Bench and MTS-Dialog:

| system | what it is | code |
|---|---|---|
| SFT | Review 2 QLoRA adapter, Review 2 prompt, 1,024 new tokens | `kaggle/review3_sft/` |
| SFT + fact table | same adapter, fact-conditioned prompt | `kaggle/review3_sft/` |
| A. Zero-shot | base Llama-3.1-8B-Instruct, Review 2 prompt | `kaggle/review3/` |
| B. + Fact table | base model, fact-conditioned prompt (`src/pipeline/`) | `kaggle/review3/` |

Test sets: ACI-Bench test 1–3 (120 encounters) and MTS-Dialog test 1–2 (400). Results:
`reports/eval_review3/` (`summary.md`, `significance.md`, one folder per system). The sentence verifier
of system C is not part of this code release; its results are reported in the paper.

```bash
python scripts/build_review3_prompts.py            # -> kaggle/review3_data/ (prompts dataset, not committed)
kaggle kernels push -p kaggle/review3              # systems A and B
kaggle kernels push -p kaggle/review3_sft          # SFT and SFT + fact table
python scripts/official_rouge.py <predictions dir> # MEDIQA-Chat ROUGE
python -m src.eval.run_eval --run <run> --system <system> --label <label> --out reports/eval_review3 --bertscore
python scripts/paired_bootstrap.py                 # -> reports/eval_review3/significance.md
python scripts/make_paper_tables.py                # -> research_paper/review3_paper/tables/
```

---

## Quick start

```bash
pip install requests huggingface_hub
python scripts/download_datasets.py --tier core --tier extra   # ~1.3 GB into data/raw/
python scripts/import_datasets.py                              # -> data/processed/<dataset>/<split>.jsonl
python scripts/make_baseline_split.py                          # -> baseline_train/val.jsonl + train_manifest.json
python scripts/audit_dataset.py                                # -> reports/data_audit/ (dups, leakage, token lengths)
python scripts/extract_clinical_facts.py                       # -> data/processed/facts/ (8 min CPU)
python -m src.eval.run_eval --run outputs/kaggle/outputs/baseline_qlora_llama31_8b --label run3_rep1.2_ngram6 --bertscore
python -m src.eval.run_eval --compare                          # -> reports/eval_baseline/comparison.md
python -m pytest tests -q
```

The `core` tier alone (~860 MB) is enough for MODEL_PLAN.md; `extra` adds `dialogue_soap`,
which the project report names as a primary training corpus, so fetch both.

---

## The downloader

`scripts/download_datasets.py` holds a registry of every corpus the project uses, with
its role in the pipeline, its licence, and how to fetch it. Downloads resume on
interruption, are skipped if already complete, and are recorded in `data/MANIFEST.json`
with sizes and SHA-256 digests.

```bash
python scripts/download_datasets.py --list                 # show the registry
python scripts/download_datasets.py --tier core            # default
python scripts/download_datasets.py --tier core --tier extra
python scripts/download_datasets.py --only meqsum,aci_bench
python scripts/download_datasets.py --skip asclepius_synthetic --tier core
python scripts/download_datasets.py --tier core --dry-run  # show what would be fetched
python scripts/download_datasets.py --only meqsum --force  # redownload
```

### Tiers

**`core`** (~860 MB, no account needed) — everything needed to train and evaluate the
full pipeline.

| key | what | role |
|---|---|---|
| `meqsum` | 1,000 consumer health question / summary pairs | question summarization |
| `mediqa2021` | MEDIQA-2021 Task1 QS, Task2 MAS, Task3 RRS | the QS/MAS sets named in the report |
| `mts_dialog` | 1,201 dialogue → note-section pairs + augmented sets | dialogue → note |
| `aci_bench` | 207 full encounters with reference SOAP notes | dialogue → full note; MEDCON metric |
| `openi_iu_xray` | 3,955 de-identified IU chest X-ray reports (XML) | Findings → Impression; MIMIC-CXR stand-in |
| `asclepius_synthetic` | 158k synthetic clinical-note instruction pairs | large-scale note → summary |
| `augmented_clinical_notes` | 30,000 notes with summaries | note → structured summary |
| `scifact` | 809 claims + 5,183 abstracts | verifier training (MedNLI fallback) |

**`extra`** (~360 MB) — optional breadth.

| key | what | role |
|---|---|---|
| `meddialog` | MedDialog-EN HealthCareMagic + iCliniq (parquet) | dialogue summarization eval |
| `dialogue_soap` | 9,250 dialogue → SOAP summary pairs | extra dialogue supervision |
| `medquad` | 47k NIH medical QA pairs | background corpus / RAG index |
| `mediqa2019` | MEDIQA-2019 NLI / RQE / QA | verifier pretraining |

**`gated`** — PhysioNet credentialed data. **Not downloaded by default.**

| key | what |
|---|---|
| `mimic_iv_note` | MIMIC-IV-Note v2.2 — 331k discharge summaries |
| `mimic_cxr_reports` | MIMIC-CXR v2.1.0 free-text reports |
| `mednli` | MedNLI — clinical NLI, the preferred verifier training set |

These require a PhysioNet account, completed CITI "Data or Specimens Only Research"
training, and a signed data use agreement **per project**. Approval typically takes
one to several weeks, so start it now:

- https://physionet.org/settings/credentialing/
- https://physionet.org/content/mimic-iv-note/2.2/
- https://physionet.org/content/mednli/1.0.0/

Once approved:

```bash
python scripts/download_datasets.py --include-gated --tier gated --physionet-user YOURNAME
```

The password is read from `PHYSIONET_PASSWORD` if set, otherwise prompted for with
`getpass` (not echoed). It is used for that session only and never written to disk.
A `403` from PhysioNet means the account is not credentialed for that specific project.

**The core pipeline does not depend on any gated data.** MIMIC is used only for the
external-validation experiment in MODEL_PLAN.md §5.5, which is upside, not a blocker.

---

## The importer

`scripts/import_datasets.py` converts the three dialogue → note corpora the report names as
primary (ACI-Bench, MTS-Dialog, DialogueSOAP) into one schema under `data/processed/`:

```json
{"id": "...", "dataset": "aci_bench", "split": "train",
 "source_dialogue": "...", "target_summary": "...", "metadata": {...}}
```

```bash
python scripts/import_datasets.py                       # all three
python scripts/import_datasets.py --only aci_bench      # one corpus
python scripts/import_datasets.py --validate-only       # schema check + stats, writes nothing
```

Record counts as of 2026-09-14 (`--validate-only`):

| corpus | train | val | test | avg dialogue words | avg note words |
|---|---|---|---|---|---|
| `aci_bench` | 67 | 20 | 40 / 40 / 40 (taskB-1, taskC-2, taskC-3) | ~1,300 | ~420 |
| `mts_dialog` | 1,201 | 100 | 200 / 200 (Chat-2023, Sum-2023) | ~100 | ~40 |
| `dialogue_soap` | 9,250 | 500 | 250 | ~415 | ~246 |

`metadata` carries `file_id` (ACI-Bench), `row_id` + `section_header` (MTS-Dialog), or `prompt`
(DialogueSOAP). Splits are the corpora's official ones; nothing is re-split.

---

## Layout

```
medsum-fact/
├── docs/                       # Review 2 documentation (summary + one document per role)
├── MODEL_PLAN.md               # full FaCTS design (Review 3)
├── REVIEW2_BASELINE.md         # plain QLoRA baseline procedure + troubleshooting (Review 2)
├── STATUS.md                   # run history
├── README.md
├── requirements.txt
├── scripts/
│   ├── download_datasets.py    # raw corpora -> data/raw/
│   ├── import_datasets.py      # data/raw/ -> data/processed/ unified jsonl
│   ├── make_baseline_split.py  # Review 2 train/val mix + leakage checks + manifest
│   ├── audit_dataset.py        # duplicates, near-duplicates, unusable samples, leakage, token lengths -> reports/data_audit/
│   ├── extract_clinical_facts.py # runs src/cfe over every split -> data/processed/facts/, data/interim/cfe_stats.json
│   ├── make_report.py          # merged Kaggle outputs -> reports/<run>/report.pdf (+ metrics.json)
│   └── fetch_kaggle_run.py     # drive kernel A -> adapter dataset -> kernel B, verify sha, download, report
├── src/
│   ├── cfe/                    # rule-based Clinical Fact Extractor: lexicon (lex_*.py), negation.py, extractor.py
│   ├── pipeline/               # Review 3: fact table + fact-conditioned prompt (fact_table.py, prompt.py)
│   └── eval/                   # metrics.py (ROUGE/BERTScore/degeneration), factuality.py, run_eval.py
├── tests/                      # pytest: test_cfe.py, test_factuality.py, test_fact_table.py
├── kaggle/
│   ├── dataset/                # what gets uploaded as the private Kaggle dataset
│   ├── baseline/               # kernel A: baseline_qlora.py — TRAINS, saves final/ + train_summary.json
│   ├── adapter/                # metadata of the private adapter dataset
│   ├── infer/                  # kernel B: baseline_infer.py — loads the pinned adapter, GENERATES, writes training_config.json
│   ├── review3/                # Review 3: systems A (zero-shot) and B (fact table) on the test sets
│   ├── review3_sft/            # Review 3: SFT and SFT + fact table on the same test sets
│   └── review3_data/           # metadata of the prompts dataset (the prompts themselves are not committed)
├── research_paper/review3_paper/ # Review 3 paper: main.pdf, LaTeX sources, tables, figure
├── data/
│   ├── raw/<dataset_key>/      # downloader writes here (git-ignored)
│   ├── processed/              # unified jsonl, baseline_train/val.jsonl, train_manifest.json, facts/ (git-ignored)
│   ├── interim/                # cfe_stats.json
│   └── MANIFEST.json
├── reports/                    # committed: data_audit/, eval_baseline/<label>/, baseline_qlora_llama31_8b/report.pdf, eval_review3/
└── outputs/                    # git-ignored: adapters, checkpoints, predictions
    ├── kaggle/outputs/baseline_qlora_llama31_8b/     # run 3 (kernel A + kernel B merged; layout in REVIEW2_BASELINE.md §9)
    ├── kaggle_run1_old_decoding/                    # run 1 predictions (old decoding, same adapter)
    └── kaggle_run2_smoke_adapter/                   # run 2 — WRONG adapter, kept only as evidence
```

## Baseline run → report

The baseline is two Kaggle kernels, because one kernel gets 12 h and training alone takes
~11 h on 2× T4 (see STATUS.md for the run that proved it):

| kernel | id | does | budget |
|---|---|---|---|
| A `kaggle/baseline/` | `hirthick17/medsum-baseline-qlora` | QLoRA training → `final/`, `trainer_state.json`, `train_summary.json` | ≤ 10.5 h train + save |
| B `kaggle/infer/` | `hirthick17/medsum-baseline-infer` | loads the adapter from the dataset `hirthick17/medsum-baseline-adapter` (sha256-pinned), generates val checks + 6 test splits → `predictions/`, `training_config.json` | ~4 h |

```bash
kaggle kernels push -p kaggle/baseline --accelerator NvidiaTeslaT4   # start training (≈ 11 h)
python scripts/fetch_kaggle_run.py                      # waits for A, downloads, uploads the adapter, pushes B, waits, downloads, verifies, report
python scripts/fetch_kaggle_run.py --stage adapter      # upload outputs/kaggle/.../final as the adapter dataset only
python scripts/fetch_kaggle_run.py --stage infer --push # re-run generation only (e.g. after a decoding change)
python scripts/make_report.py                           # (re)build reports/<run>/report.pdf from outputs/
```

The adapter goes through a dataset rather than kernel B mounting kernel A directly because Kaggle
mounts a kernel's latest *completed* version: after the cancelled 17 Sep run that was the smoke run,
and run 2 (18 Sep) evaluated a 20-step adapter for 3.8 h without anything failing. Kernel B now
refuses any adapter whose sha256 differs from `EXPECTED_ADAPTER_SHA256`, and both the fetch script
and the report check it against the local `final/` (details: STATUS.md, REVIEW2_BASELINE.md §2.2a).

## Notes on the data

- `dialogue_soap/train.json` is **JSON Lines**, not a JSON array — read it line by line.
- `mts_dialog` CSV fields contain embedded newlines; use `csv.DictReader`, not `readlines`.
- `mediqa2021/Task3` (radiology) ships `make_mimic_data.py`, which rebuilds the training
  split from MIMIC-CXR. Without credentialed access, use `indiana_dev.json` and the
  `openi_iu_xray` corpus instead.
- `asclepius_synthetic` is CC BY-NC-SA 4.0 — non-commercial only, which coursework is.
- Reading the parquet and xlsx corpora needs `pyarrow` and `openpyxl` (in requirements.txt).

## Licensing

Every corpus keeps its own licence; see the `licence` field per entry in
`--list` output and in `data/MANIFEST.json`. The PhysioNet sets additionally forbid
redistribution and any attempt at re-identification — do not commit them anywhere,
and do not paste their contents into a hosted LLM API.
