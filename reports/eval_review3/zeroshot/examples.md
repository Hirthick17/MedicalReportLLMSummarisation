# Example errors — zeroshot

Each block shows the transcript excerpt, the reference note, the generated note and the flags raised by the factuality checker.

# Split: aci_bench_test_taskB_1

## Best ROUGE-L: `aci_bench_test_taskB_1_D2N126-aci`

*highest ROUGE-L in the split*

ROUGE-L 39.3 · length ratio 0.76 · truncated False · degenerate False · hallucination 31.6 · negation-flip 0.0 · numerical consistency 100.0 · coverage 89.5

**Transcript (excerpt)**

```
[doctor] hi michelle what's been going on the medical assistant told me that you injured your knee
[patient] yeah i'm gon na have to keep this my favorite story is that i had a sandra who injured her knee cold dancing so that would immediately came up to mine but let's try skiing so i was skiing in vermont last weekend and i caught my ski when i was coming off the lift and i fell and my knee popped and it's hurt ever since
[doctor] okay and were you able to ski down the hill or did you have to be taken down by the ski patrol
[patient] i had to be taken down by the ski patrol i was unable to bear weight
[doctor] okay is n't that slightly terrifying they had to do the same thing for me and you …
```

**Reference note**

```
CHIEF COMPLAINT

Right knee injury

HISTORY OF PRESENT ILLNESS

Michelle King is a pleasant 44-year-old male who presents to the clinic today for the evaluation of a right knee injury. Her injury was sustained while skiing in Vermont last weekend after she caught her ski when coming off of the lift and fell. She reports a pop in her knee at the time of injury and has been experiencing pain since that time. Due to her fall she was unable to weight bear and had to be taken down by the ski patrol. She locates her pain to the lateral aspect of her knee and also describes the feeling of instability as well as buckling. At this time she is experiencing difficulty with knee flexion; however, she states this was not a problem immediately after the injury. Full knee extension is also quite painful for her. The patient denies any numbness or tingling in her toes. She is currently utilizing crutche …
```

**Generated note**

```
**CHIEF COMPLAINT**

Patient presents with complaint of right knee pain following a skiing accident.

**HISTORY OF PRESENT ILLNESS**

The patient, a 4-year-old mother of twins, sustained a right knee injury while skiing in Vermont last weekend. She reports catching her ski and falling, resulting in her knee "popping" and experiencing persistent pain since then. The patient was unable to bear weight and required assistance from the ski patrol. She describes the pain as located on the outside of the knee, with a feeling of instability and potential buckling. She has difficulty bending and straightening the knee, particularly upon full extension. There is no numbness or tingling in the toes.

**REVIEW OF SYSTEMS**

The patient denies any significant medical history, including hypertension, diabetes, or other chronic conditions. She takes ibuprofen for pain relief, which provides some symptom management.

**PHYSICAL EXAM**

The patient's heart exam reveals a regular rate and rhythm without murmurs. Lung exam shows clear auscultation. Right knee examination demonstrates:

* Edema and effu …
```

- unsupported entities (vs. transcript): acl tear, crepitus, joint instability, knee pain, mri, numbness
- incorrect diagnosis: —  ·  missing diagnosis: —
- incorrect medication: —  ·  missing medication: —
- dosage mismatch: [{"drug": "ibuprofen", "predicted": "600-800 mg", "source": ["600 to 800 mg"]}]
- negation flips (vs. reference): —
- unsupported numbers: —
- missing information: {"symptom": ["reduced range of motion"], "diagnosis": ["trauma"]}

## Worst ROUGE-L: `aci_bench_test_taskB_1_D2N099-virtscribe`

*lowest ROUGE-L in the split*

ROUGE-L 20.1 · length ratio 0.90 · truncated False · degenerate False · hallucination 30.8 · negation-flip 0.0 · numerical consistency 100.0 · coverage 53.3

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

The patient, Randy Gutierrez, presents with a complaint of illness lasting approximately one day, with symptoms including a runny nose, congestion, cough (non-barky), irritability, difficulty sleeping, and low-grade fever.

**HISTORY OF PRESENT ILLNESS**

Randy began experiencing symptoms around supper time last night. He developed a runny nose, congestion, and cough. His mother reported that his mucous is currently clear. The patient has been pulling on his ears and has been irritable due to discomfort. A low-grade fever of 100.3°F was noted via rectal temperature. Appetite has been variable, with Randy eating some food last night and having a small amount of breakfast this morning. Energy levels appear normal despite irritability.

**REVIEW OF SYSTEMS**

* Respiratory: Runny nose, congestion, non-barky cough.
* Ears: Pulling on ears, no apparent ear infection.
* Eyes: No mention of eye problems.
* Skin: Cradle cap present, worsening.
* Fever: Low-grade fever of 100.3°F.
* General: Irritability, difficulty sleeping.

**PHYSICAL EXAM**

Auto-text URI: Physical ex …
```

- unsupported entities (vs. transcript): blood work, insomnia, otitis media, upper respiratory infection
- incorrect diagnosis: —  ·  missing diagnosis: croup
- incorrect medication: —  ·  missing medication: saline nasal spray
- dosage mismatch: —
- negation flips (vs. reference): —
- unsupported numbers: —
- missing information: {"symptom": ["hoarseness", "purulent drainage", "sore throat", "sweating", "warmth"], "diagnosis": ["croup"], "medication": ["saline nasal spray"]}

## Hallucination example: `aci_bench_test_taskB_1_D2N126-aci`

*hallucination example*

ROUGE-L 39.3 · length ratio 0.76 · truncated False · degenerate False · hallucination 31.6 · negation-flip 0.0 · numerical consistency 100.0 · coverage 89.5

**Transcript (excerpt)**

```
[doctor] hi michelle what's been going on the medical assistant told me that you injured your knee
[patient] yeah i'm gon na have to keep this my favorite story is that i had a sandra who injured her knee cold dancing so that would immediately came up to mine but let's try skiing so i was skiing in vermont last weekend and i caught my ski when i was coming off the lift and i fell and my knee popped and it's hurt ever since
[doctor] okay and were you able to ski down the hill or did you have to be taken down by the ski patrol
[patient] i had to be taken down by the ski patrol i was unable to bear weight
[doctor] okay is n't that slightly terrifying they had to do the same thing for me and you …
```

**Reference note**

```
CHIEF COMPLAINT

Right knee injury

HISTORY OF PRESENT ILLNESS

Michelle King is a pleasant 44-year-old male who presents to the clinic today for the evaluation of a right knee injury. Her injury was sustained while skiing in Vermont last weekend after she caught her ski when coming off of the lift and fell. She reports a pop in her knee at the time of injury and has been experiencing pain since that time. Due to her fall she was unable to weight bear and had to be taken down by the ski patrol. She locates her pain to the lateral aspect of her knee and also describes the feeling of instability as well as buckling. At this time she is experiencing difficulty with knee flexion; however, she states this was not a problem immediately after the injury. Full knee extension is also quite painful for her. The patient denies any numbness or tingling in her toes. She is currently utilizing crutche …
```

**Generated note**

```
**CHIEF COMPLAINT**

Patient presents with complaint of right knee pain following a skiing accident.

**HISTORY OF PRESENT ILLNESS**

The patient, a 4-year-old mother of twins, sustained a right knee injury while skiing in Vermont last weekend. She reports catching her ski and falling, resulting in her knee "popping" and experiencing persistent pain since then. The patient was unable to bear weight and required assistance from the ski patrol. She describes the pain as located on the outside of the knee, with a feeling of instability and potential buckling. She has difficulty bending and straightening the knee, particularly upon full extension. There is no numbness or tingling in the toes.

**REVIEW OF SYSTEMS**

The patient denies any significant medical history, including hypertension, diabetes, or other chronic conditions. She takes ibuprofen for pain relief, which provides some symptom management.

**PHYSICAL EXAM**

The patient's heart exam reveals a regular rate and rhythm without murmurs. Lung exam shows clear auscultation. Right knee examination demonstrates:

* Edema and effu …
```

- unsupported entities (vs. transcript): acl tear, crepitus, joint instability, knee pain, mri, numbness
- incorrect diagnosis: —  ·  missing diagnosis: —
- incorrect medication: —  ·  missing medication: —
- dosage mismatch: [{"drug": "ibuprofen", "predicted": "600-800 mg", "source": ["600 to 800 mg"]}]
- negation flips (vs. reference): —
- unsupported numbers: —
- missing information: {"symptom": ["reduced range of motion"], "diagnosis": ["trauma"]}

## Incorrect diagnosis example: `aci_bench_test_taskB_1_D2N112-aci`

*incorrect diagnosis example*

ROUGE-L 30.5 · length ratio 0.53 · truncated False · degenerate False · hallucination 33.3 · negation-flip 0.0 · numerical consistency 88.9 · coverage 60.0

**Transcript (excerpt)**

```
[doctor] hey matthew i see here that you've had some back pain for a while and your pcp sent you over to see me how're you doing today
[patient] pretty good i'm feeling pretty good do n't like the weather you know i've been sitting in the waiting area for you know thirty minutes and that definitely makes the symptoms worse
[doctor] okay well first of all i i agree with you the weather has kinda been all over the place been hot and been cold and and and now it seems like we've had a week of pretty chilly weather hopefully that changes pretty soon so tell me a little bit about when when your back pain started and and and what happened there
[patient] well you wan na hear the long story or kind …
```

**Reference note**

```
HISTORY OF PRESENT ILLNESS

Matthew Hill is a pleasant 44-year-old male who presents to the clinic today for the evaluation of back pain. The patient was referred from his primary care physician. The onset of his pain began 30 years ago, when he fell off of a roof. He endorses that it was very bothersome and he was unable to play football. He states that he was told that he may have a fracture at that time. The patient reports that his pain has worsened 1 month ago. He locates his pain to his lower back, which radiates into his left hip, down his left leg, on the side of his calf, and into his left big toe. The patient describes his pain as an "electrical tooth ache" that radiates down his entire left leg. He notes that he has to use a cane to walk as his left foot drags when he walks. He rates his pain level as a 6 to 8 out of 10, however it can get to a 13 out of 10 at its worst. He st …
```

**Generated note**

```
**CHIEF COMPLAINT**

