# Evaluation — sft

Run: `..\medsum-fact\outputs\kaggle_run1_old_decoding\outputs\baseline_qlora_llama31_8b`  ·  generated 2026-10-28 13:32  ·  decoding: `{"max_new_tokens": 768, "do_sample": false, "repetition_penalty": 1.1}`

## Standard metrics (mean over items, ×100; ROUGE F1 with stemming; BERTScore F1 rescaled)

| split | n | ROUGE-1 | ROUGE-2 | ROUGE-L | ROUGE-Lsum | BERTScore | len ratio | truncated | degenerate | ROUGE-L excl. degenerate |
|---|---|---|---|---|---|---|---|---|---|---|
| aci_bench_test_taskB_1 | 40 | 29.3 | 11.4 | **17.9** | 26.4 | -1.8 | 1.28 | 30 | 18 | 31.2 (n=10) |
| aci_bench_test_taskC_2 | 40 | 29.7 | 12.5 | **17.6** | 27.3 | -1.6 | 1.21 | 29 | 20 | 29.6 (n=11) |
| aci_bench_test_taskC_3 | 40 | 29.7 | 11.5 | **17.4** | 27.1 | -1.9 | 1.20 | 31 | 17 | 30.1 (n=8) |
| mts_dialog_test_chat_2023 | 200 | 42.2 | 19.6 | **35.8** | 35.8 | 39.6 | 1.15 | 9 | 8 | 37.2 (n=190) |
| mts_dialog_test_sum_2023 | 200 | 40.0 | 16.2 | **33.5** | 33.5 | 38.8 | 1.02 | 2 | 3 | 33.7 (n=197) |
| val_check | 20 | 33.0 | 12.6 | **24.0** | 28.6 | 20.1 | 1.07 | 7 | 5 | 28.8 (n=13) |

## Factuality (mean of per-item rates ×100; micro = pooled over all entities of the split)

| split | n | hallucination ↓ | halluc. strict ↓ | micro halluc. ↓ | negation-flip ↓ | micro neg-flip ↓ | numerical consistency ↑ | micro num. ↑ | clinical coverage ↑ | coverage (important) ↑ | micro coverage ↑ |
|---|---|---|---|---|---|---|---|---|---|---|---|
| aci_bench_test_taskB_1 | 40 | **54.7** | 51.5 | 66.6 | **15.1** | 16.1 | **55.9** | 52.4 | **48.6** | 56.5 | 44.7 |
| aci_bench_test_taskC_2 | 40 | **46.6** | 41.5 | 63.0 | **12.9** | 11.1 | **60.9** | 53.8 | **46.1** | 53.1 | 48.2 |
| aci_bench_test_taskC_3 | 40 | **51.8** | 48.1 | 64.3 | **12.4** | 10.5 | **55.3** | 47.9 | **46.7** | 53.2 | 46.1 |
| mts_dialog_test_chat_2023 | 200 | **30.7** | 23.7 | 57.6 | **4.1** | 4.0 | **78.4** | 77.5 | **70.2** | 70.7 | 69.8 |
| mts_dialog_test_sum_2023 | 200 | **40.8** | 24.4 | 45.6 | **6.2** | 6.6 | **87.5** | 89.0 | **66.0** | 68.5 | 62.1 |
| val_check | 20 | **42.1** | 38.9 | 66.3 | **14.9** | 16.7 | **79.1** | 72.2 | **50.1** | 53.7 | 45.3 |

## Coverage by category (×100, mean per item)

| split | symptom | medical history | diagnosis | medication | investigation |
|---|---|---|---|---|---|
| aci_bench_test_taskB_1 | 58.6 | 70.1 | 48.2 | 47.6 | 26.6 |
| aci_bench_test_taskC_2 | 55.2 | 63.7 | 48.8 | 40.1 | 27.2 |
| aci_bench_test_taskC_3 | 57.2 | 72.8 | 45.5 | 39.5 | 28.6 |
| mts_dialog_test_chat_2023 | 67.4 | 66.1 | 66.3 | 78.6 | 55.5 |
| mts_dialog_test_sum_2023 | 59.9 | 69.6 | 64.9 | 70.8 | 28.3 |
| val_check | 50.8 | 76.7 | 34.2 | 60.0 | 31.3 |

## Error counts (items affected / total occurrences)

| split | n | hallucinated entities | incorrect diagnosis | missing diagnosis | incorrect medication | missing medication | dosage mismatch | negation flips | numerical errors |
|---|---|---|---|---|---|---|---|---|---|
| aci_bench_test_taskB_1 | 40 | 678 / 1018 pred. entities | 1 / 2 | 22 | 2 / 28 | 23 | 0 / 0 | 24 / 46 | 26 / 90 |
| aci_bench_test_taskC_2 | 40 | 618 / 981 pred. entities | 4 / 34 | 24 | 2 / 2 | 27 | 0 / 0 | 23 / 34 | 31 / 121 |
| aci_bench_test_taskC_3 | 40 | 710 / 1104 pred. entities | 7 / 10 | 25 | 4 / 10 | 27 | 4 / 4 | 22 / 35 | 31 / 146 |
| mts_dialog_test_chat_2023 | 200 | 468 / 812 pred. entities | 1 / 1 | 4 | 1 / 1 | 9 | 1 / 1 | 11 / 13 | 29 / 46 |
| mts_dialog_test_sum_2023 | 200 | 219 / 480 pred. entities | 1 / 1 | 3 | 3 / 3 | 9 | 0 / 0 | 13 / 18 | 15 / 16 |
| val_check | 20 | 189 / 285 pred. entities | 3 / 11 | 7 | 0 / 0 | 5 | 0 / 0 | 6 / 14 | 5 / 15 |

## Headline (five official test splits pooled, item mean ×100)

ROUGE-L **30.7** · hallucination rate **40.4** · negation-flip rate **8.2** · numerical consistency **71.1** · clinical coverage **61.3** (n = 520)
