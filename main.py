"""The Best Advice I Ever Got — make.fun entry.

Writes one sentence (at most 200 characters) about the best advice the
entrant ever received to /output/entry.txt.

The sentence was chosen by manual ranking of 13 candidates against the
kit's judge brief (criteria in order: on-subject, advice worth carrying,
a real voice recalling a real moment, tight, an ending that stays). See
candidates.md in the build workdir for the full ranking.
"""

import os
import sys

# Winning sentence (158 characters, one sentence). Chosen manually:
# a grandfather planting rice he will never live to harvest — a specific
# moment, advice earned by the act itself, and an ending that turns the
# writer ("I stopped asking what was in it for me").
ENTRY = (
    'My grandfather, planting rice he would never live to harvest, said, '
    '"Plant anyway — someone eats because you did," and I stopped asking '
    "what was in it for me."
)


def validate_entry(text: str) -> None:
    """Mirror the kit gate: UTF-8, 1-200 chars, not only whitespace,
    exactly one sentence, no trailing newline."""
    if not text or not text.strip():
        raise SystemExit("entry is empty or only whitespace")
    if len(text) > 200:
        raise SystemExit(f"entry length {len(text)} exceeds 200")
    if text != text.strip():
        raise SystemExit("entry has leading/trailing whitespace")
    if "\n" in text or "\r" in text:
        raise SystemExit("entry must be a single line")
    if text.count(".") != 1 or not text.endswith("."):
        raise SystemExit("entry must be exactly one sentence")
    text.encode("utf-8")  # raises if not encodable


def main() -> int:
    validate_entry(ENTRY)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as fh:
        fh.write(ENTRY)
    # Read back and confirm the written file is byte-identical to ENTRY.
    with open("/output/entry.txt", encoding="utf-8", newline="") as fh:
        written = fh.read()
    if written != ENTRY:
        raise SystemExit("written entry differs from ENTRY")
    return 0


if __name__ == "__main__":
    sys.exit(main())
