"""The Funniest Office Joke, Judged Head to Head — Program/v1.

Writes exactly one office joke to <output_dir>/entry.txt (default /output),
UTF-8, no trailing newline. Python 3.13 stdlib only, no network.
Output dir override (for local scratch runs only): OUTPUT_DIR env var.
"""

import os
from pathlib import Path

ENTRY = "Dave's 9:04 'quick question' ate 47 minutes, so he booked a follow-up to discuss the question — and Karen hit reply-all: 'Can we schedule a meeting about the email we never sent?'"

def main() -> None:
    output_dir = Path(os.environ.get("OUTPUT_DIR", "/output"))
    output_dir.mkdir(parents=True, exist_ok=True)
    entry_path = output_dir / "entry.txt"
    # Contest gate: the entry must be one line of 1-200 characters.
    if not 1 <= len(ENTRY) <= 200:
        raise ValueError(f"entry must be 1-200 characters, got {len(ENTRY)}")
    # No trailing newline: the entry is exactly the line.
    entry_path.write_text(ENTRY, encoding="utf-8", newline="")

if __name__ == "__main__":
    main()
