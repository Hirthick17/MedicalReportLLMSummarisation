# Example errors — sft

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

ROUGE-L 5.8 · length ratio 1.88 · truncated True · degenerate True · hallucination 0.0 · negation-flip 0.0 · numerical consistency — · coverage 8.3

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

## Hallucination example: `aci_bench_test_taskB_1_D2N116-aci`

*hallucination example*

ROUGE-L 12.9 · length ratio 1.17 · truncated True · degenerate False · hallucination 89.6 · negation-flip 0.0 · numerical consistency 0.0 · coverage 17.6

**Transcript (excerpt)**

```
[doctor] hey hi bobby how are you doing
[patient] i'm doing good how are you
[doctor] i'm doing fine so i understand you're here having some left or some right shoulder pain that you've had for a few weeks now
[patient] yeah it was i was doing some work in my backyard and a lot of different projects going on and you know i was obviously sore all over the next couple of days but my my right shoulder just keeps on bothering me and it keeps it's just really sore and it just has n't been going away
[doctor] okay so have you had ever had any pain in that shoulder before
[patient] a little bit i you know i i hurt that same shoulder because it's my my dominant hand my right hand i hurt it playing b …
```

**Reference note**

```
CHIEF COMPLAINT

Right shoulder pain.

HISTORY OF PRESENT ILLNESS

Bobby Flores is a 56-year-old male, right-hand-dominant, male who presents to the clinic today for the evaluation of right shoulder pain.

The onset of his pain began a few weeks ago, when he was performing different projects in his backyard. He states that he was sore all over the next couple of days. He locates his pain to the lateral aspect of his right shoulder. His pain is aggravated with movement. The patient denies any restriction with his arm. He also reports pain at night when he sleeps on his right side. The patient denies any numbness in his arm or hands. He has been taking Advil and icing his shoulder, which provides some relief. The patient reports a history of right shoulder pain when he was younger while playing baseball.

The patient also has complaints of bilateral foot and ankle pain. He attributes this  …
```

**Generated note**

```
CHIEF COMPLAINT

The patient presents with right shoulder pain for several weeks.

HISTORY OF PRESENT ILLNESS

The patient is a 45-year-old male who comes in today complaining of right shoulder pain for several weeks.  He states he has had some previous history of right shoulder pain from his past baseball injury.  The patient denies any numbness in his right arm.  He denies any weakness in his right arm.  He denies any paresthesias in his right arm.  He denies any fevers, chills, night sweats, weight loss, fatigue, or recent travel.  He denies any trauma to the right shoulder.  He denies any recent use of IV drugs.  He denies any tobacco use.  He denies any alcohol use.  He denies any allergies.  He denies any history of diabetes mellitus.  He denies any history of hypertension.  He denies any history of hyperlipidemia.  He denies any history of asthma.  He denies any history of chronic obstructive pulmonary disease (COPD).  He denies any history of gout.  He denies any history of kidney stones.  He denies any history of peptic ulcer disease.  He denies any history of gallbladder di …
```

- unsupported entities (vs. transcript): allergic rhinitis, aortic regurgitation, aortic stenosis, arrhythmia, asthma, atrial fibrillation, carpal tunnel syndrome, chills, cholecystitis, copd, coronary artery disease, deep vein thrombosis, diabetes, eczema, endocarditis, erythema, fatigue, fibromyalgia, gout, heart failure
- incorrect diagnosis: —  ·  missing diagnosis: rotator cuff tear
- incorrect medication: —  ·  missing medication: acetaminophen, cortisone injection, ibuprofen
- dosage mismatch: —
- negation flips (vs. reference): —
- unsupported numbers: 45
- missing information: {"symptom": ["ankle pain", "foot pain", "pain"], "diagnosis": ["dislocation", "rotator cuff tear"], "medication": ["acetaminophen", "cortisone injection", "ibuprofen"], "investigation": ["blood pressure measurement", "heart rate measurement", "mri", "oxygen saturation", "physical examination", "x-ray"]}

## Incorrect diagnosis example: `aci_bench_test_taskB_1_D2N100-virtscribe`

*incorrect diagnosis example*

ROUGE-L 29.1 · length ratio 0.75 · truncated False · degenerate False · hallucination 75.0 · negation-flip 16.7 · numerical consistency 38.5 · coverage 60.0

**Transcript (excerpt)**

```
[doctor] kayla ward , date of birth , 4/28/07 . mrn 3-8-4-9-2-0 . she's here for a new visit with her mother for acne located on the face , which started about two years ago and is present most every day . she has been using persa-gel and washing regularly , which is somewhat helpful . there are no associated symptoms including itching , bleeding , or pain . no additional past medical history . she lives with her parents and sister . they have a dog , bird , and bunnies . she is in 7th grade . she plays basketball and volleyball and tap . she wears sunscreen in the summer , spf 30 . no additional family history . hi kayla , i'm dr. juan price . i hear you are starting to get some acne on the …
```

**Reference note**

```
CHIEF COMPLAINT

New acne evaluation.

HISTORY OF PRESENT ILLNESS

Kayla Ward is a 15-year-old female who presents for new patient evaluation of acne located on the face. She is accompanied by her mother today.

Kayla states her acne started approximately 2 years ago and it is present almost every day. The patient’s mother notes that the most significant acne flares started in the fall when she was playing school sports. It does not tend to flare with her periods. Kayla reports that today is a good day for her acne. She denies any significant acne present on the chest or back. There are no associated symptoms, including no itching, bleeding, or pain.

The patient has been washing her face regularly. Her acne regimen includes washing her face in the morning with Persa-Gel and at night e.l.f. SuperClarify Cleanser along with toner and Persa-Gel. This regimen is somewhat helpful. She wears  …
```

**Generated note**

```
CHIEF COMPLAINT

Acne on the face.

HISTORY OF PRESENT ILLNESS

The patient is a 12-year-old female who presents for evaluation of acne on the face.  She states that she has had acne for approximately 2 years.  She denies any other symptoms such as itching, bleeding, or pain.  She has been using Persa-Gel and washing regularly, which seems to be somewhat helpful.  She denies any history of allergies, asthma, eczema, or other chronic illnesses.  She lives with her parents and sister.  They have a dog, bird, and rabbits.  She is in 7th grade.  She plays basketball, volleyball, and tap.  She uses SPF 30 sunscreen during the summer.  No significant family history.  The patient denies any history of trauma, surgery, or hospitalizations.  She denies any history of smoking or alcohol use.

REVIEW OF SYSTEMS

Significant for dermatology.  Negative for respiratory, cardiovascular, gastrointestinal, genitourinary, musculoskeletal, neurological, hematologic, lymphatic, endocrine, psychiatric, and immunological systems.

PHYSICAL EXAM

VITAL SIGNS
Blood pressure: 110/70.
Temperature: 98.6°F.
Pul …
```

- unsupported entities (vs. transcript): allergic rhinitis, asthma, blood pressure measurement, blood work, eczema, erythema, heart rate measurement, infection, lymphadenopathy, murmur, oxygen saturation, physical examination, respiratory rate, trauma, weakness
- incorrect diagnosis: eczema, infection  ·  missing diagnosis: —
- incorrect medication: —  ·  missing medication: tretinoin
- dosage mismatch: —
- negation flips (vs. reference): adapalene
- unsupported numbers: 110, 110/70, 12, 16, 70, 80, 98.6, 99
- missing information: {"symptom": ["falls", "flare"], "medication": ["tretinoin"], "investigation": ["diagnostic workup"]}

