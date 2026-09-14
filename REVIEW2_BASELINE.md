# Review 2 — Plain QLoRA Baseline: End-to-End Workflow

Owner: model-training role (Person 2). Scope: **Review 2 / DA2 only.**

The project report defines the *plain QLoRA fine-tune of the base LLM* as the experimental
baseline — no fact table, no ORPO, no verifier, no provenance. This document is the complete
procedure for producing that baseline and handing its outputs to the evaluation owner
(Person 3). Everything FaCTS-specific (Stages 1–4 of `MODEL_PLAN.md`) is **Review 3** and is
deliberately not covered here.

Sections map one-to-one onto the ten Review 2 tasks:

| # | Task | Section |
|---|---|---|
| 1 | Select the open-source LLM | §1 |
| 2 | Set up the Python / Hugging Face / PyTorch environment | §2 |
| 3 | Set up 4-bit QLoRA | §3 |
| 4 | Prepare the model-training pipeline | §4 |
| 5 | Fine-tune the plain baseline LLM | §5 |
| 6 | Solve model / GPU / memory / training issues | §6 |
| 7 | Test the trained model | §7 |
| 8 | Generate summaries from unseen test conversations | §8 |
| 9 | Save the adapter and training configuration | §9 |
| 10 | Hand baseline outputs to Person 3 | §10 |

Facts used below were measured on this repository on 2026-09-14
(`python scripts/import_datasets.py --validate-only`, `nvidia-smi`).

---

## 0. Scope boundary and inputs

**In scope (Review 2):** dialogue → clinical note, one instruction-tuned decoder LLM, 4-bit
QLoRA SFT, greedy inference on the held-out test splits, adapter + config saved, predictions
delivered in a fixed schema.

**Out of scope (Review 3):** clinical fact extraction, fact-table prompting, ORPO/DPO,
NLI verification and repair, provenance, Gradio demo, ablations A1–A8, external validation.

**Inputs already in place:**

| Corpus | train | val | test | avg dialogue words | avg note words | Role in the baseline |
|---|---|---|---|---|---|---|
| ACI-Bench | 67 | 20 | 40 + 40 + 40 | ~1,300 | ~420 | **Primary target task** (full encounter → SOAP note). Headline test set. |
| MTS-Dialog | 1,201 | 100 | 200 + 200 | ~100 | ~40 | Section-level supervision; second test set. |
| DialogueSOAP | 9,250 | 500 | 250 | ~415 | ~246 | **Training volume only.** Synthetic (LLM-generated); the report forbids using it as the sole basis of evaluation. Its test split is reported but is *not* a headline number. |

Raw data: `data/raw/` (downloaded, manifest in `data/MANIFEST.json`).
Unified jsonl: produced by `scripts/import_datasets.py` into `data/processed/<dataset>/<split>.jsonl`
with fields `id, dataset, split, source_dialogue, target_summary, metadata`.

---

## 1. Model selection

**Decision: `meta-llama/Llama-3.1-8B-Instruct` is the baseline. `BioMistral/BioMistral-7B` is the
fallback, triggered by a single rule (below).**

| Criterion | Llama-3.1-8B-Instruct | BioMistral-7B |
|---|---|---|
| Instruction tuning | Yes — native chat template, follows "write a SOAP note with sections S/O/A/P" reliably | Continued pre-training of Mistral-7B-Instruct-v0.1 on PubMed Central; weaker instruction following, older chat format |
| Context window | 128k (we use 4,096) | 8k sliding-window (fine for our lengths) |
| Domain knowledge | General; clinical vocabulary is adequate for note-writing | Biomedical literature — helps terminology, does not help dialogue → note structure |
| Fits T4 (15 GB) in 4-bit | Yes (~5.7 GB weights) | Yes (~4.5 GB weights) |
| Licence / access | Llama 3.1 Community Licence, **gated on HF** — must accept once, then use an `HF_TOKEN` | Apache 2.0, **ungated**, zero friction |
| Lineage in our survey | Llama family is the open-source line in [1][10][15]; ACI-Bench/MTS-Dialog work uses Llama-class models | Not used by any surveyed paper |
| Role in MODEL_PLAN | Primary base for Stage 2 | Ablation A7 (base-model swap) |