Patient presents with complaints of chronic lower back pain radiating to the left leg, exacerbated by standing and improved by lying down.

**HISTORY OF PRESENT ILLNESS**

The patient reports experiencing lower back pain for an extended period, with worsening symptoms over the past month. The pain is described as an "electrical toothache" and radiates down the entire left leg. The patient rates the pain as 6/10 currently, but up to 13/10 at its worst. Activities such as standing, walking, and coughing/sneezing exacerbate the pain, whereas lying down provides temporary relief. The patient also mentions weakness in both lower extremities, particularly in the back, and difficulty walking due to dragging his foot.

**REVIEW OF SYSTEMS**

No specific systemic symptoms were reported.

**PHYSICAL EXAM**

*   Vitals: normal
*   Back exam: tenderness at L4 vertebrae, pain with flexion and extension
*   Strength: 4/5 in the left leg and 5/5 in the right leg
*   Reflexes: brisk and intact in both lower extremities
*   Sensory: intact in both lower extremities

**RESULTS**

 …
```

- unsupported entities (vs. transcript): difficulty walking, mri, sciatica, tooth pain
- incorrect diagnosis: sciatica  ·  missing diagnosis: —
- incorrect medication: —  ·  missing medication: —
- dosage mismatch: —
- negation flips (vs. reference): —
- unsupported numbers: 13/10
- missing information: {"symptom": ["bruising", "erythema", "falls", "numbness", "tingling"], "diagnosis": ["fracture"]}

## Incorrect medication / dosage example: `aci_bench_test_taskB_1_D2N091-virtassist`

*incorrect medication / dosage example*

ROUGE-L 37.3 · length ratio 0.71 · truncated False · degenerate False · hallucination 13.3 · negation-flip 0.0 · numerical consistency 85.7 · coverage 70.6

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
**CHIEF COMPLAINT**

Jerry, a 54-year-old male, presents for an annual exam.

**HISTORY OF PRESENT ILLNESS**

The patient reports a stressful summer due to extensive travel, resulting in lack of sleep. He has tried various strategies for insomnia, including melatonin, meditation, and stretching exercises, without relief. His osteoporosis treatment consists of Fosamax, and he denies any issues with his joints or recent fractures. He takes medication for multiple sclerosis, which he started approximately six months ago, and reports no issues with the medication. He mentions a lingering issue with his right knee following surgery but states that his strength is generally good.

**REVIEW OF SYSTEMS**

The patient endorses insomnia as noted on the review of systems sheet. He denies any other issues, including chest pain, shortness of breath, or other concerns.

**PHYSICAL EXAM**

Vital signs are within normal limits. Physical examination reveals weakness of the lower extremities, with the right side being 4/5 and the left side being 3/5. Reflexes are good. Arthritic changes are noted in t …
```

- unsupported entities (vs. transcript): blood work, vaccine
- incorrect diagnosis: —  ·  missing diagnosis: osteoarthritis
- incorrect medication: vaccine  ·  missing medication: —
- dosage mismatch: [{"drug": "alendronate", "predicted": "1 tablet", "source": ["1 tab"]}]
- negation flips (vs. reference): —
- unsupported numbers: 2
- missing information: {"symptom": ["crackles", "falls", "rhonchi", "wheezing"], "diagnosis": ["osteoarthritis"]}

## Negation error example: `aci_bench_test_taskB_1_D2N127-aci`

*negation error example*

ROUGE-L 26.2 · length ratio 0.68 · truncated False · degenerate False · hallucination 16.7 · negation-flip 16.7 · numerical consistency 72.7 · coverage 80.0

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

Patient presents with complaints of neck pain following a series of motor vehicle accidents (MVAs).

**HISTORY OF PRESENT ILLNESS**

The patient reports experiencing neck pain since the most recent MVA in February of this year. He mentions having undergone surgery after another MVA and having attended therapy sessions for a few months following a second MVA. The patient expresses frustration regarding the frequency of his MVAs and acknowledges receiving advice from various professionals, including a therapist and a lawyer.

**REVIEW OF SYSTEMS**

*   Pain Scale: 12/10 (sharp, incapacitating)
*   Headaches: Present
*   Dizziness: Occasional
*   Visual Disturbances: None
*   Numbness: Present in the left arm and right leg
*   Spasms: Present throughout the body

**PHYSICAL EXAMINATION**

*   Palpation of the neck reveals pain on both the bony process and muscle.
*   Range of motion is limited due to pain; the patient cannot fully bend the neck forward or backward.
*   No visible bruising, swelling, or lacerations are observed.

**RESULTS**

*   Imaging Results: An  …
```

- unsupported entities (vs. transcript): clinical score, diagnostic workup, mri
- incorrect diagnosis: —  ·  missing diagnosis: —
- incorrect medication: —  ·  missing medication: fentanyl
- dosage mismatch: —
- negation flips (vs. reference): bruising, edema
- unsupported numbers: 12/10, 3, 5
- missing information: {"symptom": ["back pain", "fatigue", "stiffness"], "medication": ["fentanyl"]}

## Numerical error example: `aci_bench_test_taskB_1_D2N118-aci`

*numerical error example*

ROUGE-L 25.2 · length ratio 1.22 · truncated False · degenerate False · hallucination 14.3 · negation-flip 8.3 · numerical consistency 68.4 · coverage 66.7

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
**CHIEF COMPLAINT**

Patient Angela presented with complaints of suspected kidney stones, hypertension, and diabetes management.

**HISTORY OF PRESENT ILLNESS**

The patient reported experiencing intermittent pain related to suspected kidney stones, which she believed had passed approximately three days prior to her visit. She denied current pain and bleeding in her urine. The patient mentioned a history of recurrent kidney stones (approximately 7-8 episodes) and previous treatment at an emergency department with pain medication (percocet). 

She also discussed her past medical history of hypertension and diabetes mellitus type 2, currently managed with norvasc (amlodipine) 2.5 mg/day and metformin 500 mg/day, respectively. Her blood pressure was noted to be elevated at 150/90 mmHg during the visit, although she reported normal readings at home (130-140/60-70 mmHg).

Regarding dietary habits, the patient acknowledged consuming excessive amounts of fast food and sweets, which may contribute to her hypertension and diabetes management challenges.

**REVIEW OF SYSTEMS**

The patient den …
```

- unsupported entities (vs. transcript): bleeding, diagnostic workup, dyspnea
- incorrect diagnosis: —  ·  missing diagnosis: —
- incorrect medication: —  ·  missing medication: —
- dosage mismatch: —
- negation flips (vs. reference): pain
- unsupported numbers: 130, 140, 140/60, 180, 180/90, 2300
- missing information: {"symptom": ["hematuria", "rhonchi", "wheezing"], "diagnosis": ["stroke"], "investigation": ["continuous glucose monitor", "hemoglobin a1c", "urinalysis", "urine culture"]}

## Missing information example: `aci_bench_test_taskB_1_D2N105-virtscribe`

*missing information example*

ROUGE-L 24.8 · length ratio 0.47 · truncated False · degenerate False · hallucination 11.1 · negation-flip 0.0 · numerical consistency 77.8 · coverage 53.3

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

Patient Diana Scott presents with a chief complaint of a newly diagnosed heart murmur.

**HISTORY OF PRESENT ILLNESS**

The patient is a 100-year-old female who reports being told by her previous physician that she has a "new worrisome heart murmur." She denies any symptoms of chest pain, shortness of breath, or palpitations. However, she reports experiencing severe leg pain for approximately one month, which prompted her previous physician to order a chest X-ray. The patient has been taking pain medication for her leg pain. She also experiences shortness of breath with activities such as walking too fast or too long, or drinking a full glass of water without stopping. Her symptoms have worsened over the past six months, with a 70-80% increase in severity compared to six months prior.

**REVIEW OF SYSTEMS**

* Cardiovascular: Reports a 4/6 systolic murmur at the right upper sternal border with mild radiation to the carotids.
* Neurological: Gait is normal for age.
* Musculoskeletal: Severe leg pain for approximately one month.
* Respiratory: Shortness of breath w …
```

- unsupported entities (vs. transcript): hyperlipidemia, hypertension
- incorrect diagnosis: —  ·  missing diagnosis: arrhythmia, hypothyroidism, valvular heart disease
- incorrect medication: —  ·  missing medication: —
- dosage mismatch: —
- negation flips (vs. reference): —
- unsupported numbers: 2, 5
- missing information: {"symptom": ["chills", "edema", "fatigue", "fever", "syncope", "tachycardia"], "medical_history": ["allergic rhinitis", "coronary artery disease", "hypothyroidism"], "diagnosis": ["arrhythmia", "valvular heart disease"], "investigation": ["electrocardiogram", "holter monitor", "weight measurement"]}

# Split: aci_bench_test_taskC_2

## Best ROUGE-L: `aci_bench_test_taskC_2_D2N143-virtscribe`

*highest ROUGE-L in the split*

ROUGE-L 43.6 · length ratio 0.69 · truncated False · degenerate False · hallucination 11.1 · negation-flip 0.0 · numerical consistency 50.0 · coverage 88.9

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
**CHIEF COMPLAINT**

Patient presents for full-spectrum STD testing due to concerns about potential exposure after learning her partner has been engaging in extramarital activities.

**HISTORY OF PRESENT ILLNESS**

The patient is a 25-year-old female who reports experiencing symptoms of discomfort, a change in discharge, and odor in her vaginal region over the past week. She notes that the right side of her vagina has become painful. The patient denies any fever or chills. She recently discovered that her partner has been unfaithful for approximately three months.

**REVIEW OF SYSTEMS**

No systemic symptoms reported by the patient.

**PHYSICAL EXAM**

Pelvic exam demonstrates:

* No external lesions
* Normal labia majora and labia minora
* Normal physiological discharge with normal color and smell
* Cervix is normal
* Vaginal wall is normal
* No cervical motion tenderness
* No adnexal tenderness or masses noted

**RESULTS**

STD testing swabs were obtained for gonorrhea, chlamydia, trichomoniasis. Blood samples were collected for syphilis, HIV, and Hepatitis C testing.

**ASSESSMENT …
```

