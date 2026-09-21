#!/usr/bin/env python
"""
Review 2 plain-QLoRA baseline — Kaggle INFERENCE kernel (kernel B of two).

Loads the trained adapter and implements REVIEW2_BASELINE.md §7–§9 on top of it:
  1. load base model in 4-bit NF4, attach the saved adapter (final/ = best-eval checkpoint)
     — this IS the §7 step 5 adapter-reload test: a fresh process, nothing from training in memory
  2. §7 checks on a val subset: length ratio, quick ROUGE-L gates, truncation, plus the
     §7 step 6 zero-shot base-model control on the same items
  3. §8 greedy generation on the six official test splits -> predictions jsonl (schema §8.3)
  4. training_config.json = train_summary.json (from kernel A) + decoding + validation checks

Why a second kernel: each Kaggle kernel gets 12 h. Run 1 (17 Sep) trained for 7.5 h and the
cap killed it mid-generation, so nothing after training survived. Here generation has its own
budget (~4 h for 770 items on 2x T4) and decoding can be re-tuned without retraining.

Where the adapter comes from — two sources, in this order:
  1. the dataset `hirthick17/medsum-baseline-adapter` (kernel-metadata.json `dataset_sources`):
     final/ + trainer_state.json of the 17 Sep run, uploaded from the laptop with
     `python scripts/fetch_kaggle_run.py --stage adapter`
  2. the training kernel's output mounted via `kernel_sources` (/kaggle/input/notebooks/...)
The mount alone was the run-2 mistake (18 Sep): Kaggle serves kernel A's latest *completed*
version, and the 17 Sep full run was CANCELLED by the 12 h cap, so the mount held the earlier
smoke run and 3.8 h of generation used a 20-step adapter. EXPECTED_ADAPTER_SHA256 below pins the
adapter this kernel is allowed to run; a mismatch or a *_smoke path in full mode stops the kernel
in the first minute instead of after four hours.

Decoding changes vs run 1 (REVIEW2_BASELINE.md §8.2): max_new_tokens 768 -> 1024 (ACI-Bench
references reach ~1,020 tokens; 768 clipped ~15 % of correct-length notes), repetition_penalty
1.1 -> 1.2 and a 6-gram repeat block applied to the *generated* tokens only (run 1: 75 % of
ACI-Bench outputs hit the cap in "He has been having some difficulty with ..." loops). HF's own
`no_repeat_ngram_size` would also forbid copying any 6-gram from the transcript, which a
clinical note legitimately does (drug, dose, frequency), so it is not used.

MODE is set below because Kaggle scripts take no arguments:
  "smoke" — 4 val items + 2 per test split (~15 min)
  "full"  — 20 val items + all 770 test items
"""

# ---- run configuration ---------------------------------------------------------------
MODE = "full"                        # "smoke" | "full"
RUN_NAME = "baseline_qlora_llama31_8b"
# sha256 of final/adapter_model.safetensors this kernel must run. 17 Sep run: 332 steps, best eval 0.9555 @ 200.
# None disables the pin (only for a fresh kernel-A run whose train_summary.json carries the sha instead).
EXPECTED_ADAPTER_SHA256 = "14e712617f1456b669ef02e6c512e41464dbeee450bbed6245045cb568b69481"
MODEL_ID = "unsloth/Meta-Llama-3.1-8B-Instruct"   # must match the training kernel
MAX_NEW_TOKENS = 1024
GEN_BATCH = 4
REPETITION_PENALTY = 1.2
NO_REPEAT_NGRAM = 6                  # on generated tokens only (see module docstring)
SEED = 42

# ---- environment ----------------------------------------------------------------------
import os, sys, subprocess, json, time, hashlib, glob, random, shutil
os.environ["PYTORCH_CUDA_ALLOC_CONF"] = "expandable_segments:True"
os.environ["TOKENIZERS_PARALLELISM"] = "false"

import importlib.metadata as _md
try:
    _tf = _md.version("transformers")
except _md.PackageNotFoundError:
    _tf = "0"