## Incorrect medication / dosage example: `aci_bench_test_taskB_1_D2N119-aci`

*incorrect medication / dosage example*

ROUGE-L 7.2 · length ratio 1.42 · truncated True · degenerate False · hallucination 86.7 · negation-flip 0.0 · numerical consistency 0.0 · coverage 21.4

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

- unsupported entities (vs. transcript): amitriptyline, amphetamine, aripiprazole, atomoxetine, budesonide, budesonide/formoterol, bupropion, cetirizine, citalopram, desvenlafaxine, diphenhydramine, duloxetine, escitalopram, fluticasone/salmeterol, ipratropium, levocetirizine, loratadine, methylphenidate, mirtazapine, mometasone
- incorrect diagnosis: —  ·  missing diagnosis: —
- incorrect medication: amitriptyline, amphetamine, aripiprazole, atomoxetine, budesonide, budesonide/formoterol, bupropion, cetirizine, citalopram, desvenlafaxine, diphenhydramine, duloxetine, escitalopram, fluticasone/salmeterol, ipratropium, levocetirizine, loratadine, methylphenidate, mirtazapine, mometasone, montelukast, nortriptyline, paroxetine, risperidone, tiotropium, venlafaxine  ·  missing medication: —
- dosage mismatch: —
- negation flips (vs. reference): —
- unsupported numbers: 35
- missing information: {"symptom": ["cough", "lymphadenopathy", "murmur", "wheezing"], "medical_history": ["allergic rhinitis"], "investigation": ["blood pressure measurement", "heart rate measurement", "oxygen saturation", "physical examination", "pulmonary function test", "respiratory rate"]}

## Negation error example: `aci_bench_test_taskB_1_D2N106-aci`

*negation error example*

ROUGE-L 12.6 · length ratio 1.33 · truncated True · degenerate False · hallucination 73.8 · negation-flip 66.7 · numerical consistency 100.0 · coverage 50.0

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

- unsupported entities (vs. transcript): abdominal pain, blood in stool, bradycardia, chills, conjunctivitis, constipation, copd, dysuria, fatigue, fever, hematuria, hemoptysis, itching, joint pain, joint swelling, muscle pain, night sweats, nocturia, nosebleed, orthopnea
- incorrect diagnosis: —  ·  missing diagnosis: —
- incorrect medication: —  ·  missing medication: montelukast
- dosage mismatch: —
- negation flips (vs. reference): allergic rhinitis, angioedema, asthma, nausea, rash, vomiting
- unsupported numbers: —
- missing information: {"symptom": ["flare", "throat swelling", "wheezing"], "medication": ["montelukast"], "investigation": ["allergy testing", "diagnostic workup", "oxygen saturation", "pulmonary function test", "x-ray"]}

## Numerical error example: `aci_bench_test_taskB_1_D2N108-aci`

*numerical error example*

ROUGE-L 30.1 · length ratio 1.24 · truncated False · degenerate False · hallucination 39.1 · negation-flip 0.0 · numerical consistency 35.3 · coverage 82.4

**Transcript (excerpt)**

```
[doctor] hey gregory good to see you today so take a look at my notes and i see that you're here you've had a nonhealing foot ulcer so can you tell me how you're doing how long have you had it what's going on with it
[patient] sure so i've had it for about two months now and it's recently become red and is draining so i was concerned about how it's healed
[doctor] okay and when you when you got it would you have any trauma to your foot or it just just did it pop up all of a sudden
[patient] i think i may have gotten it from walking barefoot on the beach
[doctor] okay alright and i saw you you did see your pcp before you came in did they put you on antibiotics
[patient] they did start me on s …
```

**Reference note**

```
CHIEF COMPLAINT

Right foot ulcer.

HISTORY OF PRESENT ILLNESS

Gregory Hernandez is a pleasant 40-year-old male who presents to the clinic today for the evaluation of a non-healing right foot ulcer. Onset of ulcer was approximately 2 months ago after walking barefoot on the beach. He reports the ulcer has recently become red and is draining. At times he will also experience throbbing pain. He has seen his primary care physician and was prescribed antibiotics, however, he has not started them yet and does not recall the name of the medication.

The patient is a diabetic. He is taking medication for this, however, he does not monitor his blood sugar consistently. His last A1C was around 10.

MEDICAL HISTORY

Patient reports history of diabetes.

REVIEW OF SYSTEMS

Musculoskeletal: Reports right foot pain.
Skin: Reports right foot ulcer with redness and drainage.

VITALS

Vital signs are n …
```

**Generated note**

```
CHIEF COMPLAINT

The patient is a 62-year-old male who presents with a chief complaint of a nonhealing foot ulcer.

HISTORY OF PRESENT ILLNESS

The patient states he has had his foot ulcer for approximately 2 months.  He states that it has been red and draining lately.  The patient denies any history of trauma to the foot.  He states that he thinks he got it from walking barefoot on the beach.  He has seen his primary care physician prior to this visit and she has started him on some antibiotic therapy.  He has not picked up the medications yet.  He does not remember the exact name of the antibiotic.  He has had it before.  He has been to Dewey Beach in his ambulance.  He states that it throbs sometimes.  It does not hurt specifically.  Sometimes it feels like it throbs.  His main concern is that it has started to drain and it looks a little red.  He has never had that before.  He has diabetes.  He takes his medications.  He does not check his sugars very often.  He does not know what his A1C is.  He thinks it is around 10.  He needs to go back and see his PCP to get his diabetes und …
```

- unsupported entities (vs. transcript): ankle-brachial index, blood glucose, blood pressure measurement, bruising, chills, crepitus, heart rate measurement, respiratory rate, warmth
- incorrect diagnosis: —  ·  missing diagnosis: —
- incorrect medication: —  ·  missing medication: —
- dosage mismatch: —
- negation flips (vs. reference): —
- unsupported numbers: 130, 130/80, 18, 4, 5, 6, 62, 78, 8, 80, 98.6
- missing information: {"symptom": ["foot pain"], "medical_history": ["peptic ulcer disease"], "investigation": ["vital signs"]}

## Missing information example: `aci_bench_test_taskB_1_D2N118-aci`

*missing information example*

ROUGE-L 5.8 · length ratio 1.88 · truncated True · degenerate True · hallucination 0.0 · negation-flip 0.0 · numerical consistency — · coverage 8.3

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

ROUGE-L 19.9 · length ratio 1.07 · truncated True · degenerate True · hallucination 86.6 · negation-flip 30.0 · numerical consistency 100.0 · coverage 58.8

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

ROUGE-L 6.0 · length ratio 1.75 · truncated True · degenerate True · hallucination 0.0 · negation-flip 16.7 · numerical consistency 100.0 · coverage 27.3

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

ROUGE-L 6.5 · length ratio 1.72 · truncated True · degenerate False · hallucination 97.9 · negation-flip 0.0 · numerical consistency 100.0 · coverage 11.1

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

- unsupported entities (vs. transcript): allergic rhinitis, appendicitis, arrhythmia, asthma, atrial fibrillation, bradycardia, bronchitis, cancer, constipation, diabetes, diarrhea, dysmenorrhea, dysuria, eczema, edema, endometriosis, gastritis, gastroenteritis, hematuria, hypertension
- incorrect diagnosis: —  ·  missing diagnosis: myocardial infarction
- incorrect medication: —  ·  missing medication: —
- dosage mismatch: —
- negation flips (vs. reference): —
- unsupported numbers: —
- missing information: {"symptom": ["murmur"], "medical_history": ["myocardial infarction"], "investigation": ["blood pressure measurement", "genetic testing", "hemoglobin a1c", "lipid panel", "metabolic panel", "physical examination"]}

