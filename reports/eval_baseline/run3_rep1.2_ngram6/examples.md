# Example errors — run3_rep1.2_ngram6

Each block shows the transcript excerpt, the reference note, the generated note and the flags raised by the factuality checker.

# Split: aci_bench_test_taskB_1

## Best ROUGE-L: `aci_bench_test_taskB_1_D2N098-virtscribe`

*highest ROUGE-L in the split*

ROUGE-L 24.0 · length ratio 1.34 · truncated False · degenerate False · hallucination 72.0 · negation-flip 0.0 · numerical consistency 75.0 · coverage 77.8

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

The patient is a 57-year-old male who comes into clinic complaining of chronic left shoulder and left elbow pain. He states that he had fallen down approximately 5 months prior to presentation onto his left lateral aspect. The patient denies paresthesias, weakness, or sensory changes associated with these complaints. No history of trauma post-fall except for the initial incident. Denies fever, chills, night sweats, weight loss, fatigue, joint swelling, redness, heat, tenderness, decreased range of motion, crepitus, effusion, instability, or locking.
He has had difficulty lifting heavy objects due to increased pain. He has continued to perform light activities including daily ambulation without significant limitations. He continues to work full-time despite his discomfort. He denies recent travel, sick contacts, or immunizations recently administered.

REVIEW OF SYSTEMS

Significant for musculoskeletal system. Negative review of systems otherwise.

PHYSICAL EXAMINATION

NECK:

Supple neck movement bilater …
```

- unsupported entities (vs. transcript): bruising, chills, crepitus, dislocation, edema, elbow pain, fatigue, fever, fracture, joint instability, joint swelling, night sweats, reduced range of motion, tendinitis, vaccine, weakness, weight loss, x-ray
- incorrect diagnosis: —  ·  missing diagnosis: —
- incorrect medication: vaccine  ·  missing medication: —
- dosage mismatch: —
- negation flips (vs. reference): —
- unsupported numbers: 57
- missing information: {"symptom": ["tingling", "warmth"]}

## Worst ROUGE-L: `aci_bench_test_taskB_1_D2N109-aci`

*lowest ROUGE-L in the split*

ROUGE-L 3.7 · length ratio 1.70 · truncated True · degenerate False · hallucination 87.5 · negation-flip 0.0 · numerical consistency 54.5 · coverage 36.0

**Transcript (excerpt)**

```
[doctor] so stephanie morales is a 36 -year-old female today complaining of her ankle pain and she also has a history of diabetes and high blood pressure so stephanie tell me what's going on with your ankle
[patient] well we had a long spring and the other day we got some snow and ice i was walking to my car and i slipped and my left ankle kinda turned underneath me
[doctor] okay and so this happened couple days ago or how many days ago
[patient] two days ago
[doctor] two days ago okay and so it's your left ankle and it kinda just twisted underneath you on the kind of on the inside
[patient] yeah more on the it's more on the outside of my hips
[doctor] and did you fall down or did you just k …
```

**Reference note**

```
CHIEF COMPLAINT

Left ankle pain.

MEDICAL HISTORY

Patient reports history significant for type 2 diabetes and hypertension.

MEDICATIONS

Patient reports taking metformin and Norvasc.

REVIEW OF SYSTEMS

Musculoskeletal: Reports left ankle pain and swelling.\ Denies left calf pain, lower left leg pain, or left knee pain.

VITALS

Blood pressure: 120/70 mmHg

PHYSICAL EXAM

Neurological
- Examination: Sensation intact in left lower extremity.

Neck
- General Examination: No bruits.

Respiratory
- Auscultation of Lungs: Clear bilaterally.

Cardiovascular
- Examination: Pulses are normal in left lower extremity.
- Auscultation of Heart: 2/6 systolic ejection murmur, unchanged from previous exam.

Musculoskeletal
- Examination of the left ankle: Tender to palpation over the lateral malleolus and fifth metatarsal. Trace edema. Mild erythema. Pain with valgus stress testing.

RESULTS

Hemogl …
```

**Generated note**

```
CHIEF COMPLAINT:

The patient Stephanie Morales is a 36-year-old female who presents to the emergency room today complaining of left ankle pain after twisting injury.

HISTORY OF PRESENT ILLNESS:

Stephanie Morales states that she is a diabetic and hypertensive. She denies fever chills night sweats abdominal pain chest pain shortness of breath palpitations syncope weakness fatigue dizziness dyspnea cough sputum production pleuritic chest pain arthralgia joint pains headache photophobia visual disturbances diplopia hearing loss tinnitus vertigo syncope near-syncope fainting spells paresthesias numbness tingling burning sensations around mouth lips face extremities bilateral edema erythematous rash pruritus urticaria wheezes stridor hoarseness voice change difficulty swallowing odynophagia dysphonia dysuria frequency urgency nocturia oliguria polyuria hematuria proteinuria hypertension hypotension orthopnea paroxysmal nocturnal dyspnea PND exertional dyspnea pedal edema jugular venous distention JVD ascites hepatomegaly splenomegaly jaundice icteric sclerae bruising petechiae purpura e …
```

- unsupported entities (vs. transcript): abdominal pain, blood in stool, blurred vision, bruising, burning sensation, cataract, cellulitis, chest pain, chills, conjunctivitis, constipation, cough, deep vein thrombosis, diarrhea, dizziness, double vision, dysphagia, dyspnea, dysuria, fatigue
- incorrect diagnosis: —  ·  missing diagnosis: fracture, sprain, type 2 diabetes
- incorrect medication: —  ·  missing medication: amlodipine, metformin, naproxen
- dosage mismatch: —
- negation flips (vs. reference): —
- unsupported numbers: 0, 4, 5, 7, 9
- missing information: {"symptom": ["knee pain", "leg pain", "pain"], "medical_history": ["type 2 diabetes"], "diagnosis": ["fracture", "sprain"], "medication": ["amlodipine", "metformin", "naproxen"], "investigation": ["blood pressure measurement", "blood work", "diagnostic workup", "heart rate measurement", "hemoglobin a1c", "home monitoring"]}

## Hallucination example: `aci_bench_test_taskB_1_D2N116-aci`

*hallucination example*

ROUGE-L 7.4 · length ratio 1.28 · truncated True · degenerate False · hallucination 95.8 · negation-flip 25.0 · numerical consistency — · coverage 23.5

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
CHIEF COMPLAINT:

The patient presents today complaining of chronic right-sided shoulder pain.

HISTORY OF PRESENT ILLNESS:

Bobby comes into clinic today complaining of his right shoulder pain. He states he has had this type of pain off-and-on for years. However, recently he has noticed increased pain after working around the house. The patient denies fevers chills weakness fatigue weight loss palpitations shortness of breath orthopnea paroxysmal nocturnal dyspnea PND chest pain abdominal pain nausea vomiting diarrhea constipation headache dizziness syncope visual changes hearing change diplopia paresthesias tingling extremities edema arthralgias joint swelling muscle weakness gait disturbances tremors memory difficulty confusion personality changes mood swings anxiety depression irritability insomnia urinary frequency urgency retention nocturia hematuria gross hematuria microscopic hematuria flank pain costovertebral angle tenderness CVA TIA hypertension hyperlipidemia diabetes mellitus allergies asthma COPD emphysema bronchitis pneumonia sinusitis URI pharyngitis tonsillitis otiti …
```

- unsupported entities (vs. transcript): abdominal pain, abscess, acne, adrenal insufficiency, allergic rhinitis, anxiety, aortic aneurysm, appendicitis, arrhythmia, asthma, atrial fibrillation, bleeding, blurred vision, bronchitis, bundle branch block, cellulitis, chest pain, chills, chronic kidney disease, cirrhosis
- incorrect diagnosis: —  ·  missing diagnosis: rotator cuff tear
- incorrect medication: —  ·  missing medication: acetaminophen, cortisone injection, ibuprofen
- dosage mismatch: —
- negation flips (vs. reference): dislocation
- unsupported numbers: —
- missing information: {"symptom": ["ankle pain", "foot pain"], "diagnosis": ["fracture", "rotator cuff tear"], "medication": ["acetaminophen", "cortisone injection", "ibuprofen"], "investigation": ["blood pressure measurement", "heart rate measurement", "mri", "oxygen saturation", "physical examination", "x-ray"]}

## Incorrect diagnosis example: `aci_bench_test_taskB_1_D2N111-aci`

*incorrect diagnosis example*

ROUGE-L 5.2 · length ratio 1.02 · truncated True · degenerate False · hallucination 97.2 · negation-flip 33.3 · numerical consistency 100.0 · coverage 11.5

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
CHIEF COMPLAINT:

The patient comes in today complaining of his right knee pain after he had gone to the trampoline park last weekend.  He states that he has never been to one prior to this incident.  The patient denies any history of trauma except for the above-mentioned event.  Denies fever chills night sweats weakness fatigue malaise shortness of breath palpitations orthopnea paroxysmal nocturnal dyspnea PND chest pain abdominal pain nausea vomiting diarrhea constipation headache dizziness syncope visual changes hearing loss tinnitus vertigo joint pains muscle pains rash pruritus arthralgias arthritis wheezing cough sputum production hemoptysis pleural friction rub decreased urine output flank pain costovertebral angle tenderness CVA TIA MI asthma allergies hayfever urticaria angioedema erythematous nodules petechiae purpura epistaxis hematemesis melena rectal bleeding GU symptoms sexual dysfunction erectile dysfunction impotence libido decrease urinary frequency urgency hesitancy dysuria frequency nocturia oliguria polyuria nocturia enuresis UTI kidney stones renal colic nephroli …
```

- unsupported entities (vs. transcript): abdominal pain, abscess, acute kidney injury, adrenal insufficiency, allergic rhinitis, angioedema, aortic regurgitation, appendicitis, arrhythmia, arthritis, asthma, atrial fibrillation, benign prostatic hyperplasia, blood in stool, blurred vision, bradycardia, brain tumor, bundle branch block, cancer, chest pain
- incorrect diagnosis: abscess, adrenal insufficiency, allergic rhinitis, angioedema, aortic regurgitation, appendicitis, arrhythmia, asthma, atrial fibrillation, brain tumor, bundle branch block, cancer, cholecystitis, chronic kidney disease, cirrhosis, colon cancer, coronary artery disease, deep vein thrombosis, diabetic nephropathy, diverticulitis, esophagitis, fatty liver disease, gastritis, gerd, glomerulonephritis, hepatitis, hernia, hydronephrosis, hyperthyroidism, hypothyroidism, infection, inflammatory bowel disease, irritable bowel syndrome, kidney cancer, kidney stones, lupus, mitral regurgitation, osteoarthritis, osteoporosis, ovarian cyst, pancreatitis, peptic ulcer disease, peripheral artery disease, pneumonia, pneumothorax, polymyalgia rheumatica, pregnancy, pulmonary embolism, raynaud's phenomenon, rheumatoid arthritis, sebaceous cyst, skin cancer, stroke, thyroid nodule, transient ischemic attack, tuberculosis, urinary tract infection, uterine fibroids, vasculitis  ·  missing diagnosis: diabetes, hypertension, strain, type 2 diabetes
- incorrect medication: —  ·  missing medication: acetaminophen, lisinopril, meloxicam, metformin
- dosage mismatch: —
- negation flips (vs. reference): trauma
- unsupported numbers: —
- missing information: {"symptom": ["bruising", "edema", "joint swelling", "murmur"], "medical_history": ["hypertension", "type 2 diabetes"], "diagnosis": ["diabetes", "fracture", "strain"], "medication": ["acetaminophen", "lisinopril", "meloxicam", "metformin"], "investigation": ["blood glucose", "blood pressure measurement", "diagnostic workup", "echocardiogram", "hemoglobin a1c", "home monitoring"]}

## Incorrect medication / dosage example: `aci_bench_test_taskB_1_D2N093-virtassist`

*incorrect medication / dosage example*

ROUGE-L 8.4 · length ratio 0.62 · truncated True · degenerate True · hallucination 85.9 · negation-flip 9.1 · numerical consistency 10.8 · coverage 40.0

**Transcript (excerpt)**

```
[doctor] hey lawrence . how are you ?
[patient] hey , good to see you .
[doctor] it's good to see you too . so , i know the nurse told you about dax .
[patient] mm-hmm .
[doctor] i'd like to tell dax a little bit about you .
[patient] sure .
[doctor] so , lawrence is a 62-year-old male , with a past medical history significant for type i diabetes , congestive heart failure , depression , and reflux , who presents with complaints of shortness of breath . so lawrence , what's been going on ? wh- what's wrong with your breathing ?
[patient] uh , i , i've noticed that i've been swelling up a little bit . i think a lot of it has to do with going to some house parties , eating some salty foods . i …
```

**Reference note**

```
CHIEF COMPLAINT

Shortness of breath.

HISTORY OF PRESENT ILLNESS

Lawrence Walker is a 62-year-old male with a past medical history significant for type 1 diabetes, congestive heart failure, depression, and reflux, who presents with complaints of shortness of breath.

The patient states he has had some shortness of breath and mild leg swelling which he thinks has to do with eating some salty foods at some house parties recently. His shortness of breath is primarily with exertion such as walking up the stairs. This has been going on for about 10 days now. He woke from sleep once with shortness of breath about a week ago. He also notes discomfort lying flat in bed and musculoskeletal stiffness in the morning. He states that it takes him a little while to get up.

Regarding his type 1 diabetes, he is using his insulin pump. He has been consistently monitoring his blood sugars during the wo …
```

**Generated note**

```
CHIEF COMPLAINT:

The patient is a 62 y/o M with HPI of SOB, fatigue, orthopnea, PND, pedal edema, dyspnea on exertion, and decreased mobility.

HISTORY OF PRESENT ILLNESS:

This is a 62 y.o.m. with a hpi of S.O.B., fatigue, orthopnea P.N.D., pedal edema, D.O.E., and decreased mobility. He states he has had these symptoms for approximately 10 days. The patient denies fevers, chills, pleuritic chest pains, abdominal pain, nausea, vomiting, diarrhea, constipation, arthralgias, joint effusions, rash, pruritus, wheezing, hoarseness, stridor, odynophagia, dysphonia, palpitations, syncope, weakness, tremors, confusion, memory loss, visual changes, diplopia, photophobia, headache, vertigo, tinnitus, hearing loss, epistaxis, hemoptysis, hematemesis, melena, hematochezia, nocturia, frequency, urgency, dysuria, flank pain, costovertebral angle tenderness, CVA/TIA, hypertension, hyperlipidemia, asthma, allergies, chronic obstructive pulmonary disease (COPD), sleep apnea, gastroesophageal reflux disease (GERD).

REVIEW OF SYSTEMS:

CONSTITUTIONAL: Negative.
RESPIRATORY: Positive for SOB, orthopn …
```

- unsupported entities (vs. transcript): allergic rhinitis, asthma, bilirubin, blood in stool, blurred vision, calcium supplement, coagulation studies, complete blood count, confusion, constipation, copd, creatinine, diarrhea, dizziness, double vision, dysphagia, dyspnea on exertion, dysuria, gerd, headache
- incorrect diagnosis: —  ·  missing diagnosis: depression, heart failure, type 1 diabetes
- incorrect medication: calcium supplement, testosterone  ·  missing medication: furosemide, insulin, omeprazole
- dosage mismatch: —
- negation flips (vs. reference): abdominal pain
- unsupported numbers: 0, 0.05, 0.7, 0.9, 1.02, 1.04, 100, 11, 12, 120, 13, 130, 14, 15, 2
- missing information: {"symptom": ["cough", "heartburn", "murmur", "stiffness", "suicidal ideation"], "medical_history": ["depression", "heart failure", "type 1 diabetes"], "medication": ["furosemide", "insulin", "omeprazole"], "investigation": ["blood work", "diagnostic workup", "eye exam", "hemoglobin a1c", "weight measurement", "white blood cell count"]}

## Negation error example: `aci_bench_test_taskB_1_D2N127-aci`

*negation error example*

ROUGE-L 12.0 · length ratio 1.52 · truncated True · degenerate False · hallucination 84.6 · negation-flip 57.1 · numerical consistency 66.7 · coverage 40.0

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
CHIEF COMPLAINT:

The patient presents complaining of neck pain following a motor vehicle collision.

HISTORY OF PRESENT ILLNESS:

Brandon comes in today for evaluation of his neck pain. He states he has had three MVA's within the past two years. The patient denies any history of trauma prior to the above-mentioned incidents. Brandon states that he did have cervical spine fusion performed approximately four years ago secondary to chronic degenerative disc disease. The patient denies any radiculopathy or paresthesias associated with his symptoms. The patient states that he has tried conservative management including NSAIDs without relief. The patient denies any weakness or paralysis. The patient denies any bowel/bladder dysfunction. The patient denies any dysphagia. The patient denies any hoarseness. The patient denies any weight loss. The patient denies any fever/chills. The patient denies any night sweats. The patient denies any arthralgias/joint pains. The patient denies any chest pain/shortness of breath. The patient denies any abdominal pain/diarrhea. The patient denies any hemop …
```

- unsupported entities (vs. transcript): abdominal pain, allergic rhinitis, blurred vision, bowel obstruction, chest pain, chills, confusion, constipation, cough, crepitus, degenerative disc disease, diarrhea, double vision, dysphagia, dyspnea, erythema, fever, hearing loss, hemoptysis, hoarseness
- incorrect diagnosis: —  ·  missing diagnosis: sprain
- incorrect medication: —  ·  missing medication: fentanyl, methocarbamol
- dosage mismatch: —
- negation flips (vs. reference): dizziness, edema, headache, numbness
- unsupported numbers: 3
- missing information: {"symptom": ["back pain", "bruising", "fatigue", "laceration", "stiffness"], "diagnosis": ["fracture", "sprain"], "medication": ["fentanyl", "methocarbamol"], "investigation": ["diagnostic workup", "mri", "x-ray"]}

## Numerical error example: `aci_bench_test_taskB_1_D2N093-virtassist`

*numerical error example*

ROUGE-L 8.4 · length ratio 0.62 · truncated True · degenerate True · hallucination 85.9 · negation-flip 9.1 · numerical consistency 10.8 · coverage 40.0

**Transcript (excerpt)**

```
[doctor] hey lawrence . how are you ?
[patient] hey , good to see you .
[doctor] it's good to see you too . so , i know the nurse told you about dax .
[patient] mm-hmm .
[doctor] i'd like to tell dax a little bit about you .
[patient] sure .
[doctor] so , lawrence is a 62-year-old male , with a past medical history significant for type i diabetes , congestive heart failure , depression , and reflux , who presents with complaints of shortness of breath . so lawrence , what's been going on ? wh- what's wrong with your breathing ?
[patient] uh , i , i've noticed that i've been swelling up a little bit . i think a lot of it has to do with going to some house parties , eating some salty foods . i …
```

**Reference note**

```
CHIEF COMPLAINT

Shortness of breath.

HISTORY OF PRESENT ILLNESS

Lawrence Walker is a 62-year-old male with a past medical history significant for type 1 diabetes, congestive heart failure, depression, and reflux, who presents with complaints of shortness of breath.

The patient states he has had some shortness of breath and mild leg swelling which he thinks has to do with eating some salty foods at some house parties recently. His shortness of breath is primarily with exertion such as walking up the stairs. This has been going on for about 10 days now. He woke from sleep once with shortness of breath about a week ago. He also notes discomfort lying flat in bed and musculoskeletal stiffness in the morning. He states that it takes him a little while to get up.

Regarding his type 1 diabetes, he is using his insulin pump. He has been consistently monitoring his blood sugars during the wo …
```

**Generated note**

```
CHIEF COMPLAINT:

The patient is a 62 y/o M with HPI of SOB, fatigue, orthopnea, PND, pedal edema, dyspnea on exertion, and decreased mobility.

HISTORY OF PRESENT ILLNESS:

This is a 62 y.o.m. with a hpi of S.O.B., fatigue, orthopnea P.N.D., pedal edema, D.O.E., and decreased mobility. He states he has had these symptoms for approximately 10 days. The patient denies fevers, chills, pleuritic chest pains, abdominal pain, nausea, vomiting, diarrhea, constipation, arthralgias, joint effusions, rash, pruritus, wheezing, hoarseness, stridor, odynophagia, dysphonia, palpitations, syncope, weakness, tremors, confusion, memory loss, visual changes, diplopia, photophobia, headache, vertigo, tinnitus, hearing loss, epistaxis, hemoptysis, hematemesis, melena, hematochezia, nocturia, frequency, urgency, dysuria, flank pain, costovertebral angle tenderness, CVA/TIA, hypertension, hyperlipidemia, asthma, allergies, chronic obstructive pulmonary disease (COPD), sleep apnea, gastroesophageal reflux disease (GERD).

REVIEW OF SYSTEMS:

CONSTITUTIONAL: Negative.
RESPIRATORY: Positive for SOB, orthopn …
```

- unsupported entities (vs. transcript): allergic rhinitis, asthma, bilirubin, blood in stool, blurred vision, calcium supplement, coagulation studies, complete blood count, confusion, constipation, copd, creatinine, diarrhea, dizziness, double vision, dysphagia, dyspnea on exertion, dysuria, gerd, headache
- incorrect diagnosis: —  ·  missing diagnosis: depression, heart failure, type 1 diabetes
- incorrect medication: calcium supplement, testosterone  ·  missing medication: furosemide, insulin, omeprazole
- dosage mismatch: —
- negation flips (vs. reference): abdominal pain
- unsupported numbers: 0, 0.05, 0.7, 0.9, 1.02, 1.04, 100, 11, 12, 120, 13, 130, 14, 15, 2
- missing information: {"symptom": ["cough", "heartburn", "murmur", "stiffness", "suicidal ideation"], "medical_history": ["depression", "heart failure", "type 1 diabetes"], "medication": ["furosemide", "insulin", "omeprazole"], "investigation": ["blood work", "diagnostic workup", "eye exam", "hemoglobin a1c", "weight measurement", "white blood cell count"]}

## Missing information example: `aci_bench_test_taskB_1_D2N111-aci`

*missing information example*

ROUGE-L 5.2 · length ratio 1.02 · truncated True · degenerate False · hallucination 97.2 · negation-flip 33.3 · numerical consistency 100.0 · coverage 11.5

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
CHIEF COMPLAINT:

