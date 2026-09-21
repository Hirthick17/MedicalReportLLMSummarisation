#!/usr/bin/env python
"""
Review 2 plain-QLoRA baseline — Kaggle TRAINING kernel (kernel A of two).

Implements REVIEW2_BASELINE.md §3–§5 and the save step of §9:
  1. pin the training stack, detect GPU / dtype
  2. load base model in 4-bit NF4, attach LoRA r=16/alpha=32
  3. build chat-template prompts, tokenize with assistant-only labels
  4. train (Trainer, paged AdamW 8-bit, cosine, grad checkpointing) with a wall-clock guard
  5. save final/ (= best-eval checkpoint), trainer_state.json, train_summary.json, environment.txt

Generation (§7 checks, §8 test splits, training_config.json) lives in kaggle/infer/baseline_infer.py,
a second kernel that mounts this kernel's output via `kernel_sources`. Splitting gives each half
its own 12 h Kaggle budget: run 1 (17 Sep) trained for 7.5 h and was then killed by the cap
while still generating the last test split.

MODE is set below because Kaggle scripts take no arguments:
  "smoke" — 20 steps on the 64 longest examples (~15 min)
  "full"  — the real run (2 epochs ≈ 534 steps ≈ 12 h on 2x T4 at ~81 s/step; the guard stops earlier)
"""

# ---- run configuration ---------------------------------------------------------------
MODE = "full"                        # "smoke" | "full"
RUN_NAME = "baseline_qlora_llama31_8b"
MODEL_ID = "unsloth/Meta-Llama-3.1-8B-Instruct"   # ungated mirror of meta-llama/Llama-3.1-8B-Instruct
MAX_SEQ_LEN = 4096
EPOCHS = 2
LR = 2e-4
GRAD_ACCUM = 16
MAX_TRAIN_HOURS = 10.5               # graceful stop; leaves ~1 h of the 12 h cap for setup, the trailing eval and the save
SEED = 42

# ---- environment ----------------------------------------------------------------------
import os, sys, subprocess, json, time, math, re, hashlib, glob, random
# Kaggle's T4 option is 2x T4 (15 GB each). One T4 OOMs in backward at 4k tokens (smoke v4, 14 Sep),
# so the model is split across both GPUs (device_map="balanced"). Trainer detects a multi-device
# hf_device_map and runs naive pipeline parallelism instead of DataParallel.
os.environ["PYTORCH_CUDA_ALLOC_CONF"] = "expandable_segments:True"
os.environ["TOKENIZERS_PARALLELISM"] = "false"

# Kaggle's image (Py 3.12, torch cu128, triton 3) is newer than the pins in REVIEW2_BASELINE.md
# §2.3: bitsandbytes<=0.44 imports `triton.ops`, which no longer exists. Install current bnb/peft
# on top of the image and keep transformers on the 4.x API our code was written against.
import importlib.metadata as _md
try:
    _tf = _md.version("transformers")
except _md.PackageNotFoundError:
    _tf = "0"
# liger-kernel: fused linear cross-entropy so the [seq, 128k-vocab] logits are never materialised —
# without it an 8B Llama-3 at 4k tokens OOMs a 15 GB T4 inside the loss (smoke v3, 14 Sep).
PINS = ["bitsandbytes>=0.46", "peft>=0.14", "accelerate>=1.1", "rouge-score==0.1.2", "liger-kernel"]
if _tf.split(".")[0] != "4":
    PINS.append("transformers>=4.51,<5")
subprocess.run([sys.executable, "-m", "pip", "install", "-q", *PINS], check=True)

import torch, numpy as np
import transformers, peft, bitsandbytes
from transformers import (AutoModelForCausalLM, AutoTokenizer, BitsAndBytesConfig, Trainer,
                          TrainingArguments, DataCollatorForSeq2Seq, TrainerCallback, set_seed)
from peft import LoraConfig, get_peft_model, prepare_model_for_kbit_training, PeftModel
from rouge_score import rouge_scorer
try:
    import liger_kernel.transformers  # noqa: F401
    USE_LIGER = True
except Exception as _e:              # fall back to a context that fits without fused CE
    print(f"[env] liger-kernel unavailable ({_e}); falling back to MAX_SEQ_LEN=2048", flush=True)
    USE_LIGER = False
    MAX_SEQ_LEN = 2048

