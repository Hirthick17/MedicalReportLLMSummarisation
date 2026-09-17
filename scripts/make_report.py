#!/usr/bin/env python
"""
Build the Review 2 baseline report (PDF) from a downloaded Kaggle run directory.

Reads the tree that baseline_qlora.py writes (REVIEW2_BASELINE.md §9) and produces:
  reports/<run>/report.pdf        — the document
  reports/<run>/metrics.json      — every number in the PDF, machine-readable
  reports/<run>/loss_curve.png    — train / eval loss vs step
plus copies of training_config.json and trainer_state.json (small, safe to commit).
Predictions are NOT copied: they carry the corpora text and stay git-ignored under outputs/.

Sections: run summary · training · §7 validation checks · §8 test-set generation (ROUGE-1/2/L,
length ratio, truncation) · §10 handoff checklist (auto-filled) · sample predictions · environment.

Usage:
  python scripts/make_report.py                                   # auto-detect run under outputs/
  python scripts/make_report.py --run outputs/kaggle/outputs/baseline_qlora_llama31_8b
  python scripts/make_report.py --run ... --out reports/baseline_qlora_llama31_8b
"""

from __future__ import annotations

import argparse
import datetime as dt
import glob
import hashlib
import json
import shutil
import subprocess
import sys
from pathlib import Path

import numpy as np

ROOT = Path(__file__).resolve().parent.parent
TEST_SPLITS = [  # (file stem, headline?) — order matches REVIEW2_BASELINE.md §8.1
    ("aci_bench_test_taskB_1", True), ("aci_bench_test_taskC_2", True), ("aci_bench_test_taskC_3", True),
    ("mts_dialog_test_chat_2023", True), ("mts_dialog_test_sum_2023", True), ("dialogue_soap_test", False),
]
CLIP = 900                                             # characters shown per reference / prediction sample
VAL_GATES = {"aci_bench": 35.0, "mts_dialog": 30.0}   # §7 step 4 quick ROUGE-L sanity gates (F1 × 100)


