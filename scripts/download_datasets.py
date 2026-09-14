#!/usr/bin/env python
"""
Download the corpora used by the FaCTS clinical-summarization project.

Everything in the `core` and `extra` tiers is publicly downloadable with no account.
The `gated` tier is PhysioNet credentialed-access data (MIMIC, MedNLI): it is skipped
unless you pass --include-gated *and* you already hold PhysioNet credentialed access
with the data-use agreement signed for that specific project.

Usage
-----
    python scripts/download_datasets.py --list
    python scripts/download_datasets.py --tier core
    python scripts/download_datasets.py --tier core --tier extra
    python scripts/download_datasets.py --only meqsum,aci_bench
    python scripts/download_datasets.py --include-gated --physionet-user YOURNAME
    python scripts/download_datasets.py --tier core --dry-run

Downloads are resumable and idempotent: a dataset with a valid `.download_complete`
marker is skipped unless --force is given. A manifest with sizes and SHA-256 digests
is written to data/MANIFEST.json.
"""

from __future__ import annotations

import argparse
import getpass
import hashlib
import json
import os
import shutil
import sys
import tarfile
import time
import zipfile
from dataclasses import dataclass, field
from datetime import datetime, timezone
from pathlib import Path
from typing import Callable, Iterable

try:
    import requests
except ImportError:  # pragma: no cover
    sys.exit("Missing dependency: pip install requests\n(or: pip install -r requirements.txt)")


# --------------------------------------------------------------------------------------
# Registry
# --------------------------------------------------------------------------------------

@dataclass
class Dataset:
    key: str                       # folder name under data/raw/
    title: str
    tier: str                      # core | extra | gated
    kind: str                      # github_zip | http_file | hf_dataset | physionet_dir
    role: str                      # what it is used for in the pipeline
    approx_size: str
    licence: str
    # kind-specific
    url: str = ""                  # github_zip / http_file
    repo_id: str = ""              # hf_dataset
    hf_files: list[str] = field(default_factory=list)   # optional allow_patterns
    physionet_path: str = ""       # e.g. "mimic-iv-note/2.2/"
    notes: str = ""
    strip_top_level: bool = True   # for archives: drop the single wrapper directory


