#!/usr/bin/env python3
"""Make the AI Judge Laugh: the Office Joke Open.

Writes one original one-line joke about office life to
``$MAKEFUN_OUTPUT_DIR/entry.txt`` (default ``/output``).
Python 3.13 standard library only; no network, no randomness.
The joke is a single line under 200 characters.
"""

import os

JOKE = (
    "I replied-all asking to be removed from this thread, and they added "
    "me to the committee that decides who gets removed from threads."
)


def main() -> None:
    text = JOKE.strip()
    assert 1 <= len(text) <= 200, f"joke must be 1-200 chars, got {len(text)}"
    assert "\n" not in text, "joke must be a single line"
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    with open(os.path.join(output_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
