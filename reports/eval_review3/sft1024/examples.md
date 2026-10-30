# Example errors — sft1024

Each block shows the transcript excerpt, the reference note, the generated note and the flags raised by the factuality checker.

# Split: aci_bench_test_taskB_1

## Best ROUGE-L: `aci_bench_test_taskB_1_D2N097-virtassist`

*highest ROUGE-L in the split*

ROUGE-L 40.1 · length ratio 0.85 · truncated False · degenerate False · hallucination 12.5 · negation-flip 0.0 · numerical consistency 33.3 · coverage 66.7

**Transcript (excerpt)**

```
[doctor] elizabeth , how are you ?
[patient] i'm doing okay . how are you ?
[doctor] doing okay . so i know the nurse told you about dax . i'd like to tell dax a little bit about you , okay ?
[patient] okay .
[doctor] all right . elizabeth is a 66-year-old female with a past medical history of significant for depression and hypertension who presents for her annual exam . so elizabeth , it's been a year since i've seen you .
[patient] mm-hmm .
[doctor] how are you doing ?
[patient] i'm doing well . there's been so many events now that we've been able to get vaccinated , i've been able to see my grandkids again , go to more birthday parties , it's been fantastic .
[doctor] yeah , i know . i've …
```

**Reference note**

```
CHIEF COMPLAINT

Annual exam.

HISTORY OF PRESENT ILLNESS

Elizabeth Peterson is a 66-year-old female with a past medical history significant for depression and hypertension, who presents for her annual exam. It has been a year since I last saw the patient.

The patient reports that she is doing well. She has been to multiple events now that she has been able to get vaccinated for COVID-19. She reports that she has been able to see her grandchildren again and attend birthday parties.

Regarding her depression, she has been going to therapy once a week for the past year. She reports that she is starting to go in person rather than virtual, which has helped even more. The patient has a good support system at home with her husband and her children live down the street.

The patient reports that her blood pressure has been doing well. She has been using the blood pressure cuff once a day and …
```

**Generated note**

```
CHIEF COMPLAINT

The patient is a 66-year-old female who comes in for her annual exam.

HISTORY OF PRESENT ILLNESS

Elizabeth is a 66-year-old female with a past medical history significant for depression and hypertension.  She has been under treatment for these conditions.  She has been doing well.  She has been seeing her grandchildren more often and attending birthday parties.  She has been doing well with her depression.  She has been going to therapy one time per week for the past year.  She has been having difficulty with her depression in the past.  She has been doing well with her hypertension.  She has been monitoring her blood pressure daily.  She has been taking her Lisinopril 20 mg daily.  She has been doing well with her blood pressure.  She has been having some nasal congestion.  She denies any chest pain, shortness of breath, abdominal pain, nausea, vomiting, etc.

REVIEW OF SYSTEMS

Significant for depression, hypertension, and nasal congestion.  Denies any chest pain, shortness of breath, abdominal pain, nausea, vomiting, etc.

PHYSICAL EXAM

VITAL SIGNS:  Blood Pres …
```

- unsupported entities (vs. transcript): electrocardiogram, respiratory rate
- incorrect diagnosis: —  ·  missing diagnosis: —
- incorrect medication: —  ·  missing medication: —
- dosage mismatch: —
- negation flips (vs. reference): —
- unsupported numbers: 1, 130, 130/80, 16, 3, 78, 80, 98
- missing information: {"symptom": ["crackles", "rhonchi", "wheezing"], "diagnosis": ["covid-19"], "investigation": ["diagnostic workup", "home monitoring", "physical examination"]}

## Worst ROUGE-L: `aci_bench_test_taskB_1_D2N118-aci`

*lowest ROUGE-L in the split*

ROUGE-L 4.8 · length ratio 2.50 · truncated True · degenerate True · hallucination 0.0 · negation-flip 0.0 · numerical consistency — · coverage 8.3

**Transcript (excerpt)**

```
[doctor] alright so how're you doing today angela
[patient] i'm doing pretty well
[doctor] alright so looking here at your appointment notes it says you're you're here you think you have a kidney stone you had some in the past so we're gon na take a look at that and then you also have a past medical history of hypertension and diabetes we want to take a look at those as well so first thing what's going on with your kidneys you as what how long ago have you been feeling pain and and how's all that
[patient] pain's been up and down i went to the emergency room last week but now i think i'm doing a little bit better
[doctor] okay so the case of kidney stones so have you had you said you've had  …
```

**Reference note**

```
CHIEF COMPLAINT

Kidney stone.

MEDICAL HISTORY

Patient reports history of hypertension, diabetes, and kidney stones.

MEDICATIONS

Patient reports taking Norvasc 2.5 mg and metformin 500 mg.

REVIEW OF SYSTEMS

Constitutional: Reports insomnia.
Cardiovascular: Denies chest pain.
Gastrointestinal: Denies abdominal pain.
Genitourinary: Denies hematuria.

VITALS

Blood pressure: 150/90 mm Hg

PHYSICAL EXAM

Respiratory
- Auscultation of Lungs: Clear bilaterally. No wheezes, rales, or rhonchi.

Cardiovascular
- Auscultation of Heart: Grade 2/6 systolic ejection murmur, unchanged.

Gastrointestinal
- Examination of Abdomen: No masses or tenderness. No tenderness of the CVA.

RESULTS

A1c: 6.7

ASSESSMENT AND PLAN

1. Kidney stones.
- Medical Reasoning: Patient recently experience an episode of kidney stones which is her 7th or 8th episode. Based on the patient's symptoms and exam today, I t …
```

**Generated note**

```
CHIEF COMPLAINT

The patient Angela comes in for followup.

HISTORY OF PRESENT ILLNESS

The patient states she is doing well.  She has had a history of hypertension and diabetes.  She has had multiple episodes of renal colic.  She has had multiple episodes of renal colic.  She has had multiple episodes of renal colic.  She has had multiple episodes of renal colic.  She has had multiple episodes of renal colic.  She has had multiple episodes of renal colic.  She has had multiple episodes of renal colic.  She has had multiple episodes of renal colic.  She has had multiple episodes of renal colic.  She has had multiple episodes of renal colic.  She has had multiple episodes of renal colic.  She has had multiple episodes of renal colic.  She has had multiple episodes of renal colic.  She has had multiple episodes of renal colic.  She has had multiple episodes of renal colic.  She has had multiple episodes of renal colic.  She has had multiple episodes of renal colic.  She has had multiple episodes of renal colic.  She has had multiple episodes of renal colic.  She has had multiple episod …
```

- unsupported entities (vs. transcript): —
- incorrect diagnosis: —  ·  missing diagnosis: kidney stones
- incorrect medication: —  ·  missing medication: amlodipine, melatonin, metformin
- dosage mismatch: —
- negation flips (vs. reference): —
- unsupported numbers: —
- missing information: {"symptom": ["abdominal pain", "chest pain", "crackles", "hematuria", "insomnia", "murmur"], "diagnosis": ["kidney stones", "stroke"], "medication": ["amlodipine", "melatonin", "metformin"], "investigation": ["blood glucose", "blood pressure measurement", "continuous glucose monitor", "diagnostic workup", "hemoglobin a1c", "physical examination"]}

## Hallucination example: `aci_bench_test_taskB_1_D2N122-aci`

*hallucination example*

ROUGE-L 7.6 · length ratio 1.37 · truncated True · degenerate False · hallucination 89.8 · negation-flip 0.0 · numerical consistency 75.0 · coverage 27.8

**Transcript (excerpt)**

```
[doctor] hey kyle it's nice to see you today can you tell me a little bit about what brought you in
[patient] yeah i went to see my pcp for a cough which they diagnosed as bronchitis but then they did that chest x-ray to make sure i did n't have pneumonia and they found this lung nodule i went for a cat scan that confirmed it and they referred me here to you i'm really nervous document
[doctor] okay well first of all i'm i'm sorry that you're nervous and what we're gon na do is we're gon na partner together okay and i'm gon na be right by your side the whole time to hopefully make you a little less nervous and and recognize the fact that we're you're gon na have a big support team around you …
```

**Reference note**

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
Oxygen Saturation: 98% on room air.
Body Temperature: Afebrile.

PHYSICAL EXAM

Respiratory
- Auscultation of Lungs: Clear and equal bilaterally.

Cardiovascular
- Auscultation of Heart: Regular rate and rhythm.  …
```

**Generated note**

```
CHIEF COMPLAINT

The patient is a 62-year-old female who comes in for evaluation of a right upper lobe lung nodule.

HISTORY OF PRESENT ILLNESS

The patient states that she has had a cough for approximately three months.  She denies any fevers, chills, weight loss, night sweats, hemoptysis, or dyspnea.  The patient has a history of rheumatoid arthritis and is currently taking methotrexate 7.5 mg weekly.  She has a history of smoking and quit approximately 7 years ago.  She has no significant past surgical history.  She has no allergies.  She has no history of tuberculosis.  She has no history of asthma.  She has no history of chronic obstructive pulmonary disease (COPD).  She has no history of hypertension.  She has no history of diabetes mellitus.  She has no history of coronary artery disease.  She has no history of deep vein thrombosis.  She has no history of pulmonary embolism.  She has no history of atrial fibrillation.  She has no history of mitral valve prolapse.  She has no history of mitral regurgitation.  She has no history of tricuspid regurgitation.  She has no history of …
```

- unsupported entities (vs. transcript): adrenal insufficiency, allergic rhinitis, appendicitis, asthma, atrial fibrillation, bell's palsy, cataract, chills, cholecystitis, chronic kidney disease, cirrhosis, conjunctivitis, copd, coronary artery disease, deep vein thrombosis, diabetes, diverticulitis, dizziness, endocarditis, endometriosis
- incorrect diagnosis: —  ·  missing diagnosis: —
- incorrect medication: —  ·  missing medication: —
- dosage mismatch: —
- negation flips (vs. reference): —
- unsupported numbers: 62
- missing information: {"symptom": ["crepitus", "edema", "lump", "murmur"], "medical_history": ["pneumonia"], "investigation": ["blood pressure measurement", "ct scan", "heart rate measurement", "oxygen saturation", "physical examination", "pulmonary function test"]}

## Incorrect medication / dosage example: `aci_bench_test_taskB_1_D2N119-aci`

*incorrect medication / dosage example*

ROUGE-L 6.0 · length ratio 1.88 · truncated True · degenerate False · hallucination 91.5 · negation-flip 0.0 · numerical consistency 0.0 · coverage 21.4

**Transcript (excerpt)**

```
[doctor] hey betty how are you doing
[patient] i'm doing okay i just been really frustrated because with my asthma and it just seems like i can never catch a break never get better i'm always it seems like i'm always coughing and wheezing
[doctor] i'm sorry to hear that what normally triggers your asthma type symptoms
[patient] i find that it's really really when i get sick if i get sick with a cold i almost always know that my asthma is going to flare i did notice one time though that when i went to my aunt's house i i had a flare afterwards and i think it's because of her cat so i try to avoid going there and i have n't really had an issue since
[doctor] okay so now you mentioned that that …
```

**Reference note**

```
CHIEF COMPLAINT

Asthma.

MEDICAL HISTORY

Patient reports history of asthma.

SOCIAL HISTORY

The patient denies the use of any type of cigarette or tobacco product, as well as marijuana. Occasionally, she will be at a bar that allows smoking inside, which does bother the patient. She enjoys being outside and hiking.

ALLERGIES

Denies seasonal allergies.

MEDICATIONS

Patient reports using an albuterol inhaler, 2 puffs.

REVIEW OF SYSTEMS

Respiratory: Reports coughing and wheezing.

VITALS

Blood pressure: 128/82 mm Hg.
Respiratory rate: 16
O2 saturation: 99% on room air.

PHYSICAL EXAM

Neck
- General Examination: Neck is supple without lymphadenopathy. Trachea is midline. No carotid bruit.

Respiratory
- Auscultation of Lungs: Diminished lung sounds throughout with the occasional slight expiratory wheeze, bilaterally.
Cardiovascular
- Auscultation of Heart: Regular rate and rhythm.  …
```

**Generated note**

```
CHIEF COMPLAINT

The patient is a 35-year-old female who comes in for evaluation of asthma.

HISTORY OF PRESENT ILLNESS

The patient states she has asthma and has been having difficulty managing her asthma.  She has been to the ER and Urgent Care multiple times for asthma exacerbations.  She has been given Prednisone by her PCP and Urgent Care providers.  She has been given Albuterol by her PCP and Urgent Care providers.  She has been given Ventolin by her PCP and Urgent Care providers.  She has been given Flovent by her PCP.  She has been given Symbicort by her PCP.  She has been given Pulmicort by her PCP.  She has been given Asmanex by her PCP.  She has been given Azmacort by her PCP.  She has been given Aerobid by her PCP.  She has been given ProAir by her PCP.  She has been given Proventil by her PCP.  She has been given Maxair by her PCP.  She has been given DuoNeb by her PCP.  She has been given Atrovent by her PCP.  She has been given Combivent by her PCP.  She has been given Spiriva by her PCP.  She has been given Advair by her PCP.  She has been given Singulair by her PCP.  …
```

- unsupported entities (vs. transcript): amitriptyline, amoxicillin/clavulanate, amphetamine, aripiprazole, atomoxetine, budesonide, budesonide/formoterol, bupropion, buspirone, cephalexin, cetirizine, citalopram, desvenlafaxine, diphenhydramine, doxycycline, duloxetine, escitalopram, fluoxetine, fluticasone/salmeterol, gabapentin
- incorrect diagnosis: —  ·  missing diagnosis: —
- incorrect medication: amitriptyline, amoxicillin/clavulanate, amphetamine, aripiprazole, atomoxetine, budesonide, budesonide/formoterol, bupropion, buspirone, cephalexin, cetirizine, citalopram, desvenlafaxine, diphenhydramine, doxycycline, duloxetine, escitalopram, fluoxetine, fluticasone/salmeterol, gabapentin, ipratropium, lamotrigine, levetiracetam, levocetirizine, loratadine, methylphenidate, mirtazapine, mometasone, montelukast, nortriptyline, olanzapine, oxcarbazepine, paroxetine, phenytoin, pregabalin, quetiapine, risperidone, sertraline, sulfamethoxazole/trimethoprim, tiotropium, topiramate, valproate, venlafaxine  ·  missing medication: —
- dosage mismatch: —
- negation flips (vs. reference): —
- unsupported numbers: 35
- missing information: {"symptom": ["cough", "lymphadenopathy", "murmur", "wheezing"], "medical_history": ["allergic rhinitis"], "investigation": ["blood pressure measurement", "heart rate measurement", "oxygen saturation", "physical examination", "pulmonary function test", "respiratory rate"]}

## Negation error example: `aci_bench_test_taskB_1_D2N106-aci`

*negation error example*

ROUGE-L 10.6 · length ratio 1.77 · truncated True · degenerate True · hallucination 75.0 · negation-flip 66.7 · numerical consistency 100.0 · coverage 50.0

**Transcript (excerpt)**

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

**Reference note**

```
CHIEF COMPLAINT

Shortness of breath.

HISTORY OF PRESENT ILLNESS
Charles Sullivan is a pleasant 45-year-old male who presents to the clinic today for the evaluation of shortness of breath. The onset of his symptoms began 2 years ago. He has noticed that his breathing is not what it used to be. He describes an increased need to catch his breath. The patient also reports he gets “mid-shortness of breath” without reason. He has been seen at an urgent care where he received a nebulizer treatment and was prescribed an inhaler, which he uses when his symptoms are present. The patient states his symptoms are aggravated by living with a cat in his house and are present even when the cat is not around or is outside. He has experienced epiphora with rheum present that he attributes to allergies. He has had diarrhea after consuming large amounts of alcohol. He denies any symptoms at this time incl …
```

**Generated note**

```
CHIEF COMPLAINT

The patient is here for evaluation of dyspnea.

HISTORY OF PRESENT ILLNESS

