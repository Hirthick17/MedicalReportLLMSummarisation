# Evaluation — run3_rep1.2_ngram6

Run: `outputs\kaggle\outputs\baseline_qlora_llama31_8b`  ·  generated 2026-09-21 23:52  ·  decoding: `{"max_new_tokens": 1024, "do_sample": false, "num_beams": 1, "repetition_penalty": 1.2, "no_repeat_ngram_size_generated_only": 6, "eos_token_id": [128009], "batch": 4, "adapter": "final", "non_quantised_params_fp32": true}`

Training: `{"max_steps": 534, "steps": null, "best_step": 200, "best_eval_loss": 0.9555336236953735, "epochs_completed": 1.244}`

## Standard metrics (mean over items, ×100; ROUGE F1 with stemming; BERTScore F1 rescaled)

| split | n | ROUGE-1 | ROUGE-2 | ROUGE-L | ROUGE-Lsum | BERTScore | len ratio | truncated | degenerate | ROUGE-L excl. degenerate |
|---|---|---|---|---|---|---|---|---|---|---|
| aci_bench_test_taskB_1 | 40 | 21.9 | 6.6 | **11.4** | 19.3 | -13.6 | 1.28 | 29 | 21 | 19.9 (n=11) |
| aci_bench_test_taskC_2 | 40 | 20.9 | 6.2 | **10.9** | 18.5 | -16.4 | 1.11 | 28 | 25 | 17.2 (n=11) |
| aci_bench_test_taskC_3 | 40 | 23.0 | 7.2 | **12.3** | 20.8 | -14.8 | 1.02 | 27 | 25 | 21.2 (n=12) |
| mts_dialog_test_chat_2023 | 200 | 34.8 | 13.7 | **29.7** | 29.7 | 30.7 | 1.85 | 5 | 17 | 31.7 (n=183) |
| mts_dialog_test_sum_2023 | 200 | 34.1 | 11.3 | **28.6** | 28.6 | 30.7 | 1.36 | 6 | 12 | 29.9 (n=188) |
| dialogue_soap_test | 250 | 46.7 | 16.4 | **29.7** | 38.5 | 26.3 | 0.97 | 7 | 7 | 30.3 (n=243) |
| val_check | 20 | 21.0 | 6.1 | **14.7** | 18.3 | 7.5 | 1.29 | 9 | 9 | 19.4 (n=11) |
| zeroshot_base/val_check | 20 | 35.8 | 11.7 | **21.2** | 30.9 | 16.2 | 2.71 | 0 | 0 | 21.2 (n=20) |

## Factuality (mean of per-item rates ×100; micro = pooled over all entities of the split)

| split | n | hallucination ↓ | halluc. strict ↓ | micro halluc. ↓ | negation-flip ↓ | micro neg-flip ↓ | numerical consistency ↑ | micro num. ↑ | clinical coverage ↑ | coverage (important) ↑ | micro coverage ↑ |
|---|---|---|---|---|---|---|---|---|---|---|---|
| aci_bench_test_taskB_1 | 40 | **77.9** | 75.3 | 87.5 | **15.1** | 14.8 | **66.4** | 46.3 | **46.7** | 51.7 | 44.5 |
| aci_bench_test_taskC_2 | 40 | **82.6** | 80.5 | 88.8 | **17.5** | 18.1 | **52.2** | 44.6 | **47.2** | 53.5 | 45.5 |
| aci_bench_test_taskC_3 | 40 | **78.2** | 75.3 | 85.9 | **20.7** | 20.5 | **71.0** | 52.5 | **50.8** | 55.8 | 47.5 |
| mts_dialog_test_chat_2023 | 200 | **44.3** | 38.8 | 79.6 | **6.5** | 9.8 | **80.2** | 75.0 | **56.6** | 58.0 | 55.5 |
| mts_dialog_test_sum_2023 | 200 | **56.7** | 42.7 | 83.5 | **6.0** | 12.0 | **78.8** | 78.2 | **56.8** | 58.6 | 53.2 |
| dialogue_soap_test | 250 | **48.6** | 41.0 | 52.9 | **3.6** | 4.0 | **74.3** | 71.4 | **70.7** | 71.6 | 69.1 |
| val_check | 20 | **72.9** | 71.7 | 89.7 | **6.7** | 11.8 | **76.9** | 59.4 | **40.0** | 45.6 | 42.0 |
| zeroshot_base/val_check | 20 | **18.0** | 14.2 | 17.4 | **14.4** | 14.5 | **73.4** | 74.5 | **71.6** | 70.5 | 73.1 |