PINS = ["bitsandbytes>=0.46", "peft>=0.14", "accelerate>=1.1", "rouge-score==0.1.2"]
if _tf.split(".")[0] != "4":
    PINS.append("transformers>=4.51,<5")
subprocess.run([sys.executable, "-m", "pip", "install", "-q", *PINS], check=True)

import torch, numpy as np
import transformers, peft, bitsandbytes
from transformers import AutoModelForCausalLM, AutoTokenizer, BitsAndBytesConfig, set_seed
from transformers import LogitsProcessorList, NoRepeatNGramLogitsProcessor
from peft import PeftModel
from rouge_score import rouge_scorer

set_seed(SEED)
random.seed(SEED)

T0 = time.time()
N_GPU = torch.cuda.device_count()
GPU = f"{N_GPU}x {torch.cuda.get_device_name(0)}"
VRAM_GB = sum(torch.cuda.get_device_properties(i).total_memory for i in range(N_GPU)) / 2**30
DEVICE_MAP = "balanced" if N_GPU > 1 else {"": 0}
BF16 = torch.cuda.get_device_capability(0)[0] >= 8
COMPUTE_DTYPE = torch.bfloat16 if BF16 else torch.float16
print(f"[env] torch {torch.__version__} | transformers {transformers.__version__} | peft {peft.__version__} "
      f"| bnb {bitsandbytes.__version__}\n[env] GPU {GPU} {VRAM_GB:.1f} GB total | bf16={BF16} | device_map={DEVICE_MAP} | MODE={MODE}", flush=True)


def log(msg):
    print(f"[{(time.time() - T0) / 60:6.1f} min] {msg}", flush=True)


# ---- locate inputs: the dataset and the training kernel's output -----------------------------
def _first(pattern, what):
    hits = sorted(glob.glob(pattern, recursive=True))
    if not hits:
        for root, dirs, files in os.walk("/kaggle/input"):
            if root.count("/") <= 5:
                print(root, dirs[:10], files[:10])
        raise SystemExit(f"{what} not found: {pattern}")
    return hits[0]


INPUT = os.path.dirname(_first("/kaggle/input/**/baseline_val.jsonl", "dataset"))
# adapter: the uploaded dataset wins over the kernel_sources mount (see module docstring)
_adapters = sorted(glob.glob("/kaggle/input/datasets/**/final/adapter_config.json", recursive=True)) \
    or sorted(glob.glob("/kaggle/input/**/final/adapter_config.json", recursive=True))
if not _adapters:
    _first("/kaggle/input/**/final/adapter_config.json", "adapter (adapter dataset or training kernel output)")
ADAPTER = os.path.dirname(_adapters[0])
TRAIN_OUT = os.path.dirname(ADAPTER)                       # .../outputs/<run>/ (kernel A layout) or the dataset root
print(f"[env] dataset at {INPUT}\n[env] adapter at {ADAPTER}"
      + (f" (+{len(_adapters) - 1} other adapter(s) ignored)" if len(_adapters) > 1 else ""), flush=True)
if MODE == "full" and "_smoke" in ADAPTER:
    raise SystemExit(f"refusing to run MODE=full with a smoke adapter: {ADAPTER}")
_adapter_sha = hashlib.sha256(open(f"{ADAPTER}/adapter_model.safetensors", "rb").read()).hexdigest()
print(f"[env] adapter sha256 {_adapter_sha}", flush=True)
if EXPECTED_ADAPTER_SHA256 and _adapter_sha != EXPECTED_ADAPTER_SHA256:
    raise SystemExit(f"adapter sha256 {_adapter_sha[:16]} != EXPECTED_ADAPTER_SHA256 {EXPECTED_ADAPTER_SHA256[:16]}: wrong adapter "
                     f"mounted (run 2, 18 Sep: the kernel_sources mount served the smoke run). Fix the input or update the constant.")

OUT = f"/kaggle/working/outputs/{RUN_NAME}" + ("_smoke" if MODE == "smoke" else "")
os.makedirs(f"{OUT}/predictions/baseline_qlora", exist_ok=True)
os.makedirs(f"{OUT}/predictions/zeroshot_base", exist_ok=True)
with open(f"{OUT}/environment_infer.txt", "w") as fh:
    fh.write(subprocess.run([sys.executable, "-m", "pip", "freeze"], capture_output=True, text=True).stdout)
