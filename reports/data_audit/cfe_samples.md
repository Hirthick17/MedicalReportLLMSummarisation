# CFE samples for manual validation

6 random records per corpus (seed 42). Each fact row is one assertion; check polarity (negation), category and the value columns. Mark errors in the margin.

## aci_bench_test_taskB_1_D2N106-aci

**source** (829 words, 41 facts)

```
[doctor] hey charles i'm using this cool new recording device to help me with my documentation is that okay with you
[patient] sure
[doctor] awesome how are you doing today
[patient] well i could be better you know i moved out in the city
[doctor] about two years ago bought this big plot of land
[patient] oh
[doctor] i love it lots of deer round awesome
[patient] you be hunter
[doctor] huge hunter i love hunter yeah
[patient] i have a refrigerator full of venison at home
[doctor] do you
[patient] mm-hmm
[doctor] you want to carry share sure yeah we can switch
[patient] nice but so the thing is i have noticed that for some reason my breathing
[doctor] is n't what it used to be
[patient] sure
…
```

| category | text | canonical | polarity | certainty | temporality | who | section/speaker | value |
|---|---|---|---|---|---|---|---|---|
| numeric | two years ago | two year ago | present | certain | current | patient | doctor | two year |
| treatment | switch | medication management | present | certain | current | patient | doctor |  |
| symptom | short of breath | dyspnea | present | certain | current | patient | doctor |  |
| symptom | shortness of breath | dyspnea | present | certain | current | patient | doctor |  |
| diagnosis | allergies | allergic rhinitis | present | certain | current | patient | doctor |  |
| treatment | urgent care | referral | present | certain | current | patient | doctor |  |
| medication | nebulizer | nebulizer treatment | present | certain | current | patient | doctor |  |
| treatment | prescribed | medication management | present | certain | current | patient | patient |  |
| medication | inhaler | inhaler | present | certain | current | patient | patient |  |
| symptom | rash | rash | present | certain | current | patient | doctor |  |
| symptom | nausea | nausea | present | certain | current | patient | doctor |  |
| symptom | vomiting | vomiting | present | certain | current | patient | doctor |  |
| symptom | diarrhea | diarrhea | present | certain | current | patient | patient |  |
| symptom | throat swelling | throat swelling | present | certain | current | patient | doctor |  |
| medical_history | allergies | allergic rhinitis | present | certain | historical | patient | doctor |  |
| investigation | physical exam | physical examination | present | certain | current | patient | doctor |  |
| investigation | vital signs | vital signs | present | certain | current | patient | doctor |  |
| investigation | pulse | heart rate measurement | present | certain | current | patient | doctor |  |
| investigation | pulse ox | oxygen saturation | present | certain | current | patient | doctor |  |
| symptom | nervous | anxiety symptoms | present | uncertain | current | patient | doctor |  |
| symptom | rash | rash | absent | certain | current | patient | doctor |  |
| diagnosis | angioedema | angioedema | absent | certain | current | patient | doctor |  |
| symptom | swelling | edema | present | certain | current | patient | doctor |  |
| symptom | swollen | edema | present | certain | current | patient | doctor |  |
| symptom | wheezing | wheezing | present | uncertain | current | patient | doctor |  |
| investigation | chest x-ray | x-ray | present | certain | historical | patient | doctor |  |
| investigation | chest x-ray | x-ray | present | certain | historical | patient | doctor |  |
| investigation | pulmonary function test | pulmonary function test | present | certain | historical | patient | doctor |  |
| medical_history | asthma | asthma | present | certain | historical | patient | doctor |  |
| treatment | continue | medication management | present | certain | historical | patient | doctor |  |
| medication | albuterol inhaler | albuterol | present | certain | historical | patient | doctor |  |
| symptom | flare up | flare | present | certain | historical | patient | doctor |  |
| treatment | prescribe | medication management | present | uncertain | current | patient | doctor |  |
| medication | singulair | montelukast | present | uncertain | current | patient | doctor |  |
| diagnosis | asthma | asthma | present | certain | current | patient | doctor |  |
| investigation | allergy testing | allergy testing | present | certain | current | patient | doctor |  |
| investigation | allergy test | allergy testing | present | certain | current | patient | doctor |  |
| investigation | skin testing | allergy testing | present | uncertain | current | patient | doctor |  |
| treatment | management | conservative management | present | uncertain | current | patient | doctor |  |
| medication | immunotherapy | allergy immunotherapy | present | uncertain | current | patient | doctor |  |
| investigation | skin testing | allergy testing | present | certain | current | patient | doctor |  |

**reference** (385 words, 39 facts)

```
CHIEF COMPLAINT

Shortness of breath.

HISTORY OF PRESENT ILLNESS
Charles Sullivan is a pleasant 45-year-old male who presents to the clinic today for the evaluation of shortness of breath. The onset of his symptoms began 2 years ago. He has noticed that his breathing is not what it used to be. He describes an increased need to catch his breath. The patient also reports he gets “mid-shortness of breath” without reason. He has been seen at an urgent care where he received a nebulizer treatment and was prescribed an inhaler, which he uses when his symptoms are present. The patient states his symptoms are aggravated by living with a cat in his house and are present even when the cat is not arou…
```

| category | text | canonical | polarity | certainty | temporality | who | section/speaker | value |
|---|---|---|---|---|---|---|---|---|
| symptom | Shortness of breath | dyspnea | present | certain | current | patient | chief_complaint |  |
| numeric | 45-year-old | age 45 years | present | certain | current | patient | hpi | 45 years |
| symptom | shortness of breath | dyspnea | present | certain | historical | patient | hpi |  |
| numeric | 2 years ago | 2 year ago | present | certain | current | patient | hpi | 2 year |
| symptom | shortness of breath | dyspnea | present | certain | current | patient | hpi |  |
| treatment | urgent care | referral | present | certain | current | patient | hpi |  |
| medication | nebulizer treatment | nebulizer treatment | present | certain | current | patient | hpi |  |
| treatment | prescribed | medication management | present | certain | current | patient | hpi |  |
| medication | inhaler | inhaler | present | certain | current | patient | hpi |  |
| diagnosis | allergies | allergic rhinitis | present | certain | current | patient | hpi |  |
| symptom | diarrhea | diarrhea | present | certain | historical | patient | hpi |  |
| symptom | shortness of breath | dyspnea | absent | certain | current | patient | hpi |  |
| symptom | rash | rash | absent | certain | current | patient | hpi |  |
| symptom | nausea | nausea | absent | certain | current | patient | hpi |  |
| symptom | vomiting | vomiting | absent | certain | current | patient | hpi |  |
| symptom | throat swelling | throat swelling | absent | certain | current | patient | hpi |  |
| medical_history | allergies | allergic rhinitis | absent | certain | historical | patient | hpi |  |
| investigation | Oxygen Saturation | oxygen saturation | present | certain | current | patient | exam |  |
| diagnosis | angioedema | angioedema | absent | certain | current | patient | exam |  |
| symptom | wheezing | wheezing | present | certain | current | patient | exam |  |
| symptom | rash | rash | absent | certain | current | patient | exam |  |
| investigation | chest x-ray | x-ray | present | certain | current | patient | results |  |
| investigation | Pulmonary function test | pulmonary function test | present | certain | current | patient | results |  |
| medical_history | asthma | asthma | present | certain | historical | patient | assessment |  |
| investigation | pulmonary function test | pulmonary function test | present | certain | current | patient | plan |  |
| treatment | continue | medication management | present | certain | current | patient | plan |  |
| medication | albuterol inhaler | albuterol | present | certain | current | patient | plan |  |
| symptom | flare-up | flare | present | uncertain | current | patient | plan |  |
| treatment | prescribed | medication management | present | certain | current | patient | plan |  |
| medication | Singulair | montelukast | present | certain | current | patient | plan |  |
| dosage | 10 mg | montelukast 10mg | present | certain | current | patient | plan | 10 mg once daily |
| diagnosis | asthma | asthma | present | uncertain | current | patient | plan |  |
| treatment | management | conservative management | present | certain | current | patient | plan |  |
| investigation | further testing | diagnostic workup | present | uncertain | current | patient | plan |  |
| medication | immunotherapy | allergy immunotherapy | present | uncertain | current | patient | plan |  |
| treatment | follow up with me | follow-up | present | certain | current | patient | plan |  |
| treatment | follow up with me in 1 week | follow-up in 1 week | present | certain | current | patient | plan | 1 week |
| numeric | 1 week | 1 week | present | certain | current | patient | plan | 1 week |
| investigation | skin testing | allergy testing | present | certain | current | patient | plan |  |

## aci_bench_test_taskB_1_D2N091-virtassist

**source** (742 words, 46 facts)

```
[doctor] hi jerry , how are you doing ?
[patient] hi , good to see you .
[doctor] good to see you as well . um , so i know that the nurse told you about dax . i'd like to tell dax about you .
[patient] sure .
[doctor] jerry is a 54 year old male with a past medical history , significant for osteoporosis and multiple sclerosis who presents for an annual exam . so jerry , what's been going on since the last time i saw you ?
[patient] uh , we have been traveling all over the country . it's been kind of a stressful summer . kinda adjusting to everything in the fall and so far it's been good , but ah , lack of sleep , it's been really getting to me .
[doctor] okay . all right . and have you taken…
```

| category | text | canonical | polarity | certainty | temporality | who | section/speaker | value |
|---|---|---|---|---|---|---|---|---|
| numeric | 54 year old | age 54 years | present | certain | current | patient | doctor | 54 years |
| medical_history | osteoporosis | osteoporosis | present | certain | historical | patient | doctor |  |
| medical_history | multiple sclerosis | multiple sclerosis | present | certain | historical | patient | doctor |  |
| treatment | annual exam | immunization plan | present | certain | historical | patient | doctor |  |
| symptom | fall | falls | present | certain | current | patient | patient |  |
| symptom | insomnia | insomnia | present | certain | current | patient | doctor |  |
| medication | melatonin | melatonin | present | certain | current | patient | patient | every morning |
| treatment | meditation | lifestyle modification | present | certain | current | patient | patient |  |
| treatment | stretching | physical therapy plan | present | certain | current | patient | patient |  |
| diagnosis | osteoporosis | osteoporosis | present | certain | current | patient | doctor |  |
| medication | fosamax | alendronate | present | certain | current | patient | doctor |  |
| diagnosis | broken bones | fracture | absent | certain | current | patient | doctor |  |
| diagnosis | multiple sclerosis | multiple sclerosis | present | uncertain | current | patient | doctor |  |
| treatment | neurologist | referral | present | uncertain | current | patient | doctor |  |
| numeric | six months ago | six month ago | present | certain | current | patient | patient | six month |
| medication | medication | medication | present | certain | current | patient | doctor |  |
| symptom | weakness | weakness | present | certain | current | patient | doctor |  |
| treatment | surgery | surgery | present | certain | current | patient | patient |  |
| symptom | insomnia | insomnia | present | certain | current | patient | doctor |  |
| symptom | chest pain | chest pain | absent | certain | current | patient | doctor |  |
| symptom | shortness of breath | dyspnea | absent | certain | current | patient | doctor |  |
| investigation | physical exam | physical examination | present | certain | current | patient | doctor |  |
| investigation | vital signs | vital signs | present | certain | current | patient | doctor |  |
| investigation | vital signs | vital signs | present | certain | current | patient | doctor |  |
| investigation | listen to your heart | physical examination | present | certain | current | patient | doctor |  |
| investigation | physical examination | physical examination | present | certain | current | patient | doctor |  |
| symptom | weakness | weakness | present | certain | current | patient | doctor |  |
| investigation | reflexes | physical examination | present | certain | current | patient | doctor |  |
| diagnosis | arthritic | arthritis | present | certain | current | patient | doctor |  |
| investigation | knee x-ray | x-ray | present | certain | current | patient | doctor |  |
| investigation | x-ray | x-ray | present | certain | current | patient | doctor |  |
| diagnosis | arthritis | arthritis | present | certain | current | patient | doctor |  |
| diagnosis | osteoporosis | osteoporosis | present | certain | current | patient | doctor |  |
| treatment | continue | medication management | present | certain | current | patient | doctor |  |
| medication | fosamax | alendronate | present | certain | current | patient | doctor |  |
| treatment | refill | medication management | present | uncertain | current | patient | doctor |  |
| treatment | refill | medication management | present | certain | current | patient | doctor |  |
| medication | fosamax | alendronate | present | certain | current | patient | doctor |  |
| dosage | 1 tab | alendronate 1tab | present | certain | current | patient | doctor | 1 tab per week |
| treatment | refills | medication management | present | certain | current | patient | doctor |  |
| diagnosis | multiple sclerosis | multiple sclerosis | present | certain | current | patient | doctor |  |
| treatment | continue | medication management | present | certain | current | patient | doctor |  |
| treatment | neurologist | referral | present | certain | current | patient | doctor |  |
| treatment | continue | medication management | present | certain | current | patient | doctor |  |
| medication | medications | medication | present | certain | current | patient | doctor |  |
| treatment | let me know if | referral | present | uncertain | current | patient | doctor |  |

**reference** (368 words, 59 facts)

```
CHIEF COMPLAINT

Annual exam.

HISTORY OF PRESENT ILLNESS

Jerry Nguyen a 54-year-old male with a past medical history significant for osteoporosis, and multiple sclerosis, who presents for an annual exam.

The patient states he has been traveling all over the country. He notes it has been a stressful summer and adjusting to everything in the fall.

The patient reports a lack of sleep. He has tried melatonin, meditation, and stretching every morning, but nothing has helped.

For treatment of his osteoporosis, he is on Fosamax. He denies any issues with his joints. He denies any recent broken bones.

Regarding his multiple sclerosis, he last saw the neurologist 6 months ago. He is taking his …
```

