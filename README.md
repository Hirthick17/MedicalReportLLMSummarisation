# medsum-fact — FaCTS

Fact-Constrained, Traceable Summarization of clinical text.
BCSE306L mini-project (DA1 · DA2 · DA3).

Two documents describe the work:

- **[MODEL_PLAN.md](MODEL_PLAN.md)** — the full FaCTS design: architecture, baselines, metrics,
  ablations, compute budget and risk table. This is the Review 3 target.
- **[REVIEW2_BASELINE.md](REVIEW2_BASELINE.md)** — the Review 2 deliverable: the plain QLoRA
  baseline end to end (model choice, environment, 4-bit QLoRA, training, troubleshooting,
  testing, inference, saving, handoff to evaluation). Review 2 stops there.

---

## Quick start

```bash
pip install requests huggingface_hub
python scripts/download_datasets.py --tier core --tier extra   # ~1.3 GB into data/raw/
python scripts/import_datasets.py                              # -> data/processed/<dataset>/<split>.jsonl
python scripts/make_baseline_split.py                          # -> baseline_train/val.jsonl + train_manifest.json
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
├── MODEL_PLAN.md               # full FaCTS design (Review 3)
├── REVIEW2_BASELINE.md         # plain QLoRA baseline workflow (Review 2)
├── README.md
├── requirements.txt
├── scripts/
│   ├── download_datasets.py    # raw corpora -> data/raw/
│   ├── import_datasets.py      # data/raw/ -> data/processed/ unified jsonl
│   └── make_baseline_split.py  # Review 2 train/val mix + leakage checks + manifest
├── kaggle/
│   ├── dataset/                # what gets uploaded as the private Kaggle dataset
│   └── baseline/               # baseline_qlora.py + kernel-metadata.json (see REVIEW2_BASELINE.md §2.2a)
├── data/
│   ├── raw/<dataset_key>/      # downloader writes here
│   │   └── .download_complete  # marker + metadata; delete to force refetch
│   ├── interim/                # fact-extractor cache (Stage 1, Review 3)
│   ├── processed/              # unified train/dev/test jsonl
│   └── MANIFEST.json
└── outputs/                    # git-ignored: adapters, checkpoints, predictions
    └── baseline_qlora_llama31_8b/   # layout in REVIEW2_BASELINE.md §9
```

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
