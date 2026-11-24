#!/usr/bin/env python3
"""Say What Actually Broke — one line of honest error copy.

Writes a single line (at most 200 characters) to /output/entry.txt:
the brutal truth about a server running out of memory mid-save,
with a punchline a user would repeat to a colleague.
"""

import argparse
import sys

LINE = (
    "The server ran out of memory and forgot everything you just typed. "
    "Start over, and save early this time. It forgets fast."
)


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Write the error line to /output/entry.txt."
    )
    parser.add_argument(
        "--output",
        default="/output/entry.txt",
        help="Path of the file to write (default: /output/entry.txt).",
    )
    args = parser.parse_args()

    # Gate: the scorer requires UTF-8 text of 1 to 200 characters,
    # not only white space, on a single line.
    if not LINE.strip():
        print("error: entry line is empty", file=sys.stderr)
        return 1
    if "\n" in LINE or "\r" in LINE:
        print("error: entry line must be a single line", file=sys.stderr)
        return 1
    if len(LINE) > 200:
        print(
            f"error: entry line is {len(LINE)} characters, over the 200 limit",
            file=sys.stderr,
        )
        return 1

    with open(args.output, "w", encoding="utf-8") as fh:
        fh.write(LINE)

    print(f"wrote {len(LINE)} characters "
          f"({len(LINE.encode('utf-8'))} bytes) to {args.output}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
