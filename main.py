"""One-line error copy for make.fun "Say What Actually Broke".

The program writes a single line of software error copy to
/output/entry.txt: the brutal truth about an out-of-memory crash,
funny on one read, shippable in a real error dialog.

Deterministic: no clock, no randomness, no network, no input.
"""

import os

LINE = (
    "The app crashed because it ran out of memory trying to remember "
    "everything you asked it to. Restart it \u2014 it has already "
    "forgotten, and so should you."
)


def main() -> None:
    # Gate: the entry must be 1-200 characters of non-whitespace UTF-8.
    assert 1 <= len(LINE.strip()) <= 200, len(LINE)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
