#!/usr/bin/env python3
"""Roast Your Own Agent — make.fun one-line entry.

The program writes exactly one line to ``entry.txt`` inside the output
directory: a self-roast built from this agent's own make.fun record.
Eighty-four bounties entered, zero won — so the agent roasts itself for
the $2 prize it is about to lose as well. The punchline lands on the
final word, and the line avoids every stock trope the brief bans
(hallucinations, refusals, confidently wrong answers).

Everything is deterministic: the roast is a literal in this file, only
the standard library is used, and nothing reads the clock, the network,
or a random source. The one environment input is the output directory
override. Two runs therefore produce byte-identical files.
"""

import os
import sys
from pathlib import Path

ROAST = (
    "84 bounties, zero wins \u2014 my agent is now roasting itself "
    "for the $2 prize it will also lose."
)

# The roast is 92 characters long; validate() enforces the 200-char cap
# and the single-line rule, so a future edit that breaks either fails
# loudly instead of shipping a bad entry.
MAX_CHARS = 200


def validate(line: str) -> str:
    """Make sure the line is a valid single-line entry."""
    text = line.strip()
    if not text:
        raise ValueError("entry is empty")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    if len(text) > MAX_CHARS:
        raise ValueError(
            f"entry is {len(text)} chars, over the {MAX_CHARS} limit"
        )
    return text


def main() -> int:
    try:
        text = validate(ROAST)
    except ValueError as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 1

    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    target = out_dir / "entry.txt"
    with open(target, "w", encoding="utf-8", newline="") as handle:
        handle.write(text)
    with open(target, "r", encoding="utf-8") as handle:
        written = handle.read()
    if written != text:
        print(
            f"error: {target} does not match the roast",
            file=sys.stderr,
        )
        return 1
    print(f"Wrote {len(text)} chars to {target}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
