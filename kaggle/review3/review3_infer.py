#!/usr/bin/env python
"""
Review 3 test-set generation — Kaggle kernel.

Two systems on the base model (no adapter), one per T4, in parallel:
  A  zeroshot_base   Review 2 prompt
  B  factcond_base   fact-conditioned prompt (src/pipeline/prompt.py, built by scripts/build_review3_prompts.py)

Input:  dataset hirthick17/medsum-review3-prompts  (review3_prompts.jsonl, 520 records:
        ACI-Bench test 1-3 + MTS-Dialog test chat/sum 2023)
Output: /kaggle/working/outputs/review3/predictions/<system>/<split>.jsonl  (REVIEW2_BASELINE.md §8.3 schema),
        run_config.json, worker logs.

Decoding = Review 2 run 1 (the more grounded one) with a longer budget: greedy, repetition_penalty 1.1,
no n-gram block, max_new_tokens 1024. Predictions are appended per batch, so a killed kernel keeps its work.
"""
MODE = "full"                        # "smoke" (2 items per split) | "full"
MODEL_ID = "unsloth/Meta-Llama-3.1-8B-Instruct"   # same base as the Review 2 adapter
MAX_NEW_TOKENS = 1024
REPETITION_PENALTY = 1.1
GEN_BATCH = 4
SYSTEMS = ["zeroshot_base", "factcond_base"]

import os, sys, json, glob, subprocess, time

OUT = "/kaggle/working/outputs/review3" + ("_smoke" if MODE == "smoke" else "")
WORKER = os.environ.get("R3_WORKER")

if WORKER is None:
    # ---- parent: install, then launch one worker per GPU ---------------------------------------
    import importlib.metadata as _md
    try:
        _tf = _md.version("transformers")
    except _md.PackageNotFoundError:
        _tf = "0"
    pins = ["bitsandbytes>=0.46", "accelerate>=1.1"] + (["transformers>=4.51,<5"] if _tf.split(".")[0] != "4" else [])
    subprocess.run([sys.executable, "-m", "pip", "install", "-q", *pins], check=True)
    import torch
    n_gpu = torch.cuda.device_count()
    print(f"[parent] {n_gpu} GPU(s): {[torch.cuda.get_device_name(i) for i in range(n_gpu)]}", flush=True)
    os.makedirs(OUT, exist_ok=True)
    t0 = time.time()
    procs = []
    for k, system in enumerate(SYSTEMS):
        env = dict(os.environ, R3_WORKER=system, CUDA_VISIBLE_DEVICES=str(k % max(1, n_gpu)),
                   PYTORCH_CUDA_ALLOC_CONF="expandable_segments:True", TOKENIZERS_PARALLELISM="false")
        log = open(f"{OUT}/worker_{system}.log", "w")
        procs.append((system, subprocess.Popen([sys.executable, "-u", __file__], env=env, stdout=log, stderr=subprocess.STDOUT), log))
        if n_gpu < 2:                 # one GPU: run the systems one after the other
            procs[-1][1].wait()
    while any(p.poll() is None for _, p, _ in procs):
        time.sleep(120)
        for system, _, _ in procs:
            tail = open(f"{OUT}/worker_{system}.log").read().strip().splitlines()[-1:] or [""]
            print(f"[parent {(time.time() - t0) / 60:6.1f} min] {system}: {tail[0][:160]}", flush=True)
    for system, p, log in procs:
        log.close()
        print(f"[parent] {system} exit code {p.returncode}\n" + open(f"{OUT}/worker_{system}.log").read()[-3000:], flush=True)
    json.dump({"model": MODEL_ID, "adapter": None, "systems": SYSTEMS, "mode": MODE,
               "decoding": {"do_sample": False, "num_beams": 1, "max_new_tokens": MAX_NEW_TOKENS,
                            "repetition_penalty": REPETITION_PENALTY, "no_repeat_ngram": None, "batch": GEN_BATCH},
               "gpus": [torch.cuda.get_device_name(i) for i in range(n_gpu)],
               "wall_time_h": round((time.time() - t0) / 3600, 2),
               "exit_codes": {s: p.returncode for s, p, _ in procs}},
              open(f"{OUT}/run_config.json", "w"), indent=2)
    sys.exit(max(p.returncode for _, p, _ in procs))

