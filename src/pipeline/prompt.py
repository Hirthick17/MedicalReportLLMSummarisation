"""
Fact-conditioned prompt — the single source of truth for training, inference and the demo.

    messages = build_messages(dialogue, dataset="aci_bench")
    messages = build_messages(dialogue, dataset="mts_dialog", section="GENHX")
    messages = record_messages(rec)                 # a unified-schema record (data/processed/*.jsonl)

Layout of the user turn:

    <task instruction>                 same per-dataset text as the Review 2 baseline
    EXTRACTED FACTS (...):             fact table from the transcript (fact_table.py)
    - Symptoms: cough; fever (DENIED)
    ...
    TRANSCRIPT:
    <dialogue>

The transcript stays in the prompt: the CFE's lexicon misses facts, and the model must still be able
to use them. SYSTEM / TASK / MTS_SECTIONS are copied from the Review 2 kernels
(kaggle/baseline/baseline_qlora.py) so the only difference between the baseline and the
fact-conditioned run is FACT_RULES and the fact table. A Kaggle kernel cannot import src/, so the
fact-conditioned kernels must copy this module verbatim; PROMPT_VERSION is recorded in their
training_config.json to detect drift.
"""

from __future__ import annotations

from src.cfe import Fact, extract_facts

from .fact_table import format_fact_table

PROMPT_VERSION = "factcond-v1"

SYSTEM = ("You are a clinical documentation assistant. Given the transcript of a doctor-patient "
          "consultation, write the clinical note. Include only information stated in the transcript.")
FACT_RULES = (" A list of facts extracted automatically from the transcript is given before it. "
              "Use these facts, keep every fact marked (DENIED) as denied or negative, and do not state "
              "a fact marked (POSSIBLE) as certain. The list may be incomplete: you may use other facts "
              "that are clearly stated in the transcript, but never add symptoms, findings, test results, "
              "medications or doses that are not in the transcript.")
MTS_SECTIONS = {
    "FAM/SOCHX": "FAMILY HISTORY / SOCIAL HISTORY", "GENHX": "HISTORY OF PRESENT ILLNESS",
    "PASTMEDICALHX": "PAST MEDICAL HISTORY", "CC": "CHIEF COMPLAINT", "PASTSURGICAL": "PAST SURGICAL HISTORY",
    "ALLERGY": "ALLERGIES", "ROS": "REVIEW OF SYSTEMS", "MEDICATIONS": "MEDICATIONS", "ASSESSMENT": "ASSESSMENT",
    "EXAM": "PHYSICAL EXAM", "DIAGNOSIS": "DIAGNOSIS", "DISPOSITION": "DISPOSITION", "PLAN": "PLAN",
    "EDCOURSE": "EMERGENCY DEPARTMENT COURSE", "IMMUNIZATIONS": "IMMUNIZATIONS", "IMAGING": "IMAGING",
    "GYNHX": "GYNECOLOGIC HISTORY", "PROCEDURES": "PROCEDURES", "OTHER_HISTORY": "OTHER HISTORY", "LABS": "LABS",
}
TASK = {
    "aci_bench": ("Write the complete clinical note for this encounter, using upper-case section headers such as "
                  "CHIEF COMPLAINT, HISTORY OF PRESENT ILLNESS, REVIEW OF SYSTEMS, PHYSICAL EXAM, RESULTS, "
                  "ASSESSMENT AND PLAN as applicable."),
    "dialogue_soap": ("Write a SOAP note with four paragraphs labelled S:, O:, A:, P: "
                      "(Subjective, Objective, Assessment, Plan)."),
    "mts_dialog": "Write the {section} section of the clinical note.",
}


def instruction(dataset: str, section: str | None = None) -> str:
    if dataset == "mts_dialog":
        return TASK["mts_dialog"].format(section=MTS_SECTIONS.get(section or "", section or "requested"))
    return TASK.get(dataset, TASK["aci_bench"])


def build_messages(dialogue: str, dataset: str = "aci_bench", section: str | None = None,
                   facts: list[Fact] | None = None) -> list[dict]:
    """Chat messages for one encounter. `facts` may be passed in from a cache; otherwise they are
    extracted from `dialogue` (never from a reference note)."""
    if facts is None:
        facts = extract_facts(dialogue, kind="dialogue")
    user = f"{instruction(dataset, section)}\n\n{format_fact_table(facts)}\n\nTRANSCRIPT:\n{dialogue}"
    return [{"role": "system", "content": SYSTEM + FACT_RULES}, {"role": "user", "content": user}]


def record_messages(rec: dict, facts: list[Fact] | None = None) -> list[dict]:
    """build_messages for a unified-schema record (REVIEW2_BASELINE.md §8.3 / data/processed)."""
    section = (rec.get("metadata") or {}).get("section_header")
    return build_messages(rec["source_dialogue"], rec["dataset"], section, facts)
