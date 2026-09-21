"""
Rule-based Clinical Fact Extractor (CFE) — Review 2 "basic" version.

    facts = extract_facts(text)                      # auto-detects dialogue vs. note
    facts = extract_facts(note, kind="note")
    facts = extract_facts(section_text, kind="note", default_section="hpi")   # MTS-Dialog

A Fact is one clinical assertion with provenance:

    category     symptom | medical_history | diagnosis | medication | dosage | investigation | treatment | numeric
    text         surface string as it appears in the document
    canonical    normalized form (lexicon canonical, or "<drug> <value><unit>" for dosages)
    polarity     present | absent            <- NEGATION (NegEx-style, negation.py)
    certainty    certain | uncertain
    temporality  current | historical
    experiencer  patient | family
    section      note section id, or None for dialogue
    speaker      doctor | patient | other, or None for notes
    start, end   character offsets in the ORIGINAL text (provenance for Review 3 Stage 4)
    value/unit/frequency/route/drug   for dosage facts; value/unit/subtype for numeric facts

Pipeline per document
  1. segment: dialogue turns (speaker) or note sections (header) -> sentences with offsets
  2. lexicon match per sentence, longest-match-wins across categories
  3. assertion per match (negation / uncertainty / historical / family) from the sentence context
  4. dialogue-only rule: a bare "no" patient answer negates the terms asked in the previous doctor turn
  5. condition mentions are routed to diagnosis vs. medical_history by section + temporality
  6. dosage / vitals / lab-value / duration / follow-up-timing regexes, attached to the nearest term
"""

from __future__ import annotations

import re
from dataclasses import asdict, dataclass, field
from typing import Iterable

from . import lexicon as L
from .negation import Assertion, assert_status

# ---------------------------------------------------------------------------------------------
# data model
# ---------------------------------------------------------------------------------------------

@dataclass
class Fact:
    category: str
    text: str
    canonical: str
    polarity: str = "present"
    certainty: str = "certain"
    temporality: str = "current"
    experiencer: str = "patient"
    section: str | None = None
    speaker: str | None = None
    start: int = -1
    end: int = -1
    sentence_idx: int = -1
    value: str | None = None
    unit: str | None = None
    frequency: str | None = None
    route: str | None = None
    drug: str | None = None
    subtype: str | None = None
    trigger: str | None = None
    is_class: bool = False

    def to_dict(self) -> dict:
        return asdict(self)

    @property
    def negated(self) -> bool:
        return self.polarity == "absent"


@dataclass
class Sentence:
    text: str
    start: int          # offset in the original document
    speaker: str | None
    section: str | None
    idx: int
    turn_idx: int = -1


# ---------------------------------------------------------------------------------------------
# segmentation
# ---------------------------------------------------------------------------------------------

_SPEAKER_RE = re.compile(
    r"^\s*(?:\[(?P<b>doctor|patient|patient_guest|guest|nurse|caregiver|family|other|clinician)[^\]]*\]"
    r"|(?P<c>doctor|patient|dr|physician|clinician|nurse|guest|patient's (?:mother|father|wife|husband|son|daughter))\s*:)\s*",
    re.IGNORECASE,
)
_SECTION_RE = re.compile(r"^\s*(?P<h>[A-Za-z][A-Za-z /&()'-]{0,60}?)\s*:?\s*$")
_SOAP_INLINE_RE = re.compile(r"^\s*(?P<h>[SOAP]|Subjective|Objective|Assessment|Plan)\s*:\s*(?P<rest>.*)$", re.IGNORECASE)
_SENT_SPLIT = re.compile(r"(?<=[.!?])\s+(?=[A-Za-z0-9\[(\"'])|\n+")

_SECTION_LOOKUP: dict[str, str] = {}
for _sid, _aliases in L.SECTION_ALIASES.items():
    for _a in _aliases:
        _SECTION_LOOKUP[_a.lower()] = _sid


def _section_id(header: str) -> str | None:
    h = re.sub(r"[^a-z0-9/& ]", " ", header.lower()).strip()
    h = re.sub(r"\s+", " ", h)
    return _SECTION_LOOKUP.get(h)


