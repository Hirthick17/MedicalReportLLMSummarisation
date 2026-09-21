"""
Clinical lexicons for the rule-based Clinical Fact Extractor (Review 2 "basic" CFE).

Everything is a plain Python structure, so the extractor is deterministic, dependency-free and runs
on the laptop CPU in seconds. Review 3 replaces the lexicon look-up with scispaCy NER + UMLS
linking (MODEL_PLAN.md Stage 1) but keeps the same Fact schema, so nothing downstream changes.

Design notes
- Each entry maps a *surface form* (lower-case) to a *canonical form*. Canonical forms are what
  the evaluation compares, so "shortness of breath", "short of breath", "sob" and "dyspnea" all
  become "dyspnea".
- The lists are biased towards the vocabulary of ACI-Bench, MTS-Dialog and DialogueSOAP:
  primary-care / ED encounters, US brand names, common labs.
- A term lives in exactly one primary category. The extractor decides *contextually* whether a
  condition mention is a diagnosis or a history item (see extractor.py).
"""

from __future__ import annotations

from .lex_conditions import CASE_SENSITIVE_ABBREV, CONDITION_GROUPS
from .lex_medications import MEDICATION_CLASSES, MEDICATION_GROUPS
from .lex_procedures import INVESTIGATION_GROUPS, MTS_SECTION_MAP, SECTION_ALIASES, TREATMENT_GROUPS
from .lex_symptoms import SYMPTOM_GROUPS


def _build(groups: dict[str, list[str]]) -> dict[str, str]:
    """{canonical: [surface, ...]} -> {surface: canonical}; the canonical form is itself a surface."""
    out: dict[str, str] = {}
    for canon, surfaces in groups.items():
        out.setdefault(canon, canon)
        for s in surfaces:
            out.setdefault(s, canon)
    return out


SYMPTOMS = _build(SYMPTOM_GROUPS)
CONDITIONS = _build(CONDITION_GROUPS)
MEDICATIONS = _build(MEDICATION_GROUPS)
MEDICATION_CLASS_TERMS = _build(MEDICATION_CLASSES)
INVESTIGATIONS = _build(INVESTIGATION_GROUPS)
TREATMENTS = _build(TREATMENT_GROUPS)

# ---------------------------------------------------------------------------------------------
# Dosage / frequency / route vocab (used by the regexes in extractor.py)
# ---------------------------------------------------------------------------------------------
DOSE_UNITS = [
    "mg/kg/day", "mg/kg", "mcg/kg", "mg/dl", "mg/m2", "mg/ml", "mcg/ml", "g/dl", "meq/l", "mmol/l", "ng/ml", "iu/l", "u/l",
    "milligrams", "milligram", "micrograms", "microgram", "grams", "gram", "milliliters", "milliliter", "millilitres", "millilitre",
    "mg", "mcg", "µg", "ug", "gm", "ml", "cc", "units", "unit", "iu", "meq", "mmol", "mEq",
    "tablets", "tablet", "tabs", "tab", "capsules", "capsule", "caps", "puffs", "puff", "drops", "drop", "sprays", "spray",
    "patches", "patch", "pills", "pill", "vials", "vial", "sachets", "sachet", "percent", "%", "g",
]

FREQUENCY_TERMS = [
    "once a day", "once daily", "once per day", "one time a day", "one time daily", "1x daily", "1x/day", "1 time a day",
    "twice a day", "twice daily", "twice per day", "two times a day", "two times daily", "2x daily", "2x/day", "2 times a day", "2 times daily",
    "three times a day", "three times daily", "three times per day", "3x daily", "3x/day", "3 times a day", "3 times daily",
    "four times a day", "four times daily", "4x daily", "4x/day", "4 times a day", "4 times daily",
    "every morning", "every night", "every evening", "at bedtime", "at night", "in the morning", "in the evening", "with meals",
    "before meals", "after meals", "with food", "with breakfast", "with dinner", "with supper", "with lunch", "on an empty stomach",
    "every day", "everyday", "daily", "nightly", "weekly", "once a week", "once weekly", "every week", "twice a week", "twice weekly",
    "biweekly", "monthly", "once a month", "every month", "every other day", "every other week", "every 2 weeks", "every two weeks",
    "every 3 months", "every three months", "every 6 months", "every six months", "yearly", "annually",
    "every hour", "every 2 hours", "every two hours", "every 3 hours", "every three hours", "every 4 hours", "every four hours",
    "every 4-6 hours", "every 4 to 6 hours", "every 6 hours", "every six hours", "every 6-8 hours", "every 8 hours", "every eight hours",
    "every 12 hours", "every twelve hours", "every 24 hours", "every 48 hours", "every 72 hours",
    "q1h", "q2h", "q3h", "q4h", "q4-6h", "q6h", "q6-8h", "q8h", "q12h", "q24h", "q48h", "q72h", "qd", "qhs", "qam", "qpm",
    "bid", "tid", "qid", "qod", "qw", "qweek", "qmonth", "b.i.d.", "t.i.d.", "q.i.d.", "q.d.", "q.h.s.", "prn", "as needed",
    "when needed", "if needed", "as required", "stat", "once", "one time", "single dose", "one dose", "x1", "x 1",
    "per day", "a day", "/day", "/d", "per week", "a week", "/week", "/wk", "per month", "a month", "/month", "per dose", "/dose",
]

ROUTE_TERMS = [
    "by mouth", "orally", "oral", "po", "p.o.", "per os", "sublingual", "under the tongue", "buccal",
    "intravenous", "intravenously", "iv", "i.v.", "iv push", "iv drip", "iv infusion", "infusion", "drip",
    "intramuscular", "intramuscularly", "im", "i.m.", "subcutaneous", "subcutaneously", "subq", "sq", "s.c.", "sub-q", "under the skin",
    "topical", "topically", "on the skin", "transdermal", "transdermally",
    "inhaled", "inhalation", "by inhalation", "via inhaler", "via nebulizer", "nebulized", "intranasal", "intranasally", "nasal",
    "in each nostril", "per nostril", "ophthalmic", "in each eye", "in the eye", "in both eyes", "in the right eye", "in the left eye",
    "otic", "in each ear", "in the ear", "in both ears", "rectal", "rectally", "per rectum", "vaginal", "vaginally", "per vagina",
    "intravaginal", "intrathecal", "epidurally", "intra-articular", "intraarticular", "into the joint", "intralesional", "intradermal",
    "via g-tube", "via peg", "via ng tube", "per tube", "per g-tube", "enteral",
]

__all__ = [
    "SYMPTOMS", "CONDITIONS", "MEDICATIONS", "MEDICATION_CLASS_TERMS", "INVESTIGATIONS", "TREATMENTS",
    "SECTION_ALIASES", "MTS_SECTION_MAP", "CASE_SENSITIVE_ABBREV", "DOSE_UNITS", "FREQUENCY_TERMS", "ROUTE_TERMS",
]
