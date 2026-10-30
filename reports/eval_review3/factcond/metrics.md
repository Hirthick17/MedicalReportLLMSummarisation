# Evaluation — factcond

Run: `..\medsum-fact\outputs\kaggle_review3\outputs\review3`  ·  generated 2026-10-28 15:13  ·  decoding: `{"max_new_tokens": 1024, "do_sample": false, "repetition_penalty": 1.1}`

## Standard metrics (mean over items, ×100; ROUGE F1 with stemming; BERTScore F1 rescaled)

| split | n | ROUGE-1 | ROUGE-2 | ROUGE-L | ROUGE-Lsum | BERTScore | len ratio | truncated | degenerate | ROUGE-L excl. degenerate |
|---|---|---|---|---|---|---|---|---|---|---|
| aci_bench_test_taskB_1 | 40 | 54.0 | 22.2 | **30.4** | 49.3 | 22.9 | 0.79 | 0 | 0 | 30.4 (n=40) |
| aci_bench_test_taskC_2 | 40 | 53.6 | 22.4 | **29.5** | 48.5 | 21.2 | 0.75 | 0 | 0 | 29.5 (n=40) |
| aci_bench_test_taskC_3 | 40 | 53.9 | 22.0 | **29.1** | 49.6 | 21.5 | 0.73 | 0 | 0 | 29.1 (n=40) |
| mts_dialog_test_chat_2023 | 200 | 30.9 | 12.1 | **23.6** | 25.1 | 22.6 | 4.65 | 0 | 0 | 23.6 (n=200) |
| mts_dialog_test_sum_2023 | 200 | 29.2 | 10.0 | **21.2** | 23.0 | 22.3 | 4.56 | 0 | 0 | 21.2 (n=200) |

## Factuality (mean of per-item rates ×100; micro = pooled over all entities of the split)

| split | n | hallucination ↓ | halluc. strict ↓ | micro halluc. ↓ | negation-flip ↓ | micro neg-flip ↓ | numerical consistency ↑ | micro num. ↑ | clinical coverage ↑ | coverage (important) ↑ | micro coverage ↑ |
|---|---|---|---|---|---|---|---|---|---|---|---|
| aci_bench_test_taskB_1 | 40 | **11.5** | 6.3 | 10.8 | **4.5** | 4.0 | **94.0** | 92.4 | **77.2** | 77.8 | 75.7 |
| aci_bench_test_taskC_2 | 40 | **9.9** | 5.0 | 9.4 | **4.5** | 5.9 | **91.1** | 90.7 | **78.3** | 80.2 | 77.9 |
| aci_bench_test_taskC_3 | 40 | **10.3** | 5.0 | 9.3 | **5.1** | 5.4 | **93.8** | 92.1 | **76.0** | 76.7 | 74.8 |
| mts_dialog_test_chat_2023 | 200 | **11.7** | 8.8 | 11.1 | **5.9** | 6.4 | **84.8** | 80.4 | **78.6** | 79.3 | 74.0 |
| mts_dialog_test_sum_2023 | 200 | **20.2** | 15.4 | 16.9 | **4.8** | 5.1 | **83.9** | 81.0 | **64.1** | 66.3 | 68.2 |

## Coverage by category (×100, mean per item)

| split | symptom | medical history | diagnosis | medication | investigation |
|---|---|---|---|---|---|
| aci_bench_test_taskB_1 | 74.9 | 85.4 | 74.1 | 85.5 | 75.5 |
| aci_bench_test_taskC_2 | 74.6 | 85.7 | 81.6 | 92.8 | 77.7 |
| aci_bench_test_taskC_3 | 75.9 | 83.2 | 78.7 | 79.1 | 76.0 |
| mts_dialog_test_chat_2023 | 79.0 | 75.0 | 69.9 | 90.4 | 58.9 |
| mts_dialog_test_sum_2023 | 62.5 | 75.3 | 67.0 | 92.6 | 47.2 |

## Error counts (items affected / total occurrences)

| split | n | hallucinated entities | incorrect diagnosis | missing diagnosis | incorrect medication | missing medication | dosage mismatch | negation flips | numerical errors |
|---|---|---|---|---|---|---|---|---|---|
| aci_bench_test_taskB_1 | 40 | 72 / 666 pred. entities | 3 / 3 | 9 | 0 / 0 | 10 | 3 / 3 | 12 / 16 | 11 / 18 |
| aci_bench_test_taskC_2 | 40 | 66 / 703 pred. entities | 0 / 0 | 8 | 0 / 0 | 5 | 4 / 4 | 15 / 26 | 17 / 27 |
| aci_bench_test_taskC_3 | 40 | 71 / 766 pred. entities | 5 / 6 | 13 | 0 / 0 | 15 | 1 / 1 | 17 / 26 | 12 / 20 |
| mts_dialog_test_chat_2023 | 200 | 60 / 541 pred. entities | 2 / 2 | 4 | 2 / 2 | 7 | 0 / 0 | 15 / 22 | 22 / 38 |
| mts_dialog_test_sum_2023 | 200 | 79 / 467 pred. entities | 5 / 6 | 2 | 2 / 2 | 6 | 0 / 0 | 11 / 15 | 25 / 41 |

## Headline (five official test splits pooled, item mean ×100)

ROUGE-L **24.1** · hallucination rate **14.2** · negation-flip rate **5.1** · numerical consistency **87.9** · clinical coverage **73.4** (n = 520)