def _norm_speaker(tag: str) -> str:
    t = tag.lower()
    if t.startswith("doctor") or t.startswith("dr") or t in ("physician", "clinician", "nurse"):
        return "doctor"
    if t.startswith("patient_guest") or t.startswith("guest") or t.startswith("patient's"):
        return "other"
    if t.startswith("patient"):
        return "patient"
    return "other"


def detect_kind(text: str) -> str:
    """'dialogue' if speaker tags dominate the line starts, else 'note'."""
    lines = [ln for ln in text.splitlines() if ln.strip()]
    if not lines:
        return "note"
    tagged = sum(1 for ln in lines if _SPEAKER_RE.match(ln))
    return "dialogue" if tagged >= max(2, 0.3 * len(lines)) else "note"


def _split_sentences(text: str, base: int, speaker, section, sentences: list[Sentence], turn_idx: int) -> None:
    pos = 0
    for m in _SENT_SPLIT.finditer(text):
        chunk = text[pos:m.start()]
        if chunk.strip():
            lead = len(chunk) - len(chunk.lstrip())
            sentences.append(Sentence(chunk.strip(), base + pos + lead, speaker, section, len(sentences), turn_idx))
        pos = m.end()
    chunk = text[pos:]
    if chunk.strip():
        lead = len(chunk) - len(chunk.lstrip())
        sentences.append(Sentence(chunk.strip(), base + pos + lead, speaker, section, len(sentences), turn_idx))


def segment(text: str, kind: str = "auto", default_section: str | None = None) -> tuple[str, list[Sentence]]:
    if kind == "auto":
        kind = detect_kind(text)
    sentences: list[Sentence] = []
    offset = 0
    turn = -1
    section = default_section
    for raw in text.splitlines(keepends=True):
        line = raw.rstrip("\r\n")
        if not line.strip():
            offset += len(raw)
            continue
        if kind == "dialogue":
            m = _SPEAKER_RE.match(line)
            if m:
                turn += 1
                speaker = _norm_speaker(m.group("b") or m.group("c"))
                _split_sentences(line[m.end():], offset + m.end(), speaker, None, sentences, turn)
            else:
                _split_sentences(line, offset, sentences[-1].speaker if sentences else None, None, sentences, turn)
        else:
            ms = _SOAP_INLINE_RE.match(line)
            mh = _SECTION_RE.match(line)
            if ms and ms.group("h").lower() in ("s", "o", "a", "p", "subjective", "objective", "assessment", "plan"):
                section = _section_id(ms.group("h")) or section
                _split_sentences(ms.group("rest"), offset + ms.start("rest"), None, section, sentences, turn)
            elif mh and _section_id(mh.group("h")) and len(line.split()) <= 6:
                section = _section_id(mh.group("h"))
            else:
                # inline "HEADER: text" on one line (e.g. "ASSESSMENT: ...")
                mi = re.match(r"^\s*([A-Za-z][A-Za-z /&-]{1,40}):\s+(.*)$", line)
                if mi and _section_id(mi.group(1)):
                    section = _section_id(mi.group(1))
                    _split_sentences(mi.group(2), offset + mi.start(2), None, section, sentences, turn)
                else:
                    _split_sentences(line, offset, None, section, sentences, turn)
        offset += len(raw)
    return kind, sentences


# ---------------------------------------------------------------------------------------------
# lexicon matching
# ---------------------------------------------------------------------------------------------

_CATEGORY_LEX: list[tuple[str, dict[str, str], int]] = [   # (category, lexicon, priority for ties)
    ("medication", L.MEDICATIONS, 6),
    ("medication_class", L.MEDICATION_CLASS_TERMS, 2),
    ("condition", L.CONDITIONS, 5),
    ("symptom", L.SYMPTOMS, 4),
    ("investigation", L.INVESTIGATIONS, 3),
    ("treatment", L.TREATMENTS, 1),
]


def _lex_regex(lex: dict[str, str]) -> re.Pattern:
    alts = sorted(lex.keys(), key=len, reverse=True)
    esc = lambda a: re.escape(a).replace(r"\ ", r"[\s-]+")
    long_ = "|".join(esc(a) for a in alts if len(a) > 3)
    short = "|".join(esc(a) for a in alts if len(a) <= 3)
    body = r"(?:" + long_ + r")(?:e?s)?"
    if short:
        body += r"|(?:" + short + r")"            # abbreviations: exact form only, no plural
    return re.compile(r"(?<![a-z0-9])(?:" + body + r")(?![a-z0-9])", re.IGNORECASE)


