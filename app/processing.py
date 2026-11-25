import re
from collections import Counter

# A word is letters/digits, optionally joined by internal apostrophes (e.g. "don't").
_WORD_PATTERN = re.compile(r"[a-z0-9]+(?:'[a-z0-9]+)*")
_SENTENCE_END_PATTERN = re.compile(r"[.!?]")


def normalize_text(text: str) -> str:
    """
    Normalize whitespace by:
    - stripping leading/trailing whitespace
    - collapsing internal whitespace (spaces, tabs, newlines) to single spaces
    """
    return " ".join(text.split())


def _extract_words(text: str) -> list[str]:
    """Return the lowercase words in text, with surrounding punctuation removed."""
    return _WORD_PATTERN.findall(text.lower())


def character_count(text: str) -> int:
    """
    Return the number of characters in text, including spaces and punctuation.
    """
    return len(text)


def sentence_count(text: str) -> int:
    """
    Return the number of sentences in text.

    Sentences are split on '.', '!' or '?'. Pieces that are empty or contain
    only whitespace (e.g. from "..." or trailing punctuation) are ignored.
    """
    pieces = _SENTENCE_END_PATTERN.split(text)
    return sum(1 for piece in pieces if normalize_text(piece))


def unique_word_count(text: str) -> int:
    """
    Return the number of distinct words in text, ignoring case and punctuation.
    """
    return len(set(_extract_words(text)))


def top_words(text: str, n: int = 5) -> list[tuple[str, int]]:
    """
    Return the n most frequent words in text as (word, count) pairs.

    Words are compared case-insensitively with punctuation removed. Results are
    ordered by count (highest first), with ties broken alphabetically. If text
    has fewer than n distinct words, all of them are returned. If n is zero or
    negative, an empty list is returned.
    """
    if n <= 0:
        return []
    counts = Counter(_extract_words(text))
    ranked = sorted(counts.items(), key=lambda item: (-item[1], item[0]))
    return ranked[:n]
