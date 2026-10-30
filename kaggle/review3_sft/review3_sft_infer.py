#!/usr/bin/env python
"""
Review 3 — the Review 2 QLoRA adapter on the test set with the SAME decoding as systems A/B
(kaggle/review3/review3_infer.py): greedy, repetition_penalty 1.1, no n-gram block, max_new_tokens 1024.

  sft_1024       adapter + Review 2 prompt (the prompt it was trained on)   -> matched comparison with A
  sft_factcond   adapter + fact-conditioned prompt (factcond-v1)             -> "SFT + fact table" row

Input:  hirthick17/medsum-review3-prompts (520 records: ACI-Bench test 1-3 + MTS-Dialog test 1-2)
        hirthick17/medsum-baseline-adapter (final/ = 332-step adapter, sha256 pinned below)
Output: /kaggle/working/outputs/review3_sft/predictions/<system>/<split>.jsonl, run_config.json

Model loading follows kaggle/infer/baseline_infer.py: 4-bit NF4 base split over both T4s
(device_map="balanced"), non-quantised parameters upcast to fp32 as during training, tokenizer saved with
the adapter. The two systems therefore run one after the other. Predictions are appended per batch.
"""
MODE = "full"                        # "smoke" (2 items per split) | "full"
MODEL_ID = "unsloth/Meta-Llama-3.1-8B-Instruct"
EXPECTED_ADAPTER_SHA256 = "14e712617f1456b669ef02e6c512e41464dbeee450bbed6245045cb568b69481"
MAX_NEW_TOKENS = 1024
REPETITION_PENALTY = 1.1
GEN_BATCH = 4
SYSTEMS = {"sft_1024": "zeroshot_base", "sft_factcond": "factcond_base"}   # output system -> prompt key

import os, sys, json, glob, hashlib, subprocess, time
os.environ["PYTORCH_CUDA_ALLOC_CONF"] = "expandable_segments:True"
os.environ["TOKENIZERS_PARALLELISM"] = "false"

import importlib.metadata as _md
try:
    _tf = _md.version("transformers")
except _md.PackageNotFoundError:
    _tf = "0"
PINS = ["bitsandbytes>=0.46", "peft>=0.14", "accelerate>=1.1"] + (["transformers>=4.51,<5"] if _tf.split(".")[0] != "4" else [])
subprocess.run([sys.executable, "-m", "pip", "install", "-q", *PINS], check=True)

import torch
from transformers import AutoModelForCausalLM, AutoTokenizer, BitsAndBytesConfig, set_seed
from peft import PeftModel

set_seed(42)
T0 = time.time()


def log(msg):
    print(f"[{(time.time() - T0) / 60:6.1f} min] {msg}", flush=True)


N_GPU = torch.cuda.device_count()
DEVICE_MAP = "balanced" if N_GPU > 1 else {"": 0}
OUT = "/kaggle/working/outputs/review3_sft" + ("_smoke" if MODE == "smoke" else "")
os.makedirs(OUT, exist_ok=True)

prompts = sorted(glob.glob("/kaggle/input/**/review3_prompts.jsonl", recursive=True))
adapters = sorted(glob.glob("/kaggle/input/**/final/adapter_config.json", recursive=True))
assert prompts and adapters, f"inputs not mounted: prompts={prompts} adapters={adapters}"
ADAPTER = os.path.dirname(adapters[0])
sha = hashlib.sha256(open(f"{ADAPTER}/adapter_model.safetensors", "rb").read()).hexdigest()
if sha != EXPECTED_ADAPTER_SHA256:
    raise SystemExit(f"adapter sha256 {sha[:16]} != expected {EXPECTED_ADAPTER_SHA256[:16]}")
records = [json.loads(l) for l in open(prompts[0], encoding="utf-8") if l.strip()]
if MODE == "smoke":
    by = {}
    for r in records:
        by.setdefault(r["split"], []).append(r)
    records = [r for v in by.values() for r in v[:2]]
log(f"{len(records)} records | {N_GPU}x {torch.cuda.get_device_name(0)} | adapter {ADAPTER} sha {sha[:16]}")