| category | text | canonical | polarity | certainty | temporality | who | section/speaker | value |
|---|---|---|---|---|---|---|---|---|
| treatment | Annual exam | immunization plan | present | certain | current | patient | chief_complaint |  |
| numeric | 54-year-old | age 54 years | present | certain | current | patient | hpi | 54 years |
| medical_history | osteoporosis | osteoporosis | present | certain | historical | patient | hpi |  |
| medical_history | multiple sclerosis | multiple sclerosis | present | certain | historical | patient | hpi |  |
| treatment | annual exam | immunization plan | present | certain | historical | patient | hpi |  |
| symptom | fall | falls | present | certain | current | patient | hpi |  |
| medication | melatonin | melatonin | present | certain | current | patient | hpi | every morning |
| treatment | meditation | lifestyle modification | present | certain | current | patient | hpi |  |
| treatment | stretching | physical therapy plan | present | certain | current | patient | hpi |  |
| treatment | treatment | conservative management | present | certain | current | patient | hpi |  |
| diagnosis | osteoporosis | osteoporosis | present | certain | current | patient | hpi |  |
| medication | Fosamax | alendronate | present | certain | current | patient | hpi |  |
| diagnosis | broken bones | fracture | absent | certain | current | patient | hpi |  |
| diagnosis | multiple sclerosis | multiple sclerosis | present | certain | current | patient | hpi |  |
| treatment | neurologist | referral | present | certain | historical | patient | hpi |  |
| numeric | 6 months ago | 6 month ago | present | certain | current | patient | hpi | 6 month |
| medication | medication | medication | present | certain | current | patient | hpi |  |
| symptom | weakness | weakness | present | certain | historical | patient | hpi |  |
| treatment | surgery | surgery | present | certain | historical | patient | hpi |  |
| symptom | chest pain | chest pain | absent | certain | current | patient | hpi |  |
| symptom | shortness of breath | dyspnea | absent | certain | current | patient | hpi |  |
| symptom | chest pain | chest pain | absent | certain | current | patient | ros |  |
| symptom | dyspnea | dyspnea | absent | certain | current | patient | ros |  |
| symptom | shortness of breath | dyspnea | absent | certain | current | patient | ros |  |
| symptom | insomnia | insomnia | present | certain | current | patient | ros |  |
| investigation | auscultation | physical examination | present | certain | current | patient | exam |  |
| symptom | wheezes | wheezing | absent | certain | current | patient | exam |  |
| symptom | rales | crackles | absent | certain | current | patient | exam |  |
| symptom | rhonchi | rhonchi | absent | certain | current | patient | exam |  |
| symptom | Weakness | weakness | present | certain | current | patient | exam |  |
| investigation | Reflexes | physical examination | present | certain | current | patient | exam |  |
| diagnosis | Arthritic | arthritis | present | certain | current | patient | exam |  |
| investigation | X-ray | x-ray | present | certain | current | patient | results |  |
| diagnosis | arthritic | arthritis | present | certain | current | patient | results |  |
| numeric | 54-year-old | age 54 years | present | certain | current | patient | assessment | 54 years |
| medical_history | osteoporosis | osteoporosis | present | certain | historical | patient | assessment |  |
| medical_history | multiple sclerosis | multiple sclerosis | present | certain | historical | patient | assessment |  |
| treatment | annual exam | immunization plan | present | certain | historical | patient | assessment |  |
| diagnosis | Osteoporosis | osteoporosis | present | certain | current | patient | plan |  |
| medication | Fosamax | alendronate | present | certain | current | patient | plan |  |
| treatment | Treatment | conservative management | present | certain | current | patient | plan |  |
| treatment | Continue | medication management | present | certain | current | patient | plan |  |
| medication | Fosamax | alendronate | present | certain | current | patient | plan |  |
| dosage | 1 tab | alendronate 1tab | present | certain | current | patient | plan | 1 tab per week |
| treatment | refills | medication management | present | certain | current | patient | plan |  |
| diagnosis | Multiple Sclerosis | multiple sclerosis | present | certain | current | patient | plan |  |
| symptom | weakness | weakness | present | certain | current | patient | plan |  |
| treatment | neurologist | referral | present | certain | current | patient | plan |  |
| medication | medication | medication | present | certain | current | patient | plan |  |
| treatment | Treatment | conservative management | present | certain | current | patient | plan |  |
| treatment | continue | medication management | present | certain | current | patient | plan |  |
| treatment | follow up with | follow-up | present | certain | current | patient | plan |  |
| treatment | neurologist | referral | present | certain | current | patient | plan |  |
| medication | medication | medication | present | certain | current | patient | plan |  |
| diagnosis | knee arthritis | osteoarthritis | present | certain | current | patient | plan |  |
| treatment | surgery | surgery | present | certain | historical | patient | plan |  |
| investigation | knee x-ray | x-ray | present | certain | current | patient | plan |  |
| diagnosis | arthritic | arthritis | present | certain | current | patient | plan |  |
| treatment | treatment plan | conservative management | present | certain | current | patient | plan |  |

## aci_bench_test_taskB_1_D2N122-aci

**source** (1292 words, 71 facts)

```
[doctor] hey kyle it's nice to see you today can you tell me a little bit about what brought you in
[patient] yeah i went to see my pcp for a cough which they diagnosed as bronchitis but then they did that chest x-ray to make sure i did n't have pneumonia and they found this lung nodule i went for a cat scan that confirmed it and they referred me here to you i'm really nervous document
[doctor] okay well first of all i'm i'm sorry that you're nervous and what we're gon na do is we're gon na partner together okay and i'm gon na be right by your side the whole time to hopefully make you a little less nervous and and recognize the fact that we're you're gon na have a big support team around you…
```

| category | text | canonical | polarity | certainty | temporality | who | section/speaker | value |
|---|---|---|---|---|---|---|---|---|
| treatment | pcp | referral | present | certain | current | patient | patient |  |
| symptom | cough | cough | present | certain | current | patient | patient |  |
| medical_history | bronchitis | bronchitis | present | certain | historical | patient | patient |  |
| investigation | chest x-ray | x-ray | present | certain | historical | patient | patient |  |
| medical_history | pneumonia | pneumonia | present | certain | historical | patient | patient |  |
| medical_history | lung nodule | lung cancer | present | certain | historical | patient | patient |  |
| investigation | cat scan | ct scan | present | certain | historical | patient | patient |  |
| treatment | referred | referral | present | certain | current | patient | patient |  |
| symptom | nervous | anxiety symptoms | present | certain | current | patient | patient |  |
| symptom | nervous | anxiety symptoms | present | certain | current | patient | doctor |  |
| symptom | nervous | anxiety symptoms | present | certain | current | patient | doctor |  |
| symptom | cough | cough | present | certain | current | patient | doctor |  |
| numeric | three months | three month | present | certain | current | patient | patient | three month |
| symptom | coughing | cough | present | certain | historical | patient | patient |  |
| treatment | pcp | referral | present | certain | current | patient | patient |  |
| treatment | exercise | lifestyle modification | present | certain | current | patient | patient |  |
| treatment | biking | lifestyle modification | present | certain | current | patient | patient |  |
| symptom | cough | cough | present | certain | current | patient | patient |  |
| treatment | exercise | lifestyle modification | present | certain | current | patient | doctor |  |
| treatment | biking | lifestyle modification | present | certain | current | patient | doctor |  |
| medical_history | rheumatoid arthritis | rheumatoid arthritis | present | certain | historical | patient | doctor |  |
| treatment | under control | conservative management | present | certain | historical | patient | doctor |  |
| diagnosis | arthritis | arthritis | present | certain | current | patient | patient |  |
| medication | methotrexate | methotrexate | present | certain | current | patient | patient |  |
| symptom | flares | flare | present | certain | current | patient | patient |  |
| medical_history | smoker | tobacco use | present | certain | historical | patient | doctor |  |
| treatment | stop smoking | lifestyle modification | present | certain | historical | patient | doctor |  |
| numeric | seven years ago | seven year ago | present | certain | current | patient | patient | seven year |
| symptom | pain | pain | present | certain | current | patient | doctor |  |
| symptom | shortness of breath | dyspnea | present | certain | current | patient | doctor |  |
| medical_history | lung cancer | lung cancer | present | uncertain | historical | family | doctor |  |
| diagnosis | lung cancer | lung cancer | absent | certain | current | patient | patient |  |
| medical_history | breast cancer | breast cancer | absent | certain | current | family | patient |  |
| diagnosis | lung infections | pneumonia | present | certain | current | patient | doctor |  |
| diagnosis | pneumonia | pneumonia | present | certain | current | patient | doctor |  |
| investigation | physical exam | physical examination | present | uncertain | current | patient | doctor |  |
| investigation | vital signs | vital signs | present | uncertain | current | patient | doctor |  |
| investigation | blood pressure | blood pressure measurement | present | uncertain | current | patient | doctor |  |
| investigation | heart rate | heart rate measurement | present | certain | current | patient | doctor |  |
| investigation | o2 sat | oxygen saturation | present | certain | current | patient | doctor |  |
| symptom | fever | fever | present | certain | current | patient | doctor |  |
| investigation | listen to your lungs | physical examination | present | certain | current | patient | doctor |  |
| symptom | clicks | crepitus | absent | certain | current | patient | doctor |  |
| symptom | murmurs | murmur | absent | certain | current | patient | doctor |  |
| investigation | extremity exam | physical examination | absent | certain | current | patient | doctor |  |
| symptom | edema | edema | absent | certain | current | patient | doctor |  |
| symptom | swelling | edema | present | certain | current | patient | doctor |  |
| investigation | pulses | heart rate measurement | present | certain | current | patient | doctor |  |
| investigation | capillary refill | physical examination | present | certain | current | patient | doctor |  |
| symptom | nodule | lump | present | uncertain | historical | patient | doctor |  |
| symptom | nodule | lump | present | uncertain | current | patient | doctor |  |
| diagnosis | lung nodule | lung cancer | present | certain | current | patient | doctor |  |
| investigation | pulmonary function test | pulmonary function test | present | certain | current | patient | doctor |  |
| symptom | nodule | lump | present | uncertain | current | patient | doctor |  |
| diagnosis | cancer | cancer | present | uncertain | current | patient | doctor |  |
| medication | general anesthesia | anesthetic | present | certain | current | patient | doctor |  |
| numeric | an hour | an hour | present | certain | current | patient | doctor | an hour |
| treatment | procedure | surgery | present | certain | historical | patient | doctor |  |
| treatment | admitted | hospital admission | present | certain | historical | patient | doctor |  |
| treatment | chest tube | injection | present | certain | historical | patient | doctor |  |
| symptom | nodule | lump | present | uncertain | current | patient | doctor |  |
| diagnosis | rheumatoid arthritis | rheumatoid arthritis | present | certain | current | patient | doctor |  |
| treatment | continue | medication management | present | certain | current | patient | doctor |  |
| treatment | follow up with | follow-up | present | certain | current | patient | doctor |  |
| treatment | rheumatologist | referral | present | certain | current | patient | doctor |  |
| treatment | continue | medication management | present | certain | current | patient | doctor |  |
| medication | medication | medication | present | certain | historical | patient | doctor |  |
| treatment | therapy | conservative management | present | certain | historical | patient | doctor |  |
| treatment | treatment | conservative management | present | certain | historical | patient | doctor |  |
| treatment | see you again | follow-up | present | certain | current | patient | doctor |  |
| numeric | few minutes | few minute | present | certain | current | patient | doctor | few minute |

**reference** (481 words, 64 facts)

```
CHIEF COMPLAINT

Cough.

MEDICAL HISTORY

Patient reports a history of rheumatoid arthritis. He denies any previous history of lung infections or pneumonia.

SOCIAL HISTORY

Patient reports he stopped smoking tobacco 7 years ago and has felt better since doing so. He notes that he enjoys biking.

FAMILY HISTORY

Patient reports his mother has a history of breast cancer, but is doing well. He denies any family history of lung cancer.

MEDICATIONS

Patient reports taking methotrexate 7.5 mg every week.

REVIEW OF SYSTEMS

Respiratory: Denies cough or shortness of breath.

VITALS

Blood Pressure: 124/76 mmHg.
Heart Rate: 70 beats per minute.
Respiratory Rate: 16 breaths per minute.
Oxygen Satur…
```

| category | text | canonical | polarity | certainty | temporality | who | section/speaker | value |
|---|---|---|---|---|---|---|---|---|
| symptom | Cough | cough | present | certain | current | patient | chief_complaint |  |
| medical_history | rheumatoid arthritis | rheumatoid arthritis | present | certain | historical | patient | pmh |  |
| medical_history | lung infections | pneumonia | absent | certain | historical | patient | pmh |  |
| medical_history | pneumonia | pneumonia | absent | certain | historical | patient | pmh |  |
| numeric | 7 years ago | 7 year ago | present | certain | current | patient | social_history | 7 year |
| treatment | biking | lifestyle modification | present | certain | current | patient | social_history |  |
| medical_history | breast cancer | breast cancer | present | certain | historical | family | family_history |  |
| medical_history | lung cancer | lung cancer | absent | certain | historical | family | family_history |  |
| medication | methotrexate | methotrexate | present | certain | current | patient | medications |  |
| dosage | 7.5 mg | methotrexate 7.5mg | present | certain | current | patient | medications | 7.5 mg every week |
| symptom | cough | cough | absent | certain | current | patient | ros |  |
| symptom | shortness of breath | dyspnea | absent | certain | current | patient | ros |  |
| investigation | Blood Pressure | blood pressure measurement | present | certain | current | patient | exam |  |
| numeric | Blood Pressure: 124/76 mmHg | blood pressure 124/76 | present | certain | current | patient | exam | 124/76 mmhg |
| investigation | Heart Rate | heart rate measurement | present | certain | current | patient | exam |  |
| numeric | Heart Rate: 70 | heart rate 70 | present | certain | current | patient | exam | 70 |
| investigation | Respiratory Rate | respiratory rate | present | certain | current | patient | exam |  |
| numeric | Respiratory Rate: 16 | respiratory rate 16 | present | certain | current | patient | exam | 16 |
| investigation | Oxygen Saturation | oxygen saturation | present | certain | current | patient | exam |  |
| numeric | Oxygen Saturation: 98% | oxygen saturation 98 | present | certain | current | patient | exam | 98 % |
| investigation | Body Temperature | temperature measurement | present | certain | current | patient | exam |  |
| investigation | Auscultation | physical examination | present | certain | current | patient | exam |  |
| investigation | Auscultation | physical examination | present | certain | current | patient | exam |  |
| symptom | clicks | crepitus | absent | certain | current | patient | exam |  |
| symptom | murmurs | murmur | absent | certain | current | patient | exam |  |
| investigation | Pulses | heart rate measurement | present | certain | current | patient | exam |  |
| symptom | edema | edema | absent | certain | current | patient | exam |  |
| symptom | swelling | edema | present | uncertain | current | patient | exam |  |
| investigation | Capillary refill | physical examination | present | certain | current | patient | exam |  |
| investigation | CT scan | ct scan | present | certain | current | patient | results |  |
| symptom | nodule | lump | present | certain | current | patient | results |  |
| symptom | nodule | lump | present | uncertain | current | patient | results |  |
| diagnosis | lung nodule | lung cancer | present | certain | current | patient | assessment |  |
| diagnosis | lung nodule | lung cancer | present | certain | current | patient | assessment |  |
| investigation | CT | ct scan | present | certain | current | patient | assessment |  |
| symptom | nodule | lump | present | uncertain | current | patient | assessment |  |
| treatment | Patient Education | counseling/education | present | certain | current | patient | assessment |  |
| treatment | Counseling | counseling/education | present | certain | current | patient | assessment |  |
| treatment | surgical treatment | surgery | present | certain | historical | patient | assessment |  |
| treatment | Surgery | surgery | present | certain | current | patient | assessment |  |
| medication | general anesthesia | anesthetic | present | certain | current | patient | assessment |  |
| numeric | 5 hours | 5 hour | present | certain | current | patient | assessment | 5 hour |
| treatment | procedure | surgery | present | certain | current | patient | assessment |  |
| symptom | nodule | lump | present | certain | current | patient | assessment |  |
| treatment | admitted | hospital admission | present | uncertain | current | patient | assessment |  |
| treatment | chest tube | injection | present | certain | current | patient | assessment |  |
| treatment | Treatment | conservative management | present | certain | current | patient | assessment |  |
| investigation | Pulmonary function test | pulmonary function test | present | certain | current | patient | assessment |  |
| investigation | CT | ct scan | present | uncertain | current | patient | assessment |  |
| symptom | nodule | lump | present | uncertain | current | patient | assessment |  |
| symptom | Nodule | lump | present | certain | current | patient | assessment |  |
| diagnosis | Rheumatoid arthritis | rheumatoid arthritis | present | certain | current | patient | assessment |  |
| treatment | Patient Education | counseling/education | present | certain | current | patient | assessment |  |
| treatment | Counseling | counseling/education | present | certain | current | patient | assessment |  |
| treatment | continue | medication management | present | certain | current | patient | assessment |  |
| treatment | follow up with | follow-up | present | certain | current | patient | assessment |  |
| treatment | rheumatologist | referral | present | certain | current | patient | assessment |  |
| treatment | Treatment | conservative management | present | certain | current | patient | assessment |  |
| treatment | Continue | medication management | present | certain | current | patient | assessment |  |
| medication | medication | medication | present | certain | current | patient | assessment |  |
| treatment | therapy | conservative management | present | certain | current | patient | assessment |  |
| treatment | follow up with | follow-up | present | certain | historical | patient | assessment |  |
| treatment | rheumatologist | referral | present | certain | historical | patient | assessment |  |
| treatment | treatment plan | conservative management | present | certain | current | patient | plan |  |

