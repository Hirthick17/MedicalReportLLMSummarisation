"""Unit tests for the factuality checker and the standard metrics.  Run: python -m pytest tests -q"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from src.eval.factuality import check_factuality, numbers_in  # noqa: E402
from src.eval.metrics import length_stats, rouge_scores  # noqa: E402

SOURCE = """[doctor] you have a history of hypertension . any chest pain ?
[patient] no chest pain . i've had a cough for five days .
[doctor] your blood pressure is 130/85 . keep taking lisinopril 10 mg daily . i'll start azithromycin 250 mg daily ."""
REFERENCE = """HISTORY OF PRESENT ILLNESS

The patient has a history of hypertension. He denies chest pain. He reports a cough for 5 days.

PHYSICAL EXAM

Blood pressure 130/85.

ASSESSMENT AND PLAN

Acute bronchitis. Continue lisinopril 10 mg daily. Start azithromycin 250 mg daily."""


def test_faithful_prediction_scores_clean():
    r = check_factuality(SOURCE, REFERENCE, REFERENCE)
    assert r["hallucination_rate_strict"] == 0.0
    assert r["negation_flip_rate"] == 0.0
    assert r["numerical_consistency"] == 1.0
    assert r["clinical_coverage"] == 1.0
    assert not r["incorrect_diagnosis"] and not r["incorrect_medication"] and not r["dosage_mismatch"]


def test_hallucinated_entity_and_diagnosis():
    pred = REFERENCE.replace("Acute bronchitis.", "Acute bronchitis. Pneumonia. He also reports nausea.")
    r = check_factuality(SOURCE, REFERENCE, pred)
    assert "pneumonia" in r["unsupported_vs_source"] and "nausea" in r["unsupported_vs_source"]
    assert "pneumonia" in r["incorrect_diagnosis"]
    assert r["hallucination_rate"] > 0


def test_negation_flip_detected():
    pred = REFERENCE.replace("He denies chest pain.", "He reports chest pain.")
    r = check_factuality(SOURCE, REFERENCE, pred)
    assert "chest pain" in r["negation_flips"]
    assert r["negation_flip_rate"] > 0


def test_dosage_mismatch_and_wrong_drug():
    pred = REFERENCE.replace("lisinopril 10 mg", "lisinopril 40 mg").replace("azithromycin 250 mg daily", "amoxicillin 500 mg daily")
    r = check_factuality(SOURCE, REFERENCE, pred)
    assert any(m["drug"] == "lisinopril" and m["predicted"].startswith("40") for m in r["dosage_mismatch"])
    assert "amoxicillin" in r["incorrect_medication"]
    assert "azithromycin" in r["missing_medication"]


def test_numerical_error_and_word_numbers():
    assert {"5", "130/85", "10"} <= numbers_in("five days, 130/85, 10 mg")
    pred = REFERENCE.replace("cough for 5 days", "cough for 9 days").replace("130/85", "150/95")
    r = check_factuality(SOURCE, REFERENCE, pred)
    assert "9" in r["unsupported_numbers"] and "150/95" in r["unsupported_numbers"]
    assert r["numerical_consistency"] < 1.0


def test_missing_information():
    pred = "HISTORY OF PRESENT ILLNESS\n\nThe patient has a history of hypertension.\n\nASSESSMENT AND PLAN\n\nAcute bronchitis."
    r = check_factuality(SOURCE, REFERENCE, pred)
    assert r["clinical_coverage"] < 1.0
    assert "lisinopril" in r["missing_medication"] and "azithromycin" in r["missing_medication"]
    assert "cough" in r["missing_by_category"]["symptom"]


def test_rouge_and_length_stats():
    s = rouge_scores("the cat sat on the mat", "the cat sat on the mat")
    assert abs(s["rougeL"] - 1.0) < 1e-9
    ls = length_stats("a b c d " * 30, "reference note of ten words " * 2)
    assert ls["degenerate"] and ls["repeated_4gram_share"] > 0.5
    ls2 = length_stats(REFERENCE, REFERENCE)
    assert not ls2["degenerate"] and abs(ls2["length_ratio"] - 1) < 1e-9
