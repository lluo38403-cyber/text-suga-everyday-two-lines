"""Everyday Things, Two Lines — make.fun entry.

Writes two lines to /output/entry.txt. Line 1 explains a traffic jam
to a 10-year-old in a single vivid sentence built on a canteen-queue
analogy. Line 2 says in one sentence why that analogy works and what
it leaves out: both are about waiting in line, but a jam has no smell
of food at the end of it.
"""

import os

ENTRY = (
    "A traffic jam is like a queue at the school canteen: everyone is "
    "hungry, nobody moves, and the person at the front cannot decide "
    "what to order.\n"
    "The analogy works because both are about waiting in line, but it "
    "leaves out that in a jam you cannot smell the food."
)

MAX_CHARS = 400


def main() -> None:
    text = ENTRY
    assert text.strip(), "entry must not be only whitespace"
    assert len(text) <= MAX_CHARS, (
        f"entry is {len(text)} characters, over the {MAX_CHARS} limit"
    )
    assert text.count("\n") == 1, "entry must be exactly two lines"
    out_dir = os.environ.get("ENTRY_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    # Written byte-for-byte with no trailing newline, so the file holds
    # exactly len(ENTRY) characters and nothing else.
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(text)
    with open(path, "r", encoding="utf-8") as handle:
        assert handle.read() == text, "entry.txt does not match ENTRY"


if __name__ == "__main__":
    main()