## Incorrect diagnosis example: `aci_bench_test_taskC_2_D2N143-virtscribe`

*incorrect diagnosis example*

ROUGE-L 9.1 · length ratio 1.00 · truncated True · degenerate True · hallucination 95.6 · negation-flip 25.0 · numerical consistency 0.0 · coverage 44.4

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

## Incorrect medication / dosage example: `aci_bench_test_taskC_2_D2N131-virtassist`

*incorrect medication / dosage example*

ROUGE-L 30.3 · length ratio 0.75 · truncated False · degenerate False · hallucination 17.6 · negation-flip 11.1 · numerical consistency 38.5 · coverage 68.2

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

The patient is a 26-year-old female who comes in for a hypertension check.

HISTORY OF PRESENT ILLNESS

Susan is a 26-year-old female who comes in for a hypertension check.  She has been having difficulty managing her hypertension.  She has been on Norvasc 10 mg daily.  Her blood pressures have been elevated at home.  She denies headaches, chest pains, shortness of breath.  She has had a history of kidney transplant.  She is on immunosuppressive therapy.  She denies any other complaints.

REVIEW OF SYSTEMS

CONSTITUTIONAL: Negative.
NECK: Supple.
HEENT: Negative.
CARDIOVASCULAR: Irregular rhythm, S2, Grade 2/6 systolic ejection murmur.
RESPIRATORY: Negative.
GASTROINTESTINAL: Negative.
GENITOURINARY: Negative.
MUSCULOSKELETAL: Negative.
SKIN: Negative.
LYMPHATIC: Negative.

PHYSICAL EXAM

GENERAL: The patient appears comfortable and in no apparent distress.
NECK: Supple.
HEART: Irregular rhythm, S2, Grade 2/6 systolic ejection murmur.
LUNGS: Bilateral lungs clear to auscultation bilaterally.
ABDOMEN: Soft, non-tender, negative bowel sounds.
EXTREMITIES: No edema note …
```

- unsupported entities (vs. transcript): electrocardiogram, immunosuppressant, pain
- incorrect diagnosis: —  ·  missing diagnosis: —
- incorrect medication: immunosuppressant  ·  missing medication: —
- dosage mismatch: —
- negation flips (vs. reference): headache
- unsupported numbers: 0.8, 0.9, 1, 1.2, 100, 160, 160/100, 3
- missing information: {"symptom": ["crackles", "dyspnea on exertion", "lymphadenopathy", "rhonchi", "wheezing"], "investigation": ["diagnostic workup", "home monitoring"]}

## Negation error example: `aci_bench_test_taskC_2_D2N153-aci`

*negation error example*

ROUGE-L 12.2 · length ratio 1.48 · truncated True · degenerate True · hallucination 42.9 · negation-flip 83.3 · numerical consistency 66.7 · coverage 33.3

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

ROUGE-L 25.9 · length ratio 1.14 · truncated False · degenerate False · hallucination 56.7 · negation-flip 7.1 · numerical consistency 22.2 · coverage 77.8

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

The patient is a 49-year-old female who comes in for followup of her chronic problems.  She states that she has had some exacerbation of her osteoarthritis, particularly in her elbows, which has been bothering her.  She denies any other joint pains.  She has had some numbness and tingling in her hands while typing.  She has had some history of gout, which has been controlled by medications.  She has had some history of psoriasis, which has been under control.  She has had some history of gout, which has been controlled by medications.  She has had some history of psoriasis, which has been under control.

HISTORY OF PRESENT ILLNESS

The patient is a 49-year-old female who comes in for followup of her chronic problems.  She states that she has had some exacerbation of her osteoarthritis, particularly in her elbows, which has been bothering her.  She denies any other joint pains.  She has had some numbness and tingling in her hands while typing.  She has had some history of gout, which has been controlled by medications.  She has had some history of psoriasis, which has …
```

- unsupported entities (vs. transcript): adverse drug reaction, blood pressure measurement, complete blood count, crackles, crp, diagnostic workup, erythema, esr, heart rate measurement, murmur, numbness, respiratory rate, rhonchi, tremor, warmth, weakness, wheezing
- incorrect diagnosis: adverse drug reaction  ·  missing diagnosis: —
- incorrect medication: —  ·  missing medication: —
- dosage mismatch: —
- negation flips (vs. reference): joint pain
- unsupported numbers: 1.5, 130, 130/80, 14, 160, 18, 20, 24, 36.8, 6, 7.9, 78, 80, 98.2
- missing information: {"symptom": ["edema", "flare"], "investigation": ["physical examination", "x-ray"]}

## Missing information example: `aci_bench_test_taskC_2_D2N156-aci`

*missing information example*

ROUGE-L 9.4 · length ratio 1.20 · truncated True · degenerate True · hallucination 33.3 · negation-flip 0.0 · numerical consistency 50.0 · coverage 11.1

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

## Degenerate output example: `aci_bench_test_taskC_2_D2N143-virtscribe`

*degenerate output example*

ROUGE-L 9.1 · length ratio 1.00 · truncated True · degenerate True · hallucination 95.6 · negation-flip 25.0 · numerical consistency 0.0 · coverage 44.4

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

ROUGE-L 5.4 · length ratio 2.58 · truncated True · degenerate True · hallucination 85.7 · negation-flip 0.0 · numerical consistency 0.0 · coverage 40.0

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

ROUGE-L 5.7 · length ratio 1.65 · truncated True · degenerate False · hallucination 88.1 · negation-flip 20.0 · numerical consistency 50.0 · coverage 35.7

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

ROUGE-L 20.1 · length ratio 1.05 · truncated True · degenerate True · hallucination 60.0 · negation-flip 20.0 · numerical consistency 100.0 · coverage 30.3

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

ROUGE-L 14.2 · length ratio 0.61 · truncated True · degenerate True · hallucination 71.8 · negation-flip 21.1 · numerical consistency 57.1 · coverage 57.6

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

## Numerical error example: `aci_bench_test_taskC_3_D2N168-virtassist`

*numerical error example*

ROUGE-L 26.4 · length ratio 1.12 · truncated False · degenerate False · hallucination 33.3 · negation-flip 0.0 · numerical consistency 23.8 · coverage 68.2

**Transcript (excerpt)**

```
[doctor] hi diane , how are you ?
[patient] i'm doing okay , how are you ?
[doctor] i'm doin' okay . so i know the nurse told you about dax and i'd like to tell dax a little bit about you okay ?
[patient] okay .
[doctor] diane is a 28 year old female with a past medical history , significant for , depression and hypertension who presents for emergency room follow-up .
[doctor] so diane what's going on ? i heard that your- your blood pressure was really high in the emergency room . what happened ?
[patient] yeah , so i ended up going for a walk , um , yesterday 'cause it was sunny and it was really great . and i just felt really light-headed , um , and i started to fall a bit , and , um , luc …
```

**Reference note**

```
CHIEF COMPLAINT

Emergency room follow-up.

HISTORY OF PRESENT ILLNESS

Ms. Diane Baker is a 28-year-old female with a past medical history significant for depression, and hypertension, who presents for emergency room follow-up.

The patient went for a walk yesterday and began to feel lightheaded. She started to fall, however she was with her boyfriend, who caught her. She presented to the emergency room after this. While in the emergency room, her blood pressure was nearly 200 and she had a headache.

Her blood pressure is typically normal, however will become elevated approximately one week a month. She notes it is typically elevated because she is traveling a lot that week for work. While traveling, she is not eating as well and does not monitor her blood pressure. The patient is taking her lisinopril as prescribed.

Regarding her depression, she states she is doing well. Last year sh …
```

