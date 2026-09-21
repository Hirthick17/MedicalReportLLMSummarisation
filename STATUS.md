## TL;DR (updated 21 Sep, night) — Review 2 closed

- **Run 3 (kernel B v2, sha-pinned adapter) completed on 19 Sep 06:32 UTC.** The laptop poller had died
  at 0.84 h, so nothing was downloaded until 21 Sep; `fetch_kaggle_run.py --stage infer --no-wait` then
  downloaded it, verified `adapter sha256 14e71261… == final/`, merged it and built
  `reports/baseline_qlora_llama31_8b/report.pdf`. All 6 splits / 770 predictions + `training_config.json`
  + the zero-shot control exist. **No Kaggle kernel is running; no further GPU runs are planned for Review 2.**
- **The new decoding did not fix ACI-Bench.** 29 / 28 / 27 of 40 notes still hit the 1,024-token cap — the
  repetition loops of run 1 became runaway comma-lists of hallucinated terms (see
  `docs/PERSON3_EVALUATION.md`, "Degenerate output example"). MTS-Dialog (5 / 6 of 200) and DialogueSOAP
  (7 / 250) are fine. Root cause is the data mix / early best checkpoint, not decoding
  (`docs/PERSON2_MODEL_TRAINING.md` §7); a 4th decoding run was considered and not run.
- Run 1's predictions (old decoding, same adapter) were re-downloaded from the cancelled kernel A into
  `outputs/kaggle_run1_old_decoding/` so both decodings are evaluated side by side.
- **Person 1 and Person 3 deliverables are done on the laptop (CPU only):** data audit
  (`reports/data_audit/`), rule-based clinical fact extractor (`src/cfe/`, 22 unit tests) and the facts
  dataset (`data/processed/facts/`, 12,108 records), evaluation pipeline (`src/eval/`: ROUGE-1/2/L,
  BERTScore, hallucination / negation-flip / numerical-consistency / coverage, tables, figures, example
  errors) with results in `reports/eval_baseline/`. Documentation: `docs/`.

## TL;DR (19 Sep, morning — superseded by the block above)

- The QLoRA baseline **trained successfully** on Kaggle on 17 Sep (Llama-3.1-8B-Instruct, 4-bit,
  LoRA r=16, 332 steps / 1.24 epochs, best eval loss 0.9555). The adapter is saved and downloaded
  to `outputs/kaggle/outputs/baseline_qlora_llama31_8b/final/` (sha256 `14e71261…`).
- Run 1 (17–18 Sep, single kernel) was **killed by Kaggle's 12 h limit** mid-generation; we
  split training and generation into two kernels (below).
- **Run 2 (kernel B, 18 Sep 20:20 → 19 Sep 00:10 IST) completed cleanly — but with the wrong
  adapter.** Kaggle mounted kernel A's latest *completed* version, which is the 20-step smoke
  run, not the cancelled full run. All 770 predictions in that run come from a near-untrained
  adapter. Nothing in the pipeline failed; the adapter sha256 in the log gave it away.
- Fix (done 19 Sep morning, in the repo): the 17 Sep adapter is uploaded as a private Kaggle
  dataset; kernel B **pins the adapter's sha256** and refuses to run anything else; the fetch
  script and the report both verify the sha before merging/reporting. Kernel B must be re-run
  (~4 h GPU) — that is the only thing between us and the handoff.
- Silver lining: run 2 proves the **decoding fix works** — 2 / 770 truncated (run 1: 71 / 520),
  no repetition loops, ACI-Bench length ratio ≈ 1.0.
- Impact: handoff to evaluation (Person 3) moves to **19 Sep evening** at the earliest
  (kernel B re-run ≈ 4 h from push). Buffer day (20 Sep) unchanged.

## What happened, step by step

**17 Sep 22:12 IST — full run starts** on Kaggle (`hirthick17/medsum-baseline-qlora`, 2× T4).
One script did everything: train → validation checks → generate on all 6 test splits → write
`training_config.json`.

**~05:45 IST 18 Sep — training finishes.** The script's own wall-clock guard stopped it at 7.5 h,
step 332 of 534 (epoch 1.24 of 2). Best eval loss 0.9555 at step 200; the saved `final/` adapter
is that best checkpoint. Adapter, checkpoints and `trainer_state.json` were written to disk.

