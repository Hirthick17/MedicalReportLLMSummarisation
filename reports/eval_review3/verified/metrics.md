# Evaluation — verified

Run: `..\medsum-fact\outputs\kaggle_review3\outputs\review3`  ·  generated 2026-10-28 15:14  ·  decoding: `{"max_new_tokens": 1024, "do_sample": false, "repetition_penalty": 1.1}`

## Standard metrics (mean over items, ×100; ROUGE F1 with stemming; BERTScore F1 rescaled)

| split | n | ROUGE-1 | ROUGE-2 | ROUGE-L | ROUGE-Lsum | BERTScore | len ratio | truncated | degenerate | ROUGE-L excl. degenerate |
|---|---|---|---|---|---|---|---|---|---|---|
| aci_bench_test_taskB_1 | 40 | 48.4 | 20.2 | **28.5** | 44.3 | 19.6 | 0.58 | 0 | 0 | 28.5 (n=40) |
| aci_bench_test_taskC_2 | 40 | 48.2 | 20.6 | **27.9** | 44.2 | 17.9 | 0.55 | 0 | 0 | 27.9 (n=40) |
| aci_bench_test_taskC_3 | 40 | 46.6 | 19.8 | **27.1** | 43.3 | 17.0 | 0.52 | 0 | 0 | 27.1 (n=40) |
| mts_dialog_test_chat_2023 | 200 | 30.3 | 11.8 | **23.6** | 24.8 | 21.7 | 3.85 | 0 | 0 | 23.6 (n=200) |
| mts_dialog_test_sum_2023 | 200 | 27.8 | 9.3 | **21.0** | 22.5 | 20.8 | 3.50 | 0 | 0 | 21.0 (n=200) |

## Factuality (mean of per-item rates ×100; micro = pooled over all entities of the split)

| split | n | hallucination ↓ | halluc. strict ↓ | micro halluc. ↓ | negation-flip ↓ | micro neg-flip ↓ | numerical consistency ↑ | micro num. ↑ | clinical coverage ↑ | coverage (important) ↑ | micro coverage ↑ |
|---|---|---|---|---|---|---|---|---|---|---|---|
| aci_bench_test_taskB_1 | 40 | **10.8** | 5.9 | 10.0 | **2.9** | 2.7 | **94.2** | 93.0 | **65.0** | 63.4 | 64.5 |
| aci_bench_test_taskC_2 | 40 | **7.1** | 2.5 | 7.4 | **4.0** | 5.3 | **91.9** | 91.1 | **68.1** | 68.8 | 66.9 |
| aci_bench_test_taskC_3 | 40 | **8.3** | 3.8 | 7.4 | **4.6** | 5.1 | **94.8** | 92.6 | **63.6** | 63.2 | 62.2 |
| mts_dialog_test_chat_2023 | 200 | **10.6** | 7.5 | 9.4 | **7.4** | 7.7 | **87.5** | 80.3 | **70.7** | 70.4 | 64.0 |
| mts_dialog_test_sum_2023 | 200 | **18.1** | 13.3 | 15.1 | **4.7** | 4.3 | **82.9** | 79.3 | **50.7** | 52.8 | 47.9 |

## Coverage by category (×100, mean per item)

| split | symptom | medical history | diagnosis | medication | investigation |
|---|---|---|---|---|---|
| aci_bench_test_taskB_1 | 62.6 | 61.3 | 61.5 | 71.5 | 72.0 |
| aci_bench_test_taskC_2 | 62.3 | 85.7 | 74.8 | 72.9 | 70.3 |
| aci_bench_test_taskC_3 | 62.8 | 75.3 | 69.0 | 64.7 | 68.0 |
| mts_dialog_test_chat_2023 | 73.7 | 61.9 | 59.6 | 73.3 | 54.7 |
| mts_dialog_test_sum_2023 | 54.7 | 52.2 | 41.6 | 62.0 | 20.6 |

## Error counts (items affected / total occurrences)

| split | n | hallucinated entities | incorrect diagnosis | missing diagnosis | incorrect medication | missing medication | dosage mismatch | negation flips | numerical errors |
|---|---|---|---|---|---|---|---|---|---|
| aci_bench_test_taskB_1 | 40 | 56 / 560 pred. entities | 1 / 1 | 14 | 0 / 0 | 17 | 3 / 3 | 7 / 9 | 10 / 15 |
| aci_bench_test_taskC_2 | 40 | 43 / 582 pred. entities | 0 / 0 | 12 | 0 / 0 | 18 | 2 / 2 | 12 / 20 | 13 / 23 |
| aci_bench_test_taskC_3 | 40 | 46 / 618 pred. entities | 3 / 3 | 17 | 0 / 0 | 22 | 0 / 0 | 13 / 20 | 10 / 16 |
| mts_dialog_test_chat_2023 | 200 | 43 / 459 pred. entities | 2 / 2 | 4 | 0 / 0 | 13 | 0 / 0 | 16 / 23 | 13 / 29 |
| mts_dialog_test_sum_2023 | 200 | 52 / 344 pred. entities | 3 / 3 | 6 | 2 / 2 | 13 | 0 / 0 | 6 / 9 | 19 / 34 |

## Headline (five official test splits pooled, item mean ×100)

ROUGE-L **23.6** · hallucination rate **12.5** · negation-flip rate **5.3** · numerical consistency **88.8** · clinical coverage **62.4** (n = 520)