- unsupported entities (vs. transcript): blood work
- incorrect diagnosis: —  ·  missing diagnosis: —
- incorrect medication: —  ·  missing medication: —
- dosage mismatch: —
- negation flips (vs. reference): —
- unsupported numbers: 25
- missing information: {"symptom": ["vaginal discharge"]}

## Worst ROUGE-L: `aci_bench_test_taskC_2_D2N138-virtscribe`

*lowest ROUGE-L in the split*

ROUGE-L 19.5 · length ratio 0.35 · truncated False · degenerate False · hallucination 10.0 · negation-flip 0.0 · numerical consistency 100.0 · coverage 50.0

**Transcript (excerpt)**

```
[doctor] next patient is emily hernandez . date of birth , march 26 2001 . this is a 20 year old female being seen today for our yearly follow-up for asthma , allergic rhinitis and food allergy . due to insurance changes since our last office appointment in april 2020 , she was switched from symbicort to wixela . she also uses zyrtec in the spring , summer and fall for her seasonal allergy symptoms , which tend to work well . she also has known peanut allergy , she does tolerate almonds and cashews . please put in the asthma section at the very bottom that the act score is 21 . please put under interval history , written consent is obtained today to use dax for documentation .
[doctor] hi em …
```

**Reference note**

```
CHIEF COMPLAINT

Follow-up for asthma, allergic rhinitis, and food allergy.

HISTORY OF PRESENT ILLNESS

Emily Hernandez is a 20-year-old female presenting today for an annual follow-up for asthma, allergic rhinitis, and food allergy. Due to insurance changes during the interim of our last office appointment from 04/2020, she was switched from Symbicort to Wixela. She uses Zyrtec in the spring, summer, and fall for her seasonal allergy symptoms, which tends to work well. She has known peanut and tree nut allergies, which she tries to avoid. She does tolerate almonds and cashew.

Mrs. Hernandez is trying to join the military, who require a certain fitness level without use of a rescue or maintenance inhaler, so she has been weaning off her inhalers. She uses albuterol prior to a run, but otherwise functions without it. She has been reducing her Wixela dose, using 1 inhalation once daily 3 …
```

**Generated note**

```
**CHIEF COMPLAINT**

The patient, Emily Hernandez, presented for a yearly follow-up for asthma, allergic rhinitis, and food allergy.

**HISTORY OF PRESENT ILLNESS**

Emily is a 20-year-old female who has been doing well with her current treatment regimen. She was switched from Symbicort to Wixela due to insurance changes. She reports that Wixela is working well for her asthma, and she takes it once in the morning and once at night. She uses her albuterol inhaler rarely, mainly before strenuous activities. She has been trying to reduce her inhaler usage to meet the requirements for joining the military. Her average weekly usage of Wixela is three to four days per week.

**REVIEW OF SYSTEMS**

No urgent care or ER visits for breathing issues in the past year. No hospitalizations or surgeries related to her asthma.

**PHYSICAL EXAM**

The physical exam revealed normal findings, including clear lungs and a normal heart rate.

**RESULTS**

Breathing test results showed improvement compared to previous results in 2019, likely due to reduced exposure to smoke.

**INTERVAL HISTORY**

Written …
```

- unsupported entities (vs. transcript): heart rate measurement
- incorrect diagnosis: —  ·  missing diagnosis: —
- incorrect medication: —  ·  missing medication: prednisone
- dosage mismatch: —
- negation flips (vs. reference): —
- unsupported numbers: —
- missing information: {"symptom": ["falls", "laceration", "rash", "seizure"], "medical_history": ["montelukast"], "diagnosis": ["upper respiratory infection"], "medication": ["prednisone"], "investigation": ["sodium level"]}

## Hallucination example: `aci_bench_test_taskC_2_D2N135-virtassist`

*hallucination example*

ROUGE-L 27.7 · length ratio 0.65 · truncated False · degenerate False · hallucination 23.3 · negation-flip 5.9 · numerical consistency 45.5 · coverage 85.2

**Transcript (excerpt)**

```
[patient] um , i have high blood sugar . yeah , osteoarthritis , arterial fibrillation , and reflux .
[doctor] hi , hannah . how are you ?
[patient] good , how are you ?
[doctor] i'm good . you ready to get started ?
[patient] yes , i am .
[doctor] so , hannah is a , uh , 52-year-old female here for evaluation of a high blood sugar . so , hannah , what ha- what happened ? i heard you were in the emergency room with a high blood sugar .
[patient] yes . so , i've been eating a ton of sweets recently . with the holidays it just feels like there is always something sweet available. whether i am at work and there are holiday gift baskets or clients bringing in treats or when i visit my family for …
```

**Reference note**

```
CHIEF COMPLAINT

Evaluation of high blood sugar.

HISTORY OF PRESENT ILLNESS

Ms. Hannah Phillips is a 52-year-old female who presents for evaluation of high blood sugar. The patient admits to dietary indiscretion. She notes that she has been eating more sweets during the holidays. She reports that this past week, she felt really lightheaded, was seeing spots in her vision, and was really dizzy. She went to the emergency room and was told that she had high blood sugar. Ms. Phillips was given IV fluids. The patient was also instructed to get into a routine and watch her diet. She states that she is staying with family during the holidays and having trouble returning to her routine diet, but wants to make sure that her high blood sugar is not an issue.

The patient denies any fever or chills. She denies chest pain or shortness of breath. She denies abdominal pain or burning when she urinat …
```

**Generated note**

```
**CHIEF COMPLAINT**

Patient presents with complaint of high blood sugar, recent episode of lightheadedness, and visual disturbances.

**HISTORY OF PRESENT ILLNESS**

The patient is a 52-year-old female who reports experiencing symptoms of hyperglycemia, including lightheadedness and visual disturbances, following a period of consuming excessive sweets during the holiday season. She denies any fever, chills, chest pain, shortness of breath, abdominal pain, burning sensation while urinating, or joint/muscle aches. However, she does have a history of osteoarthritis, which may contribute to her reported joint pain. The patient has also experienced episodes of anxiety-related palpitations due to her atrial fibrillation (a-fib) diagnosis. Her gastroesophageal reflux disease (GERD) has been well-managed with protonix, 40 mg daily.

**REVIEW OF SYSTEMS**

* General: Denies fever, chills, or weight loss.
* Cardiovascular: Reports anxiety-related palpitations; diagnosed with atrial fibrillation.
* Respiratory: No respiratory complaints.
* Gastrointestinal: Well-managed GERD with protonix, 40  …
```

- unsupported entities (vs. transcript): anxiety, diagnostic workup, gerd, headache, heart rate measurement, vital signs, weight loss
- incorrect diagnosis: anxiety, gerd  ·  missing diagnosis: —
- incorrect medication: —  ·  missing medication: iv fluids
- dosage mismatch: —
- negation flips (vs. reference): joint pain
- unsupported numbers: 1, 3, 4, 5, 6, 7
- missing information: {"symptom": ["anxiety symptoms", "dysuria", "heartburn"], "medication": ["iv fluids"]}

## Incorrect diagnosis example: `aci_bench_test_taskC_2_D2N135-virtassist`

*incorrect diagnosis example*

ROUGE-L 27.7 · length ratio 0.65 · truncated False · degenerate False · hallucination 23.3 · negation-flip 5.9 · numerical consistency 45.5 · coverage 85.2

**Transcript (excerpt)**

```
[patient] um , i have high blood sugar . yeah , osteoarthritis , arterial fibrillation , and reflux .
[doctor] hi , hannah . how are you ?
[patient] good , how are you ?
[doctor] i'm good . you ready to get started ?
[patient] yes , i am .
[doctor] so , hannah is a , uh , 52-year-old female here for evaluation of a high blood sugar . so , hannah , what ha- what happened ? i heard you were in the emergency room with a high blood sugar .
[patient] yes . so , i've been eating a ton of sweets recently . with the holidays it just feels like there is always something sweet available. whether i am at work and there are holiday gift baskets or clients bringing in treats or when i visit my family for …
```

**Reference note**

```
CHIEF COMPLAINT

Evaluation of high blood sugar.

HISTORY OF PRESENT ILLNESS

Ms. Hannah Phillips is a 52-year-old female who presents for evaluation of high blood sugar. The patient admits to dietary indiscretion. She notes that she has been eating more sweets during the holidays. She reports that this past week, she felt really lightheaded, was seeing spots in her vision, and was really dizzy. She went to the emergency room and was told that she had high blood sugar. Ms. Phillips was given IV fluids. The patient was also instructed to get into a routine and watch her diet. She states that she is staying with family during the holidays and having trouble returning to her routine diet, but wants to make sure that her high blood sugar is not an issue.

The patient denies any fever or chills. She denies chest pain or shortness of breath. She denies abdominal pain or burning when she urinat …
```

**Generated note**

```
**CHIEF COMPLAINT**

Patient presents with complaint of high blood sugar, recent episode of lightheadedness, and visual disturbances.

**HISTORY OF PRESENT ILLNESS**

The patient is a 52-year-old female who reports experiencing symptoms of hyperglycemia, including lightheadedness and visual disturbances, following a period of consuming excessive sweets during the holiday season. She denies any fever, chills, chest pain, shortness of breath, abdominal pain, burning sensation while urinating, or joint/muscle aches. However, she does have a history of osteoarthritis, which may contribute to her reported joint pain. The patient has also experienced episodes of anxiety-related palpitations due to her atrial fibrillation (a-fib) diagnosis. Her gastroesophageal reflux disease (GERD) has been well-managed with protonix, 40 mg daily.

**REVIEW OF SYSTEMS**

* General: Denies fever, chills, or weight loss.
* Cardiovascular: Reports anxiety-related palpitations; diagnosed with atrial fibrillation.
* Respiratory: No respiratory complaints.
* Gastrointestinal: Well-managed GERD with protonix, 40  …
```

