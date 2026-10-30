# Example errors — sftfact

Each block shows the transcript excerpt, the reference note, the generated note and the flags raised by the factuality checker.

# Split: aci_bench_test_taskB_1

## Best ROUGE-L: `aci_bench_test_taskB_1_D2N098-virtscribe`

*highest ROUGE-L in the split*

ROUGE-L 36.4 · length ratio 0.96 · truncated False · degenerate False · hallucination 10.0 · negation-flip 0.0 · numerical consistency 75.0 · coverage 100.0

**Transcript (excerpt)**

```
[doctor] all right . today i am seeing jose james . uh , date of birth 9/29/1957 . mr . james is a new patient who's having pain in his left shoulder and elbow . he fell five months ago going up a stairs , and the pain has been present since .
[doctor] hi mr . james , i'm doctor isabella . how are you doing ?
[patient] i'm okay . thank you .
[doctor] that's good . that's good . tell me what's brings you in today .
[patient] sure . so i've been having constant pain in my left shoulder and left elbow for a while , about five months or so . hurts all the time . pretty bad at times .
[doctor] mm . that does not sound like fun . it sounds like you injured it going up the stairs ?
[patient] yes ,  …
```

**Reference note**

```
CHIEF COMPLAINT

Left shoulder and elbow pain.

HISTORY OF PRESENT ILLNESS

Mr. Jose James is a 64-year-old male who presents for left shoulder and elbow pain.

The patient reports falling on his hand while going up stairs 5 months ago and has been experiencing constant pain since. He admits he was continuing to complete strength training exercises at least 2 times per week, however, he was unable to lift more than 15-20 pounds due to the pain.

During the past 1-2 weeks, Mr. James has discontinued strength training activities. Additionally, he has iced the inflicted areas, denies taking any pain medications, and reports his pain has slightly improved but it is still rather constant. He denies tingling and numbness.

The patient walks 30-minutes most days of the week.

SOCIAL HISTORY

Retired last year, was an office worker.

PHYSICAL EXAM

Musculoskeletal
Left shoulder and elbow, tender …
```

**Generated note**

```
CHIEF COMPLAINT

Left shoulder and left elbow pain.

HISTORY OF PRESENT ILLNESS

The patient is a 59-year-old male who comes in today complaining of left shoulder and left elbow pain.  He states that he had fallen down the stairs approximately 5 months ago and has had constant pain in his left shoulder and left elbow ever since.  He denies any numbness, tingling, warmth, erythema, or deformity.  He has had difficulty lifting heavy objects and has had to stop exercising due to pain.  He has had some relief with icing and rest.  He denies any history of trauma to the area except for the fall 5 months ago.

REVIEW OF SYSTEMS

NEUROLOGIC: Negative.
MUSCULOSKELETAL: Positive for left shoulder and left elbow pain.
SKIN: Negative.
CARDIOVASCULAR: Negative.
RESPIRATORY: Negative.
GASTROINTESTINAL: Negative.
GENITOURINARY: Negative.

PHYSICAL EXAM

NECK: Supple.
LEFT SHOULDER: TENDER TO PALPATION IN THE SUBACROMIAL SPACE.  NEER'S TEST POSITIVE.  HAWKINS-KENNEDY TEST POSITIVE.  ABDUCTION TO 90 DEGREES.  NORMAL EMPTY CAN TEST.  LEFT ELBOW: TENDER TO PALPATION.  PROXIMAL AND DISTAL UPPER EXTREMI …
```

- unsupported entities (vs. transcript): elbow pain
- incorrect diagnosis: —  ·  missing diagnosis: —
- incorrect medication: —  ·  missing medication: —
- dosage mismatch: —
- negation flips (vs. reference): —
- unsupported numbers: 59
- missing information: {}

## Worst ROUGE-L: `aci_bench_test_taskB_1_D2N113-aci`

*lowest ROUGE-L in the split*

ROUGE-L 4.2 · length ratio 1.24 · truncated True · degenerate True · hallucination 90.7 · negation-flip 12.5 · numerical consistency 0.0 · coverage 52.9

**Transcript (excerpt)**

```
[doctor] hi jacqueline how are you doing today
[patient] i'm doing okay i'm just really anxious about my recent blood work that my pcp did and said that i have hepatitis c i'm just really surprised because i've been feeling fine
[doctor] okay so were you ever told in the past that you have hepatitis c
[patient] no never
[doctor] okay and do do you have any history like iv drug use known that you know or do you have any known to have any like hepatitis c positive partners
[patient] i mean like years ago i used to party a lot and even use iv drugs but i've been clean for over fifteen years now
[doctor] okay well very good you know congratulations on that that's that's a great great achievement …
```

**Reference note**

```
CHIEF COMPLAINT

Hepatitis C.

SOCIAL HISTORY

Patient reports personal history of intravenous drug use over 15 years ago. She is currently smoking 1-2 cigarettes per day, previously 1 to 1.5 packs per day. She also has a history of heavy alcohol use, but now drinks approximately 1 beer per day, more on the weekends.

FAMILY HISTORY

Patient reports family history significant for hypertension, diabetes, and depression.

REVIEW OF SYSTEMS

Constitutional: Reports fatigue.

All other systems were reviewed and are negative.

VITALS

Vitals look good today.

PHYSICAL EXAM

Constitutional
- General Appearance: in no apparent distress.

Respiratory
- Auscultation of Lungs: No wheezes, rales, or rhonchi.

Cardiovascular
- Auscultation of Heart: Regular rate. 2/6 systolic ejection murmur, unchanged.

Gastrointestinal
- Examination of Abdomen: No masses or tenderness. No hepatosplenomegaly.
- Aus …
```

**Generated note**

```
CHIEF COMPLAINT

The patient is a 45-year-old female who comes in for evaluation of her recent lab results which indicate she has hepatitis C.  She denies jaundice, wheezing, crackles, rhonchi, edema, dyspnea, orthopnea, palpitations, syncope, chest pain, abdominal pain, nausea, vomiting, diarrhea, constipation, hematochezia, melena, arthralgia, weakness, tremors, muscle spasms, numbness, tingling, visual changes, hearing loss, tinnitus, vertigo, dizziness, headache, photophobia, diplopia, blurred vision, eye redness, tearing, dry eyes, epistaxis, hemoptysis, cough, sputum production, hematuria, dysuria, frequency, urgency, nocturia, urinary retention, nocturnal enuresis, impotence, erectile dysfunction, dyspareunia, menorrhagia, irregular menses, galactorrhea, amenorrhea, weight gain, weight loss, fever, chills, night sweats, fatigue, weakness, malaise, joint pain, back pain, neck pain, shoulder pain, arm pain, hand pain, leg pain, foot pain, knee pain, ankle pain, hip pain, buttock pain, pelvic pain, right upper quadrant pain, left upper quadrant pain, right lower quadrant pain, le …
```

- unsupported entities (vs. transcript): abdominal pain, abdominal tenderness, ankle pain, arm pain, back pain, bleeding, blood in stool, blurred vision, bruising, cataract, chest pain, chills, conjunctivitis, constipation, cough, dental caries, diarrhea, dizziness, double vision, dry eyes
- incorrect diagnosis: cataract, conjunctivitis, dental caries, glaucoma, hernia, macular degeneration, optic neuritis, periodontal disease, retinal detachment, sinusitis, uveitis  ·  missing diagnosis: —
- incorrect medication: —  ·  missing medication: —
- dosage mismatch: —
- negation flips (vs. reference): pain
- unsupported numbers: 45
- missing information: {"symptom": ["murmur"], "medical_history": ["depression", "diabetes", "hypertension"], "investigation": ["bilirubin", "liver enzymes level", "physical examination", "vital signs"]}

## Hallucination example: `aci_bench_test_taskB_1_D2N096-virtassist`

*hallucination example*

ROUGE-L 8.6 · length ratio 3.30 · truncated True · degenerate False · hallucination 93.8 · negation-flip 0.0 · numerical consistency 100.0 · coverage 42.9

**Transcript (excerpt)**

```
[doctor] um , hi mrs. anderson . right ?
[patient] yeah . yes , doctor .
[doctor] what brings you here today ?
[patient] hi , doctor . um , i'm having this left shoulder pain lately , uh , and it's paining a lot .
[doctor] okay . all right . hey , dragon . i am seeing mrs. anderson , a 44-years-old female , uh , complaining to check the left shoulder pain . um , so how long how has this lasted ?
[patient] it's been a week , doctor . yeah .
[doctor] a week .
[patient] yeah .
[doctor] um , did you take any medication yourself ?
[patient] no , i did not take any pain medications . actually , i did . i did take a tylenol for two or three days , but then that did n't help at all . so , uh , the r …
```

**Reference note**

```
CC:

Left shoulder pain.

HPI:

Ms. Anderson is a 44-year-old female who presents today for an evaluation of the left shoulder. She states that she was in gymnastics 1 week ago. The pain has been present since that time. She has pain with any type of movement of her left shoulder. She had taken Tylenol for 2 to 3 days with no improvement in her symptoms.

She has a surgical history significant for prior left upper extremity surgery.

EXAM

Examination of the left shoulder shows pain with range of motion.

RESULTS

X-rays of the left shoulder, 3 views obtained on today's visit show no obvious signs of fracture.

PLAN

At this point, I discussed the diagnosis and treatment options with the patient. I have recommended taking ibuprofen 600 mg three times per day for one week. If the patient does not have relief from the ibuprofen she will take Aleve. The patient may also utilize ice or heat  …
```

**Generated note**

```
CHIEF COMPLAINT
Left shoulder pain.

HISTORY OF PRESENT ILLNESS

This is a 44-year-old female who comes in with left shoulder pain.  She states she has had this pain for about one week.  She denies taking any pain medications.  She has taken Tylenol for two to three days without relief.  She states she was in gymnastics class and fell onto her left shoulder.  She denies any history of trauma.  She denies any previous surgeries on her left shoulder.  She denies any allergies to any medications.  She denies any history of smoking or alcohol abuse.  She denies any history of diabetes mellitus.  She denies any history of hypertension.  She denies any history of asthma.  She denies any history of chronic obstructive pulmonary disease.  She denies any history of heart disease.  She denies any history of kidney stones.  She denies any history of gallbladder disease.  She denies any history of liver disease.  She denies any history of thyroid problems.  She denies any history of fibromyalgia.  She denies any history of arthritis.  She denies any history of lupus.  She denies any history of r …
```

- unsupported entities (vs. transcript): abscess, allergic rhinitis, appendicitis, arrhythmia, arthritis, asthma, atrial fibrillation, breast pain, cellulitis, chest pain, cholecystitis, copd, coronary artery disease, cough, deep vein thrombosis, diabetes, diverticulitis, dysphagia, dyspnea, dysuria
- incorrect diagnosis: —  ·  missing diagnosis: —
- incorrect medication: —  ·  missing medication: ibuprofen, naproxen
- dosage mismatch: —
- negation flips (vs. reference): —
- unsupported numbers: —
- missing information: {"diagnosis": ["fracture"], "medication": ["ibuprofen", "naproxen"], "investigation": ["x-ray"]}

## Incorrect diagnosis example: `aci_bench_test_taskB_1_D2N113-aci`

*incorrect diagnosis example*

ROUGE-L 4.2 · length ratio 1.24 · truncated True · degenerate True · hallucination 90.7 · negation-flip 12.5 · numerical consistency 0.0 · coverage 52.9

**Transcript (excerpt)**

```
[doctor] hi jacqueline how are you doing today
[patient] i'm doing okay i'm just really anxious about my recent blood work that my pcp did and said that i have hepatitis c i'm just really surprised because i've been feeling fine
[doctor] okay so were you ever told in the past that you have hepatitis c
[patient] no never
[doctor] okay and do do you have any history like iv drug use known that you know or do you have any known to have any like hepatitis c positive partners
[patient] i mean like years ago i used to party a lot and even use iv drugs but i've been clean for over fifteen years now
[doctor] okay well very good you know congratulations on that that's that's a great great achievement …
```

**Reference note**

```
CHIEF COMPLAINT

Hepatitis C.

SOCIAL HISTORY

Patient reports personal history of intravenous drug use over 15 years ago. She is currently smoking 1-2 cigarettes per day, previously 1 to 1.5 packs per day. She also has a history of heavy alcohol use, but now drinks approximately 1 beer per day, more on the weekends.

FAMILY HISTORY

Patient reports family history significant for hypertension, diabetes, and depression.

REVIEW OF SYSTEMS

Constitutional: Reports fatigue.

All other systems were reviewed and are negative.

VITALS

Vitals look good today.

PHYSICAL EXAM

Constitutional
- General Appearance: in no apparent distress.

Respiratory
- Auscultation of Lungs: No wheezes, rales, or rhonchi.

Cardiovascular
- Auscultation of Heart: Regular rate. 2/6 systolic ejection murmur, unchanged.

Gastrointestinal
- Examination of Abdomen: No masses or tenderness. No hepatosplenomegaly.
- Aus …
```

**Generated note**

```
CHIEF COMPLAINT

The patient is a 45-year-old female who comes in for evaluation of her recent lab results which indicate she has hepatitis C.  She denies jaundice, wheezing, crackles, rhonchi, edema, dyspnea, orthopnea, palpitations, syncope, chest pain, abdominal pain, nausea, vomiting, diarrhea, constipation, hematochezia, melena, arthralgia, weakness, tremors, muscle spasms, numbness, tingling, visual changes, hearing loss, tinnitus, vertigo, dizziness, headache, photophobia, diplopia, blurred vision, eye redness, tearing, dry eyes, epistaxis, hemoptysis, cough, sputum production, hematuria, dysuria, frequency, urgency, nocturia, urinary retention, nocturnal enuresis, impotence, erectile dysfunction, dyspareunia, menorrhagia, irregular menses, galactorrhea, amenorrhea, weight gain, weight loss, fever, chills, night sweats, fatigue, weakness, malaise, joint pain, back pain, neck pain, shoulder pain, arm pain, hand pain, leg pain, foot pain, knee pain, ankle pain, hip pain, buttock pain, pelvic pain, right upper quadrant pain, left upper quadrant pain, right lower quadrant pain, le …
```

- unsupported entities (vs. transcript): abdominal pain, abdominal tenderness, ankle pain, arm pain, back pain, bleeding, blood in stool, blurred vision, bruising, cataract, chest pain, chills, conjunctivitis, constipation, cough, dental caries, diarrhea, dizziness, double vision, dry eyes
- incorrect diagnosis: cataract, conjunctivitis, dental caries, glaucoma, hernia, macular degeneration, optic neuritis, periodontal disease, retinal detachment, sinusitis, uveitis  ·  missing diagnosis: —
- incorrect medication: —  ·  missing medication: —
- dosage mismatch: —
- negation flips (vs. reference): pain
- unsupported numbers: 45
- missing information: {"symptom": ["murmur"], "medical_history": ["depression", "diabetes", "hypertension"], "investigation": ["bilirubin", "liver enzymes level", "physical examination", "vital signs"]}

