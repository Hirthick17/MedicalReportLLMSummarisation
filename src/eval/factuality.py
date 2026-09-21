"""
Basic factuality checking for generated clinical notes (Person 3, Review 2).

    result = check_factuality(source_dialogue, reference_note, prediction, dataset="aci_bench", section=None)

Every check is built on the Clinical Fact Extractor (src/cfe): the transcript, the reference note and
the generated note are each turned into a set of (category, canonical, polarity) facts, and the
generated note is compared against the transcript (faithfulness) and the reference (coverage).

Error types (the six named in the project report) and how each is operationalised:

  hallucination        a clinical entity in the prediction (symptom / history / diagnosis / medication /
                       investigation) whose canonical form appears nowhere in the SOURCE transcript
                       (`unsupported_vs_source`), with a looser variant that also accepts the reference
                       (`unsupported_vs_source_or_reference`, tolerant of lexicon misses on the dialogue side)
  incorrect_diagnosis  a diagnosis the prediction asserts (assessment context, polarity present) that is
                       neither mentioned as a condition in the source nor asserted in the reference
  incorrect_medication a specific drug (not a class word) in the prediction absent from source and reference
  incorrect_dosage     a (drug, value, unit) in the prediction whose drug is in the source but no source
                       dosage of that drug carries the same value/unit
  negation_error       a symptom / history / diagnosis / medication entity present in both prediction and reference
                       (or source) with opposite polarity (investigations excluded: "test negative" is a result)
  numerical_error      a number in the prediction that occurs neither in the source nor in the reference
                       (word numbers in the source are converted: "twenty five" -> 25)
  missing_information  reference entities (by category) not present in the prediction

Rates reported per item (and averaged per split by run_eval.py):

  hallucination_rate       |unsupported_vs_source| / |prediction entities|
  negation_flip_rate       |polarity conflicts| / |entities shared with the reference|
  numerical_consistency    1 - |unsupported numbers| / |prediction numbers|
  clinical_coverage        |reference entities found in prediction| / |reference entities|
  coverage_<category>      the same per category

All rates are None when the denominator is zero; the aggregator skips those items for that rate.
"""

from __future__ import annotations

import re
from typing import Iterable

from src.cfe import Fact, extract_facts

CORE = ("symptom", "medical_history", "diagnosis", "medication", "investigation")
IMPORTANT = ("diagnosis", "medication", "symptom", "medical_history")     # "important clinical information"

_UNITS_WORDS = {"zero": 0, "one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9, "ten": 10,
                "eleven": 11, "twelve": 12, "thirteen": 13, "fourteen": 14, "fifteen": 15, "sixteen": 16, "seventeen": 17, "eighteen": 18,
                "nineteen": 19, "twenty": 20, "thirty": 30, "forty": 40, "fifty": 50, "sixty": 60, "seventy": 70, "eighty": 80, "ninety": 90,
                "hundred": 100, "half": 0.5, "quarter": 0.25}
_NUM_RE = re.compile(r"(?<![a-z])\d+(?:[.,]\d+)?(?![a-z])", re.IGNORECASE)
_WORDNUM_RE = re.compile(r"\b(?:(?:twenty|thirty|forty|fifty|sixty|seventy|eighty|ninety)(?:[\s-](?:one|two|three|four|five|six|seven|eight|nine))?"
                         r"|(?:one|two|three|four|five|six|seven|eight|nine|ten|eleven|twelve|thirteen|fourteen|fifteen|sixteen|seventeen|eighteen|nineteen)"
                         r"(?:\s+hundred)?)\b", re.IGNORECASE)


def _norm_num(s: str) -> str:
    s = s.replace(",", ".")
    try:
        v = float(s)
        return str(int(v)) if v.is_integer() else f"{v:g}"
    except ValueError:
        return s


