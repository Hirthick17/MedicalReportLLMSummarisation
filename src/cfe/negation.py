"""
Assertion (negation / uncertainty / history / family) detection — a NegEx/ConText-style rule set.

Given a sentence and the character span of a clinical term inside it, `assert_status()` returns:

    polarity   : "present" | "absent"
    certainty  : "certain" | "uncertain"        ("possible", "rule out", "?", ...)
    temporality: "current" | "historical"       ("history of", "years ago", "previously", ...)
    experiencer: "patient" | "family"           ("mother had", "family history of", ...)
    trigger    : the trigger phrase that fired (for auditing), or None

Rules (Chapman et al., NegEx 2001; Harkema et al., ConText 2009), adapted to dialogue:
  * Pre-triggers negate terms that FOLLOW them, up to a scope terminator or a window of
    `MAX_SCOPE` words. Commas do NOT terminate scope ("denies fever, chills, or nausea").
  * Post-triggers negate terms that PRECEDE them within the same window.
  * Pseudo-negations ("no increase", "not only", "gram negative") are masked before matching.
  * Conjunction terminators ("but", "however", "except", "although") close the scope.
  * Dialogue rule (extractor.py): a patient turn that is a bare "no"/"nope"/"never" negates the
    symptom(s) asked about in the immediately preceding doctor turn.
"""

from __future__ import annotations

import re
from dataclasses import dataclass

MAX_SCOPE = 40  # words a trigger can reach. NegEx uses 5-6, but clinical ROS lists ("denies A, B, C, ... , M") run
                # far longer; the scope is bounded by the sentence and by the terminators below instead

PRE_NEGATION = [
    "no evidence of", "no signs of", "no sign of", "no history of", "no hx of", "no complaints of", "no complaint of",
    "no known", "no further", "no longer has", "no longer having", "no longer", "free of", "absence of", "absent",
    "denies any", "denies", "denied any", "denied", "denying", "deny", "negative for", "neg for", "negative", "neg", "not have", "not having",
    "never had", "never has", "never experienced", "never", "didn't have", "did not have", "doesn't have", "does not have",
    "hasn't had", "has not had", "haven't had", "have not had", "hasn't been", "has not been", "hasn't noticed", "has not noticed",
    "isn't", "is not", "aren't", "are not", "wasn't", "was not", "weren't", "were not", "without any", "without", "rules out",
    "ruled out", "rule out", "r/o", "unremarkable for", "nothing", "none", "not", "no", "nor", "neither", "cannot", "can't",
    "unable to", "failed to", "fails to", "declines", "declined", "resolved", "resolution of", "no more", "not any",
    "don't think", "do not think", "doesn't think", "does not think", "didn't think", "don't believe", "do not believe",
    "doubt", "doubtful", "not consistent with", "inconsistent with", "no indication of", "no concern for", "not concerning for",
    "not suggestive of", "not indicative of", "no findings of", "argues against", "against",
]
POST_NEGATION = [
    "is ruled out", "was ruled out", "are ruled out", "were ruled out", "has been ruled out", "have been ruled out",
    "was negative", "is negative", "were negative", "are negative", "came back negative", "unlikely", "is unlikely",
    "has resolved", "have resolved", "resolved", "is absent", "was absent", "are absent", "were absent", "not present",
    "not seen", "not noted", "not observed", "not found", "not identified", "not detected", "was not detected",
    "is denied", "are denied", "denied", "free", "not appreciated",
]
PSEUDO_NEGATION = [
    "no increase", "no change", "no significant change", "no interval change", "no further increase", "not only",
    "not necessarily", "not certain if", "not certain whether", "gram negative", "gram-negative", "no difficulty",
    "without difficulty", "without any difficulty", "not just", "no doubt", "no problem with", "no worse", "no better",
    "not at all worse", "no new", "no other", "not to", "if not", "no way of", "no matter", "positive for negative",
]
SCOPE_TERMINATORS = [
    "but", "however", "although", "though", "except", "except for", "aside from", "other than", "apart from", "yet",
    "still", "nevertheless", "whereas", "which", "who", "because", "since", "so", "then", "unless", "until", "besides",
    "apart", "positive for", "does have", "does report", "reports", "endorses", "admits", "complains of", "presents with",
    "presenting with", "secondary to", "due to", "as well as", "in addition to", "endorses", "endorsed", "has had", "notes",
    "noted", "states", "stated", "is present", "are present", "was present", "were present", "positive", "reveals", "revealed",
    "shows", "showed", "demonstrates", "demonstrated", "significant for", "remarkable for", "consistent with", "with a",
]

