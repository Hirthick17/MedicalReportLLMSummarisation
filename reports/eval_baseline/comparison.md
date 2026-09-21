# Baseline comparison across runs / decoding configurations

All numbers ×100, item means. Runs:

- **run1_rep1.1**: `outputs\kaggle_run1_old_decoding\outputs\baseline_qlora_llama31_8b` · decoding `{"max_new_tokens": 768, "do_sample": false, "repetition_penalty": 1.1}`
- **run3_rep1.2_ngram6**: `outputs\kaggle\outputs\baseline_qlora_llama31_8b` · decoding `{"max_new_tokens": 1024, "do_sample": false, "num_beams": 1, "repetition_penalty": 1.2, "no_repeat_ngram_size_generated_only": 6, "eos_token_id": [128009], "batch": 4, "adapter": "final", "non_quantised_params_fp32": true}`

## ROUGE-L ↑

| split | run1_rep1.1 | run3_rep1.2_ngram6 |
|---|---|---|
| aci_bench_test_taskB_1 | 17.9 | 11.4 |
| aci_bench_test_taskC_2 | 17.6 | 10.9 |
| aci_bench_test_taskC_3 | 17.4 | 12.3 |
| mts_dialog_test_chat_2023 | 35.8 | 29.7 |
| mts_dialog_test_sum_2023 | 33.5 | 28.6 |
| dialogue_soap_test | — | 29.7 |
| val_check | 24.0 | 14.7 |
| zeroshot_base/val_check | — | 21.2 |

## BERTScore ↑

| split | run1_rep1.1 | run3_rep1.2_ngram6 |
|---|---|---|
| aci_bench_test_taskB_1 | -1.8 | -13.6 |
| aci_bench_test_taskC_2 | -1.6 | -16.4 |
| aci_bench_test_taskC_3 | -1.9 | -14.8 |
| mts_dialog_test_chat_2023 | 39.6 | 30.7 |
| mts_dialog_test_sum_2023 | 38.8 | 30.7 |
| dialogue_soap_test | — | 26.3 |
| val_check | 20.1 | 7.5 |
| zeroshot_base/val_check | — | 16.2 |

## hallucination ↓

| split | run1_rep1.1 | run3_rep1.2_ngram6 |
|---|---|---|
| aci_bench_test_taskB_1 | 54.7 | 77.9 |
| aci_bench_test_taskC_2 | 46.6 | 82.6 |
| aci_bench_test_taskC_3 | 51.8 | 78.2 |
| mts_dialog_test_chat_2023 | 30.7 | 44.3 |
| mts_dialog_test_sum_2023 | 40.8 | 56.7 |
| dialogue_soap_test | — | 48.6 |
| val_check | 42.1 | 72.9 |
| zeroshot_base/val_check | — | 18.0 |

## negation-flip ↓

| split | run1_rep1.1 | run3_rep1.2_ngram6 |
|---|---|---|
| aci_bench_test_taskB_1 | 15.1 | 15.1 |
| aci_bench_test_taskC_2 | 12.9 | 17.5 |
| aci_bench_test_taskC_3 | 12.4 | 20.7 |
| mts_dialog_test_chat_2023 | 4.1 | 6.5 |
| mts_dialog_test_sum_2023 | 6.2 | 6.0 |
| dialogue_soap_test | — | 3.6 |
| val_check | 14.9 | 6.7 |
| zeroshot_base/val_check | — | 14.4 |

## numerical consistency ↑

| split | run1_rep1.1 | run3_rep1.2_ngram6 |
|---|---|---|
| aci_bench_test_taskB_1 | 55.9 | 66.4 |
| aci_bench_test_taskC_2 | 60.9 | 52.2 |
| aci_bench_test_taskC_3 | 55.3 | 71.0 |
| mts_dialog_test_chat_2023 | 78.4 | 80.2 |
| mts_dialog_test_sum_2023 | 87.5 | 78.8 |
| dialogue_soap_test | — | 74.3 |
| val_check | 79.1 | 76.9 |
| zeroshot_base/val_check | — | 73.4 |

## clinical coverage ↑

| split | run1_rep1.1 | run3_rep1.2_ngram6 |
|---|---|---|
| aci_bench_test_taskB_1 | 48.6 | 46.7 |
| aci_bench_test_taskC_2 | 46.1 | 47.2 |
| aci_bench_test_taskC_3 | 46.7 | 50.8 |
| mts_dialog_test_chat_2023 | 70.2 | 56.6 |
| mts_dialog_test_sum_2023 | 66.0 | 56.8 |
| dialogue_soap_test | — | 70.7 |
| val_check | 50.1 | 40.0 |
| zeroshot_base/val_check | — | 71.6 |

## length ratio

| split | run1_rep1.1 | run3_rep1.2_ngram6 |
|---|---|---|
| aci_bench_test_taskB_1 | 1.28 | 1.28 |
| aci_bench_test_taskC_2 | 1.21 | 1.11 |
| aci_bench_test_taskC_3 | 1.20 | 1.02 |
| mts_dialog_test_chat_2023 | 1.15 | 1.85 |
| mts_dialog_test_sum_2023 | 1.02 | 1.36 |
| dialogue_soap_test | — | 0.97 |
| val_check | 1.07 | 1.29 |
| zeroshot_base/val_check | — | 2.71 |

## Truncated / degenerate outputs

| split | run1_rep1.1 trunc / degen | run3_rep1.2_ngram6 trunc / degen |
|---|---|---|
| aci_bench_test_taskB_1 | 30 / 18 (n=40) | 29 / 21 (n=40) |
| aci_bench_test_taskC_2 | 29 / 20 (n=40) | 28 / 25 (n=40) |
| aci_bench_test_taskC_3 | 31 / 17 (n=40) | 27 / 25 (n=40) |
| mts_dialog_test_chat_2023 | 9 / 8 (n=200) | 5 / 17 (n=200) |
| mts_dialog_test_sum_2023 | 2 / 3 (n=200) | 6 / 12 (n=200) |
| dialogue_soap_test | — | 7 / 7 (n=250) |
| val_check | 7 / 5 (n=20) | 9 / 9 (n=20) |
| zeroshot_base/val_check | — | 0 / 0 (n=20) |