set_seed(SEED)
random.seed(SEED)
T0 = time.time()
N_GPU = torch.cuda.device_count()
GPU = f"{N_GPU}x {torch.cuda.get_device_name(0)}"
VRAM_GB = sum(torch.cuda.get_device_properties(i).total_memory for i in range(N_GPU)) / 2**30
DEVICE_MAP = "balanced" if N_GPU > 1 else {"": 0}
if N_GPU == 1 and MAX_SEQ_LEN > 3072:
    print("[env] single GPU: capping MAX_SEQ_LEN at 3072", flush=True)
    MAX_SEQ_LEN = 3072
BF16 = torch.cuda.get_device_capability(0)[0] >= 8   # native bf16 (Ampere+); T4 reports emulated support
COMPUTE_DTYPE = torch.bfloat16 if BF16 else torch.float16
print(f"[env] torch {torch.__version__} | transformers {transformers.__version__} | peft {peft.__version__} "
      f"| bnb {bitsandbytes.__version__}\n[env] GPU {GPU} {VRAM_GB:.1f} GB total | bf16={BF16} | liger={USE_LIGER} | device_map={DEVICE_MAP} "
      f"| max_seq_len={MAX_SEQ_LEN} | MODE={MODE}", flush=True)

_hits = glob.glob("/kaggle/input/**/baseline_train.jsonl", recursive=True)
if not _hits:
    for root, dirs, files in os.walk("/kaggle/input"):
        if root.count("/") <= 5:
            print(root, dirs[:10], files[:10])
    raise SystemExit("dataset not mounted: baseline_train.jsonl not found under /kaggle/input")
INPUT = os.path.dirname(_hits[0])
print(f"[env] dataset at {INPUT}", flush=True)
OUT = f"/kaggle/working/outputs/{RUN_NAME}" + ("_smoke" if MODE == "smoke" else "")
os.makedirs(OUT, exist_ok=True)
with open(f"{OUT}/environment.txt", "w") as fh:
    fh.write(subprocess.run([sys.executable, "-m", "pip", "freeze"], capture_output=True, text=True).stdout)


def log(msg):
    print(f"[{(time.time() - T0) / 60:6.1f} min] {msg}", flush=True)


def load_jsonl(path):
    with open(path, encoding="utf-8") as fh:
        return [json.loads(l) for l in fh if l.strip()]


def find_file(name):
    hits = glob.glob(f"{INPUT}/**/{name}", recursive=True)
    assert hits, f"{name} not found under {INPUT}"
    return hits[0]


# ---- data -----------------------------------------------------------------------------
train = load_jsonl(find_file("baseline_train.jsonl"))
val = load_jsonl(find_file("baseline_val.jsonl"))
manifest = json.load(open(find_file("train_manifest.json")))
log(f"data: train {len(train)} | val {len(val)} | mix {manifest['train']['mix']}")

# ---- prompts (REVIEW2_BASELINE.md §4.2) ------------------------------------------------
SYSTEM = ("You are a clinical documentation assistant. Given the transcript of a doctor-patient "
          "consultation, write the clinical note. Include only information stated in the transcript.")
MTS_SECTIONS = {
    "FAM/SOCHX": "FAMILY HISTORY / SOCIAL HISTORY", "GENHX": "HISTORY OF PRESENT ILLNESS",
    "PASTMEDICALHX": "PAST MEDICAL HISTORY", "CC": "CHIEF COMPLAINT", "PASTSURGICAL": "PAST SURGICAL HISTORY",
    "ALLERGY": "ALLERGIES", "ROS": "REVIEW OF SYSTEMS", "MEDICATIONS": "MEDICATIONS", "ASSESSMENT": "ASSESSMENT",
    "EXAM": "PHYSICAL EXAM", "DIAGNOSIS": "DIAGNOSIS", "DISPOSITION": "DISPOSITION", "PLAN": "PLAN",
    "EDCOURSE": "EMERGENCY DEPARTMENT COURSE", "IMMUNIZATIONS": "IMMUNIZATIONS", "IMAGING": "IMAGING",
    "GYNHX": "GYNECOLOGIC HISTORY", "PROCEDURES": "PROCEDURES", "OTHER_HISTORY": "OTHER HISTORY", "LABS": "LABS",
}
TASK = {
    "aci_bench": ("Write the complete clinical note for this encounter, using upper-case section headers such as "
                  "CHIEF COMPLAINT, HISTORY OF PRESENT ILLNESS, REVIEW OF SYSTEMS, PHYSICAL EXAM, RESULTS, "
                  "ASSESSMENT AND PLAN as applicable."),
    "dialogue_soap": ("Write a SOAP note with four paragraphs labelled S:, O:, A:, P: "
                      "(Subjective, Objective, Assessment, Plan)."),
    "mts_dialog": "Write the {section} section of the clinical note.",
}