UNCERTAINTY = [
    "possible", "possibly", "probable", "probably", "likely", "most likely", "suspect", "suspected", "suspicious for",
    "concern for", "concerning for", "question of", "questionable", "may be", "might be", "could be", "may have", "might have",
    "could have", "rule out", "r/o", "versus", "vs", "vs.", "differential", "differential diagnosis", "consider", "considered",
    "consistent with", "suggestive of", "suggests", "cannot exclude", "can't rule out", "cannot rule out", "not sure", "unsure",
    "unclear", "uncertain", "presumed", "presumably", "appears to be", "appears", "seems", "seems to be", "?", "maybe", "perhaps",
    "potential", "potentially", "at risk for", "risk of", "risk for", "worry about", "worried about", "worries about", "if",
    "in case", "should", "would", "might", "may", "could", "wonder if", "wondering if", "not certain",
    "side effects", "side effect", "can include", "may include", "can cause", "may cause", "could cause", "watch for", "signs of",
    "symptoms of", "if you develop", "if you experience", "if you notice", "return if", "call if", "warning signs",
]
HISTORICAL = [
    "history of", "hx of", "h/o", "past medical history", "pmh", "pmhx", "past history", "previous", "previously", "prior",
    "in the past", "years ago", "year ago", "months ago", "month ago", "weeks ago", "week ago", "days ago", "a while ago",
    "long time ago", "when i was", "as a child", "as a kid", "childhood", "growing up", "back in", "used to", "had a", "has had",
    "have had", "known", "chronic", "long-standing", "longstanding", "long standing", "diagnosed with", "was diagnosed",
    "diagnosed", "since", "for years", "for many years", "several years", "for the past", "for the last", "status post", "s/p",
    "post", "remote", "old", "resolved", "healed", "recovered", "treated for", "was treated", "surgery in", "surgery for",
    "significant for", "past medical", "medical history", "pmh significant", "past surgical", "psh", "underwent", "on and off",
]
FAMILY = [
    "family history", "family hx", "fh", "fhx", "runs in the family", "runs in my family", "in the family", "in my family",
    "mother", "mom", "father", "dad", "parents", "parent", "brother", "sister", "sibling", "siblings", "grandmother", "grandma",
    "grandfather", "grandpa", "grandparents", "grandparent", "aunt", "uncle", "cousin", "son", "daughter", "children", "child",
    "kids", "wife", "husband", "spouse", "partner", "maternal", "paternal", "relative", "relatives", "nephew", "niece",
    "my mother's", "my father's", "his mother", "his father", "her mother", "her father", "family member", "family members",
]

_WORD = re.compile(r"[a-z0-9][a-z0-9'./+-]*|[?]")


def _compile(phrases: list[str]) -> re.Pattern:
    # longest first so "no evidence of" beats "no"
    alts = sorted({p for p in phrases}, key=len, reverse=True)
    return re.compile(r"(?<![a-z0-9])(?:" + "|".join(re.escape(a) for a in alts) + r")(?![a-z0-9])", re.IGNORECASE)


_PRE = _compile(PRE_NEGATION)
_POST = _compile(POST_NEGATION)
_PSEUDO = _compile(PSEUDO_NEGATION)
_TERM = _compile(SCOPE_TERMINATORS)
_UNC = _compile(UNCERTAINTY)
_HIST = _compile(HISTORICAL)
_FAM = _compile(FAMILY)


@dataclass(frozen=True)
class Assertion:
    polarity: str = "present"
    certainty: str = "certain"
    temporality: str = "current"
    experiencer: str = "patient"
    trigger: str | None = None


def _mask_pseudo(sentence: str) -> str:
    """Replace pseudo-negations with same-length filler so 'no' inside 'no increase' cannot fire."""
    return _PSEUDO.sub(lambda m: "#" * len(m.group(0)), sentence)


def _word_count(text: str) -> int:
    return len(_WORD.findall(text.lower()))


def assert_status(sentence: str, start: int, end: int) -> Assertion:
    """Assertion status for the term at sentence[start:end]."""
    low = _mask_pseudo(sentence.lower())
    before, after = low[:start], low[end:]

    polarity, trigger = "present", None

    # --- pre-negation: nearest trigger before the term, no terminator between, within scope
    best = None
    for m in _PRE.finditer(before):
        gap = before[m.end():]
        if _TERM.search(gap):
            continue
        if _word_count(gap) > MAX_SCOPE:
            continue
        best = m
    if best is not None:
        polarity, trigger = "absent", best.group(0)

    # --- post-negation: nearest trigger after the term, no terminator between, within scope
    if polarity == "present":
        m = _POST.search(after)
        if m is not None:
            gap = after[:m.start()]
            if not _TERM.search(gap) and _word_count(gap) <= MAX_SCOPE:
                polarity, trigger = "absent", m.group(0)

    # --- uncertainty: anywhere in a short window either side, not blocked by a terminator
    certainty = "certain"
    win_before = before[-120:]
    win_after = after[:80]
    mu = None
    for m in _UNC.finditer(win_before):
        if not _TERM.search(win_before[m.end():]):
            mu = m
    if mu is None:
        m2 = _UNC.search(win_after)
        if m2 is not None and not _TERM.search(win_after[:m2.start()]):
            mu = m2
    if mu is not None:
        certainty = "uncertain"
        trigger = trigger or mu.group(0)

    # --- temporality: historical trigger before the term in the same clause, or "ago" after it
    temporality = "current"
    mh = None
    for m in _HIST.finditer(before[-160:]):
        mh = m
    if mh is not None or re.search(r"^\s*(?:\w+\s+){0,4}(?:ago|in the past|previously)", after):
        temporality = "historical"
        if mh is not None:
            trigger = trigger or mh.group(0)

    # --- experiencer: a family term in the same sentence close before the term
    experiencer = "patient"
    mf = None
    for m in _FAM.finditer(before[-100:]):
        if not _TERM.search(before[-100:][m.end():]):
            mf = m
    if mf is not None:
        experiencer = "family"
        trigger = trigger or mf.group(0)

    return Assertion(polarity, certainty, temporality, experiencer, trigger)


__all__ = ["Assertion", "assert_status", "MAX_SCOPE", "PRE_NEGATION", "POST_NEGATION", "PSEUDO_NEGATION", "SCOPE_TERMINATORS",
           "UNCERTAINTY", "HISTORICAL", "FAMILY"]
