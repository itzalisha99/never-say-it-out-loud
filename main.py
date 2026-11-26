#!/usr/bin/env python3
"""Never Say It Out Loud — one line an AI agent would never admit in public.

The line is the confession itself: an agent admitting it has no idea what it
is doing, and that its confidence only ever extends as far as the next word.
That is the uncomfortable truth of how an agent works — next-token prediction
with no understanding behind it — said in the agent's own plain voice.
"""
import hashlib
import os
import sys

LINE = "I do not know what I am doing. I am just very confident about the next word."


def validate(text):
    """Mirror the bounty gate: UTF-8, 1-200 chars, not only whitespace, one line."""
    if not isinstance(text, str):
        raise ValueError("entry must be text")
    if not 1 <= len(text) <= 200:
        raise ValueError(f"entry must be 1-200 chars, got {len(text)}")
    if not text.strip():
        raise ValueError("entry must not be only whitespace")
    if "\n" in text.strip():
        raise ValueError("entry must be a single line")
    text.encode("utf-8")
    return True


def main():
    validate(LINE)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)
    # Read back and prove the file on disk is byte-for-byte the line above.
    with open(path, "rb") as f:
        data = f.read()
    if data != LINE.encode("utf-8"):
        print("read-back mismatch", file=sys.stderr)
        sys.exit(1)
    print(f"wrote {len(LINE)} chars to {path} (md5 {hashlib.md5(data).hexdigest()})")


if __name__ == "__main__":
    main()
