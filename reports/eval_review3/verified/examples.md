# Example errors — verified

Each block shows the transcript excerpt, the reference note, the generated note and the flags raised by the factuality checker.

# Split: aci_bench_test_taskB_1

## Best ROUGE-L: `aci_bench_test_taskB_1_D2N100-virtscribe`

*highest ROUGE-L in the split*

ROUGE-L 37.2 · length ratio 0.64 · truncated False · degenerate False · hallucination 25.0 · negation-flip 28.6 · numerical consistency 100.0 · coverage 70.0

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
**CHIEF COMPLAINT**

The patient, Kayla Ward, presents with complaints of acne located on the face, which started approximately two years ago and persists daily.

**HISTORY OF PRESENT ILLNESS**

Kayla reports that her acne began two years ago and is present most days. She has been using Persa-Gel and washing regularly, which provides some relief. There are no associated symptoms, including itching, bleeding, or pain. Her skin care routine includes wiping her face with water and a washcloth in the morning and using an ELF facial cleanser, toner, and Persa-Gel at night. However, she denies experiencing significant acne flares during her menstrual cycles.

*
No additional past medical history is reported. Kayla lives with her parents and siblings and participates in various extracurricular activities, including basketball and volleyball. She applies sunscreen with SPF 30 in the summer.

**PHYSICAL EXAMINATION**

