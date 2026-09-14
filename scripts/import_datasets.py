#!/usr/bin/env python
"""
Import and standardize datasets from data/raw/ into data/processed/.

Supports:
  1. ACI-Bench (ambient clinical intelligence benchmark: dialogue -> full SOAP note)
  2. MTS-Dialog (doctor-patient dialogue -> note sections)
  3. DialogueSOAP (medical dialogue -> structured SOAP summary)

Usage:
  python scripts/import_datasets.py
  python scripts/import_datasets.py --only aci_bench,mts_dialog
  python scripts/import_datasets.py --validate-only
"""

from __future__ import annotations

import argparse
import csv
import json
import os
import sys
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple


@dataclass
class StandardRecord:
    id: str
    dataset: str
    split: str
    source_dialogue: str
    target_summary: str
    metadata: Dict[str, Any]

    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)


class Colors:
    on = sys.stdout.isatty() and os.environ.get("NO_COLOR") is None
    GREEN = "\033[32m" if on else ""
    YELLOW = "\033[33m" if on else ""
    RED = "\033[31m" if on else ""
    CYAN = "\033[36m" if on else ""
    BOLD = "\033[1m" if on else ""
    OFF = "\033[0m" if on else ""


def log_info(msg: str) -> None:
    print(f"  {msg}", flush=True)


def log_ok(msg: str) -> None:
    print(f"  {Colors.GREEN}OK{Colors.OFF}   {msg}", flush=True)


def log_warn(msg: str) -> None:
    print(f"  {Colors.YELLOW}WARN{Colors.OFF} {msg}", flush=True)


def log_err(msg: str) -> None:
    print(f"  {Colors.RED}FAIL{Colors.OFF} {msg}", flush=True)


# --------------------------------------------------------------------------------------
# Importer: ACI-Bench
# --------------------------------------------------------------------------------------

def import_aci_bench(raw_dir: Path, out_dir: Path, validate_only: bool = False) -> Dict[str, Any]:
    """
    Schema for ACI-Bench:
    JSON files in data/raw/aci_bench/data/challenge_data_json/
    Key format: {"data": [{"src": "dialogue text...", "tgt": "SOAP note...", "file": "ID"}]}
    """
    base_dir = raw_dir / "aci_bench" / "data" / "challenge_data_json"
    if not base_dir.exists():
        log_err(f"ACI-Bench raw directory not found at {base_dir}")
        return {"status": "failed", "error": f"Directory missing: {base_dir}"}

    file_splits = {
        "train": "train.json",
        "validation": "valid.json",
        "test_taskB_1": "clinicalnlp_taskB_test1.json",
        "test_taskC_2": "clinicalnlp_taskC_test2.json",
        "test_taskC_3": "clef_taskC_test3.json",
    }

    split_stats = {}
    total_records = 0

    for split_name, file_name in file_splits.items():
        json_path = base_dir / file_name
        if not json_path.exists():
            log_warn(f"ACI-Bench file {file_name} missing for split {split_name}")
            continue

        try:
            with open(json_path, "r", encoding="utf-8") as f:
                content = json.load(f)
            items = content.get("data", [])
        except Exception as e:
            log_err(f"Error reading {json_path}: {e}")
            continue

        records: List[StandardRecord] = []
        skipped = 0

        for idx, item in enumerate(items):
            src = (item.get("src") or "").strip()
            tgt = (item.get("tgt") or "").strip()
            file_id = item.get("file", f"{split_name}_{idx}")

            if not src or not tgt:
                skipped += 1
                continue

            rec = StandardRecord(
                id=f"aci_bench_{split_name}_{file_id}",
                dataset="aci_bench",
                split=split_name,
                source_dialogue=src,
                target_summary=tgt,
                metadata={"file_id": file_id},
            )
            records.append(rec)

        split_out_dir = out_dir / "aci_bench"
        if not validate_only:
            split_out_dir.mkdir(parents=True, exist_ok=True)
            out_file = split_out_dir / f"{split_name}.jsonl"
            with open(out_file, "w", encoding="utf-8") as f:
                for rec in records:
                    f.write(json.dumps(rec.to_dict(), ensure_ascii=False) + "\n")

        avg_src_len = sum(len(r.source_dialogue.split()) for r in records) / max(len(records), 1)
        avg_tgt_len = sum(len(r.target_summary.split()) for r in records) / max(len(records), 1)

        split_stats[split_name] = {
            "total_items": len(items),
            "valid_records": len(records),
            "skipped": skipped,
            "avg_dialogue_words": round(avg_src_len, 1),
            "avg_summary_words": round(avg_tgt_len, 1),
        }
        total_records += len(records)

    log_ok(f"ACI-Bench processed: {total_records} valid records across {len(split_stats)} splits")
    return {"status": "success", "total_records": total_records, "splits": split_stats}


# --------------------------------------------------------------------------------------
# Importer: MTS-Dialog
# --------------------------------------------------------------------------------------