tok = AutoTokenizer.from_pretrained(ADAPTER)
tok.pad_token = tok.eos_token
tok.padding_side = "left"
EOS = sorted({tok.eos_token_id, tok.convert_tokens_to_ids("<|eot_id|>")})
base = AutoModelForCausalLM.from_pretrained(
    MODEL_ID, device_map=DEVICE_MAP, torch_dtype=torch.float16, attn_implementation="sdpa",
    quantization_config=BitsAndBytesConfig(load_in_4bit=True, bnb_4bit_quant_type="nf4",
                                           bnb_4bit_use_double_quant=True, bnb_4bit_compute_dtype=torch.float16))
for p in base.parameters():          # as in training (prepare_model_for_kbit_training) and baseline_infer.py
    if p.dtype in (torch.float16, torch.bfloat16):
        p.data = p.data.to(torch.float32)
model = PeftModel.from_pretrained(base, ADAPTER).eval()
model.config.use_cache = True
log("model loaded | VRAM " + " + ".join(f"{torch.cuda.memory_allocated(i) / 2**30:.1f}" for i in range(N_GPU)) + " GB")

GEN = dict(max_new_tokens=MAX_NEW_TOKENS, do_sample=False, num_beams=1, repetition_penalty=REPETITION_PENALTY,
           eos_token_id=EOS, pad_token_id=tok.eos_token_id)
times = {}
with torch.no_grad():
    for system, key in SYSTEMS.items():
        t_sys = time.time()
        os.makedirs(f"{OUT}/predictions/{system}", exist_ok=True)
        todo = sorted(records, key=lambda r: -len(r["source_dialogue"]))
        for i in range(0, len(todo), GEN_BATCH):
            batch = todo[i:i + GEN_BATCH]
            texts = [tok.apply_chat_template(r["messages"][key], tokenize=False, add_generation_prompt=True) for r in batch]
            enc = tok(texts, return_tensors="pt", padding=True, add_special_tokens=False).to(model.device)
            gen = model.generate(**enc, **GEN)
            for r, row, mask in zip(batch, gen[:, enc["input_ids"].shape[1]:], enc["attention_mask"]):
                ids = row.tolist()
                cut = next((k for k, t in enumerate(ids) if t in EOS), len(ids))
                with open(f"{OUT}/predictions/{system}/{r['split']}.jsonl", "a", encoding="utf-8") as fh:
                    fh.write(json.dumps({
                        "id": r["id"], "dataset": r["dataset"], "split": r["split"],
                        "source_dialogue": r["source_dialogue"], "reference_summary": r["reference_summary"],
                        "prediction": tok.decode(ids[:cut], skip_special_tokens=True).strip(),
                        "model": MODEL_ID, "adapter": "baseline_qlora_llama31_8b/final", "adapter_sha256": sha,
                        "system": system, "prompt": key, "prompt_version": r["prompt_version"],
                        "decoding": {"max_new_tokens": MAX_NEW_TOKENS, "do_sample": False, "repetition_penalty": REPETITION_PENALTY},
                        "prompt_tokens": int(mask.sum()), "generated_tokens": cut, "truncated": cut >= MAX_NEW_TOKENS,
                    }, ensure_ascii=False) + "\n")
            if (i // GEN_BATCH) % 10 == 0:
                log(f"{system} {min(i + GEN_BATCH, len(todo))}/{len(todo)} | peak "
                    + " + ".join(f"{torch.cuda.max_memory_allocated(g) / 2**30:.1f}" for g in range(N_GPU)) + " GB")
        times[system] = round((time.time() - t_sys) / 3600, 2)
        log(f"{system} done in {times[system]} h")

json.dump({"model": MODEL_ID, "adapter_sha256": sha, "systems": SYSTEMS, "mode": MODE,
           "decoding": {"do_sample": False, "num_beams": 1, "max_new_tokens": MAX_NEW_TOKENS,
                        "repetition_penalty": REPETITION_PENALTY, "no_repeat_ngram": None, "batch": GEN_BATCH},
           "device_map": str(DEVICE_MAP), "gpus": [torch.cuda.get_device_name(i) for i in range(N_GPU)],
           "hours_per_system": times, "wall_time_h": round((time.time() - T0) / 3600, 2)},
          open(f"{OUT}/run_config.json", "w"), indent=2)
log("DONE")