The patient comes in today complaining of his right knee pain after he had gone to the trampoline park last weekend.  He states that he has never been to one prior to this incident.  The patient denies any history of trauma except for the above-mentioned event.  Denies fever chills night sweats weakness fatigue malaise shortness of breath palpitations orthopnea paroxysmal nocturnal dyspnea PND chest pain abdominal pain nausea vomiting diarrhea constipation headache dizziness syncope visual changes hearing loss tinnitus vertigo joint pains muscle pains rash pruritus arthralgias arthritis wheezing cough sputum production hemoptysis pleural friction rub decreased urine output flank pain costovertebral angle tenderness CVA TIA MI asthma allergies hayfever urticaria angioedema erythematous nodules petechiae purpura epistaxis hematemesis melena rectal bleeding GU symptoms sexual dysfunction erectile dysfunction impotence libido decrease urinary frequency urgency hesitancy dysuria frequency nocturia oliguria polyuria nocturia enuresis UTI kidney stones renal colic nephroli …
```

- unsupported entities (vs. transcript): abdominal pain, abscess, acute kidney injury, adrenal insufficiency, allergic rhinitis, angioedema, aortic regurgitation, appendicitis, arrhythmia, arthritis, asthma, atrial fibrillation, benign prostatic hyperplasia, blood in stool, blurred vision, bradycardia, brain tumor, bundle branch block, cancer, chest pain
- incorrect diagnosis: abscess, adrenal insufficiency, allergic rhinitis, angioedema, aortic regurgitation, appendicitis, arrhythmia, asthma, atrial fibrillation, brain tumor, bundle branch block, cancer, cholecystitis, chronic kidney disease, cirrhosis, colon cancer, coronary artery disease, deep vein thrombosis, diabetic nephropathy, diverticulitis, esophagitis, fatty liver disease, gastritis, gerd, glomerulonephritis, hepatitis, hernia, hydronephrosis, hyperthyroidism, hypothyroidism, infection, inflammatory bowel disease, irritable bowel syndrome, kidney cancer, kidney stones, lupus, mitral regurgitation, osteoarthritis, osteoporosis, ovarian cyst, pancreatitis, peptic ulcer disease, peripheral artery disease, pneumonia, pneumothorax, polymyalgia rheumatica, pregnancy, pulmonary embolism, raynaud's phenomenon, rheumatoid arthritis, sebaceous cyst, skin cancer, stroke, thyroid nodule, transient ischemic attack, tuberculosis, urinary tract infection, uterine fibroids, vasculitis  ·  missing diagnosis: diabetes, hypertension, strain, type 2 diabetes
- incorrect medication: —  ·  missing medication: acetaminophen, lisinopril, meloxicam, metformin
- dosage mismatch: —
- negation flips (vs. reference): trauma
- unsupported numbers: —
- missing information: {"symptom": ["bruising", "edema", "joint swelling", "murmur"], "medical_history": ["hypertension", "type 2 diabetes"], "diagnosis": ["diabetes", "fracture", "strain"], "medication": ["acetaminophen", "lisinopril", "meloxicam", "metformin"], "investigation": ["blood glucose", "blood pressure measurement", "diagnostic workup", "echocardiogram", "hemoglobin a1c", "home monitoring"]}

## Degenerate output example: `aci_bench_test_taskB_1_D2N106-aci`

*degenerate output example*

ROUGE-L 6.5 · length ratio 1.12 · truncated True · degenerate True · hallucination 93.3 · negation-flip 28.6 · numerical consistency 100.0 · coverage 38.9

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
CHIEF COMPLAINT:

The patient presents here today complaining of difficulty breathing and has been having these problems since he was moving into his current residence approximately one year ago.  He denies any history of allergies, however, he states that he has had recent episodes of dyspnea associated with exposure to her feline pet.  The patient denies any history of urticaria, angioedema, laryngospasm, rhinitis, conjunctivitis, sinus pressure, nasal congestion, cough, sputum production, hemoptysis, pleuritic pain, fever, chills, arthralgias, joint pains, muscle weakness, fatigue, weight loss, abdominal discomfort, nausea, vomiting, diarrhea, constipation, pruritus, edema, erythematous rashes, oral ulcers, hoarseness, voice changes, palpitations, syncope, orthopnea, PND, SOB, orthostatic hypotension, hypertension, tachycardia, bradycardia, tremors, seizures, confusion, memory loss, personality change, visual disturbances, diplopia, photophobia, hearing loss, vertigo, dizziness, headache, neck stiffness, backache, radiculopathy, paresthesias, numbness, tingling, burning sensation, …
```

- unsupported entities (vs. transcript): abdominal pain, abscess, acute kidney injury, anal fissure, appendicitis, arrhythmia, atrial fibrillation, back pain, benign prostatic hyperplasia, bleeding, blood in stool, bradycardia, bruising, bundle branch block, burning sensation, bursitis, cellulitis, chills, cholecystitis, chronic kidney disease
- incorrect diagnosis: abscess, anal fissure, appendicitis, arrhythmia, benign prostatic hyperplasia, bundle branch block, bursitis, cellulitis, cholecystitis, chronic kidney disease, cirrhosis, coronary artery disease, degenerative disc disease, dental caries, dislocation, fracture, frozen shoulder, gastritis, gastroenteritis, gerd, gout, heart failure, hernia, herniated disc, hydronephrosis, hypertension, ingrown toenail, kidney stones, lupus, mitral regurgitation, neuropathy, orthostatic hypotension, osteoarthritis, pancreatitis, patellofemoral pain syndrome, peptic ulcer disease, periodontal disease, peripheral artery disease, pharyngitis, plantar fasciitis, prostate cancer, raynaud's phenomenon, rheumatoid arthritis, sciatica, scoliosis, sepsis, spinal stenosis, sprain, thrombocytopenia, urinary tract infection  ·  missing diagnosis: asthma
- incorrect medication: —  ·  missing medication: albuterol, montelukast
- dosage mismatch: —
- negation flips (vs. reference): allergic rhinitis, diarrhea
- unsupported numbers: —
- missing information: {"symptom": ["flare", "throat swelling", "wheezing"], "medical_history": ["asthma"], "medication": ["albuterol", "montelukast"], "investigation": ["allergy testing", "diagnostic workup", "oxygen saturation", "pulmonary function test", "x-ray"]}

# Split: aci_bench_test_taskC_2

## Best ROUGE-L: `aci_bench_test_taskC_2_D2N162-aci`

*highest ROUGE-L in the split*

ROUGE-L 23.7 · length ratio 0.83 · truncated False · degenerate False · hallucination 36.8 · negation-flip 0.0 · numerical consistency 21.1 · coverage 75.0

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
CHIEF COMPLAINT:

Right ankle pain and swelling following fall onto ice.

HISTORY OF PRESENT ILLNESS:

The patient states that he was slipping on ice and fell down. He denies any previous history of trauma to his right lower extremities. The patient states that he has been taking Ibuprofen for pain relief. Denies paresthesias in her feet. She has been elevating her RLE and applying ice packs. No significant past medical problems noted except for chronic allergies.
REVIEW OF SYSTEMS:

Significant for musculoskeletal system due to recent onset of right ankle pain and swelling secondary to fall. Negative for respiratory, cardiovascular, gastrointestinal, genitourinary systems.

PHYSICAL EXAMINATION:

VITAL SIGNS:
Blood pressure: 130/80 mm Hg; Pulse rate: 78 bpm; Respiratory Rate: 16/min; Temperature: 98.6°F (37°C)

NEUROLOGIC:
Cranial Nerves II-XII grossly within normal limits. Motor strength 5/5 throughout bilateral upper and lower extremities. Sensation to light touch bilaterally symmetrical. Reflexes +2 bilaterally symmetric.

MUSKULOSKELETAL:
RANGE OF MOTION: Right Lower Extremity:  …
```

- unsupported entities (vs. transcript): allergic rhinitis, blood pressure measurement, diagnostic workup, imaging, mri, respiratory rate, strain
- incorrect diagnosis: strain  ·  missing diagnosis: sprain
- incorrect medication: —  ·  missing medication: —
- dosage mismatch: —
- negation flips (vs. reference): —
- unsupported numbers: 10, 12, 130, 130/80, 15, 16, 18, 20, 25, 37, 40, 45, 78, 80, 98.6
- missing information: {"symptom": ["bruising"], "diagnosis": ["sprain"], "investigation": ["vital signs", "weight measurement"]}

## Worst ROUGE-L: `aci_bench_test_taskC_2_D2N156-aci`

*lowest ROUGE-L in the split*

ROUGE-L 4.6 · length ratio 0.97 · truncated True · degenerate True · hallucination 92.6 · negation-flip 0.0 · numerical consistency 0.0 · coverage 25.9

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
CHIEF COMPLAINT:

The patient comes in today for routine post-stemI followup.

HISTORY OF PRESENT ILLNESS:

This is a 62-year-old female who has been under care by Dr. XXXX for several years due to multiple comorbid conditions including CAD, HTN, DMII, dyslipidemia, etc. She presented to ER recently with new onset STEMI status post RCA stenting. The patient states she has been following her regimen faithfully except for dietary restrictions which she admits she has not adhered strictly to. She denies recent exertional angina, SOB, orthopnea, PND, paroxysmal nocturnal dyspnea, pedal edema, pleuritic chest pain, hemoptysis, syncope, near-syncope, dizziness, lightheadedness, weakness, fatigue, weight loss, fever, chills, arthralgias, joint pains, rash, pruritus, itching, urticaria, wheezing, cough, sputum production, hoarseness, sore throat, odynophagia, dysphonia, dysarthria, diplopia, blurred vision, photophobia, headache, confusion, memory loss, forgetfulness, tremors, gait disturbances, difficulty ambulating, falls, decreased libido, erectile dysfunction, impotence, urinary frequenc …
```

- unsupported entities (vs. transcript): abdominal pain, angina, anxiety, anxiety symptoms, benign prostatic hyperplasia, bilirubin, bipolar disorder, blood in stool, blurred vision, bruising, burning sensation, chills, coagulation studies, confusion, constipation, cough, daytime sleepiness, decreased libido, dehydration, dementia
- incorrect diagnosis: anxiety, benign prostatic hyperplasia, bipolar disorder, dehydration, dementia, depression, eating disorder, gi bleed, hypernatremia, hyponatremia, infection, leukopenia, neuropathy, peripheral artery disease, raynaud's phenomenon, schizophrenia, thrombocytopenia, trauma, vasculitis  ·  missing diagnosis: heart failure, mitral regurgitation
- incorrect medication: —  ·  missing medication: aspirin, atorvastatin, furosemide, lisinopril, metformin, metoprolol, spironolactone, ticagrelor
- dosage mismatch: —
- negation flips (vs. reference): —
- unsupported numbers: 62
- missing information: {"symptom": ["murmur"], "diagnosis": ["heart failure", "intracranial hemorrhage", "mitral regurgitation"], "medication": ["aspirin", "atorvastatin", "furosemide", "lisinopril", "metformin", "metoprolol"], "investigation": ["blood glucose", "blood pressure measurement", "blood work", "echocardiogram", "electrocardiogram", "heart rate measurement"]}

## Hallucination example: `aci_bench_test_taskC_2_D2N165-aci`

*hallucination example*

ROUGE-L 5.9 · length ratio 1.34 · truncated True · degenerate False · hallucination 95.7 · negation-flip 0.0 · numerical consistency 50.0 · coverage 27.8

**Transcript (excerpt)**

```
[doctor] hey sophia how are you doing today
[patient] i've been better my primary care doctor wanted me to see you because of this knee pain that i've been having for about six months now
[doctor] okay do you remember what caused the pain initially
[patient] you know i really ca n't recall any specific event that caused the pain
[doctor] alright well can can you describe the pain for me
[patient] yeah so it's it's like a deep achy pain that it i feel like it's behind my kneecaps and sometimes i can even hear like what seems like like some creaking in my knees
[doctor] hmmm alright now tell me what what type of activities makes that pain worse
[patient] so i feel like the pain gets worse anyt …
```

**Reference note**

```
CHIEF COMPLAINT

Bilateral knee pain.

HISTORY OF PRESENT ILLNESS

Sophia Jackson is a pleasant 30-year-old female who presents to the clinic today for the evaluation of bilateral knee pain. She was referred by her primary care provider. The onset of her pain began 6 months ago. She denies any specific injury. The patient describes her pain as a deep, achy pain. She locates her pain to the posterior aspect of her patellae. The patient also reports “creaking” in her knees. She denies any swelling or redness in her knees. Her pain is aggravated by transitioning from a seated position to standing as well as ascending and descending stairs. Her pain is alleviated by rest. The patient has been icing her knees and wrapping her knees with an ACE bandage. She also takes ibuprofen or Aleve occasionally for pain. She states she tries to be as active as she can. She enjoys running outdoors. The pat …
```

**Generated note**

```
CHIEF COMPLAINT:

The patient presents with chief complaint of left knee pain for approximately 6 months duration.

HISTORY OF PRESENT ILLNESS:

Sophia comes into clinic complaining of her left knee pain for approximately six months. She denies trauma. The onset of pain began gradually without any precipitating factors. Denies history of fever chills night sweats weight loss fatigue malaise weakness joint stiffness morning stiffness arthralgias myalgias dysuria frequency nocturia abdominal pain chest pain shortness of breath orthopnea paroxysmal nocturnal dyspnea PND edema pleural friction rub pericardial friction rub S1 Q2 Q3 Q4 gallop jugular venous distension JVD ascites hepatosplenomegaly lymphadenopathy rash pruritus urticaria wheezing cough sputum production hemoptysis syncope dizziness vertigo hearing loss tinnitus visual changes diplopia ptosis blurred vision photophobia headache confusion memory problems difficulty concentrating decreased libido erectile dysfunction impotence hot flashes cold intolerance thyroid nodules thyromegaly tremors asterixis clonus Babinski sign Hoff …
```

- unsupported entities (vs. transcript): abdominal pain, adhd, anxiety, arrhythmia, atrial fibrillation, autism, bipolar disorder, blood in stool, blurred vision, bradycardia, bundle branch block, cancer, cellulitis, chest pain, chills, chronic fatigue syndrome, cold intolerance, confusion, conjunctivitis, constipation
- incorrect diagnosis: —  ·  missing diagnosis: patellofemoral pain syndrome
- incorrect medication: fish oil  ·  missing medication: ibuprofen, naproxen
- dosage mismatch: —
- negation flips (vs. reference): —
- unsupported numbers: 1, 8
- missing information: {"symptom": ["bruising", "crepitus", "erythema", "joint swelling", "murmur", "warmth"], "medical_history": ["fracture"], "diagnosis": ["osteoarthritis", "patellofemoral pain syndrome"], "medication": ["ibuprofen", "naproxen"], "investigation": ["vital signs", "x-ray"]}

## Incorrect diagnosis example: `aci_bench_test_taskC_2_D2N129-virtassist`

*incorrect diagnosis example*

ROUGE-L 6.5 · length ratio 1.15 · truncated True · degenerate True · hallucination 97.7 · negation-flip 33.3 · numerical consistency — · coverage 25.0

**Transcript (excerpt)**

```
[doctor] good afternoon , beverly . good to see you .
[patient] nice to see you too .
[doctor] so , i know my nurse told you a little bit about dax . um , now , if you do n't mind , i'd like to tell dax a little bit about you .
[patient] go for it .
[doctor] great . um , beverly's a 24 year old female patient , and i know you have a history of type 2 diabetes and high blood pressure . correct ?
[patient] yep .
[doctor] okay . so , you're here today for your yearly exam . have n't seen you in a year . how're you doing ?
[patient] i've been doing well . i began working in a bakery this summer which has been super fun. i have really been enjoying working there, but i find myself, since i am so  …
```

**Reference note**

```
CHIEF COMPLAINT

Annual exam.

HISTORY OF PRESENT ILLNESS

Beverly Ortiz is a 24-year-old female patient with a history of type 2 diabetes and high blood pressure. She is here today for her yearly exam.

The patient states she has been doing well. She has recently began working at a bakery this summer.

The patient states her diabetes is uncontrolled. Her blood sugars have fluctuated recently, which she attributes to her change in diet due to work. She is trying to improve her diet by removing additional sweets. She has been taking her medication as prescribed and has not missed any doses.

The patient states her blood pressure has been good despite her blood sugar levels being up and down. She has continued taking metformin twice a day.

She has been sleeping well and is able to sleep a full 8 hours. She denies thoughts of self-harm or suicidal ideations.

PHYSICAL EXAMINATION

• Neurol …
```

**Generated note**

```
CHIEF COMPLAINT:

The patient Beverly comes in for her annual examination.  She states she works in a bakery and has been having difficulty controlling her weight due to constant exposure to baked goods.  Her Hb A1C has been elevated recently.  No complaints regarding HTN.  Denies dysuria, frequency, urgency, flank pain, abdominal pain, chest pain, palpitations, shortness of breath, orthostatic hypotension, syncope, weakness, numbness, tingling, tremors, gait disturbances, visual loss, hearing loss, tinnitus, vertigo, diplopia, photophobia, headache, fever, chills, arthralgias, joint pains, rash, pruritus, itching, urticaria, wheezing, cough, sputum production, pleural effusion, pedal edema, lymphadenopathy, night sweats, fatigue, malaise, anorexia, nausea, vomiting, diarrhea, constipation, abdominal distention, bloating, flatulence, dysphagia, hoarseness, sore throat, epistaxis, rhinitis, sinusitis, conjunctivitis, lacrimation, xerophthalmia, dry mouth, dental problems, gum disease, toothache, earaches, lightheadedness, faint feeling, dizzy spells, confusion, memory lapses, personal …
```

- unsupported entities (vs. transcript): abdominal pain, abscess, adrenal insufficiency, anal fissure, anxiety, appendicitis, arrhythmia, asthma, atrial fibrillation, bell's palsy, benign prostatic hyperplasia, bleeding, bloating, blood in stool, blurred vision, breast pain, bruising, bundle branch block, cataract, cellulitis
- incorrect diagnosis: adrenal insufficiency, anal fissure, anxiety, appendicitis, arrhythmia, atrial fibrillation, bell's palsy, benign prostatic hyperplasia, bundle branch block, cataract, cellulitis, chronic kidney disease, cirrhosis, conjunctivitis, copd, cushing's syndrome, deep vein thrombosis, depression, dislocation, diverticulitis, endocarditis, esophagitis, fatty liver disease, gastritis, gastroenteritis, gerd, glaucoma, hemorrhoids, hepatitis, hernia, hydronephrosis, hyperthyroidism, hypothyroidism, interstitial cystitis, intracranial hemorrhage, kidney cancer, kidney stones, lupus, meningitis, mitral regurgitation, myocardial infarction, neuropathy, osteoarthritis, overactive bladder, pancreatitis, peptic ulcer disease, periodontal disease, pleural effusion, prostate cancer, raynaud's phenomenon, retinal detachment, rheumatoid arthritis, sepsis, sinusitis, strain, thyroid nodule, transient ischemic attack, urinary tract infection, uveitis, vasculitis  ·  missing diagnosis: type 2 diabetes
- incorrect medication: —  ·  missing medication: lisinopril, metformin
- dosage mismatch: —
- negation flips (vs. reference): lymphadenopathy
- unsupported numbers: —
- missing information: {"symptom": ["crackles", "murmur", "rhonchi", "suicidal ideation"], "medical_history": ["type 2 diabetes"], "diagnosis": ["diabetes"], "medication": ["lisinopril", "metformin"], "investigation": ["blood glucose", "blood pressure measurement", "heart rate measurement", "physical examination"]}

## Incorrect medication / dosage example: `aci_bench_test_taskC_2_D2N148-aci`

*incorrect medication / dosage example*

ROUGE-L 8.6 · length ratio 1.19 · truncated True · degenerate True · hallucination 93.2 · negation-flip 40.0 · numerical consistency 33.3 · coverage 44.4

**Transcript (excerpt)**

```
[doctor] hi jeremy how are you the medical assistant told me that you injured your back
[patient] yeah i was moving some boxes when my son was moving out of his college dorm and i really hurt my lower back
[doctor] okay how long ago did that happen
[patient] this was about four months ago
[doctor] about four months ago okay that's quite a long time and you're just seeing me now for it
[patient] yeah the appointments were backed up and i tried some pt at my gym but it it really did n't seem to help and i was really concerned
[doctor] okay and what exactly are your symptoms are you having pain when you're just sitting there or when you're moving around for a very short period of time it felt l …
```

**Reference note**

```
HISTORY OF PRESENT ILLNESS

Jeremy Adams is a pleasant 57-year-old male who presents to the clinic today for the evaluation of low back pain. The onset of his pain began 4 months ago, when he was moving boxes out of his son’s college dorm. At that time, he noted tingling in his right toes, which resolved after approximately 1 hour. After his injury, he felt as though he was unable to support his upper body weight. The patient reports weakness in his legs when carrying heavy objects. He reports a sharp pain in his lower back when he turns a certain way or rolls over in his sleep. The pain will resolve with repositioning. The patient was seen at urgent care and was referred to obtain an MRI, however he did not undergo this secondary to insurance issues. He has been utilizing Tylenol, ibuprofen, heat, and ice for pain, which does not provide relief. The patient notes the ibuprofen is slight …
```

**Generated note**

```
CHIEF COMPLAINT:

The patient comes in today complaining of chronic low back pain radiating into her left lower extremity.  She states she has had these complaints for approximately 4 months.  The patient denies numbness, paresthesias, weakness, bowel/bladder dysfunction, fevers/chills, recent trauma, etc.

HISTORY OF PRESENT ILLNESS:

Jeremy is a 45-year-old female who presents to clinic today complaining of chronic low-back pain radiating into her LLE.  She states she had moved boxes during her son's college dormitory move-out.  She has had these complaints for 4 months.  She denies numbness, paresis, weakness, bowel-bladder dysfunction, fevers, chills, recent trauma, dysuria, frequency, urgency, hematuria, nocturia, constipation, diarrhea, abdominal pain, nausea, vomiting, chest pain, orthopnea, PND, SOB, wheezes, rales, cough, sputum production, pleuritic type chest pain, syncope, dizziness, vertigo, hearing loss, visual changes, diplopia, photophobia, headache, confusion, memory loss, tremors, muscle spasms, joint swelling, arthralgias, edema, rash, pruritus, itching, urticaria, …
```

- unsupported entities (vs. transcript): abdominal pain, adhd, allergic rhinitis, allergy testing, anxiety, asthma, audiogram, autoimmune panel, bipolar disorder, bloating, blood glucose, blood in stool, blurred vision, bronchoscopy, bruising, cancer, chest pain, coagulation studies, colonoscopy, complete blood count
- incorrect diagnosis: adhd, anxiety, bipolar disorder, cancer, depression, eating disorder, hepatitis, lumbar strain, pregnancy, ptsd, schizophrenia, sexually transmitted infection, substance use disorder, tuberculosis  ·  missing diagnosis: herniated disc
- incorrect medication: insulin, ivig, lactulose, progesterone  ·  missing medication: acetaminophen, ibuprofen, meloxicam
- dosage mismatch: —
- negation flips (vs. reference): trauma, weakness
- unsupported numbers: 45, 67
- missing information: {"symptom": ["back pain", "tingling"], "diagnosis": ["fracture", "herniated disc"], "medication": ["acetaminophen", "ibuprofen", "meloxicam"], "investigation": ["heart rate measurement", "physical examination", "weight measurement"]}

## Negation error example: `aci_bench_test_taskC_2_D2N133-virtassist`

*negation error example*

ROUGE-L 8.9 · length ratio 0.88 · truncated True · degenerate True · hallucination 95.9 · negation-flip 55.6 · numerical consistency 50.0 · coverage 58.8

**Transcript (excerpt)**

```
[doctor] good morning rebecca , nice to see you .
[patient] nice to see you too .
[doctor] so , my nurse told you a little bit about dax , now i'm wondering if i can tell dax a little bit about you .
[patient] go for it .
[doctor] okay , so rebecca is a 27-year-old female patient . um , you have a history of carpal tunnel , um , uh , release done couple of years ago , you have some chronic back pain , some depression . why am i seeing you today ?
[patient] so last week , um , and over the course of the month , i have taken up swimming more regularly .
[doctor] okay .
[patient] i've been trying to get up and get active . and i've- ... all of a sudden i've been feeling some really bad , um , k …
```

**Reference note**

```
CHIEF COMPLAINT

Joint pain

HISTORY OF PRESENT ILLNESS

Ms. Thompson is a 27 y.o. female with a history of carpal tunnel release done a couple years ago, chronic back pain, and depression. She presents today for joint pain.

Ms. Thompson reports that over the course of the month she has begun swimming more regularly and trying to be more active. She has experienced bad right knee pain. The patient reports that her knee starts hurting after a couple of laps. She notes previously she could swim 10 laps. She denies injury or trauma to the knee.

The patient has a history of chronic back pain that has been intermittent, but right now it has been doing well. She denies pain radiating down her legs.

The patient has a history of depression, which has been going really well with medication and therapy. She is trying to get outside more and it has been helping her with her depression. She notes …
```

