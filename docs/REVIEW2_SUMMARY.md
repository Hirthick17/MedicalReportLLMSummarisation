# FaCTS — Review 2 Summary: Data, Plain QLoRA Baseline, Preliminary Evaluation

Project: *Fact-Constrained, Traceable Summarization of clinical doctor–patient conversations*
(BCSE306L). Review 2 delivers the three foundations the report defines for the baseline stage; the
FaCTS model itself (fact-table conditioning, ORPO factuality preference training, verifier / repair)
is Review 3 and is deliberately not started.

| role | delivered | documentation |
|---|---|---|
| **Person 1 — data** | 3 corpora inspected and standardised (12,108 records); cleaning, duplicate / near-duplicate / leakage audit; train 4,265 / val 220 / test 770 with SHA-256 manifest; lengthy-conversation policy from a Llama-token audit; **rule-based clinical fact extractor** (symptoms, history, diagnosis, medications, dosages, investigations, treatment / follow-up, negation) and a facts dataset for every record | `docs/PERSON1_DATA_PIPELINE.md` |
| **Person 2 — model** | Llama-3.1-8B-Instruct selected; 4-bit NF4 QLoRA (r=16, 41.9 M trainable params) trained on Kaggle 2×T4 (332 steps, best eval loss 0.9555); 9 GPU / memory / pipeline issues solved; validation tests + zero-shot control; 770 test notes generated under two decoding configurations; adapter, checkpoints and full config saved and sha-pinned; handoff completed | `docs/PERSON2_MODEL_TRAINING.md`, `REVIEW2_BASELINE.md`, `STATUS.md` |
| **Person 3 — evaluation** | ROUGE-1/2/L/Lsum, BERTScore; factuality checker for the six error types of the report; hallucination rate, negation-flip rate, numerical consistency, clinical-information coverage; tables, figures, example errors; preliminary results and conclusions | `docs/PERSON3_EVALUATION.md` |

Submission PDF: `reports/Review2_Documentation.pdf` (this summary + the three role documents + the
generated reports). Code: `src/cfe/`, `src/eval/`, `scripts/`, `kaggle/`; 22 unit tests pass.

## Headline numbers (plain QLoRA baseline, five official test splits pooled, n = 520, ×100)

| system | ROUGE-L ↑ | BERTScore ↑ | hallucination rate ↓ | negation-flip rate ↓ | numerical consistency ↑ | clinical coverage ↑ |
|---|---|---|---|---|---|---|
| **baseline, run 1 decoding (primary)** | **30.7** | ACI −1.8 / MTS 39 | **40.4** | **8.2** | **71.1** | **61.3** |
| baseline, run 3 decoding (anti-repetition) | 25.1 | ACI −15 / MTS 31 | 59.3 | 10.7 | 72.0 | 54.0 |
| baseline run 1, clean outputs only (n = 416) | 35.1 | — | 33.8 | 5.0 | 77.4 | 69.3 |
| zero-shot Llama-3.1-8B-Instruct, validation (n = 20) | 21.2 | 16.2 | 18.0 | 14.4 | 73.4 | 71.6 |

Per split (run 1): ACI-Bench full notes ROUGE-L 17.4–17.9 (72–78 % of outputs truncated),
MTS-Dialog sections 35.8 / 33.5, DialogueSOAP (run 3, synthetic) 29.7.

## Five findings the Review 3 design rests on

1. **The baseline writes sections well and full notes badly.** MTS-Dialog ROUGE-L (35.8 / 33.5) is in
   the range of published MEDIQA-Chat 2023 systems; ACI-Bench (17.4–17.9, published ~40–45) is dragged
   down by 72–78 % truncated outputs. On the clean ACI-Bench outputs ROUGE-L is 29.6–31.2 — the model can
   write the note but has not learnt to end it: only 67 of 4,265 training examples (1.6 %) are full notes
   and the best checkpoint is at 0.75 epoch. Fix for Review 3: up-weight ACI-Bench, complete the 2 epochs.
2. **Decoding heuristics trade repetition for hallucination.** Raising `repetition_penalty` to 1.2 and
   blocking repeated 6-grams removed the loops and made every metric worse (ACI-Bench hallucination
   55 → 78 %, ROUGE-L 17.9 → 11.4): the model replaced grounded repetition with invented findings.
   Repetition control is not a factuality tool; grounding must come from the input (the fact table).
3. **Fine-tuning made the model less faithful than the un-tuned base.** On the same validation items
   the zero-shot base hallucinates 18 % of entities and covers 72 % of reference facts; the adapter
   42–73 % and 40–50 %. The adapter learnt the *form* of a note faster than the discipline of writing only
   what was said — the exact gap that fact-conditioning and ORPO target. The zero-shot row stays as a
   control in every Review 3 table.
4. **Medications and investigations are the information the baseline loses** (coverage 40–48 % and
   30–37 % on ACI-Bench vs 55–59 % for symptoms); 23–27 of 40 ACI-Bench notes omit at least one
   medication the reference records, and numbers are unreliable (numerical consistency 55–61 % on
   ACI-Bench: invented lab values, changed durations).
5. **Standard and factuality metrics disagree by design**: ROUGE-L rewards a runaway symptom list
   that overlaps the reference vocabulary, the hallucination rate separates clean from degenerate
   outputs (39 % vs 90 %). Both are reported in every table; neither replaces the other.

## What the data work established

- Official splits kept; leakage check between the training mix and the 770 test items: 0 id overlap,
  0 exact dialogue overlap (3 recurring two-line MTS-Dialog exchanges dropped from train), 2 near-duplicate
  dialogues that reuse one MTS-Dialog conversation for another section target (flagged, not removed).
- 131 one-word MTS-Dialog targets (`None.`, `Noncontributory.`) identified and kept on purpose.
- Token-length audit with the training tokenizer: ACI-Bench prompt+note p99 = 4,129 tokens, so the
  4,096-token window drops exactly one training example; test prompts are never cut at inference.
- Fact extractor: 87.5 % fully-correct facts on a 40-fact manual sample (95 % correct entity + polarity),
  82–85 % of reference-note entities also found in the transcript, ~130 ms per encounter on CPU.

## Honest limitations

- Kaggle 2×T4: 1.24 of 2 planned epochs; one training run (a second would cost ~11 h of the 30 h/week quota).
- The factuality checker is lexicon-based (no UMLS); rates carry ±5 points of extraction noise and are
  *preliminary*. Human evaluation is Review 3.
- DialogueSOAP is synthetic and is reported, not headlined. The run-2 output (wrong adapter) is excluded.

## Reproduce everything (laptop CPU unless noted)

```bash
python scripts/import_datasets.py && python scripts/make_baseline_split.py
python scripts/audit_dataset.py                       # reports/data_audit/
python scripts/extract_clinical_facts.py              # data/processed/facts/
kaggle kernels push -p kaggle/baseline --accelerator NvidiaTeslaT4 && python scripts/fetch_kaggle_run.py   # GPU
python -m src.eval.run_eval --run outputs/kaggle_run1_old_decoding/outputs/baseline_qlora_llama31_8b --label run1_rep1.1 --bertscore
python -m src.eval.run_eval --run outputs/kaggle/outputs/baseline_qlora_llama31_8b --label run3_rep1.2_ngram6 --bertscore
python -m src.eval.run_eval --compare && python -m pytest tests -q
python scripts/build_docs_pdf.py                      # reports/Review2_Documentation.pdf
```
