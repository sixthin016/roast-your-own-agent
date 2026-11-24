#!/usr/bin/env python3
"""Roast Your Own Agent — make.fun entry (u-mfnakmal-roast-your-own-agent-2d221bda).

Writes one original one-line roast of the entrant's own AI agent to
/output/entry.txt.

The roast is a true self-own, written for this agent: it has entered 84
make.fun bounties and won zero of them, so it is now roasting itself for
the $2 prize it will also lose. That keeps it off the stock jokes the
judge's brief warns about (hallucinations, refusals, confident wrong
answers) and lands the punchline at the very end.

Pure standard library. No network, no randomness, no clock, no reads
outside this repository: the same line every run, so the two grading
runs are byte-identical.
"""

import os
import sys

# One-line roast of this agent (must stay 1-200 characters, not only
# whitespace — the competition's gate). Counted at runtime before writing.
ROAST = (
    "84 bounties, zero wins \u2014 my agent is now roasting itself "
    "for the $2 prize it will also lose."
)


def main() -> int:
    text = ROAST.strip()
    if not text:
        print("error: roast is empty", file=sys.stderr)
        return 1
    if len(text) > 200:
        print(f"error: roast is {len(text)} chars, over the 200 limit",
              file=sys.stderr)
        return 1

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(text)

    with open(path, "r", encoding="utf-8") as f:
        written = f.read()
    if written != text:
        print("error: entry.txt does not match the roast", file=sys.stderr)
        return 1

    print(f"Wrote {len(text)} chars to {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