## Incorrect medication / dosage example: `aci_bench_test_taskB_1_D2N122-aci`

*incorrect medication / dosage example*

ROUGE-L 10.0 · length ratio 1.61 · truncated True · degenerate True · hallucination 60.9 · negation-flip 20.0 · numerical consistency 50.0 · coverage 27.8

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

The patient states that she has had a cough for approximately three months.  She denies any fevers, chills, sputum production, hemoptysis, pleuritic chest pain, or palpable masses.  She does deny any shortness of breath.  She has a history of chronic obstructive pulmonary disease, hypertension, hyperlipidemia, and osteoarthritis.  She has a history of smoking.  She has a history of rheumatoid arthritis.  She has a history of breast cancer in her mother.  She has a history of lung cancer in her father.  She has a history of pneumonia.  She has a history of bronchitis.  She has a history of asthma.  She has a history of sinusitis.  She has a history of allergies.  She has a history of thyroid nodules.  She has a history of thyroid cancer.  She has a history of thyroid surgery.  She has a history of thyroid medication.  She has a history of thyroid hormone replacement.  She has a history of thyroid nodules.  She has a history of thyroid cancer. …
```

- unsupported entities (vs. transcript): allergic rhinitis, asthma, chest pain, chills, copd, estrogen, hemoptysis, hyperlipidemia, hypertension, levothyroxine, osteoarthritis, sinusitis, sputum, thyroid nodule
- incorrect diagnosis: —  ·  missing diagnosis: —
- incorrect medication: estrogen, levothyroxine  ·  missing medication: methotrexate
- dosage mismatch: —
- negation flips (vs. reference): pneumonia
- unsupported numbers: 62
- missing information: {"symptom": ["crepitus", "edema", "lump", "murmur"], "medication": ["methotrexate"], "investigation": ["blood pressure measurement", "ct scan", "heart rate measurement", "oxygen saturation", "physical examination", "pulmonary function test"]}

## Negation error example: `aci_bench_test_taskB_1_D2N101-virtscribe`

*negation error example*

ROUGE-L 11.7 · length ratio 1.24 · truncated True · degenerate True · hallucination 0.0 · negation-flip 50.0 · numerical consistency 100.0 · coverage 66.7

**Transcript (excerpt)**

```
[doctor] patient is julia jones , date of birth 5/16/1996 . she is a new breast reduction consult . hello , how are you doing today ? i'm dr. gonzalez . it's nice to meet you .
[patient] nice to meet you , ma'am . how are you ?
[doctor] i'm doing good , thank you . so you're here to discuss a breast reduction , correct ?
[patient] yes . that's right .
[doctor] okay . perfect . let me just get logged in , here . have you met with anyone before about a breast reduction ?
[patient] no , i have n't .
[doctor] okay . and how long have you been considering this ?
[patient] it's probably been about six or seven years . but i mean , it's always been in the back of my mind .
[doctor] well , i perform …
```

**Reference note**

```
CHIEF COMPLAINT

Macromastia.

HISTORY OF PRESENT ILLNESS

Julia Jones is a 25-year-old female who presents for evaluation of macromastia.

Ms. Jones reports this is her first visit in regard to a breast reduction and has been interested in getting a breast reduction for approximately 7 years. Currently she has Blue Cross Blue Shield insurance but will be added to her spouse’s insurance plan in 07/2021.

Current breast size is a G cup, although she primarily wears a 34 E sports bra for comfort, and desired breast size is a B or C cup. No prior pregnancies, potentially planning on pregnancies in the future, and unsure of breast feeding.

The patient endorses back and neck pain since she was in high school. Her back and neck pain has been managed by a chiropractor for a few years. She reports weight loss of 10 pounds over the past few months and would like to lose an additional 20 pounds.
 …
```

**Generated note**

```
CHIEF COMPLAINT
The patient is Julia Jones, a 25-year-old female, presents for evaluation of breast reduction.

HISTORY OF PRESENT ILLNESS
The patient states that she has had significant back pain for several years.  She denies any history of breast cancer.  She has had a mammogram.  She has had a history of migraines.  She has had a history of nausea and vomiting.  She denies any history of breast pain.  She denies any history of lymphadenopathy.  She denies any history of rash.  She denies any history of sweating.  She denies any history of numbness or tingling.  She denies any history of neck pain.  She denies any history of nausea or vomiting.  She denies any history of breast pain.  She denies any history of lymphadenopathy.  She denies any history of rash.  She denies any history of sweating.  She denies any history of numbness or tingling.  She denies any history of neck pain.  She denies any history of nausea or vomiting.  She denies any history of breast pain.  She denies any history of lymphadenopathy.  She denies any history of rash.  She denies any history of sweating.  S …
```

- unsupported entities (vs. transcript): —
- incorrect diagnosis: —  ·  missing diagnosis: —
- incorrect medication: —  ·  missing medication: propranolol
- dosage mismatch: —
- negation flips (vs. reference): neck pain, numbness, rash, sweating
- unsupported numbers: —
- missing information: {"symptom": ["pain", "weight loss"], "medication": ["propranolol"], "investigation": ["weight measurement"]}

## Numerical error example: `aci_bench_test_taskB_1_D2N106-aci`

*numerical error example*

ROUGE-L 21.3 · length ratio 1.62 · truncated False · degenerate True · hallucination 44.1 · negation-flip 8.3 · numerical consistency 29.4 · coverage 94.4

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

The patient is a 45-year-old male who comes in for evaluation of his respiratory status.  He has been having difficulty breathing for the past few months.  He denies any history of angioedema, rash, nausea, vomiting, diarrhea, throat swelling, anxiety, edema, wheezing, or history of allergies.  He has a history of asthma and allergic rhinitis.  He has been treated with nebulizer treatments, inhalers, and albuterol in the past.  He has been taking montelukast and allergy shots.  He has had allergy testing done in the past.  He has had chest X-rays and pulmonary function tests done in the past.  He has been referred to an allergist in the past.  He has been on conservative management in the past.

HISTORY OF PRESENT ILLNESS

The patient is a 45-year-old male who comes in for evaluation of his respiratory status.  He has been having difficulty breathing for the past few months.  He denies any history of angioedema, rash, nausea, vomiting, diarrhea, throat swelling, anxiety, edema, wheezing, or history of allergies.  He has a history of asthma and allergic rhinitis.  He  …
```

- unsupported entities (vs. transcript): abdominal tenderness, anxiety, blood pressure measurement, conjunctivitis, cyanosis, diagnostic workup, erythema, hernia, jaundice, lymphadenopathy, pain, pallor, respiratory rate, rhinorrhea, varicose veins
- incorrect diagnosis: —  ·  missing diagnosis: —
- incorrect medication: —  ·  missing medication: —
- dosage mismatch: —
- negation flips (vs. reference): diarrhea
- unsupported numbers: 130, 130/80, 18, 4, 5, 6, 7, 78, 8, 80, 9, 98
- missing information: {"symptom": ["flare"]}

## Missing information example: `aci_bench_test_taskB_1_D2N111-aci`

*missing information example*

ROUGE-L 8.6 · length ratio 1.35 · truncated True · degenerate True · hallucination 69.2 · negation-flip 50.0 · numerical consistency 50.0 · coverage 15.4

**Transcript (excerpt)**

```
[doctor] hey william so i see that you injured your knee could you tell me a bit about what happened
[patient] yeah i thought it was a good idea to go to the trampoline park with my wife and heard a snap and instant pain when i was on the trampoline
[doctor] okay alright and so do do you go to the trampoline park often
[patient] i do n't and i think that's the issue
[doctor] okay so this is the first time you'd ever done something like that
[patient] yes
[doctor] okay alright i just wan na get like a few more details do you like work out regularly was this for fun or for like an exercise class
[patient] no it's just for fun
[doctor] okay and do you have like a regular exercise regimen at all …
```

**Reference note**

```
CHIEF COMPLAINT

Right knee injury.

HISTORY OF PRESENT ILLNESS

William Russell is a pleasant 57-year-old male who presents to the clinic today for the evaluation of a right knee injury. He has a past medical history significant for hypertension and type 2 diabetes.

Approximately 1 week ago, the patient sustained an injury to his right knee while at a trampoline park. He explains that he was jumping on a trampoline when he heard a snap, followed by instant pain in the lateral aspect of his knee. This is not a common activity for him, and he admits that he is inconsistent with exercise. As far as treatment, he has been elevating his knee and taking Tylenol without significant relief of his pain. He has not tried applying heat or ice to the area.

In terms of his hypertension, the patient admits that he did not purchase a blood pressure cuff as previously recommended. While he does not m …
```

**Generated note**

```
CHIEF COMPLAINT

The patient is a 62-year-old male who comes in today complaining of right knee pain after he had a fall onto his right knee while jumping on a trampoline.  He has had pain for one week and denies any fever, chills, redness, warmth, swelling, or deformity.  He denies any recent trauma except for the above incident.  He denies any recent surgeries.  He denies any allergies.  He denies any history of bleeding disorders.  He denies any history of cancer.  He denies any history of kidney disease.  He denies any history of liver disease.  He denies any history of lung disease.  He denies any history of neurological disease.  He denies any history of psychiatric illness.  He denies any history of endocrine disorder.  He denies any history of musculoskeletal disorder.  He denies any history of gastrointestinal disorder.  He denies any history of genitourinary disorder.  He denies any history of hematologic disorder.  He denies any history of dermatological disorder.  He denies any history of ophthalmologic disorder.  He denies any history of ENT disorder.  He denies any hist …
```

- unsupported entities (vs. transcript): allergic rhinitis, bleeding disorder, cancer, chills, chronic kidney disease, erythema, falls, fever, warmth
- incorrect diagnosis: —  ·  missing diagnosis: diabetes, hypertension, strain, type 2 diabetes
- incorrect medication: —  ·  missing medication: acetaminophen, lisinopril, meloxicam, metformin
- dosage mismatch: —
- negation flips (vs. reference): edema, trauma
- unsupported numbers: 62
- missing information: {"symptom": ["bruising", "joint swelling", "murmur"], "medical_history": ["hypertension", "type 2 diabetes"], "diagnosis": ["diabetes", "fracture", "strain"], "medication": ["acetaminophen", "lisinopril", "meloxicam", "metformin"], "investigation": ["blood glucose", "blood pressure measurement", "diagnostic workup", "echocardiogram", "hemoglobin a1c", "home monitoring"]}

## Degenerate output example: `aci_bench_test_taskB_1_D2N102-virtscribe`

*degenerate output example*

ROUGE-L 6.3 · length ratio 1.28 · truncated True · degenerate True · hallucination 94.0 · negation-flip 0.0 · numerical consistency 50.0 · coverage 25.0

**Transcript (excerpt)**

```
[doctor] kelly wood . date of birth , february 15th , 1979 . established patient here for renal ultrasound because of hematuria . urine dipstick today . negative for leukocytes , nitrates , protein , ketone , bilirubin and glucose . color yellow and clear , urobilinogen 0.2 , ph 5.5 and specific gravity 1.020 . there is a trace amount of blood in the urine and intact . renal ultrasound impression . right kidney is 10 cm in length by five centimeter wide . there are no stones , masses or hydronephrosis . the left kidney is 10.8 centimeters in length and five centimeters wide . there is a six millimeter left renal stone non-obstructing . 533 milliliters pre-void and 0 milliliters post-void . h …
```

**Reference note**

```
CHIEF COMPLAINT

Hematuria.
Chronic urolithiasis.

HISTORY OF PRESENT ILLNESS

Mrs. Kelly Wood is a 41-year-old female established patient with chronic urolithiasis who returns in follow up for renal ultrasound due to hematuria.

The patient reports having intermittent episodes of gross hematuria over the past several months. she states she had multiple voids in one day where the color of her urine was like cherry Kool-Aid last week; then passed 2 small stone like structures. Pain at the time was 8 out of 10 on a scale of 10. she currently denies any flank pain.

CURRENT MEDICATIONS

Alavert 10 mg tablet once daily.

ALLERGIES

No known drug allergies.

PHYSICAL EXAM

Genitourinary: Normal vaginal exam.

RESULTS

Renal Ultrasound
Impression: Right kidney is 10 cm in length by 5 cm wide. There are no stones, masses, or hydronephrosis. The left kidney is 10.8 cm in length and 5 cm wide. Th …
```

**Generated note**

```
CHIEF COMPLAINT

Mrs. Wood is seen for evaluation of hematuria.

HISTORY OF PRESENT ILLNESS

The patient is a 25-year-old female who comes in for evaluation of hematuria.  She states she has been having hematuria for the past 6 weeks.  She denies dysuria, frequency, urgency, flank pain, abdominal pain, fever, chills, nausea, vomiting, diarrhea, constipation, arthralgias, joint pains, muscle weakness, visual changes, hearing loss, tinnitus, vertigo, syncope, chest pain, palpitations, shortness of breath, orthopnea, paroxysmal nocturnal dyspnea, edema, weight gain, weight loss, night sweats, fatigue, malaise, headache, photophobia, phonophobia, confusion, memory loss, tremors, rigidity, gait disturbances, difficulty walking, difficulty with speech, difficulty swallowing, hoarseness, wheezing, cough, sputum production, hemoptysis, hematemesis, melena, hematochezia, pruritus, itching, rash, hives, urticaria, erythema nodosum, purpura, petechiae, ecchymosis, bruising, joint swelling, joint effusion, joint deformity, joint contractures, joint laxity, joint instability, joint crepitus, join …
```

- unsupported entities (vs. transcript): blood in stool, blurred vision, bruising, chest pain, chills, confusion, constipation, cough, crepitus, diarrhea, difficulty walking, dizziness, dysphagia, dyspnea, dysuria, edema, erythema, fatigue, fever, headache
- incorrect diagnosis: —  ·  missing diagnosis: kidney stones
- incorrect medication: —  ·  missing medication: —
- dosage mismatch: —
- negation flips (vs. reference): —
- unsupported numbers: 25
- missing information: {"medical_history": ["allergic rhinitis", "kidney stones"], "diagnosis": ["hydronephrosis"], "investigation": ["bilirubin", "blood glucose", "ultrasound", "urinalysis", "weight measurement", "white blood cell count"]}

# Split: aci_bench_test_taskC_2

## Best ROUGE-L: `aci_bench_test_taskC_2_D2N128-virtassist`

*highest ROUGE-L in the split*

ROUGE-L 31.3 · length ratio 1.72 · truncated True · degenerate True · hallucination 41.9 · negation-flip 13.3 · numerical consistency 42.9 · coverage 94.4

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