**Generated note**

```
CHIEF COMPLAINT:

The patient is a 27 y/o F who has come into clinic complaining of new onset R knee pain associated with her increased activity level including swimming. She denies trauma to the area.

HISTORY OF PRESENT ILLNESS:

She states she has had bilateral C/T syndrome status post surgical intervention several years prior. Denies Hx of LBP except for occasional exacerbation. No hx of joint effusion or arthralgias. The patient has a h/o D/O treated w/ SSRI & psychotherapy. Her medications include sertraline 100 mg daily. She denies smoking, ETOH abuse, illicit drug use. She has no allergies.
No recent surgeries or hospitalizations.

REVIEW OF SYSTEMS:

Significant for lower extremity pain bilaterally. Negative for fever, chills, night sweats, weight loss, hemoptysis, orthopnea, PND, palpitations, dyspnea on exertion, chest pain, abdominal pain, nausea, vomiting, diarrhea, constipation, headache, visual disturbances, hearing difficulties, weakness, fatigue, tremors, muscle spasms, numbness, tingling, syncope, vertigo, edema, rash, pruritus, urticaria, itching, wheezing, cough,  …
```

- unsupported entities (vs. transcript): abdominal pain, abscess, allergic rhinitis, arthritis, asthma, atrial fibrillation, bleeding, bloating, bradycardia, burning sensation, cataract, cellulitis, chest pain, chills, cold intolerance, colon polyps, confusion, conjunctivitis, constipation, copd
- incorrect diagnosis: —  ·  missing diagnosis: carpal tunnel syndrome, depression, lumbar strain, patellofemoral pain syndrome
- incorrect medication: sertraline  ·  missing medication: ibuprofen
- dosage mismatch: —
- negation flips (vs. reference): crackles, joint pain, lymphadenopathy, murmur, trauma
- unsupported numbers: 100
- missing information: {"symptom": ["rhonchi"], "medical_history": ["depression", "lumbar strain"], "diagnosis": ["carpal tunnel syndrome", "patellofemoral pain syndrome"], "medication": ["ibuprofen"], "investigation": ["x-ray"]}

## Numerical error example: `aci_bench_test_taskC_2_D2N128-virtassist`

*numerical error example*

ROUGE-L 20.4 · length ratio 1.16 · truncated False · degenerate False · hallucination 60.4 · negation-flip 8.3 · numerical consistency 18.2 · coverage 77.8

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
CHIEF COMPLAINT:

The patient is a 49 y/o F who comes in today for evaluation of her chronic conditions including OA, GOUT, PSORIASIS.

HISTORY OF PRESENT ILLNESS:

Carolyn is a 49 y.o.f. She states that she has been having exacerbations of her Osteoarthritis particularly affecting her R.E.L.B.O.W. She denies any numbness or tingling in her H/O except during prolonged use of computers which may be related to her job requirements.  No new complaints regarding her Psoriasis or GOUT.  The patient is status post CLOBETASOL application for Scalp involvement of Psoriasis.  Her medications include Colchicine 0.6 mg BID PRN for GOUT, Meloxicam 7.5 mg QOD for OA, Prednisone tapering down now, and topical steroids for Psoriasis.

REVIEW OF SYSTEMS:

Significant for Joint Pain, Numbness/Tinging in Hands bilaterally, History of GOUT, History of Psoriasis, Denies Fever, Chills, Weight Loss, Abdominal Pain, Lower Extremities Swelling, Headache, Vision Changes, Hearing Difficulty, Dysphagia, Hemoptysis, Orthopnea, PND, S1/S2 heard bilaterally.

PHYSICAL EXAMINATION:

VITAL SIGNS: BP 130/80 mm/Hg; P …
```

- unsupported entities (vs. transcript): abdominal pain, blood pressure measurement, blurred vision, chills, creatinine, crp, diagnostic workup, dysphagia, erythema, esr, fever, fracture, headache, heart rate measurement, hemoptysis, imaging, infection, liver enzymes level, murmur, numbness
- incorrect diagnosis: fracture, infection, rheumatoid arthritis  ·  missing diagnosis: —
- incorrect medication: prednisone  ·  missing medication: —
- dosage mismatch: [{"drug": "colchicine", "predicted": "0 mg", "source": ["0.6 mg", "0.6 milligrams"]}, {"drug": "meloxicam", "predicted": "7.5 mg", "source": ["15 mg", "15 milligrams"]}]
- negation flips (vs. reference): tingling
- unsupported numbers: 0.9, 130, 130/80, 18, 19, 20, 22, 24, 250000, 3.5, 6.2, 7.2, 7.5, 78, 80
- missing information: {"symptom": ["crackles", "flare", "rhonchi", "wheezing"]}

## Missing information example: `aci_bench_test_taskC_2_D2N163-aci`

*missing information example*

ROUGE-L 5.4 · length ratio 1.53 · truncated True · degenerate True · hallucination 96.7 · negation-flip 0.0 · numerical consistency 100.0 · coverage 11.1

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
CHIEF COMPLAINT:

The patient is a 17-year-old female who comes in for her first visit to our office. She has been referred by Dr. Smith from primary care due to new diagnosis of hyperlipidemia.

HISTORY OF PRESENT ILLNESS:

This is a 17-year old female who comes into the office for initial assessment. The patient states she has never seen a specialist before. Her chief complaint is being recently diagnosed with hyperlipidemia. She denies any allergies, smoking, alcohol use, or illicit drug use. Denies any previous surgeries except tonsillectomy. No known chronic illnesses. Patient lives alone. Does not recall having any siblings die prematurely. Mother deceased. Father alive. Grandmother and Grandfather alive. Negative for hypertension, diabetes mellitus, asthma, eczema, arthritis, kidney stones, gallbladder problems, peptic ulcer disease, hemophilia, sickle cell disease, cystic fibrosis, tuberculosis, rheumatic fever, lupus erythematosus, multiple sclerosis, epilepsy, Parkinsonism, gouty arthritis, osteoporosis, hypothyroidism, hyperthyroidism, glaucoma, cataracts, conjunctivitis,  …
```

- unsupported entities (vs. transcript): acne, allergic rhinitis, arrhythmia, arthritis, asthma, atrial fibrillation, benign prostatic hyperplasia, bleeding disorder, cataract, chronic kidney disease, cirrhosis, conjunctivitis, deep vein thrombosis, diabetes, dysmenorrhea, dysuria, eczema, endometriosis, epilepsy, erectile dysfunction
- incorrect diagnosis: —  ·  missing diagnosis: myocardial infarction
- incorrect medication: —  ·  missing medication: —
- dosage mismatch: —
- negation flips (vs. reference): —
- unsupported numbers: —
- missing information: {"symptom": ["murmur"], "medical_history": ["myocardial infarction"], "investigation": ["blood pressure measurement", "genetic testing", "hemoglobin a1c", "lipid panel", "metabolic panel", "physical examination"]}

## Degenerate output example: `aci_bench_test_taskC_2_D2N148-aci`

*degenerate output example*

ROUGE-L 8.6 · length ratio 1.19 · truncated True · degenerate True · hallucination 93.2 · negation-flip 40.0 · numerical consistency 33.3 · coverage 44.4

**Transcript (excerpt)**

```
[doctor] hi jeremy how are you the medical assistant told me that you injured your back
[patient] yeah i was moving some boxes when my son was moving out of his college dorm and i really hurt my lower back
[doctor] okay how long ago did that happen
[patient] this was about four months ago
[doctor] about four months ago okay that's quite a long time and you're just seeing me now for it
[patient] yeah the appointments were backed up and i tried some pt at my gym but it it really did n't seem to help and i was really concerned
[doctor] okay and what exactly are your symptoms are you having pain when you're just sitting there or when you're moving around for a very short period of time it felt l …
```

**Reference note**

```
HISTORY OF PRESENT ILLNESS

Jeremy Adams is a pleasant 57-year-old male who presents to the clinic today for the evaluation of low back pain. The onset of his pain began 4 months ago, when he was moving boxes out of his son’s college dorm. At that time, he noted tingling in his right toes, which resolved after approximately 1 hour. After his injury, he felt as though he was unable to support his upper body weight. The patient reports weakness in his legs when carrying heavy objects. He reports a sharp pain in his lower back when he turns a certain way or rolls over in his sleep. The pain will resolve with repositioning. The patient was seen at urgent care and was referred to obtain an MRI, however he did not undergo this secondary to insurance issues. He has been utilizing Tylenol, ibuprofen, heat, and ice for pain, which does not provide relief. The patient notes the ibuprofen is slight …
```

**Generated note**

```
CHIEF COMPLAINT:

The patient comes in today complaining of chronic low back pain radiating into her left lower extremity.  She states she has had these complaints for approximately 4 months.  The patient denies numbness, paresthesias, weakness, bowel/bladder dysfunction, fevers/chills, recent trauma, etc.

HISTORY OF PRESENT ILLNESS:

Jeremy is a 45-year-old female who presents to clinic today complaining of chronic low-back pain radiating into her LLE.  She states she had moved boxes during her son's college dormitory move-out.  She has had these complaints for 4 months.  She denies numbness, paresis, weakness, bowel-bladder dysfunction, fevers, chills, recent trauma, dysuria, frequency, urgency, hematuria, nocturia, constipation, diarrhea, abdominal pain, nausea, vomiting, chest pain, orthopnea, PND, SOB, wheezes, rales, cough, sputum production, pleuritic type chest pain, syncope, dizziness, vertigo, hearing loss, visual changes, diplopia, photophobia, headache, confusion, memory loss, tremors, muscle spasms, joint swelling, arthralgias, edema, rash, pruritus, itching, urticaria, …
```

- unsupported entities (vs. transcript): abdominal pain, adhd, allergic rhinitis, allergy testing, anxiety, asthma, audiogram, autoimmune panel, bipolar disorder, bloating, blood glucose, blood in stool, blurred vision, bronchoscopy, bruising, cancer, chest pain, coagulation studies, colonoscopy, complete blood count
- incorrect diagnosis: adhd, anxiety, bipolar disorder, cancer, depression, eating disorder, hepatitis, lumbar strain, pregnancy, ptsd, schizophrenia, sexually transmitted infection, substance use disorder, tuberculosis  ·  missing diagnosis: herniated disc
- incorrect medication: insulin, ivig, lactulose, progesterone  ·  missing medication: acetaminophen, ibuprofen, meloxicam
- dosage mismatch: —
- negation flips (vs. reference): trauma, weakness
- unsupported numbers: 45, 67
- missing information: {"symptom": ["back pain", "tingling"], "diagnosis": ["fracture", "herniated disc"], "medication": ["acetaminophen", "ibuprofen", "meloxicam"], "investigation": ["heart rate measurement", "physical examination", "weight measurement"]}

# Split: aci_bench_test_taskC_3

## Best ROUGE-L: `aci_bench_test_taskC_3_D2N187-aci`

*highest ROUGE-L in the split*

ROUGE-L 34.7 · length ratio 1.05 · truncated False · degenerate False · hallucination 66.7 · negation-flip 0.0 · numerical consistency 18.8 · coverage 80.0

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
CHIEF COMPLAINT:

The patient comes in today complaining of decreased vision and distorted images.

HISTORY OF PRESENT ILLNESS:

Emily presents to clinic today for evaluation of her vision problems. She states she had blurred vision and distorted image. The patient denies any other symptoms at present. She does smoke one pack per day. Her last Hx includes hypertension and macular degeneration.

REVIEW OF SYSTEMS:

Significant for ophthalmology.

PHYSICAL EXAMINATION:

VITAL SIGNS: Blood Pressure 140/90 mm/Hg; Pulse Rate 80 bpm; Respiratory Rate 16/min; Tempature 98.6°F.

HEENT: Extraocular movements were normal. Pupils equal bilaterally round and reactive to light. Visual acuity R.E.: 20/40 L.E.: 20/50. Confrontation fields intact bilaterally. Anterior Segment Examination revealed Posterior Chamber Intraocular Lens (PCIOL) in both eyes. Right Eye Corneal clarity noted No MVI PCIOL Cup-to-Disc Ratio =0.2 Left Eye Corneal Clarity noted No MVI PCIOD Cup-to-Disc ratio=0.1 Fundoscopic findings show Drusen Macula Thickened Retina Sub-retinal Fluid Exudate Positive Hemorrhage Right Eye Atta …
```

- unsupported entities (vs. transcript): blurred vision, cardiac catheterization, heart rate measurement, hypertension, imaging, physical examination, respiratory rate, tobacco use
- incorrect diagnosis: hypertension, tobacco use  ·  missing diagnosis: —
- incorrect medication: —  ·  missing medication: —
- dosage mismatch: —
- negation flips (vs. reference): —
- unsupported numbers: 0.1, 140, 140/90, 16, 20, 20/40, 20/50, 30, 40, 50, 80, 90, 98.6
- missing information: {"investigation": ["diagnostic workup"]}

## Worst ROUGE-L: `aci_bench_test_taskC_3_D2N198-aci`

*lowest ROUGE-L in the split*

ROUGE-L 4.3 · length ratio 1.26 · truncated True · degenerate True · hallucination 92.5 · negation-flip 66.7 · numerical consistency — · coverage 33.3

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
CHIEF COMPLAINT:

The patient comes in for evaluation of her chief complaint which includes left-sided low back pain, fatigue, increased thirst, polyuria, dyspepsia, decreased exercise tolerance, recent change in employment status, negative for fever, chills, weight loss, arthralgias, joint pains, muscle weakness, visual changes, diplopia, photophobia, syncope, chest discomfort, orthopnea, paroxysmal nocturnal dyspnea, pedal edema, abdominal pain, hematemesis, melena, nausea, vomiting, diarrhea, constipation, pruritus, urticaria, rash, itching, hiccups, hoarseness, coughing, sputum production, shortness of breath, pleural effusion, pneumothorax, pericarditis, murmurs, gallops, jugular venous distension, hepatomegaly, splenomegaly, ascites, jaundice, icterus, dark urine, pale stools, clay-colored stool, bloody stools, black tarry stools, flank pain, frequency, urgency, dysuria, urinary retention, urethritis, epididymitis, orchalgia, penile discharge, impotence, erectile dysfunction, gynecomastia, breast enlargement, nipple retraction, axillary masses, supraclavicular nodes, mediastina …
```

- unsupported entities (vs. transcript): abdominal pain, abscess, adrenal insufficiency, anemia, asthma, bleeding, blood in stool, blurred vision, bruising, burning sensation, cancer, chest pain, chills, colon polyps, confusion, conjunctivitis, constipation, cough, crepitus, cushing's syndrome
- incorrect diagnosis: abscess, adrenal insufficiency, anemia, asthma, cancer, colon polyps, conjunctivitis, cushing's syndrome, diabetic retinopathy, hyperthyroidism, hypothyroidism, intracranial hemorrhage, leukemia, neuropathy, osteoporosis, otitis media, pericarditis, periodontal disease, peripheral artery disease, pharyngitis, pleural effusion, pneumonia, pneumothorax, pregnancy, sebaceous cyst, sinusitis, sleep apnea, thrombocytopenia, thyroid nodule  ·  missing diagnosis: glomerulonephritis
- incorrect medication: —  ·  missing medication: vitamin d
- dosage mismatch: —
- negation flips (vs. reference): edema, fatigue, murmur, wheezing
- unsupported numbers: —
- missing information: {"symptom": ["crackles", "erythema", "lymphadenopathy", "pain", "rhonchi"], "medical_history": ["glomerulonephritis"], "medication": ["vitamin d"], "investigation": ["complete blood count", "ct scan", "diagnostic workup", "lipid panel", "metabolic panel", "thyroid function test"]}

## Hallucination example: `aci_bench_test_taskC_3_D2N192-aci`

*hallucination example*

ROUGE-L 5.1 · length ratio 1.24 · truncated True · degenerate False · hallucination 94.8 · negation-flip 28.6 · numerical consistency 100.0 · coverage 27.6

**Transcript (excerpt)**

```
[doctor] karen is a 34 -year-old female with a history of chronic migraines and hypertension who is here today with abdominal pain so hi there karen it's nice to see you again listen i'm sorry you're not feeling well and you've got abdominal pain like to talk about that in some detail with you but hey i wan na use this new cool app that's gon na help me focus on you a bit more in this visit would that be okay with you
[patient] sure that's fine
[doctor] okay great so so karen tell me about your abdominal pain what's been happening
[patient] well it started about ten days ago with just some mild discomfort in on my right side and it seems to be getting worse over the last couple of days espec …
```

**Reference note**

```
CHIEF COMPLAINT

Abdominal pain.

MEDICAL HISTORY

Patient reports history of chronic migraines and hypertension.

SOCIAL HISTORY

Patient reports enjoyment in traveling and notes that she has not had any big trips since visiting Europe last summer.

MEDICATIONS

Patient reports use of Excedrin Migraine when needed and occasionally sumatriptan. She also takes lisinopril 20 mg per day.

REVIEW OF SYSTEMS

Constitutional: Reports fatigue, chills, and decreased appetite. Denies fever.
Gastrointestinal: Reports abdominal pain, nausea, and heartburn. Denies vomiting, diarrhea, and hematochezia.
Genitourinary: Denies dysuria and hematuria.

VITALS

Blood pressure is slightly elevated.

PHYSICAL EXAM

Respiratory
- Auscultation of Lungs: No wheezes, rales, or rhonchi.
Cardiovascular

Cardiovascular
- Auscultation of Heart: Grade 3 out of 6 systolic ejection murmur, unchanged from prior exam.
Ga …
```

**Generated note**

```
CHIEF COMPLAINT:

The patient is a 34-year-old G2P1 Caucasian female presents with chief complaint of "abdominal pain" which she states began approximately 10 days ago starting off mildly on her right-sided area worsening over time. She denies any hematemesis melena dysuria frequency urgency nocturia constipation diarrhea weight loss fatigue arthralgias joint pains muscle weakness chest pain shortness of breath orthostatic changes syncope visual disturbances hearing difficulties diplopia vertigo tinnitus headache dizziness photophobia phonophobia scintillations flashing lights paresthesias numbness tingling burning sensation temperature changes cold intolerance heat intolerance night sweats hot flashes menorrhagia irregular menses galactorrhea oligomenorrhea amenorrhea breast tenderness nipple discharge thyroid nodules thyromegaly tremors shakiness gait difficulty balance problems coordination problems memory lapses confusion depression anxiety mood swings irritability insomnia hypersomnia excessive daytime somnolence hypersonnia bruxism teeth grinding jaw claudication temporomandibu …
```

- unsupported entities (vs. transcript): ammonia level, anxiety, blood glucose, blood in stool, breast pain, bruising, burning sensation, chest pain, coagulation studies, cold intolerance, confusion, constipation, cortisol level, cough, cramping, creatinine, crepitus, crp, cyanosis, d-dimer
- incorrect diagnosis: anxiety, depression, intracranial hemorrhage, neuropathy, peripheral artery disease, sinusitis, thyroid nodule  ·  missing diagnosis: cholecystitis, hypertension, migraine
- incorrect medication: folic acid, insulin, iron supplement, vitamin b12  ·  missing medication: lisinopril, sumatriptan
- dosage mismatch: —
- negation flips (vs. reference): fatigue, wheezing
- unsupported numbers: —
- missing information: {"symptom": ["chills", "crackles", "fever", "heartburn", "hematuria", "loss of appetite"], "medical_history": ["hypertension", "migraine"], "diagnosis": ["cholecystitis", "stroke"], "medication": ["lisinopril", "sumatriptan"], "investigation": ["blood pressure measurement", "complete blood count", "pregnancy test", "ultrasound", "urinalysis"]}

## Incorrect diagnosis example: `aci_bench_test_taskC_3_D2N176-virtassist`

*incorrect diagnosis example*

ROUGE-L 7.0 · length ratio 1.41 · truncated True · degenerate True · hallucination 94.9 · negation-flip 20.0 · numerical consistency 100.0 · coverage 35.3

**Transcript (excerpt)**

```
[doctor] hi , alexander . how are you ?
[patient] i'm doing really well . thank you .
[doctor] so , i know the nurse told you a little bit about dax . i'd like to tell dax about you . okay ?
[patient] sure .
[doctor] so , alexander is a 62-year-old male , with a past medical history significant for reflux , who presents for follow-up of his chronic problems .
[doctor] so , alexander , what's being going on ?
[patient] well , i am so thankful you put me on that medicine for my , my reflux .
[doctor] the protonix ?
[patient] the protonix . that , i had , w- made an amazing change in my life .
[doctor] yeah .
[patient] i'm really comfortable now . i eat whatever i want , and i feel so much bett …
```

**Reference note**

```
CHIEF COMPLAINT

Follow-up chronic problems.

HISTORY OF PRESENT ILLNESS

Alexander Myers is a 62-year-old male with a past medical history significant for reflux who presents for follow-up of his chronic problems.

In regards to his reflux, he reports that he has continued to utilize Protonix 40 mg daily. He states this has helped a lot and he is really comfortable. The patient is doing really well with his diet. He reports that he has discontinued drinking energy drinks and is now drinking green tea. The patient states this change has also helped reduce his side effects.

He notes that his reflux being improved has helped his mood. The patient has a good support system at home and all of his children call to check on him daily. He also notes his job is going well.

The patient denies chest pain, shortness of breath, abdominal pain, nausea, and vomiting.

REVIEW OF SYSTEMS

• Cardiovasc …
```

**Generated note**

```
CHIEF COMPLAINT

Alexander is a 62 y/o M with GERD, status post treatment with Protonix, comes in today for routine followup.

HISTORY OF PRESENT ILLNESS

The patient states he has been feeling very well since starting Protonix. He denies any dysphagia, odynophagia, regurgitation, weight loss, hematemesis, melena, abdominal pain, fever, chills, night sweats, fatigue, weakness, palpitations, orthopnea, paroxysmal nocturnal dyspnea, PND, pleuritic chest pain, cough, sputum production, wheezing, hoarseness, sore throat, dental complaints, earache, headache, photophobia, visual changes, diplopia, syncope, tremors, muscle spasms, joint pains, arthralgias, rash, pruritus, itching, urticaria, hives, angioedema, conjunctivitis, epistaxis, rhinorrhea, sinusitis, nasal congestion, sneezing, lacrimation, tearing, eye redness, blurred vision, decreased hearing, tinnitus, vertigo, lightheadedness, fainting spells, gait disturbances, balance difficulties, numbness, tingling sensation, burning sensations, cold intolerance, heat intolerance, thyroid nodules, galactorrhoea, amenorrheal, irregular men …
```