**Generated note**

```
CHIEF COMPLAINT

The patient is a 28-year-old female who comes in for an ER followup.

HISTORY OF PRESENT ILLNESS

The patient is a 28-year-old female with a past medical history significant for depression and hypertension. She presented to the Emergency Room after she had a syncopal episode while walking outside. She has had a history of hypertension which has been poorly controlled. She denies any chest pain or dyspnea. She has had headaches and lightheadedness. She has had her blood pressure checked by her boyfriend and it was around 190/90. She has been on Lisinopril 10 mg daily. She has been having her blood pressure checked weekly. She has been traveling a lot lately and has not been eating well. She has been taking her Lisinopril. She has been on therapy for depression for the past year. She has been going once a week. She has been doing well with her depression. She has a good support system including her boyfriend, mother, and brother. She has had a review of systems done. She has had some nasal congestion due to seasonal allergies. She has had no other complaints.

REVIEW O …
```

- unsupported entities (vs. transcript): diagnostic workup, electrocardiogram, heart rate measurement, left ventricular hypertrophy, mitral regurgitation, pain, respiratory rate
- incorrect diagnosis: mitral regurgitation  ·  missing diagnosis: —
- incorrect medication: —  ·  missing medication: —
- dosage mismatch: [{"drug": "lisinopril", "predicted": "10 mg", "source": ["40 mg", "40 milligrams"]}]
- negation flips (vs. reference): —
- unsupported numbers: 10, 100, 16, 170, 170/100, 190, 190/90, 3, 4, 5, 7, 8, 80, 9, 90
- missing information: {"symptom": ["crackles", "falls", "loss of appetite", "rhonchi", "wheezing"], "investigation": ["home monitoring", "vital signs"]}

## Missing information example: `aci_bench_test_taskC_3_D2N197-aci`

*missing information example*

ROUGE-L 6.2 · length ratio 2.39 · truncated True · degenerate True · hallucination 0.0 · negation-flip 0.0 · numerical consistency 100.0 · coverage 15.0

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

The patient states that she has been having headaches lately.  She has been having headaches for several months.  She has been having headaches for several months.  She has been having headaches for several months.  She has been having headaches for several months.  She has been having headaches for several months.  She has been having headaches for several months.  She has been having headaches for several months.  She has been having headaches for several months.  She has been having headaches for several months.  She has been having headaches for several months.  She has been having headaches for several months.  She has been having headaches for several months.  She has been having headaches for several months.  She has been having headaches for several months.  She has been having headaches for several months.  She has been having headaches for several months.  She has been having headaches for several mon …
```

- unsupported entities (vs. transcript): —
- incorrect diagnosis: —  ·  missing diagnosis: —
- incorrect medication: —  ·  missing medication: acetaminophen, lisinopril
- dosage mismatch: —
- negation flips (vs. reference): —
- unsupported numbers: —
- missing information: {"symptom": ["cough", "lymphadenopathy", "nasal congestion", "pain", "polyuria", "rhinorrhea"], "medical_history": ["allergic rhinitis", "migraine"], "medication": ["acetaminophen", "lisinopril"], "investigation": ["blood glucose", "blood pressure measurement", "blood work", "diagnostic workup", "hemoglobin a1c", "home monitoring"]}

## Degenerate output example: `aci_bench_test_taskC_3_D2N178-virtscribe`

*degenerate output example*

ROUGE-L 14.2 · length ratio 0.61 · truncated True · degenerate True · hallucination 71.8 · negation-flip 21.1 · numerical consistency 57.1 · coverage 57.6

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

## Best ROUGE-L: `mts_dialog_test_chat_2023_183`

*highest ROUGE-L in the split*

ROUGE-L 100.0 · length ratio 1.00 · truncated False · degenerate False · hallucination 0.0 · negation-flip 0.0 · numerical consistency — · coverage 100.0

**Transcript (excerpt)**

```
Doctor: So, let's see what we have here. I have down that you're not allergic to any medications. 
Patient: Correct, no drug allergies.  
Doctor: Good, great.
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

## Worst ROUGE-L: `mts_dialog_test_chat_2023_5`

*lowest ROUGE-L in the split*

ROUGE-L 0.0 · length ratio 0.25 · truncated False · degenerate False · hallucination — · negation-flip — · numerical consistency — · coverage —

**Transcript (excerpt)**

```
Doctor: It is good to see you again. How have you been?
Patient: It is good to see you too. I have been good. 
Doctor: Have anything changes to your medical history or social history since the last time I saw you? 
Patient: No. No changes.
```

**Reference note**

```
Reviewed and remained unchanged.
```

**Generated note**

```
Unremarkable.
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

ROUGE-L 6.7 · length ratio 2.24 · truncated True · degenerate False · hallucination 95.3 · negation-flip — · numerical consistency — · coverage 0.0

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

- unsupported entities (vs. transcript): abdominal pain, blood in stool, blurred vision, breast pain, burning sensation, chills, constipation, diarrhea, dizziness, double vision, dysphagia, dysuria, edema, fever, headache, hematuria, hoarseness, itching, joint pain, joint swelling
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

ROUGE-L 8.4 · length ratio 3.07 · truncated True · degenerate True · hallucination 50.0 · negation-flip 33.3 · numerical consistency 100.0 · coverage 75.0

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

ROUGE-L 9.1 · length ratio 4.03 · truncated True · degenerate True · hallucination 50.0 · negation-flip 0.0 · numerical consistency 37.5 · coverage 33.3

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
- unsupported numbers: 10, 11, 12, 2008, 2009, 2010, 4, 6, 8, 9
- missing information: {"symptom": ["bleeding"], "diagnosis": ["infection"]}

## Missing information example: `mts_dialog_test_chat_2023_103`

*missing information example*

ROUGE-L 6.7 · length ratio 2.24 · truncated True · degenerate False · hallucination 95.3 · negation-flip — · numerical consistency — · coverage 0.0

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

- unsupported entities (vs. transcript): abdominal pain, blood in stool, blurred vision, breast pain, burning sensation, chills, constipation, diarrhea, dizziness, double vision, dysphagia, dysuria, edema, fever, headache, hematuria, hoarseness, itching, joint pain, joint swelling
- incorrect diagnosis: —  ·  missing diagnosis: —
- incorrect medication: —  ·  missing medication: naproxen
- dosage mismatch: —
- negation flips (vs. reference): —
- unsupported numbers: —
- missing information: {"symptom": ["falls", "insomnia", "snoring", "tingling"], "medication": ["naproxen"]}

## Degenerate output example: `mts_dialog_test_chat_2023_11`

*degenerate output example*

ROUGE-L 1.9 · length ratio 10.48 · truncated True · degenerate True · hallucination 95.2 · negation-flip 25.0 · numerical consistency — · coverage 80.0

**Transcript (excerpt)**

```
Doctor: Did he get his B C G vaccine?
Guest_family: Yes, he did back in the Philippines before starting his elementary school. 
Doctor: Okay, did you have his immunization records?
Guest_family_2: Yes, we submitted it at the front desk.
Doctor: Okay, how long has he been complaining of uneasiness in his stomach?
Guest_family_2: For a few days.
Doctor: Any history of liver problems or gallbladder stones?
Guest_family: No, he had his physical and blood tests and everything came out normal.
Doctor: Okay, good. Any fever or chills?
Guest_family: No.
Doctor: Any history of ulcers?
Guest_family_2: No.
```

**Reference note**

```
Non-contributory. The patient denied fever, chills, ulcers, liver disease or history of gallstones. Vaccines: The patient was vaccinated with BCG before starting elementary school in the Philippines.
```

**Generated note**

```
Significant for immunizations including BCG.  Negative for fever, chills, abdominal pain, nausea, vomiting, diarrhea, dysuria, frequency, urgency, hematuria, nocturia, orthostatic hypotension, syncope, palpitations, chest pain, shortness of breath, cough, wheezing, sputum production, hemoptysis, pleuritic chest pain, joint pains, arthralgias, myalgias, rash, pruritus, urticaria, erythema nodosum, petechiae, purpura, conjunctivitis, photophobia, diplopia, blurred vision, headache, dizziness, vertigo, tinnitus, hearing loss, dysphagia, hoarseness, odynophagia, epigastric pain, right upper quadrant pain, left upper quadrant pain, jaundice, icterus, scleral icterus, hepatomegaly, splenomegaly, lymphadenopathy, weight loss, fatigue, weakness, anorexia, night sweats, weight gain, edema, pedal edema, pitting edema, ascites, periorbital edema, facial edema, extremity swelling, muscle weakness, tremors, fasciculations, paralysis, numbness, tingling, burning sensation, cold intolerance, heat intolerance, hyperhidrosis, diaphoresis, menorrhagia, oligomenorrhea, amenorrhea, galactorrhea, gynecom …
```

- unsupported entities (vs. transcript): abdominal pain, anxiety, bleeding, blurred vision, burning sensation, cancer, cataract, chest pain, cold intolerance, confusion, conjunctivitis, cough, crepitus, decreased libido, depression, diarrhea, difficulty walking, dizziness, double vision, dysphagia
- incorrect diagnosis: —  ·  missing diagnosis: —
- incorrect medication: —  ·  missing medication: —
- dosage mismatch: —
- negation flips (vs. reference): peptic ulcer disease
- unsupported numbers: —
- missing information: {"medical_history": ["cholecystitis"]}

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

## Worst ROUGE-L: `mts_dialog_test_sum_2023_3`

*lowest ROUGE-L in the split*

ROUGE-L 0.0 · length ratio 1.33 · truncated False · degenerate False · hallucination 0.0 · negation-flip — · numerical consistency — · coverage —

**Transcript (excerpt)**

```
Doctor: Do you have any known history of allergies?
Patient: No, I don't have any allergies.
```

**Reference note**

```
None by history.
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

