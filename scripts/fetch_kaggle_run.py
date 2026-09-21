#!/usr/bin/env python
"""
Drive the two Kaggle kernels of the baseline and turn their output into the report.

  kernel A  hirthick17/medsum-baseline-qlora   trains, writes final/ + trainer_state.json + train_summary.json
  dataset   hirthick17/medsum-baseline-adapter final/ + trainer_state.json of the run we hand over (uploaded from here)
  kernel B  hirthick17/medsum-baseline-infer   loads the adapter, generates, writes predictions/ + training_config.json

Both kernels write /kaggle/working/outputs/<run>/, so downloading both into the same directory yields
the merged §9 layout that scripts/make_report.py reads. `kaggle kernels output` returns nothing while
the latest version is still running, so each stage polls `kaggle kernels status` first.

Why the adapter dataset: kernel B originally took the adapter only from kernel A's `kernel_sources`
mount. Kaggle mounts A's latest *completed* version — the 17 Sep full run was CANCELLED at the 12 h
cap, so run 2 (18 Sep) mounted the smoke run and generated 770 predictions with a 20-step adapter.
Now the adapter we mean to evaluate is uploaded explicitly and kernel B refuses any other sha256.

Usage:
  python scripts/fetch_kaggle_run.py                    # wait for A, download, upload adapter, push B, wait, download, report
  python scripts/fetch_kaggle_run.py --stage adapter    # upload outputs/kaggle/.../final + trainer_state.json as the dataset
  python scripts/fetch_kaggle_run.py --stage infer      # B only: wait for the current B run, download, report
  python scripts/fetch_kaggle_run.py --stage infer --push   # push B first (e.g. after changing decoding), then as above
  python scripts/fetch_kaggle_run.py --stage train      # A only: wait + download (no report — it needs B's output)
  python scripts/fetch_kaggle_run.py --no-wait          # fail fast instead of polling

The poller is a plain foreground loop: if the laptop sleeps or the terminal closes it stops (run 1,
17 Sep: it died at 2 h and nothing was downloaded). Rerunning is safe — every stage is idempotent.
"""

from __future__ import annotations

import argparse
import glob
import hashlib
import json
import re
import shutil
import subprocess
import sys
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
TRAIN_KERNEL = "hirthick17/medsum-baseline-qlora"
INFER_KERNEL = "hirthick17/medsum-baseline-infer"
ADAPTER_DATASET = "hirthick17/medsum-baseline-adapter"
INFER_DIR = ROOT / "kaggle" / "infer"
ADAPTER_META = ROOT / "kaggle" / "adapter" / "dataset-metadata.json"
DEST = ROOT / "outputs" / "kaggle"
ADAPTER_STAGING = ROOT / "outputs" / "kaggle_adapter_upload"   # git-ignored (outputs/)
TERMINAL = {"COMPLETE", "ERROR", "CANCEL_ACKNOWLEDGED", "CANCELLED", "FAILED"}
ACTIVE = {"QUEUED", "RUNNING", "STARTING"}


def status(kernel: str) -> str:
    out = subprocess.run(["kaggle", "kernels", "status", kernel], capture_output=True, text=True)
    text = (out.stdout + out.stderr).strip()
    if 'status "' not in text:
        return f"UNKNOWN ({text[-120:]})"
    return text.split('status "')[1].rstrip('"').replace("KernelWorkerStatus.", "")


def wait_terminal(kernel: str, interval: int, no_wait: bool) -> str:
    t0 = time.time()
    while True:
        st = status(kernel)
        print(f"[{(time.time() - t0) / 3600:5.2f} h] {kernel}: {st}", flush=True)
        if st in TERMINAL:
            return st
        if no_wait:
            sys.exit(f"{kernel} is {st}; rerun without --no-wait to poll")
        time.sleep(interval)


