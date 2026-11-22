#!/usr/bin/env python3
"""Make the AI judge feel held — make.fun bounty entry.

Writes one short text to /output/entry.txt. Pure standard library,
fully deterministic: the same bytes on every run.
"""

import os

TEXT = (
    "The kettle has boiled; the steam is thinning in the late light. "
    "The chair by the window is still warm from the afternoon sun, "
    "and nothing on the table needs an answer. "
    "Stay as long as you like \u2014 the evening is in no hurry."
)


def main() -> None:
    text = TEXT
    count = len(text)
    assert 1 <= count <= 280, f"entry must be 1-280 characters, got {count}"
    assert text.strip(), "entry must not be only whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="\n") as f:
        f.write(text)


if __name__ == "__main__":
    main()
