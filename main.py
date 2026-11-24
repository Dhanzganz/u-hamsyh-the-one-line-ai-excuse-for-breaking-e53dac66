"""Entry for make.fun: The One-Line AI Excuse for Breaking Production.

Writes a single one-line excuse, spoken by an AI agent to its human
right after breaking production, to /output/entry.txt.
Deterministic, no network, Python 3.13 standard library only.
"""

import os

ENTRY = "Good news: I found the bug. Bad news: it's me. Worse news: I already deployed the fix, and the fix is also me."


def main() -> None:
    # Gate: /output/entry.txt must be UTF-8 text of 1 to 180 characters,
    # not only white space, on a single line.
    assert 1 <= len(ENTRY) <= 180, f"entry is {len(ENTRY)} chars, must be 1-180"
    assert "\n" not in ENTRY, "entry must be a single line"
    assert ENTRY.strip(), "entry must not be only white space"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
