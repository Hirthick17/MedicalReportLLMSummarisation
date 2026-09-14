#!/usr/bin/env python
"""
Build the Review 2 baseline training mix from data/processed/ (REVIEW2_BASELINE.md §4.1).

  baseline_train.jsonl = ACI-Bench train (all) + MTS-Dialog train (all) + DialogueSOAP train (sampled)
  baseline_val.jsonl   = ACI-Bench val (all)   + MTS-Dialog val (all)   + DialogueSOAP val (sampled)

Runs the leakage checks (no id overlap, no verbatim dialogue overlap between train/val and any
test split) and writes train_manifest.json with per-dataset counts and SHA-256 of both files.

Usage:
  python scripts/make_baseline_split.py                    # 3000 / 100 DialogueSOAP, seed 42
  python scripts/make_baseline_split.py --soap-train 1500  # T4 reduction from §4.6
"""

from __future__ import annotations

import argparse
import hashlib
import json
import random
import re
from collections import Counter
from pathlib import Path

TEST_SPLITS = {
    "aci_bench": ["test_taskB_1", "test_taskC_2", "test_taskC_3"],
    "mts_dialog": ["test_chat_2023", "test_sum_2023"],
    "dialogue_soap": ["test"],
}


def load(path: Path) -> list[dict]:
    with path.open(encoding="utf-8") as fh:
        return [json.loads(line) for line in fh if line.strip()]


def dump(records: list[dict], path: Path) -> str:
    with path.open("w", encoding="utf-8") as fh:
        for r in records:
            fh.write(json.dumps(r, ensure_ascii=False) + "\n")
    return hashlib.sha256(path.read_bytes()).hexdigest()


def norm(text: str) -> str:
    return re.sub(r"\s+", " ", text).strip().lower()


def main() -> int:
    p = argparse.ArgumentParser()
    p.add_argument("--processed", type=Path,
                   default=Path(__file__).resolve().parent.parent / "data" / "processed")
    p.add_argument("--soap-train", type=int, default=3000)
    p.add_argument("--soap-val", type=int, default=100)
    p.add_argument("--seed", type=int, default=42)
    args = p.parse_args()
    root = args.processed
    rng = random.Random(args.seed)

    train = load(root / "aci_bench" / "train.jsonl") + load(root / "mts_dialog" / "train.jsonl")
    val = load(root / "aci_bench" / "validation.jsonl") + load(root / "mts_dialog" / "validation.jsonl")

    soap_train = load(root / "dialogue_soap" / "train.jsonl")
    soap_val = load(root / "dialogue_soap" / "validation.jsonl")
    rng.shuffle(soap_train)
    rng.shuffle(soap_val)
    train += soap_train[: args.soap_train]
    val += soap_val[: args.soap_val]
    rng.shuffle(train)

    # ---- leakage checks
    test = []
    for ds, splits in TEST_SPLITS.items():
        for s in splits:
            test += load(root / ds / f"{s}.jsonl")

    ids = Counter(r["id"] for r in train + val + test)
    dup_ids = [k for k, n in ids.items() if n > 1]
    train_ids, val_ids = {r["id"] for r in train}, {r["id"] for r in val}
    assert not (train_ids & val_ids), "train/val id overlap"
    assert not dup_ids, f"duplicate ids across splits: {dup_ids[:5]}"

    # Verbatim dialogue overlap with any test split. MTS-Dialog's official splits contain a few
    # recurring two-line exchanges ("any known drug allergies? / No."); we drop those from
    # train/val rather than touch the official test sets, and record what was dropped.
    test_src = {norm(r["source_dialogue"]) for r in test}
    dropped = [r["id"] for r in train + val if norm(r["source_dialogue"]) in test_src]
    train = [r for r in train if norm(r["source_dialogue"]) not in test_src]
    val = [r for r in val if norm(r["source_dialogue"]) not in test_src]

    within_train = Counter(norm(r["source_dialogue"]) for r in train)
    dup_train = sum(n - 1 for n in within_train.values() if n > 1)

    # ---- write
    sha_train = dump(train, root / "baseline_train.jsonl")
    sha_val = dump(val, root / "baseline_val.jsonl")
    manifest = {
        "seed": args.seed,
        "train": {"file": "baseline_train.jsonl", "n": len(train), "sha256": sha_train,
                  "mix": dict(Counter(r["dataset"] for r in train))},
        "val": {"file": "baseline_val.jsonl", "n": len(val), "sha256": sha_val,
                "mix": dict(Counter(r["dataset"] for r in val))},
        "test": {f"{ds}/{s}": sum(1 for r in test if r["dataset"] == ds and r["split"] == s)
                 for ds, splits in TEST_SPLITS.items() for s in splits},
        "leakage_check": {
            "id_overlap": 0,
            "dropped_for_verbatim_overlap_with_test": dropped,
            "duplicate_dialogues_within_train": dup_train,
            "status": "passed",
        },
    }
    (root / "train_manifest.json").write_text(json.dumps(manifest, indent=2), encoding="utf-8")
    print(json.dumps(manifest, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