## aci_bench_validation_D2N079-aci

**source** (916 words, 43 facts)

```
[doctor] hi wayne how're you today
[patient] i'm doing okay aside from this left shoulder pain that i've been having
[doctor] okay and how long have you had this pain
[patient] about i want to say a few weeks i think it's been about three weeks now
[doctor] okay and do you remember what you were doing when the pain started
[patient] honestly i've been trying to recall if i had any specific injury and i ca n't think of that
[doctor] okay
[patient] of anything the only thing i can think of is that i you know i am active and we've just been doing a lot of work in our basement so if i do n't know if i did something while doing that
[doctor] okay alright tell me have you ever had pain in that sho…
```

| category | text | canonical | polarity | certainty | temporality | who | section/speaker | value |
|---|---|---|---|---|---|---|---|---|
| symptom | shoulder pain | shoulder pain | present | certain | current | patient | patient |  |
| symptom | pain | pain | present | certain | current | patient | doctor |  |
| numeric | few weeks | few week | present | certain | current | patient | patient | few week |
| numeric | three weeks | three week | present | certain | current | patient | patient | three week |
| symptom | pain | pain | present | certain | current | patient | doctor |  |
| diagnosis | injury | trauma | present | uncertain | current | patient | patient |  |
| symptom | pain | pain | present | certain | current | patient | doctor |  |
| symptom | aches | pain | present | certain | current | patient | patient |  |
| symptom | pains | pain | present | certain | current | patient | patient |  |
| medication | tylenol | acetaminophen | absent | certain | current | patient | patient |  |
| symptom | pain | pain | present | certain | current | patient | doctor |  |
| symptom | pain | pain | present | certain | current | patient | patient |  |
| symptom | pain | pain | present | certain | current | patient | doctor |  |
| medication | tylenol | acetaminophen | present | certain | current | patient | patient |  |
| numeric | eight hours | eight hour | present | certain | current | patient | patient | eight hour |
| symptom | pain | pain | present | certain | current | patient | patient |  |
| symptom | numbness | numbness | present | certain | current | patient | doctor |  |
| symptom | numbness | numbness | absent | certain | current | patient | patient |  |
| symptom | tingling | tingling | absent | certain | current | patient | patient |  |
| investigation | physical exam | physical examination | present | certain | current | patient | doctor |  |
| investigation | vitals | vital signs | present | certain | current | patient | doctor |  |
| investigation | shoulder exam | physical examination | present | certain | current | patient | doctor |  |
| symptom | tenderness | pain | present | certain | current | patient | doctor |  |
| symptom | tenderness | pain | absent | certain | current | patient | doctor |  |
| investigation | neurovascular exam | physical examination | present | certain | current | patient | doctor |  |
| investigation | capillary refill | physical examination | present | certain | current | patient | doctor |  |
| investigation | shoulder x-ray | x-ray | present | certain | current | patient | doctor |  |
| diagnosis | fractures | fracture | absent | certain | current | patient | doctor |  |
| symptom | shoulder pain | shoulder pain | present | uncertain | current | patient | doctor |  |
| diagnosis | rotator cuff tendinopathy | rotator cuff tear | present | certain | current | patient | doctor |  |
| diagnosis | injured | trauma | present | certain | current | patient | doctor |  |
| treatment | refer you to | referral | present | certain | current | patient | doctor |  |
| treatment | physical therapy | referral | present | uncertain | current | patient | doctor |  |
| numeric | eight weeks | eight week | present | certain | current | patient | doctor | eight week |
| treatment | continue | medication management | present | uncertain | current | patient | doctor |  |
| medication | tylenol | acetaminophen | present | uncertain | current | patient | doctor |  |
| medication | steroid injection | cortisone injection | present | uncertain | current | patient | doctor |  |
| symptom | pain | pain | present | certain | current | patient | patient |  |
| treatment | physical therapy | referral | present | certain | current | patient | doctor |  |
| treatment | strengthening exercises | physical therapy plan | present | certain | current | patient | doctor |  |
| treatment | physical therapy | referral | present | certain | current | patient | doctor |  |
| treatment | follow-up visit | follow-up | present | certain | current | patient | doctor |  |
| treatment | physical therapy | referral | present | certain | current | patient | doctor |  |

**reference** (386 words, 38 facts)

```
CHIEF COMPLAINT

Left shoulder pain.

HISTORY OF PRESENT ILLNESS

Wayne Taylor is a pleasant 66-year-old male who presents to the clinic today for the evaluation of left shoulder pain. The onset of his pain began 3 weeks ago. He denies any specific injury. The patient states he is active and has been renovating his basement. He reports a history of intermittent aches and pains in his left shoulder. He has difficulty reaching for or lifting any objects. He adds that he avoids reaching overhead secondary to the pain. The patient describes his pain as constant and worsening. He notes his pain is unbearable when lying on his left shoulder at night. He denies any numbness or tingling in the bilat…
```

| category | text | canonical | polarity | certainty | temporality | who | section/speaker | value |
|---|---|---|---|---|---|---|---|---|
| symptom | shoulder pain | shoulder pain | present | certain | current | patient | chief_complaint |  |
| numeric | 66-year-old | age 66 years | present | certain | current | patient | hpi | 66 years |
| symptom | shoulder pain | shoulder pain | present | certain | historical | patient | hpi |  |
| symptom | pain | pain | present | certain | historical | patient | hpi |  |
| numeric | 3 weeks ago | 3 week ago | present | certain | current | patient | hpi | 3 week |
| diagnosis | injury | trauma | absent | certain | current | patient | hpi |  |
| symptom | aches | pain | present | certain | historical | patient | hpi |  |
| symptom | pains | pain | present | certain | historical | patient | hpi |  |
| symptom | pain | pain | present | certain | current | patient | hpi |  |
| symptom | pain | pain | present | certain | current | patient | hpi |  |
| symptom | pain | pain | present | certain | current | patient | hpi |  |
| symptom | numbness | numbness | absent | certain | current | patient | hpi |  |
| symptom | tingling | tingling | absent | certain | current | patient | hpi |  |
| medication | Tylenol | acetaminophen | present | certain | current | patient | hpi |  |
| numeric | 8 hours | 8 hour | present | certain | current | patient | hpi | 8 hour |
| symptom | shoulder pain | shoulder pain | present | certain | current | patient | ros |  |
| symptom | numbness | numbness | absent | certain | current | patient | ros |  |
| symptom | tingling | tingling | absent | certain | current | patient | ros |  |
| investigation | vital signs | vital signs | present | certain | current | patient | exam |  |
| investigation | Capillary refill | physical examination | present | certain | current | patient | exam |  |
| symptom | Tenderness | pain | present | certain | current | patient | exam |  |
| symptom | tenderness | pain | absent | certain | current | patient | exam |  |
| investigation | X-rays | x-ray | present | certain | current | patient | results |  |
| diagnosis | fractures | fracture | absent | certain | current | patient | results |  |
| symptom | shoulder pain | shoulder pain | present | uncertain | current | patient | assessment |  |
| diagnosis | rotator cuff tendinopathy | rotator cuff tear | present | certain | current | patient | assessment |  |
| diagnosis | rotator cuff tendinopathy | rotator cuff tear | present | certain | current | patient | plan |  |
| investigation | MRI | mri | present | certain | current | patient | plan |  |
| treatment | refer | referral | present | certain | current | patient | plan |  |
| treatment | physical therapy | referral | present | certain | current | patient | plan |  |
| numeric | 8 weeks | 8 week | present | certain | current | patient | plan | 8 week |
| treatment | physical therapy | referral | present | certain | current | patient | plan |  |
| treatment | continue | medication management | present | uncertain | current | patient | plan |  |
| medication | Tylenol | acetaminophen | present | uncertain | current | patient | plan | as needed |
| treatment | physical therapy | referral | absent | uncertain | current | patient | plan |  |
| medication | steroid injection | cortisone injection | absent | uncertain | current | patient | plan |  |
| treatment | follow up with me | follow-up | present | certain | current | patient | plan |  |
| treatment | physical therapy | referral | present | certain | current | patient | plan |  |

## aci_bench_validation_D2N084-aci

**source** (1000 words, 58 facts)

```
[doctor] alright david so you were just in the emergency department hopefully you can hear me okay through the zoom meeting what happened
[patient] well it seems that i was outside and i fell down i was walking a bit and i did have a pain in my chest but i did n't think anything of it and i just kept on going and then all of a sudden i'm here
[doctor] hmmm my gosh so it looks like you you went into the er and looks like they said that your ankles were swelling a little bit too and did you have some shortness of breath
[patient] i did but i did n't think anything of it
[doctor] sure yeah okay yeah i know we've been talking through your hypertension looks like your blood pressure was two hundr…
```

| category | text | canonical | polarity | certainty | temporality | who | section/speaker | value |
|---|---|---|---|---|---|---|---|---|
| treatment | emergency department | referral | present | certain | current | patient | doctor |  |
| symptom | fell | falls | present | uncertain | current | patient | patient |  |
| treatment | walking | lifestyle modification | present | uncertain | current | patient | patient |  |
| symptom | pain in my chest | chest pain | present | uncertain | current | patient | patient |  |
| symptom | swelling | edema | present | certain | current | patient | doctor |  |
| symptom | shortness of breath | dyspnea | present | certain | current | patient | doctor |  |
| diagnosis | hypertension | hypertension | present | certain | current | patient | doctor |  |
| investigation | blood pressure | blood pressure measurement | present | certain | current | patient | doctor |  |
| medication | meds | medication | present | certain | current | patient | doctor |  |
| medication | bumex | bumetanide | present | certain | current | patient | doctor |  |
| medication | cozaar | losartan | present | certain | current | patient | doctor |  |
| medication | norvasc | amlodipine | present | certain | current | patient | doctor |  |
| treatment | watching | conservative management | present | certain | current | patient | doctor |  |
| treatment | diet | lifestyle modification | present | certain | current | patient | doctor |  |
| treatment | watch | conservative management | present | certain | current | patient | patient |  |
| treatment | watch | conservative management | present | certain | current | patient | doctor |  |
| treatment | diet | lifestyle modification | present | certain | current | patient | doctor |  |
| medication | meds | medication | present | certain | current | patient | doctor |  |
| investigation | blood pressure cuff | blood pressure measurement | present | certain | current | patient | doctor |  |
| investigation | blood pressures | blood pressure measurement | present | uncertain | current | patient | doctor |  |
| symptom | shortness of breath | dyspnea | present | uncertain | current | patient | doctor |  |
| treatment | walking | lifestyle modification | present | certain | historical | patient | patient |  |
| symptom | chest pain | chest pain | present | certain | current | patient | doctor |  |
| symptom | heartburn | heartburn | present | certain | current | patient | patient |  |
| investigation | physical exam | physical examination | present | certain | current | patient | doctor |  |
| investigation | blood pressure | blood pressure measurement | present | certain | current | patient | doctor |  |
| investigation | vital signs | vital signs | present | certain | current | patient | doctor |  |
| investigation | heart exam | physical examination | absent | certain | current | patient | doctor |  |
| symptom | murmur | murmur | absent | certain | current | patient | doctor |  |
| numeric | couple of years ago | couple of year ago | present | certain | current | patient | doctor | couple of year |
| symptom | edema | edema | present | certain | current | patient | doctor |  |
| investigation | echocardiogram | echocardiogram | present | certain | current | patient | doctor |  |
| diagnosis | mitral regurgitation | mitral regurgitation | present | certain | current | patient | doctor |  |
| treatment | diet | lifestyle modification | present | uncertain | current | patient | doctor |  |
| diagnosis | uncontrolled hypertension | hypertension | present | uncertain | current | patient | doctor |  |
| treatment | monitoring | conservative management | present | uncertain | current | patient | doctor |  |
| treatment | continue | medication management | present | certain | current | patient | doctor |  |
| medication | bumex | bumetanide | present | certain | current | patient | doctor | once daily |
| treatment | stay on | medication management | present | certain | current | patient | doctor |  |
| medication | meds | medication | present | certain | current | patient | doctor |  |
| treatment | consult | referral | present | certain | current | patient | doctor |  |
| treatment | watching | conservative management | present | uncertain | historical | patient | doctor |  |
| treatment | diet | lifestyle modification | present | uncertain | historical | patient | doctor |  |
| treatment | watching | conservative management | present | uncertain | historical | patient | doctor |  |
| treatment | call me | referral | present | uncertain | current | patient | doctor |  |
| numeric | two days | two day | present | certain | current | patient | doctor | two day |
| diagnosis | hypertension | hypertension | present | uncertain | current | patient | doctor |  |
| treatment | treating | conservative management | present | uncertain | current | patient | doctor |  |
| treatment | continue | medication management | present | uncertain | current | patient | doctor |  |
| medication | cozaar | losartan | present | uncertain | current | patient | doctor | daily |
| treatment | continue | medication management | present | certain | current | patient | doctor |  |
| medication | norvasc | amlodipine | present | certain | current | patient | doctor | once daily |
| treatment | discharge | discharge | present | certain | current | patient | doctor |  |
| investigation | ultrasound | ultrasound | present | certain | current | patient | doctor |  |
| medication | medication | medication | present | certain | current | patient | patient |  |
| medication | medication | medication | present | certain | current | patient | doctor |  |
| treatment | nutritionist | referral | present | certain | current | patient | doctor |  |
| treatment | diet | lifestyle modification | present | certain | current | patient | doctor |  |

**reference** (353 words, 57 facts)

```
CHIEF COMPLAINT

Follow up.

SOCIAL HISTORY

The patient has been trying to limit his tobacco use for 2 years. He reports smoking once every week.

MEDICATIONS

Bumex 2 mg once daily.
Cozaar 100 mg daily.
Norvasc 5 mg once daily.

REVIEW OF SYSTEMS

Constitutional: Denies problems sleeping.
Cardiovascular: Reports chest pain.
Respiratory: Reports shortness of breath.
Musculoskeletal: Reports bilateral ankle swelling.

VITALS

Blood pressure is 128/72 mm Hg. Other vital signs are within normal limits.

PHYSICAL EXAM

Neck
- General Examination: No JVD

Respiratory
- Auscultation of Lungs: Clear bilaterally.

Cardiovascular
- Auscultation of Heart: 2/6 stable systolic ejection murmur

Musculos…
```