The patient is a 49-year-old female who comes in for followup of her chronic problems.  She states that her osteoarthritis has been flaring up a little bit lately, particularly in her elbows and it has been bothering her.  She denies any other joint pain.  She has had some numbness and tingling in her hands when she types for long periods of time.  She has had a history of gout.  Her last episode was about three months ago.  She has had some inflammation of her toe.  She has not had any other issues with that.  The medication has controlled it and she has not seen a flareup since.  She has had some psoriasis.  That has been under control.  She has had some clobetasol for her scalp.  It has been doing a lot better.  She has had some edema and inflammation of her right olecranon.  There is some tenderness and an effusion.  She has pain to palpation of the olecranon bursa and pain with pronation and supination.  She has pain with flexion and extension of the right arm.  She has some stiffness.  She has no lower extremity edema.  She has had some autoimmune panel done.   …
```

- unsupported entities (vs. transcript): blood pressure measurement, chronic pain, crackles, crp, erythema, esr, heart rate measurement, murmur, numbness, oxygen saturation, respiratory rate, rhonchi, wheezing
- incorrect diagnosis: chronic pain  ·  missing diagnosis: —
- incorrect medication: —  ·  missing medication: hydrocortisone cream
- dosage mismatch: —
- negation flips (vs. reference): flare, joint pain
- unsupported numbers: 130, 130/80, 18, 4, 78, 80, 98.2, 99
- missing information: {"medication": ["hydrocortisone cream"]}

## Worst ROUGE-L: `aci_bench_test_taskC_2_D2N146-aci`

*lowest ROUGE-L in the split*

ROUGE-L 4.0 · length ratio 0.88 · truncated True · degenerate True · hallucination 87.5 · negation-flip 75.0 · numerical consistency 0.0 · coverage 22.2

**Transcript (excerpt)**

```
[doctor] hey good morning bobby how are you
[patient] i'm doing okay i as you're aware doctor miller sent me over for this pain in my belly that i've had for several weeks they did he did an ultrasound and and said i had gallstones and they recommended i stay several way from some high fat food but i'm just still having a lot of pain and he referred me to you
[doctor] alright well i'm i'm sorry to hear that you're having pain but i i'm glad that he sent you over to see me i wan na talk a little bit more about that pain can you describe the kind of pain that you feel
[patient] well it's it's on the right hand side of my belly it's it's right underneath my ribs and it feels like a a squeezing  …
```

**Reference note**

```
CHIEF COMPLAINT

Abdominal pain.

MEDICAL HISTORY

Patient reports history of type 2 diabetes.

SOCIAL HISTORY

Patient reports enjoying nature photography.

FAMILY HISTORY

Patient reports family history of cholelithiasis. Both of his parents have had cholecystectomies.

REVIEW OF SYSTEMS

Constitutional: Reports low-grade fevers.
Gastrointestinal: Reports right-sided abdominal pain and nausea. Denies vomiting.

VITALS

Blood Pressure: 128/88 mmHg.
Respiratory Rate: 16 breaths per minute.
Heart Rate: 68 beats per minute.
Oxygen Saturation: 99% on room air.
Body Temperature: Afebrile.

PHYSICAL EXAM

Respiratory
- Auscultation of Lungs: Clear and equal bilaterally.

Cardiovascular
- Auscultation of Heart: Regular rate and rhythm. No ectopic beats. No murmurs, clicks, or rubs.

Gastrointestinal
- Examination of Abdomen: Soft, nondistended abdomen. Positive slight guarding to the right upp …
```

**Generated note**

```
CHIEF COMPLAINT
The patient is a 62-year-old male who presents with chronic right upper quadrant pain for several weeks.

HISTORY OF PRESENT ILLNESS
The patient states that he has had chronic right upper quadrant pain for several weeks.  He denies any recent fevers, chills, nausea, vomiting, dysuria, frequency, urgency, hematuria, hematochezia, melena, arthralgias, joint pains, muscle weakness, visual changes, hearing changes, syncope, palpitations, chest pain, shortness of breath, orthopnea, paroxysmal nocturnal dyspnea, PND, edema, weight gain, weight loss, fatigue, malaise, confusion, memory loss, personality change, tremors, rigidity, bradykinesia, akathisia, gait disturbances, diplopia, photophobia, headache, neck stiffness, rash, pruritus, urticaria, wheezing, cough, sputum production, pleuritic chest pain, dysphagia, odynophagia, hoarseness, dysarthria, dysphonia, hemiparesis, hemiplegia, aphasia, apraxia, syncope, palpitations, chest pain, shortness of breath, orthopnea, PND, edema, weight gain, weight loss, fatigue, malaise, confusion, memory loss, personality change, tremor …
```

- unsupported entities (vs. transcript): blood in stool, blurred vision, chest pain, chills, confusion, cough, difficulty walking, double vision, dysphagia, dyspnea, dysuria, edema, fatigue, headache, hematuria, hoarseness, itching, joint pain, memory loss, neck pain
- incorrect diagnosis: —  ·  missing diagnosis: cholecystitis, diabetes, type 2 diabetes
- incorrect medication: —  ·  missing medication: —
- dosage mismatch: —
- negation flips (vs. reference): fever, nausea, pain
- unsupported numbers: 62
- missing information: {"symptom": ["abdominal pain", "crepitus", "erythema", "murmur"], "medical_history": ["type 2 diabetes"], "diagnosis": ["cholecystitis", "diabetes"], "investigation": ["blood pressure measurement", "heart rate measurement", "oxygen saturation", "physical examination", "respiratory rate", "temperature measurement"]}

## Hallucination example: `aci_bench_test_taskC_2_D2N156-aci`

*hallucination example*

ROUGE-L 7.3 · length ratio 1.48 · truncated True · degenerate False · hallucination 88.3 · negation-flip 20.0 · numerical consistency 50.0 · coverage 18.5

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

The patient is a 62-year-old female who comes in for a followup appointment after she has had an inferior STEMi.  She has had a history of coronary artery disease, hypertension, diabetes mellitus type II, and has had a previous myocardial infarction.  She has had a recent admission for an inferior STEMi and has had placement of a new stent.  She has had a history of falls, dyspnea, orthopnea, paroxysmal nocturnal dyspnea, orthostatic hypotension, bilateral lower extremity edema, and a history of atrial fibrillation.  She has had a history of hypertension, hyperlipidemia, and diabetes mellitus type II.  She has had a history of smoking and has had a history of alcohol abuse.  She has had a history of allergies to penicillin and sulfa.  She has had a history of chronic obstructive pulmonary disease.  She has had a history of asthma.  She has had a history of gastroesophageal reflux disease.  She has had a history of anxiety disorder.  She has had a history of depression.  She has had a history of osteoarthritis.  She has had a history of fibromyalgia.  She has had a hi …
```

- unsupported entities (vs. transcript): allergic rhinitis, anxiety, asthma, atrial fibrillation, benign prostatic hyperplasia, brain tumor, breast cancer, cancer, colon cancer, copd, deep vein thrombosis, dementia, depression, diverticulitis, esophagitis, fibromyalgia, gastritis, gerd, hernia, hyperlipidemia
- incorrect diagnosis: —  ·  missing diagnosis: heart failure, mitral regurgitation, type 2 diabetes
- incorrect medication: —  ·  missing medication: aspirin, atorvastatin, furosemide, lisinopril, metformin, metoprolol, spironolactone, ticagrelor
- dosage mismatch: —
- negation flips (vs. reference): dyspnea
- unsupported numbers: 62
- missing information: {"symptom": ["chest pain", "murmur"], "diagnosis": ["heart failure", "intracranial hemorrhage", "mitral regurgitation", "type 2 diabetes"], "medication": ["aspirin", "atorvastatin", "furosemide", "lisinopril", "metformin", "metoprolol"], "investigation": ["blood glucose", "blood pressure measurement", "blood work", "echocardiogram", "electrocardiogram", "heart rate measurement"]}

## Incorrect diagnosis example: `aci_bench_test_taskC_2_D2N128-virtassist`

*incorrect diagnosis example*

ROUGE-L 31.3 · length ratio 1.72 · truncated True · degenerate True · hallucination 41.9 · negation-flip 13.3 · numerical consistency 42.9 · coverage 94.4

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

The patient is a 49-year-old female who comes in for followup of her chronic problems.  She states that her osteoarthritis has been flaring up a little bit lately, particularly in her elbows and it has been bothering her.  She denies any other joint pain.  She has had some numbness and tingling in her hands when she types for long periods of time.  She has had a history of gout.  Her last episode was about three months ago.  She has had some inflammation of her toe.  She has not had any other issues with that.  The medication has controlled it and she has not seen a flareup since.  She has had some psoriasis.  That has been under control.  She has had some clobetasol for her scalp.  It has been doing a lot better.  She has had some edema and inflammation of her right olecranon.  There is some tenderness and an effusion.  She has pain to palpation of the olecranon bursa and pain with pronation and supination.  She has pain with flexion and extension of the right arm.  She has some stiffness.  She has no lower extremity edema.  She has had some autoimmune panel done.   …
```

- unsupported entities (vs. transcript): blood pressure measurement, chronic pain, crackles, crp, erythema, esr, heart rate measurement, murmur, numbness, oxygen saturation, respiratory rate, rhonchi, wheezing
- incorrect diagnosis: chronic pain  ·  missing diagnosis: —
- incorrect medication: —  ·  missing medication: hydrocortisone cream
- dosage mismatch: —
- negation flips (vs. reference): flare, joint pain
- unsupported numbers: 130, 130/80, 18, 4, 78, 80, 98.2, 99
- missing information: {"medication": ["hydrocortisone cream"]}

## Incorrect medication / dosage example: `aci_bench_test_taskC_2_D2N131-virtassist`

*incorrect medication / dosage example*

ROUGE-L 27.3 · length ratio 1.58 · truncated False · degenerate False · hallucination 26.3 · negation-flip 0.0 · numerical consistency 30.8 · coverage 68.2

**Transcript (excerpt)**

```
hi , susan , how are you ?
[patient] good . how are you ?
[doctor] good . are you ready to get started ?
[patient] yes , i am .
[doctor] so , susan is a 26-year-old female here for a high blood pressure check . susan , what's going on with your blood pressure ?
[patient] so , i've always struggled with , um , high blood pressure , but it's seeming to get really out of control lately . so , i wanted to come in and see if there's any type of new medication i can be on to help it get steady or if there is diet restrictions i should take , um , things like that .
[doctor] okay . so , i know that we've had you on the norvasc and we had to increase your dose , so you're on 10 milligrams a day now  …
```

**Reference note**

```
CHIEF COMPLAINT

High blood pressure check.

HISTORY OF PRESENT ILLNESS

Ms. Susan Watson is a 26-year-old female who presents to the clinic today for a high blood pressure check.

The patient reports she has always struggled with high blood pressure, but it is seems out of control recently. She notes that she has interest in new medication or diet changes to help. She is currently on Norvasc 10 mg daily. Her blood pressure at home has been over 150. She notes she has had some headaches, but she is unsure if it is due to stress at work or her high blood pressure. She denies chest pain or shortness of breath.

The patient underwent a kidney transplant a few years ago, and everything is going well. She is taking all of her immunosuppression medication.

REVIEW OF SYSTEMS

• Cardiovascular: Denies chest pain or dyspnea on exertion.
• Respiratory: Denies shortness of breath
• Neurological: E …
```

**Generated note**

```
CHIEF COMPLAINT

The patient is a 26-year-old female who comes in for a high blood pressure check.

HISTORY OF PRESENT ILLNESS

Susan is a 26-year-old female who has been having difficulty managing her hypertension.  She has had hypertension for several years and has had a kidney transplant.  She denies any chest pain, shortness of breath, or lower extremity edema.  She does have some headaches.  She has been on Norvasc 10 mg daily and Coreg 6.25 mg BID.  Her blood pressures have been elevated at home.  She has had some stress at work.  She has had a kidney transplant a few years ago.  She is on immunosuppressive therapy.  She has been compliant with her medications.

REVIEW OF SYSTEMS

CONSTITUTIONAL: Negative.
NECK: Supple.
HEENT: Negative.
CARDIOVASCULAR: Irregular rate and rhythm, S2, grade 2/6 systolic ejection murmur.
RESPIRATORY: Negative.
GASTROINTESTINAL: Negative.
GENITOURINARY: Negative.
MUSCULOSKELETAL: Negative.
SKIN: Negative.
LYMPHATIC: Negative.

PHYSICAL EXAM

GENERAL: The patient appears comfortable and in no apparent distress.
NECK: Supple.
HEART: Irregular rate an …
```

- unsupported entities (vs. transcript): electrocardiogram, immunosuppressant, obesity, pain, potassium level
- incorrect diagnosis: obesity  ·  missing diagnosis: —
- incorrect medication: immunosuppressant  ·  missing medication: —
- dosage mismatch: [{"drug": "carvedilol", "predicted": "6.25 mg", "source": ["25 mg", "25 milligrams"]}]
- negation flips (vs. reference): —
- unsupported numbers: 0.9, 1, 3, 4, 5, 6.25, 7, 8, 9
- missing information: {"symptom": ["crackles", "dyspnea on exertion", "lymphadenopathy", "rhonchi", "wheezing"], "investigation": ["diagnostic workup", "home monitoring"]}

## Negation error example: `aci_bench_test_taskC_2_D2N153-aci`

*negation error example*

ROUGE-L 7.7 · length ratio 1.86 · truncated True · degenerate True · hallucination 27.3 · negation-flip 70.0 · numerical consistency 50.0 · coverage 55.6

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

The patient is a 45-year-old male who comes in with complaints of his right knee pain and locking sensation.

HISTORY OF PRESENT ILLNESS

The patient states he has had right knee pain and locking sensation for approximately 2.5 weeks.  He denies any history of trauma, crepitus, tingling, numbness, edema, or joint swelling.  He has had past surgeries including a previous right knee surgery.  He has also had past treatments including meloxicam and ibuprofen.  He has had past referrals and physical therapy.  He has had past heat and ice treatment.  He has had past rest and activity modifications.  He has had past medication management.  He has had past surgical interventions.  He has had past imaging studies.  He has had past consultations with orthopedic surgeons.  He has had past consultations with primary care physicians.  He has had past consultations with physical therapists.  He has had past consultations with occupational therapists.  He has had past consultations with podiatrists.  He has had past consultations with rheumatologists.  He has had past consultation …
```

- unsupported entities (vs. transcript): imaging, joint instability, knee pain
- incorrect diagnosis: —  ·  missing diagnosis: strain
- incorrect medication: —  ·  missing medication: —
- dosage mismatch: —
- negation flips (vs. reference): crepitus, edema, joint swelling, knee pain, numbness, tingling, trauma
- unsupported numbers: 45
- missing information: {"symptom": ["pain"], "medical_history": ["fracture"], "diagnosis": ["dislocation", "strain"], "investigation": ["heart rate measurement", "mri", "physical examination", "x-ray"]}

## Numerical error example: `aci_bench_test_taskC_2_D2N136-virtassist`

*numerical error example*

ROUGE-L 28.1 · length ratio 1.05 · truncated False · degenerate False · hallucination 29.4 · negation-flip 0.0 · numerical consistency 20.0 · coverage 65.6

**Transcript (excerpt)**