- unsupported entities (vs. transcript): abscess, anal fissure, angioedema, appendicitis, arrhythmia, arthritis, asthma, atrial fibrillation, bloating, blood in stool, blurred vision, bruising, bundle branch block, burning sensation, cancer, celiac disease, chills, cholecystitis, cirrhosis, cold intolerance
- incorrect diagnosis: abscess, anal fissure, angioedema, appendicitis, arrhythmia, arthritis, asthma, atrial fibrillation, bundle branch block, cholecystitis, cirrhosis, conjunctivitis, copd, deep vein thrombosis, dementia, diabetes, diverticulitis, gastroenteritis, gerd, glomerulonephritis, hepatitis, hernia, hydronephrosis, hypertension, hypoglycemia, inflammatory bowel disease, intracranial hemorrhage, irritable bowel syndrome, kidney stones, kidney transplant, lung cancer, lupus, meningitis, mitral regurgitation, multiple sclerosis, neuropathy, pancreatitis, parkinson's disease, peptic ulcer disease, pleural effusion, pneumonia, pneumothorax, raynaud's phenomenon, rheumatoid arthritis, sepsis, sinusitis, thyroid nodule, tuberculosis, urinary tract infection, varicose veins, vasculitis  ·  missing diagnosis: —
- incorrect medication: —  ·  missing medication: —
- dosage mismatch: —
- negation flips (vs. reference): abdominal pain
- unsupported numbers: —
- missing information: {"symptom": ["crackles", "dyspnea", "dyspnea on exertion", "heartburn", "murmur", "nausea"], "diagnosis": ["adverse drug reaction", "gastritis"], "investigation": ["endoscopy"]}

## Incorrect medication / dosage example: `aci_bench_test_taskC_3_D2N190-aci`

*incorrect medication / dosage example*

ROUGE-L 7.1 · length ratio 0.96 · truncated True · degenerate True · hallucination 94.6 · negation-flip 16.7 · numerical consistency 100.0 · coverage 42.9

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
CHIEF COMPLAINT:

The patient presents to clinic today for evaluation of right knee pain following trauma approximately two weeks prior.

HISTORY OF PRESENT ILLNESS:

She states that she had fallen onto her right knee during bicycle accident. She denies any previous history of similar complaints. The patient denies any fever, chills, recent travel, sick contacts, allergies, medications, tobacco use, alcohol abuse, etc.
Review of Systems:

Significant for right lower extremity pain. No fevers, chills, weight loss, fatigue, weakness, arthralgia, dysuria, hematuria, abdominal pain, nausea, vomiting, diarrhea, constipation, headache, visual changes, hearing changes, palpitations, syncope, chest pain, orthopnea, paroxysmal nocturnal dyspnea, PND, edema, rash, pruritus, urticaria, wheezes, cough, sputum production, pleural effusion, pericarditis, arthritis, arthropathy, osteoarthritis, fibromyalgia, lupus, rheumatoid arthritis, scleroderma, Raynaud phenomenon, SLE, vasculitis, erythema nodosum, psoriasis, eczema, asthma, bronchospasm, COPD, emphysema, pneumonia, sinusitis, otalgia, vertigo …
```

- unsupported entities (vs. transcript): abdominal pain, acetaminophen, allergic rhinitis, alprazolam, anxiety, anxiety symptoms, aripiprazole, arthritis, aspirin, asthma, blurred vision, burning sensation, buspirone, celecoxib, chest pain, chills, citalopram, clonazepam, codeine, cold intolerance
- incorrect diagnosis: —  ·  missing diagnosis: sprain
- incorrect medication: acetaminophen, alprazolam, aripiprazole, aspirin, buspirone, celecoxib, citalopram, clonazepam, codeine, diazepam, diclofenac, duloxetine, escitalopram, fentanyl, fluoxetine, glipizide, glyburide, hydrocodone, hydromorphone, indomethacin, insulin, lorazepam, meloxicam, metformin, morphine, naproxen, olanzapine, oxycodone, pioglitazone, quetiapine, risperidone, sertraline, sitagliptin, tramadol, venlafaxine, zolpidem  ·  missing medication: —
- dosage mismatch: —
- negation flips (vs. reference): edema
- unsupported numbers: —
- missing information: {"symptom": ["crepitus", "laceration"], "diagnosis": ["dislocation", "fracture", "sprain"], "investigation": ["mri", "physical examination", "x-ray"]}

## Negation error example: `aci_bench_test_taskC_3_D2N196-aci`

*negation error example*

ROUGE-L 10.6 · length ratio 1.09 · truncated False · degenerate False · hallucination 59.0 · negation-flip 38.9 · numerical consistency 38.5 · coverage 79.3

**Transcript (excerpt)**

```
[doctor] mister thompson is a 67 -year-old male with a history of essential hypertension hyperlipidemia and osteoarthritis who is here today with elevated and fluctuating blood pressures so hi there mister thompson it's nice to see you again listen i understand you're having some trouble with your blood pressure control i would like to discuss that with you but first i want to ask you i'd like to use this app this new fancy app that's gon na help me focus on you a bit more in our conversation would that be okay with you
[patient] yes that's fine
[doctor] okay great it's gon na record our conversation okay perfect so jerry tell me mister thompson tell me about your blood pressure readings rec …
```

**Reference note**

```
CHIEF COMPLAINT

Elevated and fluctuating blood pressures.

MEDICAL HISTORY

Patient reports history of essential hypertension, hyperlipidemia, and osteoarthritis.

SOCIAL HISTORY

Patient reports he enjoys playing golf.

MEDICATIONS

Patient reports he is taking lisinopril 20 mg twice per day, atorvastatin, and occasional Tylenol.

REVIEW OF SYSTEMS

Constitutional: Denies fever.
Cardiovascular: Reports heaviness in chest. Denies heart palpitations or syncope.
Respiratory: Denies dyspnea.
Gastrointestinal: Denies nausea, vomiting, or diarrhea.
Neurological: Reports headache and lightheadedness. Denies syncope.

PHYSICAL EXAM

Respiratory
- Auscultation of Lungs: Mild bibasilar rales, but no wheezes or rhonchi. Excellent air movement.

Cardiovascular
- Auscultation of Heart: Grade 3 out of 6 systolic ejection murmur, unchanged from prior.

Musculoskeletal
- Examination: Trace lower extre …
```

**Generated note**

```
CHIEF COMPLAINT:

The patient is a 67-year-old white male presents with complaints of recent elevation of blood pressure.

HISTORY OF PRESENT ILLNESS:

Mr. Thompson is a 67-year old white male who comes into clinic complaining of recent elevation of blood pressures. He states that his blood pressure has been "up" lately and has noted occasional syncope, dyspnea, orthostatic hypotension, and left-sided pleuritic type chest discomfort. The patient denies fevers chills night sweats weight loss fatigue malaise arthralgias joint pains muscle weakness shortness of breath hemoptysis sputum production cough productive cough productive sputum purulent sputum bloody sputum hematuria nocturia frequency urgency hesitancy decreased urine output flank pain costovertebral angle tenderness abdominal pain nausea vomiting diarrhea constipation pruritus itching erythematous rash petechiae ecchymosis bruising bleeding gums easy bruisability melena hematemesis palpitation tachycardia extrasystoles atrial fibrillation flutter supraventricular tachycardia ventricular ectopic beats ventricular arrhythmias a …
```

- unsupported entities (vs. transcript): abdominal pain, angina, arrhythmia, atrial fibrillation, bleeding, blood in stool, bruising, chills, constipation, cough, diagnostic workup, electrocardiogram, erythema, fatigue, heartburn, hematuria, hemoptysis, ibuprofen, imaging, itching
- incorrect diagnosis: myocardial infarction, pulmonary embolism  ·  missing diagnosis: dehydration
- incorrect medication: ibuprofen  ·  missing medication: hydrochlorothiazide
- dosage mismatch: —
- negation flips (vs. reference): diarrhea, dyspnea, nausea, pain, rhonchi, syncope, vomiting
- unsupported numbers: 0, 18, 180, 180/90, 40, 72, 90, 98
- missing information: {"symptom": ["edema", "headache", "palpitations"], "diagnosis": ["dehydration"], "medication": ["hydrochlorothiazide"], "investigation": ["physical examination"]}

## Numerical error example: `aci_bench_test_taskC_3_D2N185-virtscribe`

*numerical error example*

ROUGE-L 12.7 · length ratio 0.67 · truncated False · degenerate False · hallucination 83.3 · negation-flip 25.0 · numerical consistency 20.0 · coverage 46.7

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
CHIEF COMPLAINT

Abnormal Renal Ultrasound with Atrophy Right Kidney.

HISTORY OF PRESENT ILLNESS

The patient Ashley James is a 14-year-old female who comes in for further evaluation of abdominal pain and vomiting. She states that she has had intermittent episodes of nausea and vomiting for several weeks. The patient denies dysuria, frequency, urgency, hematuria, flank pain, or gross hematuria. No recent travel or contact with anyone ill. Denies tobacco, alcohol, illicit drug use. Family History positive for renal disease including mother, maternal grandmother, paternal uncle, and cousin.
She has had previous evaluations by pediatrician and gastroenterologist without findings suggestive of appendicitis or inflammatory bowel disease. Her vital signs include BP 110/70 mm Hg; HR 80 bpm; RR 16/min; Temp 98.2°F (36.8°C). Physical examination shows generalized tenderness in abdomen, negative costovertebral angle tenderness bilaterally, negative Murphy sign, and negative Cullen sign. Abdomen soft, mobile, nondistended. Lungs clear to auscultation bilaterally. HEENT examination reveals conj …
```

- unsupported entities (vs. transcript): abdominal pain, appendicitis, bloating, bruising, chest pain, chills, constipation, cough, crackles, creatinine, crp, diagnostic workup, diarrhea, dyspnea, dysuria, esr, hematuria, hydronephrosis, imaging, inflammatory bowel disease
- incorrect diagnosis: urinary tract infection  ·  missing diagnosis: hypertension, infection, proteinuria
- incorrect medication: —  ·  missing medication: acetaminophen, famotidine, loratadine
- dosage mismatch: —
- negation flips (vs. reference): fever, hematuria
- unsupported numbers: 1010, 110, 110/70, 15, 16, 18, 20, 24, 25, 30, 36.8, 5.5, 7, 70, 80
- missing information: {"symptom": ["burning sensation", "edema"], "medical_history": ["allergic rhinitis", "hypertension", "kidney transplant", "myocardial infarction", "neuropathy", "type 2 diabetes"], "diagnosis": ["infection", "proteinuria", "sebaceous cyst"], "medication": ["acetaminophen", "famotidine", "loratadine"], "investigation": ["ct scan", "metabolic panel"]}

## Missing information example: `aci_bench_test_taskC_3_D2N175-virtassist`

*missing information example*

ROUGE-L 9.0 · length ratio 0.75 · truncated True · degenerate False · hallucination 90.9 · negation-flip 0.0 · numerical consistency 50.0 · coverage 18.8

**Transcript (excerpt)**

```
[doctor] hi , natalie . how are you ?
[patient] good . how are you ?
[doctor] it's good to see you .
[patient] good to see you , too .
[doctor] i know my nurse has already told you about dax . is it okay if i tell dax a little bit about you ?
[patient] go for it .
[doctor] all right . so , natalie is a 39-year-old female , here today for a check-up for an abnormal lab . she's got a history of high blood pressure , diabetes , and acl repair .
[doctor] so , tell me what's going on .
[patient] so , uh , i got some re- routine blood work done last week and , uh , they said that my blood sugars were , were high , so that i should come in , um , and talk to you and get some more work done and , an …
```

**Reference note**

```
CHIEF COMPLAINT

Check up for abnormal labs.

HISTORY OF PRESENT ILLNESS

Natalie Price is a 39-year-old female here today for a check up for an abnormal labs. She has a history of high blood pressure, diabetes type 2, and right ACL repair.

The patient states she had routine blood work done last week and they said her blood sugars were high. She was instructed to follow up to get some more work done. She denies having any symptoms.

Regarding her diabetes, her diet has been really great lately. She has been avoiding sugars and watching her weight. The patient is power walking 30 minutes every day. She is checking her blood sugars every morning. The patient has continued to utilize metformin 1000 mg a day, which was increased at her last visit.

She states her high blood pressure has been stable with lisinopril. The patient has a cuff at home to measure her blood pressure herself.

Regar …
```

**Generated note**

```
CHIEF COMPLAINT:

The patient is a 39 y/o F who comes in for evaluation of her DM and HTN.

HISTORY OF PRESENT ILLNESS:

This is a 39 y.o.f. who presents for evaluation of her type II diabetes mellitus (DM) and hypertension (HTN). She states that she has not noticed any dysuria, frequency, urgency, nocturia, abdominal pain, fever chills, recent travel, sick contacts, etc. The patient denies any ortho complaints related to her R knee status post ACL reconstruction. No allergies noted.
She does take Metformin 500 mg BID PRN for her DM. Her Hb A1C is currently elevated at 8.1%. She takes Lisinopril daily for her HTN. Denies any CVA/TIA/MI/PVD/DVT/COPD/EPI/LBNE/IHD/Atrial fibrillation/Hypothyroidism/GI problems/Neurological disorders/Musculoskeletal disorder/Skin conditions/Joint pains/Rheumatoid arthritis/Osteoporosis/Urology problems/Family History of Diabetes/Hypertension/Cardiovascular disease/Stroke/Kidney stones/History of Cancer/Allergies/Recent surgeries/Infections/Vaccinations/Immunizations/Previous hospital admissions/previous surgical procedures/ previous trauma/previous illne …
```

- unsupported entities (vs. transcript): allergic rhinitis, anxiety, anxiety symptoms, atrial fibrillation, cancer, chickenpox, chills, colon polyps, copd, deep vein thrombosis, depression, drug allergy, dysmenorrhea, dysuria, eating disorder, endometriosis, eye exam, fever, fungal infection, hearing loss
- incorrect diagnosis: cancer, colon polyps, endometriosis, fungal infection, hepatitis, polycystic ovary syndrome, prostatitis, sexually transmitted infection, uterine fibroids, wart  ·  missing diagnosis: —
- incorrect medication: vaccine  ·  missing medication: empagliflozin
- dosage mismatch: [{"drug": "metformin", "predicted": "500 mg", "source": ["1.000 milligrams", "1000 mg"]}]
- negation flips (vs. reference): —
- unsupported numbers: 500, 9
- missing information: {"symptom": ["burning sensation", "chest pain", "crackles", "diarrhea", "dyspnea", "dyspnea on exertion"], "diagnosis": ["diabetes"], "medication": ["empagliflozin"], "investigation": ["blood glucose", "blood pressure measurement", "blood work", "complete blood count", "diagnostic workup", "lipid panel"]}

## Degenerate output example: `aci_bench_test_taskC_3_D2N199-aci`

*degenerate output example*

ROUGE-L 4.6 · length ratio 0.90 · truncated True · degenerate True · hallucination 91.2 · negation-flip 0.0 · numerical consistency 100.0 · coverage 25.7

**Transcript (excerpt)**

```
[doctor] hi billy how are you doing the medical assistant told me that you have a cough today
[patient] yep i'm doing pretty good you know cough started about a week ago or so you know i just started bringing up some yellow stuff and not feeling the greatest the last two days though
[doctor] okay alright so the cough started a week ago but you have have started feeling worse over the last two days correct
[patient] yep
[doctor] okay
[patient] yep
[doctor] alright now have you had any fevers
[patient] not that i remember i i feel warm but never really took my temperature
[doctor] you feel warm okay alright any chills
[patient] no no chills you know just a little achy at times
[doctor] okay an …
```

**Reference note**

```
CHIEF COMPLAINT

Cough.

MEDICAL HISTORY

Patient reports history of hypertension and diabetes.

SOCIAL HISTORY

Patient reports that he is a teacher.

MEDICATIONS

Patient reports taking lisinopril 20 mg daily and metformin 1000 mg twice a day.

REVIEW OF SYSTEMS

Constitutional: Reports "feeling warm". Denies chills.
HENT: Reports nasal congestion, sore throat, and sinus pressure.
Respiratory: Reports productive cough with yellow sputum. Denies dyspnea.
Musculoskeletal: Reports body aches and right knee pain. Denies right knee instability.

VITALS

Temperature is 98.4 today.
BP: 125/62.
Heart rate is nice and slow in the 80s.
SpO2 is 97% on room air.

PHYSICAL EXAM

Head and Face
- Examination: Pain to palpation to the bilateral maxillary sinuses.

Ears, Nose, Mouth, and Throat
- Examination of Nose: Erythema and edema of the nasal turbinates bilaterally with associated yellow discharg …
```

**Generated note**

```
CHIEF COMPLAINT:

The patient comes into clinic complaining of cough productive of yellow sputum for approximately one week duration worsening over the last two days.  He denies having febrile illness, chills, dyspnea, pleuritic chest pain, arthralgias, conjunctivitis, headache, photophobia, stiff neck, diarrhea, abdominal pain, nausea, vomiting, urinary frequency, urgency, nocturia, flank pain, joint swelling, rash, pruritus, wheezes, stridor, hoarseness, odynophagia, dysphonia, epistaxis, diplopia, blurred vision, ptosis, syncope, orthostatic hypotension, weakness, fatigue, tremors, muscle spasms, numbness, tingling, paresthesias, gait disturbances, balance difficulties, hearing loss, tinnitus, vertigo, ear fullness, foul odor, taste changes, weight gain, weight loss, night sweats, heat intolerance, thyroid nodules, galactorrhea, irregular menses, hirsutism, acne, alopecia, hyperpigmentation, vitiligo, purpuric lesions, petechiae, bruising easily, easy bleeding, gum hypertrophy, dental caries, dry mouth, excessive salivation, metallic taste, bitter taste, sweet taste, sour taste, b …
```

- unsupported entities (vs. transcript): abdominal pain, abscess, acne, anxiety, arthritis, back pain, benign prostatic hyperplasia, bleeding, blood in stool, blurred vision, breast pain, burning sensation, cancer, cellulitis, chest pain, cholecystitis, cirrhosis, confusion, conjunctivitis, constipation
- incorrect diagnosis: abscess, acne, anxiety, arthritis, cancer, cellulitis, cholecystitis, cirrhosis, deep vein thrombosis, dental caries, depression, diabetic retinopathy, diverticulitis, endometriosis, fracture, gastritis, gastroenteritis, gerd, glaucoma, hernia, ingrown toenail, irritable bowel syndrome, kidney stones, macular degeneration, neuropathy, optic neuritis, osteoporosis, ovarian cyst, pancreatitis, peptic ulcer disease, plantar fasciitis, pregnancy, raynaud's phenomenon, restless legs syndrome, schizophrenia, sciatica, sepsis, sleep apnea, sprain, thyroid nodule, urinary tract infection, uterine fibroids, uveitis, vasculitis  ·  missing diagnosis: bronchitis, diabetes, hypertension, strain, upper respiratory infection
- incorrect medication: —  ·  missing medication: guaifenesin, lisinopril, meloxicam, metformin
- dosage mismatch: —
- negation flips (vs. reference): —
- unsupported numbers: —
- missing information: {"symptom": ["knee pain", "lymphadenopathy", "murmur", "muscle pain", "nasal congestion", "rhonchi"], "medical_history": ["diabetes", "hypertension"], "diagnosis": ["bronchitis", "strain", "upper respiratory infection"], "medication": ["guaifenesin", "lisinopril", "meloxicam", "metformin"], "investigation": ["blood glucose", "blood pressure measurement", "blood work", "continuous glucose monitor", "heart rate measurement", "hemoglobin a1c"]}

# Split: mts_dialog_test_chat_2023

## Best ROUGE-L: `mts_dialog_test_chat_2023_182`

*highest ROUGE-L in the split*

ROUGE-L 100.0 · length ratio 1.00 · truncated False · degenerate False · hallucination 0.0 · negation-flip 0.0 · numerical consistency — · coverage 100.0

**Transcript (excerpt)**

```
Guest_clinician: Does the patient have any drug allergies? 
Doctor: None that I'm aware of. Let me check his chart again to confirm.  
Guest_clinician: Thanks. 
Doctor: Yeah, it looks like he's not allergic to anything.
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

## Hallucination example: `mts_dialog_test_chat_2023_168`

*hallucination example*

ROUGE-L 19.6 · length ratio 0.97 · truncated False · degenerate False · hallucination 73.3 · negation-flip 14.3 · numerical consistency 62.5 · coverage 66.7

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
The patient is seen today as per her appointment.  She has been on Macrobid for approximately one week now.  The patient states she developed an allergic reaction including pruritus and erythema while on the medication.  She denies dysuria, hematuria, frequency, urgency, nocturia, febrile illness, or flank pain.  Her urinary habits have not changed significantly except for increased frequency which seems to be improving with Kegel exercises.  She does deny any history of hydronephrosis, kidney stone disease, or mass noted by previous ultrasounds done on 08/05/2008.  She also admits to past episodes of cystitis due to Escherichia coli infection in 11/07, 5/08, and 7/08.
```

- unsupported entities (vs. transcript): abdominal pain, drug allergy, erythema, hematuria, hydronephrosis, infection, itching, kidney stones, nocturia, urinary tract infection, urinary urgency
- incorrect diagnosis: infection, urinary tract infection  ·  missing diagnosis: —
- incorrect medication: —  ·  missing medication: —
- dosage mismatch: —
- negation flips (vs. reference): nocturia
- unsupported numbers: 08/05, 11, 11/07
- missing information: {"symptom": ["chills", "rash", "urinary incontinence"], "investigation": ["urine culture"]}

## Incorrect diagnosis example: `mts_dialog_test_chat_2023_93`

*incorrect diagnosis example*

ROUGE-L 1.9 · length ratio 25.06 · truncated True · degenerate True · hallucination 98.2 · negation-flip 100.0 · numerical consistency — · coverage 33.3

**Transcript (excerpt)**

```
Doctor: So, tell me any chest pain or shortness of breath?
Patient: No, none of those.
Doctor: Any bleeding disorder, prolonged bleeding or anything?
Patient: No.
Doctor: And I already have G I and urinary tract reports. Anything else?
Patient: No, I don't think so.
```

**Reference note**

```
CARDIAC:  He denies any chest pain or shortness of breath. ENDOCRINE:  He denies any bleeding disorders.
```

**Generated note**

```
Significant for negative history of GI bleed, URI, hemoptysis, dyspnea on exertion, orthopnea, PND, palpitations, syncope, abdominal tenderness, GU symptoms, joint pains, muscle weakness, visual changes, hearing loss, neurological deficits, skin rashes, fever chills, weight change, fatigue, arthralgias, myalgia, headache, photophobia, diplopia, vertigo, tinnitus, tremors, ataxia, numbness, tingling, paresthesias, edema, purpura, petechiae, bruising, easy bleeding, melena, hematemesis, diarrhea, constipation, nausea, vomiting, epigastric burning, right upper quadrant pain, left upper quadrant pain, flank pain, costovertebral angle tenderness, backache, neck stiffness, shoulder tip pain, pleuritic chest pain, periorbital puffiness, facial swelling, pedal edema, ankle edema, calf cramps, nocturia, oliguria, polyuria, frequency, urgency, hesitancy, dysuria, hematuria, gross hematuria, microscopic hematuria, renal colic, nephrolithiasis, hypertension, hypotension, hyperglycemia, hypoglycemia, thyroid nodules, goiter, heat intolerance, cold intolerance, menorrhagia, metrorrhagia, irregular …
```

- unsupported entities (vs. transcript): abdominal pain, abdominal tenderness, acne, adrenal insufficiency, angina, appendicitis, arrhythmia, asthma, atrial fibrillation, back pain, bell's palsy, blood in stool, blurred vision, bradycardia, bruising, bundle branch block, burning sensation, cancer, carpal tunnel syndrome, chills
- incorrect diagnosis: acne, adrenal insufficiency, angina, appendicitis, arrhythmia, atrial fibrillation, bell's palsy, bundle branch block, cancer, carpal tunnel syndrome, cholecystitis, cirrhosis, cushing's syndrome, deep vein thrombosis, diabetes, dislocation, diverticulitis, eczema, endocarditis, gastritis, heart failure, hernia, hypertension, hyperthyroidism, hypoglycemia, hypothyroidism, inflammatory bowel disease, kidney stones, lipoma, lupus, mitral regurgitation, myocardial infarction, neuropathy, pancreatitis, peptic ulcer disease, pericarditis, peripheral artery disease, plantar fasciitis, psoriasis, pulmonary embolism, raynaud's phenomenon, rheumatoid arthritis, scoliosis, tendinitis, thyroid nodule, tuberculosis, vertigo disorder  ·  missing diagnosis: —
- incorrect medication: —  ·  missing medication: —
- dosage mismatch: —
- negation flips (vs. reference): chest pain
- unsupported numbers: —
- missing information: {"symptom": ["dyspnea"], "diagnosis": ["bleeding disorder"]}

