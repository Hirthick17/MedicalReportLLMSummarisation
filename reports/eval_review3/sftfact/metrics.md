# Evaluation — sftfact

Run: `..\medsum-fact\outputs\kaggle_review3_sft\outputs\review3_sft`  ·  generated 2026-10-28 22:28  ·  decoding: `{"max_new_tokens": 1024, "do_sample": false, "repetition_penalty": 1.1}`

## Standard metrics (mean over items, ×100; ROUGE F1 with stemming; BERTScore F1 rescaled)

| split | n | ROUGE-1 | ROUGE-2 | ROUGE-L | ROUGE-Lsum | BERTScore | len ratio | truncated | degenerate | ROUGE-L excl. degenerate |
|---|---|---|---|---|---|---|---|---|---|---|
| aci_bench_test_taskB_1 | 40 | 21.7 | 8.2 | **12.9** | 19.4 | -9.5 | 1.76 | 34 | 28 | 31.7 (n=5) |
| aci_bench_test_taskC_2 | 40 | 21.9 | 8.6 | **13.1** | 20.0 | -10.6 | 1.58 | 33 | 27 | 26.8 (n=7) |
| aci_bench_test_taskC_3 | 40 | 23.3 | 8.7 | **13.8** | 21.3 | -10.6 | 1.42 | 30 | 27 | 27.2 (n=8) |
| mts_dialog_test_chat_2023 | 200 | 40.0 | 18.5 | **33.8** | 33.8 | 41.8 | 1.26 | 7 | 7 | 34.9 (n=192) |
| mts_dialog_test_sum_2023 | 200 | 37.8 | 16.0 | **31.1** | 31.1 | 40.3 | 1.35 | 10 | 10 | 32.5 (n=189) |

## Factuality (mean of per-item rates ×100; micro = pooled over all entities of the split)

| split | n | hallucination ↓ | halluc. strict ↓ | micro halluc. ↓ | negation-flip ↓ | micro neg-flip ↓ | numerical consistency ↑ | micro num. ↑ | clinical coverage ↑ | coverage (important) ↑ | micro coverage ↑ |
|---|---|---|---|---|---|---|---|---|---|---|---|
| aci_bench_test_taskB_1 | 40 | **48.1** | 44.8 | 67.1 | **15.5** | 15.0 | **59.9** | 56.6 | **51.5** | 61.3 | 49.2 |
| aci_bench_test_taskC_2 | 40 | **53.9** | 50.8 | 66.9 | **17.4** | 17.2 | **63.2** | 54.4 | **50.5** | 59.6 | 51.0 |
| aci_bench_test_taskC_3 | 40 | **51.5** | 48.0 | 65.7 | **20.3** | 18.5 | **64.8** | 54.4 | **50.1** | 60.0 | 48.8 |
| mts_dialog_test_chat_2023 | 200 | **23.6** | 18.1 | 46.4 | **8.8** | 10.2 | **82.0** | 81.8 | **71.5** | 72.9 | 72.4 |
| mts_dialog_test_sum_2023 | 200 | **33.0** | 18.9 | 56.7 | **7.9** | 10.1 | **79.2** | 81.2 | **68.1** | 71.6 | 65.6 |

## Coverage by category (×100, mean per item)

| split | symptom | medical history | diagnosis | medication | investigation |
|---|---|---|---|---|---|
| aci_bench_test_taskB_1 | 67.9 | 73.7 | 53.6 | 41.4 | 21.0 |
| aci_bench_test_taskC_2 | 65.5 | 69.7 | 44.6 | 53.0 | 26.8 |
| aci_bench_test_taskC_3 | 61.0 | 68.4 | 57.1 | 50.2 | 21.5 |
| mts_dialog_test_chat_2023 | 65.9 | 69.3 | 74.6 | 67.2 | 49.7 |
| mts_dialog_test_sum_2023 | 69.4 | 71.7 | 64.1 | 54.9 | 27.2 |

## Error counts (items affected / total occurrences)

| split | n | hallucinated entities | incorrect diagnosis | missing diagnosis | incorrect medication | missing medication | dosage mismatch | negation flips | numerical errors |
|---|---|---|---|---|---|---|---|---|---|
| aci_bench_test_taskB_1 | 40 | 775 / 1155 pred. entities | 4 / 15 | 19 | 3 / 4 | 24 | 0 / 0 | 27 / 47 | 23 / 63 |
| aci_bench_test_taskC_2 | 40 | 832 / 1244 pred. entities | 3 / 3 | 25 | 4 / 4 | 20 | 3 / 3 | 26 / 58 | 28 / 99 |
| aci_bench_test_taskC_3 | 40 | 870 / 1324 pred. entities | 6 / 17 | 17 | 4 / 25 | 21 | 1 / 1 | 25 / 69 | 26 / 103 |
| mts_dialog_test_chat_2023 | 200 | 333 / 717 pred. entities | 0 / 0 | 2 | 2 / 2 | 13 | 0 / 0 | 20 / 35 | 24 / 30 |
| mts_dialog_test_sum_2023 | 200 | 401 / 707 pred. entities | 0 / 0 | 2 | 3 / 3 | 15 | 0 / 0 | 18 / 29 | 25 / 31 |

## Headline (five official test splits pooled, item mean ×100)

ROUGE-L **28.0** · hallucination rate **35.3** · negation-flip rate **11.7** · numerical consistency **72.4** · clinical coverage **63.6** (n = 520)