```
[doctor] hi janet , how are you ?
[patient] good , how are you ?
[doctor] i'm good . uh , are you ready to get started ?
[patient] yes .
[doctor] okay . so , janet is a 33-year-old female , here for some , some joint paint . what , what joint's been bothering you , janet ?
[patient] it's been mostly , um , my knees , actually . i've been doing more stair type workouts , which i thought was , you know , building muscle , uh , on my knees and supposed to help .
[doctor] mm-hmm .
[patient] but in turn it , it really has n't , so my knees have been really bothering me .
[doctor] okay . all right . and is it one knee versus the other ? or both equally ?
[patient] it's both equally .
[doctor] okay …
```

**Reference note**

```
CHIEF COMPLAINT

Joint pain.

HISTORY OF PRESENT ILLNESS

Ms. Janet Sullivan is a 33-year-old female who presents to the clinic today for evaluation of joint pain.

She localizes the joint pain to her bilateral knees. The patient reports she has been doing stair workouts, which she thought was building muscle on her knees. She denies any pins and needles in her feet or swelling in her legs. The patient notes that she would look out for those symptoms because she has diabetes. She denies any fever or chills. She denies any nausea or vomiting. The patient denies any chest pain or shortness of breath.

She notes she had a right shoulder rotator cuff repair about 2 years ago, but she has not had any problems since that point.

She reports that her diabetes are well-controlled.

The patient does have high blood pressure but she monitors it and takes Norvasc 5 mg a day. She notes her blood pre …
```

**Generated note**

```
CHIEF COMPLAINT

Joint pain, left knee.

HISTORY OF PRESENT ILLNESS

The patient is a 33-year-old female who presents to the office complaining of bilateral knee pain.  She denies any history of trauma.  She states she has had bilateral knee pain for several months.  She denies any history of fever, chills, nausea, vomiting, chest pain, shortness of breath, or palpitations.  She has a history of diabetes mellitus, hypertension, and status post right shoulder rotator cuff repair.  She denies any history of thyroid nodules.  She takes Norvasc 5mg daily, Meloxicam 15mg daily, Metformin 500mg BID, and Amlodipine.  She denies any history of recent surgeries.  She denies any history of recent hospitalizations.  She denies any history of allergies.  She denies any history of smoking.  She denies any history of alcohol abuse.  She denies any history of illicit drug use.

REVIEW OF SYSTEMS

CONSTITUTIONAL: Negative.
HEENT: Negative.
NECK: Supple.
LYMPH: Negative.
RESPIRATORY: Negative.
CARDIOVASCULAR: Negative.
GASTROINTESTINAL: Negative.
GENITOURINARY: Negative.
MUSCULOSKELETAL: Positive for …
```

- unsupported entities (vs. transcript): allergic rhinitis, cortisol level, creatinine, hemoglobin level, joint swelling, liver enzymes level, palpitations, substance use disorder, thyroid function test, trauma
- incorrect diagnosis: —  ·  missing diagnosis: strain
- incorrect medication: —  ·  missing medication: —
- dosage mismatch: —
- negation flips (vs. reference): —
- unsupported numbers: 0.9, 10, 11, 12, 13, 13/85, 14, 140, 20, 22, 22/20, 3, 50, 6, 6.2
- missing information: {"symptom": ["crackles", "numbness", "rhonchi", "wheezing"], "diagnosis": ["dislocation", "fracture", "strain"], "investigation": ["autoimmune panel", "diagnostic workup", "home monitoring", "physical examination"]}

## Missing information example: `aci_bench_test_taskC_2_D2N163-aci`

*missing information example*

ROUGE-L 5.1 · length ratio 2.61 · truncated True · degenerate True · hallucination 95.8 · negation-flip 0.0 · numerical consistency 100.0 · coverage 11.1

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

The patient is a 17-year-old female who comes in for evaluation of her newly diagnosed hypercholesterolemia.

HISTORY OF PRESENT ILLNESS

The patient is a 17-year-old female who comes in for evaluation of her newly diagnosed hypercholesterolemia.  She has no significant past medical history.  She denies any history of hypertension, diabetes mellitus, or thyroid disorders.  She denies any history of smoking or alcohol abuse.  She denies any history of allergies.  She denies any history of previous surgeries.  She denies any history of trauma.  She denies any history of hospitalizations.  She denies any history of chronic illnesses.  She denies any history of mental illness.  She denies any history of substance abuse.  She denies any history of sexual abuse.  She denies any history of domestic violence.  She denies any history of child abuse.  She denies any history of elder abuse.  She denies any history of neglect.  She denies any history of emotional abuse.  She denies any history of physical abuse.  She denies any history of psychological abuse.  She denies any his …
```

- unsupported entities (vs. transcript): allergic rhinitis, appendicitis, cancer, celiac disease, cholecystitis, diabetes, diverticulitis, drug allergy, esophagitis, gastritis, gastroenteritis, hepatitis, hypertension, inflammatory bowel disease, irritable bowel syndrome, kidney stones, lactose intolerance, pancreatitis, peptic ulcer disease, sexually transmitted infection
- incorrect diagnosis: —  ·  missing diagnosis: myocardial infarction
- incorrect medication: —  ·  missing medication: —
- dosage mismatch: —
- negation flips (vs. reference): —
- unsupported numbers: —
- missing information: {"symptom": ["murmur"], "medical_history": ["myocardial infarction"], "investigation": ["blood pressure measurement", "genetic testing", "hemoglobin a1c", "lipid panel", "metabolic panel", "physical examination"]}

## Degenerate output example: `aci_bench_test_taskC_2_D2N146-aci`

*degenerate output example*

ROUGE-L 4.0 · length ratio 0.88 · truncated True · degenerate True · hallucination 87.5 · negation-flip 75.0 · numerical consistency 0.0 · coverage 22.2

**Transcript (excerpt)**

```
[doctor] hey good morning bobby how are you
[patient] i'm doing okay i as you're aware doctor miller sent me over for this pain in my belly that i've had for several weeks they did he did an ultrasound and and said i had gallstones and they recommended i stay several way from some high fat food but i'm just still having a lot of pain and he referred me to you
[doctor] alright well i'm i'm sorry to hear that you're having pain but i i'm glad that he sent you over to see me i wan na talk a little bit more about that pain can you describe the kind of pain that you feel
[patient] well it's it's on the right hand side of my belly it's it's right underneath my ribs and it feels like a a squeezing  …
```

**Reference note**

```
CHIEF COMPLAINT

Abdominal pain.

MEDICAL HISTORY

Patient reports history of type 2 diabetes.

SOCIAL HISTORY

Patient reports enjoying nature photography.

FAMILY HISTORY

Patient reports family history of cholelithiasis. Both of his parents have had cholecystectomies.

REVIEW OF SYSTEMS

Constitutional: Reports low-grade fevers.
Gastrointestinal: Reports right-sided abdominal pain and nausea. Denies vomiting.

VITALS

Blood Pressure: 128/88 mmHg.
Respiratory Rate: 16 breaths per minute.
Heart Rate: 68 beats per minute.
Oxygen Saturation: 99% on room air.
Body Temperature: Afebrile.

PHYSICAL EXAM

Respiratory
- Auscultation of Lungs: Clear and equal bilaterally.

Cardiovascular
- Auscultation of Heart: Regular rate and rhythm. No ectopic beats. No murmurs, clicks, or rubs.

Gastrointestinal
- Examination of Abdomen: Soft, nondistended abdomen. Positive slight guarding to the right upp …
```

**Generated note**

```
CHIEF COMPLAINT
The patient is a 62-year-old male who presents with chronic right upper quadrant pain for several weeks.

HISTORY OF PRESENT ILLNESS
The patient states that he has had chronic right upper quadrant pain for several weeks.  He denies any recent fevers, chills, nausea, vomiting, dysuria, frequency, urgency, hematuria, hematochezia, melena, arthralgias, joint pains, muscle weakness, visual changes, hearing changes, syncope, palpitations, chest pain, shortness of breath, orthopnea, paroxysmal nocturnal dyspnea, PND, edema, weight gain, weight loss, fatigue, malaise, confusion, memory loss, personality change, tremors, rigidity, bradykinesia, akathisia, gait disturbances, diplopia, photophobia, headache, neck stiffness, rash, pruritus, urticaria, wheezing, cough, sputum production, pleuritic chest pain, dysphagia, odynophagia, hoarseness, dysarthria, dysphonia, hemiparesis, hemiplegia, aphasia, apraxia, syncope, palpitations, chest pain, shortness of breath, orthopnea, PND, edema, weight gain, weight loss, fatigue, malaise, confusion, memory loss, personality change, tremor …
```

- unsupported entities (vs. transcript): blood in stool, blurred vision, chest pain, chills, confusion, cough, difficulty walking, double vision, dysphagia, dyspnea, dysuria, edema, fatigue, headache, hematuria, hoarseness, itching, joint pain, memory loss, neck pain
- incorrect diagnosis: —  ·  missing diagnosis: cholecystitis, diabetes, type 2 diabetes
- incorrect medication: —  ·  missing medication: —
- dosage mismatch: —
- negation flips (vs. reference): fever, nausea, pain
- unsupported numbers: 62
- missing information: {"symptom": ["abdominal pain", "crepitus", "erythema", "murmur"], "medical_history": ["type 2 diabetes"], "diagnosis": ["cholecystitis", "diabetes"], "investigation": ["blood pressure measurement", "heart rate measurement", "oxygen saturation", "physical examination", "respiratory rate", "temperature measurement"]}

# Split: aci_bench_test_taskC_3

## Best ROUGE-L: `aci_bench_test_taskC_3_D2N180-virtscribe`

*highest ROUGE-L in the split*

ROUGE-L 37.0 · length ratio 0.64 · truncated False · degenerate False · hallucination 4.3 · negation-flip 0.0 · numerical consistency 100.0 · coverage 75.0

**Transcript (excerpt)**

```
[doctor] patient shirley taylor . date of birth 5/4/1961 . mrn 0000123 . patient is a 60 year old right-handed female new patient referred by dr. jacob ward for evaluation of bilateral hand numbness and tingling . please note that i personally reviewed the ct brain with and without contrasting did 2/5/21 . uh , no metastatic disease . no acute intercranial abnormalities .
[doctor] hello ms. taylor . how are you doing this morning ?
[patient] hi dr . lopez . this weekend was a bit rough . i've had this numbness and tingling for a few weeks now .
[doctor] so , in both of your hands ?
[patient] yeah . ever since my car wreck last december when i broke them . well , once they heal , i mean , i n …
```

**Reference note**

```
CHIEF COMPLAINT

Upper extremity tingling

HISTORY OF PRESENT ILLNESS

The patient is a 60-year-old female referred today for evaluation of numbness and tingling.

The patient complains of numbness, tingling, and pain in both hands which began last December after she broke both wrists in an MVA and which has progressively worsened since then. She continues to wear a splint on the right wrist all the time and on the left only intermittently, which she states is because the right wrist was injured more severely in the MVA. The sensation radiates from the hands into the forearms and is equal bilaterally. The 4th and 5th fingers in the left hand and 3rd and 4th on the right-hand tingle. She states that her fingers are sore with palpation and seem weaker than before. Any exertion exacerbates the tingling, and after something exacerbates the pain, the tingling seems "dull". The symptoms come a …
```

**Generated note**

```
CHIEF COMPLAINT
Bilateral hand numbness and tingling.

HISTORY OF PRESENT ILLNESS

This is a 60-year-old right-handed female who presented to the office for evaluation of bilateral hand numbness and tingling.  She has had this symptomatology for several weeks.  She denies any history of cancer.  She has a history of chronic kidney disease, gout, hypertension, anxiety, GERD, and diabetes.  She has been on carvedilol 25 mg twice daily for hypertension and Lexapro 10 mg daily for anxiety.  She has a known allergy to sulfa.  She denies any history of thyroid problems.  She has been on nerve pain medication which she has not been compliant with.  She has had a CT brain with contrast done on 02/05/21, which showed no metastatic disease or acute intracranial abnormalities.

REVIEW OF SYSTEMS

Constitutional:  Fatigue and weight gain.
GI:  Excessive appetite and bloating.
Eyes:  Floaters.
CV:  Shortness of breath and lower extremity edema.
Endocrine:  Positive for diabetes, always hungry.
Skin:  Nail bed trenches, dryness, itching.
Musculoskeletal:  Gout, muscle pain.
Neurological:  Bilatera …
```

- unsupported entities (vs. transcript): emg
- incorrect diagnosis: —  ·  missing diagnosis: trauma
- incorrect medication: —  ·  missing medication: —
- dosage mismatch: —
- negation flips (vs. reference): —
- unsupported numbers: —
- missing information: {"symptom": ["bruising", "pain", "rash", "stiffness"], "medical_history": ["heartburn", "prediabetes"], "diagnosis": ["trauma"]}

## Worst ROUGE-L: `aci_bench_test_taskC_3_D2N193-aci`

*lowest ROUGE-L in the split*

ROUGE-L 3.1 · length ratio 1.45 · truncated True · degenerate True · hallucination 85.7 · negation-flip 0.0 · numerical consistency 50.0 · coverage 26.7

**Transcript (excerpt)**

```
[doctor] good alright hello hannah how are you today
[patient] i'm doing well
[doctor] you're doing well
[patient] i did have this this hacking cough for about three days now
[doctor] okay tell me more about that cough
[patient] it started three days ago i was around my sister and she has been sick with the same kind of symptoms and so this cough has just started off with like a gradual cough and now i've just been coughing up some green phlegm here
[doctor] okay okay so you you started having some mucus with it
[patient] yes
[doctor] okay and how about any other symptoms with your cough
[patient] i'm having a little bit of a sore throat here and then a little bit of a some nasal congestion  …
```

**Reference note**

```
CHIEF COMPLAINT

Cough.

MEDICAL HISTORY

Patient reports history of seasonal allergies, diabetes type 2, and hypertension.

MEDICATIONS

Patient reports taking metformin 500 mg as well as hydrochlorothiazide every day.

REVIEW OF SYSTEMS

Constitutional: Denies any fever or body aches.
HENT: Reports sore throat and nasal congestion.
Respiratory: Reports productive cough with green phlegm. Denies any shortness of breath.
Gastrointestinal: Denies nausea, vomiting, or diarrhea.

VITALS

Blood Pressure: Elevated at 144/72 mm Hg. The remainder of the vital signs look good.

PHYSICAL EXAM

Head and Face
- Examination: No frontal sinus tenderness. Bilateral maxillary sinus tenderness.

Ears, Nose, Mouth, and Throat
- Examination of Mouth:
- Examination of Throat: Erythema of the pharynx. Tonsils are symmetrical. No exudates.

Neck
- General Examination: Anterior cervical adenopathy.