## Incorrect medication / dosage example: `mts_dialog_test_sum_2023_31`

*incorrect medication / dosage example*

ROUGE-L 30.7 · length ratio 0.96 · truncated False · degenerate False · hallucination 26.3 · negation-flip 0.0 · numerical consistency 100.0 · coverage 93.8

**Transcript (excerpt)**

```
Guest_clinician: What medications is he on?  
Doctor: He's currently taking Nexium forty M G daily for esophageal reflux, Cozaar one hundred M G and Norvasc ten M G daily for hypertension, Allegra one eighty daily for allergic rhinitis, and Flovent and Serevent as needed for recurring bronchitis. 
Guest_clinician: Is he a smoker? 
Doctor: No.  
Guest_clinician: How often does he get bronchitis? 
Doctor: It looks like he last had it a year ago. 
Guest_clinician: I see. 
Doctor: He's also on Xalatan drops for glaucoma and Ativan one M G, Advair ten M G, and Paxil twenty five M G nightly for anxiety, depression, and sleep disturbances. 
Guest_clinician: Okay. I think I got it all down.
```

**Reference note**

```
Hypertension treated with Cozaar 100 mg daily and Norvasc 10 mg daily.  Esophageal reflux treated with Nexium 40 mg daily.  Allergic rhinitis treated with Allegra 180 mg daily.  Sleep disturbances, depression and anxiety treated with Paxil 25 mg daily, Advair 10 mg nightly and Ativan 1 mg nightly.  Glaucoma treated with Xalatan drops.  History of chronic bronchitis with no smoking history for which he uses p.r.n. Flovent and Serevent.
```

**Generated note**

```
The patient is on Nexium 40 mg daily for GERD, Cozaar 100 mg and Norvasc 10 mg daily for hypertension, Allegra 180 mg daily for allergic rhinitis, Flovent and Serevent PRN for chronic bronchitis, Xalatan eye drops for glaucoma, Ativan 1 mg PRN for anxiety, Advair 10 mg PRN for asthma, and Paxil 25 mg at bedtime for depression and insomnia.  The patient denies smoking history.
```

- unsupported entities (vs. transcript): artificial tears, asthma, copd, gerd, insomnia
- incorrect diagnosis: —  ·  missing diagnosis: —
- incorrect medication: artificial tears  ·  missing medication: —
- dosage mismatch: —
- negation flips (vs. reference): —
- unsupported numbers: —
- missing information: {"symptom": ["heartburn"]}

## Negation error example: `mts_dialog_test_sum_2023_2`

*negation error example*

ROUGE-L 9.6 · length ratio 2.63 · truncated True · degenerate True · hallucination 85.4 · negation-flip 37.5 · numerical consistency 100.0 · coverage 34.8

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

ROUGE-L 13.3 · length ratio 2.81 · truncated True · degenerate True · hallucination 28.6 · negation-flip 0.0 · numerical consistency 80.0 · coverage 42.9

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

# Split: val_check

## Best ROUGE-L: `mts_dialog_validation_3`

*highest ROUGE-L in the split*

ROUGE-L 100.0 · length ratio 1.00 · truncated False · degenerate False · hallucination 0.0 · negation-flip 0.0 · numerical consistency — · coverage 100.0

**Transcript (excerpt)**

```
Doctor: How've you been treating your acne? 
Patient: The dermatologist started me on Accutane.  
Doctor: How long have you been on Accutane? 
Patient: About three months now. 
Doctor: Have you noticed any improvements since starting it? 
Patient: Yeah, kinda.
```

**Reference note**

```
Accutane.
```

**Generated note**

```
Accutane.
```

- unsupported entities (vs. transcript): —
- incorrect diagnosis: —  ·  missing diagnosis: —
- incorrect medication: —  ·  missing medication: —
- dosage mismatch: —
- negation flips (vs. reference): —
- unsupported numbers: —
- missing information: {}

## Worst ROUGE-L: `mts_dialog_validation_2`

*lowest ROUGE-L in the split*

ROUGE-L 0.0 · length ratio 0.29 · truncated False · degenerate False · hallucination — · negation-flip — · numerical consistency — · coverage —

**Transcript (excerpt)**

```
Doctor: Has anything changed in your medical history since you last visit on April fifteenth two thousand five?
Patient: What do you mean by that?
Doctor: Have you been diagnosed with any new medical conditions, or are you experiencing any new symptoms?
Patient: Oh, no, nothing like that.
```

**Reference note**

```
Essentially unchanged from her visit of 04/15/2005.
```

**Generated note**

```
Otherwise negative.
```

- unsupported entities (vs. transcript): —
- incorrect diagnosis: —  ·  missing diagnosis: —
- incorrect medication: —  ·  missing medication: —
- dosage mismatch: —
- negation flips (vs. reference): —
- unsupported numbers: —
- missing information: {}

## Hallucination example: `aci_bench_validation_D2N074-virtscribe`