# ---- helpers ---------------------------------------------------------------------------------
def load_jsonl(path: Path) -> tuple[list[dict], int]:
    recs, bad = [], 0
    with path.open(encoding="utf-8") as fh:
        for line in fh:
            if not line.strip():
                continue
            try:
                recs.append(json.loads(line))
            except json.JSONDecodeError:
                bad += 1
    return recs, bad


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as fh:
        for chunk in iter(lambda: fh.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def find_run(explicit: str | None) -> Path:
    if explicit:
        return Path(explicit)
    hits = sorted(glob.glob(str(ROOT / "outputs" / "**" / "training_config.json"), recursive=True))
    if not hits:
        sys.exit("no training_config.json under outputs/ — run `kaggle kernels output ... -p outputs/kaggle` first")
    return Path(hits[-1]).parent


def fmt(x, nd=3):
    if x is None:
        return "—"
    if isinstance(x, float):
        return f"{x:.{nd}f}"
    return str(x)


# ---- metrics ---------------------------------------------------------------------------------
def score_split(recs: list[dict], scorer) -> dict:
    if not recs:
        return {"n": 0}
    r1, r2, rl, ratios, gen_toks = [], [], [], [], []
    for p in recs:
        s = scorer.score(p["reference_summary"], p["prediction"])
        r1.append(s["rouge1"].fmeasure); r2.append(s["rouge2"].fmeasure); rl.append(s["rougeL"].fmeasure)
        ratios.append(len(p["prediction"].split()) / max(1, len(p["reference_summary"].split())))
        gen_toks.append(p.get("generated_tokens", 0))
    return {
        "n": len(recs),
        "rouge1_f": float(np.mean(r1)) * 100, "rouge2_f": float(np.mean(r2)) * 100, "rougeL_f": float(np.mean(rl)) * 100,
        "rougeL_f_std": float(np.std(rl)) * 100,
        "length_ratio": float(np.mean(ratios)),
        "mean_generated_tokens": float(np.mean(gen_toks)),
        "truncated": int(sum(bool(p.get("truncated")) for p in recs)),
        "empty": int(sum(1 for p in recs if not p["prediction"].strip())),
        "mean_pred_words": float(np.mean([len(p["prediction"].split()) for p in recs])),
        "mean_ref_words": float(np.mean([len(p["reference_summary"].split()) for p in recs])),
    }


def collect(run: Path) -> dict:
    from rouge_score import rouge_scorer
    scorer = rouge_scorer.RougeScorer(["rouge1", "rouge2", "rougeL"], use_stemmer=True)

    cfg = json.load((run / "training_config.json").open())
    state = json.load((run / "trainer_state.json").open()) if (run / "trainer_state.json").exists() else {}
    log_hist = state.get("log_history", [])
    train_pts = [(e["step"], e["loss"]) for e in log_hist if "loss" in e and "step" in e]
    eval_pts = [(e["step"], e["eval_loss"]) for e in log_hist if "eval_loss" in e]
    lr_pts = [(e["step"], e["learning_rate"]) for e in log_hist if "learning_rate" in e]

    # §8 test splits
    pred_dir = run / "predictions" / "baseline_qlora"
    splits, samples, total_lines, total_bad = {}, {}, 0, 0
    for stem, headline in TEST_SPLITS:
        f = pred_dir / f"{stem}.jsonl"
        if not f.exists():
            splits[stem] = {"n": 0, "missing": True, "headline": headline}
            continue
        recs, bad = load_jsonl(f)
        total_lines += len(recs); total_bad += bad
        m = score_split(recs, scorer) | {"json_errors": bad, "headline": headline, "missing": False}
        splits[stem] = m
        if recs:
            # pick the record whose ROUGE-L is closest to the split mean: representative, not cherry-picked
            scored = [(abs(scorer.score(p["reference_summary"], p["prediction"])["rougeL"].fmeasure * 100 - m["rougeL_f"]), p)
                      for p in recs]
            samples[stem] = min(scored, key=lambda t: t[0])[1]

    # §7 validation checks — recompute from val_check.jsonl where possible, fall back to config
    vc = dict(cfg.get("validation_checks", {}))
    val_file = run / "predictions" / "val_check.jsonl"
    val_by_ds = {}
    if val_file.exists():
        vrecs, _ = load_jsonl(val_file)
        for ds in sorted({r["dataset"] for r in vrecs}):
            val_by_ds[ds] = score_split([r for r in vrecs if r["dataset"] == ds], scorer)
    val_gates = {ds: {"rougeL_f": val_by_ds[ds]["rougeL_f"], "gate": VAL_GATES[ds],
                      "pass": val_by_ds[ds]["rougeL_f"] >= VAL_GATES[ds]}
                 for ds in VAL_GATES if ds in val_by_ds}

    # §10 handoff checklist
    manifest_local = ROOT / "kaggle" / "dataset" / "train_manifest.json"
    manifest_run = cfg.get("data", {}).get("manifest", {})
    sha_ok = None
    if manifest_local.exists():
        local = json.load(manifest_local.open())
        sha_ok = all(local[k]["sha256"] == manifest_run.get(k, {}).get("sha256") for k in ("train", "val"))
        for k in ("train", "val"):
            f = ROOT / "kaggle" / "dataset" / local[k]["file"]
            if f.exists() and sha256(f) != local[k]["sha256"]:
                sha_ok = False
    leak = None
    train_val_ids: set[str] = set()
    for name in ("baseline_train.jsonl", "baseline_val.jsonl"):
        f = ROOT / "kaggle" / "dataset" / name
        if f.exists():
            recs, _ = load_jsonl(f)
            train_val_ids |= {r["id"] for r in recs}
    if train_val_ids:
        all_test_ids = set()
        for stem, _ in TEST_SPLITS:
            f = pred_dir / f"{stem}.jsonl"
            if f.exists():
                recs, _ = load_jsonl(f)
                all_test_ids |= {r["id"] for r in recs}
        leak = len(all_test_ids & train_val_ids)
    tr = cfg.get("training", {})
    checklist = [
        ("predictions/baseline_qlora/: 6 files, 770 lines, 0 JSON errors",
         sum(not s.get("missing") for s in splits.values()) == 6 and total_lines == 770 and total_bad == 0,
         f"{sum(not s.get('missing') for s in splits.values())} files, {total_lines} lines, {total_bad} JSON errors"),
        ("truncated == true count per split (reported for Person 3 to flag/exclude)",
         all(not s.get("missing") for s in splits.values()),
         " / ".join(str(s.get("truncated", "—")) for s in splits.values())),
        ("training_config.json matches trainer_state.json (steps, best_step)",
         bool(state) and tr.get("steps_completed") == state.get("global_step"),
         f"config steps={tr.get('steps_completed')} best={tr.get('best_step')} | state global_step={state.get('global_step')}"),
        ("train_manifest sha256 matches kaggle/dataset/baseline_{train,val}.jsonl",
         sha_ok, "verified" if sha_ok else ("MISMATCH" if sha_ok is False else "local files not present")),
        ("final/ adapter reloads and reproduces val item #0 (§7 step 5)",
         vc.get("adapter_reload_identical"),
         f"identical {vc.get('adapter_reload_identical_n', '—')} | ROUGE-L reload vs in-session {vc.get('adapter_reload_rougeL_vs_in_session', '—')}"),
        ("no test id appears in baseline_train/val.jsonl",
         leak == 0 if leak is not None else None, f"{leak} overlapping ids" if leak is not None else "train/val jsonl not present locally"),
        ("environment.txt present", (run / "environment.txt").exists(), "pip freeze captured"),
        ("final/ adapter present",
         (run / "final" / "adapter_model.safetensors").exists(),
         f"{(run / 'final' / 'adapter_model.safetensors').stat().st_size / 2**20:.1f} MB" if (run / "final" / "adapter_model.safetensors").exists() else "missing"),
    ]

    env_lines = (run / "environment.txt").read_text().splitlines() if (run / "environment.txt").exists() else []
    key_pkgs = {}
    for l in env_lines:
        for k in ("torch", "transformers", "peft", "bitsandbytes", "accelerate", "liger-kernel", "liger_kernel", "rouge-score", "rouge_score"):
            if l.lower().startswith(k.lower() + "=="):
                key_pkgs[l.split("==")[0]] = l.split("==")[1]

    return {
        "run_dir": str(run), "generated_at": dt.datetime.now().isoformat(timespec="seconds"),
        "config": cfg, "trainer_state": {k: state.get(k) for k in ("global_step", "epoch", "best_metric", "best_model_checkpoint", "max_steps", "num_train_epochs")},
        "curves": {"train": train_pts, "eval": eval_pts, "lr": lr_pts},
        "validation_checks": vc, "val_by_dataset": val_by_ds, "val_gates": val_gates,
        "test_splits": splits, "samples": samples,
        "handoff_checklist": [{"item": i, "ok": ok, "detail": d} for i, ok, d in checklist],
        "environment": key_pkgs,
        "git_commit": subprocess.run(["git", "rev-parse", "--short", "HEAD"], capture_output=True, text=True, cwd=ROOT).stdout.strip(),
    }


# ---- plots -----------------------------------------------------------------------------------
def plot_curves(m: dict, out: Path):
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt

    tr, ev = m["curves"]["train"], m["curves"]["eval"]
    fig, ax = plt.subplots(figsize=(7.2, 3.4), dpi=160)
    if tr:
        ax.plot(*zip(*tr), color="#4c72b0", lw=1.4, label="train loss")
    if ev:
        ax.plot(*zip(*ev), color="#dd8452", lw=1.6, marker="o", ms=3.5, label="eval loss")
        bs, bl = min(ev, key=lambda t: t[1])
        ax.annotate(f"best {bl:.3f} @ {bs}", (bs, bl), textcoords="offset points", xytext=(6, 8), fontsize=8, color="#dd8452")
    ax.set_xlabel("optimizer step"); ax.set_ylabel("cross-entropy (assistant tokens)")
    ax.grid(alpha=0.25); ax.legend(frameon=False, fontsize=8)
    for s in ("top", "right"):
        ax.spines[s].set_visible(False)
    fig.tight_layout(); fig.savefig(out); plt.close(fig)


# ---- PDF -------------------------------------------------------------------------------------
def build_pdf(m: dict, png: Path, out: Path):
    from reportlab.lib import colors
    from reportlab.lib.enums import TA_LEFT
    from reportlab.lib.pagesizes import A4
    from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
    from reportlab.lib.units import mm
    from reportlab.platypus import Image, PageBreak, Paragraph, SimpleDocTemplate, Spacer, Table, TableStyle
    from xml.sax.saxutils import escape

    # Helvetica (a PDF core font) has no glyphs for →, α, ≥, ☑; use DejaVu Sans, which ships with matplotlib.
    from reportlab.pdfbase import pdfmetrics
    from reportlab.pdfbase.ttfonts import TTFont
    from reportlab.lib.fonts import addMapping
    import matplotlib
    fdir = Path(matplotlib.get_data_path()) / "fonts" / "ttf"
    for name, file in (("DejaVu", "DejaVuSans.ttf"), ("DejaVu-Bold", "DejaVuSans-Bold.ttf"),
                       ("DejaVu-Italic", "DejaVuSans-Oblique.ttf"), ("DejaVu-BoldItalic", "DejaVuSans-BoldOblique.ttf"),
                       ("DejaVuMono", "DejaVuSansMono.ttf")):
        pdfmetrics.registerFont(TTFont(name, str(fdir / file)))
    addMapping("DejaVu", 0, 0, "DejaVu"); addMapping("DejaVu", 1, 0, "DejaVu-Bold")
    addMapping("DejaVu", 0, 1, "DejaVu-Italic"); addMapping("DejaVu", 1, 1, "DejaVu-BoldItalic")

    ss = getSampleStyleSheet()
    H1 = ParagraphStyle("H1", parent=ss["Heading1"], fontName="DejaVu-Bold", fontSize=14, spaceBefore=10, spaceAfter=6, keepWithNext=True)
    H2 = ParagraphStyle("H2", parent=ss["Heading2"], fontName="DejaVu-Bold", fontSize=10, spaceBefore=8, spaceAfter=3, keepWithNext=True)
    BODY = ParagraphStyle("B", parent=ss["BodyText"], fontName="DejaVu", fontSize=8.6, leading=11.5)
    SMALL = ParagraphStyle("S", parent=BODY, fontSize=7.4, leading=9.6, textColor=colors.HexColor("#444444"))
    CELL = ParagraphStyle("C", parent=BODY, fontSize=7.6, leading=9.6)
    MONO = ParagraphStyle("M", parent=BODY, fontName="DejaVuMono", fontSize=6.6, leading=8.4, alignment=TA_LEFT)

    def P(t, st=BODY):
        return Paragraph(t, st)

    def tbl(rows, widths, header=True, zebra=True):
        data = [[c if not isinstance(c, str) else P(f"<b>{c}</b>" if (header and i == 0) else c, CELL) for c in r]
                for i, r in enumerate(rows)]
        t = Table(data, colWidths=widths, repeatRows=1 if header else 0)
        style = [("GRID", (0, 0), (-1, -1), 0.3, colors.HexColor("#bbbbbb")),
                 ("VALIGN", (0, 0), (-1, -1), "TOP"),
                 ("LEFTPADDING", (0, 0), (-1, -1), 4), ("RIGHTPADDING", (0, 0), (-1, -1), 4),
                 ("TOPPADDING", (0, 0), (-1, -1), 2.5), ("BOTTOMPADDING", (0, 0), (-1, -1), 2.5)]
        if header:
            style += [("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#e8edf3")),
                      ("FONTNAME", (0, 0), (-1, 0), "DejaVu-Bold")]
        if zebra:
            for i in range(1 if header else 0, len(rows)):
                if i % 2 == 0:
                    style.append(("BACKGROUND", (0, i), (-1, i), colors.HexColor("#f7f8fa")))
        t.setStyle(TableStyle(style))
        return t

    cfg, tr, hw, lora, q = m["config"], m["config"]["training"], m["config"]["hardware"], m["config"]["lora"], m["config"]["quantization"]
    mode = cfg.get("mode", "full")
    story = []

    # -- title
    story += [P("medsum-fact — Review 2 Baseline Report", ParagraphStyle("T", parent=ss["Title"], fontName="DejaVu-Bold", fontSize=18, spaceAfter=2)),
              P("Plain 4-bit QLoRA fine-tune of Llama-3.1-8B-Instruct for dialogue → clinical note", ParagraphStyle("ST", parent=BODY, fontSize=10.5, textColor=colors.HexColor("#555555"))),
              Spacer(1, 4),
              P(f"Run <b>{escape(cfg['run_name'])}</b> · mode <b>{mode}</b> · Kaggle kernel <font face='DejaVuMono'>hirthick17/medsum-baseline-qlora</font> · "
                f"generated {m['generated_at']} from repo commit <font face='DejaVuMono'>{m['git_commit']}</font>", SMALL)]
    if mode != "full":
        story.append(P("<b>Note:</b> this is a SMOKE run (20 steps on 64 examples, 2 items per test split). Numbers below are pipeline checks, not results.", BODY))
    story.append(Spacer(1, 8))

    # -- 1 summary
    story.append(P("1. Run summary", H1))
    story.append(P("The baseline defined in REVIEW2_BASELINE.md: no fact table, no ORPO, no verifier, no provenance. "
                   "One instruction-tuned decoder, 4-bit NF4 QLoRA SFT on the assistant tokens only, greedy inference on the six official test splits.", BODY))
    kv = [
        ["Base model", f"{escape(cfg['base_model'])}<br/><font size=7 color='#666666'>{escape(cfg.get('base_model_note', ''))}</font>"],
        ["Quantization", f"4-bit {q['quant_type'].upper()}, double-quant={q['double_quant']}, compute {escape(str(q['compute_dtype']))}"],
        ["LoRA", f"r={lora['r']}, α={lora['alpha']}, dropout={lora['dropout']}, targets: {', '.join(lora['target_modules'])}<br/>"
                 f"trainable {lora['trainable_params'] / 1e6:.1f} M of {lora['total_params'] / 1e9:.2f} B ({100 * lora['trainable_params'] / lora['total_params']:.2f} %)"],
        ["Data", f"train {cfg['data']['n_train_used']} · val {cfg['data']['n_val_used']} · max_seq_len {cfg['data']['max_seq_length']}<br/>"
                 f"mix: {escape(json.dumps(cfg['data']['manifest']['train']['mix']))} · leakage check: {cfg['data']['manifest']['leakage_check']['status']}"],
        ["Optimisation", f"lr {tr['lr']} · {tr['scheduler']} · warmup {tr['warmup_ratio']} · {tr['optim']} · batch 1 × accum {tr['grad_accum']} · "
                         f"{tr['epochs']} epochs · seed {tr['seed']} · liger fused-CE={tr.get('liger_fused_ce')}"],
        ["Hardware", f"{escape(hw['gpu'])} · {hw['vram_gb_total']} GB total · device_map {escape(hw['device_map'])} · "
                     f"peak {hw['peak_vram_gb_per_gpu']} GB / GPU · wall time <b>{hw['wall_time_h']} h</b>"],
        ["Versions", " · ".join(f"{k} {v}" for k, v in cfg["versions"].items())],
    ]
    story.append(tbl([["Field", "Value"]] + kv, [30 * mm, 145 * mm]))

    # -- 2 training
    story.append(P("2. Training", H1))
    ev, ts = m["curves"]["eval"], m["trainer_state"]
    best = min(ev, key=lambda t: t[1]) if ev else (None, None)
    rows = [["Metric", "Value"],
            ["Steps completed", f"{tr.get('steps_completed')} (max_steps={tr.get('max_steps')}, epoch {fmt(m['trainer_state'].get('epoch'), 2)})"],
            ["Final train loss", fmt(tr.get("final_train_loss"), 4)],
            ["Best eval loss", f"{fmt(best[1], 4)} at step {best[0]}"],
            ["Eval loss (first → last)", f"{fmt(ev[0][1], 4)} → {fmt(ev[-1][1], 4)}" if ev else "—"],
            ["Wall-clock guard", f"{tr.get('wall_clock_guard_hours')} h — "
                                 + ("HIT (stopped early: %s of %s planned steps)" % (ts.get('global_step'), ts.get('max_steps'))
                                    if ts.get('max_steps') and ts.get('global_step') and ts['global_step'] < ts['max_steps'] else "not hit")]]
    story.append(tbl(rows, [50 * mm, 125 * mm]))
    if png.exists():
        story += [Spacer(1, 6), Image(str(png), width=165 * mm, height=78 * mm)]
        story.append(P("Figure 1 — assistant-token cross-entropy on train (every logging step) and on the 220-item validation set (every eval step). "
                       "load_best_model_at_end selects the checkpoint at the lowest eval loss for generation.", SMALL))

    # -- 3 validation checks
    story.append(P("3. Validation checks (REVIEW2_BASELINE.md §7)", H1))
    vc = m["validation_checks"]
    rows = [["Check", "Result", "Expectation"],
            ["Loss report", f"final train {fmt(tr.get('final_train_loss'), 3)} · best eval {fmt(best[1], 3)} @ {best[0]}", "eval loss decreasing, best step recorded"],
            ["Length ratio (pred / ref words)", fmt(vc.get("length_ratio")), "0.8 – 1.2"],
            ["Quick ROUGE-L on val subset (n=%s)" % vc.get("n"), fmt(vc.get("rougeL_f", 0) * 100, 1) if vc.get("rougeL_f") is not None else "—", "sanity gate only"],
            ["Truncated / empty on val", f"{vc.get('truncated')} / {vc.get('empty')}", "0 / 0"],
            ["Adapter reload test", f"{'PASS' if vc.get('adapter_reload_identical') else 'MISMATCH'} · identical {vc.get('adapter_reload_identical_n', '—')} · ROUGE-L vs in-session {vc.get('adapter_reload_rougeL_vs_in_session', '—')}",
             "byte-identical greedy output from a fresh PeftModel"]]
    for ds, g in m["val_gates"].items():
        rows.append([f"ROUGE-L gate · {ds} val", f"{g['rougeL_f']:.1f} — {'PASS' if g['pass'] else 'BELOW GATE'}", f"≥ {g['gate']:.0f}"])
    story.append(tbl(rows, [50 * mm, 75 * mm, 50 * mm]))
    if vc.get("adapter_reload_note"):
        story.append(P("Reload note: " + escape(vc["adapter_reload_note"]), SMALL))

    # -- 4 test
    story.append(P("4. Test-set generation (REVIEW2_BASELINE.md §8)", H1))
    story.append(P("Greedy decoding (num_beams=1, do_sample=False, repetition_penalty=1.1, max_new_tokens=768). ROUGE F1 × 100 with Porter stemming, "
                   "computed here as a first look — Person 3's evaluation (BERTScore, coverage, hallucination, negation, numeric consistency) supersedes these. "
                   "DialogueSOAP is synthetic and is not a headline number.", BODY))
    rows = [["Split", "n", "R-1", "R-2", "R-L", "len ratio", "gen tok", "trunc", "empty", "status"]]
    for stem, s in m["test_splits"].items():
        if s.get("missing"):
            rows.append([stem, "0", "—", "—", "—", "—", "—", "—", "—", "MISSING"])
            continue
        rows.append([stem, str(s["n"]), fmt(s["rouge1_f"], 1), fmt(s["rouge2_f"], 1), fmt(s["rougeL_f"], 1),
                     fmt(s["length_ratio"], 2), fmt(s["mean_generated_tokens"], 0), str(s["truncated"]), str(s["empty"]),
                     "headline" if s["headline"] else "synthetic"])
    hl = [s for s in m["test_splits"].values() if s.get("headline") and not s.get("missing") and s["n"]]
    if hl:
        n = sum(s["n"] for s in hl)
        w = lambda k: sum(s[k] * s["n"] for s in hl) / n
        rows.append([P("<b>headline (weighted)</b>", CELL), str(n), fmt(w("rouge1_f"), 1), fmt(w("rouge2_f"), 1), fmt(w("rougeL_f"), 1),
                     fmt(w("length_ratio"), 2), fmt(w("mean_generated_tokens"), 0), str(sum(s["truncated"] for s in hl)), str(sum(s["empty"] for s in hl)), ""])
    story.append(tbl(rows, [44 * mm, 9 * mm, 12 * mm, 12 * mm, 12 * mm, 16 * mm, 15 * mm, 12 * mm, 13 * mm, 20 * mm]))

    # -- 5 handoff
    story.append(P("5. Handoff checklist (REVIEW2_BASELINE.md §10)", H1))
    rows = [["", "Item", "Detail"]]
    for c in m["handoff_checklist"]:
        mark = "☑" if c["ok"] else ("☐" if c["ok"] is None else "☒")
        col = "#1a7f37" if c["ok"] else ("#888888" if c["ok"] is None else "#b42318")
        rows.append([P(f"<font color='{col}' size=11>{mark}</font>", CELL), c["item"], escape(str(c["detail"]))])
    story.append(tbl(rows, [8 * mm, 82 * mm, 85 * mm]))
    story.append(P("☑ verified · ☒ failed · ☐ could not be verified from this machine", SMALL))

    # -- 6 samples
    story.append(PageBreak())
    story.append(P("6. Sample predictions", H1))
    story.append(P("One item per split, chosen as the record whose ROUGE-L is closest to that split's mean (representative, not cherry-picked). "
                   f"Text is clipped to {CLIP:,} characters.", BODY))
    for stem, p in m["samples"].items():
        ref, pred = p["reference_summary"], p["prediction"]
        clip = lambda t: escape(t[:CLIP] + (" …" if len(t) > CLIP else "")).replace("\n", "<br/>")
        story.append(P(f"{escape(stem)} — <font face='DejaVuMono'>{escape(p['id'])}</font> · prompt {p.get('prompt_tokens', '?')} tok · generated {p.get('generated_tokens', '?')} tok"
                       + (" · <font color='#b42318'>TRUNCATED</font>" if p.get("truncated") else ""), H2))
        story.append(tbl([["Reference", "Prediction"], [P(clip(ref), MONO), P(clip(pred), MONO)]], [87 * mm, 88 * mm], zebra=False))
        story.append(Spacer(1, 4))

    # -- 7 environment
    story.append(P("7. Environment", H1))
    story.append(P(" · ".join(f"{escape(k)} {escape(v)}" for k, v in m["environment"].items()) or "environment.txt not found", BODY))
    story.append(P(f"Run directory: <font face='DejaVuMono'>{escape(m['run_dir'])}</font>. Predictions and adapter stay under outputs/ (git-ignored; corpora licences forbid redistribution). "
                   "This PDF, metrics.json, training_config.json and trainer_state.json are committed under reports/.", SMALL))

    def footer(canvas, doc):
        canvas.saveState(); canvas.setFont("DejaVu", 7); canvas.setFillColor(colors.HexColor("#777777"))
        canvas.drawString(15 * mm, 10 * mm, f"medsum-fact · Review 2 baseline · {cfg['run_name']}")
        canvas.drawRightString(A4[0] - 15 * mm, 10 * mm, f"page {doc.page}")
        canvas.restoreState()

    doc = SimpleDocTemplate(str(out), pagesize=A4, leftMargin=17 * mm, rightMargin=17 * mm, topMargin=15 * mm, bottomMargin=16 * mm,
                            title="medsum-fact Review 2 baseline report", author="medsum-fact")
    doc.build(story, onFirstPage=footer, onLaterPages=footer)