def instruction(rec):
    if rec["dataset"] == "mts_dialog":
        code = rec["metadata"].get("section_header", "")
        return TASK["mts_dialog"].format(section=MTS_SECTIONS.get(code, code))
    return TASK[rec["dataset"]]


def prompt_messages(rec):
    return [{"role": "system", "content": SYSTEM},
            {"role": "user", "content": f"{instruction(rec)}\n\nTRANSCRIPT:\n{rec['source_dialogue']}"}]


# ---- tokenizer + masking (§4.4) -----------------------------------------------------------
tokenizer = AutoTokenizer.from_pretrained(MODEL_ID)
tokenizer.pad_token = tokenizer.eos_token
EOT = tokenizer.convert_tokens_to_ids("<|eot_id|>")
EOS_IDS = sorted({tokenizer.eos_token_id, EOT})


def encode(rec):
    prompt_ids = tokenizer.apply_chat_template(prompt_messages(rec), tokenize=True, add_generation_prompt=True)
    if not isinstance(prompt_ids, list):            # newer transformers may return a BatchEncoding
        prompt_ids = list(prompt_ids["input_ids"])
    target_ids = tokenizer(rec["target_summary"], add_special_tokens=False)["input_ids"] + [EOT]
    ids = prompt_ids + target_ids
    labels = [-100] * len(prompt_ids) + target_ids
    return {"input_ids": ids, "attention_mask": [1] * len(ids), "labels": labels,
            "n_prompt": len(prompt_ids), "n_target": len(target_ids)}


def tokenize_split(records, name):
    enc = [encode(r) for r in records]
    lengths = np.array([len(e["input_ids"]) for e in enc])
    keep = [e for e in enc if len(e["input_ids"]) <= MAX_SEQ_LEN]
    log(f"tokens[{name}] p50/p90/p99/max = {np.percentile(lengths, [50, 90, 99, 100]).astype(int).tolist()} "
        f"| prompt share {np.mean([e['n_prompt'] / len(e['input_ids']) for e in enc]):.2f} "
        f"| dropped > {MAX_SEQ_LEN}: {len(enc) - len(keep)}")
    return [{k: e[k] for k in ("input_ids", "attention_mask", "labels")} for e in keep]


if MODE == "smoke":
    train = sorted(train, key=lambda r: -len(r["source_dialogue"]))[:64]   # worst case first
    val = val[:8]
train_tok = tokenize_split(train, "train")
val_tok = tokenize_split(val, "val")

# masking proof: decode labels of the first example
_lab = [t for t in train_tok[0]["labels"] if t != -100]
log("label-decoding check (must be note only, ends with <|eot_id|>): " + repr(tokenizer.decode(_lab)[:160]) + " ... " + repr(tokenizer.decode(_lab)[-40:]))
assert _lab[-1] == EOT and "TRANSCRIPT:" not in tokenizer.decode(_lab), "loss mask leaks the prompt"

# ---- model (§3) ------------------------------------------------------------------------
if USE_LIGER:
    # Only the fused linear cross-entropy (memory). Liger's RoPE/RMSNorm/SwiGLU Triton kernels are
    # speed-only and launch on the *current* CUDA device, which breaks non-deterministically when the
    # model is split across GPUs (smoke v6, 14 Sep: "Pointer argument cannot be accessed from Triton").
    from liger_kernel.transformers import apply_liger_kernel_to_llama
    apply_liger_kernel_to_llama(rope=False, rms_norm=False, swiglu=False,
                                cross_entropy=False, fused_linear_cross_entropy=True)

bnb = BitsAndBytesConfig(load_in_4bit=True, bnb_4bit_quant_type="nf4", bnb_4bit_use_double_quant=True,
                         bnb_4bit_compute_dtype=COMPUTE_DTYPE)
model = AutoModelForCausalLM.from_pretrained(MODEL_ID, quantization_config=bnb, device_map=DEVICE_MAP,
                                             torch_dtype=COMPUTE_DTYPE, attn_implementation="sdpa")
model.config.use_cache = False
from collections import Counter as _Counter
log(f"device map (modules per device): {dict(_Counter(str(d) for d in model.hf_device_map.values()))}")
model = prepare_model_for_kbit_training(model, use_gradient_checkpointing=True,
                                        gradient_checkpointing_kwargs={"use_reentrant": False})