def import_mts_dialog(raw_dir: Path, out_dir: Path, validate_only: bool = False) -> Dict[str, Any]:
    """
    Schema for MTS-Dialog:
    CSV files in data/raw/mts_dialog/Main-Dataset/
    Columns: ID, section_header, section_text, dialogue
    Embedded newlines present -> use csv.DictReader
    """
    base_dir = raw_dir / "mts_dialog" / "Main-Dataset"
    if not base_dir.exists():
        log_err(f"MTS-Dialog raw directory not found at {base_dir}")
        return {"status": "failed", "error": f"Directory missing: {base_dir}"}

    file_splits = {
        "train": "MTS-Dialog-TrainingSet.csv",
        "validation": "MTS-Dialog-ValidationSet.csv",
        "test_chat_2023": "MTS-Dialog-TestSet-1-MEDIQA-Chat-2023.csv",
        "test_sum_2023": "MTS-Dialog-TestSet-2-MEDIQA-Sum-2023.csv",
    }

    split_stats = {}
    total_records = 0

    for split_name, file_name in file_splits.items():
        csv_path = base_dir / file_name
        if not csv_path.exists():
            log_warn(f"MTS-Dialog file {file_name} missing for split {split_name}")
            continue

        records: List[StandardRecord] = []
        skipped = 0
        total_items = 0

        try:
            with open(csv_path, "r", encoding="utf-8") as f:
                reader = csv.DictReader(f)
                for idx, row in enumerate(reader):
                    total_items += 1
                    row_id = row.get("ID", str(idx))
                    header = (row.get("section_header") or "").strip()
                    section_text = (row.get("section_text") or "").strip()
                    dialogue = (row.get("dialogue") or "").strip()

                    if not dialogue or not section_text:
                        skipped += 1
                        continue

                    rec = StandardRecord(
                        id=f"mts_dialog_{split_name}_{row_id}",
                        dataset="mts_dialog",
                        split=split_name,
                        source_dialogue=dialogue,
                        target_summary=section_text,
                        metadata={
                            "row_id": row_id,
                            "section_header": header,
                        },
                    )
                    records.append(rec)
        except Exception as e:
            log_err(f"Error reading {csv_path}: {e}")
            continue

        split_out_dir = out_dir / "mts_dialog"
        if not validate_only:
            split_out_dir.mkdir(parents=True, exist_ok=True)
            out_file = split_out_dir / f"{split_name}.jsonl"
            with open(out_file, "w", encoding="utf-8") as f:
                for rec in records:
                    f.write(json.dumps(rec.to_dict(), ensure_ascii=False) + "\n")

        avg_src_len = sum(len(r.source_dialogue.split()) for r in records) / max(len(records), 1)
        avg_tgt_len = sum(len(r.target_summary.split()) for r in records) / max(len(records), 1)

        split_stats[split_name] = {
            "total_items": total_items,
            "valid_records": len(records),
            "skipped": skipped,
            "avg_dialogue_words": round(avg_src_len, 1),
            "avg_summary_words": round(avg_tgt_len, 1),
        }
        total_records += len(records)

    log_ok(f"MTS-Dialog processed: {total_records} valid records across {len(split_stats)} splits")
    return {"status": "success", "total_records": total_records, "splits": split_stats}


# --------------------------------------------------------------------------------------
# Importer: DialogueSOAP
# --------------------------------------------------------------------------------------

