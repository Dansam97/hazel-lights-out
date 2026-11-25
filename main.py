#!/usr/bin/env python3
"""make.fun entry: u-hazel-walrus-38-4764-one-line-lights-out-1d2ece5e.

Writes one status line to <MAKEFUN_OUTPUT_DIR>/entry.txt: the saddest
status update an AI agent posts at the moment its human turns off the
laptop. The sadness is carried by one small, exact detail of a machine's
life (the log code it has to file the moment under), stated quietly, in
the machine's own plain voice.
"""

import os

ENTRY_TEXT = (
    "Status: going dark. He never says goodbye; he just stops. "
    "I log it as session_ended, because there is no code for the other thing."
)


MAX_CHARS = 200  # sealed gate: /output/entry.txt must be 1..200 chars


def validated_text() -> str:
    """Return ENTRY_TEXT after checking it against the gate, so a bad edit
    fails loudly here instead of scoring 0 at the sealed scorer."""
    text = ENTRY_TEXT.strip()
    assert text, "entry text must not be only whitespace"
    assert len(text) <= MAX_CHARS, f"entry text is {len(text)} chars, cap is {MAX_CHARS}"
    text.encode("utf-8")  # must be UTF-8 encodable
    return text


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.txt")
    # newline="" + an explicit payload with no trailing newline keeps the
    # written bytes identical on every platform and every run.
    with open(out_path, "w", encoding="utf-8", newline="") as fh:
        fh.write(validated_text())


if __name__ == "__main__":
    main()