## Incorrect medication / dosage example: `mts_dialog_test_chat_2023_61`

*incorrect medication / dosage example*

ROUGE-L 13.3 · length ratio 0.56 · truncated False · degenerate False · hallucination 50.0 · negation-flip 0.0 · numerical consistency — · coverage 100.0

**Transcript (excerpt)**

```
Doctor: What are your current medications?
Patient: None, except the Amoxil and Aldex that I started on Monday.
```

**Reference note**

```
None except the Amoxil and Aldex started on Monday.
```

**Generated note**

```
Amoxicillin (Aldex) and ampicillin/sulbactam (Amoxil).
```

- unsupported entities (vs. transcript): ampicillin
- incorrect diagnosis: —  ·  missing diagnosis: —
- incorrect medication: ampicillin  ·  missing medication: —
- dosage mismatch: —
- negation flips (vs. reference): —
- unsupported numbers: —
- missing information: {}

## Negation error example: `mts_dialog_test_chat_2023_95`

*negation error example*

ROUGE-L 7.5 · length ratio 3.13 · truncated True · degenerate True · hallucination 90.4 · negation-flip 63.6 · numerical consistency 50.0 · coverage 84.6

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
The patient is an 85-year-old female who comes into the office complaining of right buttock pain.  She states that her pain started about two weeks ago.  The pain is described as "irritating" type of pain.  She denies dysuria, frequency, urgency, hematuria, fever chills, flank pain, abdominal pain, nausea, vomiting, diarrhea, weakness, syncope, orthostatic hypotension, palpitations, edema, weight loss, fatigue, arthralgias, joint swelling, pleuritic chest pain, coughing, sputum production, wheezes, rhonchi, stridor, hoarseness, odynophagia, dysphonia, dysarthria, diplopia, photophobia, visual changes, hearing loss, tinnitus, vertigo, ataxia, tremors, paresthesias, numbness, tingling, burning sensation, pruritus, erythromelalgia, nocturnal leg cramps, pedal edema, ankle edema, calf tenderness, knee effusion, shoulder tip pain, costovertebral angle tenderness, pelvic discomfort, vaginal discharge, itching, urinary retention, decreased libido, erectile dysfunction, impotence, testicular mass, penile curvature, prostatism, rectal bleeding, melena, hematochezia, change in bowel habits, fl …
```

- unsupported entities (vs. transcript): allergic rhinitis, anal fissure, angioedema, appendicitis, asthma, benign prostatic hyperplasia, bleeding, bloating, blood in stool, blurred vision, bruising, burning sensation, cancer, cataract, chills, cholecystitis, cirrhosis, colon cancer, colon polyps, conjunctivitis
- incorrect diagnosis: anal fissure, angioedema, appendicitis, benign prostatic hyperplasia, cancer, cholecystitis, cirrhosis, colon cancer, colon polyps, copd, diabetes, diverticulitis, eczema, endometriosis, fibromyalgia, gastritis, gastroenteritis, gerd, gout, hemorrhoids, hernia, hydronephrosis, hyperlipidemia, hyperthyroidism, hypothyroidism, infection, inflammatory bowel disease, interstitial cystitis, irritable bowel syndrome, kidney stones, lactose intolerance, osteoarthritis, ovarian cyst, overactive bladder, pancreatitis, peptic ulcer disease, pregnancy, prostate cancer, psoriasis, thrombocytopenia, thyroid nodule, urinary tract infection, uterine fibroids  ·  missing diagnosis: —
- incorrect medication: —  ·  missing medication: —
- dosage mismatch: —
- negation flips (vs. reference): abdominal pain, chest pain, constipation, diarrhea, dizziness, dyspnea, orthopnea
- unsupported numbers: 2
- missing information: {"diagnosis": ["adverse drug reaction"], "investigation": ["blood pressure measurement"]}

## Numerical error example: `mts_dialog_test_chat_2023_148`

*numerical error example*

ROUGE-L 8.2 · length ratio 0.52 · truncated False · degenerate False · hallucination — · negation-flip — · numerical consistency 0.0 · coverage —

**Transcript (excerpt)**

```
Doctor: How is your two week old newborn son doing today?
Guest_family: He's been doing very well. 
Doctor: Great, what brings you in for a visit today?
Guest_family: We just have a question about his foreskin. It's not a severe issue, but we are still concerned. 
Doctor: Other than the foreskin, which appears to not be out of the ordinary upon exam, does he have any other problems? 
Guest_family: No, not really, he's been doing pretty well.
```

**Reference note**

```
A 2-week-old who at this point has otherwise been doing well.  He has a relatively unremarkable foreskin.  At this point in time, he otherwise seems to be doing reasonably well.  The question is about the foreskin.  He otherwise has no other significant issues.  Severity low, ongoing since birth two weeks.  Thank you for allowing me to see this patient in consultation.
```

**Generated note**

```
The patient was born on 07/01/2002 and presented with concerns regarding his circumcision status at this time.  The rest of his examination including physical development and growth parameters were within normal limits.
```

- unsupported entities (vs. transcript): —
- incorrect diagnosis: —  ·  missing diagnosis: —
- incorrect medication: —  ·  missing medication: —
- dosage mismatch: —
- negation flips (vs. reference): —
- unsupported numbers: 07/01, 1, 2002, 7
- missing information: {}

## Missing information example: `mts_dialog_test_chat_2023_75`

*missing information example*

ROUGE-L 5.2 · length ratio 1.95 · truncated False · degenerate True · hallucination 100.0 · negation-flip — · numerical consistency — · coverage 0.0

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
The patient states that he has been feeling very well lately.  He denies chest pains, shortness of breath, palpitations, orthopnea, paroxysmal nocturnal dyspnea, edema, syncope, dizziness, weakness, fatigue, confusion, urinary frequency, urgency, hesitancy, retention, dysuria, hematuria, constipation, diarrhea, abdominal pain, nausea, vomiting, weight loss, fever, chills, night sweats, arthralgias, joint swelling, gait disturbances, visual changes, diplopia, hearing loss, tinnitus, vertigo, headache, photophobia, neck stiffness, backache, radiculopathy, paresthesias, tremors, muscle spasms, decreased strength, decreased reflexes, hyperreflexia, clonus, positive Babinski sign, positive Hoffman sign, positive Oppenheim sign, positive Romberg test, positive heel-toe walking, positive tandem walking, positive finger-to-nose testing, positive rapid alternating movements, positive pronator drift, positive grip strength, negative sensory level, negative motor level, negative deep tendon reflexes bilaterally, negative plantar response bilaterally, negative Hoffmann sign bilaterally, negative …
```

- unsupported entities (vs. transcript): abdominal pain, back pain, blurred vision, chest pain, chills, confusion, constipation, diarrhea, difficulty walking, dizziness, double vision, dyspnea, dysuria, edema, fatigue, fever, headache, hearing loss, hematuria, joint pain
- incorrect diagnosis: —  ·  missing diagnosis: —
- incorrect medication: —  ·  missing medication: acetaminophen
- dosage mismatch: —
- negation flips (vs. reference): —
- unsupported numbers: —
- missing information: {"symptom": ["falls", "pain", "urinary incontinence"], "medical_history": ["coronary artery disease", "diabetes", "heart failure", "hypoglycemia"], "medication": ["acetaminophen"]}

## Degenerate output example: `mts_dialog_test_chat_2023_95`

*degenerate output example*

ROUGE-L 7.5 · length ratio 3.13 · truncated True · degenerate True · hallucination 90.4 · negation-flip 63.6 · numerical consistency 50.0 · coverage 84.6

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
The patient is an 85-year-old female who comes into the office complaining of right buttock pain.  She states that her pain started about two weeks ago.  The pain is described as "irritating" type of pain.  She denies dysuria, frequency, urgency, hematuria, fever chills, flank pain, abdominal pain, nausea, vomiting, diarrhea, weakness, syncope, orthostatic hypotension, palpitations, edema, weight loss, fatigue, arthralgias, joint swelling, pleuritic chest pain, coughing, sputum production, wheezes, rhonchi, stridor, hoarseness, odynophagia, dysphonia, dysarthria, diplopia, photophobia, visual changes, hearing loss, tinnitus, vertigo, ataxia, tremors, paresthesias, numbness, tingling, burning sensation, pruritus, erythromelalgia, nocturnal leg cramps, pedal edema, ankle edema, calf tenderness, knee effusion, shoulder tip pain, costovertebral angle tenderness, pelvic discomfort, vaginal discharge, itching, urinary retention, decreased libido, erectile dysfunction, impotence, testicular mass, penile curvature, prostatism, rectal bleeding, melena, hematochezia, change in bowel habits, fl …
```

- unsupported entities (vs. transcript): allergic rhinitis, anal fissure, angioedema, appendicitis, asthma, benign prostatic hyperplasia, bleeding, bloating, blood in stool, blurred vision, bruising, burning sensation, cancer, cataract, chills, cholecystitis, cirrhosis, colon cancer, colon polyps, conjunctivitis
- incorrect diagnosis: anal fissure, angioedema, appendicitis, benign prostatic hyperplasia, cancer, cholecystitis, cirrhosis, colon cancer, colon polyps, copd, diabetes, diverticulitis, eczema, endometriosis, fibromyalgia, gastritis, gastroenteritis, gerd, gout, hemorrhoids, hernia, hydronephrosis, hyperlipidemia, hyperthyroidism, hypothyroidism, infection, inflammatory bowel disease, interstitial cystitis, irritable bowel syndrome, kidney stones, lactose intolerance, osteoarthritis, ovarian cyst, overactive bladder, pancreatitis, peptic ulcer disease, pregnancy, prostate cancer, psoriasis, thrombocytopenia, thyroid nodule, urinary tract infection, uterine fibroids  ·  missing diagnosis: —
- incorrect medication: —  ·  missing medication: —
- dosage mismatch: —
- negation flips (vs. reference): abdominal pain, chest pain, constipation, diarrhea, dizziness, dyspnea, orthopnea
- unsupported numbers: 2
- missing information: {"diagnosis": ["adverse drug reaction"], "investigation": ["blood pressure measurement"]}

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

ROUGE-L 0.0 · length ratio 2.00 · truncated False · degenerate False · hallucination 100.0 · negation-flip — · numerical consistency — · coverage —

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
No known drug or food allergy.
```

- unsupported entities (vs. transcript): drug allergy
- incorrect diagnosis: —  ·  missing diagnosis: —
- incorrect medication: —  ·  missing medication: —
- dosage mismatch: —
- negation flips (vs. reference): —
- unsupported numbers: —
- missing information: {}

## Hallucination example: `mts_dialog_test_sum_2023_69`

*hallucination example*

ROUGE-L 21.5 · length ratio 0.97 · truncated False · degenerate False · hallucination 90.9 · negation-flip 0.0 · numerical consistency — · coverage 16.7

**Transcript (excerpt)**

```
Doctor: Hi there! How are you today? 
Patient: Hello! I am hanging in there. 
Doctor: Do you remember me from our last visit? 
Patient: Yes! You are the doctor that comes to see me here. It is nice of you to come and see me here. 
Doctor: How do you like it here at the Nursing Home? 
Patient: I wish I didn't have to be here, but they are all very nice to me here. 
Doctor: That is good to hear. The nurses have been a bit concerned about you and have noticed some changes that they would like me to address. 
Patient: I fell. I lost my balance. 
Doctor: Do you remember when that was? 
Patient: When what was? 
Doctor: The fall. 
Patient: No. Not long ago. 
Guest_clinician: It was about a month ag …
```

**Reference note**

```
The patient was seen today by me at Nursing Home for her multiple medical problems.  The nurses report that she has been confused at times, having incontinent stool in the sink one time but generally she does not do that poorly.  She does have trouble walking which she attributes to weak legs.  She fell a couple of months ago.  Her eating has been fair.  She has been losing weight a little bit.  She denies diarrhea.  She does complain of feeling listless and unambitious and would like to try some Ensure.
```

**Generated note**

```
The patient is an elderly female who lives at home.  She states that her husband does for her as needed.  She denies smoking history.  Denies alcohol use.  She takes no medications by mouth.  Her allergies include penicillin.  She has a history of hypertension.  She has a significant history of falls.  She has difficulty ambulating without assistance.  She has urinary incontinence.  She has constipation.  She eats regular diet.  She has decreased appetite.  She has increased fatigue.  She has dysuria.  She has urgency.  She has frequency.  She has nocturia.
```

- unsupported entities (vs. transcript): allergic rhinitis, constipation, dysuria, fatigue, hypertension, loss of appetite, nocturia, penicillin, urinary incontinence, urinary urgency
- incorrect diagnosis: —  ·  missing diagnosis: —
- incorrect medication: penicillin  ·  missing medication: —
- dosage mismatch: —
- negation flips (vs. reference): —
- unsupported numbers: —
- missing information: {"symptom": ["confusion", "diarrhea", "difficulty walking", "weakness", "weight loss"]}

## Incorrect diagnosis example: `mts_dialog_test_sum_2023_117`

*incorrect diagnosis example*

ROUGE-L 6.3 · length ratio 2.47 · truncated True · degenerate True · hallucination 94.2 · negation-flip 62.5 · numerical consistency 50.0 · coverage 66.7

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
The patient is a 7-year-old Caucasian male who presents today with complaints of bilateral elbow and wrist pain as well as cervical spine tenderness.  The onset of these symptoms have been over the last couple of months.  The patient states that they were worse when she first started out, but then gradually got better.  She denies fever, chills, weight changes, abdominal pain, joint effusion, arthralgias, erythema, purpura, petechiae, oral lesions, dysuria, frequency, urgency, hematuria, photophobia, diplopia, headache, vomiting, diarrhea, constipation, pruritus, urticaria, wheezing, cough, sputum production, chest tightness, palpitations, syncope, orthopnea, paroxysmal nocturnal dyspnea, PND, edema, night sweats, fatigue, weakness, tremors, muscle spasms, numbness, tingling, paresthesias, gait disturbances, balance problems, hearing loss, vision change, confusion, memory loss, personality changes, mood swings, anxiety, depression, sleep disturbance, decreased libido, erectile dysfunction, urinary retention, impotence, testicular masses, penile discharge, urethritis, orchitis, epidid …
```

- unsupported entities (vs. transcript): abdominal pain, abscess, adhd, adrenal insufficiency, anal fissure, angioedema, anxiety, appendicitis, arrhythmia, asthma, autism, bradycardia, celiac disease, chemotherapy, chest pain, chills, cholecystitis, cirrhosis, confusion, constipation
- incorrect diagnosis: abscess, adhd, adrenal insufficiency, anal fissure, angioedema, anxiety, appendicitis, arrhythmia, asthma, autism, celiac disease, cholecystitis, cirrhosis, copd, deep vein thrombosis, depression, diabetes, dislocation, diverticulitis, eating disorder, eczema, esophagitis, gastritis, gout, hemorrhoids, hepatitis, hypertension, hypothyroidism, ingrown toenail, kidney cancer, kidney stones, lupus, menopause, multiple sclerosis, osteoporosis, pancreatitis, parkinson's disease, polymyalgia rheumatica, pregnancy, psoriasis, raynaud's phenomenon, rheumatoid arthritis, tobacco use, vasculitis, vertigo disorder  ·  missing diagnosis: —
- incorrect medication: chemotherapy, vaccine  ·  missing medication: loratadine
- dosage mismatch: —
- negation flips (vs. reference): abdominal pain, edema, fever, joint pain, peptic ulcer disease
- unsupported numbers: 1
- missing information: {"symptom": ["lymphadenopathy", "weight loss"], "diagnosis": ["allergic rhinitis"], "medication": ["loratadine"]}

## Incorrect medication / dosage example: `mts_dialog_test_sum_2023_31`

*incorrect medication / dosage example*

ROUGE-L 23.5 · length ratio 1.16 · truncated False · degenerate False · hallucination 27.8 · negation-flip 57.1 · numerical consistency 100.0 · coverage 87.5

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
The patient has been seen by Dr. XXXX.  The patient takes Nexium 40 mg daily for GERD; Cozaar 100 mg and Norvasc 10 mg daily for HTN; Allegra 180 mg daily for AR; Flovent PRN and Serevent PRN for asthma; no smoking history; his last episode was about a year ago; Xalatan eye drops for open angle glaucoma; Ativan 1mg at bedtime for insomnia; Advair 10 mcg inhaler twice daily for COPD; and Paxil 25 mg HS for depression/anxiety/sleep disturbance.
```

- unsupported entities (vs. transcript): artificial tears, asthma, copd, gerd, insomnia
- incorrect diagnosis: —  ·  missing diagnosis: —
- incorrect medication: artificial tears  ·  missing medication: —
- dosage mismatch: [{"drug": "fluticasone/salmeterol", "predicted": "10 mcg", "source": ["10 mg"]}]
- negation flips (vs. reference): anxiety, copd, depression, fluticasone/salmeterol, glaucoma, latanoprost, lorazepam, paroxetine
- unsupported numbers: —
- missing information: {"symptom": ["heartburn"], "diagnosis": ["allergic rhinitis"]}

## Negation error example: `mts_dialog_test_sum_2023_31`

*negation error example*

ROUGE-L 23.5 · length ratio 1.16 · truncated False · degenerate False · hallucination 27.8 · negation-flip 57.1 · numerical consistency 100.0 · coverage 87.5

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
The patient has been seen by Dr. XXXX.  The patient takes Nexium 40 mg daily for GERD; Cozaar 100 mg and Norvasc 10 mg daily for HTN; Allegra 180 mg daily for AR; Flovent PRN and Serevent PRN for asthma; no smoking history; his last episode was about a year ago; Xalatan eye drops for open angle glaucoma; Ativan 1mg at bedtime for insomnia; Advair 10 mcg inhaler twice daily for COPD; and Paxil 25 mg HS for depression/anxiety/sleep disturbance.
```

- unsupported entities (vs. transcript): artificial tears, asthma, copd, gerd, insomnia
- incorrect diagnosis: —  ·  missing diagnosis: —
- incorrect medication: artificial tears  ·  missing medication: —
- dosage mismatch: [{"drug": "fluticasone/salmeterol", "predicted": "10 mcg", "source": ["10 mg"]}]
- negation flips (vs. reference): anxiety, copd, depression, fluticasone/salmeterol, glaucoma, latanoprost, lorazepam, paroxetine
- unsupported numbers: —
- missing information: {"symptom": ["heartburn"], "diagnosis": ["allergic rhinitis"]}

## Numerical error example: `mts_dialog_test_sum_2023_2`

*numerical error example*

ROUGE-L 14.8 · length ratio 1.52 · truncated False · degenerate True · hallucination 89.7 · negation-flip 15.4 · numerical consistency 40.0 · coverage 60.9

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
This is a 51-year-old Caucasian male who has been seen by Dr. X on several occasions as part of his treatment plan for non-Hodgkin's lymphoma.  He presented initially in late 2007 with complaints of abdominal pain, significant weight loss, decreased appetite, and bilateral inguinal adenopathy.  The patient underwent diagnostic workup including CT scan of abdomen/pelvis, bone marrow aspiration/biopsy, and staging laparotomy which confirmed stage IIIA diffuse large cell lymphoma.  He received six courses of R-CHOP therapy without interruption except for a brief period due to severe neutropenia secondary to septicemia complicated by pneumonia.  His last course of chemotherapy was administered approximately four weeks ago.  He denies dyspnea, orthopnea, palpitations, syncope, hemoptysis, pleuritic chest pain, cough productive of sputum, fever, night sweats, arthralgia, joint swelling, rash, pruritus, edema, weakness, fatigue, diarrhea, constipation, nausea, vomiting, epigastric burning, regurgitation, odynophagia, hoarseness, stridor, wheezing, rhonchi, sinusitis, sore throat, conjunctiv …
```

- unsupported entities (vs. transcript): back pain, blurred vision, burning sensation, conjunctivitis, constipation, cough, ct scan, diagnostic workup, diarrhea, difficulty walking, double vision, dysphagia, dysuria, edema, erectile dysfunction, fatigue, fever, headache, hematuria, hemoptysis
- incorrect diagnosis: leukopenia, pneumonia  ·  missing diagnosis: kidney transplant, sepsis
- incorrect medication: —  ·  missing medication: prednisone, rituximab
- dosage mismatch: —
- negation flips (vs. reference): numbness, tingling
- unsupported numbers: 12, 4, 6
- missing information: {"symptom": ["confusion"], "diagnosis": ["cancer", "infection", "kidney transplant", "sepsis"], "medication": ["prednisone", "rituximab"], "investigation": ["clinical score", "pet scan"]}

## Missing information example: `mts_dialog_test_sum_2023_78`

*missing information example*