**~06:00–10:00 IST — generation.** Model reloaded, 20 val items and then the test splits
generated in order: ACI-Bench ×3 (40 each), MTS-Dialog ×2 (200 each) — all written to disk.

**~10:12 IST — Kaggle kills the kernel** at the 12 h mark while it was on the 6th and largest
split, `dialogue_soap_test` (250 items). Status: `CANCEL_ACKNOWLEDGED`. Everything after that
point never happened: the 6th split, the adapter-reload test, `training_config.json`.
Kaggle also **discards the log of a cancelled run**, so the printed metrics (peak VRAM, val
checks) are gone.

**Local side.** The script that was supposed to wait for the run and download it
(`scripts/fetch_kaggle_run.py`) stopped at 00:34 IST — the laptop slept — so nothing was
downloaded until the evening of 18 Sep. That cost us most of a working day before anyone saw the
run had been cancelled.

## Why the Kaggle run "fails"

Three separate things, in order of importance:

### 1. One kernel, 12 h cap, ~13 h of work

| stage | measured time on 2× T4 |
|---|---|
| pip install + model load + tokenising | ~15 min |
| training, 332 steps at 81 s/step | 7.5 h (the guard) |
| 3 evaluations on 220 val items | 14 min |
| model reload for generation | ~5 min |
| 540 generations (ACI-Bench notes ≈ 720 tokens each) | ~3.5 h |
| **remaining: 250 DialogueSOAP items + config** | **never ran — cap hit** |

Training is slow because of the hardware, not the code: T4s have no bf16 and no FlashAttention;
4-bit dequantisation and gradient checkpointing each cost ~1.3×; Kaggle's two T4s run as a naive
pipeline (one works while the other waits); median example ≈ 900 tokens at batch size 1.
That gives **~5 s per training example → 2 epochs over 4,265 examples ≈ 12 h on their own.**
REVIEW2_BASELINE.md §4.6 predicted 9–14 h on a T4; the single-kernel layout did not honour that.

### 2. No log, no config → the report pipeline could not run

`scripts/make_report.py` builds the Review 2 PDF from `training_config.json`, which is the last
thing the script writes. Cancelled → not written → no report, even though 90 % of the results
existed on disk.

### 3. Output quality: repetition loops on long notes (found only after inspecting predictions)

On ACI-Bench (full clinical notes, 400–800 words), **75 % of outputs hit the 768-token cap**
(30, 29, 31 of 40), most in loops like:

> He has been having some difficulty with odynophagia. He has been having some difficulty with
> globus sensation. He has been having some difficulty with regurgitation. …

Cause: `repetition_penalty=1.1` is too weak for long notes, and only 67 of the 4,265 training
examples (1.6 %) are full-length notes, so the model has barely learnt how such a note ends.
Short MTS-Dialog sections are fine (9/200 and 2/200 truncated).