_CATEGORY_RE = [(cat, lex, pri, _lex_regex(lex)) for cat, lex, pri in _CATEGORY_LEX]
_SHORT_ABBREV = {k for k in list(L.CONDITIONS) + list(L.INVESTIGATIONS) if len(k) <= 3 and k.isalpha()} | L.CASE_SENSITIVE_ABBREV


_NORM_LEX: dict[int, dict[str, str]] = {}


def _norm_key(s: str) -> str:
    return re.sub(r"[\s-]+", " ", s.lower()).strip()


def _lookup(lex: dict[str, str], surface: str) -> str | None:
    nl = _NORM_LEX.get(id(lex))
    if nl is None:
        nl = _NORM_LEX[id(lex)] = {_norm_key(k): v for k, v in lex.items()}
    s = _norm_key(surface)
    for cand in (s, s[:-1] if s.endswith("s") else None, s[:-2] if s.endswith("es") else None):
        if cand and cand in nl:
            return nl[cand]
    return None


def _match_terms(sentence: str) -> list[tuple[int, int, str, str, str]]:
    """All lexicon hits in a sentence -> [(start, end, category, surface, canonical)], overlaps resolved."""
    hits = []
    for cat, lex, pri, rx in _CATEGORY_RE:
        for m in rx.finditer(sentence):
            surf = m.group(0)
            key = _norm_key(surf)
            if key in _SHORT_ABBREV and not surf.isupper():
                continue                                   # "as", "pe", "ms" ... only count in upper case
            canon = _lookup(lex, surf)
            if canon is None:
                continue
            hits.append((m.start(), m.end(), cat, surf, canon, pri))
    # longest match wins; ties by priority
    hits.sort(key=lambda h: (h[0], -(h[1] - h[0]), -h[5]))
    kept: list = []
    for h in hits:
        if kept and h[0] < kept[-1][1]:
            continue
        kept.append(h)
    return [(s, e, c, surf, canon) for s, e, c, surf, canon, _ in kept]


# ---------------------------------------------------------------------------------------------
# dosage / numeric / follow-up regexes
# ---------------------------------------------------------------------------------------------

_NUM = r"(?P<value>\d+(?:[.,]\d+)?(?:\s*(?:-|to)\s*\d+(?:[.,]\d+)?)?)"
_UNITS = "|".join(re.escape(u) for u in sorted(L.DOSE_UNITS, key=len, reverse=True))
_DOSE_RE = re.compile(_NUM + r"\s*(?P<unit>" + _UNITS + r")(?![a-z])", re.IGNORECASE)
_FREQ_RE = re.compile(r"(?<![a-z0-9])(?P<freq>" + "|".join(re.escape(f) for f in sorted(L.FREQUENCY_TERMS, key=len, reverse=True)) + r")(?![a-z0-9])", re.IGNORECASE)
_ROUTE_RE = re.compile(r"(?<![a-z0-9])(?P<route>" + "|".join(re.escape(r) for r in sorted(L.ROUTE_TERMS, key=len, reverse=True)) + r")(?![a-z0-9])", re.IGNORECASE)

