# Evaluation — zeroshot

Run: `..\medsum-fact\outputs\kaggle_review3\outputs\review3`  ·  generated 2026-10-28 15:10  ·  decoding: `{"max_new_tokens": 1024, "do_sample": false, "repetition_penalty": 1.1}`

## Standard metrics (mean over items, ×100; ROUGE F1 with stemming; BERTScore F1 rescaled)

| split | n | ROUGE-1 | ROUGE-2 | ROUGE-L | ROUGE-Lsum | BERTScore | len ratio | truncated | degenerate | ROUGE-L excl. degenerate |
|---|---|---|---|---|---|---|---|---|---|---|
| aci_bench_test_taskB_1 | 40 | 54.8 | 22.4 | **30.8** | 50.0 | 23.3 | 0.82 | 0 | 0 | 30.8 (n=40) |
| aci_bench_test_taskC_2 | 40 | 54.2 | 22.3 | **29.7** | 49.7 | 21.8 | 0.78 | 0 | 0 | 29.7 (n=40) |
| aci_bench_test_taskC_3 | 40 | 54.2 | 22.9 | **30.7** | 50.3 | 22.1 | 0.75 | 0 | 0 | 30.7 (n=40) |
| mts_dialog_test_chat_2023 | 200 | 31.8 | 11.0 | **24.4** | 25.8 | 21.2 | 3.55 | 0 | 0 | 24.4 (n=200) |
| mts_dialog_test_sum_2023 | 200 | 33.5 | 11.7 | **25.8** | 27.4 | 23.4 | 3.52 | 0 | 0 | 25.8 (n=200) |

## Factuality (mean of per-item rates ×100; micro = pooled over all entities of the split)

| split | n | hallucination ↓ | halluc. strict ↓ | micro halluc. ↓ | negation-flip ↓ | micro neg-flip ↓ | numerical consistency ↑ | micro num. ↑ | clinical coverage ↑ | coverage (important) ↑ | micro coverage ↑ |
|---|---|---|---|---|---|---|---|---|---|---|---|
| aci_bench_test_taskB_1 | 40 | **13.7** | 8.1 | 12.7 | **3.5** | 3.3 | **85.2** | 83.0 | **78.0** | 77.0 | 76.5 |
| aci_bench_test_taskC_2 | 40 | **15.2** | 9.9 | 14.8 | **4.9** | 5.6 | **79.8** | 82.5 | **75.1** | 74.3 | 74.6 |
| aci_bench_test_taskC_3 | 40 | **14.4** | 6.9 | 14.0 | **5.7** | 5.5 | **86.2** | 84.7 | **77.2** | 75.9 | 75.8 |
| mts_dialog_test_chat_2023 | 200 | **18.0** | 13.8 | 15.6 | **4.7** | 4.3 | **87.9** | 89.8 | **70.0** | 72.0 | 69.0 |
| mts_dialog_test_sum_2023 | 200 | **23.0** | 14.1 | 19.6 | **5.2** | 3.2 | **88.8** | 83.9 | **65.8** | 67.7 | 67.1 |

## Coverage by category (×100, mean per item)

| split | symptom | medical history | diagnosis | medication | investigation |
|---|---|---|---|---|---|
| aci_bench_test_taskB_1 | 70.6 | 77.2 | 82.0 | 90.0 | 81.3 |
| aci_bench_test_taskC_2 | 62.7 | 86.7 | 81.6 | 93.5 | 80.8 |
| aci_bench_test_taskC_3 | 74.3 | 75.8 | 76.2 | 86.3 | 81.5 |
| mts_dialog_test_chat_2023 | 74.5 | 53.4 | 62.3 | 91.9 | 47.1 |
| mts_dialog_test_sum_2023 | 68.5 | 69.5 | 65.7 | 80.6 | 51.1 |

## Error counts (items affected / total occurrences)

| split | n | hallucinated entities | incorrect diagnosis | missing diagnosis | incorrect medication | missing medication | dosage mismatch | negation flips | numerical errors |
|---|---|---|---|---|---|---|---|---|---|
| aci_bench_test_taskB_1 | 40 | 86 / 675 pred. entities | 4 / 4 | 9 | 3 / 3 | 7 | 4 / 4 | 11 / 13 | 24 / 52 |
| aci_bench_test_taskC_2 | 40 | 101 / 684 pred. entities | 3 / 4 | 8 | 0 / 0 | 8 | 2 / 2 | 16 / 23 | 29 / 60 |
| aci_bench_test_taskC_3 | 40 | 108 / 773 pred. entities | 5 / 6 | 13 | 0 / 0 | 9 | 4 / 4 | 16 / 26 | 23 / 46 |
| mts_dialog_test_chat_2023 | 200 | 77 / 493 pred. entities | 4 / 5 | 2 | 0 / 0 | 7 | 0 / 0 | 13 / 14 | 16 / 18 |
| mts_dialog_test_sum_2023 | 200 | 87 / 443 pred. entities | 4 / 4 | 1 | 1 / 1 | 6 | 0 / 0 | 8 / 9 | 19 / 35 |

## Headline (five official test splits pooled, item mean ×100)

ROUGE-L **26.3** · hallucination rate **18.6** · negation-flip rate **4.9** · numerical consistency **86.3** · clinical coverage **70.8** (n = 520)