## Coverage by category (×100, mean per item)

| split | symptom | medical history | diagnosis | medication | investigation |
|---|---|---|---|---|---|
| aci_bench_test_taskB_1 | 59.0 | 58.3 | 46.8 | 37.6 | 29.9 |
| aci_bench_test_taskC_2 | 62.2 | 53.7 | 55.3 | 26.4 | 33.6 |
| aci_bench_test_taskC_3 | 60.6 | 62.4 | 40.3 | 42.4 | 36.5 |
| mts_dialog_test_chat_2023 | 53.2 | 51.5 | 47.1 | 55.7 | 28.4 |
| mts_dialog_test_sum_2023 | 52.1 | 53.3 | 50.7 | 63.2 | 22.2 |
| dialogue_soap_test | 73.4 | 78.5 | 69.1 | 60.9 | 69.1 |
| val_check | 56.4 | 53.3 | 38.3 | 25.0 | 23.6 |
| zeroshot_base/val_check | 70.0 | 60.0 | 79.2 | 78.0 | 71.6 |

## Error counts (items affected / total occurrences)

| split | n | hallucinated entities | incorrect diagnosis | missing diagnosis | incorrect medication | missing medication | dosage mismatch | negation flips | numerical errors |
|---|---|---|---|---|---|---|---|---|---|
| aci_bench_test_taskB_1 | 40 | 2223 / 2541 pred. entities | 10 / 220 | 26 | 7 / 9 | 25 | 2 / 2 | 22 / 39 | 23 / 138 |
| aci_bench_test_taskC_2 | 40 | 2713 / 3054 pred. entities | 19 / 320 | 26 | 10 / 16 | 30 | 2 / 3 | 25 / 52 | 29 / 143 |
| aci_bench_test_taskC_3 | 40 | 2458 / 2861 pred. entities | 20 / 280 | 24 | 10 / 68 | 26 | 5 / 6 | 28 / 68 | 19 / 121 |
| mts_dialog_test_chat_2023 | 200 | 1048 / 1316 pred. entities | 7 / 133 | 5 | 2 / 2 | 16 | 0 / 0 | 14 / 26 | 23 / 39 |
| mts_dialog_test_sum_2023 | 200 | 1057 / 1266 pred. entities | 6 / 169 | 6 | 9 / 10 | 12 | 1 / 1 | 12 / 28 | 23 / 32 |
| dialogue_soap_test | 250 | 2463 / 4657 pred. entities | 152 / 359 | 96 | 49 / 69 | 72 | 15 / 27 | 43 / 56 | 151 / 407 |
| val_check | 20 | 725 / 808 pred. entities | 5 / 126 | 6 | 1 / 2 | 9 | 0 / 0 | 4 / 9 | 7 / 26 |
| zeroshot_base/val_check | 20 | 33 / 190 pred. entities | 3 / 3 | 1 | 0 / 0 | 3 | 0 / 0 | 5 / 17 | 11 / 24 |

## Headline (five official test splits pooled, item mean ×100)

ROUGE-L **25.1** · hallucination rate **59.3** · negation-flip rate **10.7** · numerical consistency **72.0** · clinical coverage **54.0** (n = 520)