for name in ("trainer_state.json", "train_summary.json", "environment.txt"):   # keep the download self-contained
    if os.path.exists(f"{TRAIN_OUT}/{name}"):
        shutil.copy(f"{TRAIN_OUT}/{name}", f"{OUT}/{name}")

trainer_state = json.load(open(f"{TRAIN_OUT}/trainer_state.json")) if os.path.exists(f"{TRAIN_OUT}/trainer_state.json") else {}
train_summary = json.load(open(f"{TRAIN_OUT}/train_summary.json")) if os.path.exists(f"{TRAIN_OUT}/train_summary.json") else None
log(f"training kernel output: trainer_state={'yes' if trainer_state else 'no'} | train_summary={'yes' if train_summary else 'no (pre-split run)'}")


def load_jsonl(path):
    with open(path, encoding="utf-8") as fh:
        return [json.loads(l) for l in fh if l.strip()]


def find_file(name):
    hits = glob.glob(f"{INPUT}/**/{name}", recursive=True)
    assert hits, f"{name} not found under {INPUT}"
    return hits[0]


# ---- data -----------------------------------------------------------------------------
train = load_jsonl(find_file("baseline_train.jsonl"))       # only counted, never generated on
val = load_jsonl(find_file("baseline_val.jsonl"))
manifest = json.load(open(find_file("train_manifest.json")))
TEST_FILES = ["aci_bench_test_taskB_1", "aci_bench_test_taskC_2", "aci_bench_test_taskC_3",
              "mts_dialog_test_chat_2023", "mts_dialog_test_sum_2023", "dialogue_soap_test"]

# ---- prompts (REVIEW2_BASELINE.md §4.2) — must be byte-identical to the training kernel ------------
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
if train_summary:   # the model was trained on these exact strings; refuse to generate with drifted prompts
    assert train_summary["prompt"]["system"] == SYSTEM and train_summary["prompt"]["task_instruction"] == TASK \
        and train_summary["prompt"]["mts_section_names"] == MTS_SECTIONS, "prompt text differs from the training kernel"


def instruction(rec):
    if rec["dataset"] == "mts_dialog":
        code = rec["metadata"].get("section_header", "")
        return TASK["mts_dialog"].format(section=MTS_SECTIONS.get(code, code))
    return TASK[rec["dataset"]]


def prompt_messages(rec):
    return [{"role": "system", "content": SYSTEM},
            {"role": "user", "content": f"{instruction(rec)}\n\nTRANSCRIPT:\n{rec['source_dialogue']}"}]


# ---- model: fresh base + saved adapter (§7 step 5) ---------------------------------------------
tokenizer = AutoTokenizer.from_pretrained(ADAPTER)         # the tokenizer saved next to the adapter
tokenizer.pad_token = tokenizer.eos_token
tokenizer.padding_side = "left"
EOT = tokenizer.convert_tokens_to_ids("<|eot_id|>")
EOS_IDS = sorted({tokenizer.eos_token_id, EOT})

bnb = BitsAndBytesConfig(load_in_4bit=True, bnb_4bit_quant_type="nf4", bnb_4bit_use_double_quant=True,
                         bnb_4bit_compute_dtype=COMPUTE_DTYPE)
base = AutoModelForCausalLM.from_pretrained(MODEL_ID, quantization_config=bnb, device_map=DEVICE_MAP,
                                            torch_dtype=COMPUTE_DTYPE, attn_implementation="sdpa")
# prepare_model_for_kbit_training upcast the non-quantised params (embeddings, RMSNorm, lm_head) to fp32
# during training; do the same so the residual stream matches what the adapter was trained against.
for p_ in base.parameters():
    if p_.dtype in (torch.float16, torch.bfloat16):
        p_.data = p_.data.to(torch.float32)
