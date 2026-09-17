#!/usr/bin/env python
"""
Wait for the Kaggle baseline kernel to finish, download its output, build the report.

`kaggle kernels output` returns nothing while the latest version is still running, so this
polls `kaggle kernels status` first. Downloads land in outputs/kaggle/ (git-ignored), then
scripts/make_report.py writes reports/<run>/report.pdf.

Usage:
  python scripts/fetch_kaggle_run.py                       # poll every 10 min, then download + report
  python scripts/fetch_kaggle_run.py --no-wait             # fail fast if the kernel is still running
  python scripts/fetch_kaggle_run.py --kernel owner/slug --interval 300
"""

from __future__ import annotations

import argparse
import glob
import subprocess
import sys
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
KERNEL = "hirthick17/medsum-baseline-qlora"
DEST = ROOT / "outputs" / "kaggle"
TERMINAL = {"COMPLETE", "ERROR", "CANCEL_ACKNOWLEDGED", "CANCELLED", "FAILED"}


def status(kernel: str) -> str:
    out = subprocess.run(["kaggle", "kernels", "status", kernel], capture_output=True, text=True)
    text = (out.stdout + out.stderr).strip()
    if 'status "' not in text:
        return f"UNKNOWN ({text[-120:]})"
    return text.split('status "')[1].rstrip('"').replace("KernelWorkerStatus.", "")


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--kernel", default=KERNEL)
    ap.add_argument("--dest", default=str(DEST))
    ap.add_argument("--interval", type=int, default=600, help="poll interval in seconds")
    ap.add_argument("--no-wait", action="store_true")
    ap.add_argument("--no-report", action="store_true")
    a = ap.parse_args()

    t0 = time.time()
    while True:
        st = status(a.kernel)
        print(f"[{(time.time() - t0) / 3600:5.2f} h] {a.kernel}: {st}", flush=True)
        if st in TERMINAL:
            break
        if a.no_wait:
            sys.exit(f"kernel is {st}; rerun without --no-wait to poll")
        time.sleep(a.interval)

    if st != "COMPLETE":
        print(f"kernel ended with {st}; downloading whatever output exists (log included)", flush=True)

    Path(a.dest).mkdir(parents=True, exist_ok=True)
    subprocess.run(["kaggle", "kernels", "output", a.kernel, "-p", a.dest, "-o"], check=True)
    files = [f for f in glob.glob(f"{a.dest}/**/*", recursive=True) if Path(f).is_file()]
    print(f"downloaded {len(files)} files ({sum(Path(f).stat().st_size for f in files) / 2**20:.1f} MB) -> {a.dest}", flush=True)
    for f in sorted(files)[:40]:
        print("  ", Path(f).relative_to(a.dest))

    cfgs = glob.glob(f"{a.dest}/**/training_config.json", recursive=True)
    if not cfgs:
        sys.exit("no training_config.json in the output: the run did not reach the save step — read the kernel log")
    if a.no_report:
        return
    subprocess.run([sys.executable, str(ROOT / "scripts" / "make_report.py"), "--run", str(Path(cfgs[-1]).parent)], check=True)


if __name__ == "__main__":
    main()
