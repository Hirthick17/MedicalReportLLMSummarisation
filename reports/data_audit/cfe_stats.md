# Clinical fact extraction — corpus statistics

Generated 2026-09-21 23:54; total 590.7 s on CPU.

| split | n | src facts/doc | ref facts/doc | ref negation rate | src uncertain rate | ref entities found in src | dosage→drug link | ms/rec |
|---|---|---|---|---|---|---|---|---|
| aci_bench/train | 67 | 64.2 | 58.9 | 0.132 | 0.197 | 0.839 | 0.857 | 120.6 |
| aci_bench/validation | 20 | 63.9 | 58.5 | 0.132 | 0.193 | 0.847 | 0.914 | 117.4 |
| aci_bench/test_taskB_1 | 40 | 60.1 | 56.5 | 0.139 | 0.199 | 0.832 | 0.931 | 118.2 |
| aci_bench/test_taskC_2 | 40 | 69.2 | 60.2 | 0.136 | 0.206 | 0.836 | 0.833 | 130.2 |
| aci_bench/test_taskC_3 | 40 | 68.8 | 64.5 | 0.136 | 0.211 | 0.82 | 0.861 | 132.8 |
| mts_dialog/train | 1201 | 5.5 | 4.4 | 0.201 | 0.149 | 0.776 | 0.58 | 10.2 |
| mts_dialog/validation | 100 | 5.1 | 4.6 | 0.257 | 0.135 | 0.748 | 1.0 | 8.7 |
| mts_dialog/test_chat_2023 | 200 | 5.5 | 4.4 | 0.257 | 0.133 | 0.791 | 0.571 | 9.6 |
| mts_dialog/test_sum_2023 | 200 | 5.1 | 4.4 | 0.181 | 0.14 | 0.726 | 0.75 | 10.1 |
| dialogue_soap/train | 9250 | 37.2 | 37.4 | 0.056 | 0.084 | 0.839 | 0.238 | 53.1 |
| dialogue_soap/validation | 500 | 38.0 | 37.9 | 0.055 | 0.088 | 0.84 | 0.25 | 75.1 |
| dialogue_soap/test | 250 | 37.3 | 37.7 | 0.057 | 0.084 | 0.842 | 0.277 | 73.1 |

## Category mix in the reference notes (all splits)

| split | symptom | medical_history | diagnosis | medication | dosage | investigation | treatment | numeric |
|---|---|---|---|---|---|---|---|---|
| aci_bench/train | 987 | 208 | 342 | 393 | 147 | 612 | 984 | 272 |
| aci_bench/validation | 296 | 45 | 113 | 105 | 35 | 184 | 292 | 99 |
| aci_bench/test_taskB_1 | 587 | 101 | 220 | 216 | 72 | 289 | 596 | 178 |
| aci_bench/test_taskC_2 | 575 | 118 | 249 | 249 | 108 | 317 | 621 | 171 |
| aci_bench/test_taskC_3 | 682 | 124 | 235 | 277 | 108 | 361 | 641 | 151 |
| mts_dialog/train | 1607 | 905 | 352 | 466 | 50 | 296 | 1059 | 591 |
| mts_dialog/validation | 166 | 82 | 25 | 41 | 8 | 15 | 85 | 37 |
| mts_dialog/test_chat_2023 | 291 | 123 | 75 | 87 | 7 | 51 | 149 | 96 |
| mts_dialog/test_sum_2023 | 204 | 166 | 65 | 89 | 16 | 50 | 183 | 102 |
| dialogue_soap/train | 39426 | 17564 | 43849 | 23357 | 15544 | 66617 | 118793 | 21049 |
| dialogue_soap/validation | 2199 | 932 | 2413 | 1324 | 859 | 3661 | 6404 | 1167 |
| dialogue_soap/test | 1123 | 480 | 1203 | 662 | 423 | 1764 | 3225 | 533 |