Upon physical examination, multiple benign nevi were observed on the trunk and extremities. Scattered skin-colored papules, open and closed comedones, and erythematous papules w …
```

- unsupported entities (vs. transcript): erythema, physical examination
- incorrect diagnosis: —  ·  missing diagnosis: —
- incorrect medication: —  ·  missing medication: tretinoin
- dosage mismatch: —
- negation flips (vs. reference): adapalene, flare
- unsupported numbers: —
- missing information: {"symptom": ["falls"], "medication": ["tretinoin"], "investigation": ["diagnostic workup"]}

## Worst ROUGE-L: `aci_bench_test_taskB_1_D2N099-virtscribe`

*lowest ROUGE-L in the split*

ROUGE-L 8.8 · length ratio 0.15 · truncated False · degenerate False · hallucination 0.0 · negation-flip 0.0 · numerical consistency — · coverage 6.7

**Transcript (excerpt)**

```
[doctor] next patient is randy gutierrez . date of birth , 8/10/2020 . please use review of symptoms . all text to write . physical exam , auto text uri .
[doctor] hello , how are you doing today ?
[patient_guest] we're okay , thank you .
[doctor] that's good to hear . so , how many days has randy been feeling sick ?
[patient_guest] well , i would say it started around supper time last night .
[doctor] last night , okay , and what's been going on ?
[patient_guest] well , he started to get a runny nose .
[doctor] okay , and is he stuffy too ?
[patient_guest] yeah . yeah .
[doctor] okay , and have you noticed , is his mucous clear right now ?
[patient_guest] it is , it is right now , yes .
[do …
```

**Reference note**

```
CHIEF COMPLAINT

Cough, nasal congestion, and rhinorrhea.

HISTORY OF PRESENT ILLNESS

Randy Gutierrez is a 9-month-old male who is being evaluated today for a cough, nasal congestion, and rhinorrhea. He is accompanied by his mother.

Symptoms began yesterday around dinnertime with clear nasal drainage, pulling on his ears bilaterally, and rubbing his nose frequently. He does not have a barky cough or a sore throat. His rectal temperature was 100.3 degrees. The patient did consume a 7 ounce bottle this morning, but mostly denied the next offered bottle and declined cereal. He is irritable and having trouble falling asleep, described “like he is fighting it”.

The patient has been exposed to an older sister who is sick and a cousin who has a sinus infection.

Treatment has included saline nasal spray, Tylenol, baby Vick's, and a humidifier. When the patient aroused this morning, he was wa …
```

**Generated note**

```
**CHIEF COMPLAINT**


*

*

**PHYSICAL EXAM**


**RESULTS**


*

* Conservative management with rest, hydration, and monitoring for worsening symptoms.
* Saline mist administration to help relieve nasal congestion.
* * Avoidance of honey due to potential botulism risk.
* Use of Zarbee's for relief of nasal congestion.
* Administration of a half teaspoon of the sister's medication (presumably an antibiotic) if a barky cough develops.
*
```

- unsupported entities (vs. transcript): —
- incorrect diagnosis: —  ·  missing diagnosis: croup, upper respiratory infection
- incorrect medication: —  ·  missing medication: acetaminophen, saline nasal spray
- dosage mismatch: —
- negation flips (vs. reference): —
- unsupported numbers: —
- missing information: {"symptom": ["cough", "hoarseness", "insomnia", "irritability", "purulent drainage", "rhinorrhea"], "diagnosis": ["croup", "sinusitis", "upper respiratory infection"], "medication": ["acetaminophen", "saline nasal spray"]}

## Hallucination example: `aci_bench_test_taskB_1_D2N105-virtscribe`

*hallucination example*

ROUGE-L 27.8 · length ratio 0.46 · truncated False · degenerate False · hallucination 13.0 · negation-flip 0.0 · numerical consistency 100.0 · coverage 60.0

**Transcript (excerpt)**

```
[doctor] patient's name is diana scott . date of birth , 12/8/1920 . the date of service is 7/9/2021 . this is a new patient note .
[doctor] good afternoon . how are you today ?
[patient] i'm good , thank you .
[doctor] good . well , what brings you in to see me today ?
[patient] well , my doctor says that i have a heart murmur .
[doctor] okay .
[patient] so i do n't know how big a heart murmur i have , or really even what it is .
[doctor] okay . so how long have you had that for ? do you have any idea , or is that completely new as far as you know ?
[patient] yeah , she said it's a new worrisome heart murmur . so of course , i'm worried as well .
[doctor] got it . okay . and are you having  …
```

**Reference note**

```
CHIEF COMPLAINT

Heart murmur.

HISTORY OF PRESENT ILLNESS

Diana Scott is a 100-year-old female who presents today for evaluation of a heart murmur.

Ms. Scott has been recently diagnosed with a “new, worrisome” heart murmur. She denies chest pain, syncope, palpitations, fevers, or chills. She reports shortness of breath if she walks too fast, too long, or tries to drink a whole glass of water without stopping. The patient requires a walker and can walk around her cul-de-sac or to the end of the driveway without shortness of breath. Compared to 6 months ago, her functioning has declined 20-30%. Prior to 6 months, symptoms were absent. For the past month she has been experiencing severe, bilateral leg pain, which was limiting her mobility. She did see her doctor last week who completed a chest x-ray and prescribed pain medicine. Occasionally, she feels dizzy but takes medication for this …
```

**Generated note**

```
**CHIEF COMPLAINT**
Patient Diana Scott presents with a chief complaint of a newly diagnosed worrisome heart murmur.

**HISTORY OF PRESENT ILLNESS**
She denies experiencing chest pain, but mentions severe pains in her legs, which began approximately one month prior to presentation. She also reports experiencing shortness of breath upon walking too fast or too long, or drinking a full glass of water without stopping. Her symptoms have worsened over the past six months, with a 70-80% increase in severity compared to six months ago. She uses a walker for mobility and experiences fatigue, particularly when overexerting herself. Additionally, she reports experiencing dizziness and taking a pill for relief. She denies experiencing syncope, palpitations, or fever.

*
* Cardiovascular: Reports a 4/6 systolic murmur at the right upper sternal border with mild radiation to the carotids.
* Neurological: Gait is normal for age.
* * * * Allergic reactions: Denies experiencing any allergies to medications.

**PHYSICAL EXAM**
Constitutional: Elderly, otherwise no acute distress.
Cardiovascular: Nor …
```

- unsupported entities (vs. transcript): coronary artery disease, drug allergy, electrocardiogram
- incorrect diagnosis: —  ·  missing diagnosis: hyperlipidemia, hypertension, hypothyroidism, valvular heart disease
- incorrect medication: —  ·  missing medication: amlodipine, lisinopril
- dosage mismatch: —
- negation flips (vs. reference): —
- unsupported numbers: —
- missing information: {"symptom": ["chills", "edema", "tachycardia"], "medical_history": ["hyperlipidemia", "hypertension", "hypothyroidism"], "diagnosis": ["valvular heart disease"], "medication": ["amlodipine", "lisinopril"], "investigation": ["holter monitor", "weight measurement", "x-ray"]}

## Incorrect diagnosis example: `aci_bench_test_taskB_1_D2N113-aci`

*incorrect diagnosis example*

ROUGE-L 30.5 · length ratio 1.07 · truncated False · degenerate False · hallucination 6.2 · negation-flip 0.0 · numerical consistency 100.0 · coverage 70.6

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
**CHIEF COMPLAINT**

Patient presents with anxiety regarding recent blood work results indicating Hepatitis C.

*
The patient reports being anxious about her recent blood work results showing Hepatitis C. She states she has been feeling fine but recently noticed fatigue at the end of the day despite getting sufficient sleep. She denies any jaundice, wheezing, crackles, rhonchi, difficulty walking, or edema. She admits to a history of IV drug use in the past but claims to have been clean for over 15 years. She also reports a history of alcohol use, currently consuming approximately one beer per day, and smoking one to two cigarettes per day.

**REVIEW OF SYSTEMS**

The patient reports fatigue at the end of the day but denies any other significant symptoms. She mentions having a regular job and being a workaholic but is working on finding balance.

**PHYSICAL EXAM**

General appearance: No distress, no jaundice on skin exam.
Heart exam: Regular rate and rhythm with a 2/6 systolic murmur, which has not changed from last year.
Lungs exam: Clear with no wheezes, rales, or rhonchi.
Abdomin …
```

- unsupported entities (vs. transcript): anxiety
- incorrect diagnosis: anxiety  ·  missing diagnosis: —
- incorrect medication: —  ·  missing medication: —
- dosage mismatch: —
- negation flips (vs. reference): —
- unsupported numbers: —
- missing information: {"symptom": ["pain"], "medical_history": ["depression", "diabetes", "hypertension"], "investigation": ["vital signs"]}

## Incorrect medication / dosage example: `aci_bench_test_taskB_1_D2N103-virtscribe`

*incorrect medication / dosage example*

ROUGE-L 32.2 · length ratio 0.68 · truncated False · degenerate False · hallucination 25.0 · negation-flip 0.0 · numerical consistency 100.0 · coverage 58.3

**Transcript (excerpt)**

```
[doctor] next patient is melissa sanchez . date of birth , 9/23/1962 . mrn : 5484367 . she is being seen in office today for status post mitral valve repair done on 8/3/2020 . at her previous follow-up on 9/17 , we felt that she was doing quite well from a cardiac standpoint , and so we recommended she continue with the same medication . ecg taken on 12/26/2020 reveals atrial fibrillation with a controlled ventricular response . t-wave inversion anteriorly . compared to the previous study , there are no significant changes , and please add in the history , patient has a history of mitral regurgitation and atrial fibrillation , history of diabetes , asthma , and recurrent chest discomfort wit …
```

**Reference note**

```
CHIEF COMPLAINT

Status post mitral valve repair.

HISTORY OF PRESENT ILLNESS

Mrs. Melissa Sanchez is a 58-year-old female being seen today for a status post mitral valve repair, completed on 08/03/2020.

On 09/17/20 we saw Mrs. Sanchez in office, and she was doing well and thus we recommended maintaining her current medications, she is using a reminder app to stay compliant with medications.

The patient reports feeling better and overall, pretty good. She denies experiencing new symptoms. She is still having chest pain intermittently, and her breathing “gets shallow” which results in her “slowing down” and decreasing her exertion. An episode of shortness of breath and chest pains may last a few minutes and will not recur for a few weeks.

PAST HISTORY

Medical
Mitral regurgitation.
Atrial fibrillation.
Diabetes Type II.
Asthma.

Surgical
Mitral valve repair 08/03/2020.

CURRENT MEDICA …
```

**Generated note**

```
**CHIEF COMPLAINT**
Patient presents for follow-up after mitral valve repair on 8/3/2020.

**HISTORY OF PRESENT ILLNESS**
The patient reports feeling "pretty good" since the surgery, with improvement in her condition. These episodes occur frequently enough for her to notice. She attributes her improved condition to slowing down when experiencing symptoms and avoiding overexertion.

*
**PHYSICAL EXAM**

* Head and neck: No jugular venous distension (JVD) detected.
* Lungs: Reduced breath sounds, but auscultation and percussion were clear.
* Heart: Irregularly irregular rhythm consistent with atrial fibrillation.
* Abdomen: Slightly accentuated S1, no S3, and no tenderness upon palpation.
* Extremities: Trace peripheral edema.

**RESULTS**
The patient's ECG taken earlier today showed atrial fibrillation with a controlled ventricular response and T-wave inversion anteriorly.

**ASSESSMENT AND PLAN**
The patient's condition appears stable, with well-controlled atrial fibrillation and no significant changes in her ECG compared to the previous study. Her current medications include Coumadi …
```

- unsupported entities (vs. transcript): electrocardiogram, pain
- incorrect diagnosis: —  ·  missing diagnosis: —
- incorrect medication: —  ·  missing medication: —
- dosage mismatch: [{"drug": "furosemide", "predicted": "4 mg", "source": ["40 mg"]}]
- negation flips (vs. reference): —
- unsupported numbers: —
- missing information: {"symptom": ["chest pain", "dyspnea"], "medical_history": ["asthma", "diabetes", "mitral regurgitation"]}

## Negation error example: `aci_bench_test_taskB_1_D2N100-virtscribe`

*negation error example*

ROUGE-L 37.2 · length ratio 0.64 · truncated False · degenerate False · hallucination 25.0 · negation-flip 28.6 · numerical consistency 100.0 · coverage 70.0

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
**CHIEF COMPLAINT**

The patient, Kayla Ward, presents with complaints of acne located on the face, which started approximately two years ago and persists daily.

**HISTORY OF PRESENT ILLNESS**

Kayla reports that her acne began two years ago and is present most days. She has been using Persa-Gel and washing regularly, which provides some relief. There are no associated symptoms, including itching, bleeding, or pain. Her skin care routine includes wiping her face with water and a washcloth in the morning and using an ELF facial cleanser, toner, and Persa-Gel at night. However, she denies experiencing significant acne flares during her menstrual cycles.

*
No additional past medical history is reported. Kayla lives with her parents and siblings and participates in various extracurricular activities, including basketball and volleyball. She applies sunscreen with SPF 30 in the summer.

**PHYSICAL EXAMINATION**

Upon physical examination, multiple benign nevi were observed on the trunk and extremities. Scattered skin-colored papules, open and closed comedones, and erythematous papules w …
```

- unsupported entities (vs. transcript): erythema, physical examination
- incorrect diagnosis: —  ·  missing diagnosis: —
- incorrect medication: —  ·  missing medication: tretinoin
- dosage mismatch: —
- negation flips (vs. reference): adapalene, flare
- unsupported numbers: —
- missing information: {"symptom": ["falls"], "medication": ["tretinoin"], "investigation": ["diagnostic workup"]}

## Numerical error example: `aci_bench_test_taskB_1_D2N127-aci`

*numerical error example*

ROUGE-L 23.7 · length ratio 0.56 · truncated False · degenerate False · hallucination 9.1 · negation-flip 0.0 · numerical consistency 70.0 · coverage 55.0

**Transcript (excerpt)**

```
[doctor] hey brandon you know glad to see you in here today i see on your chart that you're experiencing some neck pain could you tell me a bit about what happened
[patient] yeah i was in a car crash
[doctor] wow okay when was that
[patient] well which car crash
[doctor] okay so multiple car crashes alright so let's see if we can how many let's start
[patient] my therapist said well my well actually my mother said i should go see the therapist and the therapist said i should see the lawyer but my neck's hurting
[doctor] okay so i'm glad that you know you're getting some advice and so let's let's talk about this neck pain how many car crashes have we had recently
[patient] well the ones that  …
```

**Reference note**

```
CHIEF COMPLAINT

Neck pain.

HISTORY OF PRESENT ILLNESS

Brandon Green is a pleasant 46-year-old male who presents to the clinic today for the evaluation of neck pain. His pain began when he was involved in a motor vehicle accident in 02/2022 when he was on his way home from a pain clinic. The patient notes that he has been in 4 motor vehicle accidents; however, he notes that he was fine after the first two accidents, but the third motor vehicle accident is when his neck and back pain began. He states that he was in therapy following the second accident and had surgery after his third accident. The patient was seen at a pain clinic secondary to neck and back pain. He was prescribed fentanyl; however, he has not received a prescription for several weeks. Today, he reports that his pain is a 12 out of 10. He describes his pain as sharp and incapacitating with stiffness and pain. The patien …
```

**Generated note**

```
**CHIEF COMPLAINT**

The patient presents with complaints of neck pain and stiffness following multiple car crashes.

*
The patient reports experiencing neck pain since the most recent car crash in February of this year. He mentions having had previous car crashes, including one in which he underwent surgery, but notes that he was fine until the latest incident. He describes his pain as sharp and incapacitating, rating it a 12 out of 10.
*
He reports occasional bruising and swelling, but none are currently visible. He has been taking fentanyl, but notes that he hasn't received a prescription for several weeks.

**PHYSICAL EXAM**

The patient exhibits moderate range of motion in his neck, with pain on palpation both on the bony process and on the muscle. He is unable to bend his neck forward or backward without significant pain.

**RESULTS**

However, the doctor notes that no fracture is visible.

**ASSESSMENT AND PLAN**

Based on the patient's symptoms and physical examination, the doctor diagnoses a neck sprain. To manage the patient's pain conservatively, the doctor orders:

1. 2.  …
```

- unsupported entities (vs. transcript): mri
- incorrect diagnosis: —  ·  missing diagnosis: —
- incorrect medication: —  ·  missing medication: —
- dosage mismatch: —
- negation flips (vs. reference): —
- unsupported numbers: 150, 3, 5
- missing information: {"symptom": ["back pain", "dizziness", "fatigue", "headache", "laceration", "numbness"], "diagnosis": ["trauma"], "investigation": ["diagnostic workup", "x-ray"]}

## Missing information example: `aci_bench_test_taskB_1_D2N099-virtscribe`

*missing information example*

ROUGE-L 8.8 · length ratio 0.15 · truncated False · degenerate False · hallucination 0.0 · negation-flip 0.0 · numerical consistency — · coverage 6.7

**Transcript (excerpt)**

```
[doctor] next patient is randy gutierrez . date of birth , 8/10/2020 . please use review of symptoms . all text to write . physical exam , auto text uri .
[doctor] hello , how are you doing today ?
[patient_guest] we're okay , thank you .
[doctor] that's good to hear . so , how many days has randy been feeling sick ?
[patient_guest] well , i would say it started around supper time last night .
[doctor] last night , okay , and what's been going on ?
[patient_guest] well , he started to get a runny nose .
[doctor] okay , and is he stuffy too ?
[patient_guest] yeah . yeah .
[doctor] okay , and have you noticed , is his mucous clear right now ?
[patient_guest] it is , it is right now , yes .
[do …
```

**Reference note**

```
CHIEF COMPLAINT

Cough, nasal congestion, and rhinorrhea.

HISTORY OF PRESENT ILLNESS

Randy Gutierrez is a 9-month-old male who is being evaluated today for a cough, nasal congestion, and rhinorrhea. He is accompanied by his mother.

Symptoms began yesterday around dinnertime with clear nasal drainage, pulling on his ears bilaterally, and rubbing his nose frequently. He does not have a barky cough or a sore throat. His rectal temperature was 100.3 degrees. The patient did consume a 7 ounce bottle this morning, but mostly denied the next offered bottle and declined cereal. He is irritable and having trouble falling asleep, described “like he is fighting it”.

The patient has been exposed to an older sister who is sick and a cousin who has a sinus infection.

Treatment has included saline nasal spray, Tylenol, baby Vick's, and a humidifier. When the patient aroused this morning, he was wa …
```

**Generated note**

```
**CHIEF COMPLAINT**


*

*

**PHYSICAL EXAM**


**RESULTS**


*

* Conservative management with rest, hydration, and monitoring for worsening symptoms.
* Saline mist administration to help relieve nasal congestion.
* * Avoidance of honey due to potential botulism risk.
* Use of Zarbee's for relief of nasal congestion.
* Administration of a half teaspoon of the sister's medication (presumably an antibiotic) if a barky cough develops.
*
```

- unsupported entities (vs. transcript): —
- incorrect diagnosis: —  ·  missing diagnosis: croup, upper respiratory infection
- incorrect medication: —  ·  missing medication: acetaminophen, saline nasal spray
- dosage mismatch: —
- negation flips (vs. reference): —
- unsupported numbers: —
- missing information: {"symptom": ["cough", "hoarseness", "insomnia", "irritability", "purulent drainage", "rhinorrhea"], "diagnosis": ["croup", "sinusitis", "upper respiratory infection"], "medication": ["acetaminophen", "saline nasal spray"]}

# Split: aci_bench_test_taskC_2

## Best ROUGE-L: `aci_bench_test_taskC_2_D2N141-virtscribe`

*highest ROUGE-L in the split*

ROUGE-L 40.3 · length ratio 0.39 · truncated False · degenerate False · hallucination 0.0 · negation-flip 0.0 · numerical consistency 100.0 · coverage 78.9

**Transcript (excerpt)**

```
[doctor] okay , so our next patient is christopher watson . date of birth 04/12/1934 . mr . watson is- is an 86-year-old male who returns in follow-up for adult hydrocephalus . this is his first visit since undergoing sh- shunt surgery , excuse me , on august 1st , 2020 .
[doctor] i have followed mr . watson since may of 2020 when he first presented with eight to ten years of progressive gait impairment , cognitive impairment , and decreased bladder control . we established a diagnosis of adult hydrocephalus with a spino catheter protocol in june 2020 , and he underwent shunt surgery on august 1st , 2020 . a medtronic strata programmable shunt in the ventricular peritoneal configuration was  …
```

**Reference note**

```
CHIEF COMPLAINT

Follow up adult hydrocephalus, 3 months status post shunt surgery.

HISTORY OF PRESENT ILLNESS

Mr. Christopher Watson is an 86-year-old male who returns in follow up of adult hydrocephalus. This is his first visit since undergoing shunt surgery 08/01/2020. He is accompanied by his daughter, Theresa, together they give his history.

I have followed Mr. Watson since May 2020. He presented with 8-10 years of progressive gait impairment, cognitive impairment, and decreased bladder control. We established a diagnosis of adult hydrocephalus with the spinal catheter protocol in June 2020 and he underwent shunt surgery on 08/01/2020. A Medtronic Strata programmable shunt in the ventriculoperitoneal configuration programmed at level 2.0 was placed.

Mr. Watson has had no hospitalizations or other illnesses since I last saw him. With respect to his walking, his daughter states th …
```

**Generated note**

```
**CHIEF COMPLAINT**

Watson, is a 86-year-old male presenting for follow-up of adult hydrocephalus post-shunt surgery.

**HISTORY OF PRESENT ILLNESS**

Mr. Watson has been experiencing progressive gait impairment, cognitive impairment, and decreased bladder control for approximately 8-10 years. His walking has improved, allowing him to walk to the dining room without assistance. However, he still experiences times where he needs help. His bladder control initially improved after surgery but has since leveled out, requiring him to wear diapers. There have been no issues with sores from wearing the diaper. Watson feeling less lost during conversations.

*
* Constitutional: Significant for impaired ability to carry out daily functions.
* Genitourinary: Significant for urinary incontinence and wearing a diaper. Negative for genital sores, decreased or painful output.
* Neurological: Significant for continued walking impairment and cognitive impairment. Negative for headaches, recent falls, or hallucinations.
* Psychiatric: Negative for depression, excessive worrying, or mood swings.

**P …
```

- unsupported entities (vs. transcript): —
- incorrect diagnosis: —  ·  missing diagnosis: —
- incorrect medication: —  ·  missing medication: —
- dosage mismatch: —
- negation flips (vs. reference): —
- unsupported numbers: —
- missing information: {"symptom": ["fever", "slurred speech", "weight loss"], "investigation": ["respiratory rate"]}

## Worst ROUGE-L: `aci_bench_test_taskC_2_D2N156-aci`

*lowest ROUGE-L in the split*

ROUGE-L 17.9 · length ratio 0.40 · truncated False · degenerate False · hallucination 5.9 · negation-flip 7.7 · numerical consistency 66.7 · coverage 59.3

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
**CHIEF COMPLAINT**

Patient presents for follow-up after recent interior STEMI and placement of another stent.

**HISTORY OF PRESENT ILLNESS**

The patient reports experiencing similar symptoms to their previous heart attack, including chest pain that persisted despite initial improvement. They report being able to exercise moderately by walking their dog approximately 1.5 to 2 miles per day. Notably, the patient has experienced lower limb edema since discharge from the hospital.

*
The patient has a history of coronary artery disease, hypertension, and diabetes. However, they admit to not strictly adhering to their diet, particularly regarding salt intake.

**PHYSICAL EXAM**

Cardiac exam notes a 3/6 systolic ejection murmur at the left base. Lung exam is clear. Lower limb edema is present, with pitting 1+ on the right radial artery. Cath site appears clean and intact.

**RESULTS**

EKG shows normal sinus rhythm and good R-wave progression. Echo reveals a reduced ejection fraction of 35%.

*
Primary diagnoses include:

* Coronary artery disease
* * Moderate mitral regurgitation
*
P …
```

- unsupported entities (vs. transcript): electrocardiogram
- incorrect diagnosis: —  ·  missing diagnosis: type 2 diabetes
- incorrect medication: —  ·  missing medication: furosemide, metformin, spironolactone
- dosage mismatch: —
- negation flips (vs. reference): chest pain
- unsupported numbers: 1.5, 8, 9
- missing information: {"symptom": ["dyspnea"], "diagnosis": ["intracranial hemorrhage", "type 2 diabetes"], "medication": ["furosemide", "metformin", "spironolactone"], "investigation": ["blood glucose", "blood pressure measurement", "blood work", "heart rate measurement", "repeat testing"]}

## Hallucination example: `aci_bench_test_taskC_2_D2N164-aci`

*hallucination example*

ROUGE-L 20.9 · length ratio 0.47 · truncated False · degenerate False · hallucination 14.8 · negation-flip 10.5 · numerical consistency 100.0 · coverage 85.7

**Transcript (excerpt)**

```
[doctor] so elizabeth is a 53 -year-old female today complaining of chest pain and she has a past medical history of diabetes and high blood pressure so elizabeth tell me what's going on with your with your chest pain
[patient] i do n't know every time i start walking i'm just having this kind of pressure and chest pain in my chest
[doctor] okay are you having it now or is it gone right now
[patient] right now it's not there
[doctor] okay and how long have you been having this
[patient] probably maybe three months
[doctor] okay and what seemed to bring it on anything exacerbated or relieve it
[patient] it mainly happens when i'm walking i like to try and walk but lately i just have n't been  …
```

**Reference note**

```
CHIEF COMPLAINT

Chest pain on exertion.

MEDICAL HISTORY

The patient has a medical history of diabetes type 2. She has not been formally diagnosed with hypertension, but her blood pressures have been trending high.

FAMILY HISTORY

Patient reports family history of heart disease.

MEDICATIONS

Patient reports taking metformin 500 mg twice daily.

REVIEW OF SYSTEMS

Constitutional: Denies diaphoresis or clamminess.
Cardiovascular: Reports chest pain.
Respiratory: Denies dyspnea.
Gastrointestinal: Denies nausea, vomiting, or diarrhea.

PHYSICAL EXAM

Neck
- General Examination: No JVD, swelling, or carotid bruits.

Respiratory
- Assessment of Respiratory Effort:
- Auscultation of Lungs: Clear bilaterally. No wheezes, rales, or rhonchi.

Cardiovascular
- Auscultation of Heart: 2/6 systolic ejection murmur, otherwise normal rate and rhythm. No murmurs, gallops or rubs. Pulses are equal.

G …
```

**Generated note**

```
**CHIEF COMPLAINT**

The patient, Elizabeth, is a 53-year-old female presenting with complaints of chest pain.

**HISTORY OF PRESENT ILLNESS**

Elizabeth reports experiencing chest pain for approximately three months, particularly when walking. She describes the pain as dull and pressure-like, without radiation to any specific area. There is no associated shortness of breath, sweating, or clamminess.

*
Her family history includes coronary artery disease. She denies nausea, vomiting, diarrhea, or any side effects from her medications.

**PHYSICAL EXAMINATION**


* * * Clear lung exam with no crackles or rhonchi
* Regular heart rate and rhythm with a 2/6 systolic ejection murmur (previously present)
* Equal pulses
* Soft and non-tender abdomen with no masses
* Back exam is fine
* Extremity exam shows 1+ non-pitting edema in both lower legs

**RESULTS**

The EKG performed during the visit showed no signs of a heart attack.

**ASSESSMENT AND PLAN**

Based on the patient's presentation and history, the primary concern is unstable angina, likely due to a blockage causing the chest pain. C …
```

- unsupported entities (vs. transcript): abdominal tenderness, diagnostic workup, electrocardiogram, sweating
- incorrect diagnosis: —  ·  missing diagnosis: type 2 diabetes
- incorrect medication: —  ·  missing medication: nitroglycerin
- dosage mismatch: —
- negation flips (vs. reference): adverse drug reaction, myocardial infarction
- unsupported numbers: —
- missing information: {"symptom": ["wheezing"], "medical_history": ["type 2 diabetes"], "medication": ["nitroglycerin"], "investigation": ["hemoglobin a1c"]}

## Incorrect medication / dosage example: `aci_bench_test_taskC_2_D2N149-aci`

*incorrect medication / dosage example*

ROUGE-L 24.8 · length ratio 0.59 · truncated False · degenerate False · hallucination 5.6 · negation-flip 0.0 · numerical consistency 100.0 · coverage 59.3

**Transcript (excerpt)**

```
[doctor] so dennis is a 57 -year-old male today complaining of shortness of breath he has also got a history of diabetes high blood pressure and history of asthma so dennis tell me what's going on how're you doing
[patient] not too good
[doctor] okay how long have you been feeling not too well
[patient] about a couple of weeks
[doctor] couple of weeks tell me what's going on
[patient] i wake up with shortness of breath
[doctor] okay
[patient] i go to when i'm short of breath there i get back home and i'm again short of breath so i had a tough time dealing with this
[doctor] have you noticed any are you coughing up anything any swelling in your legs or what's going on
[patient] yeah i've been …
```

**Reference note**

```
CHIEF COMPLAINT

Shortness of breath with hemoptysis.

MEDICAL HISTORY

Patient reports history of diabetes, hypertension, and asthma. He also has a long history of knee pain.

MEDICATIONS

Patient reports taking metformin and Norvasc.

REVIEW OF SYSTEMS

Constitutional: Denies fever.
HENT: Denies bleeding gums.
Respiratory: Reports shortness of breath, hemoptysis.
Musculoskeletal: Reports knee pain. Denies lower extremity edema.
Hematologic/Lymphatic: Denies bruising.

VITALS

Pulse oxygenation: 94 percent. Blood pressure: 120/70 mm Hg.

PHYSICAL EXAM

Neck
- General Examination: Neck is supple. No JVD. No carotid bruits.

Respiratory
- Auscultation of Lungs: Some rales and rhonchi, more on the right. No wheezing right now. There is some diminished breath sounds in the right as well.

Cardiovascular
- Auscultation of Heart: Regular rate. 2/6 systolic ejection murmur, unchanged from befo …
```

**Generated note**

```
**CHIEF COMPLAINT**

The patient presents with shortness of breath, which has been ongoing for approximately two weeks.

**HISTORY OF PRESENT ILLNESS**

The patient is a 57-year-old male with a history of diabetes, hypertension, and asthma. In addition to shortness of breath, the patient has been coughing up blood, approximately 3-4 cups per day, for the past three weeks. He denies any swelling in his legs, bruising, or bleeding elsewhere. His medical history includes diabetes, hypertension, and asthma.

**REVIEW OF SYSTEMS**


**PHYSICAL EXAM**


* * * Lung exam showed rales and rhonchi on the right side, with diminished breath sounds
* Heart exam revealed a 2/6 systolic ejection murmur, unchanged from previous examinations
* * Extremity exam showed 1+ non-pitting edema on both lower extremities

**RESULTS**

The patient's oxygen saturation was reported as 94% in the clinic. Blood pressure measurements were taken, but specific values were not provided.

**ASSESSMENT AND PLAN**


* Chest X-ray
* * *
Depending on the results of these tests, the patient may require additional treatment …
```

- unsupported entities (vs. transcript): crackles
- incorrect diagnosis: —  ·  missing diagnosis: —
- incorrect medication: —  ·  missing medication: amlodipine
- dosage mismatch: [{"drug": "metformin", "predicted": "500 mg", "source": ["750 mg"]}]
- negation flips (vs. reference): —
- unsupported numbers: —
- missing information: {"symptom": ["fever", "pain", "wheezing"], "medical_history": ["knee pain"], "medication": ["amlodipine"], "investigation": ["blood glucose", "blood work", "ct scan", "diagnostic workup", "heart rate measurement", "hemoglobin a1c"]}

## Negation error example: `aci_bench_test_taskC_2_D2N130-virtassist`

*negation error example*

ROUGE-L 29.8 · length ratio 0.37 · truncated False · degenerate False · hallucination 6.2 · negation-flip 25.9 · numerical consistency 100.0 · coverage 86.1

**Transcript (excerpt)**

```
[doctor] hi , anna , how are you ?
[patient] i'm doing okay . how are you ?
[doctor] i'm doing well . uh , so i know the nurse told you a little bit about dax . i'd like to tell dax a little bit about you .
[patient] okay .
[doctor] all right . so , uh , anna is a 26-year-old female with a past medical history , significant for epilepsy , depression , and , uh , peptic ulcer disease , who presents with , uh , some joint pain . so , anna , what's going on with your , uh , what's going on with your joints ?
[patient] so , um , it's my left elbow that's really been bothering me . uh , i sit at my desk a lot for work , and type , and i stay in this motion specifically all day . and then after ,  …
```

**Reference note**

```
CHIEF COMPLAINT

Joint pain.

HISTORY OF PRESENT ILLNESS

The patient is a 26-year-old female with a past medical history significant for epilepsy, depression, and peptic ulcer disease who presents with some joint pain.

The patient reports that her left elbow has really been bothering her. She states that she sits at her desk all day for work with her elbows bent. She reports that after work it is really hard for her to flex and extend her left elbow. She reports that it has been really stiff and painful. She also notes that she has noticed swelling on the olecranon of her elbow. She reports that she is right-handed, therefore, she can still write, which is great, but typing is difficult. She denies any numbness or tingling in her hands. She reports that she has some weakness in her arm but nothing too significant. She denies any fever or chills.

Regarding her epilepsy, she reports tha …
```

**Generated note**

```
**CHIEF COMPLAINT**

The patient, Anna, presented with complaints of left elbow pain, stiffness, and difficulty opening and closing her elbow.

**HISTORY OF PRESENT ILLNESS**

Anna is a 26-year-old female with a past medical history significant for epilepsy, depression, and peptic ulcer disease. She denies experiencing numbness or tingling in her hands, but notes a slight weakness in her arm. She also denies fever, chills, chest pain, dyspnea, abdominal pain, nausea, or vomiting.
*

* Joint pain (left elbow)
* * Swelling (left elbow)
* Weakness (left arm)
* Nasal congestion (allergies)

She denied experiencing:

* * Fever or chills
* Chest pain
* Dyspnea
* Abdominal pain
* Nausea or vomiting

**PHYSICAL EXAMINATION**

Physical examination revealed:

* Erythema and edema of the left elbow
* Pain to palpation of the olecranon
* Warmth to palpation of the left elbow
* * Palpable left radial pulse

**RESULTS**

Results of the following tests/investigations were reviewed:

* Left arm x-ray: No evidence of elbow fracture.
* Endoscopy: Recent episode of gastritis, resolving with protonix tr …
```

- unsupported entities (vs. transcript): numbness, warmth
- incorrect diagnosis: —  ·  missing diagnosis: bursitis, trauma
- incorrect medication: —  ·  missing medication: —
- dosage mismatch: —
- negation flips (vs. reference): abdominal pain, chest pain, chills, dyspnea, fever, nausea, vomiting
- unsupported numbers: —
- missing information: {"symptom": ["dyspnea on exertion", "seizure", "suicidal ideation"], "diagnosis": ["bursitis", "trauma"]}

## Numerical error example: `aci_bench_test_taskC_2_D2N145-virtscribe`

*numerical error example*

ROUGE-L 20.8 · length ratio 0.42 · truncated False · degenerate False · hallucination 16.7 · negation-flip 0.0 · numerical consistency 50.0 · coverage 83.3

**Transcript (excerpt)**

```
[doctor] uh , mrn49282721 . patient's name is jacqueline miller . use last visit exam where appropriate .
[doctor] hi , how are you doing , jacqueline ?
[patient] i'm pretty . good . how are you ?
[doctor] good as well . so it sounds like we're , um , under good control right now .
[patient] yes . it's doing much better .
[doctor] good , good . do you have any rash leftover ?
[patient] yeah , i have a- a small bit leftover . i started using , uh , doxycycline only one a day because i think the pharmacist said if it's getting better , to just limit it to once a day .
[doctor] okay , that sounds good .
[patient] but i was taking it twice a day and i did notice a lotta improvement .
[doctor] ok …
```

**Reference note**

```
CHIEF COMPLAINT

Follow-up for perioral dermatitis.

HISTORY OF PRESENT ILLNESS

Jacqueline Miller is a 40-year-old female who is being seen today for a follow-up skin exam for perioral dermatitis. She also has a history of rosacea, including ocular rosacea. Today, she states that her perioral dermatitis is well-controlled, although it has not fully resolved. The patient was applying doxycycline twice a day with improvement, but her pharmacist advised her to reduce to once daily since it had started to improve; therefore, for approximately the past week, she has been using the doxycycline only once per day. She has not seen continued improvement but it has not worsened. She is using the sulfacetamide wash twice daily, denies drying of the skin, and reports that her skin is much improved moisturization. She also applies MetroCream immediately after using the sulfacetamide wash. She denies …
```

**Generated note**

```
**CHIEF COMPLAINT**

*The patient reports noticing improvement with the doxycycline but the rash did not completely resolve.

*
**PHYSICAL EXAM**
Examination reveals faint erythematous papules and mild redness on both medial cheeks and around the nostrils.

**ASSESSMENT**
Perioral dermatitis and rosacea, including ocular rosacea.

**PLAN**
1. Continue using the sulfacetamide wash twice a day.
2. 3. Increase the dosage of doxycycline to twice a day.
4. 5. 6. Continue using the metrocream once a day after washing the face.
7. 8. Schedule a follow-up appointment in four weeks.
9. Provide the patient with samples of vanicream and petroleum jelly for moisturizing purposes.
10. Advise the patient to avoid using anti-aging products or plant-based treatments without consulting the provider.

**INSTRUCTIONS FOR THE PATIENT**

* Wash the face gently once a day with a mild cleanser such as vanicream.
* * Use the tacrolimus ointment twice a day until the rash resolves.
* * Continue using the metrocream once a day after washing the face.
* Avoid using any other products on the face without consul …
```

- unsupported entities (vs. transcript): physical examination
- incorrect diagnosis: —  ·  missing diagnosis: adverse drug reaction
- incorrect medication: —  ·  missing medication: —
- dosage mismatch: —
- negation flips (vs. reference): —
- unsupported numbers: 3, 6, 7, 8, 9
- missing information: {"diagnosis": ["adverse drug reaction"]}

## Missing information example: `aci_bench_test_taskC_2_D2N136-virtassist`

*missing information example*

ROUGE-L 22.7 · length ratio 0.52 · truncated False · degenerate False · hallucination 5.9 · negation-flip 0.0 · numerical consistency 50.0 · coverage 40.6

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
**CHIEF COMPLAINT**

**HISTORY OF PRESENT ILLNESS**
She mentions a past history of rotator cuff repair on her right shoulder, but states she has not experienced any issues since the procedure. Her blood sugars have been under control, and she monitors her high blood pressure with medication.

**REVIEW OF SYSTEMS**
The patient has a history of diabetes and hypertension. She also mentions monitoring her blood pressure at home.

**PHYSICAL EXAM**
The patient's physical examination revealed a slight erythema and edema on her left knee, along with a small effusion and decreased flexion and extension.
**RESULTS**
X-ray results showed a normal left knee x-ray, suggesting possible strain in the knee area. Laboratory results indicated a non-elevated white blood cell count, ruling out infection, and an elevated A1C level, but not severe enough to warrant changes in her diabetes regimen.

**ASSESSMENT AND PLAN**
Based on the patient's presentation and examination results, the assessment is likely a strain in the knee area.
* Order autoimmune labs to further investigate the cause of the left kne …
```

- unsupported entities (vs. transcript): joint swelling
- incorrect diagnosis: —  ·  missing diagnosis: —
- incorrect medication: —  ·  missing medication: amlodipine
- dosage mismatch: —
- negation flips (vs. reference): —
- unsupported numbers: 50
- missing information: {"symptom": ["chest pain", "chills", "crackles", "dyspnea", "fever", "joint pain"], "diagnosis": ["dislocation", "fracture"], "medication": ["amlodipine"], "investigation": ["autoimmune panel", "diagnostic workup", "home monitoring", "lipid panel"]}

# Split: aci_bench_test_taskC_3

## Best ROUGE-L: `aci_bench_test_taskC_3_D2N187-aci`

*highest ROUGE-L in the split*

ROUGE-L 43.3 · length ratio 0.89 · truncated False · degenerate False · hallucination 20.0 · negation-flip 0.0 · numerical consistency — · coverage 60.0

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
**CHIEF COMPLAINT**
Patient presents with sudden visual distortions and blurring of vision.

*The patient reports experiencing a decrease in vision when reading and straight lines appear crooked to her. She also mentions difficulty adjusting to dim lights in restaurants.
**REVIEW OF SYSTEMS**
The patient smokes a pack of cigarettes a day and has had difficulty stopping.
**PHYSICAL EXAM**
Anterior segment examination revealed posterior chamber intraocular lenses in both eyes. Fundus examination showed the retina to be attached without any tears or holes in the right eye. Posterior segment exam revealed drusen in the macula, thickening of the retina, presence of subretinal fluid, and exudates accumulation, along with a positive finding for hemorrhage in the right eye.

**RESULTS**
Diagnostic tests, including OCT, show drusen deposits, subretinal fluid accumulation, choroidal neovascular membrane, and focal areas of leakage in the right eye, consistent with neovascular age-related macular degeneration (AMD).

**ASSESSMENT AND PLAN**
The patient has advanced neovascular AMD, which typica …
```

- unsupported entities (vs. transcript): physical examination
- incorrect diagnosis: —  ·  missing diagnosis: —
- incorrect medication: —  ·  missing medication: —
- dosage mismatch: —
- negation flips (vs. reference): —
- unsupported numbers: —
- missing information: {"symptom": ["blurred vision"], "investigation": ["eye exam"]}

## Worst ROUGE-L: `aci_bench_test_taskC_3_D2N178-virtscribe`

*lowest ROUGE-L in the split*

ROUGE-L 13.0 · length ratio 0.22 · truncated False · degenerate False · hallucination 7.1 · negation-flip 0.0 · numerical consistency 100.0 · coverage 27.3

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
**CHIEF COMPLAINT**
The patient, Maria Martin, presents for follow-up.

*Maria reports being "pretty good" since her previous visit. She mentions that her sugars are not well-controlled, with an A1C level of 9.9. She reports experiencing pain in her feet due to peripheral neuropathy and has difficulty walking. She also mentions that she smokes and is not ready to quit.

**REVIEW OF SYSTEMS**
She denies experiencing wheezing, edema, or dry skin breakdown.

**PHYSICAL EXAM**
The doctor notes that Maria's carotids are normal, her pulse is within normal limits, and her heart exam reveals a regular rhythm with crisp S1 and S2 sounds. No murmurs were detected. Her lungs are clear, and she does not experience wheezing or rasper.
**RESULTS**
The patient's blood pressure is rechecked and found to be 140/60.

*She is advised to monitor for signs of low blood sugar, such as weakness, shakiness, and sweating.
```

- unsupported entities (vs. transcript): difficulty walking
- incorrect diagnosis: —  ·  missing diagnosis: diabetes, hyperlipidemia, hypertension, peripheral artery disease, type 2 diabetes
- incorrect medication: —  ·  missing medication: amlodipine, atorvastatin, glimepiride, hydrochlorothiazide, lisinopril, metformin, metoprolol
- dosage mismatch: —
- negation flips (vs. reference): —
- unsupported numbers: —
- missing information: {"symptom": ["cough", "foot pain", "nasal congestion", "nausea", "nocturia", "sputum"], "medical_history": ["cataract", "tobacco use", "type 2 diabetes"], "diagnosis": ["diabetes", "hyperlipidemia", "hypertension", "peripheral artery disease"], "medication": ["amlodipine", "atorvastatin", "glimepiride", "hydrochlorothiazide", "lisinopril", "metformin"], "investigation": ["blood glucose", "eye exam", "metabolic panel"]}

## Hallucination example: `aci_bench_test_taskC_3_D2N190-aci`

*hallucination example*

ROUGE-L 18.3 · length ratio 0.29 · truncated False · degenerate False · hallucination 30.0 · negation-flip 0.0 · numerical consistency 100.0 · coverage 64.3

**Transcript (excerpt)**

```
[patient] and good morning hi beverly
[doctor] good morning
[patient] how do you see your last name
[doctor] howard
[patient] howard nice to meet you
[doctor] you too
[patient] what can i do for you today
[doctor] well i think i like fell off of my tandem bike with my partner and my knee has been hurting ever since and when did that happen
[patient] maybe like two weeks ago
[doctor] okay and which knee are we talking about
[patient] my right knee
[doctor] alright and tell me exactly what happened so we were like riding together and i think he said he saw a squirrel or something like that he's a little distractible and you know like he went down so i went down i hit it on the curb like it's r …
```

**Reference note**

```
HISTORY OF PRESENT ILLNESS

Beverly Howard is a pleasant 33-year-old female who presents to the clinic today for the evaluation of right knee pain.

The patient reports that she fell off of a tandem bicycle and struck her right knee on a curb approximately 2 weeks ago. After the injury, she took ibuprofen and treated the wound, but the pain has persisted. She localizes her pain to the medial aspect of the knee. She also reports occasional clicking with full extension of the knee, as well as occasional instability with ambulation. The patient states that her pain is the worst when ambulating up an incline. She denies any previous right knee issues. She enjoys walking her dogs and swimming but has not done this since her injury.

SOCIAL HISTORY

The patient works in a Children's Hospital.

REVIEW OF SYSTEMS

Musculoskeletal: Reports right knee pain, clicking, and instability.

PHYSICAL EXA …
```

**Generated note**

```
**CHIEF COMPLAINT**

The patient presents with a complaint of knee pain and difficulty walking due to a fall from a tandem bike approximately two weeks prior.

*
The patient reports falling from a tandem bike and experiencing knee pain since the incident. She mentions taking ibuprofen for pain relief but notes that the pain persists despite medication.

*
She reports being physically active, including regular walks with her dog and occasional swimming.
**PHYSICAL EXAM**


**TESTS**

The patient underwent an x-ray examination, which revealed no obvious fractures or bone spurs.
**ASSESSMENT AND PLAN**

To confirm the diagnosis, an MRI scan is recommended. In the meantime, the patient is advised to continue taking ibuprofen up to three times daily and apply ice packs to reduce swelling. A prescription for a less frequent medication option is also offered.
**NOTES**
```

- unsupported entities (vs. transcript): difficulty walking, fracture, knee pain
- incorrect diagnosis: —  ·  missing diagnosis: sprain, trauma
- incorrect medication: —  ·  missing medication: —
- dosage mismatch: —
- negation flips (vs. reference): —
- unsupported numbers: —
- missing information: {"symptom": ["crepitus", "laceration"], "diagnosis": ["dislocation", "sprain", "trauma"]}

## Incorrect diagnosis example: `aci_bench_test_taskC_3_D2N198-aci`

*incorrect diagnosis example*

ROUGE-L 22.5 · length ratio 0.72 · truncated False · degenerate False · hallucination 15.8 · negation-flip 18.2 · numerical consistency 100.0 · coverage 71.4

**Transcript (excerpt)**

```
[doctor] okay michael so i see in here that you're here because you're experiencing some symptoms that your pcp was concerned about i also see that he ordered a ct so could you tell me what what started what happened why do you think you are here
[patient] hi doctor how are you
[doctor] hi i'm great thanks for asking
[patient] well so yeah i just happened to have gone in for my regular visit and i just explained to my pcp that you know what i've been having some back pain it's usually on the left and you know he asked some questions and he said i should come see you
[doctor] alright yeah back pain especially like that like was it sharp could you tell me what kind of pain it was
[patient] wel …
```

**Reference note**

```
CHIEF COMPLAINT

Back pain.

MEDICAL HISTORY

Patient reports that he has a frequent history of strep throat with 4 episodes within the last 5 months.

SOCIAL HISTORY

Patient reports that he is a student. He also mentions that he rides his bike every so often and that he is in the process of switching jobs. His new job will be at a restaurant.

FAMILY HISTORY

Patient reports that his siblings are mostly healthy. He does have a brother who smokes while at home.

REVIEW OF SYSTEMS

Constitutional: Denies fatigue or change in appetite.
Genitourinary: Reports increased urine output.
Musculoskeletal: Reports left-side back pain.
Endocrine: Reports increased water consumption

PHYSICAL EXAM

Ears, Nose, Mouth, and Throat
- Examination of Mouth: Normal.
- Examination of Throat: Pharynx without erythema, swelling, or exudate. Tonsils are midline.

Neck
- General Examination: Neck is supple wit …
```

**Generated note**

```
**CHIEF COMPLAINT**


**HISTORY OF PRESENT ILLNESS**

The patient reported experiencing back pain, which varies in intensity and location. Some days the pain is sharp, while others it is dull or absent. The pain is primarily located on the left side.
*
The patient denied recent sore throat, erythema, edema, lymphadenopathy, wheezing, crackles, rhonchi, murmur, or laceration. He reported a history of recurrent strep throat, with four episodes in the past five months.

**PHYSICAL EXAM**

The physical examination revealed no erythema, swelling, or cervical adenopathy upon inspection of the throat. The patient's lungs were clear, with no wheezes, rales, or rhonchi heard upon auscultation. The heart sounds were normal, with no murmurs, rubs, or gallops detected. The patient's abdomen was soft and non-tender upon palpation.

**RESULTS**

Further testing, including a CT scan, lipid panel, iron studies, and other laboratory tests, was ordered to investigate potential causes of the patient's symptoms.

*
Based on the patient's presentation and physical examination, the assessment was made tha …
```

- unsupported entities (vs. transcript): ct scan, diagnostic workup, pharyngitis
- incorrect diagnosis: pharyngitis  ·  missing diagnosis: —
- incorrect medication: —  ·  missing medication: vitamin d
- dosage mismatch: —
- negation flips (vs. reference): edema, pain
- unsupported numbers: —
- missing information: {"symptom": ["fatigue"], "medication": ["vitamin d"], "investigation": ["complete blood count", "metabolic panel", "thyroid function test", "urinalysis"]}

## Negation error example: `aci_bench_test_taskC_3_D2N170-virtassist`

*negation error example*

ROUGE-L 27.7 · length ratio 0.48 · truncated False · degenerate False · hallucination 0.0 · negation-flip 17.6 · numerical consistency 100.0 · coverage 66.7

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
**CHIEF COMPLAINT**

The patient, Joyce, presents for follow-up due to an abnormal lab finding, specifically a low hemoglobin level.

**HISTORY OF PRESENT ILLNESS**

Joyce is a 50-year-old female with a past medical history significant for COPD and congestive heart failure. She reports experiencing fatigue over the past couple of months, which has gradually worsened. She has been adherent to her treatment plan, including her medications and lifestyle modifications.

*
The patient reports being tired and exhausted, with decreased energy levels. She experiences dizziness but denies any other symptoms such as chest pain, shortness of breath, fever, chills, body aches, or weight loss. She has not noticed any swelling in her legs.

**PHYSICAL EXAM**

The patient's vital signs were within normal limits. On physical exam, the doctor noted a slight systolic ejection murmur on the patient's heart exam and tenderness to palpation in the right lower quadrant of the abdomen. No lower extremity edema was appreciated.

**RESULTS**

The patient's hemoglobin level was reported as 8.2, which is below …
```

- unsupported entities (vs. transcript): —
- incorrect diagnosis: —  ·  missing diagnosis: gi bleed
- incorrect medication: —  ·  missing medication: —
- dosage mismatch: —
- negation flips (vs. reference): bleeding, dyspnea, weight loss
- unsupported numbers: —
- missing information: {"symptom": ["blood in stool", "crackles", "lymphadenopathy", "rhonchi", "wheezing"], "medical_history": ["tobacco use"], "diagnosis": ["allergic rhinitis", "gi bleed"], "investigation": ["blood work", "hemoglobin a1c", "sodium level"]}

## Numerical error example: `aci_bench_test_taskC_3_D2N197-aci`

*numerical error example*

ROUGE-L 22.3 · length ratio 0.52 · truncated False · degenerate False · hallucination 7.7 · negation-flip 0.0 · numerical consistency 63.6 · coverage 65.0

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
**CHIEF COMPLAINT**
Patient presents with complaint of worsening headache over the past three weeks.

**HISTORY OF PRESENT ILLNESS**
The patient is a 37-year-old female with a history of hypertension and diabetes. She reports experiencing frequent headaches over the past three weeks, rated initially as a 7 out of 10 in severity. Her blood pressure readings have been elevated, with measurements of 160/87 mmHg and 175/92 mmHg over the past three weeks. She denies experiencing nasal congestion, cough, rhinorrhea, or lymphadenopathy.

*
**PHYSICAL EXAM**

**RESULTS**

**ASSESSMENT AND PLAN**
The patient will increase her lisinopril dosage to 40 mg once daily for hypertension management. Blood pressure monitoring and blood tests, including hemoglobin A1c and laboratory tests, will be ordered. The patient will receive diabetic education to manage her blood sugar levels. Exercise, including walking, is encouraged.
```

- unsupported entities (vs. transcript): physical examination
- incorrect diagnosis: —  ·  missing diagnosis: —
- incorrect medication: —  ·  missing medication: acetaminophen
- dosage mismatch: —
- negation flips (vs. reference): —
- unsupported numbers: 160, 160/87, 175, 175/92
- missing information: {"symptom": ["pain", "polyuria"], "medical_history": ["allergic rhinitis", "migraine"], "medication": ["acetaminophen"], "investigation": ["diagnostic workup", "home monitoring"]}

## Missing information example: `aci_bench_test_taskC_3_D2N185-virtscribe`

*missing information example*

ROUGE-L 18.1 · length ratio 0.26 · truncated False · degenerate False · hallucination 0.0 · negation-flip 0.0 · numerical consistency 85.7 · coverage 26.7

**Transcript (excerpt)**

```
[doctor] okay . next patient is ashley james , date of birth 12/27/2006 . ashley is a 14-year-old female , uh , who was previously healthy , now here for evaluation of abnormal renal ultrasound with an atrophic right kidney . hi . good afternoon , ashley . how are you doing ?
[patient] i'm doing okay . how are you .
[doctor] i'm doing well . thanks so much for asking . i'm dr. rogers . i'm one of your kidney doctors . and you guys must be mom and dad .
[patient] yes , that's correct .
[doctor] great . well ... all right . it's so nice to meet all of you . i wish it was under better circumstances , but we're gon na figure it all out , uh , here today . um , speaking of that , let's go ahead a …
```

**Reference note**

```
CHIEF COMPLAINT

Evaluation of abnormal renal ultrasound with atrophic right kidney.

HISTORY OF PRESENT ILLNESS

Next patient Ashley James is a 14-year-old female, previously healthy, who is here for evaluation of abnormal renal ultrasound with atrophic right kidney.

The father details a history of the patient coming home sick one day with extreme right-sided abdominal pain. Her parents brought her for evaluation, and they treated her for a stomach virus and administered fluids prior to sending her home. The next day, the patient's pain was more severe. The patient returned to the doctor's office and an ultrasound and additional testing was performed which revealed left kidney hypertrophy. At that time, they were encouraged to follow-up with her primary care physician. The patient was seen briefly by her physician the next day, which was insignificant. Ashley was still experiencing sto …
```

**Generated note**

```
**CHIEF COMPLAINT**

Ashley James, a 14-year-old female, presents for evaluation of abnormal renal ultrasound with an atrophic right kidney.

*
She was initially treated for a stomach virus but her condition worsened. An ultrasound revealed an atrophic right kidney.
*
The patient reports occasional difficulty starting to urinate and occasional burning sensation while urinating, especially after consuming carbonated beverages. There is no reported history of blood in the urine.

**PHYSICAL EXAM**

The physical exam is otherwise within normal limits.

**RESULTS**

* Ultrasound: Atrophic right kidney.
* Blood pressure: Within normal limits.
* *
*
1. 2. **Atrophic Right Kidney**: The patient has an atrophic right kidney, which may be contributing to her current symptoms.
3. **Proteinuria**: The patient is at risk for developing proteinuria due to her family history and current kidney function.
4. **Dehydration**: The patient is advised to stay well-hydrated, especially during physical activities, to prevent dehydration and strain on her kidneys.

**PLAN**

1. Annual ultrasound to monitor …
```

- unsupported entities (vs. transcript): —
- incorrect diagnosis: —  ·  missing diagnosis: chronic kidney disease, hypertension, infection
- incorrect medication: —  ·  missing medication: famotidine, loratadine
- dosage mismatch: —
- negation flips (vs. reference): —
- unsupported numbers: 6
- missing information: {"symptom": ["abdominal pain", "dysuria", "edema", "fever", "hematuria", "pain"], "medical_history": ["allergic rhinitis", "chronic kidney disease", "hypertension", "kidney transplant", "myocardial infarction", "neuropathy"], "diagnosis": ["infection", "sebaceous cyst"], "medication": ["famotidine", "loratadine"], "investigation": ["creatinine", "ct scan", "diagnostic workup", "imaging"]}

# Split: mts_dialog_test_chat_2023

## Best ROUGE-L: `mts_dialog_test_chat_2023_28`

*highest ROUGE-L in the split*

ROUGE-L 72.7 · length ratio 1.20 · truncated False · degenerate False · hallucination — · negation-flip — · numerical consistency — · coverage —

**Transcript (excerpt)**

```
Doctor: So, Doctor Pai how is your patient that you told me about?
Guest_clinician: Oh, we discharged her, she went home.
Doctor: That's great!
Guest_clinician: Yeah.
```

**Reference note**

```
The patient is discharged home.
```

**Generated note**

```
DISPOSITION:

The patient was discharged home.
```

- unsupported entities (vs. transcript): —
- incorrect diagnosis: —  ·  missing diagnosis: —
- incorrect medication: —  ·  missing medication: —
- dosage mismatch: —
- negation flips (vs. reference): —
- unsupported numbers: —
- missing information: {}

## Worst ROUGE-L: `mts_dialog_test_chat_2023_54`

*lowest ROUGE-L in the split*

ROUGE-L 0.0 · length ratio 12.29 · truncated False · degenerate False · hallucination 12.5 · negation-flip 0.0 · numerical consistency — · coverage 33.3

**Transcript (excerpt)**

```
Doctor: Have you been checking your blood sugar regularly? 
Patient: Yes, I check it twice a day and I make sure to record the readings each time. 
Doctor: That's great to hear. Do you mind if I take a look at the readings you brought with you today? 
Patient: No, it's not a problem. Here, let me get my bag. 
Doctor: Have you been experiencing any dizziness, excessive urination, fatigue, weight loss, or any other symptoms? 
Patient: No. 
Doctor: I have a copy of your blood work right here and it looks like your cholesterol is still pretty high. I'd like you to continue taking the cholesterol medication I prescribed and monitoring your cholesterol intake. 
Patient: I need to do a better job o …
```

**Reference note**

```
1.  Hypercholesterolemia. 2.  Diabetes mellitus. 3.  Sinusitis.
```

**Generated note**

```
ASSESSMENT:

The patient reports no current symptoms such as dizziness, excessive urination, fatigue, or weight loss.

Current medications include cholesterol medication, which will be continued under close monitoring. There is mention of past use of azithromycin (Z Pak), which has resulted in significant improvement of the patient's sinus symptoms.

Recent blood work indicates elevated cholesterol levels, for which the patient will continue to monitor their cholesterol intake.

A follow-up appointment is scheduled in a few weeks to re-evaluate the patient's condition and obtain further blood work.
```

- unsupported entities (vs. transcript): hyperlipidemia
- incorrect diagnosis: hyperlipidemia  ·  missing diagnosis: —
- incorrect medication: —  ·  missing medication: —
- dosage mismatch: —
- negation flips (vs. reference): —
- unsupported numbers: —
- missing information: {"diagnosis": ["diabetes", "sinusitis"]}

## Hallucination example: `mts_dialog_test_chat_2023_168`

*hallucination example*

ROUGE-L 26.7 · length ratio 0.83 · truncated False · degenerate False · hallucination 44.4 · negation-flip 0.0 · numerical consistency 100.0 · coverage 58.3

**Transcript (excerpt)**

```
Doctor: Has your E coli improved since your last visit, ma'am?
Patient: Yes, but I had some complications with the medicine.
Doctor: You were taking the Macrobid, correct?
Patient: Yes, I took it once a day at night for about seven days. 
Doctor: What complications did you have?
Patient: Well, I had a skin rash and hives, so I discontinued the medicine.
Doctor: Since stopping the medicine, have these symptoms gone away?
Patient: Yes, since I stopped taking the medicine.
Doctor: Do you have any pain with urination or blood in your urine?
Patient: No, nothing to report there.
Doctor: What about fever or chills?
Patient: No, nothing there either.
Doctor: Good, how many times a day do you urinat …
```

**Reference note**

```
The patient presents today for followup, recently noted for E. coli urinary tract infection.  She was treated with Macrobid for 7 days, and only took one nighttime prophylaxis.  She discontinued this medication to due to skin rash as well as hives.  Since then, this had resolved.  Does not have any dysuria, gross hematuria, fever, chills.  Daytime frequency every two to three hours, nocturia times one, no incontinence, improving stress urinary incontinence after Prometheus pelvic rehabilitation. Renal ultrasound, August 5, 2008, reviewed, no evidence of hydronephrosis, bladder mass or stone.  Discussed. Previous urine cultures have shown E. coli, November 2007, May 7, 2008 and July 7, 2008.
```

**Generated note**

```
HISTORY OF PRESENT ILLNESS:

The patient reports an improvement in her E coli infection since her last visit. However, she experienced complications with the prescribed medication, Macrobid, which included a skin rash and hives. These symptoms resolved after discontinuing the medication. The patient denies experiencing dysuria, fever, or chills. She reports frequent urination, approximately every two to three hours, with occasional nighttime voiding. Despite previous urinary tract infections, including episodes in November 2007 and May/July 2008, the patient currently has no complaints regarding pain with urination or hematuria.
```

- unsupported entities (vs. transcript): hematuria, infection, urinary frequency, urinary tract infection
- incorrect diagnosis: —  ·  missing diagnosis: —
- incorrect medication: —  ·  missing medication: —
- dosage mismatch: —
- negation flips (vs. reference): —
- unsupported numbers: —
- missing information: {"symptom": ["nocturia", "urinary incontinence"], "diagnosis": ["hydronephrosis"], "investigation": ["ultrasound", "urine culture"]}

## Incorrect diagnosis example: `mts_dialog_test_chat_2023_54`

*incorrect diagnosis example*

ROUGE-L 0.0 · length ratio 12.29 · truncated False · degenerate False · hallucination 12.5 · negation-flip 0.0 · numerical consistency — · coverage 33.3

**Transcript (excerpt)**

```
Doctor: Have you been checking your blood sugar regularly? 
Patient: Yes, I check it twice a day and I make sure to record the readings each time. 
Doctor: That's great to hear. Do you mind if I take a look at the readings you brought with you today? 
Patient: No, it's not a problem. Here, let me get my bag. 
Doctor: Have you been experiencing any dizziness, excessive urination, fatigue, weight loss, or any other symptoms? 
Patient: No. 
Doctor: I have a copy of your blood work right here and it looks like your cholesterol is still pretty high. I'd like you to continue taking the cholesterol medication I prescribed and monitoring your cholesterol intake. 
Patient: I need to do a better job o …
```

**Reference note**

```
1.  Hypercholesterolemia. 2.  Diabetes mellitus. 3.  Sinusitis.
```

**Generated note**

```
ASSESSMENT:

The patient reports no current symptoms such as dizziness, excessive urination, fatigue, or weight loss.

Current medications include cholesterol medication, which will be continued under close monitoring. There is mention of past use of azithromycin (Z Pak), which has resulted in significant improvement of the patient's sinus symptoms.

Recent blood work indicates elevated cholesterol levels, for which the patient will continue to monitor their cholesterol intake.

A follow-up appointment is scheduled in a few weeks to re-evaluate the patient's condition and obtain further blood work.
```

- unsupported entities (vs. transcript): hyperlipidemia
- incorrect diagnosis: hyperlipidemia  ·  missing diagnosis: —
- incorrect medication: —  ·  missing medication: —
- dosage mismatch: —
- negation flips (vs. reference): —
- unsupported numbers: —
- missing information: {"diagnosis": ["diabetes", "sinusitis"]}

## Negation error example: `mts_dialog_test_chat_2023_11`

*negation error example*

ROUGE-L 22.2 · length ratio 1.63 · truncated False · degenerate False · hallucination 20.0 · negation-flip 75.0 · numerical consistency — · coverage 80.0

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
REVIEW OF SYSTEMS:

* General:
  - Fever or chills: None
  - Duration of current illness: Few days
* Gastrointestinal:
  - Abdominal pain or discomfort: Uneasiness in stomach for a few days
  - History of ulcers: No
* Hepatobiliary:
  - Liver problems: No
  - Gallbladder stones: No
* Immunizations:
  - Vaccinations: Received BCG vaccine in childhood
```

- unsupported entities (vs. transcript): abdominal pain
- incorrect diagnosis: —  ·  missing diagnosis: —
- incorrect medication: —  ·  missing medication: —
- dosage mismatch: —
- negation flips (vs. reference): chills, fever, peptic ulcer disease
- unsupported numbers: —
- missing information: {"medical_history": ["cholecystitis"]}

## Numerical error example: `mts_dialog_test_chat_2023_169`

*numerical error example*

ROUGE-L 24.1 · length ratio 2.62 · truncated False · degenerate False · hallucination 0.0 · negation-flip 0.0 · numerical consistency 0.0 · coverage 55.6

**Transcript (excerpt)**

```
Doctor: Tylenol?
Patient: I take P M for sleeplessness.
Doctor: Okay. What other medications do you take?
Patient: Water pill and blood thinner. Then some multivitamins and folic.
Doctor: Okay I see Norvasc and Lanoxin too.
Patient: Yes, and my blood pressure medications should be there as well.
Doctor: Yes, I see, Diovan and Atenolol.
Patient: That sounds about right.
```

**Reference note**

```
The patient takes Tylenol PM for insomnia, Lasix, Coumadin, Norvasc, Lanoxin, Diovan, atenolol, and folic acid.
```

**Generated note**

```
MEDICATIONS:

The patient reports taking the following medications:

1. 2. Anticoagulant (blood thinner)
3. Multivitamin
4. Amlodipine (Norvasc)
5. Digoxin (Lanoxin)
6. Valsartan (Diovan)
7. Atelol (Atenolol)

Note: Acetaminophen was mentioned by the doctor, but the patient did not confirm taking it.
```

- unsupported entities (vs. transcript): —
- incorrect diagnosis: —  ·  missing diagnosis: —
- incorrect medication: —  ·  missing medication: folic acid, furosemide, warfarin
- dosage mismatch: —
- negation flips (vs. reference): —
- unsupported numbers: 1, 2, 3, 4, 5, 6, 7
- missing information: {"symptom": ["insomnia"], "medication": ["folic acid", "furosemide", "warfarin"]}

## Missing information example: `mts_dialog_test_chat_2023_95`

*missing information example*

ROUGE-L 17.4 · length ratio 0.71 · truncated False · degenerate False · hallucination 0.0 · negation-flip 0.0 · numerical consistency 100.0 · coverage 15.4

**Transcript (excerpt)**

```
Doctor: Hello there!
Patient: Hi, how are you? 
Doctor: I am good. Do ypu mind stating your age and waht brings you in today? 
Patient: Oh, yes, I am 85 years old and I am having this weird muscle pain in my rightbuttocks region that I think it's radiating from my lower back or spine area I am not sure.
Doctor: Hm, what kind of pain is it? Like sharp pain or dull? 
Patient: It's kind of difficult to explain, but it's very irritating. 
Doctor: Okay! So, it's on the right side?
Patient: Yes.
Doctor: And when was your last visit to renal clinic? 
Patient: About four months back.
Doctor: Hm and you mentioned you are doing much better than before in terms of managing your high blood pressure with …
```

**Reference note**

```
This is a return visit to the renal clinic for this patient.  She is an 85-year-old woman with history as noted above.  Her last visit was approximately four months ago.  Since that time, the patient has been considerably more compliant with her antihypertensive medications and actually had a better blood pressure reading today than she had had for many visits previously.  She is not reporting any untoward side effect.  She is not having weakness, dizziness, lightheadedness, nausea, vomiting, constipation, diarrhea, abdominal pain, chest pain, shortness of breath or difficulty breathing.  She has no orthopnea.  Her exercise capacity is about the same.  The only problem she has is musculoskeletal and that pain in the right buttock, she thinks originating from her spine.  No history of extremity pain.
```

**Generated note**

```
HISTORY OF PRESENT ILLNESS:

This 85-year-old patient presents with a complaint of muscle pain in the right buttock region, which she believes is radiating from her lower back or spine area. She describes the pain as "irritating" and states that it is difficult to explain.
Her past medical history includes hypertension, for which she claims to be doing well with her current medication regimen. She denies any side effects from her medication.

However, she does report current hip pain.

She has tried taking acetaminophen (Tylenol), which provides some relief.
```

- unsupported entities (vs. transcript): —
- incorrect diagnosis: —  ·  missing diagnosis: —
- incorrect medication: —  ·  missing medication: —
- dosage mismatch: —
- negation flips (vs. reference): —
- unsupported numbers: —
- missing information: {"symptom": ["abdominal pain", "chest pain", "constipation", "diarrhea", "dizziness", "dyspnea"], "investigation": ["blood pressure measurement"]}

# Split: mts_dialog_test_sum_2023

## Best ROUGE-L: `mts_dialog_test_sum_2023_194`

*highest ROUGE-L in the split*

ROUGE-L 64.7 · length ratio 1.46 · truncated False · degenerate False · hallucination — · negation-flip — · numerical consistency — · coverage —

**Transcript (excerpt)**

```
Guest_clinician: So, you discharged Mister Henley?
Doctor: Yes, he has been moved to a long term acute care facility under the supervision of Doctor Z.
Guest_clinician: Okay.
```

**Reference note**

```
The patient discharged to long-term acute facility under the care of Dr. Z.
```

**Generated note**

```
DISPOSITION:

Patient was discharged to a long-term acute care facility for further management under the supervision of Doctor Z.
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

ROUGE-L 0.0 · length ratio 15.00 · truncated False · degenerate False · hallucination — · negation-flip — · numerical consistency — · coverage —

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
OTHER HISTORY:

The patient denies smoking and drinking.

Family history of medical problems is negative.
```

- unsupported entities (vs. transcript): —
- incorrect diagnosis: —  ·  missing diagnosis: —
- incorrect medication: —  ·  missing medication: —
- dosage mismatch: —
- negation flips (vs. reference): —
- unsupported numbers: —
- missing information: {}

## Hallucination example: `mts_dialog_test_sum_2023_67`

*hallucination example*

ROUGE-L 17.0 · length ratio 0.61 · truncated False · degenerate False · hallucination 28.6 · negation-flip — · numerical consistency 100.0 · coverage 0.0

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
HISTORY OF PRESENT ILLNESS:

She reported generally good health during this period, with her sugars remaining within target ranges until two weeks prior when she experienced difficulties with her insulin pump. Despite efforts to troubleshoot the issue, she ultimately replaced the pump and encountered challenges setting it up, leading to variable blood glucose control.

During this period, the patient denied experiencing symptoms such as sweating, fatigue, dizziness, confusion, loss of consciousness, fainting, lightheadedness, changes in vision, or confusion. However, she mentioned possible difficulties with managing her postprandial and fasting blood glucose levels. Her usual routine includes following a fixed diet and engaging in physical activities through childcare responsibilities. She works full-time as a medical coder and occasionally misses meals due to her demanding schedule.
```

- unsupported entities (vs. transcript): insulin, syncope
- incorrect diagnosis: —  ·  missing diagnosis: —
- incorrect medication: insulin  ·  missing medication: —
- dosage mismatch: —
- negation flips (vs. reference): —
- unsupported numbers: —
- missing information: {"symptom": ["polydipsia", "polyphagia", "polyuria"], "medical_history": ["type 1 diabetes"], "diagnosis": ["diabetes"], "investigation": ["blood work", "lipid panel"]}

## Incorrect diagnosis example: `mts_dialog_test_sum_2023_145`

*incorrect diagnosis example*

ROUGE-L 28.3 · length ratio 0.51 · truncated False · degenerate False · hallucination 66.7 · negation-flip 0.0 · numerical consistency 100.0 · coverage 50.0

**Transcript (excerpt)**

```
Doctor: Good morning, sir, I hear someone just had a birthday. 
Patient: Good morning, I just turned sixty nine. 
Doctor: Congratulations on another year! 
Patient: Thank you, doctor. 
Doctor: So, I have a resident with me today, I'm just going to run over your background information with her really quick, is that okay, sir?
Patient: Sure, that's no problem. 
Doctor: Great, thank you. So, this is an African American gentleman who has stage four C K D secondary to P K D. He's had a high creatinine level over the last six months, so we've been following him closely. 
Patient: Yes, that's all correct, doctor. 
Doctor: Have you been going to the end stage kidney disease classes? 
Patient: No, I  …
```

**Reference note**

```
This is a followup for this 69-year-old African American gentleman with stage IV chronic kidney disease secondary to polycystic kidney disease.  His creatinine has ranged between 4 and 4.5 over the past 6 months, since I have been following him.  I have been trying to get him educated about end-stage kidney disease and we have been unsuccessful in getting him into classes.  On his last visit, I really stressed the importance of him taking his medications adequately and not missing some of the doses, and he returns today with much better blood pressure control.  He has also brought a machine at home, and states his blood pressure readings have been better.  He has not gone to the transplant orientation class yet and has not been to dialysis education yet, and both of these I have discussed with him in the past.  He also needs followup for his elevated PSA in the past, which has not been d …
```

**Generated note**

```
HISTORY OF PRESENT ILLNESS:

This patient is a 69-year-old African American male with a history of stage four chronic kidney disease (CKD) secondary to polycystic kidney disease (PKD).

The patient expresses difficulty attending educational classes regarding end-stage renal disease (ESRD), including transplant orientation and dialysis education classes. He acknowledges the importance of participating in these classes but has not done so yet.

A Prostate-Specific Antigen (PSA) test is scheduled today, approximately two years after the previous test. This is necessary for potential future cardiac clearance if a kidney transplant is considered.
```

- unsupported entities (vs. transcript): kidney transplant, psa
- incorrect diagnosis: kidney transplant  ·  missing diagnosis: —
- incorrect medication: —  ·  missing medication: —
- dosage mismatch: —
- negation flips (vs. reference): —
- unsupported numbers: —
- missing information: {"investigation": ["blood pressure measurement", "creatinine"]}

## Incorrect medication / dosage example: `mts_dialog_test_sum_2023_67`

*incorrect medication / dosage example*

ROUGE-L 17.0 · length ratio 0.61 · truncated False · degenerate False · hallucination 28.6 · negation-flip — · numerical consistency 100.0 · coverage 0.0

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
HISTORY OF PRESENT ILLNESS:

She reported generally good health during this period, with her sugars remaining within target ranges until two weeks prior when she experienced difficulties with her insulin pump. Despite efforts to troubleshoot the issue, she ultimately replaced the pump and encountered challenges setting it up, leading to variable blood glucose control.

During this period, the patient denied experiencing symptoms such as sweating, fatigue, dizziness, confusion, loss of consciousness, fainting, lightheadedness, changes in vision, or confusion. However, she mentioned possible difficulties with managing her postprandial and fasting blood glucose levels. Her usual routine includes following a fixed diet and engaging in physical activities through childcare responsibilities. She works full-time as a medical coder and occasionally misses meals due to her demanding schedule.
```

- unsupported entities (vs. transcript): insulin, syncope
- incorrect diagnosis: —  ·  missing diagnosis: —
- incorrect medication: insulin  ·  missing medication: —
- dosage mismatch: —
- negation flips (vs. reference): —
- unsupported numbers: —
- missing information: {"symptom": ["polydipsia", "polyphagia", "polyuria"], "medical_history": ["type 1 diabetes"], "diagnosis": ["diabetes"], "investigation": ["blood work", "lipid panel"]}

## Negation error example: `mts_dialog_test_sum_2023_159`

*negation error example*

ROUGE-L 22.1 · length ratio 1.08 · truncated False · degenerate False · hallucination 14.3 · negation-flip 40.0 · numerical consistency 0.0 · coverage 55.6

**Transcript (excerpt)**

```
Doctor: Hello sir. How are you doing? 
Patient: I'm fine. Thank you. 
Doctor: What brings you here today? 
Patient: I don't know. I feel like I have so many problems that I want to discuss with you .  
Doctor: Sure, tell me what's going on. 
Patient: My mouth has been sore since last week.  There is something going on with my eyes. I have some trouble with my eyes. I feel funny, but I'm seeing okay, my vision is fine. 
Doctor: How's your diarrhea and the pain in the abdomen? 
Patient: It's been better. There has been no more diarrhea or pain. 
Doctor: How is the bowel movement? 
Patient: It's working well. 
Doctor: Any nausea or vomiting? 
Patient: No. 
Doctor: How are your eating habits now …
```

**Reference note**

```
The patient is in with several medical problems.  He complains his mouth being sore since last week and also some "trouble with my eyes."  He states that they feel "funny" but he is seeing okay.  He denies any more diarrhea or abdominal pain.  Bowels are working okay.  He denies nausea or diarrhea.  Eating is okay.  He is emptying his bladder okay.  He denies dysuria.  His back is hurting worse.  He complains of right shoulder pain and neck pain over the last week but denies any injury.  He reports that his cough is about the same.
```

**Generated note**

```
HISTORY OF PRESENT ILLNESS:

The patient presents with a one-week history of oral mucosal discomfort described as "soreness." Additionally, he reports eye troubles without specifying the nature of the issue, stating his vision is unaffected.

He initially reported gastrointestinal issues including diarrhea and abdominal pain, which have resolved. He denies current nausea and vomiting. His bowel movements are currently normal, and his appetite appears to be intact. Urinary function seems unimpaired, with no complaints of painful urination.

Respiratory symptoms include a persistent cough, described as unchanged over time. Musculoskeletal concerns involve ongoing pain in the back, shoulder, and neck, which began last week.
```

- unsupported entities (vs. transcript): dysuria
- incorrect diagnosis: —  ·  missing diagnosis: —
- incorrect medication: —  ·  missing medication: —
- dosage mismatch: —
- negation flips (vs. reference): abdominal pain, diarrhea
- unsupported numbers: 1
- missing information: {"symptom": ["back pain", "neck pain", "shoulder pain"], "diagnosis": ["trauma"]}

## Numerical error example: `mts_dialog_test_sum_2023_176`

*numerical error example*

ROUGE-L 20.3 · length ratio 1.81 · truncated False · degenerate False · hallucination 0.0 · negation-flip 0.0 · numerical consistency 0.0 · coverage 50.0

**Transcript (excerpt)**

```
Guest_clinician: Can you give me a quick rundown of her medical history please.
Doctor: Sure. She has a history of migraine headaches without aura. She also has left ear sensorineural deafness and basil cell carcinoma resection on the nose.
Guest_clinician: Do you happen to know when she had that resection done?
Doctor: I asked her but she couldn't remember. She said it was sometime within the last couple of years.
Guest_clinician: Okay, got it.
Doctor: She also suffers from essential tremors, endometriosis, and cervical dystonia.
```

**Reference note**

```
Essential tremor, cervical dystonia, endometriosis, migraine headaches without aura, left ear sensorineural deafness, and basal cell carcinoma resection on the nose.
```

**Generated note**

```
PAST MEDICAL HISTORY:

The patient has a history of:

1. 2. 3. Basil cell carcinoma resection on the nose (exact date unknown, occurred within the last couple of years)
4. Essential tremors
5. Endometriosis
6. Cervical dystonia

Note:
```

- unsupported entities (vs. transcript): —
- incorrect diagnosis: —  ·  missing diagnosis: —
- incorrect medication: —  ·  missing medication: —
- dosage mismatch: —
- negation flips (vs. reference): —
- unsupported numbers: 1, 2, 3, 4, 5, 6
- missing information: {"diagnosis": ["migraine", "skin cancer"]}

## Missing information example: `mts_dialog_test_sum_2023_67`

*missing information example*

ROUGE-L 17.0 · length ratio 0.61 · truncated False · degenerate False · hallucination 28.6 · negation-flip — · numerical consistency 100.0 · coverage 0.0

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
HISTORY OF PRESENT ILLNESS:

She reported generally good health during this period, with her sugars remaining within target ranges until two weeks prior when she experienced difficulties with her insulin pump. Despite efforts to troubleshoot the issue, she ultimately replaced the pump and encountered challenges setting it up, leading to variable blood glucose control.

During this period, the patient denied experiencing symptoms such as sweating, fatigue, dizziness, confusion, loss of consciousness, fainting, lightheadedness, changes in vision, or confusion. However, she mentioned possible difficulties with managing her postprandial and fasting blood glucose levels. Her usual routine includes following a fixed diet and engaging in physical activities through childcare responsibilities. She works full-time as a medical coder and occasionally misses meals due to her demanding schedule.
```

- unsupported entities (vs. transcript): insulin, syncope
- incorrect diagnosis: —  ·  missing diagnosis: —
- incorrect medication: insulin  ·  missing medication: —
- dosage mismatch: —
- negation flips (vs. reference): —
- unsupported numbers: —
- missing information: {"symptom": ["polydipsia", "polyphagia", "polyuria"], "medical_history": ["type 1 diabetes"], "diagnosis": ["diabetes"], "investigation": ["blood work", "lipid panel"]}