- unsupported entities (vs. transcript): anxiety, diagnostic workup, gerd, headache, heart rate measurement, vital signs, weight loss
- incorrect diagnosis: anxiety, gerd  ·  missing diagnosis: —
- incorrect medication: —  ·  missing medication: iv fluids
- dosage mismatch: —
- negation flips (vs. reference): joint pain
- unsupported numbers: 1, 3, 4, 5, 6, 7
- missing information: {"symptom": ["anxiety symptoms", "dysuria", "heartburn"], "medication": ["iv fluids"]}

## Incorrect medication / dosage example: `aci_bench_test_taskC_2_D2N149-aci`

*incorrect medication / dosage example*

ROUGE-L 28.5 · length ratio 1.09 · truncated False · degenerate False · hallucination 13.0 · negation-flip 21.4 · numerical consistency 83.3 · coverage 81.5

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

The patient, Dennis, presents with shortness of breath, which has been ongoing for approximately two weeks. He also reports coughing up blood, which has been occurring for about three weeks.

**HISTORY OF PRESENT ILLNESS**

Dennis is a 57-year-old male with a history of diabetes, hypertension, and asthma. He describes waking up with shortness of breath, which persists throughout the day. He has been experiencing this symptom for approximately two weeks. Additionally, he reports coughing up blood, which has been ongoing for about three weeks. The amount of blood coughed up is significant, with the patient stating he spits up "three to four cups" per day.

**REVIEW OF SYSTEMS**

* Respiratory system: Patient reports shortness of breath, coughing up blood, and decreased breath sounds on the right side.
* Cardiovascular system: Patient has a history of hypertension and is currently taking Norvasc. His current blood pressure reading is 120/70 mmHg.
* Endocrine system: Patient has a history of diabetes and is currently taking Metformin. His current blood glucose levels …
```

- unsupported entities (vs. transcript): diagnostic workup, knee pain, pulmonary embolism
- incorrect diagnosis: —  ·  missing diagnosis: —
- incorrect medication: —  ·  missing medication: —
- dosage mismatch: [{"drug": "metformin", "predicted": "500 mg", "source": ["750 mg"]}]
- negation flips (vs. reference): murmur, pain, pneumonia
- unsupported numbers: 150, 75
- missing information: {"symptom": ["bleeding", "crackles", "fever", "wheezing"], "investigation": ["heart rate measurement"]}

## Negation error example: `aci_bench_test_taskC_2_D2N149-aci`

*negation error example*

ROUGE-L 28.5 · length ratio 1.09 · truncated False · degenerate False · hallucination 13.0 · negation-flip 21.4 · numerical consistency 83.3 · coverage 81.5

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

The patient, Dennis, presents with shortness of breath, which has been ongoing for approximately two weeks. He also reports coughing up blood, which has been occurring for about three weeks.

**HISTORY OF PRESENT ILLNESS**

Dennis is a 57-year-old male with a history of diabetes, hypertension, and asthma. He describes waking up with shortness of breath, which persists throughout the day. He has been experiencing this symptom for approximately two weeks. Additionally, he reports coughing up blood, which has been ongoing for about three weeks. The amount of blood coughed up is significant, with the patient stating he spits up "three to four cups" per day.

**REVIEW OF SYSTEMS**

* Respiratory system: Patient reports shortness of breath, coughing up blood, and decreased breath sounds on the right side.
* Cardiovascular system: Patient has a history of hypertension and is currently taking Norvasc. His current blood pressure reading is 120/70 mmHg.
* Endocrine system: Patient has a history of diabetes and is currently taking Metformin. His current blood glucose levels …
```

- unsupported entities (vs. transcript): diagnostic workup, knee pain, pulmonary embolism
- incorrect diagnosis: —  ·  missing diagnosis: —
- incorrect medication: —  ·  missing medication: —
- dosage mismatch: [{"drug": "metformin", "predicted": "500 mg", "source": ["750 mg"]}]
- negation flips (vs. reference): murmur, pain, pneumonia
- unsupported numbers: 150, 75
- missing information: {"symptom": ["bleeding", "crackles", "fever", "wheezing"], "investigation": ["heart rate measurement"]}

## Numerical error example: `aci_bench_test_taskC_2_D2N135-virtassist`

*numerical error example*

ROUGE-L 27.7 · length ratio 0.65 · truncated False · degenerate False · hallucination 23.3 · negation-flip 5.9 · numerical consistency 45.5 · coverage 85.2

**Transcript (excerpt)**

```
[patient] um , i have high blood sugar . yeah , osteoarthritis , arterial fibrillation , and reflux .
[doctor] hi , hannah . how are you ?
[patient] good , how are you ?
[doctor] i'm good . you ready to get started ?
[patient] yes , i am .
[doctor] so , hannah is a , uh , 52-year-old female here for evaluation of a high blood sugar . so , hannah , what ha- what happened ? i heard you were in the emergency room with a high blood sugar .
[patient] yes . so , i've been eating a ton of sweets recently . with the holidays it just feels like there is always something sweet available. whether i am at work and there are holiday gift baskets or clients bringing in treats or when i visit my family for …
```

**Reference note**

```
CHIEF COMPLAINT

Evaluation of high blood sugar.

HISTORY OF PRESENT ILLNESS

Ms. Hannah Phillips is a 52-year-old female who presents for evaluation of high blood sugar. The patient admits to dietary indiscretion. She notes that she has been eating more sweets during the holidays. She reports that this past week, she felt really lightheaded, was seeing spots in her vision, and was really dizzy. She went to the emergency room and was told that she had high blood sugar. Ms. Phillips was given IV fluids. The patient was also instructed to get into a routine and watch her diet. She states that she is staying with family during the holidays and having trouble returning to her routine diet, but wants to make sure that her high blood sugar is not an issue.

The patient denies any fever or chills. She denies chest pain or shortness of breath. She denies abdominal pain or burning when she urinat …
```

**Generated note**

```
**CHIEF COMPLAINT**

Patient presents with complaint of high blood sugar, recent episode of lightheadedness, and visual disturbances.

**HISTORY OF PRESENT ILLNESS**

The patient is a 52-year-old female who reports experiencing symptoms of hyperglycemia, including lightheadedness and visual disturbances, following a period of consuming excessive sweets during the holiday season. She denies any fever, chills, chest pain, shortness of breath, abdominal pain, burning sensation while urinating, or joint/muscle aches. However, she does have a history of osteoarthritis, which may contribute to her reported joint pain. The patient has also experienced episodes of anxiety-related palpitations due to her atrial fibrillation (a-fib) diagnosis. Her gastroesophageal reflux disease (GERD) has been well-managed with protonix, 40 mg daily.

**REVIEW OF SYSTEMS**

* General: Denies fever, chills, or weight loss.
* Cardiovascular: Reports anxiety-related palpitations; diagnosed with atrial fibrillation.
* Respiratory: No respiratory complaints.
* Gastrointestinal: Well-managed GERD with protonix, 40  …
```

- unsupported entities (vs. transcript): anxiety, diagnostic workup, gerd, headache, heart rate measurement, vital signs, weight loss
- incorrect diagnosis: anxiety, gerd  ·  missing diagnosis: —
- incorrect medication: —  ·  missing medication: iv fluids
- dosage mismatch: —
- negation flips (vs. reference): joint pain
- unsupported numbers: 1, 3, 4, 5, 6, 7
- missing information: {"symptom": ["anxiety symptoms", "dysuria", "heartburn"], "medication": ["iv fluids"]}

## Missing information example: `aci_bench_test_taskC_2_D2N138-virtscribe`

*missing information example*

ROUGE-L 19.5 · length ratio 0.35 · truncated False · degenerate False · hallucination 10.0 · negation-flip 0.0 · numerical consistency 100.0 · coverage 50.0

**Transcript (excerpt)**

```
[doctor] next patient is emily hernandez . date of birth , march 26 2001 . this is a 20 year old female being seen today for our yearly follow-up for asthma , allergic rhinitis and food allergy . due to insurance changes since our last office appointment in april 2020 , she was switched from symbicort to wixela . she also uses zyrtec in the spring , summer and fall for her seasonal allergy symptoms , which tend to work well . she also has known peanut allergy , she does tolerate almonds and cashews . please put in the asthma section at the very bottom that the act score is 21 . please put under interval history , written consent is obtained today to use dax for documentation .
[doctor] hi em …
```

**Reference note**

```
CHIEF COMPLAINT

Follow-up for asthma, allergic rhinitis, and food allergy.

HISTORY OF PRESENT ILLNESS

Emily Hernandez is a 20-year-old female presenting today for an annual follow-up for asthma, allergic rhinitis, and food allergy. Due to insurance changes during the interim of our last office appointment from 04/2020, she was switched from Symbicort to Wixela. She uses Zyrtec in the spring, summer, and fall for her seasonal allergy symptoms, which tends to work well. She has known peanut and tree nut allergies, which she tries to avoid. She does tolerate almonds and cashew.

Mrs. Hernandez is trying to join the military, who require a certain fitness level without use of a rescue or maintenance inhaler, so she has been weaning off her inhalers. She uses albuterol prior to a run, but otherwise functions without it. She has been reducing her Wixela dose, using 1 inhalation once daily 3 …
```

**Generated note**