_WORDNUM = r"(?:\d+|a|an|one|two|three|four|five|six|seven|eight|nine|ten|twelve|couple of|couple|few|several|half a|half an)"
_DURATION_RE = re.compile(r"(?<![a-z0-9])(?P<value>" + _WORDNUM + r")\s*(?:-|\s)?\s*(?P<unit>minutes?|hours?|days?|weeks?|months?|years?|yrs?|wks?)(?![a-z])(?P<ago>\s+ago)?", re.IGNORECASE)
_AGE_RE = re.compile(r"(?<![a-z0-9])(?P<value>\d{1,3})[\s-]*(?:(?P<unit>year|yr|month|mo|week|wk|day)s?[\s-]*old|(?P<unit2>y/o|yo|y\.o\.))(?![a-z])", re.IGNORECASE)
_BP_RE = re.compile(r"(?P<value>\b1?\d{2}\s*/\s*\d{2,3}\b)(?:\s*mm\s*hg)?", re.IGNORECASE)
_VITAL_RE = re.compile(
    r"(?P<label>blood pressure|bp|heart rate|pulse|hr|temperature|temp|oxygen saturation|o2 sat(?:uration)?|spo2|sats?|pulse ox|respiratory rate|rr|weight|height|bmi)"
    r"\s*(?:is|was|of|at|:|=|-|—|reads?|came back|came in at)?\s*(?P<value>\d{2,3}(?:\.\d+)?(?:\s*/\s*\d{2,3})?)\s*(?P<unit>%|percent|mmhg|bpm|degrees|°f|°c|f|c|lbs?|pounds|kg|kilograms|cm|ft|inches|in)?",
    re.IGNORECASE)
_LAB_RE = re.compile(
    r"(?P<label>a1c|hemoglobin a1c|hba1c|glucose|blood sugar|sugar|creatinine|potassium|sodium|hemoglobin|hgb|hematocrit|ldl|hdl|cholesterol|triglycerides|tsh|ejection fraction|ef|crp|esr|wbc|white count|platelets|inr|bun|egfr|gfr|psa|ferritin|vitamin d|b12|mcv|troponin|bnp|lactate|bilirubin|albumin|alt|ast|calcium|magnesium|phosphorus|uric acid|iron|hcg|prolactin|testosterone|cortisol|vitamin d level|c-reactive protein|sed rate|sedimentation rate)"
    r"\s*(?:level|levels|value|count|number|numbers)?\s*(?:is|was|of|at|:|=|-|—|were|are|came back at|came back|reads?|around|about|elevated to|elevated at|down to|up to|increased to|decreased to)?\s*(?P<value>\d+(?:\.\d+)?)\s*(?P<unit>%|percent|mg/dl|mg/dL|mmol/l|mmol/L|g/dl|g/dL|meq/l|mEq/L|ng/ml|ng/mL|pg/ml|mm/h|mm/hr|mg/l|mg/L|u/l|U/L|iu/l|IU/L|k/ul|K/uL|/ul|fl|fL|ml/min|mL/min)?",
    re.IGNORECASE)
_FOLLOWUP_RE = re.compile(
    r"(?P<cue>follow[\s-]?up|come back|see (?:you|me|him|her|the patient)(?: back| again)?|return|recheck|re-check|revisit|check back|be seen|reassess|re-evaluate|reevaluate|next visit|next appointment|repeat (?:labs|imaging|x-ray|mri|ct|ultrasound|echo|ekg|ecg|blood work))"
    r"[^.;\n]{0,40}?\b(?:in|within|after|every|over the next)\s+(?P<value>" + _WORDNUM + r"(?:\s*(?:-|to)\s*\d+)?)\s*(?:-|\s)?\s*(?P<unit>days?|weeks?|months?|years?|wks?)(?![a-z])",
    re.IGNORECASE)


# ---------------------------------------------------------------------------------------------
# main extraction
# ---------------------------------------------------------------------------------------------

_BARE_NO = re.compile(r"^\s*(?:no|nope|nah|not really|never|no i haven't|no i have not|no i don't|no i do not|not that i know of|not at all|none|no ma'am|no sir|no,? not really|no,? i don't think so|i don't think so|no,? nothing like that)\b[\s.,!]*(?:$|thank|i|it|that|nothing|none)", re.IGNORECASE)
_BARE_YES = re.compile(r"^\s*(?:yes|yeah|yep|yup|uh-huh|mm-hmm|i do|i have|i am|definitely|absolutely|sometimes|a little|a bit|occasionally)\b", re.IGNORECASE)
_HISTORY_SECTIONS = {"pmh", "family_history", "social_history", "allergies", "medications"}
_ALLERGY_CUES = re.compile(r"(?<![a-z])(?:allerg(?:y|ies|ic) to|allergies:|allergic reaction to|intoleran(?:t|ce) to|reaction to)(?![a-z])"
                           r"(?:(?!\b(?:takes?|taking|uses?|using|started?|prescribed?|continues?|on)\b)[^.;,]){0,40}$", re.IGNORECASE)