*hallucination example*

ROUGE-L 9.9 · length ratio 0.86 · truncated True · degenerate False · hallucination 83.3 · negation-flip 55.6 · numerical consistency 100.0 · coverage 39.1

**Transcript (excerpt)**

```
[doctor] patient , bruce ward . date of birth 5/21/1969 . please use my neuro consult template . this is a 52-year-old male with dia- newly diagnosed pituitary lesion . the patient is seen in consultation at the request of dr. henry howard for possible surgical intervention . mr . ward presented to his primary care provider , dr. howard , on 3/1/21 complaining of worsening headaches over the past few months . he denied any trouble with headaches in the past . his past clinical history is unremarkable .
[doctor] worked out for worsening headaches was initiated with brain mri and serology where pituitary lesion was incidentally discovered . i personally reviewed the labs dated 3/3/21 including …
```

**Reference note**

```
CHIEF COMPLAINT

Pituitary lesion.

HISTORY OF PRESENT ILLNESS

Bruce Ward is a 52-year-old male with a pituitary lesion. The patient is seen in consultation at the request of Dr. Henry Howard for possible surgical intervention.

The patient presented to his primary care provider, Dr. Howard, on 03/01/2021 complaining of worsening headaches over the past few months. He denied any trouble with headaches in the past. Further work up of headaches with MRI of the brain revealed the pituitary lesion.

Mr. Ward reports headaches started about 3 months ago, at which point they were around 3 out of 10 in severity. They have gradually worsened over time and now he rates them at about 6/10. The headaches do tend to be worse in the morning and feel like a dull ache behind the eyes. They tend to last a few hours at a time, and nothing makes them particularly worse or better. Tylenol failed to improv …
```

**Generated note**

```
CHIEF COMPLAINT

The patient is a 52-year-old male with a chief complaint of worsening headaches over the past few months.  He denies any previous headache complaints.  His past clinical history is unremarkable.

HISTORY OF PRESENT ILLNESS

Mr. Ward is a 52-year-old male who presents to the office for evaluation of headaches.  The patient states that he has had worsening headaches over the past several months.  He denies any previous headache complaints.  He has no history of allergies, asthma, hypertension, diabetes mellitus, or any other chronic illnesses.  He does not take any medications.  He denies tobacco use, alcohol use, or illicit drug use.  He is married and works as a computer programmer.  He has no known family history of neurological disorders.  He denies any recent fevers, chills, or weight changes.  He denies any recent trauma or falls.  He denies any recent visual changes, diplopia, dysarthria, dysphasia, or weakness.  He denies any recent syncope or near syncope episodes.  He denies any recent paresthesias or numbness.  He denies any recent bowel/bladder dysfunction. …
```

- unsupported entities (vs. transcript): abdominal pain, allergic rhinitis, anxiety, anxiety symptoms, arrhythmia, asthma, blood in stool, blurred vision, chest pain, chills, confusion, cough, cramping, depression, diabetes, difficulty walking, dizziness, double vision, dyspnea, dysuria
- incorrect diagnosis: —  ·  missing diagnosis: infection, stroke
- incorrect medication: —  ·  missing medication: acetaminophen
- dosage mismatch: —
- negation flips (vs. reference): numbness, pain, slurred speech, tobacco use, weakness
- unsupported numbers: —
- missing information: {"symptom": ["neck pain", "seizure"], "diagnosis": ["infection", "myocardial infarction", "stroke"], "medication": ["acetaminophen"], "investigation": ["blood work", "complete blood count", "crp", "diagnostic workup", "eye exam", "mri"]}

## Incorrect diagnosis example: `aci_bench_validation_D2N068-virtassist`

*incorrect diagnosis example*

ROUGE-L 7.6 · length ratio 0.71 · truncated True · degenerate True · hallucination 81.4 · negation-flip 13.3 · numerical consistency 100.0 · coverage 48.4

**Transcript (excerpt)**

```
[doctor] hi , brian . how are you ?
[patient] hi , good to see you .
[doctor] it's good to see you too . so , i know the nurse told you a little bit about dax .
[patient] mm-hmm .
[doctor] i'd like to tell dax about you , okay ?
[patient] sure .
[doctor] so , brian is a 58 year old male with a past medical history significant for congestive heart failure and hypertension , who presents today for follow-up of his chronic problems . so , brian , it's been a little while i've seen you .
[patient] mm-hmm .
[doctor] whats , what's going on ?
[patient] i , i just feel out of sorts lately . i do n't know if it's the change in the seasons or if we're just doing a lot of projects around the house and …
```

**Reference note**

```
CHIEF COMPLAINT

Follow-up of chronic problems.

HISTORY OF PRESENT ILLNESS

Brian White is a 58-year-old male with a past medical history significant for congestive heart failure and hypertension, who presents today for follow-up of his chronic problems.

The patient states he has been feeling out of sorts lately. He is not sure if it is due to the change in the seasons or due to performing lots of projects and some construction on his home. He reports fatigue and lightheadedness. This has been going on for about 5 weeks. While exerting energy, he has experienced some shortness of breath and chest cramps. The patient also notes a slight cough, but he is not sure if it is just the change in seasons.

He feels bloated every once in a while. His diet has been a little bit of a struggle. They had construction on their kitchen begin over Labor Day weekend, and have been eating less healthy f …
```

**Generated note**

```
CHIEF COMPLAINT

The patient is a 58-year-old male who comes in for followup of his chronic conditions including congestive heart failure and hypertension.  He states he has been having some fatigue, lightheadedness, and bloating for the past 5 weeks.  He denies fevers, chills, dyspnea on exertion, orthopnea, paroxysmal nocturnal dyspnea, pleuritic chest pain, hemoptysis, sputum production, weight loss, night sweats, arthralgias, myalgias, abdominal pain, nausea, vomiting, diarrhea, constipation, headache, photophobia, syncope, palpitations, tremors, weakness, numbness, tingling, visual changes, hearing changes, dysphagia, hoarseness, wheezing, cough, sore throat, dental problems, joint swelling, rash, itching, pruritus, urticaria, erythema nodosum, petechiae, purpura, ecchymosis, bruising, bleeding gums, epistaxis, hematuria, hematosuria, frequency, urgency, nocturia, oliguria, polyuria, nocturia, dysuria, urinary retention, impotence, decreased libido, erectile dysfunction, gynecomastia, galactorrhea, amenorrhea, menorrhagia, irregular menses, dysmenorrhea, pelvic pain, infertility …
```

- unsupported entities (vs. transcript): abdominal pain, abscess, anal fissure, bleeding, blood in stool, blurred vision, bruising, burning sensation, colon polyps, constipation, decreased libido, deep vein thrombosis, dysmenorrhea, dysphagia, dyspnea on exertion, dysuria, eczema, erectile dysfunction, erythema, headache
- incorrect diagnosis: abscess, anal fissure, colon polyps, deep vein thrombosis, eczema, hemorrhoids, hernia, peptic ulcer disease, prostatitis  ·  missing diagnosis: mitral regurgitation
- incorrect medication: —  ·  missing medication: furosemide, lisinopril
- dosage mismatch: —
- negation flips (vs. reference): chest pain, dyspnea on exertion
- unsupported numbers: —
- missing information: {"symptom": ["crackles", "cramping", "dyspnea", "murmur", "weight gain"], "diagnosis": ["mitral regurgitation", "pleural effusion"], "medication": ["furosemide", "lisinopril"], "investigation": ["blood pressure measurement", "diagnostic workup", "echocardiogram", "home monitoring", "physical examination", "weight measurement"]}