```
**CHIEF COMPLAINT**

The patient, Emily Hernandez, presented for a yearly follow-up for asthma, allergic rhinitis, and food allergy.

**HISTORY OF PRESENT ILLNESS**

Emily is a 20-year-old female who has been doing well with her current treatment regimen. She was switched from Symbicort to Wixela due to insurance changes. She reports that Wixela is working well for her asthma, and she takes it once in the morning and once at night. She uses her albuterol inhaler rarely, mainly before strenuous activities. She has been trying to reduce her inhaler usage to meet the requirements for joining the military. Her average weekly usage of Wixela is three to four days per week.

**REVIEW OF SYSTEMS**

No urgent care or ER visits for breathing issues in the past year. No hospitalizations or surgeries related to her asthma.

**PHYSICAL EXAM**

The physical exam revealed normal findings, including clear lungs and a normal heart rate.

**RESULTS**

Breathing test results showed improvement compared to previous results in 2019, likely due to reduced exposure to smoke.

**INTERVAL HISTORY**

Written …
```

- unsupported entities (vs. transcript): heart rate measurement
- incorrect diagnosis: —  ·  missing diagnosis: —
- incorrect medication: —  ·  missing medication: prednisone
- dosage mismatch: —
- negation flips (vs. reference): —
- unsupported numbers: —
- missing information: {"symptom": ["falls", "laceration", "rash", "seizure"], "medical_history": ["montelukast"], "diagnosis": ["upper respiratory infection"], "medication": ["prednisone"], "investigation": ["sodium level"]}

# Split: aci_bench_test_taskC_3

## Best ROUGE-L: `aci_bench_test_taskC_3_D2N187-aci`

*highest ROUGE-L in the split*

ROUGE-L 47.2 · length ratio 1.20 · truncated False · degenerate False · hallucination 25.0 · negation-flip 0.0 · numerical consistency 100.0 · coverage 80.0

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

**HISTORY OF PRESENT ILLNESS**

The patient reports experiencing sudden visual distortions and blurring of vision. She mentions that straight lines appear crooked to her, including door frames. Additionally, she experiences difficulty adjusting to dim lighting environments, such as restaurants. The patient notes that these symptoms have been occurring intermittently.

**REVIEW OF SYSTEMS**

The patient reports smoking a pack of cigarettes daily and has attempted to quit but has not been successful. She also mentions taking her blood pressure readings sporadically.

**PHYSICAL EXAM**

Anterior segment examination revealed posterior chamber intraocular lenses in both eyes. In the right eye, the cornea is clear, and there were no signs of macular edema (MVI). Cup-to-disc ratio is 2. Fundus examination showed the retina to be attached 360 degrees without any tears or holes. Posterior segment exam revealed drusen in the macula, thickening of the retina, presence of subretinal fluid, and exudates  …
```

- unsupported entities (vs. transcript): edema, physical examination
- incorrect diagnosis: —  ·  missing diagnosis: —
- incorrect medication: —  ·  missing medication: —
- dosage mismatch: —
- negation flips (vs. reference): —
- unsupported numbers: —
- missing information: {"symptom": ["blurred vision"]}

## Worst ROUGE-L: `aci_bench_test_taskC_3_D2N185-virtscribe`

*lowest ROUGE-L in the split*

ROUGE-L 21.2 · length ratio 0.50 · truncated False · degenerate False · hallucination 37.5 · negation-flip 9.1 · numerical consistency 75.0 · coverage 56.7

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

Ashley James, a 14-year-old female, presents with complaints of abdominal pain, nausea, vomiting, and urinary frequency.

**HISTORY OF PRESENT ILLNESS**

The patient was previously healthy until she presented with symptoms of abdominal pain, nausea, and vomiting. An initial diagnosis of appendicitis was considered, but subsequent ultrasounds revealed an atrophic right kidney. The patient underwent further evaluations, including ultrasounds, urine analysis, and imaging studies, which showed cysts on the kidney and ovaries, as well as evidence of infection. She was treated with antibiotics and fluids, resulting in some improvement of symptoms.

**REVIEW OF SYSTEMS**

The patient reports experiencing abdominal pain, particularly on the right side, which worsens after eating and drinking certain beverages. She also experiences urinary frequency and burning sensations while urinating. Her mother reports that the patient has a history of recurrent infections and fevers starting at age 4, which resolved without treatment.

**PHYSICAL EXAM**

The patient appears well-nou …
```

- unsupported entities (vs. transcript): abdominal pain, appendicitis, diagnostic workup, hematuria, imaging, nausea, urinary frequency, urinary tract infection, vital signs
- incorrect diagnosis: appendicitis, urinary tract infection  ·  missing diagnosis: dehydration, hypertension
- incorrect medication: —  ·  missing medication: famotidine, loratadine
- dosage mismatch: —
- negation flips (vs. reference): proteinuria
- unsupported numbers: 6, 7
- missing information: {"symptom": ["dysuria", "edema", "pain"], "medical_history": ["allergic rhinitis", "hypertension", "myocardial infarction", "neuropathy", "type 2 diabetes"], "diagnosis": ["dehydration"], "medication": ["famotidine", "loratadine"], "investigation": ["creatinine", "ct scan"]}

## Hallucination example: `aci_bench_test_taskC_3_D2N185-virtscribe`

*hallucination example*

ROUGE-L 21.2 · length ratio 0.50 · truncated False · degenerate False · hallucination 37.5 · negation-flip 9.1 · numerical consistency 75.0 · coverage 56.7

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

Ashley James, a 14-year-old female, presents with complaints of abdominal pain, nausea, vomiting, and urinary frequency.

**HISTORY OF PRESENT ILLNESS**

The patient was previously healthy until she presented with symptoms of abdominal pain, nausea, and vomiting. An initial diagnosis of appendicitis was considered, but subsequent ultrasounds revealed an atrophic right kidney. The patient underwent further evaluations, including ultrasounds, urine analysis, and imaging studies, which showed cysts on the kidney and ovaries, as well as evidence of infection. She was treated with antibiotics and fluids, resulting in some improvement of symptoms.

**REVIEW OF SYSTEMS**

The patient reports experiencing abdominal pain, particularly on the right side, which worsens after eating and drinking certain beverages. She also experiences urinary frequency and burning sensations while urinating. Her mother reports that the patient has a history of recurrent infections and fevers starting at age 4, which resolved without treatment.

**PHYSICAL EXAM**

The patient appears well-nou …
```

- unsupported entities (vs. transcript): abdominal pain, appendicitis, diagnostic workup, hematuria, imaging, nausea, urinary frequency, urinary tract infection, vital signs
- incorrect diagnosis: appendicitis, urinary tract infection  ·  missing diagnosis: dehydration, hypertension
- incorrect medication: —  ·  missing medication: famotidine, loratadine
- dosage mismatch: —
- negation flips (vs. reference): proteinuria
- unsupported numbers: 6, 7
- missing information: {"symptom": ["dysuria", "edema", "pain"], "medical_history": ["allergic rhinitis", "hypertension", "myocardial infarction", "neuropathy", "type 2 diabetes"], "diagnosis": ["dehydration"], "medication": ["famotidine", "loratadine"], "investigation": ["creatinine", "ct scan"]}

## Incorrect diagnosis example: `aci_bench_test_taskC_3_D2N185-virtscribe`

*incorrect diagnosis example*

ROUGE-L 21.2 · length ratio 0.50 · truncated False · degenerate False · hallucination 37.5 · negation-flip 9.1 · numerical consistency 75.0 · coverage 56.7

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

Ashley James, a 14-year-old female, presents with complaints of abdominal pain, nausea, vomiting, and urinary frequency.

**HISTORY OF PRESENT ILLNESS**

The patient was previously healthy until she presented with symptoms of abdominal pain, nausea, and vomiting. An initial diagnosis of appendicitis was considered, but subsequent ultrasounds revealed an atrophic right kidney. The patient underwent further evaluations, including ultrasounds, urine analysis, and imaging studies, which showed cysts on the kidney and ovaries, as well as evidence of infection. She was treated with antibiotics and fluids, resulting in some improvement of symptoms.

**REVIEW OF SYSTEMS**

The patient reports experiencing abdominal pain, particularly on the right side, which worsens after eating and drinking certain beverages. She also experiences urinary frequency and burning sensations while urinating. Her mother reports that the patient has a history of recurrent infections and fevers starting at age 4, which resolved without treatment.

**PHYSICAL EXAM**

The patient appears well-nou …
```

- unsupported entities (vs. transcript): abdominal pain, appendicitis, diagnostic workup, hematuria, imaging, nausea, urinary frequency, urinary tract infection, vital signs
- incorrect diagnosis: appendicitis, urinary tract infection  ·  missing diagnosis: dehydration, hypertension
- incorrect medication: —  ·  missing medication: famotidine, loratadine
- dosage mismatch: —
- negation flips (vs. reference): proteinuria
- unsupported numbers: 6, 7
- missing information: {"symptom": ["dysuria", "edema", "pain"], "medical_history": ["allergic rhinitis", "hypertension", "myocardial infarction", "neuropathy", "type 2 diabetes"], "diagnosis": ["dehydration"], "medication": ["famotidine", "loratadine"], "investigation": ["creatinine", "ct scan"]}

## Incorrect medication / dosage example: `aci_bench_test_taskC_3_D2N195-aci`

*incorrect medication / dosage example*

ROUGE-L 30.5 · length ratio 0.67 · truncated False · degenerate False · hallucination 18.2 · negation-flip 0.0 · numerical consistency 100.0 · coverage 81.8

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
**CHIEF COMPLAINT**

Patient presents with right knee pain following a recent episode of playing basketball where he experienced a "pop" sensation in his knee, resulting in swelling and difficulty walking.

**HISTORY OF PRESENT ILLNESS**

The patient reports that he was playing basketball for the first time in two years when he experienced the injury. He describes the pain as "real achy" located on the inside of the knee. The swelling has decreased slightly after sleeping overnight. He took Tylenol the previous day, which provided minimal relief. His pain level is currently a 4 out of 10.

**REVIEW OF SYSTEMS**