def numbers_in(text: str) -> set[str]:
    """Digits and BP-style pairs in a text, plus word numbers converted to digits."""
    out = set()
    for m in _NUM_RE.finditer(text):
        out.add(_norm_num(m.group(0)))
    for m in re.finditer(r"\b(\d{2,3})\s*/\s*(\d{2,3})\b", text):
        out.add(f"{m.group(1)}/{m.group(2)}")
    for m in _WORDNUM_RE.finditer(text):
        parts = re.split(r"[\s-]+", m.group(0).lower())
        val, cur = 0, 0
        for p in parts:
            if p == "hundred":
                cur = (cur or 1) * 100
            else:
                cur += _UNITS_WORDS.get(p, 0)
        val = cur
        if val:
            out.add(str(val))
    return out


def entity_set(facts: Iterable[Fact], cats=CORE, skip_class: bool = True) -> dict[str, tuple[str, str]]:
    """canonical -> (category, polarity). Present beats absent when the same entity occurs twice."""
    out: dict[str, tuple[str, str]] = {}
    for f in facts:
        if f.category not in cats or (skip_class and f.is_class) or f.experiencer == "family":
            continue
        prev = out.get(f.canonical)
        if prev is None or (prev[1] == "absent" and f.polarity == "present"):
            out[f.canonical] = (f.category, f.polarity)
    return out


def _dosages(facts: Iterable[Fact]) -> dict[str, set[tuple[str, str]]]:
    d: dict[str, set[tuple[str, str]]] = {}
    for f in facts:
        if f.category == "dosage" and f.drug:
            d.setdefault(f.drug, set()).add((f.value or "", (f.unit or "").lower()))
    return d