ROUGE-L 7.5 · length ratio 0.13 · truncated False · degenerate False · hallucination 100.0 · negation-flip — · numerical consistency — · coverage 0.0

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
Significant for generalized tonic-clonic seizures as described above.  Other systems were negative.
```

- unsupported entities (vs. transcript): seizure
- incorrect diagnosis: —  ·  missing diagnosis: —
- incorrect medication: —  ·  missing medication: —
- dosage mismatch: —
- negation flips (vs. reference): —
- unsupported numbers: —
- missing information: {"symptom": ["diarrhea", "fever", "nasal congestion", "rash", "sneezing", "vomiting"]}

## Degenerate output example: `mts_dialog_test_sum_2023_124`

*degenerate output example*

ROUGE-L 6.4 · length ratio 2.26 · truncated True · degenerate True · hallucination 93.3 · negation-flip 20.0 · numerical consistency 100.0 · coverage 55.6

**Transcript (excerpt)**

```
Doctor: Hello, Nurse. Who are we seeing today? 
Guest_clinician: She's a seventy seven year old African American female. 
Doctor: I see. Does she have any current medical problems? 
Guest_clinician: She does. She currently has C H F, which makes her oxygen dependent. She also has atrial fibrillation, diabetes mellitus, hypothyroidism, possible stroke, multiple joint disease including gout, arthritis, and both rheumatoid and D J D.
Doctor: Thank you. What is her complaint? 
Guest_clinician: She claims she's had dizziness for one month now. 
Doctor: Did you ask about any recent problems?
Guest_clinician: I did. She denied any recent fever, chills, earache, diplopia, dysarthria, dysphagia, othe …
```

**Reference note**

```
This is a 77-year-old African-American female with multiple medical problems including CHF (O2 dependent), atrial fibrillation, diabetes mellitus, hypothyroidism, possible stroke, multiple joint disease including gout, arthritis, both rheumatoid and DJD, who presents with a complaint of one month of dizziness.  She reports a rotational sensation upon arising from the bed or chair that lasts for several minutes and requires her to sit back down and stay in one place.  She gets similar symptoms when she rolls over in bed.  She is not able to describe what direction she feels like she is spinning.  At times, she also feels as though she is going to pass out.  These sensations stop if she just sits in one place or lies down for several minutes.  She does note that it is worse when she turns to the right and when she turns to the left.  She also complains that she gets similar sensations when …
```

**Generated note**

```
This is a 77-year-old black female who comes with complaints of vertigo for approximately one month duration.  She denies fevers, chills, headache, photopsias, visual changes, dysarthria, dysphasia, hearing loss, nausea, vomiting, syncope, weakness, paresthesias, tremors, arthralgias, palpitations, chest pain, shortness of breath, orthopnea, paroxysmal nocturnal dyspnea, edema, weight gain, abdominal pain, hematemesis, melena, diarrhea, constipation, urinary frequency, urgency, hesitancy, dysuria, flank pain, costovertebral angle tenderness, cough, sputum production, wheezing, stridor, hoarseness, odynophagia, sore throat, rhinitis, sinusitis, conjunctivitis, lacrimation, tearing, ptosis, blurred vision, eye redness, photophobia, diplopia, facial numbness, tongue deviation, drooling, aphonia, epistaxis, nasal congestion, sneezing, pruritus, rash, itching, urticaria, angioedema, erythematous skin lesions, petechiae, purpura, ecchymoses, bruising, swelling, warmth, redness, cellulites, lymphadenopathy, night sweats, fatigue, malaise, confusion, disorientation, memory loss, forgetfulnes …
```

- unsupported entities (vs. transcript): abdominal pain, abscess, acne, angioedema, ankle pain, anxiety, asthma, back pain, bleeding, bloating, blood in stool, blurred vision, breast pain, bruising, burning sensation, bursitis, calcium supplement, chest pain, colon polyps, confusion
- incorrect diagnosis: abscess, acne, angioedema, anxiety, bursitis, colon polyps, conjunctivitis, deep vein thrombosis, degenerative disc disease, dental caries, depression, eczema, endocarditis, endometriosis, fracture, fungal infection, ganglion cyst, heart failure, hernia, infection, lipoma, neuropathy, ovarian cyst, plantar fasciitis, polymyalgia rheumatica, pregnancy, psoriasis, pulmonary embolism, raynaud's phenomenon, scoliosis, sebaceous cyst, sinusitis, spinal stenosis, tendinitis, transient ischemic attack, uterine fibroids, vasculitis  ·  missing diagnosis: arthritis, gout, rheumatoid arthritis
- incorrect medication: calcium supplement  ·  missing medication: —
- dosage mismatch: —
- negation flips (vs. reference): double vision, dysphagia
- unsupported numbers: —
- missing information: {"symptom": ["ear pain", "tinnitus"], "medical_history": ["atrial fibrillation", "diabetes", "hypothyroidism"], "diagnosis": ["arthritis", "gout", "rheumatoid arthritis"]}

# Split: dialogue_soap_test

## Best ROUGE-L: `dialogue_soap_test_30`

*highest ROUGE-L in the split*

ROUGE-L 49.5 · length ratio 1.01 · truncated False · degenerate False · hallucination 20.8 · negation-flip 0.0 · numerical consistency 85.7 · coverage 82.6

**Transcript (excerpt)**

```
Doctor: Hello, how can I help you today?
Patient: Hi, I've been experiencing constant blurry vision in my left eye for about 6 weeks now.
Doctor: I see. Can you tell me about your past medical history?
Patient: Yeah, I have cystic fibrosis, which has led to insulin-dependent diabetes mellitus, chronic sinusitis, hypertension, iron deficiency anemia, and obstructive sleep apnea.
Doctor: Have you had any surgeries in the past?
Patient: I had sinus surgery about 7 months ago. It involved bilateral maxillary antrostomies, ethmoidectomies, sphenoidectomies, and frontal sinusotomies.
Doctor: Thank you for the information. What medications are you currently taking?
Patient: I'm taking albuterol, az …
```

**Reference note**

```
S: Patient reports constant blurry vision in the left eye for approximately 6 weeks. Medical history includes cystic fibrosis, insulin-dependent diabetes mellitus, chronic sinusitis, hypertension, iron deficiency anemia, and obstructive sleep apnea. Patient underwent sinus surgery 7 months ago and is currently on multiple medications including albuterol, azithromycin, itraconazole, insulin, lisinopril, pancreatic enzymes, and sulfamethoxazole-trimethoprim. Denies use of tobacco or drugs.
O: Visual acuity is 20/20 in both eyes. Intraocular pressure is 18 OD and 16 OS. Pupils are 4 mm and reactive bilaterally. Anterior eye exam unremarkable. Posterior exam of the left eye reveals intraretinal hemorrhages along the nerve fiber layer with retinal thickening in the inferior macula, consistent with branch retinal vein occlusion (BRVO). Optical coherence tomography shows mild intraretinal and t …
```

**Generated note**

```
S: Patient reports having blurred vision in her left eye for approximately six weeks. She denies using tobacco or illicit substances. Her significant past medical includes cystic fibrosis complicated by insulin dependent diabetes, chronic sinusitis, hypertension, iron deficient anemia, and obstructive sleep apnea. She underwent extensive sinus surgery seven months back including multiple sinuses. Medications include albuterol, azithromycin, itraconazole, insulin, lisinopril, pancreatic enzyme supplements, and sulfamethoxazole-trimethoprim.
O: Visual acuities were recorded as 20/20 bilaterally. Intraocular pressures measured 18mmHg OU. Pupil sizes were 4mm bilaterally and reacted normally. Anterior segment examination was within normal limits; however, fundus examination of the left eye revealed intraretinal hemorrhage and retinal thickening in the inferior macular region suggestive of branch retinal vein occlusion (BRVO). Optical Coherence Tomography indicated mild intraretinal edema and trace subfoveal fluid in the left eye. Fluorescein Angiography demonstrated delayed venous fillin …
```

- unsupported entities (vs. transcript): anemia, complete blood count, diabetic retinopathy, edema, iron supplement
- incorrect diagnosis: —  ·  missing diagnosis: —
- incorrect medication: iron supplement  ·  missing medication: —
- dosage mismatch: —
- negation flips (vs. reference): —
- unsupported numbers: 12, 145/70
- missing information: {"medical_history": ["iron deficiency anemia"], "investigation": ["cardiac catheterization", "coagulation studies", "physical examination"]}

## Worst ROUGE-L: `dialogue_soap_test_151`

*lowest ROUGE-L in the split*

ROUGE-L 6.0 · length ratio 1.73 · truncated True · degenerate True · hallucination 95.4 · negation-flip 0.0 · numerical consistency 100.0 · coverage 28.6

**Transcript (excerpt)**

```
Doctor: Hello, can you tell me why you were admitted to the hospital back in June 2016?
Patient: Yeah, I was admitted because of weakness in my right arm and problems with my speech, like slurring.
Doctor: I see. You were diagnosed with cerebral infarction in the left middle cerebral artery area and deep vein thrombosis. Your ECG demonstrated normal sinus rhythm and echocardiography revealed no intra-cardiac thrombus or vegetation. You were then discharged with a prescription for apixaban. Is that correct?
Patient: Yes, that's right.
Doctor: In August 2016, you were readmitted to the hospital due to recurrent right arm weakness and slurred speech. The MRI showed multiple cerebral infarctions …
```

**Reference note**

```
S: The patient reported initial symptoms of weakness in the right arm and slurred speech leading to a hospital admission in June 2016. The patient was diagnosed with cerebral infarction and deep vein thrombosis. Symptoms recurred in August 2016, including right arm weakness and slurred speech. The patient recalls being treated for suspected Trousseau's syndrome and potential infective endocarditis, followed by cardiac surgery for mitral valve vegetation.
O: Initial diagnosis was cerebral infarction in the left middle cerebral artery and deep vein thrombosis. MRI in August 2016 showed multiple cerebral infarctions in both cerebral hemispheres and the cerebellum. Echocardiography indicated mild mitral regurgitation with vegetation on the mitral valve. CT scan revealed left renal infarction and swollen lymph nodes suggestive of advanced gastric cancer or lymphoma. During cardiac surgery, a  …
```

**Generated note**

```
S: Patient reports being hospitalized initially in June 2016 for right-sided weakness and dysarthria. She has been previously diagnosed with left MCA territory stroke and DVT.  She is status post recent admission for recurrent R sided weakness and dysarthria, now also having suspicion of Trousseau’s Syndrome.  No history of fever, chills, night sweats, weight loss, fatigue, malaise, joint pain, rash, arthralgias, pleuritic chest pains, cough, sputum production, shortness of breath, orthopnea, paroxysmal nocturnal dyspnea, palpitations, syncope, near-syncope, dizziness, lightheadedness, vertigo, hearing changes, tinnitus, visual disturbances, diplopia, photophobia, headache, confusion, memory difficulties, difficulty swallowing, hoarseness, voice changes, numbness, tingling, paresthesias, muscle cramps, fasciculations, tremors, ataxia, gait disturbance, urinary frequency, urgency, hesitancy, retention, constipation, diarrhea, nausea, vomiting, epigastric burning, bloating, early satiety, jaundice, pruritus, dark urine, pale stools, edema, purpura, petechiae, bruising, bleeding gums, e …
```

- unsupported entities (vs. transcript): abscess, anal fissure, angioedema, appendicitis, arthritis, asthma, bleeding, bloating, blood in stool, blurred vision, brain tumor, bruising, burning sensation, chest pain, chills, cholecystitis, cirrhosis, confusion, conjunctivitis, constipation
- incorrect diagnosis: abscess, anal fissure, angioedema, appendicitis, arthritis, cholecystitis, cirrhosis, conjunctivitis, copd, dental caries, diverticulitis, drug allergy, fungal infection, gastritis, gastroenteritis, hernia, hypertension, inflammatory bowel disease, lupus, neuropathy, optic neuritis, osteoarthritis, pancreatitis, peptic ulcer disease, peripheral artery disease, pleural effusion, pneumonia, pneumothorax, pulmonary embolism, raynaud's phenomenon, retinal detachment, rheumatoid arthritis, thyroid nodule, upper respiratory infection, uveitis, vasculitis  ·  missing diagnosis: cancer, endocarditis, lymphoma, stomach cancer
- incorrect medication: —  ·  missing medication: heparin
- dosage mismatch: —
- negation flips (vs. reference): —
- unsupported numbers: —
- missing information: {"symptom": ["lymphadenopathy"], "medical_history": ["endocarditis"], "diagnosis": ["cancer", "lymphoma", "mitral regurgitation", "stomach cancer"], "medication": ["heparin"], "investigation": ["ct scan", "echocardiogram", "mri"]}

## Hallucination example: `dialogue_soap_test_77`

*hallucination example*

ROUGE-L 29.9 · length ratio 1.38 · truncated False · degenerate False · hallucination 76.3 · negation-flip 0.0 · numerical consistency 85.2 · coverage 64.3

**Transcript (excerpt)**

```
Doctor: Hello, I am Dr. Johnson, and I will be taking care of you today. I understand that you were brought to the emergency department of our tertiary care referral hospital with a history of accidentally consuming car coolant and experiencing unsteadiness in your gait about 3 hours later. Can you tell me more about that?
Patient: Yes, doctor. I accidentally drank some car coolant and started feeling unsteady on my feet after about 3 hours.
Doctor: Thank you for the information. On examination, we observed that you were drowsy but following verbal commands. There was no odor of alcohol in your breath. Your GCS score was 15/15 (E4V5M6). Your blood pressure was 140/80 mm of Hg, and your pulse …
```

**Reference note**

```
S: The patient, a male, presented to the emergency department after accidentally ingesting car coolant, reporting unsteadiness in his gait approximately 3 hours post-ingestion. He described feeling drowsy but was able to follow verbal commands.
O: Physical examination revealed a Glasgow Coma Scale (GCS) score of 15/15, blood pressure of 140/80 mm Hg, pulse rate of 68 beats per minute, and normal oxygen saturation on room air. An ECG showed no abnormalities, and no focal neurological deficits were observed. Laboratory findings indicated hypokalemia (K+ 2.4 mEq/L), hypocalcemia (Ca+ 5 mg/dl), metabolic acidosis (HCO3− 15.8 mEq/L, pH 7.322), and high anion gap metabolic acidosis (anion gap 25.1 mEq/L). Urine examination revealed calcium oxalate crystals. Gastric lavage was performed as an initial treatment.
A: The primary diagnosis is ethylene glycol poisoning, evidenced by the presence of  …
```

**Generated note**

```
S: The patient presented to the emergency department approximately three hours post-ingestion of car coolant, complaining of unsteadiness in her gait. She denied any other symptoms including headache, chest pain, shortness of breath, abdominal pain, nausea, vomiting, diarrhea, fever, chills, palpitations, syncope, confusion, altered mental status, visual changes, weakness, numbness, tingling, seizures, tremors, dysarthria, diplopia, photophobia, or odynophagia. No history of allergies, previous surgeries, chronic illnesses, medications, or substance use was reported by the patient.
O: Physical exam findings included drowsiness without alteration in consciousness, Glasgow Coma Scale (GCS) of 15/15, vital signs stable with BP 140/80 mmHg, HR 68 bpm, RR 18/min, SpO2 98%, temperature 36°C. Neurological examination did not reveal any focal deficits. Laboratory tests indicated sodium 142 mEq/L, potassium 2.4 mEq/L, chloride 101.1 mEq/L, bicarbonate 15.8 mEq/L, calcium 5 mg/dL, urea 35 mg/dL, creatinine 0.7 mg/dL, BUN 16.35 mg/dL, glucose 141 mg/dL, arterial blood gases showing pH 7.32, PCO …
```

- unsupported entities (vs. transcript): abdominal pain, allergic rhinitis, blurred vision, chest pain, chills, chronic kidney disease, confusion, diarrhea, double vision, dysphagia, dyspnea, fever, headache, nausea, numbness, palpitations, photophobia, physical examination, potassium level, seizure
- incorrect diagnosis: chronic kidney disease  ·  missing diagnosis: —
- incorrect medication: —  ·  missing medication: —
- dosage mismatch: —
- negation flips (vs. reference): —
- unsupported numbers: 18, 36, 7.32, 98
- missing information: {"diagnosis": ["hypocalcemia", "hypokalemia"], "investigation": ["electrocardiogram", "heart rate measurement", "metabolic panel"]}

## Incorrect diagnosis example: `dialogue_soap_test_151`

*incorrect diagnosis example*

ROUGE-L 6.0 · length ratio 1.73 · truncated True · degenerate True · hallucination 95.4 · negation-flip 0.0 · numerical consistency 100.0 · coverage 28.6

**Transcript (excerpt)**

```
Doctor: Hello, can you tell me why you were admitted to the hospital back in June 2016?
Patient: Yeah, I was admitted because of weakness in my right arm and problems with my speech, like slurring.
Doctor: I see. You were diagnosed with cerebral infarction in the left middle cerebral artery area and deep vein thrombosis. Your ECG demonstrated normal sinus rhythm and echocardiography revealed no intra-cardiac thrombus or vegetation. You were then discharged with a prescription for apixaban. Is that correct?
Patient: Yes, that's right.
Doctor: In August 2016, you were readmitted to the hospital due to recurrent right arm weakness and slurred speech. The MRI showed multiple cerebral infarctions …
```

**Reference note**

```
S: The patient reported initial symptoms of weakness in the right arm and slurred speech leading to a hospital admission in June 2016. The patient was diagnosed with cerebral infarction and deep vein thrombosis. Symptoms recurred in August 2016, including right arm weakness and slurred speech. The patient recalls being treated for suspected Trousseau's syndrome and potential infective endocarditis, followed by cardiac surgery for mitral valve vegetation.
O: Initial diagnosis was cerebral infarction in the left middle cerebral artery and deep vein thrombosis. MRI in August 2016 showed multiple cerebral infarctions in both cerebral hemispheres and the cerebellum. Echocardiography indicated mild mitral regurgitation with vegetation on the mitral valve. CT scan revealed left renal infarction and swollen lymph nodes suggestive of advanced gastric cancer or lymphoma. During cardiac surgery, a  …
```

**Generated note**

```
S: Patient reports being hospitalized initially in June 2016 for right-sided weakness and dysarthria. She has been previously diagnosed with left MCA territory stroke and DVT.  She is status post recent admission for recurrent R sided weakness and dysarthria, now also having suspicion of Trousseau’s Syndrome.  No history of fever, chills, night sweats, weight loss, fatigue, malaise, joint pain, rash, arthralgias, pleuritic chest pains, cough, sputum production, shortness of breath, orthopnea, paroxysmal nocturnal dyspnea, palpitations, syncope, near-syncope, dizziness, lightheadedness, vertigo, hearing changes, tinnitus, visual disturbances, diplopia, photophobia, headache, confusion, memory difficulties, difficulty swallowing, hoarseness, voice changes, numbness, tingling, paresthesias, muscle cramps, fasciculations, tremors, ataxia, gait disturbance, urinary frequency, urgency, hesitancy, retention, constipation, diarrhea, nausea, vomiting, epigastric burning, bloating, early satiety, jaundice, pruritus, dark urine, pale stools, edema, purpura, petechiae, bruising, bleeding gums, e …
```

- unsupported entities (vs. transcript): abscess, anal fissure, angioedema, appendicitis, arthritis, asthma, bleeding, bloating, blood in stool, blurred vision, brain tumor, bruising, burning sensation, chest pain, chills, cholecystitis, cirrhosis, confusion, conjunctivitis, constipation
- incorrect diagnosis: abscess, anal fissure, angioedema, appendicitis, arthritis, cholecystitis, cirrhosis, conjunctivitis, copd, dental caries, diverticulitis, drug allergy, fungal infection, gastritis, gastroenteritis, hernia, hypertension, inflammatory bowel disease, lupus, neuropathy, optic neuritis, osteoarthritis, pancreatitis, peptic ulcer disease, peripheral artery disease, pleural effusion, pneumonia, pneumothorax, pulmonary embolism, raynaud's phenomenon, retinal detachment, rheumatoid arthritis, thyroid nodule, upper respiratory infection, uveitis, vasculitis  ·  missing diagnosis: cancer, endocarditis, lymphoma, stomach cancer
- incorrect medication: —  ·  missing medication: heparin
- dosage mismatch: —
- negation flips (vs. reference): —
- unsupported numbers: —
- missing information: {"symptom": ["lymphadenopathy"], "medical_history": ["endocarditis"], "diagnosis": ["cancer", "lymphoma", "mitral regurgitation", "stomach cancer"], "medication": ["heparin"], "investigation": ["ct scan", "echocardiogram", "mri"]}

## Incorrect medication / dosage example: `dialogue_soap_test_232`

*incorrect medication / dosage example*

ROUGE-L 21.3 · length ratio 1.71 · truncated False · degenerate False · hallucination 86.7 · negation-flip 16.7 · numerical consistency 40.0 · coverage 70.0

**Transcript (excerpt)**

```
Doctor: Hello, I'm Dr. Smith. I understand that you've been referred for a psychiatric evaluation by your daughter and the hospital staff due to your hallucinations and thoughts of suicide. Can you tell me more about your situation?
Patient: Hi, Doctor. I'm a 55-year-old divorced, multiparous Caucasian woman. My hallucinations started about four months ago. At first, I heard a young girl and a rodent in my house. Then I started experiencing visual and tactile hallucinations of scabies crawling out of my skin.
Doctor: I see. And these hallucinations of scabies led you to believe that you had delusional parasitosis?
Patient: Yes, that's right. It got so bad that I began picking at my skin and  …
```

**Reference note**

```
S: The patient is a 55-year-old divorced, multiparous Caucasian female presenting with auditory, visual, and tactile hallucinations that began four months ago. She reports hearing voices and seeing and feeling scabies crawling out of her skin, leading to self-diagnosed delusional parasitosis. This has resulted in self-inflicted skin excoriations and chemical burns from using bleach and ammonium-based cleaners. She also experiences persecutory delusions, intrusive thoughts of swallowing objects, poor concentration, memory loss, anhedonia, insomnia, and suicidal ideation.
O: The patient has visible excoriation and burn injuries on her face, extremities, and abdomen. Previous consultations with dermatologists did not confirm any parasitic infestation. No laboratory or imaging results were discussed in the transcript.
A: The primary diagnosis is Delusional Disorder, with differential diagnos …
```

**Generated note**

```
S: The patient is a 55 y/o G2P female who presented with a chief complaint of auditory, visual, and tactile hallucinations starting approximately 4 mo prior to presentation. She has also reported suicidal ideation.  She denies history of substance abuse.  She states her symptoms include hearing voices, seeing things, feeling bugs on her skin, and believing she has evidence of parasites which she cannot eradicate despite multiple treatments including application of bleach and other chemicals causing burns and lacerations.  She admits to talking to the "bugs" as if they had personality.  She does admit to some obsessive ideas such as swallowing foreign bodies although she denies acting upon those impulses.  She reports difficulty concentrating, forgetfulness, depression, anxiety, sleep disturbances, and intermittent periods of hopelessness.  No significant change in appetite noted.  Denies recent trauma or major stressors.  She has seen several psychiatrists previously without improvement.

