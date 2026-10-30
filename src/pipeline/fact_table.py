"""
Fact table for fact-conditioned generation (Review 3, Stage 2 input).

    facts = extract_facts(dialogue, kind="dialogue")
    table = format_fact_table(facts)

The CFE returns one Fact per *mention*. A dialogue mentions the same thing several times and with
different status: the doctor's question "any chest pain?" is extracted as an uncertain mention, the
patient's "no chest pain" as a certain negated one. The table shows one line item per canonical
entity, with the status resolved as follows:

  1. certain mentions beat uncertain ones (questions, "might", "possible")
  2. among the remaining mentions, patient statements beat doctor statements
  3. among those, the last mention in the transcript wins (later corrections override)

Status tags shown to the model: (DENIED) absent · (POSSIBLE) uncertain · (FAMILY) family history ·
(PAST) historical. Present, certain, current, patient facts carry no tag.

The table is built from the SOURCE dialogue only, never from the reference note: at inference
time the dialogue is all there is, so training on reference-derived facts would leak the target.
"""

from __future__ import annotations

from typing import Iterable

from src.cfe import Fact

# (category, line label) in display order; dosage and numeric are folded in below
SECTIONS = [
    ("symptom", "Symptoms"),
    ("medical_history", "Medical history"),
    ("diagnosis", "Diagnoses"),
    ("medication", "Medications"),
    ("investigation", "Tests / investigations"),
    ("treatment", "Treatments / plan"),
    ("numeric", "Measurements"),
]
HEADER = "EXTRACTED FACTS (automatic, from the transcript; may be incomplete):"
NUMERIC_LABEL = {"duration": "duration", "age": "age", "follow_up_timing": "follow-up in"}


def _rank(f: Fact, order: int) -> tuple:
    return (f.certainty == "certain", f.speaker == "patient", order)


def _resolve(facts: list[Fact]) -> dict[tuple[str, str], tuple[int, Fact]]:
    """{(category, canonical): (first position, winning mention)}"""
    best: dict[tuple[str, str], tuple[int, int, Fact]] = {}
    for i, f in enumerate(facts):
        key = (f.category, f.canonical)
        if key not in best:
            best[key] = (i, i, f)
        else:
            first, j, g = best[key]
            if _rank(f, i) >= _rank(g, j):
                best[key] = (first, i, f)
    return {k: (first, f) for k, (first, _, f) in best.items()}


def _tags(f: Fact) -> str:
    tags = []
    if f.polarity == "absent":
        tags.append("DENIED")
    elif f.certainty == "uncertain":
        tags.append("POSSIBLE")
    if f.experiencer == "family":
        tags.append("FAMILY")
    elif f.temporality == "historical" and f.category != "medical_history":
        tags.append("PAST")
    return f" ({', '.join(tags)})" if tags else ""


def _dose_text(d: Fact) -> str:
    parts = [f"{d.value} {d.unit}" if d.unit else d.value or d.text]
    parts += [p for p in (d.route, d.frequency) if p]
    return " ".join(parts)


def _numeric_text(f: Fact) -> str:
    if f.subtype == "age" and f.value:
        return f"age {f.value}"                 # surface is "39-year-old"
    label = NUMERIC_LABEL.get(f.subtype or "")
    return f"{label} {f.text}" if label else f.canonical


def fact_items(facts: Iterable[Fact]) -> dict[str, list[str]]:
    """{category: [item, ...]} in order of first mention; dosages are merged into their medication."""
    facts = list(facts)
    doses: dict[str, list[str]] = {}
    for f in facts:
        if f.category == "dosage" and f.drug:
            text = _dose_text(f)
            if text not in doses.setdefault(f.drug, []):
                doses[f.drug].append(text)

    resolved = _resolve([f for f in facts if f.category != "dosage"])
    items: dict[str, list[str]] = {cat: [] for cat, _ in SECTIONS}
    for (cat, canon), (_, f) in sorted(resolved.items(), key=lambda kv: kv[1][0]):
        if cat not in items:
            continue
        if cat == "numeric":
            items[cat].append(_numeric_text(f))
            continue
        text = canon
        if cat == "medication" and canon in doses:
            text += " " + "; ".join(doses.pop(canon))
        items[cat].append(text + _tags(f))
    # a dosage whose drug was not matched as a medication on its own still belongs in the table
    items["medication"] += [f"{drug} {'; '.join(ds)}" for drug, ds in doses.items()]
    return items


def format_fact_table(facts: Iterable[Fact], max_per_category: int = 25) -> str:
    """The fact table as prompt text; empty categories are left out (the CFE's recall is limited,
    so "Medications: none" would tell the model to drop a drug the lexicon missed)."""
    items = fact_items(facts)
    lines = [HEADER]
    for cat, label in SECTIONS:
        if items[cat]:
            lines.append(f"- {label}: " + "; ".join(items[cat][:max_per_category]))
    if len(lines) == 1:
        lines.append("- (no facts found)")
    return "\n".join(lines)