REGISTRY: list[Dataset] = [
    # ---------------------------------------------------------------- core
    Dataset(
        key="meqsum",
        title="MeQSum - consumer health question summarization (Ben Abacha & Demner-Fushman, ACL 2019)",
        tier="core",
        kind="github_zip",
        url="https://codeload.github.com/abachaa/MeQSum/zip/refs/heads/master",
        role="question summarization; short-input eval set",
        approx_size="~1 MB",
        licence="Free for research use (NLM/LHNCBC)",
        notes="Data ships as MeQSum_ACL2019_BenAbacha_Demner-Fushman.xlsx (1,000 pairs).",
    ),
    Dataset(
        key="mediqa2021",
        title="MEDIQA-2021 shared task - QS / MAS / RRS",
        tier="core",
        kind="github_zip",
        url="https://codeload.github.com/abachaa/MEDIQA2021/zip/refs/heads/main",
        role="question summarization, multi-answer summarization, radiology report summarization",
        approx_size="~35 MB",
        licence="Free for research use",
        notes="Covers MEDIQA-QS and MEDIQA-MAS named in the project report, plus radiology RRS.",
    ),
    Dataset(
        key="mts_dialog",
        title="MTS-Dialog - doctor-patient dialogue to clinical note sections",
        tier="core",
        kind="github_zip",
        url="https://codeload.github.com/abachaa/MTS-Dialog/zip/refs/heads/main",
        role="dialogue -> note training data; cross-corpus external validation partner for ACI-Bench",
        approx_size="~10 MB",
        licence="CC BY 4.0",
        notes="1,700 train / 100 val / 200 test section-level pairs, plus augmented sets.",
    ),
    Dataset(
        key="aci_bench",
        title="ACI-Bench - ambient clinical intelligence benchmark (Yim et al., Sci. Data 2023)",
        tier="core",
        kind="github_zip",
        url="https://codeload.github.com/wyim/aci-bench/zip/refs/heads/main",
        role="full-encounter dialogue -> SOAP note; source of the MEDCON factuality metric",
        approx_size="~60 MB",
        licence="See repository LICENSE (research use)",
        notes="207 encounters with reference notes across three test splits.",
    ),
    Dataset(
        key="openi_iu_xray",
        title="Open-i / Indiana University Chest X-ray - radiology reports (NLM)",
        tier="core",
        kind="http_file",
        url="https://openi.nlm.nih.gov/imgs/collections/NLMCXR_reports.tgz",
        role="Findings -> Impression summarization; non-credentialed stand-in for MIMIC-CXR",
        approx_size="~15 MB (reports only, no images)",
        licence="Public domain / open access (NLM Open-i)",
        notes="~3,900 de-identified reports as XML.",
    ),
    Dataset(
        key="asclepius_synthetic",
        title="Asclepius Synthetic Clinical Notes (Kweon et al.)",
        tier="core",
        kind="hf_dataset",
        repo_id="starmpcc/Asclepius-Synthetic-Clinical-Notes",
        role="large-scale note -> summary/QA instruction data; MIMIC-style without credentialing",
        approx_size="~500 MB",
        licence="CC BY-NC-SA 4.0 (non-commercial - fine for coursework)",
        notes="~158k instruction pairs incl. a summarization task built on synthetic discharge notes.",
    ),
    Dataset(
        key="augmented_clinical_notes",
        title="Augmented Clinical Notes (AGBonnet / MediNote)",
        tier="core",
        kind="hf_dataset",
        repo_id="AGBonnet/augmented-clinical-notes",
        role="note -> structured summary supervision",
        approx_size="~180 MB",
        licence="See dataset card",
        notes="30k notes paired with generated summaries and structured patient info.",
    ),
    Dataset(
        key="scifact",
        title="SciFact - scientific claim verification (Wadden et al., EMNLP 2020)",
        tier="core",
        kind="http_file",
        url="https://scifact.s3-us-west-2.amazonaws.com/release/latest/data.tar.gz",
        role="ungated training data for the Stage-3 entailment verifier (MedNLI fallback)",
        approx_size="~5 MB",
        licence="CC BY-NC 2.0",
        notes="Official AI2 release. The allenai/scifact HF repo is loading-script-only and "
              "has no parquet conversion, so it cannot be used with datasets>=3.0.",
    ),

    # ---------------------------------------------------------------- extra
    Dataset(
        key="meddialog",
        title="MedDialog-EN (HealthCareMagic + iCliniq summarization splits)",
        tier="extra",
        kind="hf_dataset",
        repo_id="lighteval/med_dialog",
        hf_files=["*.parquet", "README.md"],
        role="doctor-patient dialogue summarization; the MedDialog split used by Van Veen et al. [1][10][15]",
        approx_size="~130 MB",
        licence="See dataset card / original UCSD MedDialog release",
        notes="Parquet mirror. The bigbio/meddialog and UCSD26/medical_dialog repos ship only a "
              "loading script, which datasets>=3.0 no longer executes - do not use them.",
    ),
    Dataset(
        key="dialogue_soap",
        title="Medical dialogue -> SOAP summary (omi-health)",
        tier="extra",
        kind="hf_dataset",
        repo_id="omi-health/medical-dialogue-to-soap-summary",
        role="extra dialogue->structured-note supervision; augments MTS-Dialog / ACI-Bench",
        approx_size="~40 MB",
        licence="See dataset card",
        notes="train/validation/test JSON with SOAP-formatted reference notes.",
    ),
    Dataset(
        key="medquad",
        title="MedQuAD - 47k medical question-answer pairs (NIH)",
        tier="extra",
        kind="github_zip",
        url="https://codeload.github.com/abachaa/MedQuAD/zip/refs/heads/master",
        role="domain background corpus; optional retrieval index for RAG fallback",
        approx_size="~65 MB",
        licence="CC BY 4.0 (answers from NIH sources)",
    ),
    Dataset(
        key="mediqa2019",
        title="MEDIQA-2019 shared task (NLI / RQE / QA)",
        tier="extra",
        kind="github_zip",
        url="https://codeload.github.com/abachaa/MEDIQA2019/zip/refs/heads/master",
        role="clinical NLI data for verifier pretraining",
        approx_size="~20 MB",
        licence="Free for research use",
        notes="The NLI subset is derived from MedNLI; some files may point back to PhysioNet.",
    ),

    # ---------------------------------------------------------------- gated (PhysioNet)
    Dataset(
        key="mimic_iv_note",
        title="MIMIC-IV-Note v2.2 - deidentified discharge summaries & radiology reports",
        tier="gated",
        kind="physionet_dir",
        physionet_path="mimic-iv-note/2.2/",
        role="external validation (Gap G2); 331k discharge summaries",
        approx_size="~4 GB compressed",
        licence="PhysioNet Credentialed Health Data Licence 1.5.0 - requires CITI training + signed DUA",
        notes="Apply at https://physionet.org/content/mimic-iv-note/2.2/ before running this.",
    ),
    Dataset(
        key="mimic_cxr_reports",
        title="MIMIC-CXR v2.1.0 - free-text radiology reports",
        tier="gated",
        kind="physionet_dir",
        physionet_path="mimic-cxr/2.1.0/",
        role="radiology Findings -> Impression, external validation",
        approx_size="~130 MB (reports archive only)",
        licence="PhysioNet Credentialed Health Data Licence 1.5.0",
        notes="Only mimic-cxr-reports.zip is needed; images are not used by this project.",
    ),
    Dataset(
        key="mednli",
        title="MedNLI - natural language inference for clinical text",
        tier="gated",
        kind="physionet_dir",
        physionet_path="mednli/1.0.0/",
        role="preferred training data for the Stage-3 entailment verifier",
        approx_size="~5 MB",
        licence="PhysioNet Credentialed Health Data Licence 1.5.0",
        notes="Requires the same credentialing as MIMIC-III.",
    ),
]