The patient has a history of hypertension and diabetes. He takes Norvasc (5mg) daily for hypertension and Metformin (500mg) daily for diabetes, although he admits to occasionally skipping doses due to gastrointestinal side effects. His current blood pressure reading is 140/80 mmHg. He has not been regularly monitoring his blood glucose levels.

**PHYSICAL EXAM**

The patient's lung sounds are clear, and his heart examination reveals a previously known grade 2 systolic ejectio …
```

- unsupported entities (vs. transcript): adverse drug reaction, difficulty walking, mri, trauma
- incorrect diagnosis: adverse drug reaction  ·  missing diagnosis: acl tear
- incorrect medication: —  ·  missing medication: —
- dosage mismatch: [{"drug": "amlodipine", "predicted": "7.5 mg", "source": ["5 mg"]}]
- negation flips (vs. reference): —
- unsupported numbers: —
- missing information: {"symptom": ["erythema"], "diagnosis": ["acl tear", "dislocation"], "investigation": ["hemoglobin a1c"]}

## Negation error example: `aci_bench_test_taskC_3_D2N170-virtassist`

*negation error example*

ROUGE-L 30.1 · length ratio 0.59 · truncated False · degenerate False · hallucination 3.7 · negation-flip 23.5 · numerical consistency 100.0 · coverage 69.7

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

Joyce is a 50-year-old female with a past medical history significant for COPD (chronic obstructive pulmonary disease), congestive heart failure. She reports feeling tired and exhausted over the past couple of months, despite her usual daily activities including running and climbing. Her energy levels have decreased significantly, and she has noticed a decline in her ability to maintain her exercise routine. She denies noticing any blood in her stool, dark or charred stools, or spotting during her menstrual period. Additionally, she reports no other symptoms such as chest pain, shortness of breath, fever, chills, body aches, or weight loss.

**REVIEW OF SYSTEMS**

COPD: Joyce reports that her breathing has been "okay" with occasional difficulty during seasonal changes, which she attributes to allergies. She has not smoked since quitting several years ago.

Congestive Heart Failure: Joyce reports that she has been adherin …
```

- unsupported entities (vs. transcript): hypernatremia
- incorrect diagnosis: —  ·  missing diagnosis: gi bleed
- incorrect medication: —  ·  missing medication: —
- dosage mismatch: —
- negation flips (vs. reference): bleeding, chest pain, chills, fever
- unsupported numbers: —
- missing information: {"symptom": ["blood in stool", "crackles", "dizziness", "lymphadenopathy", "rhonchi", "wheezing"], "medical_history": ["tobacco use"], "diagnosis": ["gi bleed"], "investigation": ["hemoglobin a1c", "sodium level"]}

## Numerical error example: `aci_bench_test_taskC_3_D2N193-aci`

*numerical error example*

ROUGE-L 29.1 · length ratio 0.89 · truncated False · degenerate False · hallucination 9.4 · negation-flip 0.0 · numerical consistency 62.5 · coverage 90.0

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
**CHIEF COMPLAINT**

Patient presents with a 3-day history of a hacking cough, accompanied by green phlegm production, sore throat, and nasal congestion.

**HISTORY OF PRESENT ILLNESS**

The patient reports developing a cough 3 days prior to presentation, which began gradually and worsened over time. The cough is associated with the production of green phlegm. The patient also notes a sore throat and mild nasal congestion. She denies experiencing fever, shortness of breath, body aches, nausea, or vomiting. The patient's sister has been experiencing similar symptoms, suggesting possible viral transmission.

**REVIEW OF SYSTEMS**

* Respiratory system: Cough, green phlegm production, sore throat, and nasal congestion.
* Cardiovascular system: Elevated blood pressure (144/72 mmHg).
* Endocrine system: Type 2 diabetes, with HbA1c levels reportedly within target range (120-140 mg/dL).
* Gastrointestinal system: No diarrhea or gastrointestinal complaints.
* Neurological system: No neurological symptoms reported.

**PHYSICAL EXAMINATION**

* Vital signs: Blood pressure 144/72 mmHg, pulse 78 …
```

- unsupported entities (vs. transcript): diagnostic workup, heart rate measurement, respiratory rate
- incorrect diagnosis: —  ·  missing diagnosis: —
- incorrect medication: —  ·  missing medication: —
- dosage mismatch: —
- negation flips (vs. reference): —
- unsupported numbers: 120, 140, 18, 37, 78, 98.6
- missing information: {"symptom": ["urinary frequency"], "medical_history": ["allergic rhinitis"], "investigation": ["covid test"]}

## Missing information example: `aci_bench_test_taskC_3_D2N180-virtscribe`

*missing information example*

ROUGE-L 40.5 · length ratio 0.57 · truncated False · degenerate False · hallucination 12.5 · negation-flip 0.0 · numerical consistency 100.0 · coverage 53.6

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
**CHIEF COMPLAINT**

Patient Shirley Taylor, a 60-year-old right-handed female, presents with complaints of bilateral hand numbness and tingling.

**HISTORY OF PRESENT ILLNESS**

The patient reports experiencing numbness and tingling in both hands since a car accident in December, where she broke both wrists. The symptoms worsened over the past month despite wearing splints on both wrists. She describes the tingling as starting from the middle and ring fingers on the right hand and extending to the forearm, and on the left hand, primarily affecting the pinky and ring fingers. The patient experiences occasional pain, soreness, and throbbing in her hands, which resolves when the pain subsides. She notes decreased sensitivity in her hands but can still feel objects.

**REVIEW OF SYSTEMS**

Constitutional: Fatigue and weight gain.
GI: Excessive appetite and bloating.
Eyes: Floaters.
Cardiovascular: Shortness of breath and leg swelling.
Endocrine: Positive diabetes (previously controlled through dietary changes).
Skin: Nail bed trenches, dryness, itching.
Musculoskeletal: Gout, muscle pai …
```

- unsupported entities (vs. transcript): emg, trauma
- incorrect diagnosis: —  ·  missing diagnosis: —
- incorrect medication: —  ·  missing medication: carvedilol, escitalopram
- dosage mismatch: —
- negation flips (vs. reference): —
- unsupported numbers: —
- missing information: {"symptom": ["bruising", "rash", "stiffness"], "medical_history": ["chronic kidney disease", "gerd", "heartburn", "prediabetes"], "diagnosis": ["anxiety", "cancer", "hypertension"], "medication": ["carvedilol", "escitalopram"], "investigation": ["ct scan"]}

# Split: mts_dialog_test_chat_2023

## Best ROUGE-L: `mts_dialog_test_chat_2023_101`

*highest ROUGE-L in the split*

ROUGE-L 66.7 · length ratio 1.00 · truncated False · degenerate False · hallucination 0.0 · negation-flip 0.0 · numerical consistency — · coverage 100.0

**Transcript (excerpt)**

```
Doctor: Are you taking any medication? 
Patient: Just multivitamins and calcium.
```

**Reference note**

```
Multivitamins and calcium.
```

**Generated note**

```
MEDICATIONS:

- Multivitamins
- Calcium
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

ROUGE-L 0.0 · length ratio 9.57 · truncated False · degenerate False · hallucination 12.5 · negation-flip 0.0 · numerical consistency — · coverage 33.3

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

The patient reports no current symptoms such as dizziness, excessive urination, fatigue, weight loss, or others. The patient has been compliant with recording their blood glucose readings, which were provided for review. 

Current medical issues include elevated cholesterol levels, for which the patient will continue taking prescribed cholesterol medication and monitoring dietary cholesterol intake. 

Sinus symptoms have significantly improved since initiating treatment with the Z Pak.
```

- unsupported entities (vs. transcript): hyperlipidemia
- incorrect diagnosis: hyperlipidemia  ·  missing diagnosis: —
- incorrect medication: —  ·  missing medication: —
- dosage mismatch: —
- negation flips (vs. reference): —
- unsupported numbers: —
- missing information: {"diagnosis": ["diabetes", "sinusitis"]}

## Hallucination example: `mts_dialog_test_chat_2023_103`

*hallucination example*

ROUGE-L 19.7 · length ratio 0.80 · truncated False · degenerate False · hallucination 66.7 · negation-flip 0.0 · numerical consistency 100.0 · coverage 20.0

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
**HISTORY OF PRESENT ILLNESS**

The patient reports experiencing episodes of facial grimacing without apparent cause, which she describes as involuntary movements involving her face, mouth, and possibly other areas. These episodes occur approximately once per week and have decreased in frequency over time. 

She also experiences intermittent pressure sensations in the posterior aspect of her head, described as "pins and needles" with associated pressure and sometimes likened to running water. The frequency of these episodes is reported to be about once weekly.

Additionally, the patient complains of excessive daytime somnolence, noting difficulty staying awake during non-stimulating activities such as watching TV or sitting at her desk. She attributes this to inadequate nighttime sleep, despite attempting to obtain sufficient rest. Her typical sleep duration is approximately 5-6 hours per night, with an inconsistent sleep schedule due to her late-night work hours (4 pm - midnight). 

The patient denies significant disruptions in sleep quality, aside from occasional nocturia and possi …
```

- unsupported entities (vs. transcript): daytime sleepiness, dyspnea, nocturia, sleep apnea
- incorrect diagnosis: —  ·  missing diagnosis: —
- incorrect medication: —  ·  missing medication: naproxen
- dosage mismatch: —
- negation flips (vs. reference): —
- unsupported numbers: —
- missing information: {"symptom": ["falls", "insomnia", "tingling"], "medication": ["naproxen"]}

## Incorrect diagnosis example: `mts_dialog_test_chat_2023_108`

*incorrect diagnosis example*

ROUGE-L 7.0 · length ratio 6.12 · truncated False · degenerate False · hallucination 66.7 · negation-flip 0.0 · numerical consistency 100.0 · coverage 100.0

**Transcript (excerpt)**

```
Doctor: How's she doing today? 
Guest_family: She's been blowing up green snot and complaing of ear pain. 
Doctor: Both ears? 
Guest_family: Both the right and left. 
Doctor: How long has she been bringing up green snot? 
Guest_family: Maybe six or so days? 
Doctor: Let's see. It looks like she may have sinusitis. After checking both ears, I noticed fluid buildup in the right middle ear. I'll go ahead and prescribe her some antibiotics and hopefully she'll be as good as new in a few days. I'd like her to come back for a follow up to make sure all the fluid in her ear is gone.
```

**Reference note**

```
Ongoing purulent rhinitis.  Probable sinusitis and serous otitis.
```

**Generated note**

```
ASSESSMENT:

The patient presents with symptoms of bilateral ear pain and green nasal discharge for approximately six days. Physical examination reveals fluid buildup in the right middle ear. The primary concern appears to be otitis media (middle ear infection) with possible secondary involvement of upper respiratory tract infection (sinusitis).
```

- unsupported entities (vs. transcript): otitis media, physical examination, rhinorrhea, upper respiratory infection
- incorrect diagnosis: otitis media, upper respiratory infection  ·  missing diagnosis: —
- incorrect medication: —  ·  missing medication: —
- dosage mismatch: —
- negation flips (vs. reference): —
- unsupported numbers: —
- missing information: {}

## Negation error example: `mts_dialog_test_chat_2023_66`

*negation error example*

ROUGE-L 32.3 · length ratio 0.58 · truncated False · degenerate False · hallucination 5.6 · negation-flip 12.5 · numerical consistency — · coverage 53.1

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
REVIEW OF SYSTEMS:

* General: Stable weight; no fever, chills, or night sweats.
* Gastrointestinal: Recent episodes of diarrhea (resolved); history of bowel abnormalities and IBS.
* Endocrine: Hypothyroidism (pre-existing condition).
* Cardiovascular: No chest pain or discomfort; no palpitations or heart attacks.
* Respiratory: No shortness of breath, cough, or difficulty breathing.
* Genitourinary: No urinary problems or kidney issues; no abnormal vaginal bleeding or discharge.
* Neurological: No blackouts, convulsions, seizures, paralysis, strokes, or headaches.
* Hematological: Anemia (history of); current anemia labs normal.
* Musculoskeletal: None noted.
* Dermatologic: None noted.
* Allergic/Immunologic: None noted.
* Psychiatric: None noted.
```

- unsupported entities (vs. transcript): irritable bowel syndrome
- incorrect diagnosis: —  ·  missing diagnosis: —
- incorrect medication: —  ·  missing medication: —
- dosage mismatch: —
- negation flips (vs. reference): diarrhea, irritable bowel syndrome
- unsupported numbers: —
- missing information: {"symptom": ["blurred vision", "double vision", "dysuria", "hemoptysis", "orthopnea", "paroxysmal nocturnal dyspnea"], "medical_history": ["c. diff infection", "inflammatory bowel disease"], "diagnosis": ["infection", "kidney stones"], "investigation": ["blood glucose"]}

## Numerical error example: `mts_dialog_test_chat_2023_7`

*numerical error example*

ROUGE-L 37.6 · length ratio 1.15 · truncated False · degenerate False · hallucination — · negation-flip — · numerical consistency 77.8 · coverage 0.0

**Transcript (excerpt)**

```
Doctor: What is your family medical history? 
Patient: My parents do not have any health conditions. I have two half brothers that are in good health as well. 
Doctor: How old are your brothers? 
Patient: Twenty six and twenty eight. My grandmother on my mom's side had D V T in her leg. I think she was in her forty's.
Doctor: Any family history of diabetes? 
Patient: I think my aunt from my dad's side of the family and my cousins on my mom's side of the family are diabetic? Oh. My great grandfather had bone cancer.  He was in his eighties. My mom's brother was recently diagnosed with leukemia. He is around fifty years old. Then my dad's dad had colon cancer at seventy three. He had it since  …
```

**Reference note**

```
Two half-brothers, ages 26 and 28, both in good health.  Parents are in good health.  A maternal great-grandmother had a deep venous thrombosis (DVT) of leg in her 40s.  A maternal great-uncle developed leukemia around age 50.  A maternal great-grandfather had bone cancer around age 80.  His paternal grandfather died of colon cancer at age 73, which he had had since age 68.  Adult-onset diabetes is present in distant relatives on both sides.
```

**Generated note**

```
FAMILY HISTORY/SOCIAL HISTORY:

The patient reports a negative family history for parents and two half-brothers (ages 26 and 28) who are both healthy. 

Notable family medical history includes:

- Grandmother (maternal): Deep Vein Thrombosis (DVT) in her leg, likely in her 40s.
- Aunt (paternal): Diabetes
- Cousins (maternal): Diabetes
- Great-grandfather (paternal): Bone cancer, age unknown but deceased in his 80s.
- Uncle (maternal): Leukemia, approximately 50 years old.
- Grandfather (paternal): Colon cancer, diagnosed at age 73 with a duration of approximately 5 years starting at age 68.
```

- unsupported entities (vs. transcript): —
- incorrect diagnosis: —  ·  missing diagnosis: —
- incorrect medication: —  ·  missing medication: —
- dosage mismatch: —
- negation flips (vs. reference): —
- unsupported numbers: 5, 8
- missing information: {"diagnosis": ["diabetes"]}

## Missing information example: `mts_dialog_test_chat_2023_103`

*missing information example*

ROUGE-L 19.7 · length ratio 0.80 · truncated False · degenerate False · hallucination 66.7 · negation-flip 0.0 · numerical consistency 100.0 · coverage 20.0

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
**HISTORY OF PRESENT ILLNESS**

The patient reports experiencing episodes of facial grimacing without apparent cause, which she describes as involuntary movements involving her face, mouth, and possibly other areas. These episodes occur approximately once per week and have decreased in frequency over time. 

She also experiences intermittent pressure sensations in the posterior aspect of her head, described as "pins and needles" with associated pressure and sometimes likened to running water. The frequency of these episodes is reported to be about once weekly.

Additionally, the patient complains of excessive daytime somnolence, noting difficulty staying awake during non-stimulating activities such as watching TV or sitting at her desk. She attributes this to inadequate nighttime sleep, despite attempting to obtain sufficient rest. Her typical sleep duration is approximately 5-6 hours per night, with an inconsistent sleep schedule due to her late-night work hours (4 pm - midnight). 

The patient denies significant disruptions in sleep quality, aside from occasional nocturia and possi …
```

- unsupported entities (vs. transcript): daytime sleepiness, dyspnea, nocturia, sleep apnea
- incorrect diagnosis: —  ·  missing diagnosis: —
- incorrect medication: —  ·  missing medication: naproxen
- dosage mismatch: —
- negation flips (vs. reference): —
- unsupported numbers: —
- missing information: {"symptom": ["falls", "insomnia", "tingling"], "medication": ["naproxen"]}

# Split: mts_dialog_test_sum_2023

## Best ROUGE-L: `mts_dialog_test_sum_2023_130`

*highest ROUGE-L in the split*

ROUGE-L 70.6 · length ratio 1.12 · truncated False · degenerate False · hallucination 66.7 · negation-flip 0.0 · numerical consistency — · coverage 66.7

**Transcript (excerpt)**

```
Doctor: And is she allergic to any drugs? 
Guest_family: Well, actually, my mom is allergic to many medicines. I always carry a list. Here you can have a look.
Doctor: Oh, that's really smart and helpful. Let me have a look. I see, this is quite a list. She is allergic to sulfa drugs, Darvon, codeine, N A S A I D, amox and quinine.
Guest_family: Yes, all of the above. 
Doctor: Hm.
```

**Reference note**

```
Sulfa, aspirin, Darvon, codeine, NSAID, amoxicillin, and quinine.
```

**Generated note**

```
ALLERGIES:

- Sulfa drugs
- Darvon
- Codeine
- NSAIDs
- Amoxicillin (amox)
- Quinine
```

- unsupported entities (vs. transcript): amoxicillin, nsaid
- incorrect diagnosis: —  ·  missing diagnosis: —
- incorrect medication: —  ·  missing medication: amoxicillin, aspirin, codeine
- dosage mismatch: —
- negation flips (vs. reference): —
- unsupported numbers: —
- missing information: {"medication": ["aspirin"]}

## Worst ROUGE-L: `mts_dialog_test_sum_2023_150`

*lowest ROUGE-L in the split*

ROUGE-L 0.0 · length ratio 29.00 · truncated False · degenerate False · hallucination 50.0 · negation-flip — · numerical consistency — · coverage —

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

The patient reports being a non-smoker and non-drinker. The patient denies any family history of significant medical problems. This is the patient's first episode of back pain.
```

- unsupported entities (vs. transcript): tobacco use
- incorrect diagnosis: —  ·  missing diagnosis: —
- incorrect medication: —  ·  missing medication: —
- dosage mismatch: —
- negation flips (vs. reference): —
- unsupported numbers: —
- missing information: {}

## Hallucination example: `mts_dialog_test_sum_2023_112`

*hallucination example*

ROUGE-L 19.3 · length ratio 0.48 · truncated False · degenerate False · hallucination 25.0 · negation-flip 0.0 · numerical consistency 100.0 · coverage 50.0

**Transcript (excerpt)**

```
Doctor: Hello, miss. What brings you into our clinic today? Also, before we start, it looks like you forgot to fill out your ethnicity on the new patient paperwork. Do you mind telling me what you identify as?
 Patient: Hello, doctor. I am white and I am a young sixty two years old. I have a list of issues I would like to talk about. 
Doctor: Let's begin. I know that you have been dealing with hypertension and lipometabolism disorder. Doctor X Y Z and I follow you on the hypertension. What else do we have going on?
Patient: First off I have a history of diabetes in my family. My father had it and my brother has it currently. I am afraid because I know I have gained some weight. My knee also  …
```

**Reference note**

