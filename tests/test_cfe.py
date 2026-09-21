"""Unit tests for the rule-based Clinical Fact Extractor.  Run: python -m pytest tests -q"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from src.cfe import assert_status, detect_kind, extract_facts, segment  # noqa: E402


def facts(text, **kw):
    return extract_facts(text, **kw)


def by_canon(fs, canon):
    return [f for f in fs if f.canonical == canon]


# ---- negation / assertion -------------------------------------------------------------------

def test_pre_negation_scope_over_comma_list():
    s = "The patient denies fever, chills, nausea or vomiting."
    fs = facts(s, kind="note")
    for c in ("fever", "chills", "nausea", "vomiting"):
        assert by_canon(fs, c)[0].polarity == "absent", c


def test_negation_scope_terminated_by_but():
    fs = facts("He denies chest pain but reports shortness of breath.", kind="note")
    assert by_canon(fs, "chest pain")[0].polarity == "absent"
    assert by_canon(fs, "dyspnea")[0].polarity == "present"


def test_post_negation():
    fs = facts("Pulmonary embolism was ruled out.", kind="note")
    assert by_canon(fs, "pulmonary embolism")[0].polarity == "absent"


def test_pseudo_negation_does_not_negate():
    a = assert_status("There is no increase in the knee swelling.", 25, 38)
    assert a.polarity == "present"


def test_bare_negative_style():
    fs = facts("ROS: Negative myalgia, negative joint pain, positive for headache.", kind="note")
    assert by_canon(fs, "muscle pain")[0].polarity == "absent"
    assert by_canon(fs, "joint pain")[0].polarity == "absent"
    assert by_canon(fs, "headache")[0].polarity == "present"


def test_uncertainty_and_history_and_family():
    fs = facts("Possible pneumonia. History of asthma. Her mother had breast cancer.", kind="note")
    assert by_canon(fs, "pneumonia")[0].certainty == "uncertain"
    h = by_canon(fs, "asthma")[0]
    assert h.category == "medical_history" and h.temporality == "historical"
    m = by_canon(fs, "breast cancer")[0]
    assert m.experiencer == "family" and m.category == "medical_history"


# ---- dialogue handling ----------------------------------------------------------------------

DIALOGUE = """[doctor] any fever or chills ?
[patient] no .
[doctor] any cough ?
[patient] yes , a dry cough for three days .
[doctor] i'm going to start you on amoxicillin 500 mg three times a day for 10 days ."""


def test_detect_kind():
    assert detect_kind(DIALOGUE) == "dialogue"
    assert detect_kind("CHIEF COMPLAINT\n\nKnee pain.\n\nHISTORY OF PRESENT ILLNESS\n\nThe patient ...") == "note"


def test_dialogue_bare_no_negates_question_terms_only():
    fs = facts(DIALOGUE)
    assert by_canon(fs, "fever")[0].polarity == "absent"
    assert by_canon(fs, "chills")[0].polarity == "absent"
    cough = by_canon(fs, "cough")
    assert cough and all(f.polarity == "present" for f in cough)


def test_dosage_attached_to_drug_with_frequency():
    fs = facts(DIALOGUE)
    d = [f for f in fs if f.category == "dosage"]
    assert d and d[0].drug == "amoxicillin" and d[0].value == "500" and d[0].unit == "mg" and d[0].frequency == "three times a day"


def test_duration_numeric():
    fs = facts(DIALOGUE)
    dur = [f for f in fs if f.subtype == "duration"]
    assert any(f.value == "three" and f.unit == "day" for f in dur)
    assert any(f.value == "10" and f.unit == "day" for f in dur)


# ---- notes / sections -----------------------------------------------------------------------

NOTE = """CHIEF COMPLAINT

Knee pain.

HISTORY OF PRESENT ILLNESS

Mr. X is a 62-year-old male with a past medical history significant for hypertension and type 2 diabetes. Blood pressure today 142/88.

RESULTS

X-ray of the right knee shows no fracture. Hemoglobin A1c is 7.4.

ASSESSMENT AND PLAN

1. Osteoarthritis of the right knee. Start meloxicam 15 mg daily. Refer to physical therapy. Follow up in 6 weeks.
"""


def test_sections_and_routing():
    kind, sents = segment(NOTE, kind="note")
    assert {s.section for s in sents} >= {"chief_complaint", "hpi", "results", "assessment"}
    fs = facts(NOTE, kind="note")
    assert by_canon(fs, "hypertension")[0].category == "medical_history"
    oa = by_canon(fs, "osteoarthritis")[0]
    assert oa.category == "diagnosis" and oa.subtype == "asserted" and oa.section == "assessment"
    assert by_canon(fs, "fracture")[0].polarity == "absent"


def test_vitals_labs_and_followup():
    fs = facts(NOTE, kind="note")
    assert any(f.subtype == "vital" and f.value == "142/88" for f in fs)
    assert any(f.subtype == "lab" and f.value == "7.4" and f.canonical.startswith("hemoglobin a1c") for f in fs)
    assert any(f.subtype == "age" and f.value == "62" for f in fs)
    assert any(f.subtype == "follow_up_timing" and f.value == "6" and f.unit == "week" for f in fs)
    assert any(f.category == "treatment" and f.canonical == "referral" for f in fs)
    d = [f for f in fs if f.category == "dosage" and f.drug == "meloxicam"]
    assert d and d[0].value == "15" and d[0].frequency == "daily"


def test_offsets_are_provenance():
    fs = facts(NOTE, kind="note")
    for f in fs:
        assert NOTE[f.start:f.end] == f.text


def test_short_abbreviation_needs_upper_case():
    assert not by_canon(facts("he was as tired as before", kind="note"), "aortic stenosis")
    assert by_canon(facts("Known history of CAD and CHF.", kind="note"), "coronary artery disease")


def test_class_terms_flagged():
    fs = facts("We will start an antibiotic.", kind="note")
    ab = by_canon(fs, "antibiotic")
    assert ab and ab[0].is_class