# ---- main ------------------------------------------------------------------------------------
def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--run", help="run directory containing training_config.json (default: newest under outputs/)")
    ap.add_argument("--out", help="output directory (default: reports/<run_name>)")
    a = ap.parse_args()

    run = find_run(a.run)
    m = collect(run)
    out = Path(a.out) if a.out else ROOT / "reports" / m["config"]["run_name"]
    out.mkdir(parents=True, exist_ok=True)

    png = out / "loss_curve.png"
    plot_curves(m, png)
    build_pdf(m, png, out / "report.pdf")
    json.dump(m, (out / "metrics.json").open("w"), indent=2, default=str)
    for name in ("training_config.json", "trainer_state.json"):
        if (run / name).exists():
            shutil.copy(run / name, out / name)

    hl = [s for s in m["test_splits"].values() if s.get("headline") and not s.get("missing") and s["n"]]
    print(f"report -> {out / 'report.pdf'}")
    print(f"  steps {m['config']['training'].get('steps_completed')} | best eval {fmt(m['config']['training'].get('best_eval_loss'), 4)} "
          f"| wall {m['config']['hardware']['wall_time_h']} h")
    for stem, s in m["test_splits"].items():
        print(f"  {stem:28s} n={s.get('n', 0):4d}  R-L={fmt(s.get('rougeL_f'), 1):>5}  ratio={fmt(s.get('length_ratio'), 2):>5}  trunc={s.get('truncated', '—')}")
    print("  handoff: " + ", ".join(("OK" if c["ok"] else ("??" if c["ok"] is None else "FAIL")) for c in m["handoff_checklist"]))


if __name__ == "__main__":
    main()