model = PeftModel.from_pretrained(base, ADAPTER).eval()
model.config.use_cache = True
lora_params = sum(p.numel() for n, p in model.named_parameters() if "lora_" in n)
_, total_params = model.get_nb_trainable_parameters()
adapter_sha = _adapter_sha
log(f"model loaded | adapter params {lora_params/1e6:.1f}M / {total_params/1e9:.2f}B | adapter sha256 {adapter_sha[:16]} "
    f"| VRAM " + " + ".join(f"{torch.cuda.memory_allocated(i)/2**30:.1f}" for i in range(N_GPU)) + " GB")

# which training step is final/? (load_best_model_at_end -> the best-eval checkpoint)
best = min((e for e in trainer_state.get("log_history", []) if "eval_loss" in e), key=lambda e: e["eval_loss"], default={})
ckpt_shas = {os.path.basename(d): hashlib.sha256(open(f"{d}/adapter_model.safetensors", "rb").read()).hexdigest()
             for d in sorted(glob.glob(f"{TRAIN_OUT}/checkpoints/checkpoint-*")) if os.path.exists(f"{d}/adapter_model.safetensors")}
adapter_is = [k for k, v in ckpt_shas.items() if v == adapter_sha]
log(f"final/ adapter matches checkpoint(s) {adapter_is or 'none mounted'} | best eval step {best.get('step')} ({best.get('eval_loss')})")


# ---- generation (§8.2) ---------------------------------------------------------------------
class GeneratedNoRepeatNGram(NoRepeatNGramLogitsProcessor):
    """HF's processor scans the whole sequence, prompt included, so a note could never copy a 6-gram
    from the transcript. Only the generated part is checked here."""
    def __init__(self, n, prompt_len):
        super().__init__(n)
        self.prompt_len = prompt_len

    def __call__(self, input_ids, scores):
        return super().__call__(input_ids[:, self.prompt_len:], scores)


GEN = dict(max_new_tokens=MAX_NEW_TOKENS, do_sample=False, num_beams=1, repetition_penalty=REPETITION_PENALTY,
           eos_token_id=EOS_IDS, pad_token_id=tokenizer.eos_token_id)
DECODING = {"max_new_tokens": MAX_NEW_TOKENS, "do_sample": False, "num_beams": 1, "repetition_penalty": REPETITION_PENALTY,
            "no_repeat_ngram_size_generated_only": NO_REPEAT_NGRAM, "eos_token_id": EOS_IDS, "batch": GEN_BATCH,
            "adapter": "final", "non_quantised_params_fp32": True}


@torch.no_grad()
def generate(records, system_name, adapter_name):
    # longest prompts first: batches of similar length waste less padding and OOM, if at all, at the start
    order = sorted(range(len(records)), key=lambda i: -len(records[i]["source_dialogue"]))
    out = [None] * len(records)
    for b, i in enumerate(range(0, len(order), GEN_BATCH)):
        idx = order[i:i + GEN_BATCH]
        batch = [records[j] for j in idx]
        texts = [tokenizer.apply_chat_template(prompt_messages(r), tokenize=False, add_generation_prompt=True) for r in batch]
        enc = tokenizer(texts, return_tensors="pt", padding=True, add_special_tokens=False).to(model.device)
        procs = LogitsProcessorList([GeneratedNoRepeatNGram(NO_REPEAT_NGRAM, enc["input_ids"].shape[1])]) if NO_REPEAT_NGRAM else None
        gen = model.generate(**enc, logits_processor=procs, **GEN)
        for j, r, row, mask in zip(idx, batch, gen[:, enc["input_ids"].shape[1]:], enc["attention_mask"]):
            toks = row.tolist()
            cut = next((k for k, t in enumerate(toks) if t in EOS_IDS), len(toks))
            out[j] = {
                "id": r["id"], "dataset": r["dataset"], "split": r["split"],
                "source_dialogue": r["source_dialogue"], "reference_summary": r["target_summary"],
                "prediction": tokenizer.decode(toks[:cut], skip_special_tokens=True).strip(),
                "model": MODEL_ID, "adapter": adapter_name, "system": system_name,
                "decoding": {"max_new_tokens": MAX_NEW_TOKENS, "do_sample": False, "repetition_penalty": REPETITION_PENALTY,
                             "no_repeat_ngram_size_generated_only": NO_REPEAT_NGRAM},
                "prompt_tokens": int(mask.sum()), "generated_tokens": cut,
                "truncated": cut >= MAX_NEW_TOKENS,
            }
        if b % 10 == 0:
            log(f"  gen {system_name} {i + len(idx)}/{len(records)}")
    return out