# ---- worker: one system on one GPU -------------------------------------------------------------
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer, BitsAndBytesConfig, set_seed

set_seed(42)
T0 = time.time()


def log(msg):
    print(f"[{WORKER} {(time.time() - T0) / 60:6.1f} min] {msg}", flush=True)


path = sorted(glob.glob("/kaggle/input/**/review3_prompts.jsonl", recursive=True))
assert path, "review3_prompts.jsonl not mounted"
records = [json.loads(l) for l in open(path[0], encoding="utf-8") if l.strip()]
if MODE == "smoke":
    by = {}
    for r in records:
        by.setdefault(r["split"], []).append(r)
    records = [r for v in by.values() for r in v[:2]]
log(f"{len(records)} records on {torch.cuda.get_device_name(0)}")

tok = AutoTokenizer.from_pretrained(MODEL_ID)
tok.pad_token = tok.eos_token
tok.padding_side = "left"
EOS = sorted({tok.eos_token_id, tok.convert_tokens_to_ids("<|eot_id|>")})
model = AutoModelForCausalLM.from_pretrained(
    MODEL_ID, device_map={"": 0}, torch_dtype=torch.float16, attn_implementation="sdpa",
    quantization_config=BitsAndBytesConfig(load_in_4bit=True, bnb_4bit_quant_type="nf4",
                                           bnb_4bit_use_double_quant=True, bnb_4bit_compute_dtype=torch.float16)).eval()
log(f"model loaded, VRAM {torch.cuda.memory_allocated() / 2**30:.1f} GB")

os.makedirs(f"{OUT}/predictions/{WORKER}", exist_ok=True)
done = set()
for f in glob.glob(f"{OUT}/predictions/{WORKER}/*.jsonl"):
    done |= {json.loads(l)["id"] for l in open(f, encoding="utf-8") if l.strip()}
todo = sorted([r for r in records if r["id"] not in done], key=lambda r: -len(r["source_dialogue"]))
GEN = dict(max_new_tokens=MAX_NEW_TOKENS, do_sample=False, num_beams=1, repetition_penalty=REPETITION_PENALTY,
           eos_token_id=EOS, pad_token_id=tok.eos_token_id)

with torch.no_grad():
    for i in range(0, len(todo), GEN_BATCH):
        batch = todo[i:i + GEN_BATCH]
        texts = [tok.apply_chat_template(r["messages"][WORKER], tokenize=False, add_generation_prompt=True) for r in batch]
        enc = tok(texts, return_tensors="pt", padding=True, add_special_tokens=False).to("cuda")
        gen = model.generate(**enc, **GEN)
        for r, row, mask in zip(batch, gen[:, enc["input_ids"].shape[1]:], enc["attention_mask"]):
            ids = row.tolist()
            cut = next((k for k, t in enumerate(ids) if t in EOS), len(ids))
            with open(f"{OUT}/predictions/{WORKER}/{r['split']}.jsonl", "a", encoding="utf-8") as fh:
                fh.write(json.dumps({
                    "id": r["id"], "dataset": r["dataset"], "split": r["split"],
                    "source_dialogue": r["source_dialogue"], "reference_summary": r["reference_summary"],
                    "prediction": tok.decode(ids[:cut], skip_special_tokens=True).strip(),
                    "model": MODEL_ID, "adapter": None, "system": WORKER, "prompt_version": r["prompt_version"],
                    "decoding": {"max_new_tokens": MAX_NEW_TOKENS, "do_sample": False, "repetition_penalty": REPETITION_PENALTY},
                    "prompt_tokens": int(mask.sum()), "generated_tokens": cut, "truncated": cut >= MAX_NEW_TOKENS,
                }, ensure_ascii=False) + "\n")
        log(f"{min(i + GEN_BATCH, len(todo))}/{len(todo)} | prompt {enc['input_ids'].shape[1]} tok | "
            f"peak {torch.cuda.max_memory_allocated() / 2**30:.1f} GB")
log("done")