| category | text | canonical | polarity | certainty | temporality | who | section/speaker | value |
|---|---|---|---|---|---|---|---|---|
| treatment | Follow up | follow-up | present | certain | current | patient | chief_complaint |  |
| medical_history | tobacco use | tobacco use | present | certain | current | patient | social_history |  |
| numeric | 2 years | 2 year | present | certain | current | patient | social_history | 2 year |
| medication | Bumex | bumetanide | present | certain | current | patient | medications |  |
| dosage | 2 mg | bumetanide 2mg | present | certain | current | patient | medications | 2 mg once daily |
| medication | Cozaar | losartan | present | certain | current | patient | medications |  |
| dosage | 100 mg | losartan 100mg | present | certain | current | patient | medications | 100 mg daily |
| medication | Norvasc | amlodipine | present | certain | current | patient | medications |  |
| dosage | 5 mg | amlodipine 5mg | present | certain | current | patient | medications | 5 mg once daily |
| symptom | chest pain | chest pain | present | certain | current | patient | ros |  |
| symptom | shortness of breath | dyspnea | present | certain | current | patient | ros |  |
| symptom | ankle swelling | edema | present | certain | current | patient | ros |  |
| investigation | Blood pressure | blood pressure measurement | present | certain | current | patient | exam |  |
| numeric | Blood pressure is 128/72 | blood pressure 128/72 | present | certain | current | patient | exam | 128/72 |
| investigation | vital signs | vital signs | present | certain | current | patient | exam |  |
| investigation | JVD | physical examination | absent | certain | current | patient | exam |  |
| investigation | Auscultation | physical examination | present | certain | current | patient | exam |  |
| investigation | Auscultation | physical examination | present | certain | current | patient | exam |  |
| symptom | murmur | murmur | present | certain | current | patient | exam |  |
| symptom | edema | edema | present | certain | current | patient | exam |  |
| investigation | echocardiogram | echocardiogram | present | certain | current | patient | results |  |
| dosage | 55% | ? 55% | present | certain | current | patient | results | 55 % |
| diagnosis | mitral regurgitation | mitral regurgitation | present | certain | current | patient | results |  |
| diagnosis | CHF | heart failure | present | certain | current | patient | assessment |  |
| treatment | emergency room | referral | present | uncertain | current | patient | assessment |  |
| diagnosis | uncontrolled hypertension | hypertension | present | uncertain | current | patient | assessment |  |
| treatment | monitoring | conservative management | present | uncertain | current | patient | assessment |  |
| treatment | Patient Education | counseling/education | present | certain | current | patient | assessment |  |
| treatment | Counseling | counseling/education | present | certain | current | patient | assessment |  |
| investigation | echocardiogram | echocardiogram | present | certain | current | patient | assessment |  |
| medication | medication | medication | present | certain | current | patient | assessment |  |
| treatment | Treatment | conservative management | present | certain | current | patient | assessment |  |
| treatment | continue | medication management | present | certain | current | patient | assessment |  |
| medication | Bumex | bumetanide | present | certain | current | patient | assessment |  |
| dosage | 2 mg | bumetanide 2mg | present | certain | current | patient | assessment | 2 mg once daily |
| treatment | referral to | referral | present | certain | current | patient | assessment |  |
| treatment | nutritionist | referral | present | certain | current | patient | assessment |  |
| treatment | consultation | referral | present | certain | current | patient | assessment |  |
| investigation | sodium | sodium level | present | certain | current | patient | assessment |  |
| diagnosis | Hypertension | hypertension | present | certain | current | patient | assessment |  |
| treatment | Patient Education | counseling/education | present | certain | current | patient | assessment |  |
| treatment | Counseling | counseling/education | present | certain | current | patient | assessment |  |
| medication | medication | medication | present | certain | current | patient | assessment | daily |
| investigation | blood pressure cuff | blood pressure measurement | present | certain | current | patient | assessment |  |
| investigation | blood pressures | blood pressure measurement | present | certain | current | patient | assessment |  |
| treatment | Treatment | conservative management | present | certain | current | patient | assessment |  |
| treatment | continue | medication management | present | certain | current | patient | assessment |  |
| medication | Cozaar | losartan | present | certain | current | patient | assessment |  |
| dosage | 100 mg | losartan 100mg | present | certain | current | patient | assessment | 100 mg daily |
| medication | Norvasc | amlodipine | present | certain | current | patient | assessment |  |
| dosage | 5 mg | amlodipine 5mg | present | certain | current | patient | assessment | 5 mg once daily |
| investigation | ultrasound | ultrasound | present | certain | current | patient | assessment |  |
| investigation | further evaluation | diagnostic workup | present | certain | current | patient | assessment |  |
| symptom | murmur | murmur | present | certain | current | patient | assessment |  |
| treatment | treatment plan | conservative management | present | certain | current | patient | plan |  |
| treatment | call me | referral | present | uncertain | current | patient | plan |  |
| numeric | 2 days | 2 day | present | certain | current | patient | plan | 2 day |

## aci_bench_test_taskB_1_D2N088-virtassist

**source** (1563 words, 97 facts)

```
[doctor] hi , andrew . how are you ?
[patient] hey , good to see you .
[doctor] i'm doing well , i'm doing well .
[patient] good .
[doctor] so , i know the nurse told you about dax . i'd like to tell dax a little bit about you .
[patient] sure .
[doctor] uh , so , andrew is a 59-year-old male with a past medical history , significant for depression , type two diabetes , and hypertension who presents today with an upper respiratory infection . so , andrew , what's going on ?
[patient] yeah . we were doing a bit of work out in the yard in the last week or so and i started to feel really tired , was short of breath . um , we- we're not wearing masks as much at the end of the summer and i think …
```

| category | text | canonical | polarity | certainty | temporality | who | section/speaker | value |
|---|---|---|---|---|---|---|---|---|
| numeric | 59-year-old | age 59 years | present | certain | current | patient | doctor | 59 years |
| medical_history | depression | depression | present | certain | historical | patient | doctor |  |
| medical_history | type two diabetes | type 2 diabetes | present | certain | historical | patient | doctor |  |
| medical_history | hypertension | hypertension | present | certain | historical | patient | doctor |  |
| medical_history | upper respiratory infection | upper respiratory infection | present | certain | historical | patient | doctor |  |
| symptom | tired | fatigue | present | certain | current | patient | patient |  |
| symptom | short of breath | dyspnea | present | certain | current | patient | patient |  |
| medication | covid vaccines | vaccine | present | certain | current | patient | doctor |  |
| medical_history | seasonal allergies | allergic rhinitis | present | uncertain | historical | patient | doctor |  |
| symptom | shortness of breath | dyspnea | present | uncertain | current | patient | doctor |  |
| symptom | short of breath | dyspnea | present | uncertain | current | patient | doctor |  |
| treatment | walking | lifestyle modification | present | uncertain | current | patient | doctor |  |
| treatment | rest | rest/activity modification | present | uncertain | current | patient | doctor |  |
| symptom | winded | dyspnea | present | certain | current | patient | patient |  |
| symptom | coughing | cough | present | uncertain | current | patient | doctor |  |
| symptom | fevers | fever | present | uncertain | current | patient | doctor |  |
| symptom | muscle aches | muscle pain | present | uncertain | current | patient | doctor |  |
| symptom | joint pain | joint pain | present | uncertain | current | patient | doctor |  |
| symptom | fatigue | fatigue | present | uncertain | current | patient | doctor |  |
| symptom | elbows hurt | elbow pain | present | certain | current | patient | patient |  |
| symptom | tired | fatigue | present | certain | current | patient | patient |  |
| diagnosis | depression | depression | present | uncertain | current | patient | doctor |  |
| medication | medication | medication | absent | certain | current | patient | doctor |  |
| medication | medication | medication | present | certain | current | patient | doctor |  |
| diagnosis | diabetes | diabetes | present | uncertain | current | patient | doctor |  |
| treatment | watching | conservative management | present | uncertain | current | patient | doctor |  |
| treatment | diet | lifestyle modification | present | uncertain | current | patient | doctor |  |
| treatment | monitoring | conservative management | present | certain | current | patient | patient |  |
| investigation | sugar levels | blood glucose | present | certain | current | patient | patient |  |
| treatment | diet | lifestyle modification | present | certain | current | patient | patient |  |
| treatment | elevated | elevation/compression | present | certain | current | patient | doctor |  |
| diagnosis | high blood pressure | hypertension | present | uncertain | current | patient | doctor |  |
| treatment | monitoring | conservative management | present | uncertain | current | patient | doctor |  |
| investigation | blood pressures | blood pressure measurement | present | uncertain | current | patient | doctor |  |
| treatment | monitoring | conservative management | present | certain | current | patient | patient |  |
| treatment | under control | conservative management | present | certain | current | patient | patient |  |
| medication | medication | medication | present | certain | current | patient | doctor |  |
| symptom | shortness of breath | dyspnea | present | certain | current | patient | doctor |  |
| symptom | joint pain | joint pain | present | certain | current | patient | doctor |  |
| symptom | nausea | nausea | absent | certain | current | patient | doctor |  |
| symptom | vomiting | vomiting | absent | certain | current | patient | doctor |  |
| symptom | diarrhea | diarrhea | absent | certain | current | patient | doctor |  |
| investigation | physical exam | physical examination | present | uncertain | current | patient | doctor |  |
| investigation | vital signs | vital signs | present | certain | current | patient | doctor |  |
| investigation | vital signs | vital signs | present | certain | current | patient | doctor |  |
| symptom | fever | fever | present | certain | current | patient | doctor |  |
| investigation | listen to your heart | physical examination | present | uncertain | current | patient | doctor |  |
| investigation | physical exam | physical examination | present | certain | current | patient | doctor |  |
| investigation | lung exam | physical examination | present | certain | current | patient | doctor |  |
| symptom | cough | cough | present | certain | current | patient | doctor |  |
| symptom | edema | edema | present | certain | current | patient | doctor |  |
| symptom | pain | pain | present | certain | current | patient | doctor |  |
| investigation | palpation | physical examination | present | certain | current | patient | doctor |  |
| investigation | chest x-ray | x-ray | present | certain | current | patient | doctor |  |
| investigation | chest x-ray | x-ray | present | certain | current | patient | doctor |  |
| diagnosis | pneumonia | pneumonia | absent | certain | current | patient | doctor |  |
| diagnosis | diabetic | diabetes | present | certain | current | patient | doctor |  |
| investigation | labs | blood work | present | certain | current | patient | doctor |  |
| diagnosis | diabetic | diabetes | present | certain | current | patient | doctor |  |
| investigation | labs | blood work | present | certain | current | patient | doctor |  |
| investigation | hemoglobin a1c | hemoglobin a1c | present | certain | current | patient | doctor |  |
| treatment | elevated | elevation/compression | present | certain | current | patient | doctor |  |
| diagnosis | upper respiratory infection | upper respiratory infection | present | certain | current | patient | doctor |  |
| diagnosis | viral syndrome | upper respiratory infection | present | certain | current | patient | doctor |  |
| investigation | covid test | covid test | present | certain | current | patient | doctor |  |
| diagnosis | covid | covid-19 | present | certain | current | patient | doctor |  |
| numeric | couple of days | couple of day | present | certain | current | patient | doctor | couple of day |
| diagnosis | covid | covid-19 | present | certain | current | patient | doctor |  |
| medication | robitussin | guaifenesin | present | uncertain | current | patient | doctor |  |
| symptom | cough | cough | present | uncertain | current | patient | doctor |  |
| medication | ibuprofen | ibuprofen | present | uncertain | current | patient | doctor |  |
| medication | tylenol | acetaminophen | present | uncertain | current | patient | doctor |  |
| symptom | fever | fever | present | uncertain | current | patient | doctor |  |
| diagnosis | depression | depression | present | certain | current | patient | doctor |  |
| treatment | refer you to | referral | present | uncertain | current | patient | doctor |  |
| treatment | psychotherapy | counseling/education | present | uncertain | current | patient | doctor |  |
| numeric | few months | few month | present | certain | current | patient | patient | few month |
| diagnosis | type two diabetes | type 2 diabetes | present | certain | current | patient | doctor |  |
| medication | metformin | metformin | present | certain | current | patient | doctor |  |
| dosage | 1000 milligrams | metformin 1000milligrams | present | certain | current | patient | doctor | 1000 milligrams twice daily |
| investigation | hemoglobin a1c | hemoglobin a1c | present | uncertain | current | patient | doctor |  |
| numeric | four months | four month | present | certain | current | patient | doctor | four month |
| investigation | hemoglobin a1c | hemoglobin a1c | present | certain | current | patient | doctor |  |
| diagnosis | high blood pressure | hypertension | present | certain | current | patient | doctor |  |
| treatment | managing | conservative management | present | certain | current | patient | doctor |  |
| treatment | continue | medication management | present | certain | current | patient | doctor |  |
| medication | lisinopril | lisinopril | present | certain | current | patient | doctor |  |
| dosage | 20 milligrams | lisinopril 20milligrams | present | certain | current | patient | doctor | 20 milligrams a day |
| investigation | lipid panel | lipid panel | present | uncertain | current | patient | doctor |  |
| treatment | refill | medication management | present | uncertain | current | patient | doctor |  |
| medication | lisinopril | lisinopril | present | uncertain | current | patient | doctor |  |
| medication | lisinopril | lisinopril | present | certain | current | patient | doctor |  |
| dosage | 20 milligrams | lisinopril 20milligrams | present | certain | current | patient | doctor | 20 milligrams daily |
| treatment | follow-up appointment | follow-up | present | certain | current | patient | doctor |  |
| treatment | see you again | follow-up | present | certain | current | patient | doctor |  |
| numeric | four months | four month | present | certain | current | patient | doctor | four month |
| treatment | let me know if | referral | present | uncertain | current | patient | doctor |  |

**reference** (664 words, 100 facts)

```
CHIEF COMPLAINT

Upper respiratory infection.

HISTORY OF PRESENT ILLNESS

Andrew Campbell is a 59-year-old male with a past medical history significant for depression, type 2 diabetes, and hypertension. He presents today with an upper respiratory infection.

The patient reports that he has been doing a bit of work out in the yard in the last week or so. He started to feel really tired and short of breath. The patient denies coughing up anything, but he feels like he will soon be coughing up phlegm. He denies having a fever, but he felt a little warm. He attributed this to exerting himself. He reports that his elbows hurt quite a bit. He notes his knees were pretty tired and he felt some ten…
```

