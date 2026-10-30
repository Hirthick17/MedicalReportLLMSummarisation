#!/usr/bin/env python
"""Build the prompt file for the Review 3 test-set run (kaggle/review3/review3_infer.py).

A Kaggle kernel cannot import src/, so the prompts are built here and uploaded as a dataset:

  A  "zeroshot_base"   base model, Review 2 prompt (SYSTEM + task instruction + transcript)
  B  "factcond_base"   base model, fact-conditioned prompt (src/pipeline/prompt.py, PROMPT_VERSION)

Test splits: the three official ACI-Bench test sets and the two MTS-Dialog test sets — the same
splits as the Review 2 baseline, so the SFT adapter row (run 1) is directly comparable.

    python scripts/build_review3_prompts.py
-> kaggle/review3_data/review3_prompts.jsonl  (+ dataset-metadata.json)
"""
import hashlib
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from src.cfe import extract_facts  # noqa: E402
from src.pipeline.prompt import PROMPT_VERSION, SYSTEM, instruction, record_messages  # noqa: E402

DATA = ROOT.parent / "medsum-fact" / "data" / "processed"
SPLITS = {
    "aci_bench_test_taskB_1": DATA / "aci_bench" / "test_taskB_1.jsonl",
    "aci_bench_test_taskC_2": DATA / "aci_bench" / "test_taskC_2.jsonl",
    "aci_bench_test_taskC_3": DATA / "aci_bench" / "test_taskC_3.jsonl",
    "mts_dialog_test_chat_2023": DATA / "mts_dialog" / "test_chat_2023.jsonl",
    "mts_dialog_test_sum_2023": DATA / "mts_dialog" / "test_sum_2023.jsonl",
}
OUT = ROOT / "kaggle" / "review3_data"


def baseline_messages(rec):
    """Review 2 prompt, byte-identical to kaggle/infer/baseline_infer.py prompt_messages()."""
    section = (rec.get("metadata") or {}).get("section_header")
    return [{"role": "system", "content": SYSTEM},
            {"role": "user", "content": f"{instruction(rec['dataset'], section)}\n\nTRANSCRIPT:\n{rec['source_dialogue']}"}]


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    n = 0
    with (OUT / "review3_prompts.jsonl").open("w", encoding="utf-8") as fh:
        for split, path in SPLITS.items():
            for line in path.open(encoding="utf-8"):
                rec = json.loads(line)
                facts = extract_facts(rec["source_dialogue"], kind="dialogue")
                fh.write(json.dumps({
                    "id": rec["id"], "dataset": rec["dataset"], "split": split,
                    "source_dialogue": rec["source_dialogue"], "reference_summary": rec["target_summary"],
                    "messages": {"zeroshot_base": baseline_messages(rec),
                                 "factcond_base": record_messages(rec, facts)},
                    "prompt_version": PROMPT_VERSION,
                }, ensure_ascii=False) + "\n")
                n += 1
            print(f"{split}: done", flush=True)
    sha = hashlib.sha256((OUT / "review3_prompts.jsonl").read_bytes()).hexdigest()
    (OUT / "dataset-metadata.json").write_text(json.dumps({
        "title": "medsum review3 prompts",
        "id": "hirthick17/medsum-review3-prompts",
        "licenses": [{"name": "other"}],
        "description": f"Review 3 test prompts (zero-shot and fact-conditioned, {PROMPT_VERSION}) for ACI-Bench test 1-3 "
                       f"and MTS-Dialog test chat/sum 2023; built by scripts/build_review3_prompts.py; {n} records; sha256 {sha[:16]}.",
    }, indent=2), encoding="utf-8")
    print(f"{n} records -> {OUT / 'review3_prompts.jsonl'} (sha256 {sha[:16]})")


if __name__ == "__main__":
    main()
