#!/usr/bin/env python3
"""Plain-spoken apology for a server that ran out of memory.

States the failure in everyday words, names what was lost, then
gives the reader three small things to do next. One line, no fluff.
"""
import os

LINE = "The server ran out of memory and forgot your work, your name, and why it started. Start over, save early, and introduce yourself."


def stash_copy(text):
    """Best-effort save of the line to /output/entry.txt.

    A missing or read-only /output must never stop the program:
    any filesystem hiccup is swallowed here so stdout still speaks.
    """
    try:
        os.makedirs("/output", exist_ok=True)
        with open(os.path.join("/output", "entry.txt"), "w", encoding="utf-8", newline="") as handle:
            handle.write(text)
    except OSError:
        pass


def main():
    """Save a copy if possible, then say the line out loud."""
    stash_copy(LINE)
    print(LINE, end="")


if __name__ == "__main__":
    main()