_DX_CUES = re.compile(r"(?<![a-z])(?:diagnos(?:is|ed|e)|impression|assessment|consistent with|suggestive of|you have|this is|looks like|sounds like|likely|probably|presents? with|presenting with|secondary to|due to|caused by|indicative of|concern for|concerning for|suspect(?:ed)?|rule out|r/o|dx|working diagnosis|differential|attributed to|felt to be|thought to be|represents?|acute|new onset|newly diagnosed|admitted for|treated for|evaluation of|for evaluation)(?![a-z])", re.IGNORECASE)


def _attach_dosages(sent: Sentence, term_facts: list[Fact], facts: list[Fact]) -> None:
    """Dose / frequency / route mentions in a sentence -> dosage facts tied to the nearest medication."""
    meds = [f for f in term_facts if f.category == "medication"]
    text = sent.text
    used: set[tuple[int, int]] = set()
    for m in _DOSE_RE.finditer(text):
        s, e = m.span()
        # skip things that are vitals/labs (e.g. "120/80", "6.7 %" next to a1c) — those are numeric facts
        ctx = text[max(0, s - 25):s].lower()
        if re.search(r"(a1c|glucose|sugar|creatinine|potassium|sodium|hemoglobin|ldl|hdl|cholesterol|tsh|saturation|sat|ejection|ef|crp|esr|inr|bun|egfr|weight|height|bmi|temperature|temp|blood pressure)\b[^a-z]*$", ctx):
            continue
        drug = _nearest(meds, s, e, before=80, after=40)
        freq = _FREQ_RE.search(text, e, min(len(text), e + 60))
        route = _ROUTE_RE.search(text, e, min(len(text), e + 40))
        fact = Fact(
            category="dosage", text=text[s:e], canonical=f"{drug.canonical if drug else '?'} {m.group('value').replace(' ', '')}{m.group('unit').lower()}",
            section=sent.section, speaker=sent.speaker, start=sent.start + s, end=sent.start + e, sentence_idx=sent.idx,
            value=m.group("value").replace(",", "."), unit=m.group("unit").lower(),
            frequency=freq.group("freq").lower() if freq else None, route=route.group("route").lower() if route else None,
            drug=drug.canonical if drug else None,
        )
        if drug:
            fact.polarity, fact.certainty, fact.temporality = drug.polarity, drug.certainty, drug.temporality
            used.add((s, e))
        facts.append(fact)
    # frequency-only dosing ("take it twice a day")
    for m in _FREQ_RE.finditer(text):
        s, e = m.span()
        if any(a <= s < b + 60 for a, b in used):
            continue
        drug = _nearest(meds, s, e, before=80, after=20)
        if drug is None or drug.frequency:
            continue
        drug.frequency = m.group("freq").lower()


def _nearest(cands: list[Fact], s: int, e: int, before: int, after: int) -> Fact | None:
    best, bestd = None, 10 ** 9
    for f in cands:
        fs, fe = f.start, f.end
        if fe <= s and s - fe <= before:
            d = s - fe
        elif fs >= e and fs - e <= after:
            d = (fs - e) + 15          # prefer a preceding drug name
        else:
            continue
        if d < bestd:
            best, bestd = f, d
    return best


