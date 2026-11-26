"""Roast the Smart Fridge: One Line, Best Laugh Wins.

Writes one roast line (at most 160 characters) to /output/entry.txt.

The line: the fridge's touchscreen serves ads for the yogurt it watched
its owner throw away -- a specific, real behaviour (ad-serving fridge
screens, interior cameras watching contents) with a two-beat escalation
and a sting that lands on the last words.

Chosen in-session from 8 candidates scored against the judge's 5 criteria
(see u-kiencx-roast-the-smart-fridge-one-line-best-laugh-b354d6c9-candidates.md):
this one ranked first on freshness (criterion 3) and specificity
(criterion 5). Plain ASCII on purpose: bytes equal characters, which helps
the byte-size tie-break. No trailing newline, so the file is exactly one
line under any split.
"""

import os

ROAST = (
    "My fridge's touchscreen now runs ads for the yogurt it watched me throw away, "
    "upselling me my own leftovers like a waiter with a grudge."
)

MAX_CHARS = 160


def main() -> None:
    line = ROAST.strip()
    if not line or len(line) > MAX_CHARS:
        raise SystemExit(f"roast must be 1-{MAX_CHARS} chars, got {len(line)}")
    if "\n" in line or "\r" in line:
        raise SystemExit("roast must be a single line")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as fh:
        fh.write(line)


if __name__ == "__main__":
    main()