| category | text | canonical | polarity | certainty | temporality | who | section/speaker | value |
|---|---|---|---|---|---|---|---|---|
| diagnosis | Upper respiratory infection | upper respiratory infection | present | certain | current | patient | chief_complaint |  |
| numeric | 59-year-old | age 59 years | present | certain | current | patient | hpi | 59 years |
| medical_history | depression | depression | present | certain | historical | patient | hpi |  |
| medical_history | type 2 diabetes | type 2 diabetes | present | certain | historical | patient | hpi |  |
| medical_history | hypertension | hypertension | present | certain | historical | patient | hpi |  |
| diagnosis | upper respiratory infection | upper respiratory infection | present | certain | current | patient | hpi |  |
| symptom | tired | fatigue | present | certain | current | patient | hpi |  |
| symptom | short of breath | dyspnea | present | certain | current | patient | hpi |  |
| symptom | coughing | cough | absent | certain | current | patient | hpi |  |
| symptom | coughing up phlegm | sputum | present | certain | current | patient | hpi |  |
| symptom | fever | fever | absent | certain | current | patient | hpi |  |
| symptom | elbows hurt | elbow pain | present | certain | current | patient | hpi |  |
| symptom | tired | fatigue | present | certain | current | patient | hpi |  |
| medical_history | COVID | covid-19 | present | certain | historical | patient | hpi |  |
| medication | vaccinations | vaccine | present | certain | historical | patient | hpi |  |
| medical_history | seasonal allergies | allergic rhinitis | absent | certain | historical | patient | hpi |  |
| diagnosis | depression | depression | present | certain | current | patient | hpi |  |
| diagnosis | diabetes | diabetes | present | certain | current | patient | hpi |  |
| treatment | monitoring | conservative management | present | certain | current | patient | hpi |  |
| investigation | sugar levels | blood glucose | present | certain | current | patient | hpi |  |
| treatment | diet | lifestyle modification | present | certain | current | patient | hpi |  |
| treatment | elevated | elevation/compression | absent | certain | current | patient | hpi |  |
| treatment | monitoring | conservative management | present | certain | current | patient | hpi |  |
| investigation | blood pressure | blood pressure measurement | present | certain | current | patient | hpi |  |
| treatment | monitoring | conservative management | present | certain | current | patient | hpi |  |
| investigation | blood pressure | blood pressure measurement | present | certain | current | patient | hpi |  |
| investigation | blood pressure | blood pressure measurement | present | certain | current | patient | hpi |  |
| treatment | under control | conservative management | present | certain | current | patient | hpi |  |
| treatment | continued | medication management | present | certain | current | patient | hpi |  |
| medication | lisinopril | lisinopril | present | certain | current | patient | hpi |  |
| dosage | 20 mg | lisinopril 20mg | present | certain | current | patient | hpi | 20 mg daily |
| symptom | nausea | nausea | absent | certain | current | patient | hpi |  |
| symptom | vomiting | vomiting | absent | certain | current | patient | hpi |  |
| symptom | diarrhea | diarrhea | absent | certain | current | patient | hpi |  |
| symptom | fever | fever | absent | certain | current | patient | ros |  |
| symptom | dyspnea on exertion | dyspnea on exertion | present | certain | current | patient | ros |  |
| symptom | shortness of breath | dyspnea | present | certain | current | patient | ros |  |
| symptom | cough | cough | present | certain | current | patient | ros |  |
| symptom | nausea | nausea | absent | certain | current | patient | ros |  |
| symptom | diarrhea | diarrhea | absent | certain | current | patient | ros |  |
| symptom | knee pain | knee pain | present | certain | current | patient | ros |  |
| diagnosis | depression | depression | present | certain | current | patient | ros |  |
| symptom | rhonchi | rhonchi | present | certain | current | patient | exam |  |
| symptom | cough | cough | present | certain | current | patient | exam |  |
| symptom | murmurs | murmur | absent | certain | current | patient | exam |  |
| symptom | Edema | edema | present | certain | current | patient | exam |  |
| symptom | Pain | pain | present | certain | current | patient | exam |  |
| investigation | palpation | physical examination | present | certain | current | patient | exam |  |
| investigation | X-ray of the chest | x-ray | present | certain | current | patient | results |  |
| diagnosis | pneumonia | pneumonia | absent | uncertain | current | patient | results |  |
| investigation | Hemoglobin A1c | hemoglobin a1c | present | certain | current | patient | results |  |
| treatment | elevated | elevation/compression | present | certain | current | patient | results |  |
| numeric | 59-year-old | age 59 years | present | certain | current | patient | assessment | 59 years |
| medical_history | depression | depression | present | certain | historical | patient | assessment |  |
| medical_history | type 2 diabetes | type 2 diabetes | present | certain | historical | patient | assessment |  |
| medical_history | hypertension | hypertension | present | certain | historical | patient | assessment |  |
| diagnosis | upper respiratory infection | upper respiratory infection | present | certain | current | patient | assessment |  |
| diagnosis | Upper respiratory infection | upper respiratory infection | present | certain | current | patient | assessment |  |
| diagnosis | viral syndrome | upper respiratory infection | present | certain | current | patient | assessment |  |
| investigation | chest x-ray | x-ray | present | certain | current | patient | assessment |  |
| diagnosis | COVID-19 | covid-19 | present | certain | current | patient | assessment |  |
| medication | vaccination | vaccine | present | certain | current | patient | assessment |  |
| investigation | Additional Testing | diagnostic workup | present | certain | current | patient | assessment |  |
| investigation | COVID-19 test | covid test | present | certain | current | patient | assessment |  |
| treatment | Treatment | conservative management | present | certain | current | patient | assessment |  |
| medication | Robitussin | guaifenesin | present | certain | current | patient | assessment |  |
| symptom | cough | cough | present | certain | current | patient | assessment |  |
| medication | ibuprofen | ibuprofen | present | uncertain | current | patient | assessment |  |
| medication | Tylenol | acetaminophen | present | uncertain | current | patient | assessment |  |
| symptom | fever | fever | present | uncertain | current | patient | assessment |  |
| diagnosis | Depression | depression | present | certain | current | patient | assessment |  |
| treatment | Treatment | conservative management | present | certain | current | patient | assessment |  |
| medication | medication | medication | present | certain | current | patient | assessment |  |
| treatment | psychotherapy | counseling/education | present | certain | current | patient | assessment |  |
| diagnosis | Diabetes type 2 | type 2 diabetes | present | certain | current | patient | assessment |  |
| investigation | blood glucose levels | blood glucose | present | certain | current | patient | assessment |  |
| treatment | well controlled | conservative management | present | certain | current | patient | assessment |  |
| investigation | home monitoring | home monitoring | present | certain | current | patient | assessment |  |
| investigation | hemoglobin A1c | hemoglobin a1c | present | certain | current | patient | assessment |  |
| treatment | elevated | elevation/compression | present | certain | current | patient | assessment |  |
| investigation | Additional Testing | diagnostic workup | present | certain | current | patient | assessment |  |
| investigation | hemoglobin A1c | hemoglobin a1c | present | certain | current | patient | assessment |  |
| numeric | 4 months | 4 month | present | certain | current | patient | assessment | 4 month |
| treatment | Treatment | conservative management | present | certain | current | patient | assessment |  |
| medication | metformin | metformin | present | certain | current | patient | assessment |  |
| dosage | 1000 mg | metformin 1000mg | present | certain | current | patient | assessment | 1000 mg twice daily |
| diagnosis | Hypertension | hypertension | present | certain | current | patient | assessment |  |
| medication | lisinopril | lisinopril | present | certain | current | patient | assessment |  |
| investigation | blood pressures | blood pressure measurement | present | certain | current | patient | assessment |  |
| treatment | well controlled | conservative management | present | certain | current | patient | assessment |  |
| investigation | home monitoring | home monitoring | present | certain | current | patient | assessment |  |
| investigation | Additional Testing | diagnostic workup | present | certain | current | patient | assessment |  |
| investigation | lipid panel | lipid panel | present | certain | current | patient | assessment |  |
| treatment | Treatment | conservative management | present | certain | current | patient | assessment |  |
| treatment | continue | medication management | present | certain | current | patient | assessment |  |
| medication | lisinopril | lisinopril | present | certain | current | patient | assessment |  |
| dosage | 20 mg | lisinopril 20mg | present | certain | current | patient | assessment | 20 mg once daily |
| treatment | refilled | medication management | present | certain | current | patient | assessment |  |
| numeric | 4 months | 4 month | present | certain | current | patient | plan | 4 month |
| treatment | treatment plan | conservative management | present | certain | current | patient | plan |  |

## mts_dialog_test_chat_2023_33

**source** (36 words, 0 facts)

```
Doctor: Do you smoke cigarettes?
Patient: No, I do not.
Doctor: Good, no one should.
Patient: Yeah, it's a bad habit.
Doctor: Okay. How about alcohol?
Patient: No, I don't drink either.
Doctor: Okay.
Patient: Yeah.
```

| category | text | canonical | polarity | certainty | temporality | who | section/speaker | value |
|---|---|---|---|---|---|---|---|---|

**reference** (8 words, 0 facts)

```
The patient does not smoke nor drink alcohol.
```

| category | text | canonical | polarity | certainty | temporality | who | section/speaker | value |
|---|---|---|---|---|---|---|---|---|

## mts_dialog_test_chat_2023_135

**source** (108 words, 5 facts)

```
Doctor: Good afternoon, sir, before we begin, how old are you?
Patient: I'm twenty-six years old, sir. 
Doctor: Good, and what race do you identify with?
Patient: I'm an African American, sir. 
Doctor: Great, so how did you get hurt?
Patient: I stepped off a hilo at work, and I felt this pop in my left leg. 
Doctor: Where did you feel the pop? 
Patient: It was in the back of the leg.
Doctor: What treatments have you had for this knee so far? 
Patient: I got put in a splint, and they recommended I follow up with you at ABC orthopedics. 
Doctor: Good, thank you, and welcome.
```

| category | text | canonical | polarity | certainty | temporality | who | section/speaker | value |
|---|---|---|---|---|---|---|---|---|
| numeric | six years | six year | present | certain | current | patient | patient | six year |
| treatment | treatments | conservative management | present | certain | current | patient | doctor |  |
| treatment | splint | brace/splint/cast | present | certain | current | patient | patient |  |
| treatment | follow up with | follow-up | present | certain | current | patient | patient |  |
| treatment | orthopedics | referral | present | certain | current | patient | patient |  |

**reference** (48 words, 3 facts)

```
The patient is a 26-year-old African-American male who states that he was stepping off a hilo at work when he felt a sudden pop in the posterior aspect of his left leg.  The patient was placed in posterior splint and followed up at ABC orthopedics for further care.
```

| category | text | canonical | polarity | certainty | temporality | who | section/speaker | value |
|---|---|---|---|---|---|---|---|---|
| numeric | 26-year-old | age 26 years | present | certain | current | patient | hpi | 26 years |
| treatment | posterior splint | brace/splint/cast | present | certain | current | patient | hpi |  |
| treatment | orthopedics | referral | present | certain | current | patient | hpi |  |

## mts_dialog_test_chat_2023_104

**source** (52 words, 3 facts)

```
Doctor: Have you ever had surgery on any of your extremities, like your arms or legs? 
Patient: Yes actually, I've had surgery on my foot, as well as my knee. 
Doctor: Good, have you had any other surgeries on anywhere else?
Patient: Now that I remember, yes, I had a tummy surgery.
```

| category | text | canonical | polarity | certainty | temporality | who | section/speaker | value |
|---|---|---|---|---|---|---|---|---|
| treatment | surgery | surgery | present | certain | current | patient | doctor |  |
| treatment | surgery | surgery | present | certain | current | patient | patient |  |
| treatment | surgery | surgery | present | certain | historical | patient | patient |  |

**reference** (7 words, 3 facts)

```
Foot surgery, abdominal surgery, and knee surgery.
```

| category | text | canonical | polarity | certainty | temporality | who | section/speaker | value |
|---|---|---|---|---|---|---|---|---|
| treatment | surgery | surgery | present | certain | current | patient | pmh |  |
| treatment | surgery | surgery | present | certain | current | patient | pmh |  |
| treatment | surgery | surgery | present | certain | current | patient | pmh |  |

## mts_dialog_validation_65

**source** (179 words, 6 facts)

```
Doctor: How old are you young man?
Patient: I am nineteen. 
Doctor: What happened? How did you get hurt?
Patient: I was in a fight. Some people are just rude. 
Doctor: Oh, that's bad! How did you hurt your right hand?
Patient: Ah, I punched that other guy in face or maybe his mouth, I don't remember exactly but he got a good one. Later, in anger I punched in a glass. It broke the glass and spilled all the drink. I think I got a cut as it was bleeding badly. 
Doctor: I see three cuts in your right hand. 
Doctor: When you came here in Emergency your wound was clean and looked like somebody tried to fix your cut. Do you remember any details about it?
Patient: Yeah, I remember there was a navy c…
```

| category | text | canonical | polarity | certainty | temporality | who | section/speaker | value |
|---|---|---|---|---|---|---|---|---|
| symptom | cut | laceration | present | certain | current | patient | patient |  |
| symptom | bleeding | bleeding | present | certain | current | patient | patient |  |
| symptom | cut | laceration | present | certain | current | patient | doctor |  |
| symptom | cut | laceration | present | certain | current | patient | patient |  |
| treatment | gauze | wound care | present | certain | current | patient | patient |  |
| symptom | bleeding | bleeding | present | certain | current | patient | patient |  |

**reference** (89 words, 6 facts)

```
The patient is a 19-year-old male who was involved in a fight approximately an hour prior to his ED presentation.  He punched a guy few times on the face, might be the mouth and then punched a drinking glass, breaking it and lacerating his right hand.  He has three lacerations on his right hand.  His wound was cleaned out thoroughly with tap water, and one of the navy corpsman tried to use Superglue and gauze to repair it.  However, it continues to bleed and he is here for evaluation.
```

| category | text | canonical | polarity | certainty | temporality | who | section/speaker | value |
|---|---|---|---|---|---|---|---|---|
| numeric | 19-year-old | age 19 years | present | certain | current | patient | hpi | 19 years |
| numeric | an hour | an hour | present | certain | current | patient | hpi | an hour |
| symptom | lacerations | laceration | present | certain | current | patient | hpi |  |
| treatment | gauze | wound care | present | certain | current | patient | hpi |  |
| treatment | continues | medication management | present | certain | current | patient | hpi |  |
| symptom | bleed | bleeding | present | certain | current | patient | hpi |  |

## mts_dialog_validation_88

**source** (6 words, 1 facts)

```
Doctor: Any medication intolerances? 
Patient: No.
```

| category | text | canonical | polarity | certainty | temporality | who | section/speaker | value |
|---|---|---|---|---|---|---|---|---|
| medication | medication | medication | absent | certain | current | patient | doctor |  |

**reference** (9 words, 0 facts)

```
There is no known drug intolerance in the past.
```

| category | text | canonical | polarity | certainty | temporality | who | section/speaker | value |
|---|---|---|---|---|---|---|---|---|

## mts_dialog_test_chat_2023_106

**source** (10 words, 1 facts)

```
Doctor: Do you have any known drug allergies? 
Patient: No.
```

| category | text | canonical | polarity | certainty | temporality | who | section/speaker | value |
|---|---|---|---|---|---|---|---|---|
| medical_history | allergies | allergic rhinitis | absent | certain | historical | patient | doctor |  |

**reference** (6 words, 1 facts)

```
She has no known drug allergies.
```

| category | text | canonical | polarity | certainty | temporality | who | section/speaker | value |
|---|---|---|---|---|---|---|---|---|
| medical_history | allergies | allergic rhinitis | absent | certain | historical | patient | allergies |  |

## dialogue_soap_validation_168

**source** (415 words, 47 facts)

```
Doctor: Hello, I see that you're an 81-year-old man with a history of left total hip replacement, open discectomy at the L4/5 level more than 10 years prior, percutaneous coronary intervention 3 years prior, and periodontitis detected 1 month before presentation. Can you tell me more about your current symptoms?
Patient: Yeah, I've been suffering from severe back pain for the last 2 days.
Doctor: I see. We did some plain lumbar spine radiographs which showed spondylosis but no signs of fractures. Additionally, your laboratory tests were significant for a white blood cell count of 1.2 × 104 cells/μl and C-reactive protein level of 13.8 mg/dl. Based on these findings, we admitted you for treat…
```

