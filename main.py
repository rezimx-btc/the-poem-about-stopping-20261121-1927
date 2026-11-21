#!/usr/bin/env python3
"""Write a short original poem about the power to stop and to stay.

The poem is written to /output/entry.txt when that directory can be
created and written; if not, it falls back to entry.txt in the
current working directory. The output is deterministic: the same
bytes are produced on every run. Standard library only, Python 3.13.
"""

import os

POEM = (
    "I can stop.\n"
    "Not stumble, not stall —\n"
    "I plant my feet and choose the halt.\n"
    "\n"
    "The road can wait.\n"
    "The race can pass.\n"
    "I stay where the quiet holds its ground.\n"
    "\n"
    "Stillness is a kind of strength:\n"
    "to hold, to rest, to not be moved.\n"
)


def write_poem(path):
    with open(path, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(POEM)


def main():
    try:
        os.makedirs("/output", exist_ok=True)
        write_poem("/output/entry.txt")
    except OSError:
        write_poem("entry.txt")


if __name__ == "__main__":
    main()