```
The patient is a 62-year-old white female with multiple chronic problems including hypertension and a lipometabolism disorder.  She follows with Dr. XYZ on her hypertension, as well as myself.  She continues to gain weight.  Diabetes is therefore a major concern.  In fact, her dad had diabetes and she has a brother who has diabetes.  The patient also has several additional concerns she brings up today.  One is that her left knee continues to bother her and it hurts.  She cannot really isolate where the pain is, it just seems to hurt through her knee.  She has had this for some time now and in fact as we reviewed her records, her left knee has been x-rayed in 1999.  There was some minimal narrowing of the weightbearing joint with some minor hypertrophic spurring medially.  She would like to have this x-rayed again today.  She is certainly not interested in any surgery.  She has noted that …
```

**Generated note**

```
**HISTORY OF PRESENT ILLNESS**

A 62-year-old white female presents with multiple concerns. 

She reports a history of hypertension and lipometabolism disorder, which she follows with her primary care physician (Doctor X Y Z). 

The patient expresses concern regarding her family history of diabetes, as both her father and brother have the condition. She attributes her own weight gain to this potential risk factor.

She complains of chronic left knee pain, which worsens upon kneeling. Imaging studies performed in 1999 revealed joint narrowing. 

Additionally, she reports occasional bright red rectal bleeding, often accompanied by baby yellow stools. Her last colonoscopy was in 1999. 

The patient also mentions recent gastrointestinal symptoms, including stomach pain, changes in bowel movements (hard or runny), and occasional diarrhea. 

Furthermore, she describes recent upper respiratory symptoms, including a sore throat, sneezing, and body aches, which may be related to a cold or flu. 

Lastly, she raises concerns about potential sleep apnea due to nocturnal awakenings and wonders if …
```

- unsupported entities (vs. transcript): diarrhea, knee pain, weight gain
- incorrect diagnosis: —  ·  missing diagnosis: —
- incorrect medication: —  ·  missing medication: loratadine
- dosage mismatch: —
- negation flips (vs. reference): —
- unsupported numbers: —
- missing information: {"symptom": ["itching", "loss of appetite", "pain", "snoring"], "diagnosis": ["diabetes"], "medication": ["loratadine"], "investigation": ["weight measurement"]}

## Incorrect diagnosis example: `mts_dialog_test_sum_2023_53`

*incorrect diagnosis example*

ROUGE-L 26.9 · length ratio 0.62 · truncated False · degenerate False · hallucination 21.4 · negation-flip 0.0 · numerical consistency 100.0 · coverage 85.7

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
**ASSESSMENT**

The patient, a male juvenile (Jay), presents with complaints of right shoulder pain and limited mobility following an injury sustained approximately 10 days ago while ice skating. The patient reports difficulty raising his arm above his head and occasional nocturnal numbness in his right hand fingers. 

Additionally, the patient has a history of recurrent streptococcal pharyngitis (strep throat) and currently experiences a sore throat. There is no reported fever, rash, nausea, vomiting, diarrhea, or constipation.

The patient has a pre-existing diagnosis of Attention Deficit Hyperactivity Disorder (ADHD). He is currently under treatment with Adderall and Zoloft, which appears to be effective in managing his symptoms when adhering to the prescribed regimen. However, the patient exhibits uncontrolled anger outbursts when off his medications, indicating potential non-adherence issues.
```

- unsupported entities (vs. transcript): adhd, shoulder pain, trauma
- incorrect diagnosis: adhd  ·  missing diagnosis: —
- incorrect medication: —  ·  missing medication: —
- dosage mismatch: —
- negation flips (vs. reference): —
- unsupported numbers: —
- missing information: {"symptom": ["falls"], "investigation": ["weight measurement"]}

## Incorrect medication / dosage example: `mts_dialog_test_sum_2023_67`

*incorrect medication / dosage example*

ROUGE-L 29.9 · length ratio 0.72 · truncated False · degenerate False · hallucination 33.3 · negation-flip 0.0 · numerical consistency 80.0 · coverage 28.6

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
**HISTORY OF PRESENT ILLNESS**

The patient is a 39-year-old female with a history of type one diabetes mellitus. She reports being generally well since her last visit approximately four months prior. However, she experienced difficulties with her insulin pump over the past two weeks, resulting in suboptimal blood glucose control. Despite these challenges, she denies experiencing any significant symptoms such as dizziness, sweating, or visual disturbances. Her urine output appears to be within normal limits, and she does not report excessive thirst or hunger. The patient is currently not engaging in regular exercise due to her busy schedule as a mother of three children, including twins. She works full-time as a medical coder and often forgets to eat meals, relying on snacks instead. The patient is compliant with her regular physician visits and has maintained a routine of annual check-ups, dental visits, and recent eye examination.
```

- unsupported entities (vs. transcript): insulin, polydipsia
- incorrect diagnosis: —  ·  missing diagnosis: —
- incorrect medication: insulin  ·  missing medication: —
- dosage mismatch: —
- negation flips (vs. reference): —
- unsupported numbers: 3
- missing information: {"symptom": ["polyphagia", "polyuria"], "diagnosis": ["diabetes"], "investigation": ["blood work", "lipid panel"]}

## Negation error example: `mts_dialog_test_sum_2023_6`

*negation error example*

ROUGE-L 25.5 · length ratio 0.96 · truncated False · degenerate False · hallucination 0.0 · negation-flip 100.0 · numerical consistency — · coverage 50.0

**Transcript (excerpt)**

```
Doctor: Do you feel any shortness of breath?
Patient: No.
Doctor: Any snoring or sleep disorder like interrupted breathing? 
Patient: Um, no.
Doctor: Any history of asthma or lung disease?
Patient: No.
```

**Reference note**

```
RESPIRATORY: No history of shortness of breath, no history of asthma, no history of chronic obstructive pulmonary disease, no history of obstructive sleep apnea.
```

**Generated note**

```
REVIEW OF SYSTEMS:

Respiratory System: 

- Shortness of breath: None reported.
- Snoring or sleep disorders (interrupted breathing): Denied.
- Asthma or lung disease: None reported.
```

- unsupported entities (vs. transcript): —
- incorrect diagnosis: —  ·  missing diagnosis: —
- incorrect medication: —  ·  missing medication: —
- dosage mismatch: —
- negation flips (vs. reference): asthma, dyspnea
- unsupported numbers: —
- missing information: {"medical_history": ["copd", "sleep apnea"]}

## Numerical error example: `mts_dialog_test_sum_2023_152`

*numerical error example*

ROUGE-L 29.2 · length ratio 1.40 · truncated False · degenerate False · hallucination 28.6 · negation-flip 0.0 · numerical consistency 50.0 · coverage 62.5

**Transcript (excerpt)**

```
Doctor: Do you have any medical conditions that I should be aware of? 
Patient: Yes, actually I have them written down right here. 
Doctor: May I see that list?
Patient: Absolutely, here you go, doctor. 
Doctor: Okay, this shows that you have a history of high blood pressure, high cholesterol, and non insulin dependent diabetes. Does that all sound familiar?
Patient: Yes, doctor. 
Doctor: Okay, so, what medicine do you take for your diabetes?
Patient: Honestly, I don't know, I didn't even think I had diabetes. 
Doctor: To be honest with you, that would be good information for me to know. Do you know of any other conditions? 
Patient: Yes, I had heart bypass surgery in July of two thousand si …
```

**Reference note**

```
Significant for hypertension, hypercholesterolemia and non-insulin-dependent diabetes mellitus.  The patient does not know what medications he is taking for diabetes and denies any diabetes.  CABG in July of 2006 with no preoperative angina, shortness of breath, or myocardial infarction.  History of depression, lumbar fusion surgery in 2000, left knee surgery 25 years ago.
```

**Generated note**

```
PAST MEDICAL HISTORY:

The patient has a history of the following medical conditions:

1. Hypertension (high blood pressure)
2. Hyperlipidemia (high cholesterol)
3. Non-insulin dependent diabetes mellitus (NIDDM) - unclear current treatment regimen
4. History of coronary artery disease (CAD), status post heart bypass surgery in July 2006
5. History of lower back surgery in 2000, described as a spinal fusion
6. History of left knee surgery approximately 25 years prior
7. Depression, chronic condition
```

- unsupported entities (vs. transcript): coronary artery disease, type 2 diabetes
- incorrect diagnosis: —  ·  missing diagnosis: —
- incorrect medication: —  ·  missing medication: —
- dosage mismatch: —
- negation flips (vs. reference): —
- unsupported numbers: 1, 3, 4, 5, 7
- missing information: {"symptom": ["dyspnea"], "diagnosis": ["angina", "myocardial infarction"]}

## Missing information example: `mts_dialog_test_sum_2023_78`

*missing information example*

ROUGE-L 10.2 · length ratio 1.27 · truncated False · degenerate False · hallucination 100.0 · negation-flip — · numerical consistency 66.7 · coverage 0.0

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
REVIEW OF SYSTEMS:

* General: The patient is a 10-day-old Caucasian female who appears to be thriving, feeding well, and active.
* Neurological: The patient has experienced repeated episodes (approximately six) of jerky arm and leg movements lasting about one minute each, occurring primarily while sleeping. These episodes were not associated with interrupted breathing, bluish discoloration, or eye movements.
* Gastrointestinal: The patient is feeding well, with an average of 8-9 wet diapers per day and 6-7 bowel movements per day. The stool color is described as "dirty yellowish."
* Developmental: The patient is gaining weight appropriately and meeting feeding milestones.
* Respiratory: No issues reported.
* Cardiovascular: No issues reported.
* Skin: No issues reported.
* Allergic/Immunologic: No issues reported.
* Psychiatric: No issues reported.
```

- unsupported entities (vs. transcript): weight gain
- incorrect diagnosis: —  ·  missing diagnosis: —
- incorrect medication: —  ·  missing medication: —
- dosage mismatch: —
- negation flips (vs. reference): —
- unsupported numbers: 1, 9
- missing information: {"symptom": ["diarrhea", "fever", "nasal congestion", "rash", "sneezing", "vomiting"]}
