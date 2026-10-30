# Evaluation — sft1024

Run: `..\medsum-fact\outputs\kaggle_review3_sft\outputs\review3_sft`  ·  generated 2026-10-28 22:28  ·  decoding: `{"max_new_tokens": 1024, "do_sample": false, "repetition_penalty": 1.1}`

## Standard metrics (mean over items, ×100; ROUGE F1 with stemming; BERTScore F1 rescaled)

| split | n | ROUGE-1 | ROUGE-2 | ROUGE-L | ROUGE-Lsum | BERTScore | len ratio | truncated | degenerate | ROUGE-L excl. degenerate |
|---|---|---|---|---|---|---|---|---|---|---|
| aci_bench_test_taskB_1 | 40 | 26.5 | 10.5 | **16.4** | 23.9 | -2.6 | 1.64 | 31 | 22 | 32.5 (n=9) |
| aci_bench_test_taskC_2 | 40 | 27.7 | 11.8 | **16.4** | 25.4 | -1.5 | 1.53 | 28 | 24 | 29.6 (n=12) |
| aci_bench_test_taskC_3 | 40 | 27.6 | 11.0 | **16.5** | 25.1 | -2.6 | 1.54 | 30 | 24 | 29.0 (n=9) |
| mts_dialog_test_chat_2023 | 200 | 42.1 | 19.7 | **35.6** | 35.6 | 42.5 | 1.23 | 10 | 9 | 37.3 (n=189) |
| mts_dialog_test_sum_2023 | 200 | 40.0 | 16.2 | **33.5** | 33.5 | 43.1 | 1.03 | 2 | 3 | 33.8 (n=197) |

## Factuality (mean of per-item rates ×100; micro = pooled over all entities of the split)

| split | n | hallucination ↓ | halluc. strict ↓ | micro halluc. ↓ | negation-flip ↓ | micro neg-flip ↓ | numerical consistency ↑ | micro num. ↑ | clinical coverage ↑ | coverage (important) ↑ | micro coverage ↑ |
|---|---|---|---|---|---|---|---|---|---|---|---|
| aci_bench_test_taskB_1 | 40 | **57.1** | 54.2 | 69.6 | **15.8** | 16.6 | **57.6** | 52.9 | **48.2** | 55.9 | 44.7 |
| aci_bench_test_taskC_2 | 40 | **46.9** | 42.0 | 63.6 | **13.3** | 11.7 | **61.0** | 53.6 | **46.3** | 53.2 | 48.5 |
| aci_bench_test_taskC_3 | 40 | **51.2** | 47.8 | 63.8 | **12.0** | 11.0 | **54.2** | 44.3 | **47.1** | 53.8 | 46.6 |
| mts_dialog_test_chat_2023 | 200 | **30.9** | 23.9 | 58.0 | **4.1** | 4.0 | **78.4** | 77.1 | **70.2** | 70.7 | 69.8 |
| mts_dialog_test_sum_2023 | 200 | **40.8** | 24.4 | 45.6 | **6.2** | 6.6 | **87.5** | 89.0 | **66.0** | 68.5 | 62.1 |

## Coverage by category (×100, mean per item)

| split | symptom | medical history | diagnosis | medication | investigation |
|---|---|---|---|---|---|
| aci_bench_test_taskB_1 | 58.4 | 70.1 | 46.2 | 46.2 | 27.3 |
| aci_bench_test_taskC_2 | 55.7 | 63.7 | 48.8 | 39.2 | 29.7 |
| aci_bench_test_taskC_3 | 56.8 | 72.8 | 45.9 | 43.1 | 28.4 |
| mts_dialog_test_chat_2023 | 67.4 | 66.1 | 66.3 | 78.6 | 55.5 |
| mts_dialog_test_sum_2023 | 59.9 | 69.6 | 64.9 | 70.8 | 28.3 |

## Error counts (items affected / total occurrences)

| split | n | hallucinated entities | incorrect diagnosis | missing diagnosis | incorrect medication | missing medication | dosage mismatch | negation flips | numerical errors |
|---|---|---|---|---|---|---|---|---|---|
| aci_bench_test_taskB_1 | 40 | 775 / 1114 pred. entities | 0 / 0 | 23 | 2 / 45 | 23 | 0 / 0 | 24 / 47 | 25 / 89 |
| aci_bench_test_taskC_2 | 40 | 644 / 1012 pred. entities | 4 / 35 | 24 | 2 / 2 | 28 | 0 / 0 | 24 / 36 | 31 / 124 |
| aci_bench_test_taskC_3 | 40 | 705 / 1105 pred. entities | 6 / 9 | 24 | 4 / 10 | 26 | 4 / 4 | 20 / 37 | 31 / 162 |
| mts_dialog_test_chat_2023 | 200 | 474 / 817 pred. entities | 1 / 1 | 4 | 1 / 1 | 9 | 1 / 1 | 11 / 13 | 29 / 47 |
| mts_dialog_test_sum_2023 | 200 | 219 / 480 pred. entities | 1 / 1 | 3 | 3 / 3 | 9 | 0 / 0 | 13 / 18 | 15 / 16 |

## Headline (five official test splits pooled, item mean ×100)

ROUGE-L **30.4** · hallucination rate **40.6** · negation-flip rate **8.3** · numerical consistency **71.2** · clinical coverage **61.4** (n = 520)