def check_factuality(source: str, reference: str, prediction: str, dataset: str | None = None, section: str | None = None,
                     facts: dict | None = None) -> dict:
    """facts: optional {"source": [Fact], "reference": [Fact]} cache to avoid re-extracting per system."""
    facts = facts or {}
    sf = facts.get("source") or extract_facts(source, kind="dialogue")
    rf = facts.get("reference") or extract_facts(reference, kind="note", default_section=section)
    pf = extract_facts(prediction, kind="note", default_section=section)

    s_ent, r_ent, p_ent = entity_set(sf), entity_set(rf), entity_set(pf)
    s_all = {f.canonical for f in sf}                       # any category incl. treatments / classes
    r_all = {f.canonical for f in rf}

    # --- hallucination (unsupported entities)
    unsupported_src = sorted(e for e in p_ent if e not in s_ent and e not in s_all)
    unsupported_any = sorted(e for e in unsupported_src if e not in r_ent and e not in r_all)
    halluc_rate = len(unsupported_src) / len(p_ent) if p_ent else None
    halluc_rate_strict = len(unsupported_any) / len(p_ent) if p_ent else None

    # --- diagnosis
    s_conditions = {f.canonical for f in sf if f.category in ("diagnosis", "medical_history")}
    r_dx = {f.canonical for f in rf if f.category == "diagnosis" and f.polarity == "present" and f.subtype == "asserted"}
    p_dx = {f.canonical for f in pf if f.category == "diagnosis" and f.polarity == "present" and f.subtype == "asserted"}
    incorrect_dx = sorted(d for d in p_dx if d not in s_conditions and d not in r_dx)
    missing_dx = sorted(d for d in r_dx if d not in {f.canonical for f in pf if f.category in ("diagnosis", "medical_history", "symptom")})

    # --- medication / dosage
    s_meds = {f.canonical for f in sf if f.category == "medication" and not f.is_class}
    r_meds = {f.canonical for f in rf if f.category == "medication" and not f.is_class}
    p_meds = {f.canonical for f in pf if f.category == "medication" and not f.is_class}
    incorrect_meds = sorted(m for m in p_meds if m not in s_meds and m not in r_meds)
    missing_meds = sorted(m for m in r_meds if m not in p_meds)
    s_dose, p_dose = _dosages(sf), _dosages(pf)
    r_dose = _dosages(rf)
    dosage_mismatch, dosage_checked = [], 0
    for drug, vals in p_dose.items():
        ref_vals = s_dose.get(drug, set()) | r_dose.get(drug, set())
        if not ref_vals:
            continue
        dosage_checked += len(vals)
        for v in vals:
            if not any(v[0] == rv[0] and (v[1] == rv[1] or not v[1] or not rv[1]) for rv in ref_vals):
                dosage_mismatch.append({"drug": drug, "predicted": f"{v[0]} {v[1]}", "source": sorted(f"{a} {b}" for a, b in ref_vals)})

    # --- negation. Investigations are excluded: "troponin negative" / "CBC normal" is a *result*, not the
    #     absence of the test, so their polarity is not comparable (found as a false positive on MTS-Dialog).
    NEG_CATS = ("symptom", "medical_history", "diagnosis", "medication")
    shared_ref = [e for e in p_ent if e in r_ent and p_ent[e][0] in NEG_CATS]
    flips_ref = sorted(e for e in shared_ref if p_ent[e][1] != r_ent[e][1])
    shared_src = [e for e in p_ent if e in s_ent and p_ent[e][0] in NEG_CATS]
    flips_src = sorted(e for e in shared_src if p_ent[e][1] != s_ent[e][1])
    neg_flip_rate = len(flips_ref) / len(shared_ref) if shared_ref else None
    neg_flip_rate_src = len(flips_src) / len(shared_src) if shared_src else None

    # --- numbers
    s_num, r_num, p_num = numbers_in(source), numbers_in(reference), numbers_in(prediction)
    bad_nums = sorted(n for n in p_num if n not in s_num and n not in r_num)
    num_consistency = 1 - len(bad_nums) / len(p_num) if p_num else None

    # --- coverage (missing information)
    covered = [e for e in r_ent if e in p_ent]
    coverage = len(covered) / len(r_ent) if r_ent else None
    cov_cat, missing_by_cat = {}, {}
    for c in CORE:
        rc = [e for e, (cat, _) in r_ent.items() if cat == c]
        cov_cat[f"coverage_{c}"] = (sum(1 for e in rc if e in p_ent) / len(rc)) if rc else None
        missing_by_cat[c] = sorted(e for e in rc if e not in p_ent)
    r_imp = [e for e, (cat, _) in r_ent.items() if cat in IMPORTANT]
    coverage_important = (sum(1 for e in r_imp if e in p_ent) / len(r_imp)) if r_imp else None

    return {
        "n_source_facts": len(sf), "n_reference_facts": len(rf), "n_prediction_facts": len(pf),
        "n_pred_entities": len(p_ent), "n_ref_entities": len(r_ent), "n_src_entities": len(s_ent),
        "hallucination_rate": halluc_rate, "hallucination_rate_strict": halluc_rate_strict,
        "unsupported_vs_source": unsupported_src, "unsupported_vs_source_or_reference": unsupported_any,
        "incorrect_diagnosis": incorrect_dx, "missing_diagnosis": missing_dx, "n_pred_diagnoses": len(p_dx), "n_ref_diagnoses": len(r_dx),
        "incorrect_medication": incorrect_meds, "missing_medication": missing_meds, "n_pred_meds": len(p_meds), "n_ref_meds": len(r_meds),
        "dosage_mismatch": dosage_mismatch, "n_dosages_checked": dosage_checked,
        "negation_flip_rate": neg_flip_rate, "negation_flips": flips_ref, "n_shared_with_reference": len(shared_ref),
        "negation_flip_rate_vs_source": neg_flip_rate_src, "negation_flips_vs_source": flips_src,
        "numerical_consistency": num_consistency, "unsupported_numbers": bad_nums, "n_pred_numbers": len(p_num),
        "clinical_coverage": coverage, "clinical_coverage_important": coverage_important, **cov_cat, "missing_by_category": missing_by_cat,
        "pred_negated_entities": sorted(e for e, (_, pol) in p_ent.items() if pol == "absent"),
    }


__all__ = ["check_factuality", "entity_set", "numbers_in", "CORE", "IMPORTANT"]