def write_preds(preds, path):
    with open(path, "w", encoding="utf-8") as fh:
        for p in preds:
            fh.write(json.dumps(p, ensure_ascii=False) + "\n")


scorer = rouge_scorer.RougeScorer(["rougeL"], use_stemmer=True)


def checks(preds):
    by_ds = {}
    for ds in sorted({p["dataset"] for p in preds}):
        sub = [p for p in preds if p["dataset"] == ds]
        by_ds[ds] = round(float(np.mean([scorer.score(p["reference_summary"], p["prediction"])["rougeL"].fmeasure for p in sub])) * 100, 1)
    return {
        "n": len(preds),
        "rougeL_f": float(np.mean([scorer.score(p["reference_summary"], p["prediction"])["rougeL"].fmeasure for p in preds])),
        "rougeL_f_by_dataset_x100": by_ds,
        "length_ratio": float(np.mean([len(p["prediction"].split()) / max(1, len(p["reference_summary"].split())) for p in preds])),
        "truncated": sum(p["truncated"] for p in preds),
        "empty": sum(1 for p in preds if not p["prediction"]),
    }


# ---- §7 validation checks on the val subset ------------------------------------------------
val_subset = [r for r in val if r["dataset"] == "aci_bench"][:10] + [r for r in val if r["dataset"] == "mts_dialog"][:10]
if MODE == "smoke":
    val_subset = val_subset[:2] + val_subset[10:12]
val_preds = generate(val_subset, "baseline_qlora", f"{RUN_NAME}/final")
val_checks = checks(val_preds)
log(f"val checks (adapter): {val_checks}")
write_preds(val_preds, f"{OUT}/predictions/val_check.jsonl")
for p in val_preds[:2]:
    print("=" * 80, f"\n[{p['id']}] REFERENCE:\n{p['reference_summary'][:600]}\n--- PREDICTION:\n{p['prediction'][:600]}", flush=True)

# §7 step 6 — zero-shot base-model control on the same items (adapter switched off, same prompt, same decoding)
with model.disable_adapter():
    base_preds = generate(val_subset, "zeroshot_base", None)
base_checks = checks(base_preds)
log(f"val checks (zero-shot base): {base_checks}")
write_preds(base_preds, f"{OUT}/predictions/zeroshot_base/val_check.jsonl")

# ---- §8 test splits -------------------------------------------------------------------------
test_stats = {}
for name in TEST_FILES:
    recs = load_jsonl(find_file(f"{name}.jsonl"))
    if MODE == "smoke":
        recs = recs[:2]
    preds = generate(recs, "baseline_qlora", f"{RUN_NAME}/final")
    write_preds(preds, f"{OUT}/predictions/baseline_qlora/{name}.jsonl")   # written per split: partial progress survives a kill
    test_stats[name] = {"n": len(preds), "truncated": sum(p["truncated"] for p in preds),
                        "rougeL_x100": round(float(np.mean([scorer.score(p["reference_summary"], p["prediction"])["rougeL"].fmeasure for p in preds])) * 100, 1)}
    log(f"wrote {name}: {test_stats[name]}")

# ---- training_config.json (§9) -------------------------------------------------------------
if train_summary:
    config = dict(train_summary)