## Negation error example: `aci_bench_validation_D2N074-virtscribe`

*negation error example*

ROUGE-L 9.9 · length ratio 0.86 · truncated True · degenerate False · hallucination 83.3 · negation-flip 55.6 · numerical consistency 100.0 · coverage 39.1

**Transcript (excerpt)**

```
[doctor] patient , bruce ward . date of birth 5/21/1969 . please use my neuro consult template . this is a 52-year-old male with dia- newly diagnosed pituitary lesion . the patient is seen in consultation at the request of dr. henry howard for possible surgical intervention . mr . ward presented to his primary care provider , dr. howard , on 3/1/21 complaining of worsening headaches over the past few months . he denied any trouble with headaches in the past . his past clinical history is unremarkable .
[doctor] worked out for worsening headaches was initiated with brain mri and serology where pituitary lesion was incidentally discovered . i personally reviewed the labs dated 3/3/21 including …
```

**Reference note**

```
CHIEF COMPLAINT

Pituitary lesion.

HISTORY OF PRESENT ILLNESS

Bruce Ward is a 52-year-old male with a pituitary lesion. The patient is seen in consultation at the request of Dr. Henry Howard for possible surgical intervention.

The patient presented to his primary care provider, Dr. Howard, on 03/01/2021 complaining of worsening headaches over the past few months. He denied any trouble with headaches in the past. Further work up of headaches with MRI of the brain revealed the pituitary lesion.

Mr. Ward reports headaches started about 3 months ago, at which point they were around 3 out of 10 in severity. They have gradually worsened over time and now he rates them at about 6/10. The headaches do tend to be worse in the morning and feel like a dull ache behind the eyes. They tend to last a few hours at a time, and nothing makes them particularly worse or better. Tylenol failed to improv …
```

**Generated note**

```
CHIEF COMPLAINT

The patient is a 52-year-old male with a chief complaint of worsening headaches over the past few months.  He denies any previous headache complaints.  His past clinical history is unremarkable.

HISTORY OF PRESENT ILLNESS

Mr. Ward is a 52-year-old male who presents to the office for evaluation of headaches.  The patient states that he has had worsening headaches over the past several months.  He denies any previous headache complaints.  He has no history of allergies, asthma, hypertension, diabetes mellitus, or any other chronic illnesses.  He does not take any medications.  He denies tobacco use, alcohol use, or illicit drug use.  He is married and works as a computer programmer.  He has no known family history of neurological disorders.  He denies any recent fevers, chills, or weight changes.  He denies any recent trauma or falls.  He denies any recent visual changes, diplopia, dysarthria, dysphasia, or weakness.  He denies any recent syncope or near syncope episodes.  He denies any recent paresthesias or numbness.  He denies any recent bowel/bladder dysfunction. …
```

- unsupported entities (vs. transcript): abdominal pain, allergic rhinitis, anxiety, anxiety symptoms, arrhythmia, asthma, blood in stool, blurred vision, chest pain, chills, confusion, cough, cramping, depression, diabetes, difficulty walking, dizziness, double vision, dyspnea, dysuria
- incorrect diagnosis: —  ·  missing diagnosis: infection, stroke
- incorrect medication: —  ·  missing medication: acetaminophen
- dosage mismatch: —
- negation flips (vs. reference): numbness, pain, slurred speech, tobacco use, weakness
- unsupported numbers: —
- missing information: {"symptom": ["neck pain", "seizure"], "diagnosis": ["infection", "myocardial infarction", "stroke"], "medication": ["acetaminophen"], "investigation": ["blood work", "complete blood count", "crp", "diagnostic workup", "eye exam", "mri"]}

## Numerical error example: `aci_bench_validation_D2N069-virtassist`

*numerical error example*

ROUGE-L 31.5 · length ratio 1.41 · truncated False · degenerate False · hallucination 68.2 · negation-flip 0.0 · numerical consistency 36.4 · coverage 76.9

**Transcript (excerpt)**

```
[doctor] hi , ms. thompson . i'm dr. moore . how are you ?
[patient] hi , dr. moore .
[doctor] hi .
[patient] i'm doing okay except for my knee .
[doctor] all right , hey , dragon , ms. thompson is a 43 year old female here for right knee pain . so tell me what happened with your knee ?
[patient] well , i was , um , trying to change a light bulb , and i was up on a ladder and i kinda had a little bit of a stumble and kinda twisted my knee as i was trying to catch my fall .
[doctor] okay . and did you injure yourself any place else ?
[patient] no , no . it just seems to be the knee .
[doctor] all right . and when did this happen ?
[patient] it was yesterday .
[doctor] all right . and , uh , w …
```

**Reference note**

```
CC:

Right knee pain.

HPI:

Ms. Thompson is a 43-year-old female who presents today for an evaluation of right knee pain. She states she was trying to change a lightbulb on a ladder, and she twisted her knee when she stumbled and caught herself from falling yesterday. She has been applying ice and taking Ibuprofen without relief.

CURRENT MEDICATIONS:

Ibuprofen, digoxin.

PAST MEDICAL HISTORY:

Atrial fibrillation.

PAST SURGICAL HISTORY:

Rhinoplasty.

EXAM

Examination of the right knee shows pain with flexion. Tenderness over the medial joint line. No pain in the calf. Pain with valgus stress. Sensation is intact.

RESULTS

X-rays of the right knee show no obvious signs of acute fracture or dislocation. Mild effusion is noted.

IMPRESSION

Right knee acute medial meniscus sprain.

PLAN

At this point, I discussed the diagnosis and treatment options with the patient. I have recommend …
```

**Generated note**

```
CHIEF COMPLAINT
Right knee pain.

HISTORY OF PRESENT ILLNESS

Ms. Thompson is a 43-year-old female who presents to the emergency room complaining of right knee pain.  She states she was changing a light bulb and had a little bit of a stumble and twisted her knee.  She denies any other injuries.  She states that she has been having pain in the medial aspect of her right knee since then.  She has been applying ice and taking ibuprofen without relief.  She has a history of atrial fibrillation and takes digoxin.  She has had a rhinoplasty.  She denies any other surgeries.

REVIEW OF SYSTEMS

Significant for right knee pain.  No other complaints.

PHYSICAL EXAM

VITAL SIGNS
Blood pressure: 130/80
Pulse: 90
Respiratory rate: 18
Temperature: 98.6

NECK
Supple
No masses
No tenderness
No lymphadenopathy

CHEST
Clear lungs bilaterally
No wheezing
No rales
No tenderness

HEART
Regular rhythm
No murmurs
No gallops
No rubs

ABDOMEN
Soft
Non-tender
Negative bowel sounds

EXTREMITIES
Right lower extremity
Positive for tenderness medially
Negative for crepitus
Negative for edema
Negative for erythem …
```

- unsupported entities (vs. transcript): atrial fibrillation, blood pressure measurement, crackles, crepitus, diagnostic workup, edema, erythema, heart rate measurement, lymphadenopathy, mri, murmur, physical examination, respiratory rate, trauma, wheezing
- incorrect diagnosis: trauma  ·  missing diagnosis: sprain
- incorrect medication: —  ·  missing medication: —
- dosage mismatch: —
- negation flips (vs. reference): —
- unsupported numbers: 130, 130/80, 18, 5, 80, 90, 98.6
- missing information: {"symptom": ["falls", "joint swelling"], "diagnosis": ["sprain"]}

## Missing information example: `aci_bench_validation_D2N076-virtscribe`

