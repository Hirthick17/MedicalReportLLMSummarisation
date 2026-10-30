"""Unit tests for the fact table and the fact-conditioned prompt.  Run: python -m pytest tests -q"""

import ast
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

from src.cfe import extract_facts  # noqa: E402
from src.pipeline import build_messages, fact_items, format_fact_table, record_messages  # noqa: E402
from src.pipeline import prompt as P  # noqa: E402
from tests.test_cfe import DIALOGUE  # noqa: E402

DIALOGUE_2 = """[doctor] hi , what brings you in today ?
[patient] my blood pressure has been high and i get headaches . my mom had a stroke .
[doctor] are you taking anything for it ?
[patient] i take lisinopril 10 mg once a day . i might have diabetes too , not sure .
[doctor] any chest pain or shortness of breath ?
[patient] no chest pain . a little short of breath on the stairs .
[doctor] your blood pressure today is 150/95 . we'll check an a1c and a lipid panel ."""


def items(text):
    return fact_items(extract_facts(text, kind="dialogue"))


# ---- status resolution ----------------------------------------------------------------------

def test_bare_no_answer_marks_denied():
    sym = items(DIALOGUE)["symptom"]
    assert "fever (DENIED)" in sym and "chills (DENIED)" in sym


def test_patient_answer_overrides_doctor_question():
    sym = items(DIALOGUE_2)["symptom"]
    assert "chest pain (DENIED)" in sym          # asked (uncertain), then "no chest pain"
    assert "dyspnea" in sym                       # asked (uncertain), then confirmed
    assert not any(s.startswith("dyspnea (") for s in sym)


def test_one_item_per_entity():
    sym = items(DIALOGUE)["symptom"]
    assert [s for s in sym if s.startswith("cough")] == ["cough"]   # "cough" + "dry cough" -> one item


def test_uncertain_and_family_tags():
    it = items(DIALOGUE_2)
    assert "diabetes (POSSIBLE)" in it["diagnosis"]
    assert "stroke (FAMILY)" in it["medical_history"]


# ---- dosages / measurements -----------------------------------------------------------------

def test_dosage_merged_into_medication():
    assert items(DIALOGUE)["medication"] == ["amoxicillin 500 mg three times a day"]
    assert items(DIALOGUE_2)["medication"] == ["lisinopril 10 mg once a day"]


def test_measurements():
    m = items(DIALOGUE_2)["numeric"]
    assert "blood pressure 150/95" in m
    assert "duration three days" in items(DIALOGUE)["numeric"]
    assert "age 39" in items("[doctor] she is a 39-year-old female .")["numeric"]


# ---- table text -----------------------------------------------------------------------------

def test_table_leaves_out_empty_categories():
    table = format_fact_table(extract_facts(DIALOGUE, kind="dialogue"))
    assert table.splitlines()[0].startswith("EXTRACTED FACTS")
    assert "- Symptoms: fever (DENIED); chills (DENIED); cough" in table
    assert "Diagnoses" not in table


def test_table_without_facts():
    assert format_fact_table([]).endswith("- (no facts found)")


def test_table_is_short():
    table = format_fact_table(extract_facts(DIALOGUE_2, kind="dialogue"))
    assert len(table.split()) < 80               # ~100 tokens for a 7-turn dialogue


# ---- prompt ---------------------------------------------------------------------------------

def test_messages_layout():
    sys_msg, user = build_messages(DIALOGUE, dataset="dialogue_soap")
    assert sys_msg["role"] == "system" and "(DENIED)" in sys_msg["content"]
    u = user["content"]
    assert u.startswith(P.TASK["dialogue_soap"])
    assert u.index("EXTRACTED FACTS") < u.index("TRANSCRIPT:\n") and u.endswith(DIALOGUE)


def test_record_messages_uses_mts_section():
    rec = {"dataset": "mts_dialog", "source_dialogue": DIALOGUE, "metadata": {"section_header": "GENHX"}}
    assert record_messages(rec)[1]["content"].startswith("Write the HISTORY OF PRESENT ILLNESS section")


def test_facts_come_from_the_dialogue_not_the_reference():
    rec = {"dataset": "aci_bench", "source_dialogue": DIALOGUE,
           "target_summary": "ASSESSMENT AND PLAN\n\nPneumonia. Start azithromycin 250 mg daily."}
    u = record_messages(rec)[1]["content"]
    assert "pneumonia" not in u.lower() and "azithromycin" not in u.lower()


def test_prompt_text_matches_review2_kernel():
    """Baseline vs fact-conditioned must differ only in FACT_RULES and the table."""
    tree = ast.parse((ROOT / "kaggle" / "baseline" / "baseline_qlora.py").read_text(encoding="utf-8"))
    kernel = {t.id: ast.literal_eval(node.value) for node in tree.body if isinstance(node, ast.Assign)
              for t in node.targets if isinstance(t, ast.Name) and t.id in ("SYSTEM", "TASK", "MTS_SECTIONS")}
    assert kernel == {"SYSTEM": P.SYSTEM, "TASK": P.TASK, "MTS_SECTIONS": P.MTS_SECTIONS}