else:   # kernel A output from before the split: rebuild the training half from trainer_state + the known constants
    config = {
        "run_name": RUN_NAME, "mode": "full", "system": "baseline_qlora",
        "base_model": MODEL_ID, "base_model_note": "ungated mirror of meta-llama/Llama-3.1-8B-Instruct (Llama 3.1 Community Licence)",
        "quantization": {"load_in_4bit": True, "quant_type": "nf4", "double_quant": True, "compute_dtype": str(COMPUTE_DTYPE)},
        "lora": {"r": 16, "alpha": 32, "dropout": 0.05, "target_modules": ["q_proj", "k_proj", "v_proj", "o_proj", "gate_proj", "up_proj", "down_proj"],
                 "trainable_params": lora_params, "total_params": total_params},
        "data": {"train": "baseline_train.jsonl", "val": "baseline_val.jsonl", "manifest": manifest,
                 "n_train_used": len(train), "n_val_used": len(val), "max_seq_length": 4096},
        "prompt": {"system": SYSTEM, "task_instruction": TASK, "mts_section_names": MTS_SECTIONS, "loss_on": "assistant_only"},
        "training": {"liger_fused_ce": True, "batch_size": 1, "grad_accum": 16, "epochs": trainer_state.get("num_train_epochs"),
                     "max_steps": trainer_state.get("max_steps"), "lr": 2e-4, "scheduler": "cosine", "warmup_ratio": 0.03,
                     "optim": "paged_adamw_8bit", "seed": SEED, "eval_every": 100, "planned_steps": trainer_state.get("max_steps"),
                     "steps_completed": trainer_state.get("global_step"), "epochs_completed": round(trainer_state.get("epoch") or 0, 3),
                     "best_step": best.get("step"), "best_eval_loss": best.get("eval_loss"),
                     "final_train_loss": next((e.get("train_loss") for e in reversed(trainer_state.get("log_history", [])) if "train_loss" in e), None),
                     "train_runtime_h": round(next((e.get("train_runtime", 0) for e in reversed(trainer_state.get("log_history", [])) if "train_runtime" in e), 0) / 3600, 2),
                     "wall_clock_guard_hours": 7.5, "wall_clock_guard_hit": (trainer_state.get("global_step") or 0) < (trainer_state.get("max_steps") or 0),
                     "note": "train_summary.json absent: this adapter came from the single-kernel run of 17 Sep 2026 (killed by the 12 h cap after training)"},
        "hardware": {"gpu": GPU, "n_gpu": N_GPU, "device_map": str(DEVICE_MAP), "vram_gb_total": round(VRAM_GB, 1),
                     "peak_vram_gb_per_gpu": None, "wall_time_h": None},
        "versions": {},
    }
config["training_kernel"] = "hirthick17/medsum-baseline-qlora"
config["inference_kernel"] = "hirthick17/medsum-baseline-infer"
config["hardware_inference"] = {"gpu": GPU, "n_gpu": N_GPU, "device_map": str(DEVICE_MAP), "vram_gb_total": round(VRAM_GB, 1),
                                "peak_vram_gb_per_gpu": round(max(torch.cuda.max_memory_allocated(i) for i in range(N_GPU)) / 2**30, 2),
                                "wall_time_h": round((time.time() - T0) / 3600, 2)}
config["versions_inference"] = {"torch": torch.__version__, "transformers": transformers.__version__, "peft": peft.__version__,
                                "bitsandbytes": bitsandbytes.__version__, "python": sys.version.split()[0]}
config["decoding"] = DECODING
config["validation_checks"] = val_checks | {
    "adapter_reload_fresh_process": True,
    "adapter_sha256": adapter_sha,
    "adapter_matches_checkpoint": adapter_is[0] if adapter_is else None,
    "adapter_matches_train_summary": (train_summary or {}).get("adapter_sha256") == adapter_sha if train_summary else None,
    "adapter_reload_note": "generation runs in a separate kernel from training (fresh base + PeftModel.from_pretrained), "
                           "which is the §7 step 5 reload test itself; non-quantised params upcast to fp32 as in training",
    "zeroshot_base_control": base_checks,
}
config["test_stats"] = test_stats
json.dump(config, open(f"{OUT}/training_config.json", "w"), indent=2, default=str)
log(f"DONE -> {OUT}")
print(json.dumps({k: config[k] for k in ("training", "decoding", "validation_checks", "test_stats")}, indent=2, default=str))