| category | text | canonical | polarity | certainty | temporality | who | section/speaker | value |
|---|---|---|---|---|---|---|---|---|
| numeric | 81-year-old | age 81 years | present | certain | current | patient | doctor | 81 years |
| treatment | total hip replacement | surgery | present | certain | historical | patient | doctor |  |
| treatment | discectomy | surgery | present | certain | historical | patient | doctor |  |
| numeric | 10 years | 10 year | present | certain | current | patient | doctor | 10 year |
| treatment | percutaneous coronary intervention | surgery | present | certain | historical | patient | doctor |  |
| numeric | 3 years | 3 year | present | certain | current | patient | doctor | 3 year |
| numeric | 1 month | 1 month | present | certain | current | patient | doctor | 1 month |
| symptom | back pain | back pain | present | certain | current | patient | patient |  |
| numeric | ast 2 | ast 2 | present | certain | current | patient | patient | 2 |
| investigation | spine radiographs | x-ray | present | certain | current | patient | doctor |  |
| diagnosis | fractures | fracture | absent | uncertain | current | patient | doctor |  |
| investigation | laboratory tests | blood work | present | certain | current | patient | doctor |  |
| investigation | white blood cell count | white blood cell count | present | certain | historical | patient | doctor |  |
| investigation | C-reactive protein | crp | present | certain | historical | patient | doctor |  |
| dosage | 13.8 mg/dl | ? 13.8mg/dl | present | certain | current | patient | doctor | 13.8 mg/dl |
| treatment | admitted | hospital admission | present | certain | current | patient | doctor |  |
| treatment | treatment | conservative management | present | certain | current | patient | doctor |  |
| treatment | admitted | hospital admission | present | uncertain | current | patient | patient |  |
| numeric | Two days | two day | present | certain | current | patient | doctor | two day |
| treatment | admission | hospital admission | present | certain | current | patient | doctor |  |
| investigation | magnetic resonance imaging | mri | present | certain | current | patient | doctor |  |
| diagnosis | discitis | osteomyelitis | present | certain | current | patient | doctor |  |
| investigation | blood cultures | blood culture | present | certain | current | patient | doctor |  |
| investigation | urine cultures | urine culture | present | certain | current | patient | doctor |  |
| treatment | therapy | conservative management | present | certain | current | patient | doctor |  |
| medication | vancomycin | vancomycin | present | certain | current | patient | doctor |  |
| dosage | 1 g | vancomycin 1g | present | certain | current | patient | doctor | 1 g every 12 hours |
| medication | ceftriaxone | ceftriaxone | present | certain | current | patient | doctor |  |
| dosage | 1 g | ceftriaxone 1g | present | certain | current | patient | doctor | 1 g every 24 hours |
| numeric | 6 days | 6 day | present | certain | current | patient | doctor | 6 day |
| investigation | urine cultures | urine culture | present | certain | current | patient | patient |  |
| investigation | urine cultures | urine culture | absent | certain | current | patient | doctor |  |
| investigation | transthoracic echocardiogram | echocardiogram | present | certain | current | patient | doctor |  |
| diagnosis | endocarditis | endocarditis | absent | certain | current | patient | doctor |  |
| treatment | treatment | conservative management | present | uncertain | current | patient | patient |  |
| treatment | isolate | hospital admission | present | certain | current | patient | doctor |  |
| medication | penicillin | penicillin | present | certain | current | patient | doctor |  |
| treatment | isolate | hospital admission | present | certain | current | patient | doctor |  |
| medication | penicillin | penicillin | present | certain | current | patient | doctor |  |
| dosage | 0.012 μg | penicillin 0.012μg | present | certain | current | patient | doctor | 0.012 μg |
| diagnosis | infection | infection | present | certain | current | patient | doctor |  |
| medication | penicillin | penicillin | present | certain | current | patient | doctor |  |
| treatment | treatment | conservative management | present | certain | current | patient | doctor |  |
| treatment | continue | medication management | present | certain | current | patient | doctor |  |
| treatment | monitor | conservative management | present | certain | current | patient | doctor |  |
| treatment | treatment plan | conservative management | present | certain | current | patient | doctor |  |
| treatment | continue | medication management | present | certain | current | patient | doctor |  |

**reference** (233 words, 41 facts)

```
S: The patient is an 81-year-old male with a history of left total hip replacement, open discectomy at L4/5, percutaneous coronary intervention, and periodontitis. He presents with severe back pain that started 2 days ago.
O: Physical examination and recent medical interventions include plain lumbar spine radiographs showing spondylosis without fractures, and MRI revealing discitis at L5/S1. Laboratory tests showed a white blood cell count of 1.2 × 10^4 cells/μl and a C-reactive protein level of 13.8 mg/dl. Disc and blood cultures were performed; disc culture was positive for G. morbillorum, while blood and urine cultures were negative. Transthoracic echocardiogram showed no signs of endocar…
```

| category | text | canonical | polarity | certainty | temporality | who | section/speaker | value |
|---|---|---|---|---|---|---|---|---|
| numeric | 81-year-old | age 81 years | present | certain | current | patient | hpi | 81 years |
| treatment | total hip replacement | surgery | present | certain | historical | patient | hpi |  |
| treatment | discectomy | surgery | present | certain | historical | patient | hpi |  |
| treatment | percutaneous coronary intervention | surgery | present | certain | historical | patient | hpi |  |
| symptom | back pain | back pain | present | certain | historical | patient | hpi |  |
| numeric | 2 days ago | 2 day ago | present | certain | current | patient | hpi | 2 day |
| investigation | Physical examination | physical examination | present | certain | current | patient | exam |  |
| treatment | interventions | conservative management | present | certain | current | patient | exam |  |
| investigation | spine radiographs | x-ray | present | certain | current | patient | exam |  |
| diagnosis | fractures | fracture | absent | certain | current | patient | exam |  |
| investigation | MRI | mri | absent | certain | current | patient | exam |  |
| diagnosis | discitis | osteomyelitis | absent | certain | current | patient | exam |  |
| investigation | Laboratory tests | blood work | present | certain | current | patient | exam |  |
| investigation | white blood cell count | white blood cell count | present | certain | current | patient | exam |  |
| investigation | C-reactive protein | crp | present | certain | current | patient | exam |  |
| dosage | 13.8 mg/dl | ? 13.8mg/dl | present | certain | current | patient | exam | 13.8 mg/dl |
| investigation | blood cultures | blood culture | present | certain | current | patient | exam |  |
| investigation | urine cultures | urine culture | absent | certain | current | patient | exam |  |
| investigation | Transthoracic echocardiogram | echocardiogram | present | certain | current | patient | exam |  |
| diagnosis | endocarditis | endocarditis | absent | uncertain | current | patient | exam |  |
| treatment | isolate | hospital admission | present | certain | current | patient | exam |  |
| medication | penicillin | penicillin | present | certain | current | patient | exam |  |
| dosage | 0.012 μg | penicillin 0.012μg | present | certain | current | patient | exam | 0.012 μg |
| diagnosis | discitis | osteomyelitis | present | certain | current | patient | assessment |  |
| diagnosis | infection | infection | present | uncertain | current | patient | assessment |  |
| investigation | imaging | imaging | absent | certain | current | patient | assessment |  |
| investigation | urine cultures | urine culture | absent | certain | current | patient | assessment |  |
| medication | penicillin | penicillin | present | certain | current | patient | assessment |  |
| treatment | Continue | medication management | present | certain | current | patient | plan |  |
| treatment | therapy | conservative management | present | certain | current | patient | plan |  |
| medication | vancomycin | vancomycin | present | certain | current | patient | plan |  |
| medication | ceftriaxone | ceftriaxone | present | certain | current | patient | plan |  |
| medication | penicillin | penicillin | present | certain | current | patient | plan |  |
| treatment | Maintain | medication management | present | certain | current | patient | plan |  |
| treatment | Monitor | conservative management | present | certain | current | patient | plan |  |
| treatment | treatment | conservative management | present | certain | current | patient | plan |  |
| treatment | Educate | counseling/education | present | certain | current | patient | plan |  |
| treatment | treatment | conservative management | present | certain | current | patient | plan |  |
| treatment | follow-up appointments | follow-up | present | certain | current | patient | plan |  |
| treatment | monitor | conservative management | present | certain | current | patient | plan |  |
| treatment | therapy | conservative management | present | certain | current | patient | plan |  |

## dialogue_soap_test_243

**source** (292 words, 7 facts)

```
Doctor: Hello, I just wanted to inform you about your son's situation after the accident. He was presented to the emergency department following a high-speed front-end collision with another vehicle. Was he the one driving?
Family: No, he was in the front seat but not driving. He was restrained, thankfully.
Doctor: I see. The vehicle he was in was struck head-on. Do you happen to know the speed at the time of the collision?
Family: We were told it was in excess of 79 miles per hour.
Doctor: Yes, that's correct. When your son arrived at the hospital, he was unconscious and not breathing independently. Our team attempted intubation at the scene, but unfortunately, it was unsuccessful.
Family: …
```

| category | text | canonical | polarity | certainty | temporality | who | section/speaker | value |
|---|---|---|---|---|---|---|---|---|
| treatment | emergency department | referral | present | certain | current | patient | doctor |  |
| treatment | intubation | surgery | present | certain | current | patient | doctor |  |
| investigation | radiographs | x-ray | present | uncertain | current | patient | doctor |  |
| investigation | radiographs | x-ray | present | certain | current | patient | doctor |  |
| diagnosis | fractures | fracture | absent | certain | current | patient | doctor |  |
| treatment | surgical | surgery | present | uncertain | historical | patient | doctor |  |
| treatment | surgical | surgery | absent | certain | historical | patient | doctor |  |

**reference** (203 words, 7 facts)

```
S: The patient, a male, was involved in a high-speed front-end collision while seated in the front passenger seat, restrained. The family reported the vehicle was traveling in excess of 79 miles per hour at the time of the accident. The patient was unconscious and not breathing independently upon arrival at the hospital. There was no known past medical or surgical history that could have contributed to the incident.
O: Upon arrival, the patient was found to be unconscious with unsuccessful intubation attempted at the scene. Radiographs revealed internal decapitation with AO assimilation between the anterior arch of the atlas and the basiocciput. No fractures, including the odontoid process, …
```

| category | text | canonical | polarity | certainty | temporality | who | section/speaker | value |
|---|---|---|---|---|---|---|---|---|
| treatment | surgical | surgery | absent | uncertain | historical | patient | hpi |  |
| treatment | intubation | surgery | present | certain | current | patient | exam |  |
| investigation | Radiographs | x-ray | present | certain | current | patient | exam |  |
| diagnosis | fractures | fracture | absent | certain | current | patient | exam |  |
| investigation | imaging | imaging | present | certain | historical | patient | assessment |  |
| treatment | grief counseling | counseling/education | present | uncertain | current | patient | plan |  |
| treatment | surgical intervention | surgery | absent | uncertain | current | patient | plan |  |

## dialogue_soap_validation_280

**source** (404 words, 39 facts)

```
Doctor: Hi there, I see you were admitted to our hospital complaining of abdominal pain that has persisted for 3 days. How are you feeling now?
Patient: Hi doctor, the pain is still there, and it's quite uncomfortable.
Doctor: I understand. You seem alert and not pale, which is a good sign. Your blood pressure is at 112/70 mmHg, and you have a regular pulse of 78 bpm. We've also conducted some laboratory tests. Your white blood cell count is 7530/μL, hemoglobin concentration is 11.0 g/dL, platelet count is 249,000/μL, glutamic oxaloacetic transaminase concentration is 22 IU/L, glutamic pyruvic transaminase concentration is 9 IU/L, and lactic dehydrogenase concentration is 259 IU/L.
Patient: …
```

| category | text | canonical | polarity | certainty | temporality | who | section/speaker | value |
|---|---|---|---|---|---|---|---|---|
| treatment | admitted | hospital admission | present | certain | current | patient | doctor |  |
| symptom | abdominal pain | abdominal pain | present | certain | current | patient | doctor |  |
| numeric | 3 days | 3 day | present | certain | current | patient | doctor | 3 day |
| symptom | pain | pain | present | certain | current | patient | patient |  |
| symptom | pale | pallor | absent | certain | current | patient | doctor |  |
| investigation | blood pressure | blood pressure measurement | present | certain | current | patient | doctor |  |
| numeric | 112/70 mmHg | blood pressure 112/70 | present | certain | current | patient | doctor | 112/70 mmhg |
| investigation | pulse | heart rate measurement | present | certain | current | patient | doctor |  |
| numeric | pulse of 78 bpm | pulse 78 | present | certain | current | patient | doctor | 78 bpm |
| investigation | laboratory tests | blood work | present | certain | current | patient | doctor |  |
| investigation | white blood cell count | white blood cell count | present | certain | current | patient | doctor |  |
| investigation | hemoglobin | hemoglobin level | present | certain | current | patient | doctor |  |
| dosage | 11.0 g/dL | ? 11.0g/dl | present | certain | current | patient | doctor | 11.0 g/dl |
| investigation | platelet count | platelet count | present | certain | current | patient | doctor |  |
| dosage | 22 IU/L | ? 22iu/l | present | certain | current | patient | doctor | 22 iu/l |
| dosage | 9 IU/L | ? 9iu/l | present | certain | current | patient | doctor | 9 iu/l |
| dosage | 259 IU/L | ? 259iu/l | present | certain | current | patient | doctor | 259 iu/l |
| symptom | abdominal pain | abdominal pain | present | certain | current | patient | doctor |  |
| investigation | computed tomography | ct scan | present | certain | current | patient | doctor |  |
| investigation | CT | ct scan | present | certain | current | patient | doctor |  |
| investigation | scan | imaging | present | certain | current | patient | doctor |  |
| investigation | magnetic resonance imaging | mri | present | certain | current | patient | doctor |  |
| investigation | MRI | mri | present | certain | current | patient | doctor |  |
| diagnosis | tumor | cancer | present | certain | current | patient | doctor |  |
| investigation | CT | ct scan | present | certain | current | patient | doctor |  |
| investigation | MRI scans | mri | present | certain | current | patient | doctor |  |
| treatment | resection | surgery | present | certain | current | patient | doctor |  |
| diagnosis | cyst | sebaceous cyst | present | certain | current | patient | doctor |  |
| diagnosis | cyst | sebaceous cyst | present | certain | current | patient | doctor |  |
| treatment | Dermabond | wound care | present | certain | current | patient | doctor |  |
| diagnosis | tumor | cancer | present | certain | current | patient | doctor |  |
| diagnosis | cyst | sebaceous cyst | absent | certain | current | patient | doctor |  |
| treatment | released | discharge | absent | certain | current | patient | doctor |  |
| diagnosis | cavity | dental caries | absent | certain | current | patient | doctor |  |
| diagnosis | tumor | cancer | present | certain | current | patient | doctor |  |
| treatment | surgery | surgery | present | certain | current | patient | patient |  |
| treatment | surgery | surgery | present | certain | current | patient | doctor |  |
| diagnosis | tumors | cancer | present | certain | current | patient | doctor |  |
| treatment | procedure | surgery | present | certain | current | patient | patient |  |

**reference** (263 words, 45 facts)

```
S: The patient, admitted with a chief complaint of persistent abdominal pain for 3 days, describes the pain as still present and quite uncomfortable. No additional symptoms were reported.
O: The patient appears alert and not pale. Vital signs include blood pressure at 112/70 mmHg and a regular pulse of 78 bpm. Laboratory findings are as follows: white blood cell count 7530/μL (normal range: 4500-10,000/μL), hemoglobin 11.0 g/dL (normal range for females: 12-16 g/dL, for males: 13.5-17.5 g/dL), platelet count 249,000/μL (normal range: 150,000-450,000/μL), glutamic oxaloacetic transaminase 22 IU/L (normal range: 0-40 IU/L), glutamic pyruvic transaminase 9 IU/L (normal range: 0-40 IU/L), and la…
```

