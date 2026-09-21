# Person 2 — Plain QLoRA Baseline: Model Selection, Training, Inference, Handoff (Review 2)

Owner: model-training role. Scope: the **plain QLoRA baseline** only (the report defines this model
as the experimental baseline; FaCTS fact-conditioning, ORPO and the verifier are Review 3).

This document is the *record* of what was done and what came out. The full step-by-step procedure,
with code and the troubleshooting table, is `REVIEW2_BASELINE.md` (§1–§10); the run-by-run narrative
of what went wrong and how it was fixed is `STATUS.md`. Both are referenced by section below rather
than repeated.

| # | Task | Outcome | Where |
|---|---|---|---|
| 1 | Select the open-source LLM | Llama-3.1-8B-Instruct (ungated mirror `unsloth/Meta-Llama-3.1-8B-Instruct`); BioMistral-7B kept as fallback, not needed | §1, REVIEW2_BASELINE §1 |
| 2 | Python / HF / PyTorch environment | Kaggle 2×T4 driven headlessly from the laptop with the Kaggle CLI; versions pinned in `training_config.json` | §2, REVIEW2_BASELINE §2 |
| 3 | 4-bit QLoRA setup | NF4 + double-quant, fp16 compute (T4 has no bf16), LoRA r=16 α=32 on all 7 projections, 41.9 M trainable / 8.07 B (0.52%) | §3, REVIEW2_BASELINE §3 |
| 4 | Training pipeline | `kaggle/baseline/baseline_qlora.py`: chat-template prompts, assistant-only loss, length audit, leakage check, Liger fused cross-entropy, 2-GPU naive pipeline, wall-clock guard | §3, REVIEW2_BASELINE §4 |
| 5 | Fine-tune the baseline | 332 optimizer steps / 1.24 epochs on 4,265 examples, 7.5 h; best eval loss 0.9555 at step 200 → adapter `final/` (sha256 `14e71261…`) | §4 |
| 6 | Solve model / GPU / memory / training issues | 9 distinct issues hit and fixed (OOM in cross-entropy, OOM in backward, cross-device loss, P100 incompatibility, bitsandbytes/triton drift, 12-h cap, lost log, wrong adapter mounted, repetition loops) | §5, REVIEW2_BASELINE §6, STATUS |
| 7 | Test the trained model | validation checks in a fresh process (adapter reload = the test itself), zero-shot base control on the same items | §6 |
| 8 | Generate summaries for unseen test conversations | 770 predictions on the 6 official test splits, two decoding configurations (run 1, run 3) | §6–§7 |
| 9 | Save adapter + training configuration | `outputs/kaggle/outputs/baseline_qlora_llama31_8b/` (adapter, checkpoints 200/332, trainer_state, training_config, environments) + private Kaggle dataset `hirthick17/medsum-baseline-adapter` | §8 |
| 10 | Provide baseline outputs to Person 3 | handoff checklist filled in §9; evaluated in `docs/PERSON3_EVALUATION.md` | §9 |

---

## 1. Model selection

Decision table in `REVIEW2_BASELINE.md` §1. Summary of the reasoning:

- The baseline must be the *fairest possible comparison* for the Review 3 FaCTS model, which will be
  built on the same base. The base therefore has to be the one with the best instruction following and
  the tokenizer/chat template we will keep: **Llama-3.1-8B-Instruct**.
- BioMistral-7B's advantage (biomedical pre-training) is exactly the kind of knowledge the Review 3
  fact table supplies explicitly; using it in the baseline would confound the ablation. It remains
  the no-blocker fallback and ablation A7.
- Access: `meta-llama/Llama-3.1-8B-Instruct` is gated and the team had no approved token by the
  deadline. `unsloth/Meta-Llama-3.1-8B-Instruct` is a byte-identical, ungated redistribution under
  the Llama 3.1 Community Licence (verified through the HF API: `gated: false`, same chat template).
  `training_config.json` records this (`base_model_note`).

## 2. Environment