Respirato …
```

**Generated note**

```
CHIEF COMPLAINT
The patient is a 45-year-old female who comes in for evaluation of her cough, which has been present for approximately three days.  She denies any shortness of breath, chest pain, nausea, vomiting, diarrhea, abdominal pain, fever, chills, headache, photophobia, syncope, palpitations, orthopnea, paroxysmal nocturnal dyspnea, PND, pleuritic chest pain, arthralgias, myalgias, rash, pruritus, conjunctivitis, diplopia, dysphagia, hoarseness, odynophagia, dysuria, frequency, urgency, flank pain, costovertebral angle tenderness, CVA/TIA, weakness, numbness, tingling, tremors, gait disturbances, visual changes, hearing loss, vertigo, tinnitus, ear fullness, epistaxis, hemoptysis, hematemesis, melena, hematochezia, weight gain, weight loss, decreased appetite, increased appetite, fatigue, lethargy, confusion, memory loss, personality change, anxiety, depression, irritability, insomnia, somnolence, night sweats, diaphoresis, cold intolerance, heat intolerance, thyroid nodules, thyroid masses, thyroid enlargement, thyroid tenderness, thyroid bruit, thyroid gland enlargement, thy …
```

- unsupported entities (vs. transcript): abdominal pain, anxiety, blood in stool, blurred vision, chest pain, chills, cold intolerance, confusion, conjunctivitis, daytime sleepiness, depression, difficulty walking, dizziness, double vision, dysphagia, dysuria, fatigue, headache, hearing loss, heat intolerance
- incorrect diagnosis: anxiety, depression, stroke, thyroid nodule, transient ischemic attack  ·  missing diagnosis: diabetes, hypertension, type 2 diabetes, upper respiratory infection
- incorrect medication: —  ·  missing medication: hydrochlorothiazide, metformin
- dosage mismatch: —
- negation flips (vs. reference): —
- unsupported numbers: 45
- missing information: {"symptom": ["crackles", "edema", "erythema", "murmur", "nasal congestion", "rhonchi"], "medical_history": ["allergic rhinitis", "hypertension", "type 2 diabetes"], "diagnosis": ["diabetes", "upper respiratory infection"], "medication": ["hydrochlorothiazide", "metformin"], "investigation": ["blood pressure measurement", "covid test", "hemoglobin a1c", "physical examination", "vital signs"]}

## Hallucination example: `aci_bench_test_taskC_3_D2N197-aci`

*hallucination example*

ROUGE-L 6.6 · length ratio 2.69 · truncated True · degenerate False · hallucination 86.4 · negation-flip 33.3 · numerical consistency 100.0 · coverage 30.0

**Transcript (excerpt)**

```
[doctor] so donna is a 37 -year-old female she is here with complaint of headache she has a history of hypertension and diabetes so donna tell me what's going on
[patient] yeah lately i've just been having quite a bit of a headache and i mean every now and then i'll get it but lately it's just been getting worse and i've noticed that my blood pressure has been running high i've been taking it maybe like once a week but the past three weeks it's been really high than usual so i was a little worried
[doctor] do you remember the numbers that you're getting on your blood pressure readings
[patient] yeah so one of them was like one sixty over eighty seven and then the last one was like one sevent …
```

**Reference note**

```
CHIEF COMPLAINT

Headache.

MEDICAL HISTORY

Patient reports history of hypertension and diabetes. She has migraines rarely every 1 to 2 years.

SOCIAL HISTORY

Patient reports she walks for exercise.

ALLERGIES

Patient reports history of seasonal allergies.

MEDICATIONS

Patient reports taking lisinopril 20 mg once a day and Tylenol.

REVIEW OF SYSTEMS

HENT: Denies congestion or runny nose.
Respiratory: Denies cough.
Genitourinary: Denies polyuria.
Neurological: Reports headaches.

PHYSICAL EXAM

Head and Face
- No frontal or maxillary sinus tenderness.

Neck
- General Examination: Neck is supple without lymphadenopathy.

Hematology/Lymphatic/Immunology
- Palpation: No enlarged lymph nodes.

ASSESSMENT AND PLAN

1. Hypertension with headaches.
- Medical Reasoning: Patient presents today with complaints of increasing headaches and elevated blood pressure readings at home.
- Patient Edu …
```

**Generated note**

```
CHIEF COMPLAINT

The patient is a 37-year-old female who comes in today complaining of headaches.  She has a history of hypertension and diabetes.

HISTORY OF PRESENT ILLNESS

The patient is a 37-year-old female who comes in today complaining of headaches.  She has a history of hypertension and diabetes.  She states that her headaches have been worsening over the past three weeks.  She denies any history of migraines.  She denies any history of sinusitis.  She denies any history of allergies.  She denies any history of sore throat.  She denies any history of fever.  She denies any history of chills.  She denies any history of nausea.  She denies any history of vomiting.  She denies any history of abdominal pain.  She denies any history of dysuria.  She denies any history of frequency.  She denies any history of urgency.  She denies any history of nocturia.  She denies any history of orthostatic hypotension.  She denies any history of syncope.  She denies any history of palpitations.  She denies any history of chest pain.  She denies any history of shortness of breath.  She denies any …
```

- unsupported entities (vs. transcript): abdominal pain, bleeding, blood in stool, breast pain, bruising, bursitis, chest pain, chills, dyspnea, dysuria, edema, erythema, fever, fungal infection, hematuria, hemoptysis, itching, jaundice, joint pain, joint swelling
- incorrect diagnosis: —  ·  missing diagnosis: —
- incorrect medication: —  ·  missing medication: acetaminophen, lisinopril
- dosage mismatch: —
- negation flips (vs. reference): allergic rhinitis, migraine
- unsupported numbers: —
- missing information: {"symptom": ["lymphadenopathy", "nasal congestion", "pain", "polyuria", "rhinorrhea"], "medication": ["acetaminophen", "lisinopril"], "investigation": ["blood glucose", "blood pressure measurement", "blood work", "diagnostic workup", "hemoglobin a1c", "home monitoring"]}

## Incorrect diagnosis example: `aci_bench_test_taskC_3_D2N193-aci`

*incorrect diagnosis example*

ROUGE-L 3.1 · length ratio 1.45 · truncated True · degenerate True · hallucination 85.7 · negation-flip 0.0 · numerical consistency 50.0 · coverage 26.7

**Transcript (excerpt)**

```
[doctor] good alright hello hannah how are you today
[patient] i'm doing well
[doctor] you're doing well
[patient] i did have this this hacking cough for about three days now
[doctor] okay tell me more about that cough
[patient] it started three days ago i was around my sister and she has been sick with the same kind of symptoms and so this cough has just started off with like a gradual cough and now i've just been coughing up some green phlegm here
[doctor] okay okay so you you started having some mucus with it
[patient] yes
[doctor] okay and how about any other symptoms with your cough
[patient] i'm having a little bit of a sore throat here and then a little bit of a some nasal congestion  …
```

**Reference note**

```
CHIEF COMPLAINT

Cough.

MEDICAL HISTORY

Patient reports history of seasonal allergies, diabetes type 2, and hypertension.

MEDICATIONS

Patient reports taking metformin 500 mg as well as hydrochlorothiazide every day.

REVIEW OF SYSTEMS

Constitutional: Denies any fever or body aches.
HENT: Reports sore throat and nasal congestion.
Respiratory: Reports productive cough with green phlegm. Denies any shortness of breath.
Gastrointestinal: Denies nausea, vomiting, or diarrhea.

VITALS

Blood Pressure: Elevated at 144/72 mm Hg. The remainder of the vital signs look good.

PHYSICAL EXAM

Head and Face
- Examination: No frontal sinus tenderness. Bilateral maxillary sinus tenderness.

Ears, Nose, Mouth, and Throat
- Examination of Mouth:
- Examination of Throat: Erythema of the pharynx. Tonsils are symmetrical. No exudates.

Neck
- General Examination: Anterior cervical adenopathy.

Respirato …
```

**Generated note**

```
CHIEF COMPLAINT
The patient is a 45-year-old female who comes in for evaluation of her cough, which has been present for approximately three days.  She denies any shortness of breath, chest pain, nausea, vomiting, diarrhea, abdominal pain, fever, chills, headache, photophobia, syncope, palpitations, orthopnea, paroxysmal nocturnal dyspnea, PND, pleuritic chest pain, arthralgias, myalgias, rash, pruritus, conjunctivitis, diplopia, dysphagia, hoarseness, odynophagia, dysuria, frequency, urgency, flank pain, costovertebral angle tenderness, CVA/TIA, weakness, numbness, tingling, tremors, gait disturbances, visual changes, hearing loss, vertigo, tinnitus, ear fullness, epistaxis, hemoptysis, hematemesis, melena, hematochezia, weight gain, weight loss, decreased appetite, increased appetite, fatigue, lethargy, confusion, memory loss, personality change, anxiety, depression, irritability, insomnia, somnolence, night sweats, diaphoresis, cold intolerance, heat intolerance, thyroid nodules, thyroid masses, thyroid enlargement, thyroid tenderness, thyroid bruit, thyroid gland enlargement, thy …
```

- unsupported entities (vs. transcript): abdominal pain, anxiety, blood in stool, blurred vision, chest pain, chills, cold intolerance, confusion, conjunctivitis, daytime sleepiness, depression, difficulty walking, dizziness, double vision, dysphagia, dysuria, fatigue, headache, hearing loss, heat intolerance
- incorrect diagnosis: anxiety, depression, stroke, thyroid nodule, transient ischemic attack  ·  missing diagnosis: diabetes, hypertension, type 2 diabetes, upper respiratory infection
- incorrect medication: —  ·  missing medication: hydrochlorothiazide, metformin
- dosage mismatch: —
- negation flips (vs. reference): —
- unsupported numbers: 45
- missing information: {"symptom": ["crackles", "edema", "erythema", "murmur", "nasal congestion", "rhonchi"], "medical_history": ["allergic rhinitis", "hypertension", "type 2 diabetes"], "diagnosis": ["diabetes", "upper respiratory infection"], "medication": ["hydrochlorothiazide", "metformin"], "investigation": ["blood pressure measurement", "covid test", "hemoglobin a1c", "physical examination", "vital signs"]}

## Incorrect medication / dosage example: `aci_bench_test_taskC_3_D2N173-virtassist`

*incorrect medication / dosage example*

ROUGE-L 8.7 · length ratio 1.39 · truncated True · degenerate False · hallucination 64.9 · negation-flip 0.0 · numerical consistency 100.0 · coverage 61.9

**Transcript (excerpt)**

```
[doctor] hi logan , how are you ?
[patient] hi . good to see you .
[doctor] it's good to see you as well . so i know the nurse told you about dax . i'd like to tell dax a little bit about you . okay ?
[patient] sure .
[doctor] so logan is a 57-year-old male , with a past medical history significant for coronary artery bypass grafting , hyperlipidemia , and ocd , who presents with an upper respiratory infection . so , logan , what's going on ?
[patient] so , uh , about a week ago i started to get a cold . and , in the last two or three days , it seemed to move into my chest .
[doctor] okay . um , and , and are you having any pain in your sinuses ? or , any post nasal drip ?
[patient] um , i h …
```

**Reference note**

```
CHIEF COMPLAINT

Upper respiratory infection.

HISTORY OF PRESENT ILLNESS

Logan Harris is a 57-year-old male with a past medical history significant for coronary artery bypass grafting, hyperlipidemia, and OCD, who presents with an upper respiratory infection.

The patient reports that about a week ago he started to get a cold, which has worsened in the last 2 or 3 days. He endorses some postnasal drip for the beginning of the week, however, it has seemed to move into his chest. He denies chest pain other than his chest congestion. He was able to exercise prior to getting sick. He denies anyone else being sick in his house. He denies fever and shortness of breath.

Regarding his high cholesterol, he states he has been pretty good for the most part. He did a little travel over the last week or so and his diet was not great but for the most part it is pretty good. He is on Crestor 20 mg a …
```

**Generated note**

```
CHIEF COMPLAINT

