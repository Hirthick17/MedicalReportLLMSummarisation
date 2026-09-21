"""Clinical Fact Extractor (rule-based, Review 2). See extractor.py for the Fact schema."""
from .extractor import CATEGORIES, Fact, detect_kind, extract_facts, facts_to_dicts, segment, summarize
from .negation import Assertion, assert_status

__all__ = ["CATEGORIES", "Fact", "detect_kind", "extract_facts", "facts_to_dicts", "segment", "summarize", "Assertion", "assert_status"]