| where | spec | used for |
|---|---|---|
| laptop (Windows 11, RTX 2050 4 GB, Python 3.13, torch 2.11 CPU) | data prep, audits, fact extraction, evaluation, report building | everything that is not an 8B forward pass |
| Kaggle kernel A `hirthick17/medsum-baseline-qlora` | 2× Tesla T4 (2×15 GB, no bf16, no flash-attention), Python 3.12, torch 2.10+cu128, transformers 4.57, peft 0.19, bitsandbytes 0.50, liger-kernel | training |
| Kaggle kernel B `hirthick17/medsum-baseline-infer` | same hardware | validation checks + test-set generation |

Kaggle is driven from the terminal (`kaggle kernels push/status/output`, `scripts/fetch_kaggle_run.py`),
never from a browser, so every run is reproducible from the repository. The exact `pip freeze` of
each kernel is stored as `environment.txt` / `environment_infer.txt` next to the adapter.

## 3. QLoRA configuration and training pipeline (as run)

```
base           unsloth/Meta-Llama-3.1-8B-Instruct           quantization  NF4, double-quant, fp16 compute
LoRA           r=16, alpha=32, dropout=0.05                 targets       q,k,v,o,gate,up,down_proj
trainable      41,943,040 / 8,072,204,288  (0.52 %)          max_seq_len   4096 (1 of 4,265 examples dropped)
batch          1 × grad-accum 16 = 16 examples / step        epochs        2 planned = 534 steps
lr             2e-4, cosine, warmup 3 %                      optimizer     paged AdamW 8-bit
loss           assistant tokens only (prompt masked to -100), EOT appended
memory         Liger fused linear-cross-entropy (never materialises [4096 × 128,256] logits)
parallelism    device_map="balanced" over 2 T4 (naive pipeline; one T4 OOMs in backward at 4k tokens)
guard          stop gracefully at MAX_TRAIN_HOURS so eval + save always fit the 12 h kernel cap
seed           42 (data sampling, shuffling, trainer)
```

Data in: `baseline_train.jsonl` (4,265) / `baseline_val.jsonl` (220) with SHA-256 checked against
`train_manifest.json` inside the kernel; the leakage check and the token-length audit are re-run in
the kernel and their output is in the log. Prompt format (`REVIEW2_BASELINE.md` §4.2): one system
instruction, a per-corpus task instruction (`Write a complete clinical note with the sections …` /
`Write a SOAP note …` / `Write the {section_header} section …`), the transcript as the user turn, the
note as the assistant turn — rendered with the model's own chat template so training and inference
tokenise identically.

## 4. The training run

| | |
|---|---|
| kernel / date | `medsum-baseline-qlora`, 17 Sep 2026 22:12 IST → 18 Sep ~05:45 IST |
| steps | 332 of 534 planned (1.24 of 2 epochs); stopped by the 7.5 h wall-clock guard (81 s / step measured) |
| loss | train 0.73 (step 10) → 0.42–0.45 (steps 280–330), two spikes at steps 270 and 310 (long ACI-Bench examples, grad-norm 1.0); eval 1.118 (100) → **0.9555 (200)** → 0.9614 (300) |
| selected adapter | `final/` = checkpoint-200 (best eval loss); checkpoint-332 (last, with optimizer state) also kept |
| adapter sha256 | `14e712617f1456b669ef02e6c512e41464dbeee450bbed6245045cb568b69481` |
| eval loss rising after step 200 | the 67 ACI-Bench examples (1.6 % of the mix) are seen ~3× by step 300; train loss keeps falling while eval rises → mild over-fitting to the small full-note slice, hence best-checkpoint selection |

The loss curve is in `reports/baseline_qlora_llama31_8b/loss_curve.png` and the full training
report (auto-generated, with the §7 validation checks and a per-split table) in
`reports/baseline_qlora_llama31_8b/report.pdf`.

## 5. Issues solved

All nine are documented with symptom → cause → fix in `REVIEW2_BASELINE.md` §6 and dated in
`STATUS.md`. The ones that changed the design:

| issue | fix that is now in the code |
|---|---|
| OOM inside `cross_entropy` at 4k tokens (logits `[4096 × 128k]` in fp32 + shifted copy ≈ 4 GB) | Liger fused linear-CE (`use_liger_kernel`), the single biggest memory saving |
| OOM in backward on one T4 even with Liger (32 × 4k × 4k attention, no flash-attention on sm75) | split across 2 T4 (`device_map="balanced"`), `PipelineTrainer.compute_loss` moves the loss scalar to the `lm_head` device |
| one kernel cannot train (7.5 h) *and* generate (≈ 5 h) inside 12 h → run 1 killed mid-generation, log lost | training and generation are separate kernels; every stage of `fetch_kaggle_run.py` is idempotent |
| kernel B mounted the wrong (20-step smoke) adapter because Kaggle mounts the latest *completed* version of kernel A, and the full run was *cancelled* (run 2 evaluated it for 3.8 h without any check failing) | the adapter is uploaded as an explicit dataset; kernel B pins `EXPECTED_ADAPTER_SHA256` and exits in minute 1 otherwise; the fetch script and the report compare the sha before merging/reporting |
| run 1: 75 % of ACI-Bench notes hit `max_new_tokens=768` in "He has been having some difficulty with X." loops | run 3 decoding: `max_new_tokens=1024`, `repetition_penalty=1.2`, 6-gram block on *generated* tokens only (HF's `no_repeat_ngram_size` would also forbid copying "metformin 500 mg twice a day" from the transcript) |

## 6. Testing the trained model (validation split, 20 items: 10 ACI-Bench + 10 MTS-Dialog)

Kernel B loads base + adapter in a fresh process — this *is* the §7 adapter-reload test — verifies the
sha256, generates the 20 validation items with the adapter and again with the adapter disabled
(zero-shot base control), and writes `training_config.json`:

| system (run 3 decoding) | ROUGE-L ACI-Bench | ROUGE-L MTS-Dialog | length ratio | truncated / 20 |
|---|---|---|---|---|
| adapter (`final/`) | 10.5 | 18.8 | 1.29 | 9 |
| zero-shot base (same prompt) | 26.6 | 15.8 | 2.78 | 0 |

Interpretation: on short section tasks the adapter beats the un-tuned base; on full notes the
adapter is *worse than the base model under this decoding* and truncates half of the items. This
is the long-note failure analysed in §7 and in `docs/PERSON3_EVALUATION.md`.

## 7. Test-set generation and the decoding comparison

770 notes on the six official test splits, greedy, deterministic. Two configurations were run with
the **same adapter** (the run-2 output with the smoke adapter is excluded from every table):

| | run 1 (17 Sep, in-kernel) | run 3 (19 Sep, kernel B v2) |
|---|---|---|
| `max_new_tokens` | 768 | 1024 |
| `repetition_penalty` | 1.1 | 1.2 |
| n-gram block | none | 6-gram, generated tokens only |
| splits produced | 5 of 6 (DialogueSOAP lost to the 12 h cap) | 6 of 6 |
| ACI-Bench truncated | 30 / 29 / 31 of 40 | 29 / 28 / 27 of 40 |
| ACI-Bench failure mode | sentence-level **repetition loops** | **runaway comma lists** of hallucinated terms (ROS-style "denies A, B, C, …" that never ends) |
| MTS-Dialog truncated | 9 / 2 of 200 | 5 / 6 of 200 |
| DialogueSOAP truncated | — | 7 / 250 |

Run 1's predictions were recovered from the cancelled kernel's output
(`outputs/kaggle_run1_old_decoding/`) so that both configurations could be evaluated side by side;
the numbers are in `docs/PERSON3_EVALUATION.md` and `reports/eval_baseline/comparison.md`.

**Root cause of the ACI-Bench degeneration (why decoding alone cannot fix it).** The adapter was
selected at step 200 (0.75 epoch); only 67 of the 4,265 training examples (1.6 %) are full-length
notes, so the model has seen ~50 full-note endings. It writes correct openings (CC, HPI) and then does
not know how such a note ends; whatever the decoder forbids (exact loops at 1.1; repeated 6-grams at
1.2) it replaces with the nearest allowed continuation — a list of ever-new medical terms. The
zero-shot base model, which has *not* been pushed towards ROS-style enumeration by DialogueSOAP and
MTS-Dialog, terminates every note (0/20 truncated). Short outputs (MTS-Dialog sections, SOAP notes)
are unaffected because their endings are abundantly represented in training. A fourth generation run
with a milder penalty (1.05) was considered and deliberately **not** run: it would spend ~5 GPU-hours
on the symptom. The fix is a data-mix change (up-weight ACI-Bench, add its augmented variants, train
the full 2 epochs) and belongs to the Review 3 training run, where the fact table also constrains
what the model may enumerate.

## 8. Saved artefacts

```
outputs/kaggle/outputs/baseline_qlora_llama31_8b/
├── final/                       adapter (adapter_config.json, adapter_model.safetensors 168 MB, tokenizer, chat_template.jinja)
├── checkpoints/checkpoint-200/  = final/, with optimizer/scheduler/rng state (resumable)
├── checkpoints/checkpoint-332/  last step, resumable
├── trainer_state.json           loss curve, best step
├── training_config.json         single source of truth: base, quantization, LoRA, data manifest + SHA, training, hardware,
│                                versions (both kernels), decoding, validation checks (+ adapter sha256), per-split test stats
├── environment.txt / environment_infer.txt   pip freeze of kernel A / kernel B
└── predictions/
    ├── baseline_qlora/<split>.jsonl   six files, 770 lines, schema REVIEW2_BASELINE.md §8.3
    ├── val_check.jsonl                20 validation items, adapter
    └── zeroshot_base/val_check.jsonl  the same 20 items, adapter disabled
outputs/kaggle_run1_old_decoding/…/predictions/   run 1 (768 / 1.1), 5 splits + val_check, same schema
reports/baseline_qlora_llama31_8b/{report.pdf, metrics.json, loss_curve.png, training_config.json, trainer_state.json}
Kaggle: dataset hirthick17/medsum-baseline-adapter (final/ + trainer_state.json), private
```

The adapter is *not* merged into the base weights (a 16 GB artefact that cannot be reloaded in
4-bit without re-quantising); Person 3 and Review 3 reload base + adapter.

## 9. Handoff to Person 3 (filled in)

```
HANDOFF — plain QLoRA baseline                                   date: 2026-09-21
[x] predictions/baseline_qlora/  6 files, 770 lines total, 0 JSON errors
[x] predictions/zeroshot_base/   1 file (val_check, 20 lines)
[x] truncated == true per split: 29 / 28 / 27 / 5 / 6 / 7   (ACI B-1, C-2, C-3, MTS chat, MTS sum, SOAP)
[x] training_config.json present; steps_completed 332, best_step 200 match trainer_state.json
[x] train_manifest.json sha256 matches data/processed/baseline_{train,val}.jsonl   (audit: True / True)
[x] final/ adapter reloads in a fresh process (kernel B); sha256 14e71261… == adapter used for generation
[x] no test id appears in baseline_train.jsonl or baseline_val.jsonl                (audit: 0 / 0)
[x] environment.txt + environment_infer.txt present
[x] run 1 predictions (old decoding) recovered for the decoding comparison
[!] known: ACI-Bench outputs degenerate in ~70 % of items under both decodings — flagged per item
    (`truncated`, and `degenerate` in the evaluation) so Person 3 can report with and without them
```

## 10. Reproduce

```bash
kaggle kernels push -p kaggle/baseline --accelerator NvidiaTeslaT4     # kernel A: train (~11 h with the 10.5 h guard)
python scripts/fetch_kaggle_run.py                                      # wait, download, upload adapter dataset, push B, wait, download, verify sha, report
python scripts/fetch_kaggle_run.py --stage infer --no-wait              # re-download a finished kernel B run (what was done on 21 Sep)
python scripts/make_report.py --run outputs/kaggle/outputs/baseline_qlora_llama31_8b
```