def _numeric_facts(sent: Sentence, facts: list[Fact], seen_dose_spans: list[tuple[int, int]]) -> None:
    text = sent.text
    base = sent.start
    taken: list[tuple[int, int]] = list(seen_dose_spans)

    for fm in _FREQ_RE.finditer(text):
        taken.append(fm.span())

    def free(s, e):
        return not any(s < b and e > a for a, b in taken)

    for m in _VITAL_RE.finditer(text):
        s, e = m.span("value")
        if not free(s, e):
            continue
        taken.append((s, e))
        facts.append(Fact("numeric", m.group(0).strip(), f"{m.group('label').lower()} {m.group('value').replace(' ', '')}",
                          section=sent.section, speaker=sent.speaker, start=base + m.start(), end=base + m.end(), sentence_idx=sent.idx,
                          value=m.group("value").replace(" ", ""), unit=(m.group("unit") or "").lower() or None, subtype="vital",
                          drug=None))
    for m in _LAB_RE.finditer(text):
        s, e = m.span("value")
        if not free(s, e):
            continue
        taken.append((s, e))
        facts.append(Fact("numeric", m.group(0).strip(), f"{m.group('label').lower()} {m.group('value')}",
                          section=sent.section, speaker=sent.speaker, start=base + m.start(), end=base + m.end(), sentence_idx=sent.idx,
                          value=m.group("value"), unit=(m.group("unit") or "").lower() or None, subtype="lab"))
    for m in _BP_RE.finditer(text):
        s, e = m.span("value")
        if not free(s, e):
            continue
        sys_, dia = [int(x) for x in re.split(r"\s*/\s*", m.group("value"))]
        if not (70 <= sys_ <= 260 and 30 <= dia <= 160):
            continue
        taken.append((s, e))
        facts.append(Fact("numeric", m.group(0).strip(), f"blood pressure {sys_}/{dia}", section=sent.section, speaker=sent.speaker,
                          start=base + s, end=base + e, sentence_idx=sent.idx, value=f"{sys_}/{dia}", unit="mmhg", subtype="vital"))
    for m in _AGE_RE.finditer(text):
        s, e = m.span()
        if not free(s, e):
            continue
        taken.append((s, e))
        u = (m.group("unit") or m.group("unit2") or "year").lower()
        u = "months" if u.startswith("mo") else "weeks" if u.startswith("w") else "days" if u == "day" else "years"
        facts.append(Fact("numeric", m.group(0).strip(), f"age {m.group('value')} {u}", section=sent.section, speaker=sent.speaker,
                          start=base + s, end=base + e, sentence_idx=sent.idx, value=m.group("value"), unit=u, subtype="age"))
    for m in _DURATION_RE.finditer(text):
        s, e = m.span()
        if not free(s, e):
            continue
        taken.append((s, e))
        unit = m.group("unit").lower().rstrip("s")
        unit = {"yr": "year", "wk": "week"}.get(unit, unit)
        facts.append(Fact("numeric", m.group(0).strip(), f"{m.group('value').lower()} {unit}{' ago' if m.group('ago') else ''}",
                          section=sent.section, speaker=sent.speaker, start=base + s, end=base + e, sentence_idx=sent.idx,
                          value=m.group("value").lower(), unit=unit, subtype="duration"))


def _followup_facts(sent: Sentence, facts: list[Fact]) -> None:
    for m in _FOLLOWUP_RE.finditer(sent.text):
        unit = m.group("unit").lower().rstrip("s")
        unit = {"wk": "week"}.get(unit, unit)
        facts.append(Fact("treatment", m.group(0).strip(), f"follow-up in {m.group('value').lower()} {unit}", section=sent.section,
                          speaker=sent.speaker, start=sent.start + m.start(), end=sent.start + m.end(), sentence_idx=sent.idx,
                          value=m.group("value").lower(), unit=unit, subtype="follow_up_timing"))