lora = LoraConfig(r=16, lora_alpha=32, lora_dropout=0.05, bias="none", task_type="CAUSAL_LM",
                  target_modules=["q_proj", "k_proj", "v_proj", "o_proj", "gate_proj", "up_proj", "down_proj"])
model = get_peft_model(model, lora)
trainable, total = model.get_nb_trainable_parameters()
log(f"model loaded | trainable {trainable/1e6:.1f}M / {total/1e9:.2f}B ({100*trainable/total:.2f}%) "
    f"| VRAM " + " + ".join(f"{torch.cuda.memory_allocated(i)/2**30:.1f}" for i in range(N_GPU)) + " GB")


# ---- training (§4.5, §5) ----------------------------------------------------------------
class WallClock(TrainerCallback):
    def on_step_end(self, args, state, control, **kw):
        if (time.time() - T0) / 3600 > MAX_TRAIN_HOURS:
            log(f"wall-clock guard hit at step {state.global_step}; stopping training gracefully")
            control.should_training_stop = True
            control.should_save = True
        return control


class PipelineTrainer(Trainer):
    """Model split across GPUs (naive pipeline). Two device fixes (smoke v5/v7, 14 Sep):
    - Trainer hands `num_items_in_batch` over as a tensor; accelerate's top-level AlignDevicesHook
      then moves every tensor kwarg to cuda:0, while the Liger loss runs on the lm_head GPU (cuda:1)
      -> 'Expected all tensors to be on the same device'. Passing it as a plain int sidesteps the hook.
    - Return the step loss on args.device so the running-loss accumulator never mixes devices.
    The fused-CE Triton kernel launches on the *current* CUDA device, so pin that to the lm_head GPU
    for the whole forward+backward."""
    @staticmethod
    def _head_device(model):
        return model.get_output_embeddings().weight.device

    def compute_loss(self, model, inputs, return_outputs=False, num_items_in_batch=None):
        if torch.is_tensor(num_items_in_batch):
            num_items_in_batch = int(num_items_in_batch.item())
        return super().compute_loss(model, inputs, return_outputs=return_outputs,
                                    num_items_in_batch=num_items_in_batch)

    def training_step(self, model, inputs, num_items_in_batch=None):
        with torch.cuda.device(self._head_device(model)):
            loss = super().training_step(model, inputs, num_items_in_batch)
        return loss.to(self.args.device) if torch.is_tensor(loss) else loss

    def prediction_step(self, model, inputs, prediction_loss_only, ignore_keys=None):
        with torch.cuda.device(self._head_device(model)):
            out = super().prediction_step(model, inputs, prediction_loss_only, ignore_keys=ignore_keys)
        loss, logits, labels = out
        return (loss.to(self.args.device) if torch.is_tensor(loss) else loss), logits, labels


steps_per_epoch = math.ceil(len(train_tok) / GRAD_ACCUM)
eval_every = 200 if MODE == "full" else 10   # 220-item eval ≈ 4.6 min on 2x T4
args = TrainingArguments(
    output_dir=f"{OUT}/checkpoints",
    per_device_train_batch_size=1, per_device_eval_batch_size=1,
    gradient_accumulation_steps=GRAD_ACCUM,
    num_train_epochs=EPOCHS, max_steps=20 if MODE == "smoke" else -1,
    learning_rate=LR, lr_scheduler_type="cosine", warmup_ratio=0.03,
    optim="paged_adamw_8bit", weight_decay=0.0, max_grad_norm=1.0,
    bf16=BF16, fp16=not BF16,
    gradient_checkpointing=True, gradient_checkpointing_kwargs={"use_reentrant": False},
    logging_steps=5 if MODE == "smoke" else 10,
    eval_strategy="steps", eval_steps=eval_every,
    save_strategy="steps", save_steps=eval_every, save_total_limit=2,
    load_best_model_at_end=True, metric_for_best_model="eval_loss", greater_is_better=False,
    group_by_length=True, dataloader_num_workers=2,
    use_liger_kernel=False,                  # applied manually above (fused CE only)
    report_to="none", seed=SEED, remove_unused_columns=False,
)
trainer = PipelineTrainer(model=model, args=args, train_dataset=train_tok, eval_dataset=val_tok,
                  data_collator=DataCollatorForSeq2Seq(tokenizer, padding=True, label_pad_token_id=-100,
                                                       pad_to_multiple_of=8),
                  callbacks=[WallClock()])