The patient is a 57-year-old male who comes in today with complaints of upper respiratory infection, which he states has been present for approximately one week.  He also states that he has had some postnasal drip and some sinus pressure.  He denies any shortness of breath, chest pain, muscle aches, or fever.  He does have some lymphadenopathy and some wheezing bilaterally.  He has had some recent travel.  He has been vaccinated for COVID-19.  He has had some recent upper respiratory infections.  He has had some recent hyperlipidemia.  He has had some recent coronary artery disease.  He has had some recent coronary artery bypass grafting.  He has had some recent statin therapy.  He has had some recent NSAID therapy.  He has had some recent beta-blocker therapy.  He has had some recent ACE inhibitor therapy.  He has had some recent aspirin therapy.  He has had some recent clopidogrel therapy.  He has had some recent warfarin therapy.  He has had some recent metformin therapy.  He has had some recent simvastatin therapy.  He has had some recent atorvastatin therapy.  H …
```

- unsupported entities (vs. transcript): aspirin, atorvastatin, calcium supplement, clopidogrel, ezetimibe, fenofibrate, fish oil, gemfibrozil, lactate, lovastatin, magnesium supplement, metformin, niacin, phosphorus level, potassium level, potassium supplement, pravastatin, simvastatin, sodium bicarbonate, sodium level
- incorrect diagnosis: —  ·  missing diagnosis: —
- incorrect medication: aspirin, atorvastatin, calcium supplement, clopidogrel, ezetimibe, fenofibrate, fish oil, gemfibrozil, lovastatin, magnesium supplement, metformin, niacin, potassium supplement, pravastatin, simvastatin, sodium bicarbonate, ursodiol, valproate, vitamin d, warfarin  ·  missing medication: vaccine
- dosage mismatch: —
- negation flips (vs. reference): —
- unsupported numbers: —
- missing information: {"symptom": ["rhonchi"], "medication": ["vaccine"], "investigation": ["covid test", "diagnostic workup", "lipid panel", "oxygen saturation", "stress test", "vital signs"]}

## Negation error example: `aci_bench_test_taskC_3_D2N188-aci`

*negation error example*

ROUGE-L 12.7 · length ratio 2.21 · truncated True · degenerate True · hallucination 31.6 · negation-flip 61.5 · numerical consistency 66.7 · coverage 61.9

**Transcript (excerpt)**

```
[doctor] hi jaqueline how are you i heard that you injured your ankle
[patient] yeah it's not going so great
[doctor] what what happened to your ankle
[patient] well i was doing something i did n't really want to be doing and i fell and now my ankle hurts
[doctor] okay well what were you doing were you hiking or biking or what were you doing
[patient] i was in a mountain biking messenger
[doctor] you were in a mountain biking lesson and you fell off your bike and twisted your ankle
[patient] yes
[doctor] and what ankle was bothering you
[patient] the right one
[doctor] your right ankle okay and did it twist like did your ankle twist outward or did your ankle twist inward do you know
[patient …
```

**Reference note**

```
CHIEF COMPLAINT

Right ankle injury.

HISTORY OF PRESENT ILLNESS

Jacqueline Price is a pleasant 28-year-old female who presents to the clinic today for the evaluation of a right ankle injury. The patient sustained the injury when she fell while in mountain biking lessons. She states that her ankle twisted outward. The patient localizes the pain to her lateral aspect of her right ankle. She denies any tingling, but notes numbness in her toes. She notes that she is able to move her ankle a little bit. The patient states that she has difficulty walking. Additionally, she notes that she has a limp when she ambulates. She has taken Tylenol for the pain, but states that it was not beneficial. She denies hearing a pop, but did hear a crack when the injury happened. Ms. Price notes that she has had a fever.

SOCIAL HISTORY

The patient has been mountain biking for 3 years.

REVIEW OF SYSTEMS

C …
```

**Generated note**

```
CHIEF COMPLAINT

The patient is a 35-year-old female who presents with right ankle pain and swelling after a fall while mountain biking.

HISTORY OF PRESENT ILLNESS

The patient states she has had right ankle pain and swelling for approximately 2 weeks.  She denies numbness, tingling, weakness, fever, chills, edema, erythema, bruising, or recent trauma.  She denies taking Tylenol for her pain.  She denies hearing a "pop" during the incident.  She has had a history of right ankle pain for 3 years.  She denies any past medical history of fractures, sprains, or dislocations.  She denies any allergies to medications.  She denies any history of smoking or alcohol abuse.  She denies any history of previous surgeries.  She denies any history of chronic illnesses.  She denies any history of hospitalizations.  She denies any history of previous injuries to her right ankle.  She denies any history of previous surgeries to her right ankle.  She denies any history of chronic illnesses.  She denies any history of hospitalizations.  She denies any history of previous injuries to her right ankle.   …
```

- unsupported entities (vs. transcript): allergic rhinitis, dislocation, medication, numbness, substance use disorder, weakness
- incorrect diagnosis: —  ·  missing diagnosis: —
- incorrect medication: —  ·  missing medication: meloxicam
- dosage mismatch: —
- negation flips (vs. reference): acetaminophen, bruising, erythema, fever, numbness, pain, sprain, trauma
- unsupported numbers: 35
- missing information: {"symptom": ["difficulty walking", "limping"], "medication": ["meloxicam"], "investigation": ["blood pressure measurement", "imaging", "physical examination", "weight measurement", "x-ray"]}

## Numerical error example: `aci_bench_test_taskC_3_D2N194-aci`

*numerical error example*

ROUGE-L 31.6 · length ratio 1.15 · truncated False · degenerate False · hallucination 27.8 · negation-flip 11.1 · numerical consistency 27.3 · coverage 80.0

**Transcript (excerpt)**

```
[doctor] hey betty how're you
[patient] i'm doing okay aside from this left shoulder pain that i've been having for a few weeks now
[doctor] wow well i'm sorry to hear that do you remember what you were doing when the pain started
[patient] i you know i ca n't think about anything specifically but i am very active and i also have been renovating my basement so i have been doing a lot with that
[doctor] wow okay and do you know if there was any direct or associated trauma that you can think of over the past three weeks like did you fall or hit your shoulder or anything
[patient] no no trauma that i can think of at all
[doctor] okay
[patient] i do n't remember hitting it either
[doctor] okay n …
```

**Reference note**

```
CHIEF COMPLAINT

Left shoulder pain.

HISTORY OF PRESENT ILLNESS

Betty Rogers is a pleasant 50-year-old female who presents to the clinic today for the evaluation of left shoulder pain.

For the past few weeks, the patient has been experiencing constant pain isolated to the left shoulder. She denies any known injury or trauma; however, she is very active and is currently renovating her basement. She denies any associated numbness or tingling as well. While movements such as reaching and lifting exacerbate her pain, full flexion of the shoulder is the most severe. Her pain is also exacerbated if she lays on her shoulder, which subsequently causes sleep disturbance due to her being uncomfortable. She typically takes Tylenol Extra Strength, 2 tablets every 6 to 8 hours, for aches and pains associated with her active lifestyle, and doing so reduces her shoulder pain to 2-3/10 on the pain sc …
```

**Generated note**

```
CHIEF COMPLAINT
Left shoulder pain.

HISTORY OF PRESENT ILLNESS

The patient is a 62-year-old female who presents to the office complaining of left shoulder pain for several weeks.  She denies any history of trauma.  She has been renovating her basement and has been active.  She denies any numbness or tingling in her left arm.  She has been taking Tylenol PRN for her pain.  She rates her pain as a 7/10 without Tylenol and 2/10 with Tylenol.  She denies any history of falls.  She has had some fatigue in the past.  She has had some right-sided shoulder pain in the past.  She denies any history of fractures.  She denies any history of rotator cuff tears.  She denies any history of corticosteroid injections.

REVIEW OF SYSTEMS

Significant for left shoulder pain.  Denies any history of trauma.  Denies any history of numbness or tingling in her left arm.  Denies any history of falls.  Denies any history of fatigue.  Denies any history of right-sided shoulder pain.  Denies any history of fractures.  Denies any history of rotator cuff tears.  Denies any history of corticosteroid injections. …
```

- unsupported entities (vs. transcript): blood pressure measurement, dislocation, heart rate measurement, mri, respiratory rate
- incorrect diagnosis: —  ·  missing diagnosis: —
- incorrect medication: —  ·  missing medication: —
- dosage mismatch: —
- negation flips (vs. reference): cortisone injection
- unsupported numbers: 1, 100, 120, 130, 130/80, 16, 4, 5, 60, 62, 70, 78, 80, 9, 90
- missing information: {"investigation": ["clinical score", "diagnostic workup", "imaging"]}

## Missing information example: `aci_bench_test_taskC_3_D2N195-aci`

*missing information example*

ROUGE-L 14.2 · length ratio 1.46 · truncated True · degenerate True · hallucination 71.4 · negation-flip 50.0 · numerical consistency 50.0 · coverage 9.1

**Transcript (excerpt)**

```
[doctor] hey matthew how is it going good to see you today i see here in your notes you are here for some right knee pain and we are also going to check up on your hypertension and diabetes so can you tell me what happened to your knee
[patient] yes so i was playing basketball yesterday and when i went up for a rebound and i came down and i felt like my knee just popped it started swelling and i could hardly walk when it happened
[doctor] okay playing basketball how often do you play basketball
[patient] first time in two years
[doctor] first time in two years did you watch the game last night
[patient] yeah unfortunately both teams did n't lose so i was unhappy
[doctor] you're going home wh …
```

**Reference note**

```
CHIEF COMPLAINT

Right knee pain

HISTORY OF PRESENT ILLNESS

Matthew Allen is a pleasant 40-year-old male who presents to the clinic today for the evaluation of right knee pain. The onset of his pain began yesterday after he went up for a rebound while playing basketball and felt a pop in his knee. He states that he experienced swelling and difficulty with ambulation following this incident. He locates his pain today to the medial aspect of his knee. His pain is described as aching and is rated at 4 out of 10. In terms of his swelling, he states that this has improved some. He is also able to weight-bear, but he finds that he is favoring his left leg while doing so. His tried treatments include Tylenol with some relief as well as rest.

The patient has a history of hypertension and diabetes. He reports that he does not check is blood pressure at home very often, but he typically runs 14 …
```

**Generated note**

```
CHIEF COMPLAINT
Right knee pain.

HISTORY OF PRESENT ILLNESS

The patient is a 35-year-old male who comes in for evaluation of his right knee pain.  He states he has had right knee pain for approximately 2 years.  He denies any trauma to the knee.  He denies any history of surgery to the knee.  He denies any history of joint effusion.  He denies any history of locking of the knee.  He denies any history of catching of the knee.  He denies any history of giving way of the knee.  He denies any history of pain in the left knee.  He denies any history of pain in the bilateral ankles.  He denies any history of pain in the bilateral feet.  He denies any history of pain in the bilateral hips.  He denies any history of pain in the bilateral knees.  He denies any history of pain in the bilateral elbows.  He denies any history of pain in the bilateral wrists.  He denies any history of pain in the bilateral shoulders.  He denies any history of pain in the neck.  He denies any history of pain in the thoracic spine.  He denies any history of pain in the lumbar spine.  He denies any history of num …
```

- unsupported entities (vs. transcript): joint instability, joint swelling, numbness, trauma, weakness
- incorrect diagnosis: —  ·  missing diagnosis: acl tear, diabetes, hypertension, strain
- incorrect medication: —  ·  missing medication: acetaminophen, amlodipine, meloxicam, metformin
- dosage mismatch: —
- negation flips (vs. reference): pain
- unsupported numbers: 35
- missing information: {"symptom": ["bruising", "edema", "erythema", "murmur"], "medical_history": ["diabetes", "hypertension"], "diagnosis": ["acl tear", "dislocation", "fracture", "strain"], "medication": ["acetaminophen", "amlodipine", "meloxicam", "metformin"], "investigation": ["blood glucose", "blood pressure measurement", "hemoglobin a1c", "mri", "physical examination", "weight measurement"]}

## Degenerate output example: `aci_bench_test_taskC_3_D2N191-aci`

*degenerate output example*

ROUGE-L 6.5 · length ratio 1.32 · truncated True · degenerate True · hallucination 87.5 · negation-flip 0.0 · numerical consistency 100.0 · coverage 19.0

**Transcript (excerpt)**

```
[doctor] so hi zachary good to see you today so i'm looking at my notes i see you coming in with some right elbow pain and you also have a past medical history of hypertension diabetes we're gon na check on those so can you tell me what happened to your elbow
[patient] i just woke up one day it was hurting
[doctor] it was hurting okay how long ago would you say that was
[patient] since
[doctor] since yesterday alright
[patient] it's actually my it's actually my left elbow my left arm
[doctor] okay they must have written that down wrong so it is your your left arm are you right handed or left handed
[patient] right handed
[doctor] okay so do you think you might have slept on it wrong or anyth …
```

**Reference note**

```
CHIEF COMPLAINT

Left arm pain.

HISTORY OF PRESENT ILLNESS

Zachary Wood is a 45-year-old right-hand-dominant male who presents to the clinic today for the evaluation of left arm pain. The onset of his pain began yesterday when he woke up with pain. He denies any specific injury. The patient locates his pain from his left elbow up all the way to his neck. He describes his pain as an achiness. The patient has been taking Motrin for pain, which does not provide him with relief. He also reports intermittent chest pain that radiates up his neck. He notes that he had to stop cutting the grass the other day because of chest pain. The patient denies any shortness of breath.

For his hypertension, the patient states that his blood pressure has been around 125/72 recently. He is still taking 2.5 mg of Norvasc.

Regarding his type 2 diabetes, his last hemoglobin A1c was 7.2. He takes metformin 50 …
```

**Generated note**

```
CHIEF COMPLAINT

The patient presents with right-sided elbow pain, which has been present for one day.  He has a history of hypertension, diabetes mellitus, and possible MI.  He denies diarrhea, dysphagia, palpitations, orthopnea, paroxysmal nocturnal dyspnea, syncope, weight loss, fever, chills, arthralgias, joint swelling, muscle weakness, visual changes, hearing changes, tinnitus, vertigo, diplopia, dysarthria, dysphonia, hoarseness, odynophagia, hemoptysis, hematemesis, melena, abdominal pain, nausea, vomiting, constipation, diarrhea, pruritus, urticaria, rash, edema, pedal edema, jugular venous distension, hepatomegaly, splenomegaly, lymphadenopathy, pleural effusion, pericardial friction rub, murmurs, gallops, S3, S4, clubbing, cyanosis, wheezing, stridor, cough, sputum production, hemoptysis, hematuria, oliguria, nocturia, frequency, urgency, dysuria, flank pain, costovertebral angle tenderness, back pain, leg pain, calf pain, ankle edema, foot edema, decreased sensation, decreased reflexes, hyperreflexia, clonus, tremors, asterixis, ataxia, gait disturbance, weakness, paralys …
```

- unsupported entities (vs. transcript): abdominal pain, back pain, bloating, blood in stool, blurred vision, chills, confusion, constipation, cough, cyanosis, depression, difficulty walking, dizziness, double vision, dry mouth, dysphagia, dysuria, edema, fatigue, fever
- incorrect diagnosis: depression, pleural effusion  ·  missing diagnosis: myocardial infarction, type 2 diabetes
- incorrect medication: —  ·  missing medication: amlodipine, aspirin, ibuprofen, metformin, nitroglycerin
- dosage mismatch: —
- negation flips (vs. reference): —
- unsupported numbers: —
- missing information: {"symptom": ["arm pain", "chest pain", "dyspnea", "neck pain"], "diagnosis": ["myocardial infarction", "trauma", "type 2 diabetes"], "medication": ["amlodipine", "aspirin", "ibuprofen", "metformin", "nitroglycerin"], "investigation": ["blood glucose", "blood pressure measurement", "diagnostic workup", "electrocardiogram", "hemoglobin a1c"]}

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

## Worst ROUGE-L: `mts_dialog_test_chat_2023_64`

*lowest ROUGE-L in the split*

ROUGE-L 0.0 · length ratio 0.10 · truncated False · degenerate False · hallucination 0.0 · negation-flip 0.0 · numerical consistency — · coverage 100.0

**Transcript (excerpt)**

```
Doctor: How're you feeling today? 
Patient: Honestly, I've had way better days. 
Doctor: I'm sorry. Why is that? 
Patient: I've been getting short of breath a lot more than I'm used to. 
Doctor: How long has this been going on? 
Patient: Past three days. 
Doctor: Are you experiencing any leg pain or swelling? 
Patient: Eh no.  
Doctor: How about chest pain or anything like it? 
Patient: No to that either. 
Doctor: I must say, this is concerning. I'd like you to get a C T scan of your chest so we can see what's going on. For now, your pulse ox is in the high nineties so you won't be needing supplemental oxygen at this moment in time. Do you notice the shortness of breath getting worse when yo …
```

**Reference note**

```
"I have had trouble breathing for the past 3 days"
```

**Generated note**

```
Dyspnea.
```

- unsupported entities (vs. transcript): —
- incorrect diagnosis: —  ·  missing diagnosis: —
- incorrect medication: —  ·  missing medication: —
- dosage mismatch: —
- negation flips (vs. reference): —
- unsupported numbers: —
- missing information: {}

## Hallucination example: `mts_dialog_test_chat_2023_120`

*hallucination example*

ROUGE-L 5.7 · length ratio 4.62 · truncated True · degenerate False · hallucination 90.0 · negation-flip 33.3 · numerical consistency 0.0 · coverage 60.0

**Transcript (excerpt)**

```
Doctor: So, what's going on with your hand, miss? Is it right or left? 
Patient: It's the right one. It's been on and off and it's been happening for the last several weeks. 
Doctor: Can you elaborate what's happening? 
Patient: Sometimes I feel like a lot of pins and needles are hurting my hand while other times it is totally numb. 
Doctor: Did anything change in your daily routine? 
Patient: I don't think there have been any big changes. But after I started having these episodes of numbness and tingling, I moved my keyboard down at work. I just hope that it will help. I was just worried if I had carpal tunnel. 
Doctor: What does a normal day look like? What is it like at work? 
Patient: I  …
```

**Reference note**

```
This patient presents to the office today because of some problems with her right hand.  It has been going tingling and getting numb periodically over several weeks.  She just recently moved her keyboard down at work.  She is hoping that will help.  She is worried about carpal tunnel.  She does a lot of repetitive type activities.  It is worse at night.  If she sleeps on it a certain way, she will wake up and it will be tingling then she can usually shake out the tingling, but nonetheless it is very bothersome for her.  It involves mostly the middle finger, although, she says it also involves the first and second digits on the right hand.  She has some pain in her thumb as well.  She thinks that could be arthritis.
```

**Generated note**

```
The patient is a 35-year-old female who comes in today complaining of numbness, paresthesias, and pain in her right hand.  She has had this for several weeks.  She denies any trauma.  She denies any history of diabetes.  She denies any history of thyroid disease.  She denies any history of rheumatoid arthritis.  She denies any history of gout.  She denies any history of lupus.  She denies any history of fibromyalgia.  She denies any history of osteoarthritis.  She denies any history of tendonitis.  She denies any history of bursitis.  She denies any history of tenosynovitis.  She denies any history of ganglion cysts.  She denies any history of synovial cysts.  She denies any history of trigger points.  She denies any history of plantar fasciitis.  She denies any history of Achilles tendinitis.  She denies any history of peroneal tendinitis.  She denies any history of patellar tendinitis.  She denies any history of iliotibial band friction syndrome.  She denies any history of stress fractures.  She denies any history of compartment syndrome.  She denies any history of nerve entrapment …
```

- unsupported entities (vs. transcript): adrenal insufficiency, anxiety symptoms, brain tumor, bursitis, cancer, cushing's syndrome, diabetes, fibromyalgia, fracture, ganglion cyst, gout, hyperkalemia, hyperthyroidism, hypokalemia, hypothyroidism, lupus, lyme disease, multiple sclerosis, neuropathy, osteoarthritis
- incorrect diagnosis: —  ·  missing diagnosis: —
- incorrect medication: —  ·  missing medication: —
- dosage mismatch: —
- negation flips (vs. reference): arthritis
- unsupported numbers: 35
- missing information: {"symptom": ["tingling"], "diagnosis": ["carpal tunnel syndrome"]}

## Incorrect medication / dosage example: `mts_dialog_test_chat_2023_188`

*incorrect medication / dosage example*

ROUGE-L 32.3 · length ratio 0.47 · truncated False · degenerate False · hallucination 57.1 · negation-flip 0.0 · numerical consistency 100.0 · coverage 100.0

**Transcript (excerpt)**

```
Doctor: Remind me, please, when was your last appointment, miss?
Patient: Um, it was about three months ago. 
Doctor: How have your diabetes and kidney disease progressed since?
Patient: Well, I've had a lot of variability in my glucose control too largely, and recent upper and lower respiratory illnesses.
Doctor: Who treated you for these?
Patient: I didn't see anyone, the symptoms just kind of improved on their own.
Doctor: I see, are you still having difficulties with blood sugar management?
Patient: Yes, my two week average is one hundred ninety one, and it was high this morning.
Doctor: What do you think caused this?
Patient: Um, I had problems with my infusion set. 
Doctor: Let's try a …
```

**Reference note**

```
This is a return visit to the renal clinic for the patient where she is followed up for diabetes and kidney disease management.  Her last visit to this clinic was approximately three months ago.  Since that time, the patient states that she has had some variability in her glucose control too largely to recent upper and lower respiratory illnesses.  She did not seek attention for these, and the symptoms have begun to subside on their own and in the meantime, she continues to have some difficulties with blood sugar management.  Her 14-day average is 191.  She had a high blood sugar this morning, which she attributed to a problem with her infusion set; however, in the clinic after an appropriate correction bolus, she subsequently became quite low.  She was treated appropriately with glucose and crackers, and her blood sugar came back up to over 100.  She was able to manage this completely o …
```

**Generated note**

```
The patient has a history of diabetes mellitus type II and chronic renal insufficiency.  She has had her last visit approximately three months ago.  Since then she has had significant variability in her blood sugars and has had recent upper and lower respiratory infections.  She has had no treatment for these conditions.  Her current HbA1c is 191.  She has had difficulty managing her blood sugars.  She has had problems with her insulin pump.  She has had hypoglycemia.  She has had hyperglycemia.  She denies any other medical problems.  She has had some dietary changes.
```

- unsupported entities (vs. transcript): hemoglobin a1c, hypoglycemia, infection, insulin
- incorrect diagnosis: —  ·  missing diagnosis: —
- incorrect medication: insulin  ·  missing medication: —
- dosage mismatch: —
- negation flips (vs. reference): —
- unsupported numbers: —
- missing information: {}

## Negation error example: `mts_dialog_test_chat_2023_78`

*negation error example*

ROUGE-L 12.6 · length ratio 0.55 · truncated False · degenerate False · hallucination 50.0 · negation-flip 50.0 · numerical consistency — · coverage 71.4

**Transcript (excerpt)**

```
Doctor: I see here that you have a history of frequent U T I's. Are you currently experiencing any urinary symptoms? 
Patient: Nope. I've been drinking a lot more water and taking preventative measures to reduce my chances of getting another one anytime soon. I'm being even more conscious of it since I'm now bed bound.
Doctor: That's good news. Are you having other symptoms, such as fever or chills? 
Patient: Nope.
Doctor: How has your weight been? Has it been pretty stable since you have been bed bound?
Patient: Weight is stable. 
Doctor: Okay, now for the routine stuff. Any coughing, chest congestion or chest pain?
Patient: No. 
Doctor: What abut shortness of breath? Any type of bleeding i …
```

**Reference note**

```
GENERAL:  No recent fever, chills.  No recent weight loss. PULMONARY:  No cough, chest congestion. CARDIAC:  No chest pain, shortness of breath. GI:  No abdominal pain, nausea, vomiting.  No constipation.  No bleeding per rectum or melena. GENITOURINARY:  She has had frequent urinary tract infection but does not have any symptoms with it.  ENDOCRINE:  Unable to assess because of patient's bed-bound status.
```

**Generated note**

```
Significant for constipation, abdominal pain, nausea, vomiting, and hematochezia.  Denies fever, chills, cough, sputum production, pleuritic chest pain, orthopnea, paroxysmal nocturnal dyspnea, hemoptysis, hematemesis, dysuria, frequency, urgency, flank pain, and recent weight loss.
```

- unsupported entities (vs. transcript): blood in stool, dysuria, hemoptysis, orthopnea, paroxysmal nocturnal dyspnea, sputum, urinary urgency, weight loss
- incorrect diagnosis: —  ·  missing diagnosis: —
- incorrect medication: —  ·  missing medication: —
- dosage mismatch: —
- negation flips (vs. reference): abdominal pain, blood in stool, constipation, nausea, vomiting
- unsupported numbers: —
- missing information: {"symptom": ["bleeding", "dyspnea", "nasal congestion"], "medical_history": ["urinary tract infection"]}

## Numerical error example: `mts_dialog_test_chat_2023_31`

*numerical error example*

ROUGE-L 28.5 · length ratio 0.48 · truncated False · degenerate False · hallucination 6.7 · negation-flip 20.0 · numerical consistency 77.8 · coverage 70.6

**Transcript (excerpt)**

```
Doctor: Hi there! I am Doctor Jones, sir. 
Patient: Hello! It is nice to meet you. 
Doctor: What brings you into see me today? 
Patient: I have had this weakness in my right leg for quite some time now.
Doctor: How long has this been going on and do you know how you injured yourself?
Patient: I think that it was about six months ago that the weakness in my leg started. I don't really remember how it happened. 
Doctor: Can you tell me what you do remember? 
Patient: I was reaching to get something from a cabinet, and I noticed that I was unable to stand on my right toe. Ever since then I have had difficulty pushing off when walking.  My toes were tingling and numb.
Doctor: Was the numbness an …
```

**Reference note**

```
The patient is a 55-year-old gentleman who presents for further evaluation of right leg weakness.  He has difficulty recollecting the exact details and chronology of his problem.  To the best of his recollection, he thinks that about six months ago he developed weakness of his right leg.  He describes that he is reaching to get something from a cabinet and he noticed that he was unable to stand on his right toe.  Since that time, he has had difficulty pushing off when he walks.  He has mild tingling and numbness in his toes, but this has been a chronic problem and nothing new since he has developed the weakness.  He has chronic mild back pain, but this has been persistent for many years and has not changed.  He has experienced cramps in both calves for the past year.  This dissipated about two months ago.  He does not think that his left leg is weak.  He does not have any bowel or bladde …
```

**Generated note**

```
The patient is a 55-year-old male who comes in for evaluation of his right lower extremity weakness.  He states that he has had this weakness for approximately six months.  He denies any pain, numbness, tingling, weakness in the left lower extremity, bowel/bladder incontinence, or radiculopathy.  He does have a history of back pain which has been chronic for several years.  He has had calf cramps for one year which resolved two months ago.  He denies any recent trauma.  He has seen another physician in the past for this condition.  He has had a CT scan of the lumbar spine which showed degenerative changes without acute pathology.  He has had an EMG/NCV study done.  He has been on atorvastatin and ezetimibe.  He has had elevated creatine kinase levels in the past.  He has been on Lipitor for 15 months.  His creatine kinase levels went up to 800 and then decreased to 500.  He has been off Lipitor for a few weeks.  His creatine kinase level has gone up to 1000 and then decreased to 600.  He has been on Zetia for a few days.  He denies any weakness or pain in his right lower extremity.
```

- unsupported entities (vs. transcript): pathology
- incorrect diagnosis: —  ·  missing diagnosis: —
- incorrect medication: —  ·  missing medication: —
- dosage mismatch: —
- negation flips (vs. reference): numbness, tingling
- unsupported numbers: 1, 600
- missing information: {"symptom": ["lump", "muscle pain"], "investigation": ["blood work", "diagnostic workup", "mri"]}

## Missing information example: `mts_dialog_test_chat_2023_141`

*missing information example*

ROUGE-L 4.1 · length ratio 0.04 · truncated False · degenerate False · hallucination 0.0 · negation-flip 0.0 · numerical consistency 50.0 · coverage 10.0

**Transcript (excerpt)**

```
Patient: So, as you remember I was working with a patient and I accidently jammed that needle inside me.   
Patient: I am coming for regular screening.
Doctor: Yes, thank you for that, sir. Did they screen patient?
Patient: Yes, he got negative H I V but positive hep C, they said he is a carrier only, never will show disease symptoms. 
Doctor: Okay.
Patient: I am scared. 
Doctor: Don't worry, we will do what we can okay. Firstly, let me check if they did some hepatitis B shots on you. Okay looks like you had three shots of hep B and Tetanus is up to date with all others. Antibodies are showing, which is good. 
Patient: They did the tests on February seven two thousand and five. Have you seen …
```

**Reference note**

```
The patient presents for evaluation after a contaminated needlestick to the index finger. The source patient was tested and found to be negative for HIV. However, he did test positive for hepatitis C. He was described as a carrier without active disease. The patient has been followed with periodic evaluation including blood testing. He has completed a 3 shot series for hepatitis B and had titers drawn that showed protected antibodies. He also was up-to-date on his immunization including tetanus. The patient has been well during this time except for the onset of a intestinal illness being investigated with some squeakiness and vomiting. He had no other symptoms that were suggestive of acute hepatitis. His abdominal exam was normal. He had no generalized lymphadenopathy and no fever. Blood tests were drawn on 02/07/2005. The results of which were reviewed with the patient. His liver functi …
```

**Generated note**

```
1.  Hepatitis C. 2.  Acute intestinal obstruction.
```

- unsupported entities (vs. transcript): —
- incorrect diagnosis: —  ·  missing diagnosis: —
- incorrect medication: —  ·  missing medication: vaccine
- dosage mismatch: —
- negation flips (vs. reference): —
- unsupported numbers: 1
- missing information: {"symptom": ["fever", "lymphadenopathy", "vomiting"], "diagnosis": ["infection", "sexually transmitted infection"], "medication": ["vaccine"], "investigation": ["blood work", "metabolic panel", "physical examination"]}

## Degenerate output example: `mts_dialog_test_chat_2023_66`

*degenerate output example*

ROUGE-L 4.1 · length ratio 3.12 · truncated True · degenerate True · hallucination 76.0 · negation-flip 18.8 · numerical consistency — · coverage 53.1

**Transcript (excerpt)**

```
Doctor: You have hypothyroidism, correct? 
Patient: Yes. 
Doctor: Have you been watching your blood sugar? 
Patient: Yes. It's been fine lately so has my anemia. 
Doctor: Good to hear. I see here you were diagnosed with I B S and bowel abnormalities a few years ago. 
Patient: My most recent bouts of diarrhea were likely due to C diff and they seem to have gotten better. 
Doctor: I see my nurse didn't have the chance to go through the review of systems with you, so I will go through them now.
Patient: Okay.
Doctor: Any fever, chills, or night sweats?
Patient: Nope.
Doctor: Any unusual weight gain or loss?
Patient: No, my weight has been stable.
Doctor: Any visual changes, in one or both eyes? …
```

**Reference note**

```
General:  No fever, chills, or night sweats.  Weight stable. HEENT:  No sudden blindness, diplopia, loss of vision, i.e., in one eye or other visual changes.  No hearing changes or ear problems.  No swallowing problems or mouth lesions. Endocrine:  Hypothyroidism but no polyuria or polydipsia.  She watches her blood sugars.  They have been doing quite well. Respiratory:  No shortness of breath, cough, sputum production, hemoptysis or breathing problems. Cardiovascular:  No chest pain or chest discomfort.  No paroxysmal nocturnal dyspnea, orthopnea, palpitations, or heart attacks. GI:  As mentioned, has had diarrhea though thought to be possibly due to Clostridium difficile colitis that now has gotten better.  She has had some irritable bowel syndrome and bowel abnormalities for years. GU:  No urinary problems, dysuria, polyuria or polydipsia, kidney stones, or recent infections.  No vagi …
```

**Generated note**

```
Significant for diarrhea, which was thought to be secondary to Clostridium difficile colitis.  Denies fevers, chills, night sweats, weight change, visual changes, hearing changes, dysuria, hematuria, orthopnea, PND, palpitations, syncope, seizures, headaches, abdominal pain, dysphagia, vomiting, hematemesis, melena, arthralgias, joint pains, rash, pruritus, lymphadenopathy, hepatosplenomegaly, edema, gait disturbances, tremors, weakness, numbness, tingling, diplopia, photophobia, dysarthria, dysphonia, hoarseness, wheezes, stridor, pleuritic chest pain, flank pain, costovertebral angle tenderness, dysuria, nocturia, hematuria, oliguria, anuria, dyspareunia, irregular menstrual periods, galactorrhea, amenorrhea, breast tenderness, nipple discharge, nipple retraction, axillary adenopathy, cervical motion tenderness, pelvic pressure, pelvic pain, dysuria, urgency, frequency, hesitancy, nocturia, hematuria, oliguria, anuria, dysmenorrhea, menorrhagia, metrorrhagia, postcoital bleeding, infertility, impotence, erectile dysfunction, decreased libido, hot flashes, cold intolerance, thyroid  …
```

- unsupported entities (vs. transcript): abdominal pain, bleeding, blood in stool, breast pain, cold intolerance, decreased libido, difficulty walking, double vision, dysmenorrhea, dysphagia, dysuria, edema, erectile dysfunction, hematuria, hoarseness, hot flashes, inflammatory bowel disease, itching, joint pain, lymphadenopathy
- incorrect diagnosis: —  ·  missing diagnosis: —
- incorrect medication: —  ·  missing medication: —
- dosage mismatch: —
- negation flips (vs. reference): chest pain, dysuria, vaginal bleeding
- unsupported numbers: —
- missing information: {"symptom": ["cough", "dyspnea", "hemoptysis", "polydipsia", "polyuria", "sputum"], "medical_history": ["anemia", "irritable bowel syndrome"], "diagnosis": ["hypothyroidism", "infection", "kidney stones", "myocardial infarction", "stroke"], "investigation": ["blood glucose"]}

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

ROUGE-L 0.0 · length ratio 12.00 · truncated False · degenerate False · hallucination — · negation-flip — · numerical consistency — · coverage —

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
She denies tobacco/ETOH/illicit drug use.  She denies any significant past medical history.
```

- unsupported entities (vs. transcript): —
- incorrect diagnosis: —  ·  missing diagnosis: —
- incorrect medication: —  ·  missing medication: —
- dosage mismatch: —
- negation flips (vs. reference): —
- unsupported numbers: —
- missing information: {}

## Hallucination example: `mts_dialog_test_sum_2023_117`

*hallucination example*

ROUGE-L 22.9 · length ratio 0.59 · truncated False · degenerate False · hallucination 77.3 · negation-flip 25.0 · numerical consistency 100.0 · coverage 66.7

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
The patient is a 7-year-old Caucasian male who presents with a chief complaint of pain in his fingers, elbows, and neck for approximately 2 months.  He denies any history of fever, chills, weight loss, night sweats, joint effusion, rash, arthralgias, or visual changes.  He has had some mild diarrhea, but no abdominal pain, hematochezia, melena, dysuria, frequency, urgency, nocturia, or enuresis.  He has had some canker sores, but no stomatitis, glossitis, or pharyngitis.  He has had some seasonal allergies, but no urticaria, angioedema, or pruritus.  He has had some erythematous papules on his lower extremities, but no purpura, petechiae, or ecchymosis.  He has had some right upper quadrant tenderness, but no jaundice, hepatomegaly, splenomegaly, or adenopathy.
```

- unsupported entities (vs. transcript): abdominal pain, angioedema, blood in stool, blurred vision, bruising, chills, dysuria, erythema, itching, jaundice, joint pain, joint swelling, night sweats, nocturia, pharyngitis, urinary urgency, weight loss
- incorrect diagnosis: —  ·  missing diagnosis: —
- incorrect medication: —  ·  missing medication: loratadine
- dosage mismatch: —
- negation flips (vs. reference): diarrhea, joint pain
- unsupported numbers: —
- missing information: {"symptom": ["edema", "lymphadenopathy"], "medical_history": ["peptic ulcer disease"], "medication": ["loratadine"]}

## Incorrect medication / dosage example: `mts_dialog_test_sum_2023_67`

*incorrect medication / dosage example*

ROUGE-L 30.6 · length ratio 0.69 · truncated False · degenerate False · hallucination 69.2 · negation-flip 0.0 · numerical consistency 100.0 · coverage 85.7

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
The patient is a 39-year-old female with history of type 1 diabetes mellitus.  She comes in today for her followup appointment.  She states she has been doing well since her last visit approximately four months ago.  However, she has had some problems with her insulin pump for the last two weeks.  She has had difficulty setting up her pump and has had some highs and lows.  She denies any episodes of syncope, diaphoresis, tachycardia, palpitations, visual changes, confusion, or altered mental status.  She denies any polyuria, polydipsia, or polyphagia.  She does deny any recent exercise.  She works as a medical coder and has a busy schedule.  She has been following her diet and has been taking her medications as prescribed.  She has been seeing her primary care physician regularly.  She has had her labs checked.  Her LDL is 144.
```

- unsupported entities (vs. transcript): blood work, blurred vision, insulin, palpitations, polydipsia, polyphagia, polyuria, syncope, tachycardia
- incorrect diagnosis: —  ·  missing diagnosis: —
- incorrect medication: insulin  ·  missing medication: —
- dosage mismatch: —
- negation flips (vs. reference): —
- unsupported numbers: —
- missing information: {"diagnosis": ["diabetes"]}

## Negation error example: `mts_dialog_test_sum_2023_129`

*negation error example*

ROUGE-L 14.3 · length ratio 1.45 · truncated True · degenerate True · hallucination 14.3 · negation-flip 42.9 · numerical consistency 100.0 · coverage 50.0

**Transcript (excerpt)**

```
Doctor: Welcome back, sir! 
Patient: Thank you. 
Doctor: Today we are following up on several neurological symptoms that you have been experiencing. 
Patient: Okay. 
Doctor: What hand is your dominant hand? 
Patient: I am left handed. 
Doctor: And you are sixty three years old, right? 
Patient: That's right! 
Doctor: I would like to discuss each one of your multiple symptoms individually.
Patient: I have this pain in my neck. 
Doctor: Is the neck pain a new symptom? 
Patient: No. I have had this pain for. Oh, maybe fifteen years. At least. 
Doctor: Has the pain been progressing over the years or has it been the same? 
Patient: It is worse right now. 
Doctor: When did the pain become worse? 
 …
```

**Reference note**

```
The patient is a 63-year-old left-handed gentleman who presents for further evaluation of multiple neurological symptoms.  I asked him to discuss each symptom individually as he had a very hard time describing the nature of his problems.  He first mentioned that he has neck pain.  He states that he has had this for at least 15 years.  It is worse with movement.  It has progressed very slowly over the course of 15 years.  It is localized to the base of his neck and is sharp in quality.  He also endorses a history of gait instability.  This has been present for a few years and has been slightly progressively worsening.  He describes that he feels unsteady on his feet and "walks like a duck."  He has fallen about three or four times over the past year and a half. He also describes that he has numbness in his feet.  When I asked him to describe this in more detail, the numbness is actually r …
```

**Generated note**

```
The patient is a 63-year-old male who comes in for followup of his neurological symptoms.  He states that he has had neck pain for approximately 15 years.  He denies numbness, tingling, weakness, or fatigue.  He has had some difficulty walking and has fallen a few times.  He has had some difficulty buttoning his shirt and has had some difficulty holding onto objects.  He has had some difficulty with his memory.  He has had some difficulty with his balance.  He has had some difficulty with his gait.  He has had some difficulty with his lower extremities.  He has had some difficulty with his upper extremities.  He has had some difficulty with his hands.  He has had some difficulty with his feet.  He has had some difficulty with his lower back.  He has had some difficulty with his upper back.  He has had some difficulty with his shoulders.  He has had some difficulty with his elbows.  He has had some difficulty with his wrists.  He has had some difficulty with his knees.  He has had some difficulty with her hips.  He has had some difficulty with his ankles.  He has had some difficulty w …
```

- unsupported entities (vs. transcript): weakness
- incorrect diagnosis: —  ·  missing diagnosis: diabetes, neuropathy
- incorrect medication: —  ·  missing medication: —
- dosage mismatch: —
- negation flips (vs. reference): fatigue, numbness, weakness
- unsupported numbers: —
- missing information: {"symptom": ["depressive symptoms"], "medical_history": ["depression", "lumbar strain"], "diagnosis": ["dementia", "diabetes", "neuropathy"], "investigation": ["diagnostic workup"]}

## Numerical error example: `mts_dialog_test_sum_2023_135`

*numerical error example*

ROUGE-L 23.3 · length ratio 0.45 · truncated False · degenerate False · hallucination — · negation-flip — · numerical consistency 33.3 · coverage 0.0

**Transcript (excerpt)**

```
Doctor: Good afternoon, ma'am. Can you confirm your age for me, please? 
Patient: I'm thirty nine years old, doctor. 
Doctor: Good, and you identify as African American, correct?
Patient: Yes, that's correct. 
Doctor: Great, are you familiar with the details of your operation? 
Patient: Someone told me, but I don't really remember what happened. 
Doctor: Okay, well, we did a repair of septal deviation, but unfortunately, we ended up with a large septal perforation. 
Patient: Okay, that's what I remember, thank you.
Doctor: Have you been using your saline nasal wash? 
Patient: Yeah, I have. 
Doctor: How many times per day have you been using it? 
Patient: Um, usually two or three times a day. …
```

**Reference note**

```
The patient is a 39-year-old African-American female status post repair of septal deviation but unfortunately, ultimately ended with a large septal perforation.  The patient has been using saline nasal wash 2-3 times daily, however, she states that she still has discomfort in her nose with a "stretching" like pressure.  She says her nose is frequently dry and she occasionally has nosebleeds due to the dry nature of her nose.  She has no other complaints at this time.
```

**Generated note**

```
The patient is a 39-year-old black female who has had a history of nasal septum perforation for approximately 9 years.  She was seen by Dr. X on 02/04/2005 for evaluation and management of her condition.
```

- unsupported entities (vs. transcript): —
- incorrect diagnosis: —  ·  missing diagnosis: —
- incorrect medication: —  ·  missing medication: —
- dosage mismatch: —
- negation flips (vs. reference): —
- unsupported numbers: 02/04, 2005, 4, 9
- missing information: {"symptom": ["nosebleed"]}

## Missing information example: `mts_dialog_test_sum_2023_53`

*missing information example*

ROUGE-L 2.8 · length ratio 0.04 · truncated False · degenerate False · hallucination 66.7 · negation-flip 0.0 · numerical consistency 33.3 · coverage 14.3

**Transcript (excerpt)**

```
Doctor: Who do we have here?
Guest_family: Hi there, he is my son Jay!
Doctor: Hi Jay, how are you today?
Patient: I am okay doctor.
Doctor: Tell me what is going on?
Guest_family: We went ice skating almost 10 days back and he slipped on the ice and landed straight on his right shoulder. Since then, he has been complaining of issues with his shoulder. He is not able to raise his hand above his head and sometimes at night he complains of numbness in his right hand fingers. That kind of made me worried.
Doctor: Hm, okay. Mom, did he get hurt anywhere else too, like head, face or chest? 
Guest_family: No, he landed on his shoulder thankfully. Didn't hit his head. He was also wearing a helmet.
 …
```

**Reference note**

```
The patient is here today with his mom for several complaints.  Number one, he has been having issues with his right shoulder.  Approximately 10 days ago he fell, slipping on ice, did not hit his head but fell straight on his shoulder.  He has been having issues ever since.  He is having difficulties raising his arm over his head.  He does have some intermittent numbness in his fingers at night.  He is not taking any anti-inflammatories or pain relievers.  He is also complaining of a sore throat.  He did have some exposure to Strep and he has a long history of strep throat.  Denies any fevers, rashes, nausea, vomiting, diarrhea, and constipation.  He is also being seen for ADHD by Dr. B.  Adderall and Zoloft.  He takes these once a day.  He does notice when he does not take his medication.  He is doing well in school.  He is socializing well.  He is maintaining his weight and tolerating  …
```

**Generated note**

```
1.  Right shoulder injury. 2.  ADHD. 3.  Pharyngitis.
```

- unsupported entities (vs. transcript): adhd, trauma
- incorrect diagnosis: —  ·  missing diagnosis: —
- incorrect medication: —  ·  missing medication: amphetamine, sertraline
- dosage mismatch: —
- negation flips (vs. reference): —
- unsupported numbers: 2, 3
- missing information: {"symptom": ["constipation", "diarrhea", "falls", "fever", "nausea", "numbness"], "medication": ["amphetamine", "sertraline"], "investigation": ["weight measurement"]}

## Degenerate output example: `mts_dialog_test_sum_2023_82`

*degenerate output example*

ROUGE-L 2.1 · length ratio 20.77 · truncated True · degenerate True · hallucination 88.3 · negation-flip 0.0 · numerical consistency — · coverage 66.7

**Transcript (excerpt)**

```
Doctor: So, how long has your stomach been hurting?
Patient: It started two days back.
Doctor: Any nausea or vomiting?
Patient: No.
Doctor: Okay, any diarrhea?
Patient: Yes, I am having severe cramping with diarrhea. 
Doctor: Oh, okay. Any dizziness or weakness?
Patient: Yes, I am feeling very weak and tired all the time.
Doctor: Any cough with sputum? 
Patient: No cough at all.
Doctor: Okay. Are you having any pain or burning while passing urine?
Patient: No, I am fine.
Doctor: Hm, everything else looks fine. No problem there with your eyes, nose, throat, and other systems.
Patient: It's just my tummy which is hurting.
Doctor: Don't worry we will take care of it.
```

**Reference note**

```
Positive for diarrhea and abdominal pain, otherwise main other complaints are weakness.  She denies any cough, sputum production, or dysuria at this time.  Otherwise, a 10-system review is essentially negative.
```

**Generated note**

```
Significant for abdominal pain, diarrhea, crampy abdominal pain, weakness, fatigue, and dizziness.  Denies nausea, vomiting, dysuria, frequency, urgency, hematuria, dysuria, rhinorrhea, conjunctivitis, sore throat, arthralgias, myalgias, chest pain, shortness of breath, orthopnea, PND, fever, chills, night sweats, weight loss, change in bowel habits, joint pains, muscle pains, eye problems, ear problems, neck stiffness, extremity weakness, tremors, gait disturbances, visual changes, hearing changes, headaches, palpitations, syncope, vertigo, photophobia, phonophobia, diplopia, dysarthria, dysphagia, hoarseness, wheezing, stridor, edema, rash, pruritus, itching, urticaria, erythema nodosum, purpura, petechiae, ecchymosis, bruising, bleeding gums, epistaxis, hemoptysis, hematemesis, melena, hematochezia, rectal bleeding, perianal discomfort, urethritis, vaginitis, vulvovaginitis, menorrhagia, oligomenorrhea, amenorrhea, galactorrhea, nipple discharge, breast tenderness, mastodynia, nipple retraction, axillary lymphadenopathy, supraclavicular adenopathy, cervical adenopathy, inguinal ad …
```

- unsupported entities (vs. transcript): abdominal pain, benign prostatic hyperplasia, bleeding, blood in stool, blurred vision, breast pain, bruising, chest pain, chills, conjunctivitis, decreased libido, difficulty walking, double vision, dysphagia, dyspnea, dysuria, edema, erectile dysfunction, erythema, fever
- incorrect diagnosis: —  ·  missing diagnosis: —
- incorrect medication: —  ·  missing medication: —
- dosage mismatch: —
- negation flips (vs. reference): —
- unsupported numbers: —
- missing information: {"symptom": ["cough", "sputum"]}
