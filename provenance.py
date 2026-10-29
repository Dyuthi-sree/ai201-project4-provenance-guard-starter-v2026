"""
Signal three: source-attribution evidence.

This signal looks for visible provenance cues such as URLs, attribution
phrases, and quotations. It cannot verify that a cited source is genuine or
that the source actually supports the text.
"""

import re


def source_signal(text: str) -> float:
    """
    Return a 0–1 score where higher means more likely AI.

    A text without visible source cues receives a neutral score of 0.5.
    URLs, attribution language, and quotations lower the score because they
    provide readers with some evidence they can inspect.
    """
    if not isinstance(text, str) or not text.strip():
        return 0.5

    url_count = len(re.findall(r"https?://\S+|www\.\S+", text, re.IGNORECASE))

    attribution_count = len(re.findall(
        r"\b(?:according to|reported by|published by|research by|"
        r"a study by|data from|source:|cited by)\b",
        text,
        re.IGNORECASE,
    ))

    quotation_count = len(re.findall(
        r'"[^"]{10,}"|“[^”]{10,}”',
        text,
    ))

    evidence_credit = min(
        0.5,
        0.25 * url_count
        + 0.15 * attribution_count
        + 0.10 * quotation_count,
    )

    return round(0.5 - evidence_credit, 4)


if __name__ == "__main__":
    import sys

    sample = " ".join(sys.argv[1:])
    print(f"source_signal {source_signal(sample):.4f}")
    print("(higher = more likely AI; 0.5 means no visible source evidence)")