The patient is a 45-year-old male who was referred by Dr. Smith for evaluation of dyspnea.  He has been having difficulty breathing for several months.  The patient denies any history of allergies, asthma, or chronic obstructive pulmonary disease (COPD).  He has no history of smoking.  He has been evaluated by his primary physician and has been started on albuterol inhaler.  He has been taking this medication for approximately one month.  He has had some relief of his symptoms.  He has had some episodes of dyspnea while he is outdoors.  He has had some episodes of dyspnea while he is indoors.  He has had some episodes of dyspnea while he is near his cat.  He has had some episodes of dyspnea while he is away from his cat.  He has had some episodes of rhinorrhea.  He has had some episodes of conjunctivitis.  He has had some episodes of pruritus.  He has had some episodes of urticaria.  He has had some episodes of angioedema.  He has had some episodes of laryngospasm.  He has had some episodes o …
```

- unsupported entities (vs. transcript): abdominal pain, blood in stool, bradycardia, chills, conjunctivitis, constipation, copd, dysuria, fatigue, fever, hematuria, hemoptysis, hypertension, hypotension, itching, joint pain, joint swelling, muscle pain, night sweats, nocturia
- incorrect diagnosis: —  ·  missing diagnosis: —
- incorrect medication: —  ·  missing medication: montelukast
- dosage mismatch: —
- negation flips (vs. reference): allergic rhinitis, angioedema, asthma, nausea, rash, vomiting
- unsupported numbers: —
- missing information: {"symptom": ["flare", "throat swelling", "wheezing"], "medication": ["montelukast"], "investigation": ["allergy testing", "diagnostic workup", "oxygen saturation", "pulmonary function test", "x-ray"]}

## Numerical error example: `aci_bench_test_taskB_1_D2N095-virtassist`

*numerical error example*

ROUGE-L 23.0 · length ratio 1.03 · truncated True · degenerate True · hallucination 71.9 · negation-flip 18.2 · numerical consistency 36.8 · coverage 55.0

**Transcript (excerpt)**

```
[doctor] hi , cheryl . how are you ?
[patient] i'm doing well . how are you ?
[doctor] i'm doing well . so i know the nurse told you a little bit about dax . i'd like to tell dax about you .
[patient] okay .
[doctor] cheryl is a 34-year-old female with a past medical history significant for hypertension , who presents today with back pain . cheryl , what happened to your back ?
[patient] so i've been walking a lot lately . i've been walking to ... 30 minutes to an hour or so a day . and all of a sudden , um , when i was walking , my , um , back just kind of seized up on me . and i do n't really know what it was . maybe i was going a little bit faster . but it just all kind of clenched .
[doc …
```

**Reference note**

```
CHIEF COMPLAINT

Back pain.

HISTORY OF PRESENT ILLNESS

Ms. Ramirez is a 34-year-old female with a past medical history significant for hypertension, who presents today with back pain.

The patient reports she has been walking a lot lately, 30 minutes to an hour or so a day. While walking 6 days ago, she felt her back seize up on her. She is not sure what caused it but thinks she was walking a little faster than usual. She describes the sensation as a spasm. She has been taking ibuprofen and using heat on it but it is still pretty stiff. She denies any known trauma or injury to her back. She notes she has been weightlifting around 3 times a week. She did do deadlifts that day before her walk and thinks she may have been using her back more than her legs to lift. She locates the pain in her mid lower back. She denies any lower extremity numbness, tingling, and weakness.

Regarding her hy …
```

**Generated note**

```
CHIEF COMPLAINT

Back pain.

HISTORY OF PRESENT ILLNESS

The patient is a 34-year-old female with a past medical history significant for hypertension, who presents today with back pain.  She has been walking a lot lately, approximately 30 minutes to an hour per day, and suddenly her back "seized" up on her.  She denies any trauma, fever, chills, congestion, cough, chest pain, shortness of breath, numbness, tingling, or weakness in her lower extremities.  She has been taking ibuprofen and applying heat to the area, but it is still stiff.  She has been lifting more frequently, approximately three times a week, and possibly doing deadlifts the day prior to the onset of her back pain.  The pain is located in the lower back bilaterally.  No radiation of pain down her legs.  No paresthesias or weakness in her lower extremities.  Her blood pressure is well-controlled.  She has been monitoring her blood pressure at home and has been following her diet.  She has been taking Lisinopril 10 mg daily.

REVIEW OF SYSTEMS

Significant for hypertension.  Denies fevers, chills, night sweats, weight l …
```

- unsupported entities (vs. transcript): abdominal pain, blurred vision, conjunctivitis, constipation, diarrhea, dizziness, double vision, dysphagia, dysuria, edema, eye exam, fatigue, headache, hearing loss, heart rate measurement, hematuria, hemoptysis, hoarseness, itching, joint pain
- incorrect diagnosis: —  ·  missing diagnosis: lumbar strain
- incorrect medication: —  ·  missing medication: meloxicam
- dosage mismatch: —
- negation flips (vs. reference): nasal congestion, weakness
- unsupported numbers: 0, 130, 130/80, 18, 4, 5, 7, 78, 8, 80, 9, 98.6
- missing information: {"symptom": ["murmur"], "diagnosis": ["allergic rhinitis", "fracture", "lumbar strain"], "medication": ["meloxicam"], "investigation": ["blood work", "home monitoring", "physical examination", "x-ray"]}

## Missing information example: `aci_bench_test_taskB_1_D2N118-aci`

*missing information example*

ROUGE-L 4.8 · length ratio 2.50 · truncated True · degenerate True · hallucination 0.0 · negation-flip 0.0 · numerical consistency — · coverage 8.3

**Transcript (excerpt)**

```
[doctor] alright so how're you doing today angela
[patient] i'm doing pretty well
[doctor] alright so looking here at your appointment notes it says you're you're here you think you have a kidney stone you had some in the past so we're gon na take a look at that and then you also have a past medical history of hypertension and diabetes we want to take a look at those as well so first thing what's going on with your kidneys you as what how long ago have you been feeling pain and and how's all that
[patient] pain's been up and down i went to the emergency room last week but now i think i'm doing a little bit better
[doctor] okay so the case of kidney stones so have you had you said you've had  …
```

**Reference note**

```
CHIEF COMPLAINT

Kidney stone.

MEDICAL HISTORY

Patient reports history of hypertension, diabetes, and kidney stones.

MEDICATIONS

Patient reports taking Norvasc 2.5 mg and metformin 500 mg.

REVIEW OF SYSTEMS

Constitutional: Reports insomnia.
Cardiovascular: Denies chest pain.
Gastrointestinal: Denies abdominal pain.
Genitourinary: Denies hematuria.

VITALS

Blood pressure: 150/90 mm Hg

PHYSICAL EXAM

Respiratory
- Auscultation of Lungs: Clear bilaterally. No wheezes, rales, or rhonchi.

Cardiovascular
- Auscultation of Heart: Grade 2/6 systolic ejection murmur, unchanged.

Gastrointestinal
- Examination of Abdomen: No masses or tenderness. No tenderness of the CVA.

RESULTS

A1c: 6.7

ASSESSMENT AND PLAN

1. Kidney stones.
- Medical Reasoning: Patient recently experience an episode of kidney stones which is her 7th or 8th episode. Based on the patient's symptoms and exam today, I t …
```

**Generated note**

```
CHIEF COMPLAINT

The patient Angela comes in for followup.

HISTORY OF PRESENT ILLNESS

The patient states she is doing well.  She has had a history of hypertension and diabetes.  She has had multiple episodes of renal colic.  She has had multiple episodes of renal colic.  She has had multiple episodes of renal colic.  She has had multiple episodes of renal colic.  She has had multiple episodes of renal colic.  She has had multiple episodes of renal colic.  She has had multiple episodes of renal colic.  She has had multiple episodes of renal colic.  She has had multiple episodes of renal colic.  She has had multiple episodes of renal colic.  She has had multiple episodes of renal colic.  She has had multiple episodes of renal colic.  She has had multiple episodes of renal colic.  She has had multiple episodes of renal colic.  She has had multiple episodes of renal colic.  She has had multiple episodes of renal colic.  She has had multiple episodes of renal colic.  She has had multiple episodes of renal colic.  She has had multiple episodes of renal colic.  She has had multiple episod …
```

- unsupported entities (vs. transcript): —
- incorrect diagnosis: —  ·  missing diagnosis: kidney stones
- incorrect medication: —  ·  missing medication: amlodipine, melatonin, metformin
- dosage mismatch: —
- negation flips (vs. reference): —
- unsupported numbers: —
- missing information: {"symptom": ["abdominal pain", "chest pain", "crackles", "hematuria", "insomnia", "murmur"], "diagnosis": ["kidney stones", "stroke"], "medication": ["amlodipine", "melatonin", "metformin"], "investigation": ["blood glucose", "blood pressure measurement", "continuous glucose monitor", "diagnostic workup", "hemoglobin a1c", "physical examination"]}

## Degenerate output example: `aci_bench_test_taskB_1_D2N091-virtassist`

*degenerate output example*

ROUGE-L 17.5 · length ratio 1.36 · truncated True · degenerate True · hallucination 86.6 · negation-flip 30.0 · numerical consistency 100.0 · coverage 58.8

**Transcript (excerpt)**

```
[doctor] hi jerry , how are you doing ?
[patient] hi , good to see you .
[doctor] good to see you as well . um , so i know that the nurse told you about dax . i'd like to tell dax about you .
[patient] sure .
[doctor] jerry is a 54 year old male with a past medical history , significant for osteoporosis and multiple sclerosis who presents for an annual exam . so jerry , what's been going on since the last time i saw you ?
[patient] uh , we have been traveling all over the country . it's been kind of a stressful summer . kinda adjusting to everything in the fall and so far it's been good , but ah , lack of sleep , it's been really getting to me .
[doctor] okay . all right . and have you taken …
```

**Reference note**

```
CHIEF COMPLAINT

Annual exam.

HISTORY OF PRESENT ILLNESS

Jerry Nguyen a 54-year-old male with a past medical history significant for osteoporosis, and multiple sclerosis, who presents for an annual exam.

The patient states he has been traveling all over the country. He notes it has been a stressful summer and adjusting to everything in the fall.

The patient reports a lack of sleep. He has tried melatonin, meditation, and stretching every morning, but nothing has helped.

For treatment of his osteoporosis, he is on Fosamax. He denies any issues with his joints. He denies any recent broken bones.

Regarding his multiple sclerosis, he last saw the neurologist 6 months ago. He is taking his medication and denies any issues with this. Previously, he experienced right leg weakness, however, this has resolved.

He does have some lingering issues with his right knee after previous surgery, b …
```

**Generated note**

```
CHIEF COMPLAINT

Jerry is a 54-year-old male who comes in for his annual exam.  He has a history of osteoporosis and multiple sclerosis.  He states he has had insomnia lately and has tried various things including melatonin, meditation, and T-stretching without much success.  No new joint pains or recent fractures.  He has seen his neurologist about 6 months ago and has been on her prescribed medications.  He has had some residual weakness in his right leg after knee surgery.  He denies any other symptoms such as chest pain, shortness of breath, etc.

HISTORY OF PRESENT ILLNESS

The patient is a 54-year-old white male who comes in for his annual exam.  He has a history of osteoporosis and multiple sclerosis.  He has been on Fosamax for osteoporosis.  He has had insomnia lately and has tried various things including melatonin, meditation, and T-stretching without much success.  No new joint pains or recent fractures.  He has seen his neurologist about 6 months ago and has been on her prescribed medications.  He has had some residual weakness in his right leg after knee surgery.  He de …
```

- unsupported entities (vs. transcript): abdominal pain, angioedema, anxiety, asthma, blood in stool, blurred vision, burning sensation, chills, confusion, conjunctivitis, constipation, cough, cramping, depression, diarrhea, difficulty walking, dizziness, double vision, dysphagia, dysuria
- incorrect diagnosis: —  ·  missing diagnosis: arthritis, osteoarthritis
- incorrect medication: —  ·  missing medication: —
- dosage mismatch: —
- negation flips (vs. reference): chest pain, fracture, wheezing
- unsupported numbers: —
- missing information: {"symptom": ["crackles", "falls", "rhonchi"], "diagnosis": ["arthritis", "osteoarthritis"], "investigation": ["physical examination", "x-ray"]}

# Split: aci_bench_test_taskC_2

## Best ROUGE-L: `aci_bench_test_taskC_2_D2N162-aci`

*highest ROUGE-L in the split*

ROUGE-L 40.2 · length ratio 0.76 · truncated False · degenerate False · hallucination 22.2 · negation-flip 0.0 · numerical consistency 36.4 · coverage 87.5

**Transcript (excerpt)**

```
[patient] okay
[doctor] hi gregory hi how are you doing today
[patient] good how are you
[doctor] i'm alright so i understand that you were having some you know right ankle pain and some swelling after you fell can you can you tell me a little bit about what happened
[patient] yeah so i was going out to take off the trash and i you know i was icy and i i was being very careful and then i noticed that there must have been a little patch of ice or something because all i know is that i slipped and i was on the ground and i was being really really careful
[doctor] okay yeah i know especially this this winter has been rough so you got ta watch for those little ice patches sometimes well okay so  …
```

**Reference note**

```
CHIEF COMPLAINT

Right ankle pain and swelling.

HISTORY OF PRESENT ILLNESS

Gregory Hernandez is a pleasant 42-year-old male who presents to the clinic today for evaluation of right ankle pain and swelling. The onset of his pain began yesterday after he slipped and fell on the ice while taking out the trash. He states that he was unable to ambulate at the time of injury and that a friend had to help him up. He then proceeded to ice and elevate his ankle throughout the night. His pain has since improved and he is able to bear more weight on his right ankle, however he is still limping. He denies experiencing any numbness to his right foot. In addition to ice and elevation he has been taking ibuprofen for his pain, which has provided some relief. He does not recall any other previous injury to his right ankle.

SOCIAL HISTORY

Patient reports that he is very active and enjoys playing socc …
```

**Generated note**

```
CHIEF COMPLAINT

Right ankle pain and swelling.

HISTORY OF PRESENT ILLNESS

The patient is a 35-year-old male who comes in complaining of right ankle pain and swelling.  He states that he was slipping on ice and fell onto his right ankle.  He denies any numbness in his right foot.  He has had some pain and swelling in his right ankle.  He has been taking ibuprofen and applying ice to the area.  He has had no previous injuries to his right ankle.  He is a soccer player and plays for the community league.  His children are involved in soccer as well.  He has had no numbness in his right foot.

REVIEW OF SYSTEMS

Significant for right ankle pain and swelling.  No numbness in the right foot.

PHYSICAL EXAM

VITAL SIGNS
Blood pressure: 130/80 mm Hg.
Pulse: 78 bpm.
Respiratory rate: 16 breaths per minute.
Temperature: 98.6°F.

NEUROLOGIC
Cranial Nerves II-XII are grossly intact.
Motor strength 5/5 in bilateral upper extremities and lower extremities.
Sensory examination shows decreased sensation to light touch in the right lower extremity.
Reflexes are 2+ bilaterally.

MUSCULOSKELETAL
Rig …
```

- unsupported entities (vs. transcript): blood pressure measurement, erythema, respiratory rate, warmth
- incorrect diagnosis: —  ·  missing diagnosis: —
- incorrect medication: —  ·  missing medication: —
- dosage mismatch: —
- negation flips (vs. reference): —
- unsupported numbers: 130, 130/80, 16, 35, 78, 80, 98.6
- missing information: {"symptom": ["limping"], "investigation": ["vital signs"]}

## Worst ROUGE-L: `aci_bench_test_taskC_2_D2N158-aci`

*lowest ROUGE-L in the split*

ROUGE-L 4.9 · length ratio 2.34 · truncated True · degenerate True · hallucination 0.0 · negation-flip 16.7 · numerical consistency 100.0 · coverage 27.3

**Transcript (excerpt)**

```
[doctor] yeah so sorry so barbara is a 31 -year-old female and she has history of diabetes type two and asthma and she is here today with abdominal pain so barbara tell me a little more about your abdominal pain what's been going on
[patient] so i've been having this pain for the past one week and as you know i have a longstanding history of diabetes and i guess i've been drinking too much coffee lately i do n't know if that triggered my gastritis so
[doctor] yeah
[patient] i think it's been but lately
[doctor] okay alright and so is it increasing in severity would you say or staying about the same or what
[patient] it's gradually increasing for sure
[doctor] okay alright and along with the  …
```

**Reference note**

```
CHIEF COMPLAINT

Abdominal pain.

MEDICAL HISTORY

Patient reports history of diabetes type 2, asthma, and gastritis.

SOCIAL HISTORY

Patient reports history of moderately heavy alcohol use. She also enjoys coffee.

MEDICATIONS

Patient reports taking metformin 500 mg twice daily, Flovent twice daily, and albuterol as-needed.

REVIEW OF SYSTEMS

Constitutional: Denies fever.
Gastrointestinal: Reports abdominal pain, nausea, and vomiting. Denies diarrhea.

PHYSICAL EXAM

Respiratory
- Auscultation of Lungs: Mild end expiratory wheezes, very faint.

Cardiovascular
- Auscultation of Heart: Grade 3/6 systolic ejection murmur, unchanged from prior exam.

Gastrointestinal
- Examination of Abdomen: Mild tenderness in the epigastrium. Abdomen is soft. No tenderness in the right lower quadrant. No significant tenderness in the right upper quadrant.

ASSESSMENT AND PLAN

1. Abdominal pain.
- Medi …
```

**Generated note**

```
CHIEF COMPLAINT

Abdominal Pain.

HISTORY OF PRESENT ILLNESS

The patient is a 31-year-old female who comes in today with complaints of abdominal pain.  She has a history of diabetes type II and asthma.  She states that her abdominal pain has been present for the past one week.  She denies any fevers.  She has had some nausea and vomiting.  She has had some diarrhea.  She has had some abdominal pain.  She has had some abdominal pain.  She has had some abdominal pain.  She has had some abdominal pain.  She has had some abdominal pain.  She has had some abdominal pain.  She has had some abdominal pain.  She has had some abdominal pain.  She has had some abdominal pain.  She has had some abdominal pain.  She has had some abdominal pain.  She has had some abdominal pain.  She has had some abdominal pain.  She has had some abdominal pain.  She has had some abdominal pain.  She has had some abdominal pain.  She has had some abdominal pain.  She has had some abdominal pain.  She has had some abdominal pain.  She has had some abdominal pain.  She has had some abdominal pain.  She has had som …
```

- unsupported entities (vs. transcript): —
- incorrect diagnosis: —  ·  missing diagnosis: gastritis, type 2 diabetes
- incorrect medication: —  ·  missing medication: albuterol, fluticasone, metformin, ranitidine
- dosage mismatch: —
- negation flips (vs. reference): diarrhea
- unsupported numbers: —
- missing information: {"symptom": ["murmur", "pain", "wheezing"], "medical_history": ["gastritis", "type 2 diabetes"], "medication": ["albuterol", "fluticasone", "metformin", "ranitidine"], "investigation": ["complete blood count", "continuous glucose monitor", "home monitoring", "metabolic panel", "physical examination", "pregnancy test"]}

## Hallucination example: `aci_bench_test_taskC_2_D2N163-aci`

*hallucination example*

ROUGE-L 5.8 · length ratio 2.19 · truncated True · degenerate False · hallucination 98.0 · negation-flip 0.0 · numerical consistency 100.0 · coverage 11.1

**Transcript (excerpt)**

```
[doctor] julie cruz is a 17 -year-old non- binary immensipated minor with no significant past medical history presents for evaluation of newly diagnosed hypercholesterolemia patient is here at the clinic hi julie how're you doing
[patient] i'm okay
[doctor] so i now i know you're worried about you know what's been happening with your with your you know with your blood cholesterol so can you tell me a little bit more about what's going on
[patient] yeah i mean i'm worried about this finding i went for my annual checkup and they checked my cholesterol one of those finger prick tests and it came back elevated and they told me i should come and see you
[doctor] okay alright well i think it's a g …
```

**Reference note**

```
CHIEF COMPLAINT

Hypercholesterolemia.

SOCIAL HISTORY

Patient denies any history of smoking; however, they note that their parents smoked when they lived with them. They enjoy being outside and riding their bike on trails.

FAMILY HISTORY

Patient reports a cousin who died of a heart attack in their 40's. but denies any family history of hypercholesterolemia.

VITALS

Blood pressure looks good.

PHYSICAL EXAM

Eyes
- Examination: No xanthomas noted.

Neck
- General Examination: Neck is supple without thyromegaly.

Respiratory
- Auscultation of Lungs: Clear bilaterally.

Cardiovascular
- Auscultation of Heart: No murmurs, gallops or rubs.

Gastrointestinal
- Examination of Abdomen: No hepatomegaly or splenomegaly.

RESULTS

Recent cholesterol level is reviewed and shows patient is elevated at 210.

ASSESSMENT AND PLAN

1. Elevated cholesterol.
- Medical Reasoning: The patient's previous …
```

**Generated note**

```
CHIEF COMPLAINT

The patient is a 17-year-old female who comes in for evaluation of newly diagnosed hypercholesterolemia.

HISTORY OF PRESENT ILLNESS

This is a 17-year-old female who comes in for evaluation of newly diagnosed hypercholesterolemia.  She has no significant past medical history.  The patient states she is concerned about her recent diagnosis of hypercholesterolemia.  She denies any history of hypertension, diabetes mellitus, or dyslipidemia in her family.  She has a history of being overweight.  She denies smoking or alcohol use.  She has a history of asthma.  She has a history of allergies.  She has a history of eczema.  She has a history of sinusitis.  She has a history of bronchitis.  She has a history of pneumonia.  She has a history of tonsillitis.  She has a history of strep throat.  She has a history of mononucleosis.  She has a history of appendicitis.  She has a history of gastritis.  She has a history of gastroenteritis.  She has a history of constipation.  She has a history of diarrhea.  She has a history of irritable bowel syndrome.  She has a history of ur …
```

- unsupported entities (vs. transcript): abscess, allergic rhinitis, appendicitis, arrhythmia, asthma, atrial fibrillation, bradycardia, bronchitis, cancer, constipation, diabetes, diarrhea, dysmenorrhea, dysuria, eczema, edema, endometriosis, gastritis, gastroenteritis, hematuria
- incorrect diagnosis: —  ·  missing diagnosis: myocardial infarction
- incorrect medication: —  ·  missing medication: —
- dosage mismatch: —
- negation flips (vs. reference): —
- unsupported numbers: —
- missing information: {"symptom": ["murmur"], "medical_history": ["myocardial infarction"], "investigation": ["blood pressure measurement", "genetic testing", "hemoglobin a1c", "lipid panel", "metabolic panel", "physical examination"]}

## Incorrect diagnosis example: `aci_bench_test_taskC_2_D2N143-virtscribe`

*incorrect diagnosis example*

ROUGE-L 7.8 · length ratio 1.33 · truncated True · degenerate True · hallucination 95.6 · negation-flip 25.0 · numerical consistency 0.0 · coverage 44.4

**Transcript (excerpt)**

```
[doctor] next patient is grace ross . date of birth 8-23-97 . ms. ross is a new patient . she's here today for a full spectrum std testing . the patient states that she's having symptoms of discomfort , a change in discharge , and odor in her vaginal region . she says that the right side of her vagina is starting to become painful . she denies any fevers or chills . she reports , that she recently learned , her partner has been in sexual encounters with other people , and she wants to be evaluated for all stds .
[doctor] hello , ms. ross . i'm dr. diaz . it's good to meet you .
[patient] hi . yes . nice to meet you , too .
[doctor] so , how are you doing today ? i hear that you're here for s …
```

**Reference note**

```
CHIEF COMPLAINT

Full-spectrum sexually transmitted disease testing.

HISTORY OF PRESENT ILLNESS

Ms. Ross is a 23-year-old female who presents today as a new patient for full-spectrum STD testing.

The patient states that she is having symptoms of discomfort, a change in discharge, and an odor in her vaginal region. She says that the right side of her vagina is starting to become painful but denies any fever or chills. She states that she recently learned her partner of 3 years has been engaging in sexual encounters with other people for quite some time, and she wants to be evaluated for all sexually transmitted diseases.

Ms. Ross reports noticing a change in the odor, color, and consistency of her vaginal discharge last week. She notes that this did not alarm her until the right side of her vagina became painful and sore, which has not subsided. She states that she had an abnormal Pap …
```

**Generated note**

```
CHIEF COMPLAINT

The patient is a 17-year-old female who comes in for STD screening.  She has been experiencing dyspareunia, changes in discharge, and odor in her vagina.  She denies fever, chills, abdominal pain, nausea, vomiting, diarrhea, constipation, hematuria, dysuria, frequency, urgency, nocturia, arthralgias, joint swelling, muscle weakness, fatigue, weight loss, night sweats, chest pain, palpitations, shortness of breath, wheezing, cough, sputum production, hemoptysis, headache, dizziness, syncope, visual disturbances, diplopia, photophobia, hearing loss, tinnitus, vertigo, tremors, rigidity, gait disturbance, urinary retention, urinary incontinence, fecal incontinence, rectal bleeding, pruritus ani, pruritus vulvae, itching, burning, redness, swelling, warmth, tenderness, nodules, cysts, ulcers, purulent drainage, lymphadenopathy, rash, urticaria, angioedema, edema, erythema, petechiae, ecchymosis, bruising, jaundice, icterus, scleral icterus, conjunctival xerosis, dry mouth, xerostomia, dysphagia, odynophagia, hoarseness, stridor, aphonia, dysarthria, dysphasia, confusion, …
```

- unsupported entities (vs. transcript): abdominal pain, anal fissure, angioedema, anxiety, appendicitis, blood in stool, bruising, burning sensation, cancer, chest pain, cholecystitis, cirrhosis, colon cancer, confusion, constipation, cough, depression, diarrhea, difficulty walking, diverticulitis
- incorrect diagnosis: anal fissure, angioedema, anxiety, appendicitis, cancer, cholecystitis, cirrhosis, colon cancer, depression, diverticulitis, esophagitis, gastritis, gastroenteritis, gerd, hemorrhoids, hernia, hypertension, inflammatory bowel disease, irritable bowel syndrome, pancreatic cancer, pancreatitis, peptic ulcer disease, pericarditis, pleural effusion, prostatitis, schizophrenia, sebaceous cyst, stomach cancer  ·  missing diagnosis: hepatitis
- incorrect medication: —  ·  missing medication: —
- dosage mismatch: —
- negation flips (vs. reference): pain
- unsupported numbers: 17
- missing information: {"symptom": ["vaginal discharge"], "diagnosis": ["hepatitis"], "investigation": ["pap smear", "physical examination", "std testing"]}

## Incorrect medication / dosage example: `aci_bench_test_taskC_2_D2N161-aci`

*incorrect medication / dosage example*

ROUGE-L 23.6 · length ratio 1.52 · truncated False · degenerate False · hallucination 13.6 · negation-flip 9.1 · numerical consistency 88.2 · coverage 85.0

**Transcript (excerpt)**

```
[doctor] patient is an 82 -year-old male with past medical history significant for hypertension and stage three chronic kidney disease who presents for hospital follow-up after an acute on chronic chf exacerbation alright hey hey kevin how are you doing today
[patient] hi document well i mean i thought i was doing good but then i've been trying to watch my diet like you said and i really noticed that my ankles were swelling and then one day i got really super short of breath and i even had to call nine one one now when the paramedics got there they put me on the special mask to breathe when i got to the er the doctor in the er said my blood pressure was super high
[doctor] yeah okay so yeah  …
```

**Reference note**

```
CHIEF COMPLAINT

Hospital follow-up after acute on chronic CHF exacerbation.

MEDICAL HISTORY

Patient reports history of hypertension and stage 3 chronic kidney disease.

SOCIAL HISTORY

Patient reports being a football fan.

MEDICATIONS

Patient reports taking Bumex 2 mg once daily, Cozaar 100 mg daily, and Norvasc 5 mg once daily.

REVIEW OF SYSTEMS

Cardiovascular: Denies chest pain.
Respiratory: Denies shortness of breath.
Musculoskeletal: Reports bilateral ankle swelling.
Neurological: Denies any sleep disturbance.

VITALS

BP: 128/72.
HR: 79 bpm.
RR: 26.
SpO2: 99%.

PHYSICAL EXAM

Neck
- General Examination: No jugular venous distension noted.

Respiratory
- Auscultation of Lungs: Clear bilaterally.

Cardiovascular
- Auscultation of Heart: Regular rate. There is a 2/6 systolic ejection murmur, stable.

Musculoskeletal
- Examination: There is trace edema to the bilateral lower extr …
```

**Generated note**

```
CHIEF COMPLAINT

An 82-year-old male with past medical history significant for hypertension and stage III chronic kidney disease who presents for hospital followup after an acute on chronic CHF exacerbation.

HISTORY OF PRESENT ILLNESS

The patient is an 82-year-old male who comes in for hospital followup after an acute on chronic CHF exacerbation.  He states he has been trying to watch his diet and has noticed his ankles have been swelling and he has been having shortness of breath.  He has been having difficulty breathing and had to call 911.  The paramedics placed him on oxygen via nasal cannula.  When he arrived at the ER, his BP was noted to be elevated at 200/90.  He has been admitted for CHF.  He denies any chest pain.  He has been taking his medications mostly but does miss a few doses occasionally.  He has been eating a lot of cheese, pizza, and chicken wings.  He has been going to parties on the weekend.  He has been watching his diet but has had some slips.  He feels good now.  He has been in the hospital for a couple of days.  They have given him Lasix IV and Bumex PO.  H …
```

- unsupported entities (vs. transcript): supplemental oxygen, weight gain, weight measurement
- incorrect diagnosis: —  ·  missing diagnosis: —
- incorrect medication: supplemental oxygen  ·  missing medication: —
- dosage mismatch: —
- negation flips (vs. reference): dyspnea
- unsupported numbers: 200/90, 911
- missing information: {"medical_history": ["mitral regurgitation"], "investigation": ["diagnostic workup", "home monitoring"]}

## Negation error example: `aci_bench_test_taskC_2_D2N153-aci`

*negation error example*

ROUGE-L 10.1 · length ratio 1.98 · truncated True · degenerate True · hallucination 42.9 · negation-flip 83.3 · numerical consistency 66.7 · coverage 33.3

**Transcript (excerpt)**

```
[patient] i hope i did n't hurt it again
[doctor] hi gregory how are you i the medical assistant told me that you injured your knee
[patient] yeah yeah i heard it stepping off a curb
[doctor] how long ago did that happen
[patient] about two and a half weeks ago
[doctor] two and a half weeks ago and what what knee is bothering you
[patient] the right knee the outside of my right knee
[doctor] the outside of your right knee
[patient] yeah
[doctor] okay and did you actually fall down when this happened or
[patient] no i just sorta turned over my ankle
[doctor] okay
[patient] to the outside and i thought my ankle was the thing that was gon na hurt most but after the ankle soreness went away the  …
```

**Reference note**

```
HISTORY OF PRESENT ILLNESS

Gregory Price is a pleasant 68-year-old male who presents to the clinic today for the evaluation of a right knee injury. The onset of his pain began 2.5 weeks ago, when he stepped off of a curb and turned over his ankle. He locates his pain to the lateral aspect of his right knee. The patient also reports clicking with ambulation. He denies any pain with ambulation unless he stands on one foot for an extended period of time. The patient also reports locking of his knee with prolonged standing. He notices pain when he is resting his foot on his heel. He denies any pain at rest and elevated, or when his foot is flat on the ground. The patient states that he is more active during the day, which does not impact his knee pain. He adds that he is able to perform a full squat without pain. The patient reports numbness and tingling in his right foot, however this is n …
```

**Generated note**

```
CHIEF COMPLAINT

The patient is here for evaluation of his right knee pain.

HISTORY OF PRESENT ILLNESS

The patient is a 45-year-old male who comes in for evaluation of his right knee pain.  He states he has had pain in his right knee for approximately 2.5 weeks.  The patient states he has had no trauma to the knee.  He denies any locking or catching.  He states he has had some stiffness in the morning.  He denies any numbness or tingling in the lower extremities.  He has had some pain in his right knee when he stands on one leg.  He has had some pain when he bends his knee.  He has had some pain when he extends his knee.  He has had some pain when he flexes his knee.  He has had some pain when he rotates his knee.  He has had some pain when he twists his knee.  He has had some pain when he pivots his knee.  He has had some pain when he steps up onto stairs.  He has had some pain when he steps down from stairs.  He has had some pain when he walks.  He has had some pain when he runs.  He has had some pain when he jumps.  He has had some pain when he climbs stairs.  He has had some pa …
```

- unsupported entities (vs. transcript): joint instability, knee pain, stiffness
- incorrect diagnosis: —  ·  missing diagnosis: strain
- incorrect medication: —  ·  missing medication: ibuprofen, meloxicam
- dosage mismatch: —
- negation flips (vs. reference): joint instability, knee pain, numbness, tingling, trauma
- unsupported numbers: 45
- missing information: {"symptom": ["crepitus", "edema", "joint swelling"], "medical_history": ["fracture"], "diagnosis": ["dislocation", "strain"], "medication": ["ibuprofen", "meloxicam"], "investigation": ["heart rate measurement", "mri", "physical examination", "x-ray"]}

## Numerical error example: `aci_bench_test_taskC_2_D2N128-virtassist`

*numerical error example*

ROUGE-L 29.7 · length ratio 1.31 · truncated False · degenerate False · hallucination 44.0 · negation-flip 18.2 · numerical consistency 26.1 · coverage 72.2

**Transcript (excerpt)**

```
[doctor] hi , carolyn . how are you ?
[patient] good . how are you ?
[doctor] i'm good . you're ready to get started ?
[patient] yes , i am .
[doctor] so carolyn is a 49-year-old female here for follow-up of her chronic problems . so , how are you doing , carolyn ?
[patient] i'm doing okay . um , my osteoarthritis has been flaring up a little bit lately , um , so i wan na get- talk about that primarily . so , it's mostly in um , my elbows and it's really been bothering me . i've been sitting at the computer , at the desk more , um , in the office so i do n't know if it's being stagnant in that position all day has um , increased flare-ups for that , but i wanted to talk to you about that .
[ …
```

**Reference note**

```
CHIEF COMPLAINT

Follow-up of chronic problem.

HISTORY OF PRESENT ILLNESS

Ms. Carolyn Garcia is a 49-year-old female who presents to the clinic today for follow-up of her chronic problem.

The patient reports her osteoarthritis has been flaring up a little lately, and she would like to talk about that, primarily in her elbows. She states she has been sitting at the computer more in the office, so she is unsure if it is stagnant in that position all day. She notes her right elbow bothers her more than her left elbow, but she is primarily typing all day versus writing. She denies any other joint pain. She notes occasional numbness and tingling in her hands, which she tries to shake out her arms to relieve the numbness.

She also has a history of gout. Her last episode was about 3 months ago. She had some inflammation of her toe at that time. She denies any other issues with that. She sta …
```

**Generated note**

```
CHIEF COMPLAINT

The patient is a 49-year-old female who comes in for followup of her chronic problems.  She states that she has had some exacerbation of her osteoarthritis, particularly in her elbows, which has been bothering her.  She denies any other joint pains.  She has had some numbness and tingling in her hands while typing.  She has had some history of gout, which has been controlled by medications.  She has not had any recent episodes of gout.  She has had some history of psoriasis, which has been under control.  She has had some treatment for her scalp psoriasis with clobetasol, which has been effective.

HISTORY OF PRESENT ILLNESS

The patient is a 49-year-old female who comes in for followup of her chronic problems.  She states that she has had some exacerbation of her osteoarthritis, particularly in her elbows, which has been bothering her.  She denies any other joint pains.  She has had some numbness and tingling in her hands while typing.  She has had some history of gout, which has been controlled by medications.  She has not had any recent episodes of gout.  She has  …
```

- unsupported entities (vs. transcript): adverse drug reaction, blood pressure measurement, bursitis, crepitus, crp, esr, heart rate measurement, murmur, numbness, reduced range of motion, respiratory rate
- incorrect diagnosis: adverse drug reaction, bursitis  ·  missing diagnosis: —
- incorrect medication: —  ·  missing medication: hydrocortisone cream
- dosage mismatch: —
- negation flips (vs. reference): edema, joint pain
- unsupported numbers: 1.5, 10, 130, 130/80, 16, 20, 24, 3.5, 4, 5, 6, 7, 7.2, 7.8, 78
- missing information: {"symptom": ["crackles", "flare", "rhonchi", "wheezing"], "medication": ["hydrocortisone cream"]}

## Missing information example: `aci_bench_test_taskC_2_D2N156-aci`

*missing information example*

ROUGE-L 7.9 · length ratio 1.61 · truncated True · degenerate True · hallucination 33.3 · negation-flip 0.0 · numerical consistency 50.0 · coverage 11.1

**Transcript (excerpt)**

```
[doctor] alright julia so you've been coming to see me for a while now ever since you had an rca stent placed back in twenty eighteen but i see you're here for follow-up after an interior stemi where we had to put in another stent right so like how are you doing
[patient] well i mean it was a real shock for me i thought everything was fine after my last heart attack and then i just started having this horrible chest pain and it would n't go away so i went to the emergency room and yeah they told me i needed another stent
[doctor] wow so you were experiencing similar symptoms similar to what you had the first time
[patient] yeah yeah it was yeah it was bad it was just like the last time
[doct …
```

**Reference note**

```
CHIEF COMPLAINT

Follow up status post inferior STEMI.

SURGICAL HISTORY

RCA stent 2018

MEDICATIONS

aspirin 81 mg daily
Brilinta 90 mg twice daily
Lipitor 80 mg daily
Toprol 50 mg daily
lisinopril 20 mg daily
metformin

REVIEW OF SYSTEMS

Cardiovascular: Denies chest pain.
Respiratory: Denies shortness of breath.
Musculoskeletal: Reports bilateral leg swelling.

VITALS

Within normal limits

PHYSICAL EXAM

Neck
- General Examination: No jugular venous distention.

Respiratory
- Auscultation of Lungs: Clear bilaterally.

Cardiovascular
- Auscultation of Heart: No carotid bruits. A 3/6 systolic ejection murmur is heard at the left base.
- Examination: Right radial artery cath site is clean, dry, and intact without hematoma. Radial artery pulses are palpable.

Musculoskeletal
- Examination: Bilateral lower limb edema. Pitting 1+.

RESULTS

EKG is reviewed and demonstrates a normal sinus  …
```

**Generated note**

```
CHIEF COMPLAINT

The patient is a 62-year-old female who comes in for a routine followup visit.  She has a history of coronary artery disease, hypertension, and diabetes mellitus type II.  She has had a recent interior STEMI and has had a stent placement.  She has had a history of RCA stent placement in 2018.  She has had a history of hypertension, diabetes mellitus type II, and coronary artery disease.  She has had a history of dyslipidemia.  She has had a history of smoking.  She has had a history of obesity.  She has had a history of hypertension.  She has had a history of diabetes mellitus type II.  She has had a history of coronary artery disease.  She has had a history of dyslipidemia.  She has had a history of smoking.  She has had a history of obesity.  She has had a history of hypertension.  She has had a history of diabetes mellitus type II.  She has had a history of coronary artery disease.  She has had a history of dyslipidemia.  She has had a history of smoking.  She has had a history of obesity.  She has had a history of hypertension.  She has had a history of diabetes  …
```

- unsupported entities (vs. transcript): hyperlipidemia, obesity
- incorrect diagnosis: —  ·  missing diagnosis: heart failure, mitral regurgitation, type 2 diabetes
- incorrect medication: —  ·  missing medication: aspirin, atorvastatin, furosemide, lisinopril, metformin, metoprolol, spironolactone, ticagrelor
- dosage mismatch: —
- negation flips (vs. reference): —
- unsupported numbers: 62
- missing information: {"symptom": ["chest pain", "dyspnea", "edema", "murmur"], "diagnosis": ["heart failure", "intracranial hemorrhage", "mitral regurgitation", "type 2 diabetes"], "medication": ["aspirin", "atorvastatin", "furosemide", "lisinopril", "metformin", "metoprolol"], "investigation": ["blood glucose", "blood pressure measurement", "blood work", "echocardiogram", "electrocardiogram", "heart rate measurement"]}

## Degenerate output example: `aci_bench_test_taskC_2_D2N137-virtassist`

*degenerate output example*

ROUGE-L 12.3 · length ratio 1.35 · truncated True · degenerate True · hallucination 90.9 · negation-flip 40.0 · numerical consistency 100.0 · coverage 33.3

**Transcript (excerpt)**

```
[doctor] morning christine , nice to see you .
[patient] nice to see you too .
[doctor] so i know my nurse told you a little bit of- ... um , about dax and i'm gon na tell dax a little bit about you , if that's okay ?
[patient] go for it .
[doctor] okay , great . um , uh , this is christine . she's a 63-year-old female patient . you're here for your routine , um , yearly exam . um , i know you have a history of high blood pressure and you've had some depression in the past . and i also know you did have a carpal tunnel release done about two years ago . um , how have you been doing ?
[patient] i've been doing well . um , the depression standpoint is doing great . i've been using , um , the m …
```

**Reference note**

```
CHIEF COMPLAINT

Annual exam.

HISTORY OF PRESENT ILLNESS

Christine Flores is a 63-year-old female presenting for her yearly exam. She has a history of high blood pressure and depression in the past. She also had a right carpal tunnel release done about 2 years ago.

The patient states that she has been doing well with her depression. She notes that she has been taking her medication as prescribed at her last visit. She states that she has been going to therapy every week, which has helped her manage her symptoms. The patient notes that she is sleeping well at night and has been getting a full 8 hours. She denies any thoughts of self-harm or harming others.

The patient states that she has been checking her blood pressure at home. She notes that her blood pressure has fluctuated lately. She states that she has not had a normal reading in a couple of weeks. The patient has continued util …
```

**Generated note**

```
CHIEF COMPLAINT

This is a 63-year-old female who comes in for her annual examination.  She has a history of hypertension and depression.  She has had a carpal tunnel release approximately two years ago.

HISTORY OF PRESENT ILLNESS

The patient is a 63-year-old female who comes in for her annual examination.  She has a history of hypertension and depression.  She has had a carpal tunnel release approximately two years ago.  The patient states that she has been doing well.  She has been taking her depression medication and attending weekly therapy sessions.  She denies any suicidal ideation.  She has been having difficulty sleeping at night.  She has been having some headaches.  She denies any dysarthria, diplopia, dysphagia, dysuria, hematuria, hemoptysis, palpitations, orthopnea, PND, syncope, chest pain, abdominal pain, arthralgias, joint effusions, edema, weight loss, fever, chills, fatigue, weakness, muscle spasms, muscle cramps, tremors, tinnitus, hearing loss, visual disturbances, photophobia, phonophobia, vertigo, syncope, palpitations, orthopnea, PND, shortness of breath, whe …
```

- unsupported entities (vs. transcript): abdominal pain, abdominal tenderness, bloating, blood in stool, bruising, chest pain, chills, constipation, cough, cramping, diarrhea, dizziness, double vision, dysphagia, dyspnea, dysuria, fatigue, fever, hearing loss, hematuria
- incorrect diagnosis: —  ·  missing diagnosis: —
- incorrect medication: —  ·  missing medication: lisinopril
- dosage mismatch: —
- negation flips (vs. reference): lymphadenopathy, wheezing
- unsupported numbers: —
- missing information: {"symptom": ["crackles", "murmur", "numbness", "rhonchi", "tingling"], "medication": ["lisinopril"], "investigation": ["blood pressure measurement", "blood work", "physical examination", "vital signs"]}

# Split: aci_bench_test_taskC_3

## Best ROUGE-L: `aci_bench_test_taskC_3_D2N203-aci`

*highest ROUGE-L in the split*

ROUGE-L 40.5 · length ratio 0.76 · truncated False · degenerate False · hallucination 40.0 · negation-flip 0.0 · numerical consistency 36.8 · coverage 55.6

**Transcript (excerpt)**

```
[doctor] good afternoon matthew how are you
[patient] i'm okay
[doctor] it looks like here that the that you've been brought in for some vision changes and looks like you're having trouble with your right eye can you tell me a little bit about what brought you in to see me today
[patient] yeah you know i started noticing my wife and i we we eat out almost every night and it's when especially when we go to fancy place
[doctor] mm-hmm
[patient] i have trouble adjusting in the that dark dim environment
[doctor] okay and i reviewed my technician's notes before i came in to see you and it says you know you you've been having that decreased vision when you're reading especially in dark place like  …
```

**Reference note**

```
CHIEF COMPLAINT

Vision changes in the right eye.

MEDICAL HISTORY

Patient reports history of high blood pressure.

SOCIAL HISTORY

Patient reports he is smoking 1 pack of cigarettes daily.

REVIEW OF SYSTEMS

Eyes: Reports right eye vision changes.

PHYSICAL EXAM

Eyes
- Examination of the right eye: Posterior chamber intraocular lenses present bilaterally. Right eye cornea is clear without NVI and cup-disc ratio is 0.2. Fundus of right eye shows retina is intact 360 degrees without holes or tears noted, and RPE changes in fovea. Posterior segment shows drusen of the macula, retinal thickening, and presence of subretinal fluid and exudate accumulation. Positive hemorrhage
Examination of the left eye: Cornea is clear. No NVI. Cup-disc ration is 0.3. RPE changes in fovea. No hemorrhage noted or subretinal fluid noted. Retina is attached appropriately.

RESULTS

OTC:
Drusen deposits under …
```

**Generated note**

```
CHIEF COMPLAINT

The patient is a 62-year-old male who comes in for evaluation of his right eye vision changes.

HISTORY OF PRESENT ILLNESS

The patient states he has had difficulty adjusting to darkness and has had blurred vision in his right eye for the past 3-4 months.  He denies any recent trauma to the eye.  The patient has a history of hypertension and is a smoker.  He has not been compliant with his medications.

REVIEW OF SYSTEMS

Significant for hypertension and smoking.

PHYSICAL EXAM

VITAL SIGNS
Blood Pressure: 140/90
Pulse: 80
Respiratory Rate: 16
Temperature: 98.6

HEENT
Right Eye Examination: Visual Acuity: 20/40 OD
Left Eye Examination: Visual Acuity: 20/30 OS
Anterior Segment Examination: Posterior Chamber Intraocular Lens in both eyes.  Right Eye Cornea is clear, No NVI, Peak Hole Cup to Disc Ratio is 0.2.  Fundus Examination of the right eye shows the retina to be attached 360 degrees, no holes or tears noted, RPE changes in the fovea.  Posterior Segment Exam shows Drusen in the Macula, Retinal Thickening, Presence of Subretinal Fluid and Exudate Accumulation, Posi …
```

- unsupported entities (vs. transcript): heart rate measurement, respiratory rate, tobacco use, trauma
- incorrect diagnosis: —  ·  missing diagnosis: —
- incorrect medication: —  ·  missing medication: —
- dosage mismatch: —
- negation flips (vs. reference): —
- unsupported numbers: 140, 140/90, 16, 20, 20/30, 20/40, 30, 40, 62, 80, 90, 98.6
- missing information: {"symptom": ["numbness", "pain", "vision loss"], "investigation": ["diagnostic workup"]}

## Worst ROUGE-L: `aci_bench_test_taskC_3_D2N187-aci`

*lowest ROUGE-L in the split*

ROUGE-L 4.4 · length ratio 3.47 · truncated True · degenerate True · hallucination 85.7 · negation-flip 0.0 · numerical consistency 0.0 · coverage 40.0

**Transcript (excerpt)**

```
[doctor] well good morning emily how are you
[patient] good morning
[doctor] how are you doing
[patient] doing okay i'm okay
[doctor] i understand you're having some sudden visual distortions and some blurring of your vision is that right
[patient] it is yes
[doctor] okay so what's going on
[patient] sorry to put you off i do n't think i have that script
[doctor] oh
[patient] maybe a different one i wonder if patient has history of
[doctor] macular degeneration yeah yeah i was because we do n't we do n't to do the intro anymore i was just going with that you you're coming in with sudden visual distortion and blurring of vision so i'll just you know i'll just say i'll just go ahead and go int …
```

**Reference note**

```
CHIEF COMPLAINT

Changes in vision.

SOCIAL HISTORY

Patient smokes approximately 1 pack of cigarettes per day.

REVIEW OF SYSTEMS

Eyes: Reports visual distortions and blurred vision.

PHYSICAL EXAM

Eyes
- Examination: Anterior segment examination reveals posterior chamber intraocular lenses in both eyes.
Right eye: The cornea is clear. No MVI. PCIOL cup to disc is 0.2. Fundus examination of the right eye shows the retina to be attached 360 degrees without any tears or holes. RPE changes in the fovea. Posterior segment exam shows drusen in the macula, thickening of the retina, presence of subretinal fluid and exudates accumulation. Positive for hemorrhage.
Left eye: The cornea is clear. No MVI. Cup to disc is 0.3. RPE changes in the fovea. No hemorrhage or subretinal fluid. Retina is attached.

RESULTS

Optical coherence tomography shows drusen deposit. Retinal pigment epithelium with  …
```

**Generated note**

```
CHIEF COMPLAINT

The patient comes in today complaining of sudden onset blurred vision and distorted vision.

HISTORY OF PRESENT ILLNESS

Emily is a 62-year-old female who presents to the office today with complaints of sudden onset blurred vision and distorted vision.  She denies any recent trauma, infection, or surgery.  She does have a history of hypertension, hyperlipidemia, and macular degeneration.  She is a smoker and has had difficulty quitting.  She has been taking her medications as prescribed by her primary care physician.  She has been having some difficulty adjusting to low light environments at night.  She has been having some difficulty seeing straight lines and door frames.  She has been having some difficulty reading.  She has been having some difficulty driving at night.  She has been having some difficulty seeing in the dark.  She has been having some difficulty seeing colors.  She has been having some difficulty seeing details.  She has been having some difficulty seeing objects in front of her.  She has been having some difficulty seeing objects behind her.  She  …
```

- unsupported entities (vs. transcript): blurred vision, hyperlipidemia, hypertension, infection, tobacco use, trauma
- incorrect diagnosis: —  ·  missing diagnosis: —
- incorrect medication: —  ·  missing medication: —
- dosage mismatch: —
- negation flips (vs. reference): —
- unsupported numbers: 62
- missing information: {"symptom": ["bleeding"], "investigation": ["diagnostic workup", "eye exam"]}

## Hallucination example: `aci_bench_test_taskC_3_D2N200-aci`

*hallucination example*

ROUGE-L 4.9 · length ratio 2.08 · truncated True · degenerate False · hallucination 88.1 · negation-flip 20.0 · numerical consistency 50.0 · coverage 35.7

**Transcript (excerpt)**

```
[doctor] alright okay theresa so i understand that you're you're having a bit of some headache here and then your blood pressure has been running high can you tell me a little bit about what's happening
[patient] yeah i've had blood high blood pressure for a long time my provider gave me chlorthalidone i do n't really take it because it gives me a stomachache but yeah i get headaches right here on the top of my head they kinda come and go they're throbbing tylenol helps the headache
[doctor] okay alright and then so how long have you had this headache has this been recent or like acute or you've been having this for since you've had your blood pressures
[patient] hmmm it's been on and off fo …
```

**Reference note**

```
CHIEF COMPLAINT

Headache and high blood pressure.

REVIEW OF SYSTEMS

Respiratory: Denies shortness of breath.
Cardiovascular: Denies chest pain.
Neurological: Reports blurry vision, dizziness, and headaches.

VITALS

Blood pressure today was 172/98. Oxygenation is within normal limits.

PHYSICAL EXAM

Neck
- General Examination: No jugular venous distention. No carotid bruits.

Respiratory
- Auscultation of Lungs: Clear bilaterally.

Cardiovascular
- Auscultation of Heart: Regular rate. Slight 2/6 systolic ejection murmur, unchanged from last year.

Musculoskeletal
- Examination: Slight edema to bilateral upper extremities. 1+ pitting edema noted in the bilateral lower extremities.

ASSESSMENT AND PLAN

1. Hypertension, uncontrolled.
- Medical Reasoning: The patient's blood pressure is is elevated.
- Patient Education and Counseling: We discussed that this could be multifactorial; for  …
```

**Generated note**

```
CHIEF COMPLAINT

The patient is a 62-year-old female who comes in for evaluation of her hypertension and diabetes mellitus type II.

HISTORY OF PRESENT ILLNESS

The patient states she has had hypertension for many years and has been on Chlorthalidone.  She denies compliance with her medications due to side effects.  She has had headaches for approximately one month.  The headaches are described as throbbing and located on the top of her head.  She denies photophobia, phonophobia, or scintillating scotoma.  She denies visual loss.  She denies syncope, vertigo, or tinnitus.  She denies dysarthria, diplopia, or dysphagia.  She denies orthopnea, paroxysmal nocturnal dyspnea, or PND.  She denies chest pain or palpitations.  She denies hemoptysis or hematemesis.  She denies abdominal pain or melena.  She denies fever or chills.  She denies weight loss or gain.  She denies arthralgias or myalgias.  She denies weakness or fatigue.  She denies numbness or tingling.  She denies tremors or gait disturbances.  She denies urinary frequency or urgency.  She denies dysuria or nocturia.  She denies  …
```

- unsupported entities (vs. transcript): adverse drug reaction, anxiety, blood in stool, bruising, chills, confusion, constipation, cough, cramping, depression, diarrhea, difficulty walking, double vision, dry mouth, dysphagia, dysuria, fatigue, fever, hallucinations, hearing loss
- incorrect diagnosis: adverse drug reaction  ·  missing diagnosis: type 2 diabetes
- incorrect medication: —  ·  missing medication: metformin
- dosage mismatch: —
- negation flips (vs. reference): dizziness
- unsupported numbers: 62
- missing information: {"symptom": ["blurred vision", "dyspnea", "edema", "murmur"], "diagnosis": ["type 2 diabetes"], "medication": ["metformin"], "investigation": ["blood glucose", "blood pressure measurement", "physical examination"]}

## Incorrect diagnosis example: `aci_bench_test_taskC_3_D2N174-virtassist`

*incorrect diagnosis example*

ROUGE-L 26.3 · length ratio 0.96 · truncated False · degenerate True · hallucination 50.8 · negation-flip 4.5 · numerical consistency 33.3 · coverage 84.8

**Transcript (excerpt)**

```
[doctor] hi , james , how are you ?
[patient] hi , good to see you .
[doctor] it's good to see you too . so i know the nurse told you about dax , i'd like to tell dax a little bit about you .
[patient] sure .
[doctor] james is a 57 year old male with a past medical history significant for coronary artery disease and lupus , who presents today with joint pain . so james , what's what's going on ?
[patient] yeah . i've been putting a , a few more miles on the bike each day and , uh , my knees have been killing me , just more so in the last three or four days or so .
[doctor] okay . is it one knee versus the other , or both ?
[patient] both equally .
[doctor] okay . and , um , does it hurt more …
```

**Reference note**

```
CHIEF COMPLAINT

Joint pain.

HISTORY OF PRESENT ILLNESS

Mr. James Moore is a 57-year-old male with a past medical history significant for coronary artery disease and lupus, who presents today with some joint pain.

The patient reports he has been " putting a few more miles on the bike each day ". His bilateral knees have been sore in the last 3 to 4 days. He states his bilateral knees are equally painful. He notes stiffness and soreness in the morning and, by the end of the day, he feels the same sensation. He endorses swelling and redness in his knees which reduces in severity by the afternoon. The patient denies any other associated fatigue. He denies any injury to his knees. He denies pain in any other joints including his elbows, wrists, or shoulders.

In regards to his coronary artery disease, Mr. Moore states he is compliant with his aspirin and Crestor. He denies chest pain or s …
```

**Generated note**

```
CHIEF COMPLAINT

The patient is a 57-year-old male who comes in today complaining of bilateral knee pain.

HISTORY OF PRESENT ILLNESS

This is a 57-year-old male with a past medical history significant for coronary artery disease and lupus, who presents today with joint pain.  The patient states he has been increasing his biking activity over the past several weeks and has had bilateral knee pain for the past 3-4 days.  He denies any trauma to the knees.  He denies any fevers, chills, night sweats, weight loss, abdominal pain, nausea, vomiting, diarrhea, dysuria, frequency, urgency, hematuria, arthralgias, myalgias, weakness, fatigue, chest pain, SOB, orthopnea, PND, CVA, TIA, HTN, DM, allergies, or any other significant past medical history.  He takes Plavix, Aspirin, Crestor, and Synthroid daily.  He denies any tobacco use, alcohol use, or illicit drug use.

REVIEW OF SYSTEMS

Significant for joint pain, negative for febrile illness, negative for respiratory complaints, negative for gastrointestinal complaints, negative for genitourinary complaints, negative for neurological compla …
```

- unsupported entities (vs. transcript): allergic rhinitis, arrhythmia, arthritis, bloating, chills, diarrhea, dizziness, dysphagia, dysuria, electrocardiogram, gout, hearing loss, hematuria, hoarseness, hypertension, levothyroxine, muscle pain, night sweats, orthopnea, osteoarthritis
- incorrect diagnosis: arthritis, gout, osteoarthritis, rheumatoid arthritis  ·  missing diagnosis: —
- incorrect medication: levothyroxine  ·  missing medication: —
- dosage mismatch: —
- negation flips (vs. reference): murmur
- unsupported numbers: 130, 130/80, 18, 5, 78, 80, 96, 98.6
- missing information: {"symptom": ["crackles", "rhonchi", "stiffness", "wheezing"], "investigation": ["diagnostic workup"]}

## Incorrect medication / dosage example: `aci_bench_test_taskC_3_D2N170-virtassist`

*incorrect medication / dosage example*

ROUGE-L 17.3 · length ratio 1.42 · truncated True · degenerate True · hallucination 60.0 · negation-flip 20.0 · numerical consistency 100.0 · coverage 30.3

**Transcript (excerpt)**

```
[doctor] hi joyce , how are you ?
[patient] i'm good . how are you ?
[doctor] i'm doing well . so , i know the nurse told you about dax . i'd like to tell dax a little bit about you when we get started , okay ?
[patient] okay .
[doctor] all right . so , joyce is a 50 year old female with a past medical history significant for copd , congestive heart failure who presents for follow-up to an abnormal lab finding . so , joyce , i , i got the results of your lab , uh , your labs . your hemoglobin was low . uh , so , i asked them to schedule a follow-up appointment with me . so , how are you feeling ?
[patient] i've been feeling really tired lately . over the past couple of months , i've noticed  …
```

**Reference note**

```
CHIEF COMPLAINT

Follow-up to an abnormal labs.

HISTORY OF PRESENT ILLNESS

Joyce Price is a 50-year-old female with a past medical history significant for COPD, congestive heart failure who presents for follow-up to an abnormal lab finding.

The patient reports that she has been feeling really tired lately. She reports that over the past couple of months, her energy has really gone down. She used to be really active, trying to be as healthy as she can be with running and climbing, at least an hour or two a day. Over the past month, her activity has slowly decreased. She reports that, due to her fatigue, she has not been able to keep up with her exercise. She reports that she had noticed a little weight loss, but she believes that was due to her doing really well with her exercises.

The patient reports that her COPD is doing well. She reports that she has not been smoking since she qui …
```

**Generated note**

```
CHIEF COMPLAINT

Joyce is a 50-year-old female with a past medical history significant for COPD, congestive heart failure who presents for follow-up to an abnormal lab finding.

HISTORY OF PRESENT ILLNESS

The patient states she has been feeling very tired lately. She has had decreased energy over the past couple of months. She denies any melena, hematochezia, dysuria, frequency, urgency, nocturia, orthostatic hypotension, syncope, chest pain, SOB, fevers, chills, arthralgias, myalgias, weight loss, night sweats, or pedal edema. The patient denies any recent travel history. She has been compliant with her medications and dietary restrictions. She has been exercising regularly. She has been having difficulty keeping up with her usual activities due to fatigue. She has been having some seasonal allergy symptoms. She has been compliant with her COPD management. She has been compliant with her CHF management. She has been compliant with her medication regimen. She has been compliant with her diet. She has been compliant with her fluid restriction. She has been compliant with her sodium r …
```

- unsupported entities (vs. transcript): blood in stool, calcium supplement, dysuria, folic acid, iron supplement, joint pain, multivitamin, night sweats, nocturia, orthostatic hypotension, potassium level, syncope, urinary urgency, vitamin b12, vitamin d
- incorrect diagnosis: —  ·  missing diagnosis: anemia, gi bleed
- incorrect medication: calcium supplement, folic acid, iron supplement, multivitamin, vitamin b12, vitamin d  ·  missing medication: furosemide, lisinopril, metoprolol
- dosage mismatch: —
- negation flips (vs. reference): dyspnea, weight loss
- unsupported numbers: —
- missing information: {"symptom": ["bleeding", "crackles", "dizziness", "lymphadenopathy", "murmur", "pain"], "medical_history": ["tobacco use"], "diagnosis": ["allergic rhinitis", "anemia", "gi bleed"], "medication": ["furosemide", "lisinopril", "metoprolol"], "investigation": ["blood work", "colonoscopy", "diagnostic workup", "endoscopy", "hemoglobin a1c", "hemoglobin level"]}

## Negation error example: `aci_bench_test_taskC_3_D2N178-virtscribe`

*negation error example*

ROUGE-L 12.1 · length ratio 0.90 · truncated True · degenerate True · hallucination 71.8 · negation-flip 21.1 · numerical consistency 57.1 · coverage 57.6

**Transcript (excerpt)**

```
[doctor] okay . maria martin , date of birth 03/05/1946 , has been informed and consents to have this visit recorded . the patient is here for follow-up .
[doctor] hi , maria . how have you been doing ?
[patient] same i guess . pretty good .
[doctor] okay , so you got my letter last time on the results . your sugars are not very well controlled .
[patient] yeah , i got them .
[doctor] okay . so did you increase your glimepiride ?
[patient] did i increase it ?
[doctor] yeah .
[patient] i'm still taking the two milligrams .
[doctor] yeah . so we want you to , as the letter said , from the last time , when your a1c was 9.9 , we wanted you to increase it to four milligrams twice a day , so let's …
```

**Reference note**

```
CHIEF COMPLAINT

Follow-up for diabetes management, hypertension, hyperlipidemia, peripheral vascular disease.

HISTORY OF PRESENT ILLNESS

Maria Martin is a 75-year-old female who presents today for follow-up for diabetes.

The patient’s blood glucose levels are poorly controlled and her most recent hemoglobin A1C is 9.9%. She denies increasing glimepiride to 4 mg twice a day as advised but confirms she is compliant with 2 mg twice a day. She mostly denies reducing sugar and carbohydrate intake, although she opts for wheat bread, she does not have pasta at home, and she does not drink much soda and instead drinks club soda or seltzer water. She reports that her diabetic eye exams are up to date and she follows with Dr. Sanchez at Optimum Optometrists. She recently underwent cataract surgery and received a new prescription for her glasses, noting improvement in her vision to one eye and  …
```

**Generated note**

```
CHIEF COMPLAINT

Followup.

HISTORY OF PRESENT ILLNESS

The patient is a 62-year-old female who presents for followup.  She states that she has been following her diabetes regimen as directed.  She has been taking her prescribed medications including her glimepiride 2 mg twice daily.  She has been eating healthy and has been limiting her carbohydrate intake.  She denies any history of tobacco use.  She has been drinking club soda and seltzer water.  She has had recent eye examination and has had cataract surgery.  She has had hypertension and has been on metoprolol 50 mg once daily, lisinopril 20 mg with HCTZ 12.5 mg once daily, and amlodipine 10 mg once daily.  She has had peripheral artery disease and has been on atorvastatin 80 mg once daily.  She has had chronic lower extremity pain and has been diagnosed with peripheral neuropathy.  She has had chronic cough and has been evaluated for possible pneumonia.  She has had dysuria and frequency.  She has had no history of allergies.  She has had no history of previous surgeries.  She has had no history of hospitalizations.  She has ha …
```

- unsupported entities (vs. transcript): abdominal pain, allergic rhinitis, bloating, blood in stool, blurred vision, constipation, crackles, cramping, crepitus, diabetes, diarrhea, difficulty walking, double vision, dysmenorrhea, dysphagia, dysuria, erectile dysfunction, erythema, fatigue, hair loss
- incorrect diagnosis: —  ·  missing diagnosis: hyperlipidemia, hypoglycemia, type 2 diabetes
- incorrect medication: —  ·  missing medication: metformin
- dosage mismatch: [{"drug": "hydrochlorothiazide", "predicted": "12.5 mg", "source": ["25 mg", "25 milligrams"]}]
- negation flips (vs. reference): edema, nocturia, tobacco use, wheezing
- unsupported numbers: 12.5, 62, 80
- missing information: {"symptom": ["foot pain", "murmur", "nasal congestion"], "medical_history": ["type 2 diabetes"], "diagnosis": ["hyperlipidemia", "hypoglycemia"], "medication": ["metformin"], "investigation": ["blood glucose", "blood pressure measurement", "eye exam", "heart rate measurement", "hemoglobin a1c", "metabolic panel"]}

## Numerical error example: `aci_bench_test_taskC_3_D2N172-virtassist`

*numerical error example*

ROUGE-L 24.4 · length ratio 1.43 · truncated False · degenerate False · hallucination 65.5 · negation-flip 0.0 · numerical consistency 15.6 · coverage 69.2

**Transcript (excerpt)**

```
[doctor] morning roy , how are you doing ?
[patient] hey , good to see you .
[doctor] so , my nurse told you a little bit about dax ? so , if you do n't mind , i'm going to tell dax a little bit about you today .
[patient] perfect .
[doctor] great , great . so , roy is a 50-year-old male patient who comes in with a history of depression , you had some , um , high blood pressure and some hypertension .
[doctor] so , tell me how have you been doing?
[patient] sure . so it's been a , a pretty stressful winter and spring . and , uh , we've been onboarding a couple new employees and we have been pretty short-staffed in the meantime .
[doctor] um , any changes in , um , weight gain or anything lik …
```

**Reference note**

```
CHIEF COMPLAINT

History of depression.

HISTORY OF PRESENT ILLNESS

Roy Sanchez is a 50-year-old male who comes in with a history of depressionand high blood pressure. He presents today for abnormal labs.

He states it has been a pretty stressful winter and spring, as they have been very short-staffed at work. The patient admits to recent weight gain. He has been hosting friends over vacation and at the beach this summer so the diet is off the charts out the window.

The patient has a history of depression and is doing well. He has been consistent with utilizing his Zoloft 50 mg a day. The patient states this has been a challenging year and a half. He is sleeping okay at night, occasionally waking up at 5 a.m. Denies thoughts of self-harm or suicidal ideation

His high blood pressure has been under good control recently

REVIEW OF SYSTEMS

• Constitutional: Endorses weight gain.
• Psych …
```

**Generated note**

```
CHIEF COMPLAINT

The patient is a 50-year-old male who comes in for followup.

HISTORY OF PRESENT ILLNESS

This is a 50-year-old male who comes in for followup.  He has a history of depression, hypertension, and hyperlipidemia.  The patient states he has been having a very stressful time lately.  He has gained approximately 10 pounds over the past month.  He denies any suicidal ideation.  He has been taking Zoloft 50 mg per day.  He has been having difficulty sleeping.  He wakes up at 5:00 am.  He denies any homicidal ideation.  His blood pressure has been well controlled.  He has a history of a grade II systolic ejection murmur.  He has had no other significant findings on his review of systems.

PHYSICAL EXAM

VITAL SIGNS:  Blood Pressure 140/90, Pulse 80, Respiratory Rate 16, Temperature 98.6, Oxygen Saturation 96% on room air.

HEENT:  Eyes:  conjunctiva was negative for exudate.  Lids showed no ptosis.  Extraocular movements were intact.  PERRLA.  Fundoscopic examination shows no papilledema.  Ears:  tympanic membranes were intact.  No discharge.  Nose:  nasal mucosa was moist.  …
```

- unsupported entities (vs. transcript): bilirubin, blood glucose, creatinine, crp, cyanosis, esr, heart rate measurement, hemoglobin level, hyperlipidemia, insomnia, lipid panel, liver enzymes level, oxygen saturation, pain, papilledema, platelet count, respiratory rate, suicidal ideation, white blood cell count
- incorrect diagnosis: hyperlipidemia  ·  missing diagnosis: —
- incorrect medication: —  ·  missing medication: —
- dosage mismatch: —
- negation flips (vs. reference): —
- unsupported numbers: 0.2, 0.5, 0.7, 1, 1.1, 10, 100, 120, 140, 140/90, 15, 150, 16, 180, 20
- missing information: {"symptom": ["crackles", "rhonchi", "wheezing"], "investigation": ["blood work"]}

## Missing information example: `aci_bench_test_taskC_3_D2N177-virtassist`

*missing information example*

ROUGE-L 13.6 · length ratio 1.59 · truncated True · degenerate True · hallucination 60.0 · negation-flip 0.0 · numerical consistency 100.0 · coverage 14.8

**Transcript (excerpt)**

```
[doctor] hi bruce , how are you ?
[patient] hey , good to see you .
[doctor] good to see you as well . uh , so i know the nurse told you a little bit about dax .
[patient] mm-hmm .
[doctor] i'd like to tell dax about you-
[patient] sure .
[doctor] okay ?
[doctor] so bruce is a 60 year old male , with a past medical history , significant for depression , type two diabetes and hypertension , who presents for followup of his chronic problems .
[doctor] so , bruce , i saw you a couple months ago-
[patient] mm-hmm .
[doctor] how are- how are you doing ?
[patient] it's been a crazy year and a half and i think the uh the anxiety , the pressure of getting ready for thanksgiving was really starting t …
```

**Reference note**

```
CHIEF COMPLAINT

Follow up of chronic problems.

HISTORY OF PRESENT ILLNESS

Bruce Howard is a 60-year-old male with a past medical history significant for depression, type 2 diabetes, and hypertension who presents for follow up of his chronic problems.

In regards to his depression, the patient notes that it has been a crazy year and a half. He experienced a lot of anxiety while getting ready for Thanksgiving but it is starting to resolve now. He denies suicidal and homicidal ideation. The patient and his wife began going on walks and gardening over the summer and he notes good relief of his depression from this; however, the season has changed and he needs an alterative method of management. He has preferred to avoid medications in the past.

The patient is still taking metformin for his diabetes. He notes some dietary indiscretion with Thanksgiving but he is doing better with this now …
```

**Generated note**

```
CHIEF COMPLAINT

Followup of chronic conditions including depression, type II diabetes mellitus, and hypertension.

HISTORY OF PRESENT ILLNESS

The patient is a 60-year-old male with a past medical history significant for depression, type II diabetes mellitus, and hypertension.  He comes in today for followup of his chronic conditions.  The patient has had a history of anxiety and depression.  He has been on no antidepressants.  He has been trying to manage his depression by himself.  He has been walking daily during the summer.  He has been unable to continue this activity due to the cold weather.  He has been trying to find alternative activities.  He has been monitoring his blood sugars closely.  He has been trying to eat less sweets.  He has been eating more fruits and vegetables.  He has been drinking plenty of water.  He has been exercising regularly.  He has been feeling stressed lately.  He has been feeling anxious.  He has been feeling depressed.  He has been having trouble sleeping.  He has been having trouble concentrating.  He has been having trouble remembering things.   …
```

- unsupported entities (vs. transcript): anxiety symptoms, blood glucose, depressive symptoms, insomnia, irritability, memory loss
- incorrect diagnosis: —  ·  missing diagnosis: —
- incorrect medication: —  ·  missing medication: lisinopril, metformin
- dosage mismatch: —
- negation flips (vs. reference): —
- unsupported numbers: —
- missing information: {"symptom": ["abdominal pain", "blood in stool", "chest pain", "crackles", "dyspnea", "dyspnea on exertion"], "diagnosis": ["diabetes"], "medication": ["lisinopril", "metformin"], "investigation": ["blood pressure measurement", "blood work", "diagnostic workup", "echocardiogram", "electrocardiogram", "hemoglobin a1c"]}

## Degenerate output example: `aci_bench_test_taskC_3_D2N178-virtscribe`

*degenerate output example*

ROUGE-L 12.1 · length ratio 0.90 · truncated True · degenerate True · hallucination 71.8 · negation-flip 21.1 · numerical consistency 57.1 · coverage 57.6

**Transcript (excerpt)**

```
[doctor] okay . maria martin , date of birth 03/05/1946 , has been informed and consents to have this visit recorded . the patient is here for follow-up .
[doctor] hi , maria . how have you been doing ?
[patient] same i guess . pretty good .
[doctor] okay , so you got my letter last time on the results . your sugars are not very well controlled .
[patient] yeah , i got them .
[doctor] okay . so did you increase your glimepiride ?
[patient] did i increase it ?
[doctor] yeah .
[patient] i'm still taking the two milligrams .
[doctor] yeah . so we want you to , as the letter said , from the last time , when your a1c was 9.9 , we wanted you to increase it to four milligrams twice a day , so let's …
```

**Reference note**

```
CHIEF COMPLAINT

Follow-up for diabetes management, hypertension, hyperlipidemia, peripheral vascular disease.

HISTORY OF PRESENT ILLNESS

Maria Martin is a 75-year-old female who presents today for follow-up for diabetes.

The patient’s blood glucose levels are poorly controlled and her most recent hemoglobin A1C is 9.9%. She denies increasing glimepiride to 4 mg twice a day as advised but confirms she is compliant with 2 mg twice a day. She mostly denies reducing sugar and carbohydrate intake, although she opts for wheat bread, she does not have pasta at home, and she does not drink much soda and instead drinks club soda or seltzer water. She reports that her diabetic eye exams are up to date and she follows with Dr. Sanchez at Optimum Optometrists. She recently underwent cataract surgery and received a new prescription for her glasses, noting improvement in her vision to one eye and  …
```

**Generated note**

```
CHIEF COMPLAINT

Followup.

HISTORY OF PRESENT ILLNESS

The patient is a 62-year-old female who presents for followup.  She states that she has been following her diabetes regimen as directed.  She has been taking her prescribed medications including her glimepiride 2 mg twice daily.  She has been eating healthy and has been limiting her carbohydrate intake.  She denies any history of tobacco use.  She has been drinking club soda and seltzer water.  She has had recent eye examination and has had cataract surgery.  She has had hypertension and has been on metoprolol 50 mg once daily, lisinopril 20 mg with HCTZ 12.5 mg once daily, and amlodipine 10 mg once daily.  She has had peripheral artery disease and has been on atorvastatin 80 mg once daily.  She has had chronic lower extremity pain and has been diagnosed with peripheral neuropathy.  She has had chronic cough and has been evaluated for possible pneumonia.  She has had dysuria and frequency.  She has had no history of allergies.  She has had no history of previous surgeries.  She has had no history of hospitalizations.  She has ha …
```

- unsupported entities (vs. transcript): abdominal pain, allergic rhinitis, bloating, blood in stool, blurred vision, constipation, crackles, cramping, crepitus, diabetes, diarrhea, difficulty walking, double vision, dysmenorrhea, dysphagia, dysuria, erectile dysfunction, erythema, fatigue, hair loss
- incorrect diagnosis: —  ·  missing diagnosis: hyperlipidemia, hypoglycemia, type 2 diabetes
- incorrect medication: —  ·  missing medication: metformin
- dosage mismatch: [{"drug": "hydrochlorothiazide", "predicted": "12.5 mg", "source": ["25 mg", "25 milligrams"]}]
- negation flips (vs. reference): edema, nocturia, tobacco use, wheezing
- unsupported numbers: 12.5, 62, 80
- missing information: {"symptom": ["foot pain", "murmur", "nasal congestion"], "medical_history": ["type 2 diabetes"], "diagnosis": ["hyperlipidemia", "hypoglycemia"], "medication": ["metformin"], "investigation": ["blood glucose", "blood pressure measurement", "eye exam", "heart rate measurement", "hemoglobin a1c", "metabolic panel"]}

# Split: mts_dialog_test_chat_2023

## Best ROUGE-L: `mts_dialog_test_chat_2023_99`

*highest ROUGE-L in the split*

ROUGE-L 100.0 · length ratio 1.00 · truncated False · degenerate False · hallucination — · negation-flip — · numerical consistency — · coverage —

**Transcript (excerpt)**

```
Doctor: Are you experiencing any symptoms? 
Patient: Nope.
```

**Reference note**

```
Negative.
```

**Generated note**

```
Negative.
```

- unsupported entities (vs. transcript): —
- incorrect diagnosis: —  ·  missing diagnosis: —
- incorrect medication: —  ·  missing medication: —
- dosage mismatch: —
- negation flips (vs. reference): —
- unsupported numbers: —
- missing information: {}

## Worst ROUGE-L: `mts_dialog_test_chat_2023_90`

*lowest ROUGE-L in the split*

ROUGE-L 0.0 · length ratio 5.00 · truncated False · degenerate False · hallucination — · negation-flip — · numerical consistency — · coverage —

**Transcript (excerpt)**

```
Doctor: Have you ever been hospitalized for anything? 
Patient: No, thankfully. I was close to being hospitalized once, but it never actually happened. 
Doctor: And when was this? 
Patient: About two years ago. I got into a pretty brutal skateboarding accident.  
Doctor: Oh gosh. How long have you been skateboarding? 
Patient: Since I was a kid. Bout eight or nine years old. 
Doctor: Do you skate in your neighborhood or at a skatepark? 
Patient: Skatepark. I'll go with my friends every now and again.  
Doctor: Nice. I've never been skateboarding, but I've always been in awe of kids like you who know how to do cool skateboard tricks.
```

**Reference note**

```
None.
```

**Generated note**

```
She has had no hospitalizations.
```

- unsupported entities (vs. transcript): —
- incorrect diagnosis: —  ·  missing diagnosis: —
- incorrect medication: —  ·  missing medication: —
- dosage mismatch: —
- negation flips (vs. reference): —
- unsupported numbers: —
- missing information: {}

## Hallucination example: `mts_dialog_test_chat_2023_103`

*hallucination example*

ROUGE-L 5.6 · length ratio 2.90 · truncated True · degenerate False · hallucination 95.6 · negation-flip — · numerical consistency — · coverage 0.0

**Transcript (excerpt)**

```
Doctor: How's everything going on? 
Patient: I'm having this weird feeling where I feel that my face is going to twitch and I start doing these grimacing actions on my face, mouth, and then it kind of suppresses it, but I'm not sure what's happening. I'm still having a fear of feeling of pressure in the backside of my head and it comes approximately like once each week. 
Doctor: What exactly does this pressure feels like? 
Patient: It feels like pins and needles in my head and a lot of pressure and often it feels like water is running down my hair. 
Doctor: How frequent are these feelings? Is anything helping you? Are you taking any medications or anything else for it? 
Patient: It is like I …
```

**Reference note**

```
The patient had several episodes where she felt like her face was going to twitch, which she could suppress it with grimacing movements of her mouth and face.  She reports she is still having right posterior head pressure like sensations approximately one time per week.  These still are characterized by a tingling, pressure like sensation that often has a feeling as though water is running down on her hair.  This has also decreased in frequency occurring approximately one time per week and seems to respond to over-the-counter analgesics such as Aleve.  Lastly during conversation today, she brought again the problem of daydreaming at work and noted that she occasionally falls asleep when sitting in non-stimulating environments or in front of the television.  She states that she feels fatigued all the time and does not get good sleep.  She describes it as insomnia, but upon questioning she …
```

**Generated note**

```
The patient states she has been experiencing facial grimacing, which she describes as "tic-like" movements.  She also has had some occipital headaches with paresthesias and dysesthesias.  She denies any history of syncope or loss of consciousness.  She denies any history of seizures.  She denies any history of tremors.  She denies any history of weakness.  She denies any history of dysarthria.  She denies any history of diplopia.  She denies any history of visual changes.  She denies any history of hearing changes.  She denies any history of vertigo.  She denies any history of tinnitus.  She denies any history of dysphagia.  She denies any history of hoarseness.  She denies any history of palpitations.  She denies any history of orthopnea.  She denies any history of paroxysmal nocturnal dyspnea.  She denies any history of lower extremity edema.  She denies any history of weight gain.  She denies any history of weight loss.  She denies any history of abdominal pain.  She denies any history of nausea.  She denies any history of vomiting.  She denies any history of hematemesis.  She den …
```

- unsupported entities (vs. transcript): abdominal pain, blood in stool, blurred vision, breast pain, bruising, burning sensation, chills, constipation, diarrhea, dizziness, double vision, dysphagia, dysuria, edema, fever, headache, hematuria, hoarseness, itching, joint pain
- incorrect diagnosis: —  ·  missing diagnosis: —
- incorrect medication: —  ·  missing medication: naproxen
- dosage mismatch: —
- negation flips (vs. reference): —
- unsupported numbers: —
- missing information: {"symptom": ["falls", "insomnia", "snoring", "tingling"], "medication": ["naproxen"]}

## Incorrect diagnosis example: `mts_dialog_test_chat_2023_179`

*incorrect diagnosis example*

ROUGE-L 35.9 · length ratio 0.44 · truncated False · degenerate False · hallucination 36.4 · negation-flip 0.0 · numerical consistency 100.0 · coverage 100.0

**Transcript (excerpt)**

```
Doctor: Good afternoon, sir, did you just have your forty first birthday? 
Patient: Yes, I just had it. 
Doctor: Happy birthday! Just to confirm my charts, you identify as White, correct? 
Patient: Yes, doctor. That's correct. 
Doctor: Great, thank you. So, we've treated you for H I V in the past. I have your lab results from your last visit right here.
Patient: Can you tell me those numbers again, doctor? 
Doctor: Absolutely, your C D 4 count was four hundred twenty five, your viral load was less than fifty, and that was in August of two thousand seven. 
Patient: Are those normal? 
Doctor: Both of those are low, actually, but the low viral load is good. 
Patient: Oh, that's good, I guess. 
 …
```

**Reference note**

```
The patient is a 41-year-old white male with a history of HIV disease.  His last CD4 count was 425, viral load was less than 50 in 08/07.  He was recently hospitalized for left gluteal abscess, for which he underwent I&D and he has newly diagnosed diabetes mellitus.  He also has a history of hypertension and hypertriglyceridemia.  He had been having increased urination and thirst.  He was seen in the hospital by the endocrinology staff and treated with insulin while hospitalized and getting treatment for his perirectal abscess.  The endocrine team apparently felt that insulin might be best for this patient, but because of financial issues, elected to place him on Glucophage and glyburide.  The patient reports that he has been taking the medication.  He is in general feeling better.  He says that his gluteal abscess is improving and he will be following up with Surgery today.
```

**Generated note**

```
The patient is a 41-year-old white male who has HIV.  He has had his labs reviewed by me.  His CD4 count is 425, and his viral load is <50.  He has had recent hospitalization for left buttock abscess.  He has hypertension, hypertriglyceridemia, and he has been diagnosed with diabetes mellitus type II.  He has polyuria and polydipsia.  He has been on insulin, Glucophage, and glyburide.
```

- unsupported entities (vs. transcript): hyperlipidemia, polydipsia, polyuria, sexually transmitted infection
- incorrect diagnosis: hyperlipidemia  ·  missing diagnosis: —
- incorrect medication: —  ·  missing medication: —
- dosage mismatch: —
- negation flips (vs. reference): —
- unsupported numbers: —
- missing information: {}

## Incorrect medication / dosage example: `mts_dialog_test_chat_2023_19`

*incorrect medication / dosage example*

ROUGE-L 31.8 · length ratio 0.79 · truncated False · degenerate False · hallucination 0.0 · negation-flip 0.0 · numerical consistency 100.0 · coverage 100.0

**Transcript (excerpt)**

```
Doctor: Nice to see you again, miss. I see your last visit was back on August tenth two thousand and four. How are you?
Patient: Hi, doctor. Nice to see you again as well. I've been doing fine. 
Doctor: How is your husband doing? 
Patient: He's doing fine. Just working a lot. 
Doctor: Great! I hope the work isn't getting him too stressed out. Also, I need to fill out the ethnicity section in your paperwork; it seems to be missing. What ethnicity do you identify as?
Patient: Oh, yes. I am white. 
Doctor: Thanks! Are you still working too? 
Patient: Yeah, I am. My secretary position has been super stressful lately. 
Doctor: I understand. How is your acne doing? 
Patient: I think it's been gett …
```

**Reference note**

```
The patient is a 49-year-old white female, established patient to Dermatology, last seen in the office on 08/10/2004.  She comes in today for reevaluation of her acne plus she has had what she calls a rash for the past two months now on her chest, stomach, neck, and back.  On examination, this is a flaring of her acne with small folliculitis lesions.  The patient has been taking amoxicillin 500 mg b.i.d. and using Tazorac cream 0.1, and her face is doing well, but she has been out of her medicine now for three days also.  She has also been getting photofacials at Healing Waters and was wondering about what we could offer as far as cosmetic procedures and skin care products, etc.  The patient is married.  She is a secretary.
```

**Generated note**

```
The patient is a 49-year-old female who comes in today with her husband.  She states she has been doing well since her last visit on 08/10/04.  Her husband works a lot and is very stressed.  The patient is white.  She is a secretary and has been having a lot of stress lately.  She has had some acne and has had some rashes on her chest, abdomen, neck, and back for the past two months.  She has had some folliculitis on her chest.  She has been taking 500 mg of Amoxicillin BID and.1% Tazorac cream.  She has been using Healing Waters for photofacial treatments.
```

- unsupported entities (vs. transcript): —
- incorrect diagnosis: —  ·  missing diagnosis: —
- incorrect medication: —  ·  missing medication: —
- dosage mismatch: [{"drug": "amoxicillin", "predicted": "1 %", "source": ["500 mg"]}]
- negation flips (vs. reference): —
- unsupported numbers: —
- missing information: {}

## Negation error example: `mts_dialog_test_chat_2023_170`

*negation error example*

ROUGE-L 6.7 · length ratio 4.10 · truncated True · degenerate True · hallucination 50.0 · negation-flip 33.3 · numerical consistency 100.0 · coverage 75.0

**Transcript (excerpt)**

```
Doctor: Hello nurse, who do we have here today?
Guest_clinician: This is a thirty-seven-year-old, left-handed male. He visited us one month ago for headaches, nausea, and vomiting. His exams from that time showed no evidence of bowel obstruction and he was released home.
Doctor: Was there any improvement after your discharge, sir?
Patient: No, I had the same symptoms on and off after that. 
Doctor: What problems are you facing now?
Patient: I am seeing things blurred and having difficulty concentrating. My headaches are worse when sitting up. I notice them first thing in the morning. 
Doctor: How would you describe your headaches? 
Patient: They're dull, constant, and it feels like as if my  …
```

**Reference note**

```
This 37y/o LHM was seen one month prior to this presentation for HA, nausea and vomiting. Gastrointestinal evaluation at that time showed no evidence of bowel obstruction and he was released home. These symptoms had been recurrent since onset. At presentation he complained of mild blurred vision (OU), difficulty concentrating and HA which worsened upon sitting up. The headaches were especially noticeable in the early morning. He described them as non-throbbing headaches. They begin in the bifrontal region and radiate posteriorly. They occurred up to 6 times/day. The HA improved with lying down or dropping the head down between the knees towards the floor. The headaches were associated with blurred vision, nausea,vomiting, photophobia, and phonophobia. He denied any scotomata or positive visual phenomena. He denies any weakness, numbness, tingling, dysarthria or diplopia. His weight has f …
```

**Generated note**

```
This is a 37 y/o left-handed male who presented to the emergency room one month ago with complaints of headaches, nausea, vomiting, and abdominal pain.  The patient was evaluated by Dr. ___________ and was found to have no signs of bowel obstruction.  He was discharged home.  Since that time, he has had some improvement in his condition, but still has had some episodes of headaches, nausea, vomiting, and blurred vision.  He also has had some episodes of photophobia, phonophobia, and has had some episodes of vertigo.  He has had some episodes of syncope.  He has had some episodes of diplopia.  He has had some episodes of dysarthria.  He has had some episodes of right-sided weakness.  He has had some episodes of left-sided weakness.  He has had some episodes of right-sided paresthesias.  He has had some episodes of left-sided paresthesias.  He has had some episodes of right-sided numbness.  He has had some episodes of left-sided numbness.  He has had some episodes of right-sided tremor.  He has had some episodes of left-sided tremor.  He has had some episodes of right-sided ataxia.  He …
```

- unsupported entities (vs. transcript): abdominal pain, dizziness, one-sided weakness, photophobia, slurred speech, syncope, tremor
- incorrect diagnosis: —  ·  missing diagnosis: —
- incorrect medication: —  ·  missing medication: —
- dosage mismatch: —
- negation flips (vs. reference): double vision, numbness, slurred speech
- unsupported numbers: —
- missing information: {"symptom": ["tingling", "weakness"], "investigation": ["weight measurement"]}

## Numerical error example: `mts_dialog_test_chat_2023_146`

*numerical error example*

ROUGE-L 7.2 · length ratio 5.37 · truncated True · degenerate True · hallucination 50.0 · negation-flip 0.0 · numerical consistency 35.3 · coverage 33.3

**Transcript (excerpt)**

```
Doctor: Good morning, young man. Is this your mother?
Patient: Yes, doctor.
Doctor: Good, nice to mee you. Can you tell me more about your son, please? 
Guest_family: Good morning to you too, doctor. Well, he's about five and a half now, and he broke both the bones in his forearm in September of two thousand seven. 
Doctor: How did the fracture heal? Generally, children heal very well. 
Guest_family: Well, yes, until he also rebroke it about a month ago. 
Doctor: Yes, I see now, there's an ulnar nail pretty prominently visible under the skin, did he have surgery for this? 
Guest_family: Yes, about a month ago now. Should we remove the nail?
Doctor: We'll have to, even though its early.
Guest …
```

**Reference note**

```
The patient is a 5-year, 5-month-old male who sustained a both-bone forearm fracture in September 2007.  The fracture healed uneventfully, but then the patient subsequently suffered a refracture one month ago.  The patient had shortening in arms, noted in both bones.  The parents opted for surgical stabilization with nailing.  This was performed one month ago on return visit.  His ulnar nail was quite prominent underneath the skin.  It was decided to remove the ulnar nail early and place the patient in another cast for 3 weeks. Risks and benefits of the surgery were discussed with the mother.  Risk of surgery incudes risks of anesthesia, infection, bleeding, changes in sensation in most of the extremity, need for longer casting.  All questions were answered and mother agreed to above plan.
```

**Generated note**

```
The patient is a 5-year-old male who has had multiple fractures of the right forearm.  He was first injured in 09/2007 with bilateral radius fractures.  He healed well but then had a rebreak of the same area in 10/2008.  He had an open reduction internal fixation with an ulnar nail.  He had a break again in 11/2008.  He had an open reduction internal fixation with an ulnar nail.  He had a break again in 12/2008.  He had an open reduction internal fixation with an ulnar nail.  He had a break again in 01/2009.  He had an open reduction internal fixation with an ulnar nail.  He had a break again in 02/2009.  He had an open reduction internal fixation with an ulnar nail.  He had a break again in 03/2009.  He had an open reduction internal fixation with an ulnar nail.  He had a break again in 04/2009.  He had an open reduction internal fixation with an ulnar nail.  He had a break again in 05/2009.  He had an open reduction internal fixation with an ulnar nail.  He had a break again in 06/2009.  He had an open reduction internal fixation with an ulnar nail.  He had a break again in 07/2009 …
```

- unsupported entities (vs. transcript): trauma
- incorrect diagnosis: —  ·  missing diagnosis: —
- incorrect medication: —  ·  missing medication: —
- dosage mismatch: —
- negation flips (vs. reference): —
- unsupported numbers: 10, 11, 12, 2008, 2009, 2010, 2011, 4, 6, 8, 9
- missing information: {"symptom": ["bleeding"], "diagnosis": ["infection"]}

## Missing information example: `mts_dialog_test_chat_2023_103`

*missing information example*

ROUGE-L 5.6 · length ratio 2.90 · truncated True · degenerate False · hallucination 95.6 · negation-flip — · numerical consistency — · coverage 0.0

**Transcript (excerpt)**

```
Doctor: How's everything going on? 
Patient: I'm having this weird feeling where I feel that my face is going to twitch and I start doing these grimacing actions on my face, mouth, and then it kind of suppresses it, but I'm not sure what's happening. I'm still having a fear of feeling of pressure in the backside of my head and it comes approximately like once each week. 
Doctor: What exactly does this pressure feels like? 
Patient: It feels like pins and needles in my head and a lot of pressure and often it feels like water is running down my hair. 
Doctor: How frequent are these feelings? Is anything helping you? Are you taking any medications or anything else for it? 
Patient: It is like I …
```

**Reference note**

```
The patient had several episodes where she felt like her face was going to twitch, which she could suppress it with grimacing movements of her mouth and face.  She reports she is still having right posterior head pressure like sensations approximately one time per week.  These still are characterized by a tingling, pressure like sensation that often has a feeling as though water is running down on her hair.  This has also decreased in frequency occurring approximately one time per week and seems to respond to over-the-counter analgesics such as Aleve.  Lastly during conversation today, she brought again the problem of daydreaming at work and noted that she occasionally falls asleep when sitting in non-stimulating environments or in front of the television.  She states that she feels fatigued all the time and does not get good sleep.  She describes it as insomnia, but upon questioning she …
```

**Generated note**

```
The patient states she has been experiencing facial grimacing, which she describes as "tic-like" movements.  She also has had some occipital headaches with paresthesias and dysesthesias.  She denies any history of syncope or loss of consciousness.  She denies any history of seizures.  She denies any history of tremors.  She denies any history of weakness.  She denies any history of dysarthria.  She denies any history of diplopia.  She denies any history of visual changes.  She denies any history of hearing changes.  She denies any history of vertigo.  She denies any history of tinnitus.  She denies any history of dysphagia.  She denies any history of hoarseness.  She denies any history of palpitations.  She denies any history of orthopnea.  She denies any history of paroxysmal nocturnal dyspnea.  She denies any history of lower extremity edema.  She denies any history of weight gain.  She denies any history of weight loss.  She denies any history of abdominal pain.  She denies any history of nausea.  She denies any history of vomiting.  She denies any history of hematemesis.  She den …
```

- unsupported entities (vs. transcript): abdominal pain, blood in stool, blurred vision, breast pain, bruising, burning sensation, chills, constipation, diarrhea, dizziness, double vision, dysphagia, dysuria, edema, fever, headache, hematuria, hoarseness, itching, joint pain
- incorrect diagnosis: —  ·  missing diagnosis: —
- incorrect medication: —  ·  missing medication: naproxen
- dosage mismatch: —
- negation flips (vs. reference): —
- unsupported numbers: —
- missing information: {"symptom": ["falls", "insomnia", "snoring", "tingling"], "medication": ["naproxen"]}

## Degenerate output example: `mts_dialog_test_chat_2023_75`

*degenerate output example*

ROUGE-L 4.2 · length ratio 4.20 · truncated True · degenerate True · hallucination 93.7 · negation-flip 0.0 · numerical consistency — · coverage 75.0

**Transcript (excerpt)**

```
Doctor: Good afternoon, sir, and who is this with you today? 
Patient: How are you doing, doctor? This is my daughter. 
Doctor: I'm doing well, but how are you? How have you been doing since I last saw you? 
Patient: I've been doing quite well, doctor. 
Doctor: So, no symptoms of heart disease, or failure? 
Patient: Nope, absolutely not. 
Doctor: Did you follow up with Doctor X? 
Patient: Yes, she said I was doing well, too. 
Doctor: Great! How has your blood sugar been? 
Patient: It's been in a normal range, which I'm thankful for. 
Doctor: Have you had any falls since your last visit? 
Patient: Nope, I've been doing really well. 
Doctor: How is your knee doing? 
Patient: Well, my right kne …
```

**Reference note**

```
The patient has been doing quite well since he was last seen.  He comes in today with his daughter.  He has had no symptoms of CAD or CHF.  He had followup with Dr. X and she thought he was doing quite well as well.  He has had no symptoms of hyperglycemia or hypoglycemia.  He has had no falls.  His right knee does pain him at times and he is using occasional doses of Tylenol for that.  He wonders whether he could use a knee brace to help him with that issue as well.  His spirits are good.  He has had no incontinence.  His memory is clear, as is his thinking.
```

**Generated note**

```
The patient is here with his daughter.  He states that he has been doing very well since his last visit.  Denies any history of heart disease, congestive heart failure, diabetes mellitus, falls, dysuria, urinary incontinence, constipation, diarrhea, abdominal pain, nausea, vomiting, hematemesis, melena, chest pain, palpitations, orthopnea, paroxysmal nocturnal dyspnea, syncope, shortness of breath, wheezing, cough, sputum production, hemoptysis, fever, chills, arthralgias, joint swelling, weakness, fatigue, weight loss, weight gain, anorexia, dysphagia, hoarseness, odynophagia, hematuria, flank pain, dysuria, frequency, urgency, nocturia, noctural enuresis, confusion, disorientation, forgetfulness, difficulty concentrating, difficulty remembering recent events, difficulty remembering past events, difficulty remembering names of people, places, things, difficulty remembering words, difficulty speaking, difficulty swallowing, difficulty hearing, tinnitus, vertigo, dizziness, headache, photophobia, phonophobia, diplopia, blurred vision, decreased visual acuity, eye pain, tearing, rednes …
```

- unsupported entities (vs. transcript): abdominal pain, arm pain, blood in stool, blurred vision, burning sensation, carpal tunnel syndrome, chest pain, chills, confusion, constipation, cough, diabetes, diarrhea, dizziness, double vision, dysphagia, dyspnea, dysuria, elbow pain, erythema
- incorrect diagnosis: —  ·  missing diagnosis: —
- incorrect medication: —  ·  missing medication: acetaminophen
- dosage mismatch: —
- negation flips (vs. reference): —
- unsupported numbers: —
- missing information: {"medical_history": ["hypoglycemia"], "medication": ["acetaminophen"]}

# Split: mts_dialog_test_sum_2023

## Best ROUGE-L: `mts_dialog_test_sum_2023_188`

*highest ROUGE-L in the split*

ROUGE-L 100.0 · length ratio 1.00 · truncated False · degenerate False · hallucination 0.0 · negation-flip 0.0 · numerical consistency — · coverage 100.0

**Transcript (excerpt)**

```
Doctor: Any known drug allergies? 
Patient: No, none.
```

**Reference note**

```
No known drug allergies.
```

**Generated note**

```
No known drug allergies.
```

- unsupported entities (vs. transcript): —
- incorrect diagnosis: —  ·  missing diagnosis: —
- incorrect medication: —  ·  missing medication: —
- dosage mismatch: —
- negation flips (vs. reference): —
- unsupported numbers: —
- missing information: {}

## Worst ROUGE-L: `mts_dialog_test_sum_2023_150`

*lowest ROUGE-L in the split*

ROUGE-L 0.0 · length ratio 14.00 · truncated False · degenerate False · hallucination 100.0 · negation-flip — · numerical consistency — · coverage —

**Transcript (excerpt)**

```
Doctor: Hello. Looks like you're a new patient. How are you doing today?
Patient: I'm doing fine. My back has been hurting lately. 
Doctor: I see. Before we begin, I want to confirm some information with you. 
Patient: Sounds good. 
Doctor: Do you smoke or drink? 
Patient: Never have never will. 
Doctor: Does anyone in your family have a history of medical problems? 
Patient: Nope. 
Doctor: Thank you. Back to your injury. Have you ever had back pain before?
Patient: I've never. This is my first time.
```

**Reference note**

```
unremarkable.
```

**Generated note**

```
She denies tobacco use and alcohol use.  She denies any significant past medical history.
```

- unsupported entities (vs. transcript): tobacco use
- incorrect diagnosis: —  ·  missing diagnosis: —
- incorrect medication: —  ·  missing medication: —
- dosage mismatch: —
- negation flips (vs. reference): —
- unsupported numbers: —
- missing information: {}

## Hallucination example: `mts_dialog_test_sum_2023_117`

*hallucination example*

ROUGE-L 26.9 · length ratio 0.66 · truncated False · degenerate False · hallucination 76.0 · negation-flip 11.1 · numerical consistency 100.0 · coverage 75.0

**Transcript (excerpt)**

```
Doctor: Good morning, young man, and can I assume that you're his mother? 
Guest_family: Yes, doctor, good morning, that's correct. 
Doctor: Good, tell me a little more about your son, please. 
Guest_family: Well, he's seven years old now, and he's been healthy all his life. But he recently started having pain in his fingers, elbows, and neck. 
Doctor: What race does your family identify with?
Guest_family: We're white, doctor. 
Doctor: Okay, how long has he had this pain? 
Guest_family: It's been, um, about two months now. 
Doctor: Has the pain improved any since it began?
Patient: Well, it's a little better now. 
Guest_family: Yeah, he says it's almost gone now, but he was at a point where …
```

**Reference note**

```
We had the pleasure of seeing the patient today in our Pediatric Rheumatology Clinic.  He was sent here with a chief complaint of joint pain in several joints for few months.  This is a 7-year-old white male who has no history of systemic disease, who until 2 months ago, was doing well and 2 months ago, he started to complain of pain in his fingers, elbows, and neck.  At this moment, this is better and is almost gone, but for several months, he was having pain to the point that he would cry at some point.  He is not a complainer according to his mom and he is a very active kid.  There is no history of previous illness to this or had gastrointestinal problems.  He has problems with allergies, especially seasonal allergies and he takes Claritin for it.  Other than that, he has not had any other problem.  Denies any swelling except for that doctor mentioned swelling on his elbow.  There is  …
```

**Generated note**

```
The patient is a 7-year-old Caucasian male who presents with complaints of pain in his fingers, elbows, and neck for approximately 2 months.  The pain has been improving over time.  He denies fever, chills, weight loss, night sweats, joint effusion, rash, arthralgias, diarrhea, dysuria, hematuria, abdominal pain, vomiting, headaches, photophobia, diplopia, dysphagia, dysarthria, weakness, numbness, tingling, paresthesias, or visual changes.  He has had no history of recent trauma.  He has had no history of recent travel.  He has had no history of sick contacts.  He has had no history of recent surgeries.  He has had no history of allergies except for seasonal allergies.  He takes Claritin for his allergies.  He has had no history of significant past illnesses.  He has had no history of significant past surgical procedures.
```

- unsupported entities (vs. transcript): abdominal pain, blurred vision, chills, double vision, dysphagia, dysuria, headache, hematuria, joint pain, joint swelling, night sweats, numbness, photophobia, slurred speech, tingling, trauma, vomiting, weakness, weight loss
- incorrect diagnosis: —  ·  missing diagnosis: —
- incorrect medication: —  ·  missing medication: —
- dosage mismatch: —
- negation flips (vs. reference): joint pain
- unsupported numbers: —
- missing information: {"symptom": ["edema", "lymphadenopathy"], "medical_history": ["peptic ulcer disease"]}

## Incorrect diagnosis example: `mts_dialog_test_sum_2023_32`

*incorrect diagnosis example*

ROUGE-L 30.8 · length ratio 2.67 · truncated False · degenerate False · hallucination 50.0 · negation-flip — · numerical consistency — · coverage —

**Transcript (excerpt)**

```
Doctor: Please don't be scared. We will evaluate you for possible infection in blood due to accidental exposure.
Patient: I am nervous.
Doctor: Oh.
Patient: Yeah.
Doctor: Please don't be. We are all with you.
```

**Reference note**

```
Blood-borne pathogen exposure.
```

**Generated note**

```
Possible blood-borne infection secondary to needle stick injury.
```

- unsupported entities (vs. transcript): trauma
- incorrect diagnosis: trauma  ·  missing diagnosis: —
- incorrect medication: —  ·  missing medication: —
- dosage mismatch: —
- negation flips (vs. reference): —
- unsupported numbers: —
- missing information: {}

## Incorrect medication / dosage example: `mts_dialog_test_sum_2023_67`

*incorrect medication / dosage example*

ROUGE-L 29.4 · length ratio 0.62 · truncated False · degenerate False · hallucination 71.4 · negation-flip 0.0 · numerical consistency 66.7 · coverage 57.1

**Transcript (excerpt)**

```
Doctor: Hello, how are you doing? 
Patient: Hanging in there. Thank you. 
Doctor: So, you just celebrated your birthday. How was it? How is it feeling to be close to forties? 
Patient: I just turned thirty nine. I would say older the wiser. 
Doctor: That's true. Okay, so you are here for your follow up. Let's see, you have type one diabetes mellitus, right?
Patient: Yeah, that's right. Last time I was here almost four months ago. 
Doctor: How are you doing since last visit? 
Patient: I have been good. My sugar has been under the range. Unfortunately, my pump was having some issues for the last two weeks. 
Doctor: Oh no. What happened? 
Patient: I don't know. I tried to get it fixed but nothi …
```

**Reference note**

```
The patient is a 39-year-old woman returns for followup management of type 1 diabetes mellitus.  Her last visit was approximately 4 months ago.  Since that time, the patient states her health had been good and her glycemic control had been good, however, within the past 2 weeks she had a pump malfunction, had to get a new pump and was not certain of her pump settings and has been having some difficulty with glycemic control over the past 2 weeks.  She is not reporting any severe hypoglycemic events, but is having some difficulty with hyperglycemia both fasting and postprandial.  She is not reporting polyuria, polydipsia or polyphagia.  She is not exercising at this point and has a diet that is rather typical of woman with twins and a young single child as well.  She is working on a full-time basis and so eats on the run a lot, probably eats more than she should and not making the best ch …
```

**Generated note**

```
The patient is a 39-year-old female with history of Type I Diabetes Mellitus.  She comes in today for her routine followup.  The patient states she has been doing well.  Her sugars have been within target ranges.  However, she has had some problems with her insulin pump for the last two weeks.  She has had difficulty setting up her pump and has had some difficulties controlling her blood glucose during this period.  She denies any episodes of hypoglycemia, syncope, diaphoresis, tachycardia, palpitations, visual changes, confusion, polyuria, polydipsia, polyphagia, or weight loss.  She does deny any recent exercise.  She is a full-time employee and works as a medical coder.  She is a mother of three children including twins and a young infant.  She denies any recent travel.
```

- unsupported entities (vs. transcript): blurred vision, hypoglycemia, insulin, palpitations, polydipsia, polyphagia, polyuria, syncope, tachycardia, weight loss
- incorrect diagnosis: —  ·  missing diagnosis: —
- incorrect medication: insulin  ·  missing medication: —
- dosage mismatch: —
- negation flips (vs. reference): —
- unsupported numbers: 3
- missing information: {"diagnosis": ["diabetes"], "investigation": ["blood work", "lipid panel"]}

## Negation error example: `mts_dialog_test_sum_2023_2`

*negation error example*

ROUGE-L 7.9 · length ratio 3.56 · truncated True · degenerate True · hallucination 85.4 · negation-flip 37.5 · numerical consistency 100.0 · coverage 34.8

**Transcript (excerpt)**

```
Doctor: Good afternoon, sir. My chart here says that you are a fifty one year old white male, is that correct?
Patient: Good afternoon, doctor. Yes, all of that is correct. 
Doctor: Great, thank you. Please, walk me through the history of your symptoms, when did everything begin. 
Patient: Well, I was diagnosed with P T L D towards the end of two thousand seven. 
Doctor: What symptoms were you experiencing? 
Patient: I had swollen lymph nodes, stomach pain, I was losing a lot of weight, and I wasn't really eating. 
Doctor: How have you been treated for this?
Patient: Well, I didn't go to the doctor right away, but eventually I went to the hospital, and they did a biopsy of my groin lymph nod …
```

**Reference note**

```
A 51-year-old white male diagnosed with PTLD in latter half of 2007.  He presented with symptoms of increasing adenopathy, abdominal pain, weight loss, and anorexia.  He did not seek medical attention immediately.  He was finally hospitalized by the renal transplant service and underwent a lymph node biopsy in the groin, which showed diagnosis of large cell lymphoma.  He was discussed at the hematopathology conference.  Chemotherapy with rituximab plus cyclophosphamide, daunorubicin, vincristine, and prednisone was started.  First cycle of chemotherapy was complicated by sepsis despite growth factor support.  He also appeared to have become disoriented either secondary to sepsis or steroid therapy. The patient has received 5 cycles of chemotherapy to date.  He did not keep his appointment for a PET scan after 3 cycles because he was not feeling well.  His therapy has been interrupted for …
```

**Generated note**

```
This is a 51-year-old white male who has been diagnosed with PTLD.  He has been on chemotherapy since 2007.  He has had multiple admissions to the hospital for his condition.  He has had multiple surgeries including a recent surgery for squamous cell carcinoma of the skin.  He has had multiple infections including pneumonia and cellulitis.  He has had multiple episodes of sepsis.  He has had multiple episodes of neutropenia.  He has had multiple episodes of thrombocytopenia.  He has had multiple episodes of anemia.  He has had multiple episodes of hypokalemia.  He has had multiple episodes of hyponatremia.  He has had multiple episodes of hyperkalemia.  He has had multiple episodes of hypertension.  He has had multiple episodes of tachycardia.  He has had multiple episodes of atrial fibrillation.  He has had multiple episodes of ventricular tachycardia.  He has had multiple episodes of syncope.  He has had multiple episodes of confusion.  He has had multiple episodes of disorientation.  He has had multiple episodes of memory loss.  He has had multiple episodes of forgetfulness.  He h …
```

- unsupported entities (vs. transcript): anemia, anxiety, arrhythmia, atrial fibrillation, cellulitis, constipation, daytime sleepiness, depression, diarrhea, dizziness, dysuria, edema, fatigue, hematuria, hyperkalemia, hypertension, hypokalemia, hyponatremia, insomnia, irritability
- incorrect diagnosis: —  ·  missing diagnosis: kidney transplant
- incorrect medication: —  ·  missing medication: prednisone, rituximab
- dosage mismatch: —
- negation flips (vs. reference): fatigue, nausea, vomiting
- unsupported numbers: —
- missing information: {"symptom": ["chest pain", "cough", "dyspnea", "loss of appetite", "numbness", "tingling"], "medical_history": ["lymphoma"], "diagnosis": ["cancer", "kidney transplant"], "medication": ["prednisone", "rituximab"], "investigation": ["biopsy", "clinical score", "pet scan"]}

## Numerical error example: `mts_dialog_test_sum_2023_107`

*numerical error example*

ROUGE-L 47.6 · length ratio 0.99 · truncated False · degenerate False · hallucination 33.3 · negation-flip 0.0 · numerical consistency 50.0 · coverage 66.7

**Transcript (excerpt)**

```
Doctor: Good afternoon, ma'am, I just need some information before we get started today. 
Patient: Absolutely, good afternoon, doctor. 
Doctor: My chart says here that you're fifty nine years old, is that correct? 
Patient: Yes, that's correct. 
Doctor: I also see that you have a history of breast cancer, is that correct as well?
Patient: Yes, that's also correct. 
Doctor: When were you diagnosed initially? 
Patient: Um, I was diagnosed in June of nineteen ninety four. 
Doctor: How has this been managed in the past, ma'am? 
Patient: Um, I've taken Zometa, Faslodex, and Aromasin. 
Doctor: How has the cancer progressed since you were diagnosed? 
Patient: The doctors said I had rising tumor mar …
```

**Reference note**

```
She is a very pleasant 59-year-old nurse with a history of breast cancer.  She was initially diagnosed in June 1994.  Her previous treatments included Zometa, Faslodex, and Aromasin.  She was found to have disease progression first noted by rising tumor markers.  PET/CT scan revealed metastatic disease and she was enrolled in clinical trial of CTSU/C40502.  She was randomized to the ixabepilone plus Avastin.  She experienced dose-limiting toxicity with the fourth cycle.  The Ixempra was skipped on day 1 and day 8.  She then had a dose reduction and has been tolerating treatment well with the exception of progressive neuropathy.  Early in the month she had concerned about possible perforated septum.  She was seen by ENT urgently.  She was found to have nasal septum intact.  She comes into clinic today for day eight Ixempra.
```

**Generated note**

```
The patient is a 59-year-old female who comes in for her eighth day of Ixempra.  She has a history of breast cancer diagnosed in 06/1994.  She has been treated with Zometa, Faslodex, and Aromasin.  Her cancer has been progressive with rising tumor markers.  She has had a PET CT scan which shows metastatic disease.  She has been in the CTSU 40502 trial where she was randomized to the Ixabepilone plus Avastin arm.  She developed dose limiting toxicity after the fourth cycle.  She missed Ixempra on the 1st and 8th day.  She has had her dose reduced.  She has tolerated the treatment fairly well except for some neuropathy.  She denies any other significant side effects.  She does have a history of perforated septum which was evaluated by ENT and found to be negative.
```

- unsupported entities (vs. transcript): adverse drug reaction, ct scan
- incorrect diagnosis: —  ·  missing diagnosis: —
- incorrect medication: —  ·  missing medication: —
- dosage mismatch: —
- negation flips (vs. reference): —
- unsupported numbers: 40502, 6
- missing information: {"investigation": ["imaging", "pet scan"]}

## Missing information example: `mts_dialog_test_sum_2023_78`

*missing information example*

ROUGE-L 3.7 · length ratio 0.15 · truncated False · degenerate False · hallucination 100.0 · negation-flip — · numerical consistency — · coverage 0.0

**Transcript (excerpt)**

```
Doctor: Hello there, how are you?
Guest_family: I am little scared. 
Doctor: I understand, so how old is she? 
Guest_family: She is ten days old today. 
Doctor: And just wanted to confirm the ethnicity is Caucasian, right?
Guest_family: Yes. 
Doctor: Okay, so tell me what's going on with her?
Guest_family: I was feeding her and then I suddenly noticed this unusual jerky movement in both her arms and legs. 
Guest_family: It lasted about a minute. 
Doctor: When did you first notice it? 
Guest_family: The first day when I was feeding her. She was barely a day old.
Doctor: Okay, and how many times till now?
Guest_family: About six times. 
Doctor: Did you notice any interrupted breathing or bluis …
```

**Reference note**

```
Negative fever, negative fussiness, tracks with her eyes, some sneezing and hiccups.  This patient has developed some upper airway congestion in the past day.  She has not had any vomiting or diarrhea.  Per mom, she does not spit up, and mom is also unable to notice any relationship between these movements and feeds.  This patient has not had any rashes.  Mom was notified by the nurses at birth that her temperature may be low of approximately 97.5 degrees Fahrenheit.  Otherwise, the above history of present illness and other review of systems negative.
```

**Generated note**

```
Significant for generalized tonic-clonic seizures.  Negative for respiratory distress, cyanosis, or altered mental status.
```

- unsupported entities (vs. transcript): confusion, cyanosis, seizure
- incorrect diagnosis: —  ·  missing diagnosis: —
- incorrect medication: —  ·  missing medication: —
- dosage mismatch: —
- negation flips (vs. reference): —
- unsupported numbers: —
- missing information: {"symptom": ["diarrhea", "fever", "nasal congestion", "rash", "sneezing", "vomiting"]}

## Degenerate output example: `mts_dialog_test_sum_2023_162`

*degenerate output example*

ROUGE-L 10.6 · length ratio 3.77 · truncated True · degenerate True · hallucination 28.6 · negation-flip 0.0 · numerical consistency 80.0 · coverage 42.9

**Transcript (excerpt)**

```
Doctor: Good afternoon, ma'am. Before we begin, how old are you?
Patient: Good afternoon, doctor, I'm forty five years young. 
Doctor: Great, and with what race do you identify?
Patient: I'm an African American. 
Doctor: Thank you, what seems to be the problem today?
Patient: It started a while ago. I've had this pain in my left shoulder and neck for the last year and a half.
Doctor: I see, have these symptoms been persistent for the last year and a half? Or do they come and go?
Patient: The pain actually went away all on its own once, but now I have pain in my right foot.
Doctor: Is there any injury that you can remember?
Patient: No, but I started working out really hard in November of two …
```

**Reference note**

```
The patient is a 45-year-old African-American female whose symptoms first started some one and a half years ago with pain in the left shoulder and some neck pain.  This has subsequently resolved.  She started vigorous workouts in November 2005.  In March of this year, she suddenly could not feel her right foot on the bathroom floor and subsequently went to her primary care physician.  By her report, she had a nerve conduction study and a diagnosis of radiculopathy was made.  She had an MRI of lumbosacral spine, which was within normal limits.  She then developed a tingling sensation in the right middle toe.  Symptoms progressed to sensory symptoms of her knees, elbows, and left middle toe.  She then started getting sensory sensations in the left hand and arm.  She states that she feels a little bit wobbly at the knees and that she is slightly dragging her left leg.  Symptoms have been mi …
```

**Generated note**

```
The patient is a 45-year-old black female who comes in today complaining of left shoulder and neck pain for the past 1 1/2 years.  She has had some periods where she has had no pain, but she has had some periods where she has had pain.  She also has had some pain in her right foot.  She denies any trauma.  She has been working out since November 2005.  In March 2006, she could not feel her right foot when she got out of the shower.  She has had some numbness and tingling in her right middle toe, her left middle toe, her knees, and her elbows.  She has had some weakness in her left leg.  She has had some difficulty walking.  She has had some difficulty with balance.  She has had some difficulty with her gait.  She has had some difficulty with her left leg.  She has had some difficulty with her right foot.  She has had some difficulty with her right ankle.  She has had some difficulty with her right knee.  She has had some difficulty with her right hip.  She has had some difficulty with her right thigh.  She has had some difficulty with her right calf.  She has had some difficulty with …
```

- unsupported entities (vs. transcript): difficulty walking, neck pain
- incorrect diagnosis: —  ·  missing diagnosis: —
- incorrect medication: —  ·  missing medication: —
- dosage mismatch: —
- negation flips (vs. reference): —
- unsupported numbers: 2006
- missing information: {"medical_history": ["sciatica"], "investigation": ["diagnostic workup", "emg", "mri"]}