def push(kernel_dir: Path, kernel: str):
    # --accelerator: Kaggle's API default GPU is the P100, which the current torch build no longer supports
    print(f"pushing {kernel} from {kernel_dir}", flush=True)
    subprocess.run(["kaggle", "kernels", "push", "-p", str(kernel_dir), "--accelerator", "NvidiaTeslaT4"], check=True)
    # the status endpoint keeps reporting the previous version's terminal state for a while after a push
    for _ in range(24):
        st = status(kernel)
        if st in ACTIVE:
            print(f"{kernel}: {st}", flush=True)
            return
        time.sleep(5)
    print(f"warning: {kernel} did not report QUEUED/RUNNING within 2 min (status {st}); polling anyway", flush=True)


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as fh:
        for chunk in iter(lambda: fh.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def local_adapter(dest: Path) -> Path:
    adapters = sorted(glob.glob(f"{dest}/**/final/adapter_model.safetensors", recursive=True))
    if not adapters:
        sys.exit(f"no final/adapter_model.safetensors under {dest}: run `--stage train --no-wait` first")
    if len(adapters) > 1:
        sys.exit("several adapters under outputs/kaggle, refusing to guess:\n  " + "\n  ".join(adapters))
    return Path(adapters[0])


def upload_adapter(dest: Path):
    """Stage final/ + trainer_state.json + environment.txt of the downloaded run and push them as the adapter dataset.
    The dataset root mirrors kernel A's run directory, so kernel B's TRAIN_OUT = dirname(final/) still works."""
    adapter = local_adapter(dest)
    run = adapter.parent.parent
    sha = sha256(adapter)
    pinned = re.search(r'EXPECTED_ADAPTER_SHA256\s*=\s*"([0-9a-f]{64})"', (INFER_DIR / "baseline_infer.py").read_text(encoding="utf-8"))
    if pinned and pinned.group(1) != sha:
        sys.exit(f"{adapter} has sha256 {sha[:16]} but kaggle/infer/baseline_infer.py pins {pinned.group(1)[:16]} — "
                 "update EXPECTED_ADAPTER_SHA256 if this adapter is the one you mean to evaluate")
    if ADAPTER_STAGING.exists():
        shutil.rmtree(ADAPTER_STAGING)
    ADAPTER_STAGING.mkdir(parents=True)
    shutil.copytree(run / "final", ADAPTER_STAGING / "final")
    for name in ("trainer_state.json", "environment.txt", "train_summary.json"):
        if (run / name).exists():
            shutil.copy(run / name, ADAPTER_STAGING / name)
    shutil.copy(ADAPTER_META, ADAPTER_STAGING / "dataset-metadata.json")
    size = sum(f.stat().st_size for f in ADAPTER_STAGING.rglob("*") if f.is_file()) / 2**20
    print(f"uploading {ADAPTER_DATASET} from {run} (sha256 {sha[:16]}, {size:.0f} MB)", flush=True)
    exists = subprocess.run(["kaggle", "datasets", "status", ADAPTER_DATASET], capture_output=True, text=True)
    if "ready" in (exists.stdout + exists.stderr).lower():
        cmd = ["kaggle", "datasets", "version", "-p", str(ADAPTER_STAGING), "--dir-mode", "zip", "-t", "-m", f"adapter {sha[:16]} from {run.name}"]
    else:
        cmd = ["kaggle", "datasets", "create", "-p", str(ADAPTER_STAGING), "--dir-mode", "zip", "-t"]
    subprocess.run(cmd, check=True)
    # a new dataset/version is not mountable until Kaggle has unpacked it
    for _ in range(60):
        st = subprocess.run(["kaggle", "datasets", "status", ADAPTER_DATASET], capture_output=True, text=True)
        text = (st.stdout + st.stderr).strip()
        print(f"{ADAPTER_DATASET}: {text[-80:]}", flush=True)
        if "ready" in text.lower():
            return
        time.sleep(10)
    print(f"warning: {ADAPTER_DATASET} not reported ready after 10 min; pushing the kernel anyway", flush=True)


def download(kernel: str, dest: Path) -> list[Path]:
    dest.mkdir(parents=True, exist_ok=True)
    before = {Path(f) for f in glob.glob(f"{dest}/**/*", recursive=True) if Path(f).is_file()}
    subprocess.run(["kaggle", "kernels", "output", kernel, "-p", str(dest), "-o"], check=True)
    files = [Path(f) for f in glob.glob(f"{dest}/**/*", recursive=True) if Path(f).is_file()]
    new = [f for f in files if f not in before or f.stat().st_mtime > time.time() - 600]
    print(f"{kernel}: {len(files)} files in {dest} ({sum(f.stat().st_size for f in files) / 2**20:.1f} MB), {len(new)} new/updated", flush=True)
    for f in sorted(new)[:40]:
        print("  ", f.relative_to(dest))
    return files


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--stage", choices=["all", "train", "adapter", "infer"], default="all")
    ap.add_argument("--push", action="store_true", help="push the inference kernel before waiting for it (stage infer)")
    ap.add_argument("--dest", default=str(DEST))
    ap.add_argument("--interval", type=int, default=300, help="poll interval in seconds")
    ap.add_argument("--no-wait", action="store_true")
    ap.add_argument("--no-report", action="store_true")
    a = ap.parse_args()
    dest = Path(a.dest)

    if a.stage in ("all", "train"):
        st = wait_terminal(TRAIN_KERNEL, a.interval, a.no_wait)
        if st != "COMPLETE":
            print(f"{TRAIN_KERNEL} ended with {st}; downloading whatever output exists", flush=True)
        download(TRAIN_KERNEL, dest)
        local_adapter(dest)   # exits if the run never reached the save step
        if not glob.glob(f"{dest}/**/train_summary.json", recursive=True):
            print("note: no train_summary.json (output predates the two-kernel split); the inference kernel rebuilds the training half from trainer_state.json", flush=True)
        if a.stage == "train":
            return

    if a.stage in ("all", "adapter"):
        upload_adapter(dest)
        if a.stage == "adapter":
            return
        push(INFER_DIR, INFER_KERNEL)

    if a.stage == "infer" and a.push:
        push(INFER_DIR, INFER_KERNEL)

    st = wait_terminal(INFER_KERNEL, a.interval, a.no_wait)
    if st != "COMPLETE":
        print(f"{INFER_KERNEL} ended with {st}; downloading whatever output exists", flush=True)
    # B lands in a staging dir first: it also writes trainer_state.json, and merging a wrong-adapter run
    # into dest would overwrite A's real one (that is how run 2 would have looked like a valid run)
    staging = dest.parent / f"{dest.name}_infer_staging"
    if staging.exists():
        shutil.rmtree(staging)
    download(INFER_KERNEL, staging)
    cfgs = glob.glob(f"{staging}/**/training_config.json", recursive=True)
    if not cfgs:
        sys.exit(f"no training_config.json in the inference output ({staging}): the run did not reach the config step — `kaggle kernels logs {INFER_KERNEL}`")
    staged_run = Path(cfgs[-1]).parent
    adapter = local_adapter(dest)
    run = adapter.parent.parent
    if staged_run.name != run.name:
        sys.exit(f"kernel B wrote {staged_run.name} but the local training run is {run.name}; not merging")
    used = json.load((staged_run / "training_config.json").open()).get("validation_checks", {}).get("adapter_sha256")
    have = sha256(adapter)
    if used != have:
        sys.exit(f"ADAPTER MISMATCH: kernel B generated with sha256 {str(used)[:16]} but {adapter} is {have[:16]}. "
                 f"Left in {staging}, NOT merged into {run}. Check what kernel B mounted: `kaggle kernels logs {INFER_KERNEL}`")
    print(f"adapter provenance OK: generation used {have[:16]} = final/", flush=True)
    shutil.copytree(staged_run, run, dirs_exist_ok=True)
    shutil.rmtree(staging)
    print(f"merged kernel B output into {run}", flush=True)
    if a.no_report:
        return
    subprocess.run([sys.executable, str(ROOT / "scripts" / "make_report.py"), "--run", str(run)], check=True)


if __name__ == "__main__":
    main()