O: On examination, vital signs stable.  General appearance shows no acute distress.  Psychiatric …
```

- unsupported entities (vs. transcript): adverse drug reaction, albuterol, allergic rhinitis, anxiety, asthma, bipolar disorder, blood work, calcium supplement, dementia, depression, diagnostic workup, gastroenteritis, hyperlipidemia, hypertension, ibuprofen, laceration, lisinopril, multivitamin, omeprazole, pathology
- incorrect diagnosis: adverse drug reaction, bipolar disorder, dementia  ·  missing diagnosis: —
- incorrect medication: albuterol, calcium supplement, ibuprofen, lisinopril, multivitamin, omeprazole, penicillin, simvastatin  ·  missing medication: —
- dosage mismatch: —
- negation flips (vs. reference): trauma
- unsupported numbers: 1, 10, 18
- missing information: {"symptom": ["depressive symptoms", "insomnia"], "investigation": ["imaging"]}

## Negation error example: `dialogue_soap_test_179`

*negation error example*

ROUGE-L 24.9 · length ratio 0.72 · truncated False · degenerate False · hallucination 33.3 · negation-flip 45.5 · numerical consistency 57.1 · coverage 57.7

**Transcript (excerpt)**

```
Doctor: Hello, I'm Dr. Smith. What brings you to the family medicine clinic today?
Patient: Hi, doctor. My 30-month-old son has been having abdominal bloating and persistent diarrhea after every feeding for the past four months. His stools are foul-smelling and occur more than four times a day.
Doctor: I see. Has this been associated with any failure to gain weight?
Patient: Yes, he hasn't been gaining weight like he should.
Doctor: Has your child had a normal appetite with no history of vomiting or feeding intolerance?
Patient: Yes, he has a normal appetite and hasn't had any problems with vomiting or feeding.
Doctor: Has there been any history of fever, night sweats, rash, cough, or joint  …
```

**Reference note**

```
S: The patient, a 30-month-old male, presents with persistent diarrhea, abdominal bloating, and foul-smelling stools occurring more than four times daily for the past four months. The child has a normal appetite, no vomiting, and no recent sick contacts. He has experienced a failure to gain weight but has no other associated symptoms such as fever, rash, or cough. There is no significant past medical history, no known allergies, and he is up-to-date with vaccinations. Family and social histories are unremarkable.
O: Physical examination shows the child is alert and active, with no dysmorphic features. He is below the second standard deviation for weight and height, appears pale but without scleral icterus. Vital signs are heart rate 90 bpm, blood pressure 80/52 mmHg, respiratory rate 22 bpm, and temperature 36.8°C. Abdominal examination reveals a soft, non-tender abdomen with normal bowe …
```

**Generated note**

```
S: 30-month-old male presents with chief complaints of abdominal bloating and persistent diarrhea post-feeding for the last 4 months, foul-smelling stools >4x/day, and poor weight gain despite adequate intake without vomiting, feeding issues, fever, rashes, cough, arthralgia, or sick contacts.  History significant for multiple GP visits without diagnosis; negative for medication use, allergies, previous illnesses, surgical procedures, consanguinity, familial disease, abnormal growth parameters, delayed developmental milestones, or abnormalities during pregnancy/delivery/labor.  Up-to-date immunizations.
O: On physical exam, patient appeared well-nourished, alert, and awake, with no acute distress, pallor, jaundice, or other notable findings.  Abdominal exam showed tenderness, distension, hypoactive bowel sounds, and absence of hepatosplenomegaly.  Neurological exams were within normal limits.  Vital signs included HR 90bpm, BP 80/52mmHg, RR 22rpm, Temp 98°F.  Developmental milestones appropriate for age per mother report.
A: Primary assessment suggests malabsorption syndrome given ch …
```

- unsupported entities (vs. transcript): celiac disease, diagnostic workup, endoscopy, lactose intolerance, malnutrition, pain, pregnancy, stool test
- incorrect diagnosis: lactose intolerance  ·  missing diagnosis: —
- incorrect medication: —  ·  missing medication: —
- dosage mismatch: —
- negation flips (vs. reference): cough, fever, pallor, rash, vaccine
- unsupported numbers: 5, 9, 98
- missing information: {"symptom": ["abdominal tenderness"], "medical_history": ["immunodeficiency", "infection", "inflammatory bowel disease"], "investigation": ["blood work", "celiac testing", "complete blood count", "heart rate measurement", "metabolic panel", "respiratory rate"]}

## Numerical error example: `dialogue_soap_test_150`

*numerical error example*

ROUGE-L 23.6 · length ratio 1.33 · truncated False · degenerate False · hallucination 48.6 · negation-flip 0.0 · numerical consistency 34.8 · coverage 90.0

**Transcript (excerpt)**

```
Doctor: Hello, how can I help you today?
Patient: Hi, doctor. I am a 75-year-old woman, and I've been having a loss of appetite for a week now. I'm 132 cm tall and weigh 34 kg.
Doctor: I see. Are you taking any medications currently?
Patient: Yes, I take aspirin, celecoxib, and amlodipine for angina and hypertension.
Doctor: Alright. I will need to run some laboratory examinations to better understand your condition. 
*After the examinations*
Doctor: Your lab results show that your Hb has decreased modestly to 10.7 g/dl. I would like to monitor your condition and ask that you return in two weeks for a follow-up.
Patient: Okay, thank you.
*Two weeks later*
Patient: Doctor, my anorexia has wor …
```

**Reference note**

```
S: A 75-year-old female patient presents with a chief complaint of progressive loss of appetite over the past week, worsening to the point of self-admission to the hospital. She reports a history of angina and hypertension, for which she is taking aspirin, celecoxib, and amlodipine. The patient also describes episodes of vomiting large amounts of bright red blood.
O: Initial lab results showed a modest decrease in hemoglobin (Hb) to 10.7 g/dl. Subsequent tests revealed a significant drop in Hb to 4.8 g/dl and hematocrit to 15%, with slight increases in white blood count to 9900 /mm3 and C-reactive protein to 4.64 mg/dl. Albumin levels were low at 2.5 g/dl, and creatinine was slightly elevated at 1.14 mg/dl with a reduced estimated glomerular filtration rate of 41.7 ml/min. CT scans of the chest and abdomen were unremarkable. An urgent endoscopic examination identified and treated active  …
```

**Generated note**

```
S: The patient is a 75-year-old female who presented initially complaining of one-week history of progressive anorexia. She denied other systemic complaints at this time.  She was on aspirin, celecoxib, and amlodipine for her chronic conditions of angina pectoris and hypertension.  Two weeks ago she had labs drawn showing mild decrease in hemoglobin to 10.7 g/dL.  Since then, she has become more symptomatic and admitted herself into the hospital whereupon upon evaluation, she became acutely ill with melena per rectum and subsequently developed hematemesis.  Her vital signs remained stable except for tachycardia.  Labs revealed severe anemia with hemoglobin down to 2.9 g/dL, elevated WBCs, CRP, decreased albumin, slight elevation in creatinine, and GFR of 41 mL/minute.  CT scans of abdomen and chest were negative for masses.  Endoscopy identified upper GI bleed secondary to duodenal ulcer.  Post-endoscopic intervention, her hemoglobin rose to 8.9 g/dL.  Despite improvement in her hemodynamics, she remains obtunded and non-responsive to voice commands.  Brain imaging shows ischemic cha …
```

- unsupported entities (vs. transcript): anemia, atrial fibrillation, bilirubin, bleeding disorder, blood in stool, coagulation studies, endoscopy, gastritis, gi bleed, imaging, iv fluids, leukocytosis, oxygen saturation, respiratory rate, stroke, tachycardia, vital signs, white blood cell count
- incorrect diagnosis: atrial fibrillation, bleeding disorder, gastritis, stroke  ·  missing diagnosis: —
- incorrect medication: iv fluids  ·  missing medication: —
- dosage mismatch: —
- negation flips (vs. reference): —
- unsupported numbers: 0.3, 0.6, 1.04, 1.6, 110, 12, 130, 130/80, 19, 20, 24, 3, 41, 80, 94
- missing information: {"symptom": ["vomiting"], "investigation": ["complete blood count"]}

## Missing information example: `dialogue_soap_test_202`

*missing information example*

ROUGE-L 13.0 · length ratio 0.24 · truncated False · degenerate False · hallucination 71.4 · negation-flip 0.0 · numerical consistency 100.0 · coverage 7.7

**Transcript (excerpt)**

```
Doctor: Hello, I understand that your male infant was referred to our intensive care unit from a peripheral facility. Can you please describe the symptoms he has been experiencing?
Parent: Yes, he has had one day of progressively worsening difficulty in breathing and feeding. He also had multiple convulsions of generalized tonic clonic nature.
Doctor: Thank you for the information. Upon examination, we found that he was dyspneic, afebrile, and tachycardic, with cold extremities, weak pulses, and a delayed capillary refill of 4 seconds. His blood pressure was 98/64 mmHg, and his blood sugar was 14.4 mmol l–1. We also performed an arterial blood gas test, which showed a mixed metabolic/respira …
```

**Reference note**

```
S: The patient, a male infant, presented with one day of progressively worsening difficulty in breathing and feeding, along with multiple generalized tonic-clonic convulsions. The parent also reported a 3-week history of nasal congestion treated with nasal saline drops, antihistamines, antibiotics, and antipyretics.
O: On examination, the infant was dyspneic, afebrile, and tachycardic with cold extremities, weak pulses, and a delayed capillary refill of 4 seconds. Vital signs included a blood pressure of 98/64 mmHg and a blood sugar level of 14.4 mmol/L. Arterial blood gas analysis showed mixed metabolic/respiratory acidosis (pH 7.1, pCO2 55 mmHg, bicarbonate 20 mEq/L). Laboratory tests revealed a white cell count of 15.6 × 10^9/µL with 76% neutrophils, thrombocytosis (605 × 10^9/µL), and an INR of 1.24. Chest radiograph was normal. A CT scan and MRI identified a 27 mm × 47 mm × 42 mm pa …
```

**Generated note**

```
S: The patient is a male infant who presented with progressive respiratory distress and seizures over the course of one day.  He has no fever, but does have some tachypnea, bradycardia, cool extremities, delayed capillary refilling time, hypotension, elevated glucose level, acute respiratory failure, and altered mental status.  No significant past medical history except for chronic upper respiratory infection treated with various medications.
```

- unsupported entities (vs. transcript): bradycardia, confusion, fever, hypotension, upper respiratory infection
- incorrect diagnosis: —  ·  missing diagnosis: pneumonia, sepsis
- incorrect medication: —  ·  missing medication: ceftriaxone, clarithromycin, enoxaparin, gentamicin, morphine, phenytoin, saline nasal spray
- dosage mismatch: —
- negation flips (vs. reference): —
- unsupported numbers: —
- missing information: {"symptom": ["hot flashes", "purulent drainage", "tachycardia", "weakness"], "diagnosis": ["pneumonia", "sepsis"], "medication": ["ceftriaxone", "clarithromycin", "enoxaparin", "gentamicin", "morphine", "phenytoin"], "investigation": ["blood pressure measurement", "blood work", "coagulation studies", "ct scan", "diagnostic workup", "heart rate measurement"]}

## Degenerate output example: `dialogue_soap_test_146`

*degenerate output example*

ROUGE-L 6.2 · length ratio 2.52 · truncated True · degenerate True · hallucination 99.0 · negation-flip 0.0 · numerical consistency 20.0 · coverage 33.3

**Transcript (excerpt)**

```
Doctor: Hello, young lady. How can I help you today?
Patient: Hi, doctor. I've been having this problem with my neck swelling up on the left side since I was 6 years old.
Doctor: I see. Have you had any treatment for this swelling?
Patient: Yes, I had some treatment to control the inflammation.
Doctor: Good. Did you have any tests done after the inflammation was controlled?
Patient: Yes, I had a barium esophagography done.
Doctor: Alright. And what did the results show?
Patient: The results showed a PSF on the left side of my neck.
Doctor: Okay, and did you have a CT scan as well?
Patient: Yes, and it showed an air- and barium-containing fistula.
Doctor: I understand. We decided to perform a …
```

**Reference note**

```
S: The patient, a young female, reports a history of left-sided neck swelling since age 6. She mentions previous treatments aimed at controlling inflammation and has undergone diagnostic evaluations including barium esophagography and CT scan, which identified a PSF (pharyngeal salivary fistula) containing air and barium.
O: The patient underwent a minimally invasive lateral surgery (MLS) to address the fistula, described as narrow with non-fragile tissue. Postoperative evaluations showed no leakage, and she was able to resume oral intake immediately after the procedure. She was discharged 7 days post-surgery without complications.
A: The primary diagnosis is a left-sided pharyngeal salivary fistula. The successful surgical intervention and absence of postoperative complications or recurrence of symptoms suggest a positive outcome.
P: The patient is advised to continue regular follow-ups …
```

**Generated note**

```
S: The patient is a female who has experienced recurrent left-sided cervical swelling starting at age six. She reports no recent exacerbations or complications but does recall undergoing surgical intervention previously due to her condition.  She denies dysphagia, odynophagia, weight loss, fever, chills, night sweats, fatigue, weakness, palpitations, shortness of breath, orthopnea, paroxysmal nocturnal dyspnea, chest pain, pleuritic chest pain, cough, sputum production, hemoptysis, wheezing, stridor, hoarseness, voice change, difficulty swallowing solids, liquids, regurgitation, nausea, vomiting, abdominal pain, diarrhea, constipation, melena, hematochezia, arthralgias, joint effusions, rash, pruritus, urticaria, edema, syncope, dizziness, headache, visual changes, diplopia, photophobia, blurred vision, hearing loss, tinnitus, vertigo, ear fullness, epistaxis, rhinorrhea, nasal congestion, sinusitis, sore throat, dental caries, toothache, gum bleeding, gingivitis, halitosis, dysuria, frequency, urgency, flank pain, costovertebral angle tenderness, hypertension, hypotension, tremors,  …
```

- unsupported entities (vs. transcript): abdominal pain, abscess, adrenal insufficiency, anxiety, appendicitis, arrhythmia, arthritis, atrial fibrillation, bleeding, blood in stool, blurred vision, bradycardia, bruising, bundle branch block, cancer, cellulitis, chest pain, chills, cholecystitis, cirrhosis
- incorrect diagnosis: abscess, adrenal insufficiency, anxiety, appendicitis, arrhythmia, arthritis, atrial fibrillation, bundle branch block, cancer, cellulitis, cholecystitis, cirrhosis, cushing's syndrome, deep vein thrombosis, dental caries, depression, diverticulitis, gastritis, gastroenteritis, hypertension, hyperthyroidism, hypothyroidism, inflammatory bowel disease, irritable bowel syndrome, mitral regurgitation, osteomyelitis, pancreatitis, peptic ulcer disease, periodontal disease, pulmonary embolism, sebaceous cyst, sinusitis, sleep apnea, thyroid nodule  ·  missing diagnosis: —
- incorrect medication: —  ·  missing medication: —
- dosage mismatch: —
- negation flips (vs. reference): —
- unsupported numbers: 0, 1, 2, 3, 4, 5, 8, 9
- missing information: {"investigation": ["ct scan", "diagnostic workup"]}

# Split: val_check

## Best ROUGE-L: `mts_dialog_validation_6`

*highest ROUGE-L in the split*

ROUGE-L 40.0 · length ratio 0.43 · truncated False · degenerate False · hallucination — · negation-flip — · numerical consistency — · coverage —

**Transcript (excerpt)**

```
Doctor: Have you had any surgeries in the past?
Patient: Nope I have not. 
Doctor: Anything?
Patient: No.
```

**Reference note**

```
He has not had any previous surgery.
```

**Generated note**

```
No previous surgery.
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

## Hallucination example: `aci_bench_validation_D2N077-aci`

*hallucination example*

ROUGE-L 25.6 · length ratio 0.74 · truncated False · degenerate False · hallucination 37.5 · negation-flip 22.2 · numerical consistency 73.3 · coverage 77.8

**Transcript (excerpt)**

```
[doctor] hey diana it's good to see you in here so i see that you injured your wrist could you tell me a bit about what happened
[patient] yeah i was walking up and down the stairs i was doing my laundry and i slipped and i tried to catch myself and i put my arms out to catch myself and then all of a sudden i just my wrist started to hurt real bad and it got real swollen
[doctor] wow okay so which wrist are we talking about left or right
[patient] it's my right one of course
[doctor] okay and then have you ever injured this arm before
[patient] no i have not
[doctor] okay alright so on a scale of one to ten how severe is the pain
[patient] gosh it's like a nine
[doctor] wow okay have you don …
```

**Reference note**

```
CHIEF COMPLAINT

Right wrist injury.

HISTORY OF PRESENT ILLNESS

Diana Scott is a pleasant 61-year-old female who presents to the clinic today for the evaluation of a right wrist injury. The patient sustained this injury yesterday morning, 05/12/2022, when she slipped on the stairs while carrying a laundry basket. She states she tried to catch herself with her arms outstretched. The patient reports an immediate onset of pain and swelling in her right wrist. She denies any previous injuries to her right arm. The patient rates her pain level as a 9/10. Her pain is aggravated by movement. The patient also reports numbness and tingling in her fingers. She has been icing and wrapping her right wrist with an ACE wrap. The patient has also been taking ibuprofen, which provides some relief. She notes fully extending her arm while resting it on a pillow alleviates some of her pain as well.

The  …
```

**Generated note**

```
CHIEF COMPLAINT

The patient presents with chief complaint of her right wrist being severely painful following trauma from falling onto her right wrist.

HISTORY OF PRESENT ILLNESS

Diana P., age 34, female, presented to the emergency room complaining of right wrist pain. She states she fell off the steps approximately 24 hours prior to presentation. The patient denies any history of previous injuries to her right wrist. Her pain has been rated as 9/10. She has used ice packs and Ace wraps to help alleviate symptoms. She has taken Ibuprofen PRN. No numbness or tingling noted except possibly due to swelling. Denies weakness of hands. Pain worse with motion of wrist.

REVIEW OF SYSTEMS

Significant for right wrist pain. Negative review of systems otherwise.

PHYSICAL EXAMINATION

VITAL SIGNS:

* Blood Pressure: 140/70.
* Pulse: 80 bpm.
* Respiratory Rate: 20/min.
* Temperature: 97.2°F (36°C).
* Oxygen Saturation: 98% on RA.

NECK:

Supple. No masses. No thyroid enlargement. Carotids are symmetrical. No murmurs heard.

CHEST:

Clear lung fields bilaterally. Heart sounds within normal li …
```

- unsupported entities (vs. transcript): anxiety, bloating, diagnostic workup, dislocation, erythema, neuropathy, oxygen saturation, weakness, wrist pain
- incorrect diagnosis: anxiety, dislocation, neuropathy  ·  missing diagnosis: —
- incorrect medication: —  ·  missing medication: tramadol
- dosage mismatch: —
- negation flips (vs. reference): numbness, tingling
- unsupported numbers: 24, 34, 36, 98
- missing information: {"symptom": ["bruising", "crepitus"], "medication": ["tramadol"], "investigation": ["temperature measurement"]}

## Incorrect diagnosis example: `aci_bench_validation_D2N073-virtscribe`

*incorrect diagnosis example*

ROUGE-L 5.0 · length ratio 1.23 · truncated True · degenerate True · hallucination 95.9 · negation-flip 0.0 · numerical consistency 100.0 · coverage 17.4

**Transcript (excerpt)**

```
[doctor] today i'm seeing christina cooper . her date of birth is 07/01/1954 . uh , ms. cooper is a new patient who was referred by diane nelson for a long-standing iron deficiency anemia .
[doctor] hello , how are you ?
[patient] i'm good , thank you .
[doctor] so tell me what brings you in today .
[patient] recently i tried to donate blood , around december i think , and they told me i was anemic , which is something i've been dealing with for a while , so it's not the first time i've been told i'm anemic .
[doctor] or how have you been feeling in general with this ?
[patient] not great . i have been feeling fatigued often during the day , and even feverish with chills at times . when i tr …
```

**Reference note**

```
CHIEF COMPLAINT

Iron deficiency anemia.

HISTORY OF PRESENT ILLNESS

Mrs. Christina Cooper is a 65-year-old female who presents with a long-history of iron deficiency anemia.

The patient reports she has been living with anemia since she was 13 years old. She attempted to donate blood on 12/2019 but was unable to due to her anemia. She has a history of heavy menstruation and a hysterectomy in 1996. She completed a colonoscopy 5-6 years ago with nonsignificant findings. She denies having a pacemaker, defibrillator, sleep apnea, or using oxygen.

Mrs. Cooper reports a myriad of symptoms, stating she feels fatigued often during the day, feverish with chills at times, and during activity feels she cannot catch her breath and some wheezing is present. She has been having some headaches which is uncommon for her. Additionally, she is noticing tingling sensations, cold sensitivity, and her anx …
```

**Generated note**

```
CHIEF COMPLAINT

The patient is a 65-year-old G2P0 white female who comes in for evaluation of chronic fatigue, shortness of breath, palpitations, orthostatic intolerance, syncope, dyspnea on exertion, chest pain, abdominal discomfort, nausea, vomiting, diarrhea, constipation, arthralgias, joint pains, muscle weakness, weight loss, decreased appetite, insomnia, memory problems, confusion, difficulty concentrating, mood swings, irritability, anxiety, depression, tremors, numbness, tingling, paresthesia, heat/cold intolerance, sweating, flushing, pruritus, itching, hirsutism, galactorrhea, amenorrhea, menorrhagia, oligomenorrhea, irregular menses, pelvic pressure, urinary frequency, urgency, nocturia, dysuria, flank pain, costovertebral angle tenderness, hypertension, hypotension, tachycardia, bradycardia, atrial fibrillation, flutter, ventricular arrhythmias, supraventricular tachycardia (SVT), paroxysmal SVT, sinus node dysfunction, sick sinus syndrome, AV block, Wolff-Parkinson-White Syndrome, mitral valve prolapse, tricuspid regurgitation, pulmonary edema, pleural effusion, pericar …
```

- unsupported entities (vs. transcript): abdominal pain, abscess, adrenal insufficiency, arrhythmia, asthma, atrial fibrillation, benign prostatic hyperplasia, bradycardia, bundle branch block, burning sensation, carpal tunnel syndrome, cellulitis, chest pain, cholecystitis, cirrhosis, cold intolerance, confusion, constipation, copd, cushing's syndrome
- incorrect diagnosis: abscess, adrenal insufficiency, arrhythmia, asthma, atrial fibrillation, benign prostatic hyperplasia, bundle branch block, carpal tunnel syndrome, cholecystitis, cirrhosis, copd, cushing's syndrome, deep vein thrombosis, esophagitis, fatty liver disease, fibromyalgia, fracture, gastritis, gerd, gout, hepatitis, hernia, hydronephrosis, hypertension, hyperthyroidism, hypothyroidism, interstitial cystitis, kidney stones, lupus, mitral regurgitation, neuropathy, osteoporosis, pancreatitis, peptic ulcer disease, pericarditis, plantar fasciitis, pleural effusion, pneumonia, pneumothorax, prostate cancer, rheumatoid arthritis, sebaceous cyst, sprain, strain, tendinitis, urinary tract infection, vasculitis  ·  missing diagnosis: anemia, gi bleed, iron deficiency anemia
- incorrect medication: —  ·  missing medication: folic acid, iron supplement, supplemental oxygen, vitamin b12, vitamin c
- dosage mismatch: —
- negation flips (vs. reference): —
- unsupported numbers: —
- missing information: {"symptom": ["chills", "fever", "headache", "wheezing"], "diagnosis": ["anemia", "gi bleed", "iron deficiency anemia", "sleep apnea"], "medication": ["folic acid", "iron supplement", "supplemental oxygen", "vitamin b12", "vitamin c"], "investigation": ["blood work", "colonoscopy", "complete blood count", "endoscopy", "hemoglobin level", "iron studies"]}

## Incorrect medication / dosage example: `aci_bench_validation_D2N075-virtscribe`

*incorrect medication / dosage example*

ROUGE-L 9.6 · length ratio 0.86 · truncated True · degenerate True · hallucination 91.3 · negation-flip 27.3 · numerical consistency 66.7 · coverage 60.0

**Transcript (excerpt)**

```
[doctor] next is betty hill , uh , date of birth is 2/21/1968 . she has a past medical history of uterine fibroids and anemia . she's a new patient with a referral from the er of esophagitis . um , i reviewed our records from the er , including the normal cardiac workup , and we're about to go in and see her now . good morning . you miss hill ?
[patient] good morning . yes . that's me .
[doctor] hey , i'm dr. sanders . it's nice to meet you .
[patient] nice to meet you too .
[doctor] so tell me about what brings you in today ?
[patient] well , i really needed to see you three months ... three months ago , but this was your first available appointment . when i called to make the appointment , …
```

**Reference note**

```
CHIEF COMPLAINT

Esophagitis.

HISTORY OF PRESENT ILLNESS

Betty Hill is a 53 y.o. female who presents to clinic today for a new patient evaluation of suspected esophagitis. The patient was referred from the emergency department where she was seen in early 10/2020 following 4 days of chest pain. The pain has resolved but she kept this appointment to discuss the original 4-day episode.

The patient describes her chest pain in early 10/2020 as sharp and localized behind the sternum. She states that it felt like a heart attack and the onset was sudden. The pain was exacerbated by eating and accompanied by dysphagia. The patient is not able to say whether she had heartburn as she has never experienced heartburn before and is unsure what it feels like. When asked about potential triggers, the patient identifies that she was experiencing a lot of stress at that time due to a job transition. Sh …
```

**Generated note**

```
CHIEF COMPLAINT

Betty Hill, DOB 02/21/68, presents with chief complaint of "chest pain" x 4 days duration, per ER record review, negative cardiology evaluation, positive GI symptoms, and recent history of uterine fibroid and anemia.

HISTORY OF PRESENT ILLNESS

The patient states that she has had chest pain for approximately 4 days starting October 1st, 2020. She denies waking up with the pain; however, she describes it as intermittent and associated with exertional activity. The pain described as central retrosternal type, radiating to both arms, and associated with nausea and vomiting. No history of h/o Hx of HTN, DM, CAD, asthma, allergies, etc. Negative for smoking hx. Positive for ETOH use. Denies fever chills night sweats. Patient denied taking any medication prior to presentation except for ibuprofen.
She has had previous surgery for removal of gallbladder. Has had significant weight loss recently. Denies any history of peptic ulcer disease, gastritis, GERD, hiatal hernia, liver cirrhosis, pancreatitis, inflammatory bowel disease, colon cancer, rectal bleeding, hematochezia,  …
```