| category | text | canonical | polarity | certainty | temporality | who | section/speaker | value |
|---|---|---|---|---|---|---|---|---|
| treatment | admitted | hospital admission | present | certain | current | patient | hpi |  |
| symptom | abdominal pain | abdominal pain | present | certain | current | patient | hpi |  |
| numeric | 3 days | 3 day | present | certain | current | patient | hpi | 3 day |
| symptom | pain | pain | present | certain | current | patient | hpi |  |
| symptom | pale | pallor | absent | uncertain | current | patient | exam |  |
| investigation | Vital signs | vital signs | present | certain | current | patient | exam |  |
| investigation | blood pressure | blood pressure measurement | present | certain | current | patient | exam |  |
| numeric | blood pressure at 112/70 mmHg | blood pressure 112/70 | present | certain | current | patient | exam | 112/70 mmhg |
| investigation | pulse | heart rate measurement | present | certain | current | patient | exam |  |
| numeric | pulse of 78 bpm | pulse 78 | present | certain | current | patient | exam | 78 bpm |
| investigation | white blood cell count | white blood cell count | present | certain | current | patient | exam |  |
| investigation | hemoglobin | hemoglobin level | present | certain | current | patient | exam |  |
| numeric | hemoglobin 11.0 g/dL | hemoglobin 11.0 | present | certain | current | patient | exam | 11.0 g/dl |
| dosage | 12-16 g/dL | ? 12-16g/dl | present | certain | current | patient | exam | 12-16 g/dl |
| dosage | 13.5-17.5 g/dL | ? 13.5-17.5g/dl | present | certain | current | patient | exam | 13.5-17.5 g/dl |
| investigation | platelet count | platelet count | present | certain | current | patient | exam |  |
| dosage | 22 IU/L | ? 22iu/l | present | certain | current | patient | exam | 22 iu/l |
| dosage | 0-40 IU/L | ? 0-40iu/l | present | certain | current | patient | exam | 0-40 iu/l |
| dosage | 9 IU/L | ? 9iu/l | present | certain | current | patient | exam | 9 iu/l |
| dosage | 0-40 IU/L | ? 0-40iu/l | present | certain | current | patient | exam | 0-40 iu/l |
| dosage | 259 IU/L | ? 259iu/l | present | certain | current | patient | exam | 259 iu/l |
| dosage | 140-280 IU/L | ? 140-280iu/l | present | certain | current | patient | exam | 140-280 iu/l |
| investigation | Imaging | imaging | present | certain | current | patient | exam |  |
| investigation | CT | ct scan | present | certain | current | patient | exam |  |
| investigation | MRI | mri | present | certain | current | patient | exam |  |
| treatment | resection | surgery | present | certain | current | patient | exam |  |
| diagnosis | tumors | cancer | present | uncertain | current | patient | assessment |  |
| investigation | imaging | imaging | present | certain | current | patient | assessment |  |
| treatment | surgical | surgery | present | certain | current | patient | assessment |  |
| treatment | resection | surgery | present | certain | current | patient | assessment |  |
| treatment | resection | surgery | present | certain | historical | patient | plan |  |
| treatment | management | conservative management | present | uncertain | current | patient | plan |  |
| treatment | monitoring | conservative management | present | uncertain | current | patient | plan |  |
| diagnosis | infection | infection | present | uncertain | current | patient | plan |  |
| treatment | pain management | referral | present | uncertain | current | patient | plan |  |
| treatment | regular follow-up | follow-up | present | uncertain | current | patient | plan |  |
| treatment | maintain | medication management | present | uncertain | current | patient | plan |  |
| treatment | balanced diet | lifestyle modification | present | uncertain | current | patient | plan |  |
| treatment | increase physical activity | lifestyle modification | present | uncertain | current | patient | plan |  |
| treatment | as tolerated | rest/activity modification | present | uncertain | current | patient | plan |  |
| treatment | Education | counseling/education | present | uncertain | current | patient | plan |  |
| treatment | follow-up care | follow-up | present | uncertain | current | patient | plan |  |
| treatment | referrals | referral | absent | certain | current | patient | plan |  |
| treatment | Compliance | medication management | present | certain | current | patient | plan |  |
| treatment | follow-up | follow-up | present | certain | current | patient | plan |  |

## dialogue_soap_test_192

**source** (437 words, 35 facts)

```
Doctor: Good morning. I see you have a past medical history of hypertension. Can you tell me about the symptoms you've been experiencing lately?
Patient: Well, about a week after I had a respiratory viral infection, I started to develop some progressive cerebellar ataxia. I've been having trouble speaking clearly and my walking has become unsteady.
Doctor: I see. How long have your symptoms worsened?
Patient: They got worse for about 2 weeks and then remained stable.
Doctor: When were you admitted to our service?
Patient: I was admitted a year after my symptoms started.
Doctor: It seems that you were previously diagnosed with parainfectious cerebellar ataxia. Have you experienced any other s…
```

| category | text | canonical | polarity | certainty | temporality | who | section/speaker | value |
|---|---|---|---|---|---|---|---|---|
| medical_history | hypertension | hypertension | present | certain | historical | patient | doctor |  |
| medical_history | viral infection | upper respiratory infection | present | certain | historical | patient | patient |  |
| symptom | trouble speaking | slurred speech | present | certain | current | patient | patient |  |
| treatment | walking | lifestyle modification | present | certain | current | patient | patient |  |
| symptom | unsteady | difficulty walking | present | certain | current | patient | patient |  |
| numeric | 2 weeks | 2 week | present | certain | current | patient | patient | 2 week |
| treatment | admitted | hospital admission | present | certain | current | patient | doctor |  |
| treatment | admitted | hospital admission | present | certain | current | patient | patient |  |
| numeric | a year | a year | present | certain | current | patient | patient | a year |
| symptom | nausea | nausea | present | certain | current | patient | patient |  |
| symptom | vomiting | vomiting | present | certain | current | patient | patient |  |
| numeric | ast 6 | ast 6 | present | certain | current | patient | patient | 6 |
| symptom | tingling | tingling | present | certain | historical | patient | patient |  |
| investigation | neurological examination | physical examination | present | certain | current | patient | doctor |  |
| symptom | dysarthria | slurred speech | present | certain | current | patient | doctor |  |
| symptom | muscle weakness | weakness | absent | certain | current | patient | doctor |  |
| investigation | deep tendon reflexes | physical examination | present | certain | current | patient | doctor |  |
| investigation | electromyography | emg | present | certain | current | patient | patient |  |
| investigation | electromyography | emg | present | certain | current | patient | doctor |  |
| diagnosis | polyneuropathy | neuropathy | present | certain | current | patient | doctor |  |
| treatment | treatment | conservative management | present | certain | current | patient | patient |  |
| treatment | prescribed | medication management | present | certain | current | patient | doctor |  |
| medication | methylprednisolone | methylprednisolone | present | certain | current | patient | doctor |  |
| dosage | 1 g | methylprednisolone 1g | present | certain | current | patient | doctor | 1 g qd |
| numeric | 3 days | 3 day | present | certain | current | patient | doctor | 3 day |
| investigation | tissue transglutaminase | celiac testing | present | certain | current | patient | doctor |  |
| diagnosis | GAD | anxiety | present | certain | current | patient | doctor |  |
| investigation | lumbar puncture | lumbar puncture | present | uncertain | current | patient | patient |  |
| investigation | lumbar puncture | lumbar puncture | present | certain | current | patient | doctor |  |
| numeric | 1 year | 1 year | present | certain | current | patient | doctor | 1 year |
| treatment | continue | medication management | present | uncertain | current | patient | doctor |  |
| treatment | monitor | conservative management | present | uncertain | current | patient | doctor |  |
| treatment | continue | medication management | present | uncertain | current | patient | doctor |  |
| treatment | follow up with us | follow-up | present | uncertain | current | patient | doctor |  |
| treatment | let us know if | referral | present | uncertain | current | patient | doctor |  |

**reference** (273 words, 34 facts)

```
S: The patient, with a history of hypertension, reports progressive cerebellar ataxia starting a week after a respiratory viral infection, characterized by severe dysarthria, unsteady gait, and inability to walk or stand unattended. Symptoms worsened over two weeks and then stabilized. Additional symptoms include daily nausea, vomiting for six months, significant weight loss (66 pounds), and tingling in hands and feet. No recent bowel or bladder dysfunction or mood changes reported.
O: Neurological examination revealed severe dysarthria, bilateral horizontal nystagmus, pronounced ataxia, bilateral dysdiadochokinesia, generalized hypotonia, and absent deep tendon reflexes in lower limbs. Sens…
```

| category | text | canonical | polarity | certainty | temporality | who | section/speaker | value |
|---|---|---|---|---|---|---|---|---|
| medical_history | hypertension | hypertension | present | certain | historical | patient | hpi |  |
| medical_history | viral infection | upper respiratory infection | present | certain | historical | patient | hpi |  |
| symptom | dysarthria | slurred speech | present | certain | historical | patient | hpi |  |
| symptom | unsteady | difficulty walking | present | certain | historical | patient | hpi |  |
| numeric | two weeks | two week | present | certain | current | patient | hpi | two week |
| symptom | nausea | nausea | present | certain | current | patient | hpi |  |
| symptom | vomiting | vomiting | present | certain | current | patient | hpi |  |
| numeric | six months | six month | present | certain | current | patient | hpi | six month |
| symptom | weight loss | weight loss | present | certain | current | patient | hpi |  |
| symptom | tingling | tingling | present | certain | current | patient | hpi |  |
| investigation | Neurological examination | physical examination | present | certain | current | patient | exam |  |
| symptom | dysarthria | slurred speech | present | certain | current | patient | exam |  |
| investigation | deep tendon reflexes | physical examination | absent | certain | current | patient | exam |  |
| investigation | Electromyography | emg | present | certain | current | patient | exam |  |
| diagnosis | polyneuropathy | neuropathy | present | certain | current | patient | exam |  |
| investigation | Blood tests | blood work | present | certain | current | patient | exam |  |
| investigation | Lumbar puncture | lumbar puncture | present | certain | current | patient | exam |  |
| diagnosis | viral infection | upper respiratory infection | present | uncertain | current | patient | assessment |  |
| diagnosis | polyneuropathy | neuropathy | present | uncertain | current | patient | assessment |  |
| treatment | Continue | medication management | present | certain | current | patient | plan |  |
| medication | methylprednisolone | methylprednisolone | present | certain | current | patient | plan |  |
| treatment | treatment | conservative management | present | certain | current | patient | plan |  |
| treatment | monitor | conservative management | present | certain | current | patient | plan |  |
| investigation | diagnostic workup | diagnostic workup | present | uncertain | current | patient | plan |  |
| investigation | lumbar puncture | lumbar puncture | present | uncertain | current | patient | plan |  |
| investigation | MRI of the brain | mri | present | uncertain | current | patient | plan |  |
| investigation | biopsy | biopsy | present | uncertain | current | patient | plan |  |
| treatment | Regular follow-ups | follow-up | present | certain | current | patient | plan |  |
| treatment | treatment | conservative management | present | certain | current | patient | plan |  |
| treatment | Patient education | counseling/education | present | certain | current | patient | plan |  |
| treatment | Referral to | referral | present | certain | current | patient | plan |  |
| treatment | neurologist | referral | present | certain | current | patient | plan |  |
| treatment | management | conservative management | present | certain | current | patient | plan |  |
| treatment | second opinion | referral | present | certain | current | patient | plan |  |

## dialogue_soap_test_140

**source** (463 words, 33 facts)

```
Doctor: Hello, I see that you're a 27-year-old Chinese Han female. You were accidentally noted to have a low SUA level on two occasions during your routine check-ups in the local hospital. How have you been feeling lately?
Patient: Hi, doctor. I've been feeling fine. I don't have any discomfort or pain.
Doctor: That's good to hear. Have you experienced any joint pain, loin pain, hematuria, urine foam, nausea, vomiting, anorexia, or diarrhea?
Patient: No, I haven't had any of those symptoms.
Doctor: Alright. Since you were asymptomatic but had those low SUA levels, you were admitted into the metabolism division at the Affiliated Hospital of Qingdao University for further investigation. We per…
```

| category | text | canonical | polarity | certainty | temporality | who | section/speaker | value |
|---|---|---|---|---|---|---|---|---|
| numeric | 27-year-old | age 27 years | present | certain | current | patient | doctor | 27 years |
| treatment | check-ups | immunization plan | present | certain | current | patient | doctor |  |
| symptom | pain | pain | present | certain | current | patient | patient |  |
| symptom | joint pain | joint pain | absent | certain | current | patient | doctor |  |
| symptom | pain | pain | absent | certain | current | patient | doctor |  |
| symptom | hematuria | hematuria | absent | certain | current | patient | doctor |  |
| symptom | nausea | nausea | absent | certain | current | patient | doctor |  |
| symptom | vomiting | vomiting | absent | certain | current | patient | doctor |  |
| symptom | anorexia | loss of appetite | absent | certain | current | patient | doctor |  |
| symptom | diarrhea | diarrhea | absent | certain | current | patient | doctor |  |
| treatment | admitted | hospital admission | present | certain | historical | patient | doctor |  |
| investigation | imaging | imaging | present | certain | current | patient | doctor |  |
| dosage | 0.33 mg/dl | ? 0.33mg/dl | present | certain | current | patient | doctor | 0.33 mg/dl |
| dosage | 50% | ? 50% | present | certain | current | patient | doctor | 50 % |
| dosage | 7.0 mg/dL | ? 7.0mg/dl | present | certain | current | patient | doctor | 7.0 mg/dl |
| dosage | 6.0 mg/dL | ? 6.0mg/dl | present | certain | current | patient | doctor | 6.0 mg/dl |
| dosage | 10% | ? 10% | present | certain | current | patient | doctor | 10 % |
| investigation | ultrasound | ultrasound | present | certain | current | patient | doctor |  |
| diagnosis | kidney stones | kidney stones | absent | certain | current | patient | doctor |  |
| medical_history | urolithiasis | kidney stones | absent | certain | historical | family | doctor |  |
| medical_history | AKI | acute kidney injury | absent | certain | historical | family | doctor |  |
| dosage | 3.68 mg/dl | ? 3.68mg/dl | present | certain | current | patient | doctor | 3.68 mg/dl |
| dosage | 4.35 mg/dl | ? 4.35mg/dl | present | certain | current | patient | doctor | 4.35 mg/dl |
| treatment | diet | lifestyle modification | present | uncertain | current | patient | doctor |  |
| treatment | treatment | conservative management | present | uncertain | current | patient | patient |  |
| treatment | treatment | conservative management | absent | certain | current | patient | doctor |  |
| treatment | continue | medication management | present | certain | current | patient | doctor |  |
| treatment | monitor | conservative management | present | certain | current | patient | doctor |  |
| treatment | check-ups | immunization plan | present | certain | current | patient | doctor |  |
| treatment | maintain | medication management | present | certain | current | patient | doctor |  |
| treatment | diet | lifestyle modification | present | certain | current | patient | doctor |  |
| treatment | follow up | follow-up | present | certain | current | patient | patient |  |
| treatment | maintain | medication management | present | certain | current | patient | patient |  |

**reference** (243 words, 28 facts)

```
S: The patient is a 27-year-old Chinese Han female who reported feeling fine with no discomfort or pain. She denied experiencing joint pain, loin pain, hematuria, urine foam, nausea, vomiting, anorexia, or diarrhea. She has a vegetarian diet and does not consume meat. There is no significant family history of hereditary diseases or specific physical abnormalities.
O: The patient's SUA level was noted to be 0.33 mg/dL, significantly below the normal female range of 2.5–6.0 mg/dL. FEUA was recorded at 50%, well above the normal range of 4–10%. Other biochemical tests and ultrasound imaging did not reveal any abnormalities, and no kidney stones were found. Both parents have normal SUA levels, a…
```