BY_KEY = {d.key: d for d in REGISTRY}
TIERS = ("core", "extra", "gated")

USER_AGENT = "medsum-fact-dataset-downloader/1.0 (coursework; contact: project owner)"
CHUNK = 1 << 16


# --------------------------------------------------------------------------------------
# Small helpers
# --------------------------------------------------------------------------------------

class Colors:
    on = sys.stdout.isatty() and os.environ.get("NO_COLOR") is None
    GREEN = "\033[32m" if on else ""
    YELLOW = "\033[33m" if on else ""
    RED = "\033[31m" if on else ""
    DIM = "\033[2m" if on else ""
    BOLD = "\033[1m" if on else ""
    OFF = "\033[0m" if on else ""


def info(msg: str) -> None:
    print(f"  {msg}", flush=True)


def ok(msg: str) -> None:
    print(f"  {Colors.GREEN}OK{Colors.OFF}   {msg}", flush=True)


def warn(msg: str) -> None:
    print(f"  {Colors.YELLOW}WARN{Colors.OFF} {msg}", flush=True)


def fail(msg: str) -> None:
    print(f"  {Colors.RED}FAIL{Colors.OFF} {msg}", flush=True)


def human(n: float) -> str:
    for unit in ("B", "KB", "MB", "GB", "TB"):
        if abs(n) < 1024:
            return f"{n:,.1f} {unit}"
        n /= 1024
    return f"{n:,.1f} PB"