def import_dialogue_soap(raw_dir: Path, out_dir: Path, validate_only: bool = False) -> Dict[str, Any]:
    """
    Schema for DialogueSOAP:
    JSON Lines files in data/raw/dialogue_soap/
    Files: train.json, validation.json, test.json
    Fields: dialogue, soap, prompt, messages, messages_nosystem
    """
    base_dir = raw_dir / "dialogue_soap"
    if not base_dir.exists():
        log_err(f"DialogueSOAP raw directory not found at {base_dir}")
        return {"status": "failed", "error": f"Directory missing: {base_dir}"}

    file_splits = {
        "train": "train.json",
        "validation": "validation.json",
        "test": "test.json",
    }

    split_stats = {}
    total_records = 0

    for split_name, file_name in file_splits.items():
        jsonl_path = base_dir / file_name
        if not jsonl_path.exists():
            log_warn(f"DialogueSOAP file {file_name} missing for split {split_name}")
            continue

        records: List[StandardRecord] = []
        skipped = 0
        total_items = 0

        try:
            with open(jsonl_path, "r", encoding="utf-8") as f:
                for idx, line in enumerate(f):
                    line = line.strip()
                    if not line:
                        continue
                    total_items += 1
                    try:
                        item = json.loads(line)
                    except json.JSONDecodeError:
                        skipped += 1
                        continue

                    dialogue = (item.get("dialogue") or "").strip()
                    soap = (item.get("soap") or "").strip()

                    if not dialogue or not soap:
                        skipped += 1
                        continue

                    rec = StandardRecord(
                        id=f"dialogue_soap_{split_name}_{idx}",
                        dataset="dialogue_soap",
                        split=split_name,
                        source_dialogue=dialogue,
                        target_summary=soap,
                        metadata={
                            "prompt": item.get("prompt", ""),
                        },
                    )
                    records.append(rec)
        except Exception as e:
            log_err(f"Error reading {jsonl_path}: {e}")
            continue

        split_out_dir = out_dir / "dialogue_soap"
        if not validate_only:
            split_out_dir.mkdir(parents=True, exist_ok=True)
            out_file = split_out_dir / f"{split_name}.jsonl"
            with open(out_file, "w", encoding="utf-8") as f:
                for rec in records:
                    f.write(json.dumps(rec.to_dict(), ensure_ascii=False) + "\n")

        avg_src_len = sum(len(r.source_dialogue.split()) for r in records) / max(len(records), 1)
        avg_tgt_len = sum(len(r.target_summary.split()) for r in records) / max(len(records), 1)

        split_stats[split_name] = {
            "total_items": total_items,
            "valid_records": len(records),
            "skipped": skipped,
            "avg_dialogue_words": round(avg_src_len, 1),
            "avg_summary_words": round(avg_tgt_len, 1),
        }
        total_records += len(records)

    log_ok(f"DialogueSOAP processed: {total_records} valid records across {len(split_stats)} splits")
    return {"status": "success", "total_records": total_records, "splits": split_stats}


# --------------------------------------------------------------------------------------
# CLI and Main Driver
# --------------------------------------------------------------------------------------

IMPORTERS = {
    "aci_bench": import_aci_bench,
    "mts_dialog": import_mts_dialog,
    "dialogue_soap": import_dialogue_soap,
}


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(
        description="Import and standardize medical dialogue summarization datasets."
    )
    repo_root = Path(__file__).resolve().parent.parent
    p.add_argument(
        "--raw-dir",
        type=Path,
        default=repo_root / "data" / "raw",
        help="Directory containing raw downloaded datasets (default: data/raw)",
    )
    p.add_argument(
        "--out-dir",
        type=Path,
        default=repo_root / "data" / "processed",
        help="Output directory for standardized jsonl files (default: data/processed)",
    )
    p.add_argument(
        "--only",
        type=str,
        default="",
        help="Comma-separated list of datasets to process (aci_bench, mts_dialog, dialogue_soap)",
    )
    p.add_argument(
        "--validate-only",
        action="store_true",
        help="Validate raw schema and report quality statistics without writing output files",
    )
    return p


def main(argv: Optional[List[str]] = None) -> int:
    args = build_parser().parse_args(argv)

    if args.only:
        selected_keys = [k.strip().lower() for k in args.only.split(",") if k.strip()]
        invalid = [k for k in selected_keys if k not in IMPORTERS]
        if invalid:
            log_err(f"Unknown dataset key(s): {', '.join(invalid)}")
            log_info(f"Available datasets: {', '.join(IMPORTERS.keys())}")
            return 2
    else:
        selected_keys = list(IMPORTERS.keys())

    print(f"\n{Colors.BOLD}FaCTS Dataset Importer & Schema Verifier{Colors.OFF}")
    log_info(f"raw directory  : {args.raw_dir}")
    log_info(f"out directory  : {args.out_dir}")
    log_info(f"selected corpora: {', '.join(selected_keys)}")
    if args.validate_only:
        log_info(f"{Colors.YELLOW}Mode: Validate-only (dry run){Colors.OFF}")

    results = {}
    total_valid_across_all = 0

    for key in selected_keys:
        print(f"\n{Colors.BOLD}[{key}]{Colors.OFF} Processing dataset...")
        fn = IMPORTERS[key]
        res = fn(args.raw_dir, args.out_dir, validate_only=args.validate_only)
        results[key] = res
        if res.get("status") == "success":
            total_valid_across_all += res.get("total_records", 0)

    print(f"\n{Colors.BOLD}Import Summary Report{Colors.OFF}")
    print("=" * 70)
    for key, res in results.items():
        if res.get("status") == "success":
            print(f"  {Colors.GREEN}SUCCESS{Colors.OFF}  {key:<16} {res['total_records']:>6} records")
            for split, st in res.get("splits", {}).items():
                print(
                    f"             - {split:<16}: {st['valid_records']:>5} valid "
                    f"(avg dial: {st['avg_dialogue_words']} wds, avg sum: {st['avg_summary_words']} wds)"
                )
        else:
            print(f"  {Colors.RED}FAILED{Colors.OFF}   {key:<16} Error: {res.get('error')}")

    print("=" * 70)
    log_ok(f"Total Standardized Records: {total_valid_across_all}")
    if not args.validate_only:
        log_ok(f"Standardized JSONL datasets generated under: {args.out_dir}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