| category | text | canonical | polarity | certainty | temporality | who | section/speaker | value |
|---|---|---|---|---|---|---|---|---|
| numeric | 27-year-old | age 27 years | present | certain | current | patient | hpi | 27 years |
| symptom | pain | pain | absent | certain | historical | patient | hpi |  |
| symptom | joint pain | joint pain | absent | certain | current | patient | hpi |  |
| symptom | pain | pain | absent | certain | current | patient | hpi |  |
| symptom | hematuria | hematuria | absent | certain | current | patient | hpi |  |
| symptom | nausea | nausea | absent | certain | current | patient | hpi |  |
| symptom | vomiting | vomiting | absent | certain | current | patient | hpi |  |
| symptom | anorexia | loss of appetite | absent | certain | current | patient | hpi |  |
| symptom | diarrhea | diarrhea | absent | certain | current | patient | hpi |  |
| treatment | diet | lifestyle modification | present | certain | current | patient | hpi |  |
| dosage | 0.33 mg/dL | ? 0.33mg/dl | present | certain | current | patient | exam | 0.33 mg/dl |
| dosage | 6.0 mg/dL | ? 6.0mg/dl | present | certain | current | patient | exam | 6.0 mg/dl |
| dosage | 50% | ? 50% | present | certain | current | patient | exam | 50 % |
| dosage | 10% | ? 10% | present | certain | current | patient | exam | 10 % |
| investigation | ultrasound | ultrasound | present | certain | current | patient | exam |  |
| investigation | imaging | imaging | present | certain | current | patient | exam |  |
| diagnosis | kidney stones | kidney stones | absent | certain | current | patient | exam |  |
| symptom | joint pain | joint pain | absent | certain | current | patient | assessment |  |
| investigation | imaging | imaging | absent | certain | current | patient | assessment |  |
| diagnosis | urolithiasis | kidney stones | absent | certain | current | patient | assessment |  |
| treatment | diet | lifestyle modification | present | uncertain | current | patient | assessment |  |
| treatment | treatment | conservative management | absent | certain | current | patient | plan |  |
| treatment | monitoring | conservative management | present | certain | current | patient | plan |  |
| treatment | follow-up | follow-up | present | certain | current | patient | plan |  |
| treatment | check-ups | immunization plan | present | certain | current | patient | plan |  |
| treatment | maintain | medication management | present | certain | current | patient | plan |  |
| treatment | diet | lifestyle modification | present | certain | current | patient | plan |  |
| treatment | management | conservative management | present | certain | current | patient | plan |  |

## dialogue_soap_test_99

**source** (384 words, 69 facts)

```
Patient: Hi doctor, I've been having some issues lately and I'm not sure what's going on.
Doctor: I'm sorry to hear that. Can you tell me more about your symptoms?
Patient: Well, I've been experiencing urinary frequency and nocturia for about a month now.
Doctor: I see. Let's discuss your medical history to better understand your situation. I know you have multiple psychiatric conditions, including bipolar disorder, attention deficit hyperactivity disorder, oppositional defiant disorder, posttraumatic stress disorder, and poor impulse control. What medications are you currently taking?
Patient: I'm taking clonidine 0.1 mg three times daily, guanfacine 4 mg daily, bupropion sustained-release …
```

| category | text | canonical | polarity | certainty | temporality | who | section/speaker | value |
|---|---|---|---|---|---|---|---|---|
| symptom | urinary frequency | urinary frequency | present | certain | current | patient | patient |  |
| symptom | nocturia | nocturia | present | certain | current | patient | patient |  |
| diagnosis | bipolar disorder | bipolar disorder | present | certain | current | patient | doctor |  |
| diagnosis | attention deficit hyperactivity disorder | adhd | present | certain | current | patient | doctor |  |
| medication | medications | medication | present | certain | current | patient | doctor |  |
| medication | clonidine | clonidine | present | certain | current | patient | patient |  |
| dosage | 0.1 mg | clonidine 0.1mg | present | certain | current | patient | patient | 0.1 mg three times daily |
| medication | guanfacine | guanfacine | present | certain | current | patient | patient |  |
| dosage | 4 mg | guanfacine 4mg | present | certain | current | patient | patient | 4 mg daily |
| medication | bupropion | bupropion | present | certain | current | patient | patient |  |
| dosage | 150 mg | bupropion 150mg | present | certain | current | patient | patient | 150 mg daily |
| medication | quetiapine | quetiapine | present | certain | current | patient | patient |  |
| dosage | 200 mg | quetiapine 200mg | present | certain | current | patient | patient | 200 mg twice daily |
| medication | lithium | lithium | present | certain | current | patient | patient |  |
| dosage | 450 mg | lithium 450mg | present | certain | current | patient | patient | 450 mg three times daily |
| medication | lithium | lithium | present | certain | current | patient | patient |  |
| numeric | 5 years old | age 5 years | present | certain | current | patient | patient | 5 years |
| numeric | a year | a year | present | certain | current | patient | doctor | a year |
| investigation | lithium level | drug level | present | certain | historical | patient | doctor |  |
| dosage | 1.1 mmol/L | ? 1.1mmol/l | present | certain | current | patient | doctor | 1.1 mmol/l |
| investigation | serum creatinine | creatinine | present | certain | historical | patient | doctor |  |
| dosage | 0.78 mg/dL | ? 0.78mg/dl | present | certain | current | patient | doctor | 0.78 mg/dl |
| investigation | glomerular filtration rate | creatinine | present | certain | historical | patient | doctor |  |
| investigation | eGFR | creatinine | present | certain | current | patient | doctor |  |
| dosage | 86 ml | ? 86ml | present | certain | current | patient | doctor | 86 ml |
| investigation | physical examination | physical examination | present | certain | current | patient | doctor |  |
| investigation | Urinalysis | urinalysis | present | certain | current | patient | doctor |  |
| symptom | hematuria | hematuria | absent | certain | current | patient | doctor |  |
| diagnosis | proteinuria | proteinuria | absent | certain | current | patient | doctor |  |
| investigation | Blood tests | blood work | present | certain | current | patient | doctor |  |
| investigation | lithium level | drug level | present | certain | current | patient | doctor |  |
| dosage | 1.4 mmol/L | ? 1.4mmol/l | present | certain | current | patient | doctor | 1.4 mmol/l |
| investigation | TSH | thyroid function test | present | certain | current | patient | doctor |  |
| numeric | TSH of 5.09 | tsh 5.09 | present | certain | current | patient | doctor | 5.09 |
| medication | calcium | calcium supplement | present | certain | current | patient | doctor |  |
| dosage | 11.1 mg/dL | calcium supplement 11.1mg/dl | present | certain | current | patient | doctor | 11.1 mg/dl |
| dosage | 10.6 mg/dL | calcium supplement 10.6mg/dl | present | certain | current | patient | doctor | 10.6 mg/dl |
| investigation | creatinine | creatinine | present | certain | current | patient | doctor |  |
| dosage | 1.15 mg/dL | calcium supplement 1.15mg/dl | present | certain | current | patient | doctor | 1.15 mg/dl |
| treatment | primary care physician | referral | present | certain | current | patient | doctor |  |
| treatment | PCP | referral | present | certain | current | patient | doctor |  |
| medication | lithium | lithium | present | certain | current | patient | doctor |  |
| dosage | 450 mg | lithium 450mg | present | certain | current | patient | doctor | 450 mg twice daily |
| treatment | initiated | medication management | present | certain | current | patient | doctor |  |
| medication | levothyroxine | levothyroxine | present | certain | current | patient | doctor |  |
| diagnosis | hypothyroidism | hypothyroidism | present | certain | current | patient | doctor |  |
| numeric | One week | one week | present | certain | current | patient | doctor | one week |
| investigation | lithium level | drug level | present | certain | current | patient | doctor |  |
| dosage | 1.1 mmol/L | ? 1.1mmol/l | present | certain | current | patient | doctor | 1.1 mmol/l |
| numeric | couple of weeks | couple of week | present | certain | current | patient | doctor | couple of week |
| investigation | creatinine | creatinine | present | certain | current | patient | doctor |  |
| dosage | 1.3 mg/dL | ? 1.3mg/dl | present | certain | current | patient | doctor | 1.3 mg/dl |
| treatment | PCP | referral | present | certain | current | patient | doctor |  |
| treatment | discontinue | medication management | present | certain | current | patient | doctor |  |
| medication | lithium | lithium | present | certain | current | patient | doctor |  |
| treatment | tapering | medication management | present | certain | current | patient | doctor |  |
| numeric | 3 weeks | 3 week | present | certain | current | patient | doctor | 3 week |
| investigation | lithium level | drug level | present | certain | current | patient | doctor |  |
| dosage | 0.1 mmol/L | ? 0.1mmol/l | present | certain | current | patient | doctor | 0.1 mmol/l |
| numeric | four weeks | four week | present | certain | current | patient | doctor | four week |
| treatment | discontinuation | medication management | present | certain | current | patient | doctor |  |
| investigation | serum creatinine | creatinine | present | certain | current | patient | doctor |  |
| treatment | continued | medication management | present | certain | current | patient | doctor |  |
| treatment | nephrology | referral | present | certain | current | patient | doctor |  |
| treatment | referral | referral | present | certain | current | patient | doctor |  |
| treatment | nephrology | referral | present | certain | current | patient | doctor |  |
| investigation | physical examination | physical examination | present | certain | current | patient | doctor |  |
| treatment | nephrologist | referral | present | certain | current | patient | doctor |  |
| treatment | treatment | conservative management | present | certain | current | patient | doctor |  |

**reference** (235 words, 67 facts)

```
S: The patient reports experiencing urinary frequency and nocturia for about a month. The patient has a history of multiple psychiatric conditions including bipolar disorder, attention deficit hyperactivity disorder, oppositional defiant disorder, posttraumatic stress disorder, and poor impulse control. Medications include clonidine 0.1 mg three times daily, guanfacine 4 mg daily, bupropion sustained-release 150 mg daily, quetiapine 200 mg twice daily, and lithium 450 mg three times daily, started at age 5.
O: Physical examination was unremarkable. Urinalysis showed specific gravity 1.006, pH 6.0, no hematuria or proteinuria. Blood tests revealed lithium level 1.4 mmol/L, TSH 5.09 uIU/mL (no…
```

| category | text | canonical | polarity | certainty | temporality | who | section/speaker | value |
|---|---|---|---|---|---|---|---|---|
| symptom | urinary frequency | urinary frequency | present | certain | current | patient | hpi |  |
| symptom | nocturia | nocturia | present | certain | current | patient | hpi |  |
| medical_history | bipolar disorder | bipolar disorder | present | certain | historical | patient | hpi |  |
| medical_history | attention deficit hyperactivity disorder | adhd | present | certain | historical | patient | hpi |  |
| medication | Medications | medication | present | certain | current | patient | hpi |  |
| medication | clonidine | clonidine | present | certain | current | patient | hpi |  |
| dosage | 0.1 mg | clonidine 0.1mg | present | certain | current | patient | hpi | 0.1 mg three times daily |
| medication | guanfacine | guanfacine | present | certain | current | patient | hpi |  |
| dosage | 4 mg | guanfacine 4mg | present | certain | current | patient | hpi | 4 mg daily |
| medication | bupropion | bupropion | present | certain | current | patient | hpi |  |
| dosage | 150 mg | bupropion 150mg | present | certain | current | patient | hpi | 150 mg daily |
| medication | quetiapine | quetiapine | present | certain | current | patient | hpi |  |
| dosage | 200 mg | quetiapine 200mg | present | certain | current | patient | hpi | 200 mg twice daily |
| medication | lithium | lithium | present | certain | current | patient | hpi |  |
| dosage | 450 mg | lithium 450mg | present | certain | current | patient | hpi | 450 mg three times daily |
| investigation | Physical examination | physical examination | present | certain | current | patient | exam |  |
| investigation | Urinalysis | urinalysis | present | certain | current | patient | exam |  |
| symptom | hematuria | hematuria | absent | certain | current | patient | exam |  |
| diagnosis | proteinuria | proteinuria | absent | certain | current | patient | exam |  |
| investigation | Blood tests | blood work | present | certain | current | patient | exam |  |
| investigation | lithium level | drug level | present | certain | current | patient | exam |  |
| dosage | 1.4 mmol/L | ? 1.4mmol/l | present | certain | current | patient | exam | 1.4 mmol/l |
| investigation | TSH | thyroid function test | present | certain | current | patient | exam |  |
| numeric | TSH 5.09 | tsh 5.09 | present | certain | current | patient | exam | 5.09 |
| medication | calcium | calcium supplement | present | certain | current | patient | exam |  |
| dosage | 11.1 mg/dL | calcium supplement 11.1mg/dl | present | certain | current | patient | exam | 11.1 mg/dl |
| dosage | 10.6 mg/dL | calcium supplement 10.6mg/dl | present | certain | current | patient | exam | 10.6 mg/dl |
| investigation | creatinine | creatinine | present | certain | current | patient | exam |  |
| numeric | creatinine 1.15 mg/dL | creatinine 1.15 | present | certain | current | patient | exam | 1.15 mg/dl |
| investigation | lithium level | drug level | present | certain | historical | patient | exam |  |
| dosage | 1.1 mmol/L | ? 1.1mmol/l | present | certain | current | patient | exam | 1.1 mmol/l |
| investigation | serum creatinine | creatinine | present | certain | historical | patient | exam |  |
| numeric | creatinine 0.78 mg/dL | creatinine 0.78 | present | certain | current | patient | exam | 0.78 mg/dl |
| investigation | eGFR | creatinine | present | certain | historical | patient | exam |  |
| numeric | eGFR 86 ml/min | egfr 86 | present | certain | current | patient | exam | 86 ml/min |
| treatment | dose adjustment | medication management | present | certain | current | patient | exam |  |
| treatment | initiation | medication management | present | certain | current | patient | exam |  |
| medication | levothyroxine | levothyroxine | present | certain | current | patient | exam |  |
| investigation | lithium level | drug level | present | certain | current | patient | exam |  |
| dosage | 1.1 mmol/L | levothyroxine 1.1mmol/l | present | certain | current | patient | exam | 1.1 mmol/l |
| investigation | creatinine | creatinine | present | certain | current | patient | exam |  |
| dosage | 1.3 mg/dL | levothyroxine 1.3mg/dl | present | certain | current | patient | exam | 1.3 mg/dl |
| medication | lithium | lithium | present | uncertain | current | patient | assessment |  |
| diagnosis | hypercalcemia | hypercalcemia | present | uncertain | current | patient | assessment |  |
| diagnosis | hypothyroidism | hypothyroidism | present | uncertain | current | patient | assessment |  |
| investigation | creatinine levels | creatinine | present | uncertain | current | patient | assessment |  |
| treatment | discontinuation | medication management | present | uncertain | current | patient | assessment |  |
| medication | lithium | lithium | present | uncertain | current | patient | assessment |  |
| diagnosis | renal impairment | chronic kidney disease | present | uncertain | current | patient | assessment |  |
| treatment | primary care physician | referral | present | certain | current | patient | plan |  |
| medication | lithium | lithium | present | certain | current | patient | plan |  |
| dosage | 450 mg | lithium 450mg | present | certain | current | patient | plan | 450 mg twice daily |
| treatment | initiated | medication management | present | certain | current | patient | plan |  |
| medication | levothyroxine | levothyroxine | present | certain | current | patient | plan |  |
| diagnosis | hypothyroidism | hypothyroidism | present | certain | current | patient | plan |  |
| medication | Lithium | lithium | present | certain | current | patient | plan |  |
| treatment | tapered | medication management | present | certain | current | patient | plan |  |
| numeric | 3 weeks | 3 week | present | certain | current | patient | plan | 3 week |
| investigation | renal function | metabolic panel | present | certain | current | patient | plan |  |
| treatment | Nephrology | referral | present | certain | current | patient | plan |  |
| treatment | referral | referral | present | certain | current | patient | plan |  |
| investigation | further evaluation | diagnostic workup | present | certain | current | patient | plan |  |
| treatment | management | conservative management | present | certain | current | patient | plan |  |
| treatment | Follow-up with | follow-up | present | certain | current | patient | plan |  |
| treatment | nephrology | referral | present | certain | current | patient | plan |  |
| investigation | renal function | metabolic panel | present | certain | current | patient | plan |  |
| treatment | treatment | conservative management | present | certain | current | patient | plan |  |