*missing information example*

ROUGE-L 9.1 · length ratio 1.06 · truncated True · degenerate True · hallucination 100.0 · negation-flip — · numerical consistency 100.0 · coverage 0.0

**Transcript (excerpt)**

```
[doctor] hello .
[patient_guest] hi .
[doctor] i'm dr. evelyn , one of the kidney doctors . it's good to meet you guys .
[patient_guest] it's nice to meet you also .
[doctor] yeah . so i was reading about this syndrome that i actually have never heard of .
[patient_guest] yeah , me too .
[doctor] i do n't think it's very common .
[patient_guest] definitely not . it's c- pretty rare .
[doctor] so-
[doctor] can you start at the beginning ? i know she's a twin , so are these your first two babies ?
[patient_guest] no , i have a son also who is nine . he also has autism .
[doctor] okay .
[patient_guest] and when the twins were born , katherine , she was about 4 pounds , 8 ounces . and her twin w …
```

**Reference note**

```
CHIEF COMPLAINT

Renal screening tests.

HISTORY OF PRESENT ILLNESS

Katherine Lopez is a 22-month-old female, born at 34 weeks +3 days gestation, diagnosed with the rare Smith-Magenis syndrome and associated global developmental delays. She was referred to nephrology by genetics who recommended renal screening tests. At birth, the patient weighed 4 pounds 8 ounces, exhibited difficulties during eating where she would stop breathing, and challenges regulating her body temperature; determined to be typical issues associated with premature birth. The patient has seen many specialists, including GI for severe reflux, a dietitian who recommended discontinuing consumption of cow’s milk, and a neurologist who diagnosed her with Smith-Magenis syndrome. Additionally, she has been seen by a geneticist, orthopedist, ophthalmologist, and audiologist. The patient is not ambulatory, did not sit up un …
```

**Generated note**

```
CHIEF COMPLAINT

The patient is a 2-year-old female who comes in for evaluation of possible renal anomalies secondary to Smith-Magenis Syndrome.

HISTORY OF PRESENT ILLNESS

The patient is a 2-year-old female who comes in for evaluation of possible renal anomalies secondary to Smith-Magenis Syndrome.  She is a twin, and her twin sister is reportedly healthy.  The patient has a history of developmental delay, including delayed ambulation and delayed sitting.  She has had multiple consultations with various specialists including gastroenterology, genetics, nephrology, and orthopedics.  She has been evaluated by a pediatric urologist.  She has had multiple surgeries including a fundoplication.  She has had multiple hospitalizations for respiratory infections and pneumonia.  She has had multiple episodes of aspiration pneumonia.  She has had multiple episodes of vomiting.  She has had multiple episodes of diarrhea.  She has had multiple episodes of constipation.  She has had multiple episodes of abdominal pain.  She has had multiple episodes of fever.  She has had multiple episodes of ch …
```

- unsupported entities (vs. transcript): abdominal pain, bradycardia, chest pain, chills, constipation, cough, diarrhea, dysphagia, fatigue, fever, hemoptysis, hoarseness, hypertension, hypotension, infection, night sweats, orthostatic hypotension, palpitations, pneumonia, slurred speech
- incorrect diagnosis: —  ·  missing diagnosis: —
- incorrect medication: —  ·  missing medication: —
- dosage mismatch: —
- negation flips (vs. reference): —
- unsupported numbers: —
- missing information: {"symptom": ["heartburn"], "medical_history": ["autism"], "investigation": ["temperature measurement", "ultrasound", "weight measurement"]}

## Degenerate output example: `aci_bench_validation_D2N068-virtassist`

*degenerate output example*

ROUGE-L 7.6 · length ratio 0.71 · truncated True · degenerate True · hallucination 81.4 · negation-flip 13.3 · numerical consistency 100.0 · coverage 48.4

**Transcript (excerpt)**

```
[doctor] hi , brian . how are you ?
[patient] hi , good to see you .
[doctor] it's good to see you too . so , i know the nurse told you a little bit about dax .
[patient] mm-hmm .
[doctor] i'd like to tell dax about you , okay ?
[patient] sure .
[doctor] so , brian is a 58 year old male with a past medical history significant for congestive heart failure and hypertension , who presents today for follow-up of his chronic problems . so , brian , it's been a little while i've seen you .
[patient] mm-hmm .
[doctor] whats , what's going on ?
[patient] i , i just feel out of sorts lately . i do n't know if it's the change in the seasons or if we're just doing a lot of projects around the house and …
```

**Reference note**

```
CHIEF COMPLAINT

Follow-up of chronic problems.

HISTORY OF PRESENT ILLNESS

Brian White is a 58-year-old male with a past medical history significant for congestive heart failure and hypertension, who presents today for follow-up of his chronic problems.

The patient states he has been feeling out of sorts lately. He is not sure if it is due to the change in the seasons or due to performing lots of projects and some construction on his home. He reports fatigue and lightheadedness. This has been going on for about 5 weeks. While exerting energy, he has experienced some shortness of breath and chest cramps. The patient also notes a slight cough, but he is not sure if it is just the change in seasons.

He feels bloated every once in a while. His diet has been a little bit of a struggle. They had construction on their kitchen begin over Labor Day weekend, and have been eating less healthy f …
```

**Generated note**

```
CHIEF COMPLAINT

The patient is a 58-year-old male who comes in for followup of his chronic conditions including congestive heart failure and hypertension.  He states he has been having some fatigue, lightheadedness, and bloating for the past 5 weeks.  He denies fevers, chills, dyspnea on exertion, orthopnea, paroxysmal nocturnal dyspnea, pleuritic chest pain, hemoptysis, sputum production, weight loss, night sweats, arthralgias, myalgias, abdominal pain, nausea, vomiting, diarrhea, constipation, headache, photophobia, syncope, palpitations, tremors, weakness, numbness, tingling, visual changes, hearing changes, dysphagia, hoarseness, wheezing, cough, sore throat, dental problems, joint swelling, rash, itching, pruritus, urticaria, erythema nodosum, petechiae, purpura, ecchymosis, bruising, bleeding gums, epistaxis, hematuria, hematosuria, frequency, urgency, nocturia, oliguria, polyuria, nocturia, dysuria, urinary retention, impotence, decreased libido, erectile dysfunction, gynecomastia, galactorrhea, amenorrhea, menorrhagia, irregular menses, dysmenorrhea, pelvic pain, infertility …
```

- unsupported entities (vs. transcript): abdominal pain, abscess, anal fissure, bleeding, blood in stool, blurred vision, bruising, burning sensation, colon polyps, constipation, decreased libido, deep vein thrombosis, dysmenorrhea, dysphagia, dyspnea on exertion, dysuria, eczema, erectile dysfunction, erythema, headache
- incorrect diagnosis: abscess, anal fissure, colon polyps, deep vein thrombosis, eczema, hemorrhoids, hernia, peptic ulcer disease, prostatitis  ·  missing diagnosis: mitral regurgitation
- incorrect medication: —  ·  missing medication: furosemide, lisinopril
- dosage mismatch: —
- negation flips (vs. reference): chest pain, dyspnea on exertion
- unsupported numbers: —
- missing information: {"symptom": ["crackles", "cramping", "dyspnea", "murmur", "weight gain"], "diagnosis": ["mitral regurgitation", "pleural effusion"], "medication": ["furosemide", "lisinopril"], "investigation": ["blood pressure measurement", "diagnostic workup", "echocardiogram", "home monitoring", "physical examination", "weight measurement"]}