log(f"training: {len(train_tok)} ex x {EPOCHS} ep / accum {GRAD_ACCUM} = ~{steps_per_epoch * EPOCHS} steps "
    f"(max_steps={args.max_steps})")
train_result = trainer.train()
log(f"train done: {train_result.metrics}")
peak_gb = max(torch.cuda.max_memory_allocated(i) for i in range(N_GPU)) / 2**30

trainer.save_model(f"{OUT}/final")
tokenizer.save_pretrained(f"{OUT}/final")
trainer.state.save_to_json(f"{OUT}/trainer_state.json")
best = min((e for e in trainer.state.log_history if "eval_loss" in e), key=lambda e: e["eval_loss"], default={})
log(f"adapter saved | best eval_loss {best.get('eval_loss')} at step {best.get('step')} | peak VRAM {peak_gb:.1f} GB")

# ---- train_summary.json (§9, training half) ----------------------------------------------
# The inference kernel merges this with its decoding / validation results into training_config.json.
# final/ is the best-eval checkpoint (load_best_model_at_end), so record which step that was.
summary = {
    "run_name": RUN_NAME, "mode": MODE, "system": "baseline_qlora",
    "base_model": MODEL_ID, "base_model_note": "ungated mirror of meta-llama/Llama-3.1-8B-Instruct (Llama 3.1 Community Licence)",
    "quantization": {"load_in_4bit": True, "quant_type": "nf4", "double_quant": True, "compute_dtype": str(COMPUTE_DTYPE)},
    "lora": {"r": 16, "alpha": 32, "dropout": 0.05, "target_modules": lora.target_modules if isinstance(lora.target_modules, list) else sorted(lora.target_modules),
             "trainable_params": trainable, "total_params": total},
    "data": {"train": "baseline_train.jsonl", "val": "baseline_val.jsonl", "manifest": manifest,
             "n_train_used": len(train_tok), "n_val_used": len(val_tok), "max_seq_length": MAX_SEQ_LEN},
    "prompt": {"system": SYSTEM, "task_instruction": TASK, "mts_section_names": MTS_SECTIONS, "loss_on": "assistant_only"},
    "training": {"liger_fused_ce": USE_LIGER, "batch_size": 1, "grad_accum": GRAD_ACCUM, "epochs": EPOCHS, "max_steps": args.max_steps, "lr": LR,
                 "scheduler": "cosine", "warmup_ratio": 0.03, "optim": "paged_adamw_8bit", "seed": SEED,
                 "eval_every": eval_every, "planned_steps": steps_per_epoch * EPOCHS,
                 "steps_completed": trainer.state.global_step, "epochs_completed": round(trainer.state.epoch or 0, 3),
                 "best_step": best.get("step"), "best_eval_loss": best.get("eval_loss"),
                 "final_train_loss": train_result.metrics.get("train_loss"),
                 "train_runtime_h": round(train_result.metrics.get("train_runtime", 0) / 3600, 2),
                 "sec_per_step": round(train_result.metrics.get("train_runtime", 0) / max(1, trainer.state.global_step), 1),
                 "wall_clock_guard_hours": MAX_TRAIN_HOURS,
                 "wall_clock_guard_hit": trainer.state.global_step < trainer.state.max_steps},
    "hardware": {"gpu": GPU, "n_gpu": N_GPU, "device_map": str(DEVICE_MAP), "vram_gb_total": round(VRAM_GB, 1),
                 "peak_vram_gb_per_gpu": round(peak_gb, 2),
                 "wall_time_h": round((time.time() - T0) / 3600, 2)},
    "versions": {"torch": torch.__version__, "transformers": transformers.__version__, "peft": peft.__version__,
                 "bitsandbytes": bitsandbytes.__version__, "python": sys.version.split()[0]},
    "adapter_sha256": hashlib.sha256(open(f"{OUT}/final/adapter_model.safetensors", "rb").read()).hexdigest(),
}
json.dump(summary, open(f"{OUT}/train_summary.json", "w"), indent=2, default=str)

# Checkpoints stay (best + last, ~260 MB each): the last one carries optimizer/scheduler/rng state, so a
# follow-up kernel can `trainer.train(resume_from_checkpoint=...)` if the guard stopped this run early.
log(f"DONE -> {OUT}")
print(json.dumps({k: summary[k] for k in ("training", "hardware")}, indent=2, default=str))