def sha256_of(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as fh:
        for block in iter(lambda: fh.read(1 << 20), b""):
            h.update(block)
    return h.hexdigest()


def dir_stats(root: Path) -> tuple[int, int]:
    """(file_count, total_bytes) for a directory tree, ignoring marker files."""
    files = 0
    total = 0
    for p in root.rglob("*"):
        if p.is_file() and not p.name.startswith(".download_") and ".cache" not in p.parts:
            files += 1
            total += p.stat().st_size
    return files, total


# --------------------------------------------------------------------------------------
# HTTP with resume
# --------------------------------------------------------------------------------------

def stream_download(
    url: str,
    dest: Path,
    session: requests.Session,
    auth: tuple[str, str] | None = None,
    retries: int = 3,
    extra_headers: dict[str, str] | None = None,
) -> Path:
    """Download `url` to `dest`, resuming a partial `.part` file when the server allows it."""
    part = dest.with_suffix(dest.suffix + ".part")
    dest.parent.mkdir(parents=True, exist_ok=True)

    for attempt in range(1, retries + 1):
        have = part.stat().st_size if part.exists() else 0
        headers = {"User-Agent": USER_AGENT, **(extra_headers or {})}
        if have:
            headers["Range"] = f"bytes={have}-"
        try:
            with session.get(url, headers=headers, stream=True, timeout=60, auth=auth,
                             allow_redirects=True) as r:
                if r.status_code == 416:          # already complete
                    break
                if have and r.status_code == 200:  # server ignored Range -> restart
                    have = 0
                    part.unlink(missing_ok=True)
                r.raise_for_status()

                total = int(r.headers.get("Content-Length", 0)) + have
                mode = "ab" if have else "wb"
                done = have
                last = time.monotonic()
                with part.open(mode) as fh:
                    for chunk in r.iter_content(CHUNK):
                        if not chunk:
                            continue
                        fh.write(chunk)
                        done += len(chunk)
                        now = time.monotonic()
                        if Colors.on and now - last > 0.4:
                            last = now
                            pct = f"{done / total * 100:5.1f}%" if total else "  ?  "
                            print(f"\r       {pct}  {human(done)}"
                                  + (f" / {human(total)}" if total else "") + "        ",
                                  end="", flush=True)
                if Colors.on:
                    print("\r" + " " * 60 + "\r", end="")
            break
        except (requests.RequestException, OSError) as exc:
            if attempt == retries:
                raise
            wait = 2 ** attempt
            warn(f"{type(exc).__name__}: {exc} - retry {attempt}/{retries - 1} in {wait}s")
            time.sleep(wait)

    part.replace(dest)
    return dest


# --------------------------------------------------------------------------------------
# Safe extraction
# --------------------------------------------------------------------------------------

def _is_within(base: Path, target: Path) -> bool:
    try:
        target.resolve().relative_to(base.resolve())
        return True
    except ValueError:
        return False


def extract_archive(archive: Path, out_dir: Path, strip_top_level: bool = True) -> None:
    """Extract zip/tar into out_dir, refusing path traversal, optionally stripping one wrapper dir."""
    staging = out_dir / ".download_staging"
    if staging.exists():
        shutil.rmtree(staging)
    staging.mkdir(parents=True)

    name = archive.name.lower()
    if name.endswith(".zip"):
        with zipfile.ZipFile(archive) as zf:
            for member in zf.namelist():
                target = staging / member
                if not _is_within(staging, target):
                    raise RuntimeError(f"unsafe path in archive: {member}")
            zf.extractall(staging)
    elif name.endswith((".tgz", ".tar.gz", ".tar", ".tar.bz2", ".tbz2", ".tar.xz")):
        with tarfile.open(archive) as tf:
            for member in tf.getmembers():
                target = staging / member.name
                if member.issym() or member.islnk() or not _is_within(staging, target):
                    raise RuntimeError(f"unsafe entry in archive: {member.name}")
            if sys.version_info >= (3, 12):
                tf.extractall(staging, filter="data")
            else:
                tf.extractall(staging)
    else:
        raise RuntimeError(f"don't know how to extract {archive.name}")

    # A GitHub zip contains exactly one wrapper directory (repo-branch/). Flatten it.
    entries = [p for p in staging.iterdir() if p.name != "__MACOSX"]
    src_root = entries[0] if (strip_top_level and len(entries) == 1 and entries[0].is_dir()) else staging

    for item in list(src_root.iterdir()):
        target = out_dir / item.name
        if target.exists():
            shutil.rmtree(target) if target.is_dir() else target.unlink()
        shutil.move(str(item), str(target))

    shutil.rmtree(staging, ignore_errors=True)


# --------------------------------------------------------------------------------------
# Per-kind handlers
# --------------------------------------------------------------------------------------

def get_archive(ds: Dataset, out_dir: Path, session: requests.Session,
                keep_archive: bool) -> dict:
    filename = ds.url.rstrip("/").split("/")[-1]
    if ds.kind == "github_zip" or not Path(filename).suffix:
        filename = f"{ds.key}.zip" if ds.kind == "github_zip" else filename
    archive = out_dir / f".download_{filename}"

    info(f"GET {ds.url}")
    stream_download(ds.url, archive, session)
    digest = sha256_of(archive)
    size = archive.stat().st_size
    info(f"extracting {human(size)} ...")
    extract_archive(archive, out_dir, ds.strip_top_level)
    if not keep_archive:
        archive.unlink(missing_ok=True)
    return {"source_url": ds.url, "archive_sha256": digest, "archive_bytes": size}


def _hf_resolve_download(ds: Dataset, out_dir: Path, session: requests.Session) -> str:
    """
    Fallback HF fetch: list the repo over the public API and pull each file from its
    /resolve/main/ URL ourselves.

    huggingface_hub occasionally fails on brotli-encoded responses for uncompressed
    file types (plain .json in particular). Requesting identity encoding sidesteps it,
    and this path also works when huggingface_hub is not installed at all.
    """
    import fnmatch

    token = os.environ.get("HF_TOKEN") or os.environ.get("HUGGING_FACE_HUB_TOKEN")
    api_headers = {"User-Agent": USER_AGENT}
    if token:
        api_headers["Authorization"] = f"Bearer {token}"

    r = session.get(f"https://huggingface.co/api/datasets/{ds.repo_id}",
                    headers=api_headers, timeout=60)
    r.raise_for_status()
    names = [s["rfilename"] for s in r.json().get("siblings", [])]
    if ds.hf_files:
        names = [n for n in names
                 if any(fnmatch.fnmatch(n, pat) or fnmatch.fnmatch(Path(n).name, pat)
                        for pat in ds.hf_files)]
    names = [n for n in names if not n.startswith(".git")]

    dl_headers = {"Accept-Encoding": "identity"}
    if token:
        dl_headers["Authorization"] = f"Bearer {token}"
    for name in names:
        url = f"https://huggingface.co/datasets/{ds.repo_id}/resolve/main/{name}"
        info(f"  {name}")
        stream_download(url, out_dir / name, session, extra_headers=dl_headers)
    return f"resolve/main ({len(names)} files)"


def get_hf_dataset(ds: Dataset, out_dir: Path, session: requests.Session) -> dict:
    path = ""
    try:
        from huggingface_hub import snapshot_download
    except ImportError:
        warn("huggingface_hub not installed - using direct HTTPS fallback")
        path = _hf_resolve_download(ds, out_dir, session)
    else:
        info(f"snapshot_download({ds.repo_id}, repo_type='dataset')")
        try:
            path = snapshot_download(
                repo_id=ds.repo_id,
                repo_type="dataset",
                local_dir=str(out_dir),
                allow_patterns=ds.hf_files or None,
                token=os.environ.get("HF_TOKEN") or os.environ.get("HUGGING_FACE_HUB_TOKEN"),
            )
        except Exception as exc:
            warn(f"snapshot_download failed ({type(exc).__name__}: {exc}) - "
                 "retrying over direct HTTPS")
            path = _hf_resolve_download(ds, out_dir, session)

    # Some older Hub repos contain only a Python loading script and no data. `datasets`
    # 3.x refuses to execute those, so a "successful" snapshot there is really an empty
    # download. Catch it here rather than three weeks into preprocessing.
    DATA_EXT = {".parquet", ".csv", ".tsv", ".json", ".jsonl", ".arrow",
                ".txt", ".xlsx", ".zip", ".gz", ".xml"}
    # Metadata that ships alongside a loading script and must not count as data.
    META_NAMES = {"dataset_infos.json", "dataset_dict.json", "readme.md",
                  ".gitattributes", "state.json"}
    data_files = [
        p for p in out_dir.rglob("*")
        if p.is_file()
        and p.suffix.lower() in DATA_EXT
        and p.name.lower() not in META_NAMES
        and ".cache" not in p.parts
    ]
    if not data_files:
        scripts = [p.name for p in out_dir.rglob("*.py")]
        raise RuntimeError(
            f"{ds.repo_id} produced no data files"
            + (f" (only loading script(s): {', '.join(scripts)})" if scripts else "")
            + " - this repo needs a different mirror."
        )

    return {"source_url": f"https://huggingface.co/datasets/{ds.repo_id}",
            "snapshot_path": str(path),
            "data_files": len(data_files)}


def get_physionet(ds: Dataset, out_dir: Path, session: requests.Session,
                  user: str, password: str) -> dict:
    """
    Recursively mirror a PhysioNet credentialed directory over HTTPS basic auth.

    PhysioNet serves credentialed files under /files/<path>. A 403 means the account
    is not credentialed for that project (or the DUA is unsigned) - not a bug here.
    """
    base = "https://physionet.org/files/" + ds.physionet_path.lstrip("/")
    auth = (user, password)
    fetched: list[str] = []

    def walk(url: str, rel: Path) -> None:
        r = session.get(url, auth=auth, timeout=60, headers={"User-Agent": USER_AGENT})
        if r.status_code in (401, 403):
            raise RuntimeError(
                f"PhysioNet returned {r.status_code} for {url}\n"
                "       Your account is not credentialed for this project, or the "
                "data use agreement is unsigned."
            )
        r.raise_for_status()
        # Directory listing: parse hrefs. Anything ending in '/' is a subdirectory.
        import re
        hrefs = re.findall(r'href="([^"?#]+)"', r.text)
        for href in hrefs:
            if href.startswith(("..", "/", "http", "#", "?")):
                continue
            if href.endswith("/"):
                walk(url + href, rel / href.rstrip("/"))
            else:
                target = out_dir / rel / href
                if target.exists():
                    continue
                info(f"  {rel / href}")
                stream_download(url + href, target, session, auth=auth)
                fetched.append(str(rel / href))

    walk(base, Path("."))
    return {"source_url": base, "files_fetched": len(fetched)}


# --------------------------------------------------------------------------------------
# Driver
# --------------------------------------------------------------------------------------

MARKER = ".download_complete"


def process(ds: Dataset, raw_root: Path, session: requests.Session, args,
            physionet_creds: tuple[str, str] | None) -> dict:
    out_dir = raw_root / ds.key
    marker = out_dir / MARKER

    print(f"\n{Colors.BOLD}[{ds.key}]{Colors.OFF} {ds.title}")
    info(f"{Colors.DIM}tier={ds.tier}  role={ds.role}  size~{ds.approx_size}{Colors.OFF}")
    info(f"{Colors.DIM}licence: {ds.licence}{Colors.OFF}")
    if ds.notes:
        info(f"{Colors.DIM}note: {ds.notes}{Colors.OFF}")

    if marker.exists() and not args.force:
        meta = json.loads(marker.read_text(encoding="utf-8"))
        ok(f"already present ({meta.get('files', '?')} files, "
           f"{human(meta.get('bytes', 0))}) - use --force to redownload")
        return {**meta, "status": "cached"}

    if args.dry_run:
        target = ds.url or ds.repo_id or ("physionet:" + ds.physionet_path)
        info(f"{Colors.YELLOW}dry-run{Colors.OFF} would fetch {target} -> {out_dir}")
        return {"status": "dry-run"}

    if args.force and out_dir.exists():
        shutil.rmtree(out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)

    started = time.monotonic()
    try:
        if ds.kind in ("github_zip", "http_file"):
            extra = get_archive(ds, out_dir, session, args.keep_archives)
        elif ds.kind == "hf_dataset":
            extra = get_hf_dataset(ds, out_dir, session)
        elif ds.kind == "physionet_dir":
            if not physionet_creds:
                raise RuntimeError("no PhysioNet credentials available")
            extra = get_physionet(ds, out_dir, session, *physionet_creds)
        else:
            raise RuntimeError(f"unknown kind {ds.kind!r}")
    except Exception as exc:
        fail(f"{type(exc).__name__}: {exc}")
        return {"status": "failed", "error": f"{type(exc).__name__}: {exc}"}

    files, total = dir_stats(out_dir)
    meta = {
        "key": ds.key,
        "title": ds.title,
        "tier": ds.tier,
        "licence": ds.licence,
        "path": str(out_dir),
        "files": files,
        "bytes": total,
        "downloaded_at": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "elapsed_s": round(time.monotonic() - started, 1),
        **extra,
    }
    marker.write_text(json.dumps(meta, indent=2), encoding="utf-8")
    ok(f"{files} files, {human(total)} in {meta['elapsed_s']}s -> {out_dir}")
    return {**meta, "status": "downloaded"}


def print_registry() -> None:
    for tier in TIERS:
        rows = [d for d in REGISTRY if d.tier == tier]
        print(f"\n{Colors.BOLD}{tier.upper()}{Colors.OFF}"
              + ("   (requires PhysioNet credentialed access)" if tier == "gated" else ""))
        for d in rows:
            print(f"  {d.key:<26} {d.approx_size:<22} {d.title}")
            print(f"  {'':<26} {Colors.DIM}{d.role}{Colors.OFF}")
    print()


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(
        description="Download datasets for the FaCTS clinical-summarization project.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=__doc__,
    )
    here = Path(__file__).resolve().parent.parent
    p.add_argument("--data-root", type=Path, default=here / "data",
                   help="project data directory (default: <repo>/data)")
    p.add_argument("--tier", action="append", choices=TIERS,
                   help="tier to download; repeatable (default: core)")
    p.add_argument("--only", type=str, help="comma-separated dataset keys, overrides --tier")
    p.add_argument("--skip", type=str, default="", help="comma-separated dataset keys to skip")
    p.add_argument("--list", action="store_true", help="show the registry and exit")
    p.add_argument("--force", action="store_true", help="redownload even if already present")
    p.add_argument("--dry-run", action="store_true", help="show what would be fetched")
    p.add_argument("--keep-archives", action="store_true", help="keep downloaded .zip/.tgz files")
    p.add_argument("--include-gated", action="store_true",
                   help="also fetch PhysioNet credentialed data (needs approved access)")
    p.add_argument("--physionet-user", type=str, default=os.environ.get("PHYSIONET_USER", ""),
                   help="PhysioNet username (or set PHYSIONET_USER)")
    return p


def main(argv: Iterable[str] | None = None) -> int:
    args = build_parser().parse_args(argv)

    if args.list:
        print_registry()
        return 0

    # ---- selection
    skip = {s.strip() for s in args.skip.split(",") if s.strip()}
    if args.only:
        keys = [k.strip() for k in args.only.split(",") if k.strip()]
        unknown = [k for k in keys if k not in BY_KEY]
        if unknown:
            print(f"Unknown dataset key(s): {', '.join(unknown)}", file=sys.stderr)
            print("Run with --list to see valid keys.", file=sys.stderr)
            return 2
        selected = [BY_KEY[k] for k in keys]
    else:
        tiers = set(args.tier or ["core"])
        if args.include_gated:
            tiers.add("gated")
        selected = [d for d in REGISTRY if d.tier in tiers]

    selected = [d for d in selected if d.key not in skip]

    gated = [d for d in selected if d.tier == "gated"]
    if gated and not args.include_gated and not args.only:
        selected = [d for d in selected if d.tier != "gated"]
        gated = []

    # ---- PhysioNet credentials, only if actually needed
    physionet_creds: tuple[str, str] | None = None
    if gated and not args.dry_run:
        print(f"\n{Colors.YELLOW}PhysioNet credentialed data selected.{Colors.OFF}")
        print("  These corpora are governed by the PhysioNet Credentialed Health Data")
        print("  Licence. You must already have completed CITI training and signed the")
        print("  data use agreement for each project. Credentials are used for this")
        print("  session only and are never written to disk.")
        user = args.physionet_user or input("  PhysioNet username: ").strip()
        password = os.environ.get("PHYSIONET_PASSWORD") or getpass.getpass("  PhysioNet password: ")
        if not user or not password:
            print("  No credentials given - skipping gated datasets.", file=sys.stderr)
            selected = [d for d in selected if d.tier != "gated"]
        else:
            physionet_creds = (user, password)

    if not selected:
        print("Nothing selected.", file=sys.stderr)
        return 1

    raw_root = args.data_root / "raw"
    for sub in ("raw", "interim", "processed"):
        (args.data_root / sub).mkdir(parents=True, exist_ok=True)

    print(f"\n{Colors.BOLD}FaCTS dataset downloader{Colors.OFF}")
    print(f"  data root : {args.data_root}")
    print(f"  selected  : {len(selected)} dataset(s) - {', '.join(d.key for d in selected)}")

    session = requests.Session()
    results: dict[str, dict] = {}
    for ds in selected:
        results[ds.key] = process(ds, raw_root, session, args, physionet_creds)

    # ---- manifest
    if not args.dry_run:
        manifest_path = args.data_root / "MANIFEST.json"
        existing = {}
        if manifest_path.exists():
            try:
                existing = json.loads(manifest_path.read_text(encoding="utf-8")).get("datasets", {})
            except json.JSONDecodeError:
                pass
        existing.update({k: v for k, v in results.items() if v.get("status") != "failed"})
        manifest_path.write_text(json.dumps(
            {"generated_at": datetime.now(timezone.utc).isoformat(timespec="seconds"),
             "datasets": existing}, indent=2), encoding="utf-8")

    # ---- summary
    print(f"\n{Colors.BOLD}Summary{Colors.OFF}")
    total_bytes = 0
    failed = []
    for key, r in results.items():
        status = r.get("status", "?")
        if status == "failed":
            failed.append(key)
            print(f"  {Colors.RED}FAILED{Colors.OFF}     {key:<26} {r.get('error', '')[:90]}")
        elif status == "dry-run":
            print(f"  {Colors.YELLOW}DRY-RUN{Colors.OFF}    {key}")
        else:
            total_bytes += r.get("bytes", 0)
            print(f"  {Colors.GREEN}{status:<10}{Colors.OFF} {key:<26} "
                  f"{r.get('files', 0):>6} files  {human(r.get('bytes', 0))}")
    if total_bytes:
        print(f"  {'':<11} {'total':<26} {'':>6}        {human(total_bytes)}")
    if failed:
        print(f"\n{Colors.YELLOW}{len(failed)} dataset(s) failed.{Colors.OFF} "
              "Rerun with --only " + ",".join(failed) + " to retry just those.")
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
