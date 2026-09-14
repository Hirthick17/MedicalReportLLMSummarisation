# FaCTS — Fact-Constrained, Traceable Summarization of Clinical Text

Model plan for BCSE306L mini-project (DA1 → DA2 → DA3).
Derived from `ARTIFICIAL INTELLIGENCE PROJECT REPORT.docx` and `Literature_Survey_Editable.docx`.

---

## 1. Why this design

The literature survey converges on five gaps. Every stage below exists to close a specific one —
this mapping is what makes the architecture defensible in the DA1/DA3 rubric ("justification for
each design choice, backed by a citation or a stated hypothesis").

| Gap (from survey) | Evidence | Stage that addresses it |
|---|---|---|
| G1 Hallucination / factual inconsistency | [1][3][6][10][15] | Stage 1 fact extraction + Stage 2 fact conditioning + Stage 2b factuality DPO + Stage 3 verify-and-repair |
| G2 Limited external validation | [4][8][11] — only 7% of studies validate externally | Cross-dataset protocol (§6.3): train on one corpus, test on a held-out corpus from a different institution/modality |
| G3 No standardized evaluation | [4][8][12][13] | Fixed metric suite (§5) reported for *every* baseline and ablation, single harness, released config |
| G4 Limited explainability | [3][21] — explainability raised clinician acceptance 27.3% | Stage 4 sentence-level provenance + entailment score attached to every output sentence |
| G5 No real-world deployment evidence | [9][11][14] | Stage 6 clinician-facing demo + reader study protocol (§5.3) |

The key claim of the project: **generation conditioned on an explicitly extracted fact table, then
filtered by an entailment verifier, reduces hallucination rate at equal or better ROUGE compared to
a plain QLoRA fine-tune** — which is the setup used by [1], [10] and [15], the strongest baselines
in the survey.

---

## 2. Pipeline

```
                    ┌──────────────────────────────────────────────┐
 raw clinical text  │ Stage 0  Ingest & Normalize                  │
 (note / report /   │  de-ID scrub, section split, sentence split  │
  dialogue)         │  out: S = [s_1 … s_n] with char offsets      │
                    └───────────────┬──────────────────────────────┘
                                    │
              ┌─────────────────────┴──────────────────────┐
              ▼                                            ▼
 ┌────────────────────────────┐              ┌─────────────────────────────┐
 │ Stage 1  Clinical Fact     │              │  (source text, verbatim)    │
 │ Extractor  (CFE)           │              └──────────────┬──────────────┘
 │  scispaCy NER + UMLS link  │                             │
 │  + negspaCy assertion      │                             │
 │  out: F = {f_1 … f_m}      │                             │
 └──────────────┬─────────────┘                             │
                └───────────────┬────────────────────────────┘
                                ▼
                 ┌───────────────────────────────────┐
                 │ Stage 2  Grounded Generator  (G)   │   ◀── NOVELTY 1: fact-table conditioning
                 │  8B decoder LLM, 4-bit QLoRA       │   ◀── NOVELTY 2: factuality DPO on
                 │  prompt = [FACTS] + [REPORT] + inst│           perturbation-generated negatives
                 │  out: draft summary Ŷ              │
                 └───────────────┬───────────────────┘
                                 ▼
                 ┌───────────────────────────────────┐
                 │ Stage 3  Verifier & Repair  (V)    │   ◀── NOVELTY 3: closed repair loop
                 │  per-sentence NLI vs. retrieved    │
                 │  source evidence; τ threshold;     │
                 │  ≤R regeneration rounds; else drop │
                 └───────────────┬───────────────────┘
                                 ▼
                 ┌───────────────────────────────────┐
                 │ Stage 4  Provenance Assembly       │   ◀── NOVELTY 4: traceable output
                 │  each sentence ← (src ids, CUIs,   │
                 │  entailment score)                 │
                 └───────────────┬───────────────────┘
                                 ▼
        Stage 5 Evaluation  ·  Stage 6 Clinician demo (Gradio)
```

### Stage 0 — Ingest & normalize
- PHI scrub with `philter`-style regex + Presidio (datasets are already de-identified; this is a
  deployment-safety component, and it is what the report's privacy constraint refers to).
- Section segmentation by header regex (`HISTORY`, `FINDINGS`, `IMPRESSION`, `ASSESSMENT/PLAN`, …).
  Radiology corpora already carry a Findings→Impression split; reuse it directly.
- Sentence split with `scispacy` sentencizer. Keep `(start_char, end_char)` per sentence — Stage 4
  provenance depends on these offsets surviving the whole pipeline.
- Output tensor/shape: token ids `[B, L_src]`, `L_src` = 4096 (8192 for full discharge summaries).

### Stage 1 — Clinical Fact Extractor (CFE)
Non-trainable, deterministic. Runs once per document and is cached to disk.

- NER: `en_core_sci_scibert` (scispaCy).
- Concept normalization: scispaCy `EntityLinker(name="umls")` → CUI + canonical name, keep top-1
  above 0.80 similarity.
- Assertion: `negspacy` + ConText rules → `present | absent | hypothetical | family | historical`.
- Numeric/value capture: regex over measurements, dosages, lab values, dates.

A fact is the tuple

```
f = ⟨cui, surface, semantic_type, assertion, value, unit, temporality, (start,end)⟩
```

Serialized into the prompt as a compact table (≈ 40–120 facts per note, ~300–900 tokens):

```
FACTS
- C0018802 | congestive heart failure | Disease | present | — | hist:chronic
- C0020538 | hypertension            | Disease | present | — | hist:chronic
- C0004153 | atelectasis             | Finding | absent  | — | current
- C0428886 | ejection fraction       | Lab     | present | 35 | %  | current
```

*Hypothesis:* surfacing normalized concepts and, critically, **assertion status** in the prompt
reduces two dominant clinical hallucination modes reported in [1] and [6] — inventing a finding, and
flipping a negation. Negation-flip is measured separately in §5.2 to test this directly.

### Stage 2 — Grounded Generator (G)

| Item | Choice | Reason |
|---|---|---|
| Base model | `meta-llama/Llama-3.1-8B-Instruct` (primary), `BioMistral/BioMistral-7B` (domain-adapted control) | Report names Llama-3 / BioMistral / MedGemma as candidates. Llama-3.1 is gated → accept the licence on HF; BioMistral is ungated, so it is the no-blocker fallback. |
| Quantization | 4-bit NF4, double-quant, bf16 compute | Fits 8B + 4k context in ~11 GB → Colab L4/T4-high-RAM |
| Adapter | LoRA r=16, α=32, dropout 0.05, on `q,k,v,o,gate,up,down_proj` | Standard QLoRA recipe; matches the PEFT setup in [1][10][15] so the comparison is like-for-like |
| Context | 4096 train / 8192 infer | 95th-percentile note length |
| Loss masking | loss on completion tokens only | Prevents the model memorizing the prompt-side fact table |
| Optimizer | paged AdamW 8-bit, lr 2e-4, cosine, warmup 3%, 3 epochs, bs 1 × grad-accum 16 | |

**Stage 2b — Factuality preference tuning (ORPO or DPO).**
This is where the anti-hallucination signal actually enters the weights, and it costs almost nothing
to build because the CFE gives free supervision:

1. `chosen` = the reference (or SFT-model) summary that passes the verifier.
2. `rejected` = the same summary with one controlled corruption injected by the CFE:
   - entity swap (replace a CUI with a semantically-close sibling from UMLS),
   - negation flip (`absent` → `present`),
   - numeric perturbation (±20–200% on a lab value / dosage),
   - unsupported-sentence insertion (a fact present in a *different* patient's note).
3. Train ORPO (single-stage, no reference model → cheaper than DPO on a Colab budget), β = 0.1,
   1 epoch over ~8–15k pairs.

*Hypothesis:* the model learns to prefer summaries whose facts are entailed by the source, rather
than summaries that merely read fluently — which is exactly the failure mode [1] and [3] report.

### Stage 3 — Verifier & Repair (V)

- **Evidence retrieval** per generated sentence `ŷ_j`: BM25 top-10 ∪ SapBERT-embedding top-5 over
  source sentences `S`. (`cambridgeltl/SapBERT-from-PubMedBERT-fulltext`.)
- **Entailment**: cross-encoder `microsoft/deberta-v3-base` fine-tuned on MedNLI (PhysioNet, gated)
  — fallback if MedNLI access is pending: SciFact + the synthetic perturbation pairs from Stage 2b,
  which are in-domain and free.
  Score `e_j = max_k P(entail | s_k, ŷ_j)`.
- **Decision**: keep if `e_j ≥ τ` (τ tuned on dev for best factuality at ≤1 ROUGE-L point of loss;
  expect τ ≈ 0.5–0.7).
- **Repair loop**: flagged sentences are regenerated with the corrective instruction
  `"Sentence N is not supported by the report. Rewrite it using only these facts: {...}, or omit it."`
  Max `R = 2` rounds; still-unsupported sentences are dropped and logged.
  Deletion is safe here — omitting an unsupported claim cannot harm a clinician; asserting a false
  one can. Coverage cost of deletion is reported explicitly in §5.

### Stage 4 — Provenance assembly
Each surviving sentence emits `{text, source_sent_ids, matched_cuis, entailment_score}`. Rendered as
inline markers `[S12, S14]`, with the source spans highlighted on hover. This is the concrete answer
to G4 — the summary is auditable sentence by sentence, without any post-hoc attribution method.

---

## 3. Data plan

Run `python scripts/download_datasets.py --tier core` (see `README.md`).

| Role | Corpus | Pairs (approx) | Access |
|---|---|---|---|
| Train — dialogue → note | ACI-Bench, MTS-Dialog | 207 full encounters + 1.7k section pairs | open |
| Train — note → summary | Asclepius Synthetic Clinical Notes, Augmented Clinical Notes | 158k / 30k | open |
| Train/eval — radiology Findings → Impression | Open-i IU X-Ray, MEDIQA-2021 RRS | ~3.9k / ~2.4k | open |
| Train/eval — question summarization | MeQSum, MEDIQA-2021 QS | 1k / 1k | open |
| Eval — multi-answer summarization | MEDIQA-2021 MAS | ~0.6k | open |
| Eval — consumer dialogue | MedDialog-EN | large | open |
| Verifier training | MedNLI (preferred), SciFact (fallback) | 14k / 5k | gated / open |
| **External validation** | MIMIC-IV-Note discharge summaries, MIMIC-CXR reports | 331k / 227k | PhysioNet credentialed |

Splits: use official splits where they exist (ACI-Bench, MTS-Dialog, MEDIQA, MeQSum). Otherwise
80/10/10 **grouped by document/patient id** — never random over sentences, or the eval leaks.

---

## 4. Baselines

Chosen so each row in the results table answers a row in the literature survey.

1. **Extractive** — LexRank, and Oracle-extractive (upper bound on copy-only factuality).
2. **Seq2seq pretrained** — BART-large-CNN, FLAN-T5-large, PEGASUS-PubMed (FLAN-T5 appears in [1]).
3. **Zero-shot LLM** — Llama-3.1-8B-Instruct, BioMistral-7B, no tuning.
4. **ICL LLM** — same models, 3-shot retrieval-selected exemplars (the [1]/[10]/[15] recipe).
5. **Plain QLoRA SFT** — *the primary comparison*: identical base model, identical data, no fact
   table, no ORPO, no verifier. Every gain must be shown against this, not against zero-shot.
6. **GPT-4o-mini / GPT-4.1-mini via API** — reference ceiling, budget-permitting (≤500 test items).
7. **FaCTS (ours)**, plus ablations.

---

## 5. Evaluation

### 5.1 Standard
ROUGE-1 / ROUGE-2 / ROUGE-Lsum (`rouge_score`, stemming on), BERTScore-F1 (`deberta-xlarge-mnli`,
rescaled with baseline), and length ratio |Ŷ|/|Y|.

### 5.2 Factuality — the metrics the project is actually judged on
| Metric | Definition | Direction |
|---|---|---|
| **HalluRate** | \|CUIs(Ŷ) \ CUIs(X)\| / \|CUIs(Ŷ)\| — fraction of summary concepts absent from the source | ↓ |
| **FactCoverage** | \|CUIs(Ŷ) ∩ CUIs(Y)\| / \|CUIs(Y)\| — critical concepts retained | ↑ |
| **MEDCON-F1** | UMLS concept F1 between Ŷ and Y, restricted to clinically relevant semantic types (as in ACI-Bench) | ↑ |
| **NegFlip** | rate of assertion-status mismatch on shared CUIs | ↓ |
| **NumErr** | rate of numeric value mismatch on shared measurement CUIs | ↓ |
| **SummaC-ZS / mean entailment** | NLI-based consistency score over source | ↑ |

HalluRate and NegFlip are the headline numbers: they are what the report promises to improve, and
neither ROUGE nor BERTScore detects them.

### 5.3 Human evaluation (reader study)
50 test items, 2–3 evaluators (medical students / a clinician if reachable), blinded and shuffled
across systems. 5-point Likert on **completeness, correctness, conciseness** — the same three axes
used in [1] and [15], so the numbers are directly comparable to the published baseline. Report
Krippendorff's α. Additionally count *safety-critical errors* (an error that could change management)
per 100 summaries.

### 5.4 Ablations
| # | Variant | Question it answers |
|---|---|---|
| A0 | full FaCTS | — |
| A1 | − fact table (Stage 1 off) | does explicit grounding help, or is it just extra tokens? |
| A2 | − ORPO (SFT only) | does preference tuning on perturbed negatives move factuality? |
| A3 | − verifier/repair | how much of the gain is inference-time filtering vs. learned? |
| A4 | verifier without repair (flag-and-drop only) | is regeneration worth the latency? |
| A5 | τ ∈ {0.3, 0.5, 0.7, 0.9} | factuality/coverage trade-off curve |
| A6 | R ∈ {0, 1, 2, 3} | diminishing returns of the repair loop |
| A7 | base model swap (Llama-3.1-8B ↔ BioMistral-7B ↔ Qwen2.5-7B) | is the method model-agnostic? |
| A8 | 3B base (Llama-3.2-3B) | compute-constrained deployment viability |

### 5.5 External validation (G2)
Train on ACI-Bench + MTS-Dialog + Asclepius; test **zero-shot** on Open-i radiology and (if
credentialed) MIMIC-IV-Note. Report the degradation vs. in-domain. This single experiment is what
93% of the surveyed papers did not do.

---

## 6. Compute & schedule

| Job | Hardware | Time |
|---|---|---|
| CFE preprocessing (all corpora, cached) | CPU, 8 cores | 3–5 h one-off |
| SFT, 8B QLoRA, 4k ctx, 3 ep, ~40k pairs | 1× A100-40G / L4-22G | 6–10 h |
| ORPO, 1 ep, ~12k pairs | same | 2–3 h |
| Verifier DeBERTa-v3-base | 1× T4 | ~1 h |
| Full eval + ablations (9 configs × ~2k test) | 1× L4 | 8–12 h |

Fits Colab Pro / Kaggle (30 h/week T4·P100) with checkpointing to Drive. Fallbacks if GPU is short:
drop to Llama-3.2-3B, 2048 context, LoRA r=8, and subsample the training set to 15k pairs — the
ablation structure is unchanged.

**Milestones**
- **Now → 20.09.2026 (Review 2 / DA2):** the **plain QLoRA baseline only** (§4 row 5) —
  model selection, environment, 4-bit QLoRA SFT on ACI-Bench + MTS-Dialog + DialogueSOAP,
  greedy inference on the official test splits, adapter + config saved, predictions handed to
  the evaluation owner. Full procedure in `REVIEW2_BASELINE.md`. Stages 1–4, ORPO, the
  verifier and every ablation are explicitly *not* Review 2 work: the report defines the plain
  QLoRA model as the baseline, and Review 2 delivers that baseline.
- **20.09 → 20.10.2026 (Review 3 / DA3):** CFE cache → fact-conditioned SFT → verifier →
  ORPO → ablations A1–A8, external validation, reader study, Gradio demo, IEEE paper draft.
  Reuses the Review 2 data mix, base model and LoRA hyper-parameters unchanged so every
  ablation differs from the baseline by exactly one component.

---

## 7. Risks and fallbacks

| Risk | Mitigation |
|---|---|
| PhysioNet credentialing (CITI course + DUA) takes weeks | Start it immediately; the entire core pipeline runs on open corpora, so MIMIC is upside for §5.5, not a dependency |
| Llama-3.1 licence gate on HF | BioMistral-7B and Qwen2.5-7B are ungated and are already in the ablation grid |
| UMLS licence needed for QuickUMLS/MEDCON | scispaCy's bundled UMLS linker KB needs no licence; MEDCON-F1 computed from scispaCy CUIs instead |
| scispaCy linking is noisy → noisy fact table | Threshold at 0.80, restrict to clinical semantic types, and measure CFE precision on 100 hand-checked notes; report it as a known error source |
| Verifier itself hallucinates (NLI models are imperfect) | Report verifier accuracy on a held-out perturbation set; keep flag-and-drop (A4) as the conservative mode |
| No clinician available for §5.3 | Pre-register the rubric, use 2 senior medical students, report α; state the limitation rather than dropping the study |
| GPU quota exhausted | 3B fallback config above |

---

## 8. Repository layout

```
medsum-fact/
├── MODEL_PLAN.md            ← this file (Review 3 design)
├── REVIEW2_BASELINE.md      ← Review 2 baseline workflow
├── README.md
├── requirements.txt
├── scripts/
│   ├── download_datasets.py ← implemented
│   ├── import_datasets.py   ← implemented: raw → unified {source, target, meta} jsonl
│   └── make_baseline_split.py ← implemented: Review 2 train/val mix, leakage checks
├── kaggle/baseline/         ← implemented: Review 2 QLoRA baseline as a Kaggle kernel
├── src/
│   ├── train/                 Review 2: sft.py (plain QLoRA); Review 3: orpo.py, perturb.py
│   ├── infer/                 Review 2: generate.py → predictions jsonl (schema in REVIEW2_BASELINE.md §8.3)
│   ├── cfe/                   Review 3: Stage 1 fact extractor
│   ├── verify/                Review 3: retriever.py, nli.py, repair.py
│   ├── eval/                  evaluation owner: rouge_bertscore.py, factuality.py, run_eval.py
│   └── app/                   Review 3: gradio demo with provenance highlighting
├── outputs/                 ← git-ignored; adapters, checkpoints, predictions per run
└── data/
    ├── raw/                   downloader writes here
    ├── interim/               CFE cache (Review 3)
    └── processed/             unified jsonl + baseline_train/val.jsonl
```