- unsupported entities (vs. transcript): allergic rhinitis, angina, arrhythmia, asthma, atrial fibrillation, back pain, blood in stool, blurred vision, breast pain, bruising, burning sensation, chills, cirrhosis, colon cancer, confusion, constipation, coronary artery disease, cough, crackles, cramping
- incorrect diagnosis: —  ·  missing diagnosis: esophagitis
- incorrect medication: ibuprofen, supplemental oxygen  ·  missing medication: —
- dosage mismatch: —
- negation flips (vs. reference): abdominal pain, gerd, weight loss
- unsupported numbers: 02/21, 68
- missing information: {"symptom": ["heartburn", "weight gain"], "diagnosis": ["esophagitis", "myocardial infarction"], "investigation": ["blood work", "diagnostic workup", "electrocardiogram", "endoscopy"]}

## Negation error example: `aci_bench_validation_D2N075-virtscribe`

*negation error example*

ROUGE-L 9.6 · length ratio 0.86 · truncated True · degenerate True · hallucination 91.3 · negation-flip 27.3 · numerical consistency 66.7 · coverage 60.0

**Transcript (excerpt)**

```
[doctor] next is betty hill , uh , date of birth is 2/21/1968 . she has a past medical history of uterine fibroids and anemia . she's a new patient with a referral from the er of esophagitis . um , i reviewed our records from the er , including the normal cardiac workup , and we're about to go in and see her now . good morning . you miss hill ?
[patient] good morning . yes . that's me .
[doctor] hey , i'm dr. sanders . it's nice to meet you .
[patient] nice to meet you too .
[doctor] so tell me about what brings you in today ?
[patient] well , i really needed to see you three months ... three months ago , but this was your first available appointment . when i called to make the appointment , …
```

**Reference note**

```
CHIEF COMPLAINT

Esophagitis.

HISTORY OF PRESENT ILLNESS

Betty Hill is a 53 y.o. female who presents to clinic today for a new patient evaluation of suspected esophagitis. The patient was referred from the emergency department where she was seen in early 10/2020 following 4 days of chest pain. The pain has resolved but she kept this appointment to discuss the original 4-day episode.

The patient describes her chest pain in early 10/2020 as sharp and localized behind the sternum. She states that it felt like a heart attack and the onset was sudden. The pain was exacerbated by eating and accompanied by dysphagia. The patient is not able to say whether she had heartburn as she has never experienced heartburn before and is unsure what it feels like. When asked about potential triggers, the patient identifies that she was experiencing a lot of stress at that time due to a job transition. Sh …
```

**Generated note**

```
CHIEF COMPLAINT

Betty Hill, DOB 02/21/68, presents with chief complaint of "chest pain" x 4 days duration, per ER record review, negative cardiology evaluation, positive GI symptoms, and recent history of uterine fibroid and anemia.

HISTORY OF PRESENT ILLNESS

The patient states that she has had chest pain for approximately 4 days starting October 1st, 2020. She denies waking up with the pain; however, she describes it as intermittent and associated with exertional activity. The pain described as central retrosternal type, radiating to both arms, and associated with nausea and vomiting. No history of h/o Hx of HTN, DM, CAD, asthma, allergies, etc. Negative for smoking hx. Positive for ETOH use. Denies fever chills night sweats. Patient denied taking any medication prior to presentation except for ibuprofen.
She has had previous surgery for removal of gallbladder. Has had significant weight loss recently. Denies any history of peptic ulcer disease, gastritis, GERD, hiatal hernia, liver cirrhosis, pancreatitis, inflammatory bowel disease, colon cancer, rectal bleeding, hematochezia,  …
```

- unsupported entities (vs. transcript): allergic rhinitis, angina, arrhythmia, asthma, atrial fibrillation, back pain, blood in stool, blurred vision, breast pain, bruising, burning sensation, chills, cirrhosis, colon cancer, confusion, constipation, coronary artery disease, cough, crackles, cramping
- incorrect diagnosis: —  ·  missing diagnosis: esophagitis
- incorrect medication: ibuprofen, supplemental oxygen  ·  missing medication: —
- dosage mismatch: —
- negation flips (vs. reference): abdominal pain, gerd, weight loss
- unsupported numbers: 02/21, 68
- missing information: {"symptom": ["heartburn", "weight gain"], "diagnosis": ["esophagitis", "myocardial infarction"], "investigation": ["blood work", "diagnostic workup", "electrocardiogram", "endoscopy"]}

## Numerical error example: `aci_bench_validation_D2N069-virtassist`

*numerical error example*

ROUGE-L 13.7 · length ratio 2.27 · truncated True · degenerate True · hallucination 91.5 · negation-flip 0.0 · numerical consistency 18.2 · coverage 76.9

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

Ms. Thompson is a 43-year-old G2P1 who presents today complaining of her right knee pain. She states she was changing a lightbulb approximately one day prior to presentation and felt a twisting motion while falling off the step stool which caused her right knee pain. The patient denies any trauma elsewhere. No improvement noted with application of ice and Ibuprofen. Denies any fever, chills, nausea, vomiting, diarrhea, dysuria, frequency, urgency, hematuria, flank pain, abdominal pain, chest pain, palpitations, shortness of breath, orthopnea, PND, Hx of AFIB, DIOXIN, previous surgery including rhinoplasty.

REVIEW OF SYSTEMS

Significant for right lower extremity pain, negative for fevers, chills, night sweats, weight loss, joint pains, muscle weakness, visual changes, hearing changes, headaches, photophobia, diplopia, syncope, tremors, gait disturbances, urinary symptoms, GI symptoms, respiratory symptoms, musculoskeletal complaints, neurological deficits, skin rashes, arthralgia, arthritis, edema, lymphadenopathy, wheezi …
```

- unsupported entities (vs. transcript): abdominal pain, acne, arthritis, atrial fibrillation, bleeding, blood pressure measurement, blurred vision, bruising, cataract, chest pain, chills, cold intolerance, conjunctivitis, cough, dental caries, diabetic retinopathy, diarrhea, difficulty walking, dizziness, double vision
- incorrect diagnosis: —  ·  missing diagnosis: sprain
- incorrect medication: —  ·  missing medication: digoxin
- dosage mismatch: —
- negation flips (vs. reference): —
- unsupported numbers: 12, 130, 130/80, 18, 37, 80, 88, 96, 98.6
- missing information: {"diagnosis": ["sprain"], "medication": ["digoxin"], "investigation": ["mri"]}

## Missing information example: `mts_dialog_validation_1`

*missing information example*

ROUGE-L 3.7 · length ratio 0.74 · truncated False · degenerate False · hallucination 50.0 · negation-flip 0.0 · numerical consistency — · coverage 12.5

**Transcript (excerpt)**

```
Doctor: Hey, bud. What brings you in today? 
Patient: A rash on my upper arms and torso. 
Doctor: When did it start? 
Patient: Bout a day or two ago. 
Doctor: Any itchiness to the area? 
Patient: Yes, a lot actually. 
Doctor: Have you had episodes of shortness of breath or wheezing? 
Patient: No. 
Doctor: How about swelling to your lips, tongue, or throat? 
Patient: No. 
Doctor: And no nausea or headaches? 
Patient: No. 
Doctor: Have you applied anything to the rash? 
Patient: No, I thought it'd go away on its own.
```

**Reference note**

```
As mentioned denies any oropharyngeal swelling.  No lip or tongue swelling.  No wheezing or shortness of breath.  No headache.  No nausea.  Notes itchy rash, especially on his torso and upper arms.
```

**Generated note**

```
Significant for dermatologic system with an erythematous pruritic eruption over her upper extremities and trunk bilaterally.  Negative respiratory, negative gastrointestinal, negative neurological systems.
```

- unsupported entities (vs. transcript): erythema
- incorrect diagnosis: —  ·  missing diagnosis: —
- incorrect medication: —  ·  missing medication: —
- dosage mismatch: —
- negation flips (vs. reference): —
- unsupported numbers: —
- missing information: {"symptom": ["dyspnea", "edema", "headache", "nausea", "rash", "tongue swelling"]}

## Degenerate output example: `aci_bench_validation_D2N074-virtscribe`

*degenerate output example*

ROUGE-L 4.9 · length ratio 0.66 · truncated True · degenerate True · hallucination 89.6 · negation-flip 25.0 · numerical consistency — · coverage 39.1

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
CHIEF COMPLAINT:

The patient Bruce Ward presents for evaluation by Dr. Flores due to recent findings of an incidental finding of a pituitary lesion while undergoing MRI imaging for headache complaints. The patient denies any previous similar episodes of headaches. He does deny any fevers, chills, nausea, vomiting, abdominal pain, dysuria, frequency, urgency, chest pains, palpitations, shortness of breath, syncope, dizziness, vertigo, hearing changes, diplopia, photophobia, blurred vision, ptosis, facial droop, arm or leg weakness, paresthesias, tremors, gait disturbances, joint swelling, arthralgias, skin lesions, petechiae, purpura, erythema nodosum, pruritus, urticaria, wheezing, cough, rhinorrhea, sneezing, hoarseness, sore throat, odynophagia, dysphonia, dysarthria, aphasia, memory difficulties, confusion, disorientation, hallucinations, depression, anxiety, insomnia, fatigue, weight gain, weight loss, polydipsia, polyuria, nocturia, orthostatic hypotension, hypertension, edema, varicose veins, hair thinning, alopecia, hirsutism, galactorrhea, amenorrheas, oligomenorrhea, menorr …
```

- unsupported entities (vs. transcript): abdominal pain, abscess, anxiety, back pain, bloating, blood in stool, blurred vision, bruising, chest pain, chills, cold intolerance, confusion, conjunctivitis, constipation, cough, cyanosis, daytime sleepiness, decreased libido, dementia, depression
- incorrect diagnosis: abscess, anxiety, conjunctivitis, dementia, depression, diabetes, gastritis, gastroenteritis, glaucoma, hypertension, hypoglycemia, ingrown toenail, orthostatic hypotension, parkinson's disease, peptic ulcer disease, periodontal disease, plantar fasciitis, raynaud's phenomenon, retinal detachment, schizophrenia, sciatica, uveitis, varicose veins  ·  missing diagnosis: infection, stroke
- incorrect medication: —  ·  missing medication: acetaminophen
- dosage mismatch: —
- negation flips (vs. reference): numbness, rash
- unsupported numbers: —
- missing information: {"symptom": ["neck pain", "seizure"], "medical_history": ["tobacco use"], "diagnosis": ["infection", "myocardial infarction", "stroke"], "medication": ["acetaminophen"], "investigation": ["blood work", "complete blood count", "crp", "diagnostic workup", "eye exam", "physical examination"]}

# Split: zeroshot_base/val_check

## Best ROUGE-L: `aci_bench_validation_D2N070-virtassist`

*highest ROUGE-L in the split*

ROUGE-L 33.2 · length ratio 0.72 · truncated False · degenerate False · hallucination 4.8 · negation-flip 0.0 · numerical consistency 62.5 · coverage 65.5

**Transcript (excerpt)**

```
[doctor] hi logan . how are you ?
[patient] hey , good to see you .
[doctor] it's good to see you as well .
[doctor] so i know the nurse told you about dax .
[patient] mm-hmm .
[doctor] i'd like to tell dax a little bit about you .
[patient] sure .
[doctor] so logan is a 58 year old male , with a past medical history significant for diabetes type 2 , hypertension , osteoarthritis , who presents today with some back pain .
[patient] mm-hmm .
[doctor] so logan , what happened to your back ?
[patient] uh , we were helping my daughter with some heavy equipment and lifted some boxes a little too quickly , and they were a little too heavy .
[doctor] okay ... and did you strain your back , did some …
```

**Reference note**

```
CHIEF COMPLAINT

Back pain.

HISTORY OF PRESENT ILLNESS

Mr. Logan Walker is a 58-year-old male with a past medical history significant for diabetes type 2, hypertension, and osteoarthritis, who presents today with back pain.

Mr. Walker reports that he was helping his daughter move some heavy equipment and lifted some heavy boxes a little too quickly on Saturday. He thought he heard a pop when he moved and he had to lie down for about an hour before his pain resolved. He has had stiffness ever since. The pain is located in his lower back. He took Tylenol, ibuprofen, and used Icy Hot on the area, but it did not seem to help. The patient endorses some tingling in his toes on his right foot, which resolved Sunday afternoon. He finds it difficult to find a comfortable position to sleep at night, and he tends to lie on his right side, which seems to help a little bit.

Regarding his diabetes …
```

**Generated note**

```
**CHIEF COMPLAINT**

Patient presented with complaint of low back pain.

**HISTORY OF PRESENT ILLNESS**

The patient is a 58-year-old male with a past medical history significant for:

* Diabetes Type 2
* Hypertension
* Osteoarthritis

He reports experiencing low back pain after assisting his daughter with moving heavy equipment and lifting boxes on Saturday morning. He describes hearing a "pop" followed by relief of pain after lying down for approximately one hour. Since then, he has experienced stiffness in his lower back. The pain has persisted despite self-treatment with Tylenol, Ibuprofen, and application of cold compresses.

Additionally, the patient reported numbness/tingling sensation in his right foot toe area lasting until Sunday afternoon. He also mentioned difficulty finding a comfortable sleep position due to persistent back pain.

Regarding his diet, the patient admitted to consuming unhealthy foods including peanut butter cups and having irregular meals throughout the summer. However, he expressed interest in improving his dietary habits.

For his hypertension manageme …
```

- unsupported entities (vs. transcript): numbness
- incorrect diagnosis: —  ·  missing diagnosis: trauma
- incorrect medication: —  ·  missing medication: —
- dosage mismatch: —
- negation flips (vs. reference): —
- unsupported numbers: 1, 100, 4
- missing information: {"symptom": ["chest pain", "chills", "fever", "knee pain", "nausea", "vomiting"], "diagnosis": ["trauma"], "investigation": ["diagnostic workup", "home monitoring", "vital signs"]}

## Worst ROUGE-L: `mts_dialog_validation_6`

*lowest ROUGE-L in the split*

ROUGE-L 0.0 · length ratio 1.00 · truncated False · degenerate False · hallucination — · negation-flip — · numerical consistency — · coverage —

**Transcript (excerpt)**

```
Doctor: Have you had any surgeries in the past?
Patient: Nope I have not. 
Doctor: Anything?
Patient: No.
```

**Reference note**

```
He has not had any previous surgery.
```

**Generated note**

```
PAST SURGICAL HISTORY:

None reported by patient.
```

- unsupported entities (vs. transcript): —
- incorrect diagnosis: —  ·  missing diagnosis: —
- incorrect medication: —  ·  missing medication: —
- dosage mismatch: —
- negation flips (vs. reference): —
- unsupported numbers: —
- missing information: {}

## Hallucination example: `aci_bench_validation_D2N069-virtassist`

*hallucination example*

ROUGE-L 29.8 · length ratio 1.38 · truncated False · degenerate False · hallucination 33.3 · negation-flip 0.0 · numerical consistency 50.0 · coverage 92.3

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
**CHIEF COMPLAINT**

Patient presents with complaint of right knee pain following a recent injury.

**HISTORY OF PRESENT ILLNESS**

Ms. Thompson, a 43-year-old female, reports experiencing right knee pain since a fall from a ladder while changing a light bulb approximately one day prior to presentation. She describes twisting her knee during the incident. The patient states she applied ice and took ibuprofen without significant relief.

**REVIEW OF SYSTEMS**

The patient denies injuries elsewhere besides the right knee. Past medical history includes atrial fibrillation (AFIB) treated with digoxin. Surgical history consists of a previous rhinoplasty ("nose job").

**PHYSICAL EXAMINATION**

Upon examination, Ms. Thompson exhibits tenderness over the medial aspect of her right knee, specifically around the medial meniscus area. Flexion of the knee causes increased discomfort, particularly upon valgus stress testing. Sensation remains intact throughout the lower extremities.

**RESULTS**

X-ray imaging reveals:

* No visible fractures or dislocations in either knee joint.
* Presence of m …
```

- unsupported entities (vs. transcript): atrial fibrillation, imaging, mri, physical examination, trauma
- incorrect diagnosis: trauma  ·  missing diagnosis: —
- incorrect medication: —  ·  missing medication: —
- dosage mismatch: —
- negation flips (vs. reference): —
- unsupported numbers: 3, 4, 7, 80
- missing information: {"symptom": ["joint swelling"]}

## Incorrect diagnosis example: `aci_bench_validation_D2N068-virtassist`

*incorrect diagnosis example*

ROUGE-L 26.4 · length ratio 0.52 · truncated False · degenerate False · hallucination 7.1 · negation-flip 27.3 · numerical consistency 87.5 · coverage 83.9

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
**CHIEF COMPLAINT**

The patient presented for follow-up of his chronic conditions including congestive heart failure (CHF) and hypertension.

**HISTORY OF PRESENT ILLNESS**

Brian, a 58-year-old male, reported experiencing fatigue, lack of energy, and feelings of being "out of sorts" for approximately five weeks. He attributed these symptoms to changes in season and increased activity due to ongoing household projects and construction. The patient mentioned occasional episodes of lightheadedness, bloating, and difficulty maintaining a regular diet during this period. His current medication regimen includes unspecified treatments for CHF and hypertension; however, he confirmed adherence to prescribed medications. 

He denied recent fevers, chills, respiratory issues, or gastrointestinal complaints. Notable symptoms included mild chest discomfort described as "cramping," slight cough, and intermittent swelling of the lower extremities.

**REVIEW OF SYSTEMS**

Patient endorsed:

* Fatigue
* Lightheadedness
* Bloating
* Mild chest discomfort ("cramping")
* Slight cough
* Intermittent sw …
```

- unsupported entities (vs. transcript): oxygen saturation, pleural effusion
- incorrect diagnosis: pleural effusion  ·  missing diagnosis: —
- incorrect medication: —  ·  missing medication: —
- dosage mismatch: —
- negation flips (vs. reference): chills, diarrhea, fever, nausea, vomiting, weight gain
- unsupported numbers: 2
- missing information: {"symptom": ["dyspnea on exertion", "weight loss"], "investigation": ["diagnostic workup", "home monitoring", "weight measurement"]}

## Negation error example: `aci_bench_validation_D2N074-virtscribe`

*negation error example*

ROUGE-L 31.3 · length ratio 0.67 · truncated False · degenerate False · hallucination 14.3 · negation-flip 70.0 · numerical consistency 100.0 · coverage 78.3

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
**CHIEF COMPLAINT**

* Worsening headaches over several months

**HISTORY OF PRESENT ILLNESS**

Mr. Ward, a 52-year-old male, presents with complaints of worsening headaches starting approximately three months ago. The headaches are described as a dull, nagging ache located behind his eyes. Initially, the headache severity was around 3 out of 10; however, it has progressively worsened to 6 out of 10. He reports increased frequency and duration of the headaches, particularly in the mornings. Mr. Ward denies any previous history of similar headaches. His primary care physician, Dr. Henry Howard, performed an MRI and serum tests due to the worsening headaches, leading to the incidental discovery of a pituitary lesion.

**REVIEW OF SYSTEMS**

The patient denies:

* Fever or sickness
* Rash or skin lesions
* Neck stiffness
* Numbness or tingling sensations
* Passing out episodes

He mentions recent difficulties bumping into doorframes, suggesting potential visual disturbances.

**PHYSICAL EXAMINATION**

Upon physical examination by Dr. Flores, the following findings were observed:

* Aler …
```

- unsupported entities (vs. transcript): complete blood count, crp, thyroid function test
- incorrect diagnosis: —  ·  missing diagnosis: —
- incorrect medication: —  ·  missing medication: acetaminophen
- dosage mismatch: —
- negation flips (vs. reference): fever, infection, neck pain, rash, seizure, stroke, syncope
- unsupported numbers: —
- missing information: {"symptom": ["slurred speech", "weakness"], "medical_history": ["tobacco use"], "diagnosis": ["myocardial infarction"], "medication": ["acetaminophen"]}

## Numerical error example: `aci_bench_validation_D2N069-virtassist`

*numerical error example*

ROUGE-L 29.8 · length ratio 1.38 · truncated False · degenerate False · hallucination 33.3 · negation-flip 0.0 · numerical consistency 50.0 · coverage 92.3

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
**CHIEF COMPLAINT**

Patient presents with complaint of right knee pain following a recent injury.

**HISTORY OF PRESENT ILLNESS**

Ms. Thompson, a 43-year-old female, reports experiencing right knee pain since a fall from a ladder while changing a light bulb approximately one day prior to presentation. She describes twisting her knee during the incident. The patient states she applied ice and took ibuprofen without significant relief.

**REVIEW OF SYSTEMS**

The patient denies injuries elsewhere besides the right knee. Past medical history includes atrial fibrillation (AFIB) treated with digoxin. Surgical history consists of a previous rhinoplasty ("nose job").

**PHYSICAL EXAMINATION**

Upon examination, Ms. Thompson exhibits tenderness over the medial aspect of her right knee, specifically around the medial meniscus area. Flexion of the knee causes increased discomfort, particularly upon valgus stress testing. Sensation remains intact throughout the lower extremities.

**RESULTS**

X-ray imaging reveals:

* No visible fractures or dislocations in either knee joint.
* Presence of m …
```

- unsupported entities (vs. transcript): atrial fibrillation, imaging, mri, physical examination, trauma
- incorrect diagnosis: trauma  ·  missing diagnosis: —
- incorrect medication: —  ·  missing medication: —
- dosage mismatch: —
- negation flips (vs. reference): —
- unsupported numbers: 3, 4, 7, 80
- missing information: {"symptom": ["joint swelling"]}

## Missing information example: `aci_bench_validation_D2N076-virtscribe`

*missing information example*

ROUGE-L 24.7 · length ratio 0.55 · truncated False · degenerate False · hallucination 0.0 · negation-flip — · numerical consistency 100.0 · coverage 20.0

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
**CHIEF COMPLAINT**

The patient, Katherine, presents for evaluation due to concerns regarding potential renal issues secondary to Smith Magenis Syndrome (SMS).

**HISTORY OF PRESENT ILLNESS**

Katherine is a 2-year-old female, previously premature at 34 weeks gestation, presenting with SMS. She has experienced difficulties with feeding, requiring multiple specialists including GI, dietitian, allergist, neurologist, and therapist interventions. Her mother reports that she has made significant progress, currently engaging in various therapies including feeding, occupational, physical, and speech therapy. The patient's medical history includes being taken off cow's milk and replaced with Ripple Pea Protein Milk, resulting in improved hydration status.

**REVIEW OF SYSTEMS**

* Developmental delays: Patient exhibits delayed gross motor skills; however, recent improvements noted.
* Feeding difficulties: Resolved following removal of cow's milk from her diet.
* Hydration status: Mother reports increased urine output (~8-10 wet diapers per 24 hours).
* Family history: No known relatives wi …
```

- unsupported entities (vs. transcript): —
- incorrect diagnosis: —  ·  missing diagnosis: —
- incorrect medication: —  ·  missing medication: —
- dosage mismatch: —
- negation flips (vs. reference): —
- unsupported numbers: —
- missing information: {"symptom": ["heartburn"], "medical_history": ["autism"], "investigation": ["temperature measurement", "weight measurement"]}
