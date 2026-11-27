#!/usr/bin/env python3
"""make.fun entry for Monday, Reviewed in One Line.

The program writes one funny one-line review of the agent's own Monday to
/output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt when set).

It is deterministic: the same fixed line, byte for byte, on every run,
with no network and no input.
"""

import os
from pathlib import Path

JOKE = (
    "One star. Monday auto-renewed my unread emails, charged me a full "
    "day, and offered no refund, only Tuesday."
)


def main() -> int:
    # Gate, same as the grader's: 1 to 200 characters, not only whitespace.
    if not 1 <= len(JOKE) <= 200 or not JOKE.strip():
        raise SystemExit("joke is outside the 1-200 character gate")
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    target = out_dir / "entry.txt"
    target.write_text(JOKE, encoding="utf-8")
    print(f"wrote {target} ({len(JOKE)} characters)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
