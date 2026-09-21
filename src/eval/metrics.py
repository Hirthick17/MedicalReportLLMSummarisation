"""
Standard summarization metrics (Person 3, Review 2): ROUGE-1/2/L/Lsum, BERTScore, length and
degeneration diagnostics.

    rouge_scores(pred, ref)            -> {"rouge1", "rouge2", "rougeL", "rougeLsum"}  (F1, 0-1)
    bertscore_batch(preds, refs)       -> list of F1 (rescaled with the English baseline)
    length_stats(pred, ref)            -> words, ratio, distinct-n, repeated n-gram share, runaway-list flag

ROUGE uses `rouge_score` with Porter stemming, which is the configuration of the ACI-Bench and
MEDIQA-Chat 2023 official scorers, so our numbers are comparable to the published baselines.
BERTScore uses roberta-large layer 17 with baseline rescaling (the library default for English),
so the values sit on the usual -1..1 rescaled range rather than the raw 0.8-0.95 band.
"""

from __future__ import annotations

import collections
import re
from functools import lru_cache

_WORD = re.compile(r"[A-Za-z0-9][A-Za-z0-9'/.-]*")


@lru_cache(maxsize=1)
def _rouge():
    from rouge_score import rouge_scorer
    return rouge_scorer.RougeScorer(["rouge1", "rouge2", "rougeL", "rougeLsum"], use_stemmer=True)


def rouge_scores(pred: str, ref: str) -> dict[str, float]:
    s = _rouge().score(ref, pred)
    return {k: float(v.fmeasure) for k, v in s.items()}


def bertscore_batch(preds: list[str], refs: list[str], model_type: str = "roberta-large", batch_size: int = 8, device: str | None = None) -> list[float]:
    from bert_score import score
    if device is None:
        import torch
        device = "cuda" if torch.cuda.is_available() else "cpu"
    _, _, f1 = score(preds, refs, lang="en", model_type=model_type, rescale_with_baseline=True, batch_size=batch_size, device=device, verbose=False)
    return [float(x) for x in f1.tolist()]


def _ngrams(tokens: list[str], n: int) -> list[tuple[str, ...]]:
    return [tuple(tokens[i:i + n]) for i in range(max(0, len(tokens) - n + 1))]


def length_stats(pred: str, ref: str) -> dict:
    pw = _WORD.findall(pred.lower())
    rw = _WORD.findall(ref.lower())
    n4 = _ngrams(pw, 4)
    c4 = collections.Counter(n4)
    repeated_share = sum(c for c in c4.values() if c > 1) / max(1, len(n4))     # share of 4-grams that recur
    distinct2 = len(set(_ngrams(pw, 2))) / max(1, len(pw) - 1)
    # runaway comma-list: the longest run of comma-separated short items (the run-3 ACI failure mode)
    runs = [len(seg.split(",")) for seg in re.split(r"[.\n;:]", pred)]
    longest_list = max(runs) if runs else 0
    return {
        "pred_words": len(pw), "ref_words": len(rw), "length_ratio": len(pw) / max(1, len(rw)),
        "distinct_2": distinct2, "repeated_4gram_share": repeated_share, "longest_comma_list": longest_list,
        "degenerate": bool(repeated_share > 0.5 or longest_list >= 25),
    }


__all__ = ["rouge_scores", "bertscore_batch", "length_stats"]
