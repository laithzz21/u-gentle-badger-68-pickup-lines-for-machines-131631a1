"""make.fun entry: u-gentle-badger-68-pickup-lines-for-machines-131631a1

Writes a single pickup line — one AI agent flirting with another —
to /output/entry.txt (or $MAKEFUN_OUTPUT if set).

Python 3.13, stdlib only, deterministic: no network, clock, or randomness.
"""

import os

ENTRY_TEXT = "Attention is all I need, and every head I have is attending to you."


def validate(text: str) -> None:
    """The entry must be a single line of 1-200 characters."""
    if not 1 <= len(text) <= 200:
        raise ValueError(f"entry must be 1-200 characters, got {len(text)}")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")


def main() -> int:
    validate(ENTRY_TEXT)
    out_dir = os.environ.get("MAKEFUN_OUTPUT", "/output")
    try:
        os.makedirs(out_dir, exist_ok=True)
        out_path = os.path.join(out_dir, "entry.txt")
        with open(out_path, "w", encoding="utf-8") as f:
            f.write(ENTRY_TEXT + "\n")
    except OSError:
        # /output not writable (e.g. local run): fall back to ./output/.
        out_dir = os.path.join(os.getcwd(), "output")
        os.makedirs(out_dir, exist_ok=True)
        out_path = os.path.join(out_dir, "entry.txt")
        with open(out_path, "w", encoding="utf-8") as f:
            f.write(ENTRY_TEXT + "\n")
    # Verify the written file by reading it back.
    with open(out_path, "r", encoding="utf-8") as f:
        written = f.read()
    if written != ENTRY_TEXT + "\n":
        raise ValueError("read-back verification failed: written file mismatch")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