Run 1 numbers (ROUGE F1 × 100, stemmed; first look only — Person 3's evaluation supersedes):

| split | n | R-1 | R-2 | R-L | len ratio | truncated |
|---|---|---|---|---|---|---|
| aci_bench taskB-1 / C-2 / C-3 | 40 each | 29.3–29.7 | 11.4–12.5 | **17.4–17.9** | 1.18–1.26 | 29–31 / 40 |
| mts_dialog chat-2023 | 200 | 42.2 | 19.6 | **35.8** | 1.15 | 9 |
| mts_dialog sum-2023 | 200 | 40.0 | 16.2 | **33.5** | 1.02 | 2 |
| dialogue_soap test | 0 / 250 | — | — | — | — | lost |

## Run 2 (18 Sep, kernel B): completed, wrong adapter

**What the Kaggle terminal shows.** `hirthick17/medsum-baseline-infer` — status `COMPLETE`,
3.82 h wall, peak 10.5 GB / GPU, all six splits written, `training_config.json` written. Log
(kept at `outputs/kaggle_run2_smoke_adapter/medsum-baseline-infer.log`):

```
[env] adapter at /kaggle/input/notebooks/hirthick17/medsum-baseline-qlora/outputs/baseline_qlora_llama31_8b_smoke/final
model loaded | adapter params 41.9M / 8.07B | adapter sha256 f431c7434ba6e411 | VRAM 2.8 + 4.6 GB
final/ adapter matches checkpoint(s) none mounted | best eval step 20 (0.9539413452148438)
```

The adapter we hold locally is `14e712617f1456b6…` (332 steps, best step 200). `f431c743…` is the
smoke-test adapter: 20 optimizer steps over the 64 longest training examples. The
`training_config.json` it produced says `max_steps: 20, epochs_completed: 5.0` for the same reason.

**Why.** Kernel B lists kernel A in `kernel_sources`. Kaggle mounts the latest *successfully
completed* version of A. The 17 Sep full run ended `CANCEL_ACKNOWLEDGED`, so the version before
it — the smoke run — is what got mounted. `kaggle kernels output` *does* return a cancelled run's
files, which is why we have the real adapter on the laptop but the kernel did not.

**Why nothing caught it.** Every check inside kernel B is self-consistent: the adapter loaded, it
matched the (smoke) `trainer_state.json` it found next to it, outputs were non-empty and
untruncated. No check compared what the kernel ran against what *we* intended to run.

**What run 2 does tell us** (`reports/run2_smoke_adapter_18sep/report.pdf`, red banner):

| split | n | R-L (smoke adapter) | R-L run 1 (real adapter, old decoding) | len ratio | truncated |
|---|---|---|---|---|---|
| aci_bench taskB-1 / C-2 / C-3 | 40 each | 32.4 / 32.3 / 31.2 | 17.4–17.9 | 0.97–1.05 | 1 / 0 / 1 |
| mts_dialog chat-2023 | 200 | 24.5 | 35.8 | 3.31 | 0 |
| mts_dialog sum-2023 | 200 | 24.4 | 33.5 | 3.13 | 0 |
| dialogue_soap test | 250 | 25.6 | — | 0.57 | 0 |

- Decoding fix confirmed: the repetition loops are gone, ACI-Bench notes end at the right length,
  2 of 770 truncated. This holds regardless of the adapter.
- The MTS-Dialog collapse (35.8 → 24.5, outputs 3× too long) and short SOAP notes are what a
  20-step adapter looks like — a reminder that the 332-step adapter is doing real work.
- Zero-shot base control on the same 20 val items: ROUGE-L 21.2 vs 26.7 for the smoke adapter.
- **None of the run-2 numbers are baseline numbers.** They are kept under
  `outputs/kaggle_run2_smoke_adapter/` and `reports/run2_smoke_adapter_18sep/`, both labelled.

**Fix (in the repo, 19 Sep morning).**

| where | change |
|---|---|
| `kaggle/adapter/dataset-metadata.json` + `fetch_kaggle_run.py --stage adapter` | the 17 Sep `final/` + `trainer_state.json` are uploaded as the private dataset `hirthick17/medsum-baseline-adapter` (~185 MB); kernel B lists it in `dataset_sources` |
| `kaggle/infer/baseline_infer.py` | prefers `/kaggle/input/datasets/**/final/` over the notebook mount; refuses a `*_smoke` path in full mode; `EXPECTED_ADAPTER_SHA256 = 14e71261…` — any other adapter stops the kernel in minute 1, not hour 4 |
| `scripts/fetch_kaggle_run.py` | kernel B's output is downloaded to a staging dir and merged into `outputs/kaggle/` only if the sha kernel B hashed equals the local `final/adapter_model.safetensors` (run 2 would otherwise have overwritten the real `trainer_state.json`) |
| `scripts/make_report.py` | first line of the §10 handoff checklist is now "adapter used for generation == final/ (sha256)"; a mismatch, or a `*_smoke` checkpoint under `mode=full`, puts a red **NOT THE BASELINE** banner on page 1; auto-detect refuses when several runs exist under `outputs/` |

**Next step:** `python scripts/fetch_kaggle_run.py --stage adapter` (upload, ~5 min), then
`python scripts/fetch_kaggle_run.py --stage infer --push` (≈ 4 h; downloads, verifies, builds the
report). Kaggle GPU quota used this week: ≈ 12 h (run 1) + 3.8 h (run 2) of 30 h; the re-run
takes ≈ 4 h more.

## How we solved it (all in the repo as of 18 Sep)

**Two kernels instead of one.**

| kernel | Kaggle id | does | budget |
|---|---|---|---|
| A `kaggle/baseline/` | `hirthick17/medsum-baseline-qlora` | trains only → `final/`, `trainer_state.json`, `train_summary.json` | guard at 10.5 h (≈ 1.75 epochs), save fits easily |
| B `kaggle/infer/` | `hirthick17/medsum-baseline-infer` | loads the adapter from the dataset `hirthick17/medsum-baseline-adapter` (sha256-pinned; see Run 2), runs the §7 checks + zero-shot base control, generates all 6 splits, writes `training_config.json` | ~4 h (measured 3.8 h) |

Both write the same output path, so downloading both gives one merged folder that the report
script reads. **B can be re-run in ~4 h to change decoding without retraining.** (The original
plan had B mount A's output directly via `kernel_sources`; see Run 2 for why that was replaced by
an explicit adapter dataset.)

**Decoding fixes in kernel B** (REVIEW2_BASELINE.md §8.2):
- `max_new_tokens` 768 → **1024** — ACI-Bench references reach ~1,020 tokens; 768 was clipping
  ~15 % of correct-length notes even without loops.
- `repetition_penalty` 1.1 → **1.2**.
- **6-gram repeat block on generated tokens only.** HF's built-in `no_repeat_ngram_size` also
  forbids copying a 6-gram from the transcript ("metformin 500 mg twice a day"), which a faithful
  note must do — so we use a custom processor that only looks at what the model has generated.

**Tooling:**
- `scripts/fetch_kaggle_run.py` now drives both kernels (wait for A → download → push B → wait →
  download → report), every stage idempotent — if the poller dies again, rerun it, nothing is lost.
- `scripts/make_report.py` reads the merged output and shows the decoding actually used.
- B rebuilds the training half of `training_config.json` from `trainer_state.json` when given
  pre-split output (the 17 Sep run has no `train_summary.json`).

## What this means for you

**Person 3 (evaluation):** expect the handoff (`outputs/…/predictions/baseline_qlora/*.jsonl`,
6 files / 770 lines, plus `training_config.json` and the PDF) once kernel B has been re-run with
the right adapter — target evening of 19 Sep. Do not use anything from
`outputs/kaggle_run2_smoke_adapter/`. Schema unchanged (§8.3); two new fields inside `decoding`
(`no_repeat_ngram_size_generated_only`, `num_beams`). The `truncated` flag is still there; expect
far fewer `true` on ACI-Bench. There is also a `predictions/zeroshot_base/val_check.jsonl` — the
un-adapted base model on the same 20 val items, a free control row for the results table.

**Everyone:** the adapter we hand over is the **1.24-epoch** one from 17 Sep. Retraining with the
new 10.5 h guard would give ~1.75 epochs and a properly completed cosine schedule, but costs
~11 h + 2.5 h of the 30 h/week Kaggle GPU quota (run 1 used ~12 h; B uses ~2.5 h). Proposal: ship
DA2 on the 17 Sep adapter with the fixed decoding; retrain only if the quota and calendar allow
before the 20th. Objections → say so today.

**Review 3 note:** the long-note weakness is a data-mix issue (1.6 % ACI-Bench) that no decoding
setting fixes. Up-weighting ACI-Bench / adding its augmented splits goes on the Review 3 list.

## Timeline vs plan

| Appendix A | planned | actual |
|---|---|---|
| Full training run | 16 Sep | 17 Sep 22:12 → done ~05:45 18 Sep |
| §7 checks on val | 17 Sep | 18 Sep (in-run; re-done in kernel B) |
| §8 generation, 6 splits | 18 Sep | 5/6 on 18 Sep morning (run 1); all 6 on 19 Sep 00:10 but wrong adapter (run 2); re-run 19 Sep |
| §10 handoff | 19 Sep | 19 Sep evening (best case) |
| Buffer / submission | 20 Sep | unchanged |