Why Llama wins for a *baseline*: the baseline's job is to be the strongest fair comparison for
the FaCTS model in Review 3. The Review 3 model will be built on the same base, so the base
should be the one with the best instruction following and the same tokenizer/template we will
use later. Domain pre-training (BioMistral's advantage) is exactly what the Review 3 fact table
is meant to supply explicitly — using it in the baseline would blur the ablation.

**Access (resolved 2026-09-14):** `meta-llama/Llama-3.1-8B-Instruct` is manually gated on HF and
the team has no HF token. `unsloth/Meta-Llama-3.1-8B-Instruct` is an **ungated mirror of the
identical weights**, redistributed under the Llama 3.1 Community Licence — verified via the HF
API (`gated: false`, chat template present). The kernel uses that repo id; `training_config.json`
records it with a note. No BioMistral fallback was needed. (If the mirror ever disappears,
BioMistral-7B remains the fallback; every step below is model-agnostic except the chat template
in §4.2.)

**Compute-shortfall fallback:** `meta-llama/Llama-3.2-3B-Instruct` (same template, same
tokenizer family, ~2.2 GB in 4-bit) if the 8B run cannot finish inside the available GPU quota.
This is MODEL_PLAN ablation A8, so the run is not wasted.

---

## 2. Environment

### 2.1 Where things run

| Machine | Spec (measured) | Use it for |
|---|---|---|
| Local laptop | RTX 2050, **4 GB VRAM**, Python 3.13, `torch 2.11.0+cpu`, no transformers/peft/trl/bitsandbytes | Data preparation, token-length audit, reading outputs. **Not** training or 8B inference. |
| Google Colab (free) | T4 16 GB, fp16 only, ~12 h session cap, quota varies | Pilot runs, small-subset training |
| Google Colab Pro | L4 24 GB (bf16) or A100 40 GB | Full baseline run |
| Kaggle | T4 ×2 or P100 16 GB, 30 GPU-h/week | Alternative to Colab; same notebook |

Working files (adapter, checkpoints, predictions) are written to Google Drive under
`MyDrive/medsum-fact/outputs/` so a session disconnect loses at most one checkpoint interval.

### 2.2 Local (data preparation only)

```bash
cd medsum-fact
python scripts/import_datasets.py            # data/raw/ -> data/processed/<dataset>/<split>.jsonl
python scripts/make_baseline_split.py        # -> baseline_train.jsonl, baseline_val.jsonl, train_manifest.json
```

`make_baseline_split.py` builds the §4.1 mix with seed 42, runs the leakage checks, and writes
SHA-256s. Result on 2026-09-14: **4,265 train / 220 val**; 3 MTS-Dialog train rows were dropped
because their two-line dialogue ("any known drug allergies? / No.") recurs verbatim in the
official test set — recorded in `train_manifest.json` under
`dropped_for_verbatim_overlap_with_test`.

### 2.2a Kaggle execution (the path actually used)

Kaggle is driven headlessly from the local terminal with the official CLI — no browser, no
Colab. One-time setup: an API token from kaggle.com/settings stored at
`~/.kaggle/access_token`; phone verification on the account for GPU access.

```
kaggle/
├── dataset/                       # -> private dataset hirthick17/medsum-fact-processed (~21 MB)
│   ├── dataset-metadata.json
│   ├── baseline_train.jsonl, baseline_val.jsonl, train_manifest.json
│   └── test/<dataset>_<split>.jsonl        (the six official test splits)
└── baseline/
    ├── kernel-metadata.json       # id hirthick17/medsum-baseline-qlora, GPU on, internet on
    └── baseline_qlora.py          # the whole §3–§9 pipeline as one Kaggle script
```

```bash
cd kaggle/dataset  && kaggle datasets create -p . --dir-mode zip     # first time
cd kaggle/dataset  && kaggle datasets version -p . --dir-mode zip -m "msg"   # after re-splitting
cd kaggle/baseline && kaggle kernels push -p . --accelerator NvidiaTeslaT4   # run (MODE set in the script)
kaggle kernels status hirthick17/medsum-baseline-qlora
kaggle kernels output hirthick17/medsum-baseline-qlora -p ../../outputs/kaggle   # logs + files
```

`baseline_qlora.py` has a `MODE` constant: `"smoke"` (20 steps on the 64 longest examples, then
a few generations — validates memory at the true worst case) and `"full"`. It tokenizes and
masks labels itself and uses the plain `transformers.Trainer`, so `trl` is not a dependency.
It forces `CUDA_VISIBLE_DEVICES=0` (Kaggle's 2×T4 would otherwise make `Trainer` wrap the 4-bit
model in `DataParallel`) and stops training gracefully at 7.5 h so inference and saving always
finish inside Kaggle's 12 h cap. Everything lands in `/kaggle/working/outputs/<run>/` in the §9
layout.

### 2.3 Colab / Kaggle training environment

Pin versions. The `trl` and `transformers` APIs move quickly and most "it worked yesterday"
failures are version drift.

```bash
pip install -q -U "torch>=2.4" --index-url https://download.pytorch.org/whl/cu121
pip install -q \
  transformers==4.46.3 \
  peft==0.13.2 \
  trl==0.12.1 \
  bitsandbytes==0.44.1 \
  accelerate==1.1.1 \
  datasets==3.1.0 \
  sentencepiece \
  rouge-score \
  huggingface_hub
```

Verify before doing anything else:

```python
import torch, transformers, peft, trl, bitsandbytes
print(torch.__version__, torch.cuda.is_available(), torch.cuda.get_device_name(0))
print(torch.cuda.get_device_properties(0).total_memory / 2**30, "GB")
print("bf16 supported:", torch.cuda.is_bf16_supported())
```

`bf16 supported: False` means T4/P100 → use fp16 compute (§3). `True` means L4/A100 → bf16.

### 2.4 Hugging Face access

```python
from huggingface_hub import login
login()   # paste HF_TOKEN; never hard-code it in the notebook
```

Store the token in Colab *Secrets* (key icon in the sidebar) as `HF_TOKEN` and read it with
`userdata.get("HF_TOKEN")`. Tokens must never be committed — `.gitignore` already excludes
`.env` and `*.token`.

### 2.5 Reproducibility

- `transformers.set_seed(42)` at the top of every notebook.
- `pip freeze > outputs/<run>/environment.txt` after installation.
- Record GPU name and total memory in `training_config.json`.

---

## 3. 4-bit QLoRA setup

### 3.1 Quantization

```python
from transformers import BitsAndBytesConfig
import torch

compute_dtype = torch.bfloat16 if torch.cuda.is_bf16_supported() else torch.float16

bnb_config = BitsAndBytesConfig(
    load_in_4bit=True,
    bnb_4bit_quant_type="nf4",          # NormalFloat4 — the QLoRA paper's data type
    bnb_4bit_use_double_quant=True,     # quantizes the quantization constants, saves ~0.4 GB
    bnb_4bit_compute_dtype=compute_dtype,
)
```

### 3.2 Model and tokenizer

```python
from transformers import AutoModelForCausalLM, AutoTokenizer
from peft import prepare_model_for_kbit_training

MODEL_ID = "meta-llama/Llama-3.1-8B-Instruct"

tokenizer = AutoTokenizer.from_pretrained(MODEL_ID)
tokenizer.pad_token = tokenizer.eos_token        # Llama has no pad token
tokenizer.padding_side = "right"                 # training; switch to "left" for batched generation

model = AutoModelForCausalLM.from_pretrained(
    MODEL_ID,
    quantization_config=bnb_config,
    device_map="auto",
    torch_dtype=compute_dtype,
    attn_implementation="sdpa",                  # flash-attn 2 if available on A100; sdpa is safe everywhere
)
model.config.use_cache = False                   # incompatible with gradient checkpointing
model = prepare_model_for_kbit_training(model, use_gradient_checkpointing=True)
```

### 3.3 LoRA adapter

```python
from peft import LoraConfig, get_peft_model

lora_config = LoraConfig(
    r=16,
    lora_alpha=32,
    lora_dropout=0.05,
    bias="none",
    task_type="CAUSAL_LM",
    target_modules=["q_proj", "k_proj", "v_proj", "o_proj",
                    "gate_proj", "up_proj", "down_proj"],
)
model = get_peft_model(model, lora_config)
model.print_trainable_parameters()
# expected: ~41.9M trainable / ~8.07B total (~0.52%) for Llama-3.1-8B
```

These values (r=16, α=32, all linear projections) are the QLoRA recipe used in [1][10][15], so
the baseline is like-for-like with the published numbers. They are also what `MODEL_PLAN.md`
Stage 2 specifies for the FaCTS model, which keeps the Review 3 comparison controlled.

### 3.4 Expected memory footprint (8B, 4-bit, 4,096 tokens, batch 1, grad checkpointing)

| Component | Approx. |
|---|---|
| Quantized transformer layers | 5.3 GB |
| `embed_tokens` + `lm_head` (128k vocab, **not** quantized, fp16) | 2.1 GB |
| LoRA params + 8-bit paged AdamW state | 0.3 GB |
| Activations (checkpointed) | 3–5 GB |
| **Logits + loss copy** at 4k tokens: 4096 × 128 256 × (fp16 + fp32 + shifted copy) | **~4 GB** ← the item the original estimate missed |
| CUDA context + fragmentation | 0.5–1 GB |
| **Total** | **~15–17 GB naive → OOM on a T4** (measured 14 Sep: 7.4 GB after load, OOM at 13.7 GB inside `cross_entropy`) |

The logits term is the Llama-3 128k-vocabulary tax and is the single largest allocation at
training time. The fix is a fused linear-cross-entropy that never materialises `[seq, vocab]`
(`liger-kernel`; `TrainingArguments(use_liger_kernel=True)` — `Trainer` patches the PEFT base
model itself). With it the T4 budget is ~10–12 GB at 4,096 tokens. Without it, the T4 needs
`max_seq_length=2048`, which drops most ACI-Bench examples — unacceptable for the target task.
The kernel script enables Liger when importable and falls back to 2,048 otherwise.

---

## 4. Training pipeline

### 4.1 Data mix for the baseline

| Source | Records used | Reason |
|---|---|---|
| ACI-Bench train | all 67 | the target task |
| MTS-Dialog train | all 1,201 | cheap, in-domain section-writing supervision |
| DialogueSOAP train | **3,000 random (seed 42)** of 9,250 | enough volume to teach SOAP structure; the full 9,250 triples training time for little gain on a *baseline* and is synthetic |
| **Total** | **~4,270** | |

Validation: ACI-Bench val (20) + MTS-Dialog val (100) + DialogueSOAP val (100 random) = 220
items, evaluated by loss every `eval_steps`. Test splits are never touched before §8.

Persist the exact sample as `data/processed/baseline_train.jsonl` /
`baseline_val.jsonl` so Person 3 and Review 3 use the identical mix.

**Leakage checks before training** (report them in the notebook):

1. No `id` appears in more than one of train/val/test.
2. No `source_dialogue` string in test appears verbatim in train (exact match after whitespace
   normalization). ACI-Bench and MTS-Dialog share provenance (MEDIQA-Chat 2023), so this check
   is not optional.

### 4.2 Prompt format

One system instruction, the dialogue as the user turn, the note as the assistant turn, rendered
with the model's own chat template so train and inference tokenize identically.

```python
SYSTEM = (
    "You are a clinical documentation assistant. Given the transcript of a "
    "doctor-patient consultation, write the clinical note. Include only "
    "information stated in the transcript."
)

TASK_INSTRUCTION = {
    "aci_bench":     "Write a complete clinical note with the sections: HISTORY OF PRESENT ILLNESS, "
                     "PHYSICAL EXAM, RESULTS, ASSESSMENT AND PLAN.",
    "dialogue_soap": "Write a SOAP note with the sections: Subjective, Objective, Assessment, Plan.",
    "mts_dialog":    "Write the {section_header} section of the clinical note.",
}

def build_messages(rec):
    instr = TASK_INSTRUCTION[rec["dataset"]].format(**rec["metadata"])
    return [
        {"role": "system", "content": SYSTEM},
        {"role": "user",   "content": f"{instr}\n\nTRANSCRIPT:\n{rec['source_dialogue']}"},
        {"role": "assistant", "content": rec["target_summary"]},
    ]
```

`tokenizer.apply_chat_template(messages, tokenize=False)` produces the training string.
For BioMistral, the same function works — its tokenizer carries the Mistral `[INST]` template
(fold the system text into the user turn, since Mistral v0.1 has no system role).

The per-dataset instruction is the *only* thing that differs between corpora. Do not include
dataset names, fact tables, or few-shot examples — those are Review 3 variables.

### 4.3 Token-length audit (do this before training, on CPU if necessary)

```python
lengths = [len(tokenizer.apply_chat_template(build_messages(r), tokenize=True)) for r in train]
import numpy as np
print(np.percentile(lengths, [50, 90, 95, 99, 100]))
```

Expected for ACI-Bench: roughly 1.3–1.5 tokens per word → ~2,300–2,600 tokens per example,
p99 under 4,096. Set `max_seq_length` to cover p99; truncating an ACI-Bench note silently
teaches the model to stop early.

### 4.4 Loss masking

Train on **assistant tokens only**. With `trl==0.12` this is
`DataCollatorForCompletionOnlyLM(response_template="<|start_header_id|>assistant<|end_header_id|>", tokenizer=tokenizer)`
for Llama-3, or `response_template="[/INST]"` for BioMistral. Verify once by decoding a batch's
`labels` with `-100` stripped — it must show *only* the note, not the transcript.

This is not cosmetic: with ~2,000 prompt tokens per ~600 completion tokens, unmasked loss would
spend 77% of the gradient learning to reproduce the transcript.

### 4.5 Training arguments

```python
from trl import SFTConfig, SFTTrainer

args = SFTConfig(
    output_dir="/content/drive/MyDrive/medsum-fact/outputs/baseline_qlora_llama31_8b",
    max_seq_length=4096,
    per_device_train_batch_size=1,
    gradient_accumulation_steps=16,          # effective batch 16
    num_train_epochs=2,
    learning_rate=2e-4,
    lr_scheduler_type="cosine",
    warmup_ratio=0.03,
    optim="paged_adamw_8bit",
    bf16=torch.cuda.is_bf16_supported(),
    fp16=not torch.cuda.is_bf16_supported(),
    gradient_checkpointing=True,
    gradient_checkpointing_kwargs={"use_reentrant": False},
    logging_steps=10,
    eval_strategy="steps",
    eval_steps=100,
    save_strategy="steps",
    save_steps=100,
    save_total_limit=3,
    load_best_model_at_end=True,
    metric_for_best_model="eval_loss",
    group_by_length=True,                    # packs similar lengths → ~30% faster on mixed corpora
    report_to="none",
    seed=42,
)
```

`packing=False` — packing concatenates examples and breaks the completion-only mask.

### 4.6 Budget

~4,270 examples × 2 epochs ÷ 16 = **~535 optimizer steps**.

| GPU | s / example (typical for 8B 4-bit, 2–4k tokens) | Wall time for 2 epochs |
|---|---|---|
| T4 (fp16) | 4–6 s | 9–14 h → **split across two sessions with checkpoint resume, or drop to 1 epoch** |
| L4 (bf16) | 1.5–2.5 s | 3.5–6 h |
| A100-40G | 0.7–1.0 s | 1.7–2.4 h |

If only T4 is available, the sanctioned reduction is: 1 epoch, DialogueSOAP sample 1,500,
`max_seq_length=3072` — and say so in `training_config.json`. Do not silently change r, α, or
learning rate; those are the like-for-like knobs.

---

## 5. Fine-tuning procedure

1. Mount Drive, install (§2.3), log in (§2.4), `set_seed(42)`.
2. Load `baseline_train.jsonl` / `baseline_val.jsonl`, run the leakage checks (§4.1) and the
   token-length audit (§4.3). Paste both outputs into the notebook's markdown.
3. Build model + adapter (§3). Print trainable parameter count.
4. Build `SFTTrainer(model, args, train_dataset, eval_dataset, tokenizer, data_collator)`.
5. **Smoke test first**: `max_steps=20` on 64 examples. Confirm loss decreases from ~2.x and
   nothing OOMs at the longest example (sort the 64 by length descending so the first batch is
   the worst case). Delete that output dir.
6. Full run: `trainer.train()` — or `trainer.train(resume_from_checkpoint=True)` after a
   disconnect; the checkpoint in Drive carries optimizer and scheduler state.
7. Watch `train/loss` and `eval/loss` every 100 steps. Healthy: train loss ~1.4 → ~0.8,
   eval loss tracking within ~0.15 of train. Eval rising while train falls = overfitting the
   small ACI-Bench slice → stop and keep the best checkpoint (already automatic).
8. On completion `trainer.save_model()` saves only the adapter (§9).

Expected quality signal for a sane baseline on ACI-Bench dev: ROUGE-L in the low-to-mid 40s
(published LED / BART baselines on ACI-Bench sit around 40–45 ROUGE-L). Far below 30 means a
template, masking or truncation bug, not a model limitation.

---

## 6. Troubleshooting

| Symptom | Cause | Fix (in order) |
|---|---|---|
| **(hit 14 Sep, v1)** `Tesla P100 ... sm_60 is not compatible with the current PyTorch installation` | Kaggle's API default GPU is the P100, which its current torch build no longer supports | `kaggle kernels push -p . --accelerator NvidiaTeslaT4` — always pass the flag |
| **(hit 14 Sep, v3)** `torch.OutOfMemoryError ... Tried to allocate 1.92 GiB` with the traceback ending in `cross_entropy` | logits `[4096, 128256]` upcast to fp32 plus a shifted copy — see §3.4 | `use_liger_kernel=True` (fused linear CE). Only if Liger is unavailable: `max_seq_length` 3072 → 2048 |
| **(hit 14 Sep, v4)** with Liger, step 1 completes, then OOM in `backward` needing 1.25 GiB on one T4 | the 32 × 4096 × 4096 attention matrix (no flash-attention on sm75) on top of ~13 GB | split the model across Kaggle's **2× T4** with `device_map="balanced"` (~29 GB); `Trainer` sees a multi-device `hf_device_map` and runs naive pipeline parallelism. Single-GPU fallback in the script caps context at 3,072 |
| **(hit 14 Sep, v5)** `Expected all tensors to be on the same device ... cuda:1 and cuda:0` inside Liger's loss | with the model split, `Trainer` passes `num_items_in_batch` on `cuda:0` but `lm_head` (and the loss) is on `cuda:1` | `PipelineTrainer.compute_loss` moves the scalar to `model.get_output_embeddings().weight.device` |
| **(hit 14 Sep, v1)** `ModuleNotFoundError: No module named 'triton.ops'` on `import bitsandbytes` | `bitsandbytes==0.44.1` pinned per §2.3 predates Kaggle's Python 3.12 / CUDA 12.8 / triton 3 image | install `bitsandbytes>=0.46` and `peft>=0.14` on top of the image; cap `transformers<5` only if the image ships 5.x. The §2.3 pins are for Colab's older image; the script now chooses at runtime |
| `CUDA out of memory` at first step | sequence too long for the card | `max_seq_length` 4096 → 3072 → 2048; confirm `gradient_checkpointing=True`; set `PYTORCH_CUDA_ALLOC_CONF=expandable_segments:True`; last resort Llama-3.2-3B. (`gradient_accumulation_steps` does not change peak memory; batch size is already 1.) |
| OOM mid-run, not at step 0 | fragmentation or a rare long example | same env var; `torch.cuda.empty_cache()` in an eval callback; filter examples > `max_seq_length` instead of truncating |
| OOM during **eval** only | eval batch size larger than train | `per_device_eval_batch_size=1`; `eval_accumulation_steps=1` |
| `RuntimeError: expected scalar type BFloat16/Half` | bf16 requested on T4 | use the `is_bf16_supported()` switch in §3.1/§4.5 |
| Loss is `nan` after a few steps on T4 | fp16 overflow | `fp16=True` with `max_grad_norm=1.0` (default); lower lr to 1e-4; ensure `torch_dtype` matches `bnb_4bit_compute_dtype` |
| `ImportError: bitsandbytes ... CUDA` | wrong wheel or CPU torch | reinstall torch from the cu121 index first, then `bitsandbytes==0.44.1`; on Windows use WSL or Colab — this is why training is not local |
| `401` / `GatedRepoError` loading Llama | licence not accepted or token missing | accept on the model page, `login()` with a *read* token; after 24 h apply the fallback rule in §1 |
| Colab disconnects / "GPU quota exceeded" | session cap or free-tier quota | `resume_from_checkpoint=True`; `save_steps=100` ensures ≤ ~1 h lost; switch to Kaggle with the same notebook |
| Training is 3× slower than the table | attention fallback or no `group_by_length` | check `model.config._attn_implementation` is `sdpa`; confirm `group_by_length=True`; check the GPU is not shared |
| Generated notes stop after one section | truncated targets during training | re-run the token-length audit; raise `max_seq_length` or filter long examples |
| Generated notes repeat a sentence forever | no EOS learned | check `tokenizer.eos_token` is appended by the template and `labels` contain it; at inference set `eos_token_id=[128001, 128009]` for Llama-3 (`<\|end_of_text\|>`, `<\|eot_id\|>`) and `repetition_penalty=1.1` |
| Model echoes the transcript | loss masking not applied | inspect a batch's `labels` (§4.4); the collator `response_template` must match the template's exact header string |
| `trl` raises on `SFTConfig` / `DataCollatorForCompletionOnlyLM` | version drift | pin `trl==0.12.1`; newer trl replaced the collator with `completion_only_loss=True` in `SFTConfig` — either works, not both |
| `pad_token` warnings, attention mask all ones | pad = eos with right padding | fine for training; for **batched inference** set `padding_side="left"` |

---

## 7. Testing the trained model

Run all of these on the **validation** split before touching test data.

1. **Loss report**: final train loss, best eval loss, step at which it occurred (from
   `trainer_state.json`).
2. **Qualitative check**: generate for 5 ACI-Bench val + 5 MTS-Dialog val items, print
   prediction next to reference. Look for: all four sections present, no transcript echo,
   no repetition, terminates with EOS, no invented patient names/dates.
3. **Length ratio**: mean `len(pred)/len(ref)` in words. Expect 0.8–1.2. Outside that range is
   a decoding-length or truncation bug.
4. **Quick ROUGE-L on val** (`rouge_score`, stemming on) — not the official number, just a
   sanity gate: ACI-Bench val ≥ 35, MTS-Dialog val ≥ 30.
5. **Adapter reload test**: in a fresh process, load base + adapter from the saved directory
   and regenerate one val item; output must be identical to the in-session generation under
   greedy decoding. This proves §9 actually saved what was trained.
6. **Base-model control**: generate the same 5 items with the *unadapted* base model (zero-shot,
   same prompt). The fine-tuned output should be visibly more note-like and shorter. This is a
   free extra row for Person 3's table (baseline row 3 in `MODEL_PLAN.md` §4).

---

## 8. Generating summaries on unseen test conversations

### 8.1 Test sets

| Split file | n | Status in the results table |
|---|---|---|
| `aci_bench/test_taskB_1.jsonl` | 40 | headline |
| `aci_bench/test_taskC_2.jsonl` | 40 | headline |
| `aci_bench/test_taskC_3.jsonl` | 40 | headline |
| `mts_dialog/test_chat_2023.jsonl` | 200 | headline |
| `mts_dialog/test_sum_2023.jsonl` | 200 | headline |
| `dialogue_soap/test.jsonl` | 250 | reported, marked *synthetic* |

Total 770 generations.

### 8.2 Decoding

Greedy, deterministic — the baseline must be reproducible and Person 3 must be able to regenerate
it. No sampling, no temperature.

```python
gen_kwargs = dict(
    max_new_tokens=768,          # ACI-Bench notes ≈ 420 words ≈ 600 tokens; 768 leaves headroom
    do_sample=False,
    num_beams=1,
    repetition_penalty=1.1,
    eos_token_id=[tokenizer.eos_token_id, tokenizer.convert_tokens_to_ids("<|eot_id|>")],
    pad_token_id=tokenizer.eos_token_id,
)
```

`model.config.use_cache = True` for inference, `tokenizer.padding_side = "left"`, batch size 4
on L4/A100, 1–2 on T4. Prompt = §4.2 messages **without** the assistant turn, rendered with
`add_generation_prompt=True`. Strip everything after the first EOS. Estimated time: 770 items ×
~15 s on T4 ≈ 3 h; ~40 min on A100.

### 8.3 Output schema

One jsonl per test split in `outputs/<run>/predictions/`, one line per item:

```json
{
  "id": "aci_bench_test_taskB_1_D2N088",
  "dataset": "aci_bench",
  "split": "test_taskB_1",
  "source_dialogue": "...",
  "reference_summary": "...",
  "prediction": "...",
  "model": "meta-llama/Llama-3.1-8B-Instruct",
  "adapter": "baseline_qlora_llama31_8b/final",
  "system": "baseline_qlora",
  "decoding": {"max_new_tokens": 768, "do_sample": false, "repetition_penalty": 1.1},
  "prompt_tokens": 2311,
  "generated_tokens": 588,
  "truncated": false
}
```

`truncated` is `true` when `generated_tokens == max_new_tokens` — Person 3 needs it to exclude
or flag cut-off outputs. Keep `source_dialogue` and `reference_summary` in the file so the
evaluation is self-contained and never re-joins on ids.

Also produce `zeroshot_base/*.jsonl` with the same schema and `"system": "zeroshot_base"` from
§7 step 6 if time allows (770 more generations; only ACI-Bench + MTS-Dialog if it does not).

---

## 9. Saving the adapter and configuration

Directory layout, written to Drive and mirrored to the repo's `outputs/` (git-ignored):

```
outputs/baseline_qlora_llama31_8b/
├── final/                       # trainer.save_model() → adapter only, ~170 MB
│   ├── adapter_config.json
│   ├── adapter_model.safetensors
│   ├── tokenizer.json, tokenizer_config.json, special_tokens_map.json
│   └── README.md                # auto-generated model card; add the base model id
├── checkpoint-*/                # last 3, with optimizer state, for resume
├── training_config.json         # see below — the single source of truth
├── trainer_state.json           # loss curve, best step
├── environment.txt              # pip freeze
├── train_manifest.json          # sha256 of baseline_train/val.jsonl + counts per dataset
└── predictions/
    ├── baseline_qlora/{split}.jsonl
    └── zeroshot_base/{split}.jsonl
```

`training_config.json` — write it by hand from the actual objects, not from memory:

```json
{
  "run_name": "baseline_qlora_llama31_8b",
  "system": "baseline_qlora",
  "base_model": "meta-llama/Llama-3.1-8B-Instruct",
  "base_model_revision": "<commit sha from HF>",
  "quantization": {"load_in_4bit": true, "quant_type": "nf4", "double_quant": true, "compute_dtype": "bfloat16"},
  "lora": {"r": 16, "alpha": 32, "dropout": 0.05, "target_modules": ["q_proj","k_proj","v_proj","o_proj","gate_proj","up_proj","down_proj"], "trainable_params": 41943040},
  "data": {"train": "data/processed/baseline_train.jsonl", "val": "data/processed/baseline_val.jsonl",
           "mix": {"aci_bench": 67, "mts_dialog": 1201, "dialogue_soap": 3000}, "sample_seed": 42,
           "leakage_check": "passed"},
  "prompt": {"system": "...", "task_instruction": {"aci_bench": "...", "dialogue_soap": "...", "mts_dialog": "..."}, "loss_on": "assistant_only"},
  "training": {"max_seq_length": 4096, "batch_size": 1, "grad_accum": 16, "epochs": 2, "lr": 2e-4, "scheduler": "cosine", "warmup_ratio": 0.03, "optim": "paged_adamw_8bit", "seed": 42, "steps": 535, "best_step": 400, "best_eval_loss": 0.81},
  "hardware": {"gpu": "NVIDIA L4", "vram_gb": 22.5, "wall_time_h": 4.2},
  "decoding": {"max_new_tokens": 768, "do_sample": false, "repetition_penalty": 1.1},
  "versions": {"transformers": "4.46.3", "peft": "0.13.2", "trl": "0.12.1", "bitsandbytes": "0.44.1", "torch": "2.4.1+cu121"}
}
```

(The `steps`, `best_step`, `best_eval_loss`, `hardware` values above are placeholders — fill
them from `trainer_state.json` and `nvidia-smi` after the run.)

Optional: `model.push_to_hub("<user>/medsum-baseline-qlora-llama31-8b", private=True)` gives
Person 3 and Review 3 a stable download. Never push merged full weights of a gated base model.

**Do not** merge the adapter into the base weights for the deliverable. The merged 16 GB model is
not needed for evaluation and cannot be reloaded in 4-bit without re-quantizing.

---

## 10. Handoff to Person 3 (evaluation)

Deliver one folder — the `outputs/baseline_qlora_llama31_8b/` tree above — plus this checklist,
filled in:

```
HANDOFF — plain QLoRA baseline                                   date: ____-__-__
[ ] predictions/baseline_qlora/  6 files, 770 lines total, 0 JSON errors
[ ] predictions/zeroshot_base/   __ files (optional)
[ ] truncated == true count per split: ___ / ___ / ___ / ___ / ___ / ___
[ ] training_config.json present and matches trainer_state.json (steps, best_step)
[ ] train_manifest.json sha256 matches data/processed/baseline_{train,val}.jsonl
[ ] final/ adapter reloads and reproduces val item #0 byte-for-byte (§7 step 5)
[ ] no test id appears in baseline_train.jsonl or baseline_val.jsonl
[ ] environment.txt present
```

What Person 3 computes on these files (from the report's success criteria — all of it is their
scope, none of it is Review 2's): ROUGE-1/2/L, BERTScore, clinical-information coverage,
hallucination rate, negation-flip rate, numerical consistency, clinician-oriented assessment.
The schema in §8.3 is sufficient for every one of those; if Person 3 needs a column added, it
goes into `metadata`, not into a schema change.

What Review 3 consumes from this run: the same `baseline_train.jsonl` / `baseline_val.jsonl`
(identical data for the FaCTS model), the same base model and LoRA hyper-parameters, and the
`baseline_qlora` predictions as the comparison row in every results table.

---

## Appendix A — Six-day plan to DA2 (20 Sep 2026)

| Day | Do |
|---|---|
| 14 Sep | Request Llama-3.1 access. Run `import_datasets.py`. Write `baseline_train/val.jsonl`, leakage check, token audit. Upload to Drive. |
| 15 Sep | Colab: environment, model load, smoke test (§5 step 5). Decide Llama vs BioMistral by the 24 h rule. |
| 16 Sep | Full training run (L4/A100), checkpoints to Drive. |
| 17 Sep | Finish/resume training if needed. §7 tests on val. Fix any §6 issue. |
| 18 Sep | §8 generation on all six test splits (+ zero-shot base if time). Write `training_config.json`. |
| 19 Sep | §10 handoff to Person 3. Freeze `outputs/`. Write the Review 2 results section from Person 3's numbers. |
| 20 Sep | Buffer / submission. |

## Appendix B — Where this sits in the other documents

- `MODEL_PLAN.md` §4 baseline 5 ("Plain QLoRA SFT — the primary comparison") is this run.
- `MODEL_PLAN.md` §2 Stage 2 hyper-parameters are reused unchanged so ablations A2/A3 in
  Review 3 differ from this baseline by exactly one component each.
- The report's Feasibility Note names the fallback ladder used in §1 and §6 (shorter sequence,
  lower rank, smaller batch, subset, gradient checkpointing, smaller instruct model).