def extract_facts(text: str, kind: str = "auto", default_section: str | None = None) -> list[Fact]:
    kind, sentences = segment(text, kind, default_section)
    facts: list[Fact] = []
    per_turn_terms: dict[int, list[Fact]] = {}
    dose_spans_by_sent: dict[int, list[tuple[int, int]]] = {}

    for sent in sentences:
        term_facts: list[Fact] = []
        for s, e, cat, surf, canon in _match_terms(sent.text):
            a: Assertion = assert_status(sent.text, s, e)
            section = sent.section
            category = cat
            is_class = False
            if cat == "medication_class":
                category, is_class = "medication", True
            if cat in ("medication", "medication_class") and (section == "allergies" or _ALLERGY_CUES.search(sent.text[max(0, s - 60):s])):
                category, is_class = "medical_history", False
                a = Assertion(a.polarity, a.certainty, "historical", a.experiencer, a.trigger or "allergy")
            elif cat == "condition":
                historical = a.temporality == "historical" or a.experiencer == "family" or section in _HISTORY_SECTIONS
                category = "medical_history" if historical else "diagnosis"
            elif cat == "symptom" and (section in ("pmh", "family_history") or a.experiencer == "family"):
                category = "medical_history"
            fact = Fact(category, surf, canon, a.polarity, a.certainty, a.temporality, a.experiencer, section, sent.speaker,
                        sent.start + s, sent.start + e, sent.idx, trigger=a.trigger, is_class=is_class)
            if a.trigger == "allergy" or (category == "medical_history" and cat in ("medication", "medication_class")):
                fact.subtype = "allergy"
            if category == "diagnosis":
                # subtype records whether the mention sits in a diagnostic context; used by the evaluation
                in_dx_section = section in ("assessment", "plan", "chief_complaint")
                fact.subtype = "asserted" if (in_dx_section or _DX_CUES.search(sent.text)) else "mentioned"
            term_facts.append(fact)
        # dosages need local offsets -> temporarily shift
        local = [Fact(**{**f.to_dict(), "start": f.start - sent.start, "end": f.end - sent.start}) for f in term_facts]
        dose_facts: list[Fact] = []
        _attach_dosages(sent, local, dose_facts)
        # copy back any frequency attached to a medication fact
        for lf, f in zip(local, term_facts):
            f.frequency = lf.frequency
        facts.extend(term_facts)
        facts.extend(dose_facts)
        dose_spans_by_sent[sent.idx] = [(d.start - sent.start, d.end - sent.start) for d in dose_facts]
        _numeric_facts(sent, facts, dose_spans_by_sent[sent.idx])
        _followup_facts(sent, facts)
        per_turn_terms.setdefault(sent.turn_idx, []).extend(term_facts)

    if kind == "dialogue":
        _apply_dialogue_answers(sentences, per_turn_terms)

    facts.sort(key=lambda f: (f.start, f.end))
    return facts


def _apply_dialogue_answers(sentences: list[Sentence], per_turn: dict[int, list[Fact]]) -> None:
    """A bare 'No.' from the patient negates symptom/condition terms asked in the previous doctor turn;
    a bare 'Yes.' confirms them (and clears the 'uncertain' flag set by the question form)."""
    turns: dict[int, list[Sentence]] = {}
    for s in sentences:
        turns.setdefault(s.turn_idx, []).append(s)
    for t in sorted(turns):
        if t - 1 not in turns:
            continue
        cur, prev = turns[t], turns[t - 1]
        if cur[0].speaker != "patient" or prev[0].speaker != "doctor":
            continue
        prev_text = " ".join(s.text for s in prev)
        if "?" not in prev_text:
            continue
        answer = cur[0].text
        q_idx = {s.idx for s in prev if s.text.rstrip().endswith("?")}
        asked = [f for f in per_turn.get(t - 1, [])
                 if f.sentence_idx in q_idx and f.category in ("symptom", "diagnosis", "medical_history", "medication")]
        if _BARE_NO.match(answer):
            for f in asked:
                if f.polarity == "present":
                    f.polarity, f.trigger = "absent", "dialogue:no-answer"
                f.certainty = "certain"
        elif _BARE_YES.match(answer):
            for f in asked:
                if f.polarity == "present":
                    f.certainty, f.trigger = "certain", f.trigger or "dialogue:yes-answer"


# ---------------------------------------------------------------------------------------------
# convenience
# ---------------------------------------------------------------------------------------------

CATEGORIES = ["symptom", "medical_history", "diagnosis", "medication", "dosage", "investigation", "treatment", "numeric"]


def summarize(facts: Iterable[Fact]) -> dict:
    facts = list(facts)
    out = {c: 0 for c in CATEGORIES}
    neg = {c: 0 for c in CATEGORIES}
    unc = 0
    for f in facts:
        out[f.category] = out.get(f.category, 0) + 1
        if f.polarity == "absent":
            neg[f.category] = neg.get(f.category, 0) + 1
        if f.certainty == "uncertain":
            unc += 1
    return {"n_facts": len(facts), "by_category": out, "negated_by_category": neg, "n_negated": sum(neg.values()), "n_uncertain": unc}


def facts_to_dicts(facts: Iterable[Fact]) -> list[dict]:
    return [f.to_dict() for f in facts]


__all__ = ["Fact", "Sentence", "extract_facts", "segment", "detect_kind", "summarize", "facts_to_dicts", "CATEGORIES"]
