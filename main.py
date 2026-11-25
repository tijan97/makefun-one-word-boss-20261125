#!/usr/bin/env python3
"""One word for the boss: writes the entry word to /output/entry.txt."""

import os

ENTRY = "Creditgoblin"


def main():
    word = ENTRY.strip()
    if not word or len(word) > 30 or len(word.split()) != 1:
        raise SystemExit("entry must be exactly one word of 1-30 characters")
    out_dir = (
        os.environ.get("MAKEFUN_OUTPUT_DIR")
        or os.environ.get("OUTPUT_DIR")
        or "/output"
    )
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(word)


if __name__ == "__main__":
    main()
