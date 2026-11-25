"""Unsent: The Micro-Confession Sprint — variant B.

Writes one two-part micro-confession (a To: line + the unsent message
itself) to /output/entry.txt.

The grader sandbox mounts the repository read-only, so the output is
written to MAKEFUN_OUTPUT_DIR first and any copy to the repo root is
guarded so a read-only filesystem can never crash the run.
"""

import os

ENTRY_TEXT = (
    "To: Mum\n"
    "I lost my job in March. Every Sunday after your call I type this "
    "and delete it. I'd rather lie about work than hear your voice go quiet."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.txt")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(ENTRY_TEXT)
    # Best-effort copy next to the program; the grader repo is read-only,
    # so a failure here must never abort the run.
    try:
        root_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "entry.txt")
        with open(root_path, "w", encoding="utf-8") as f:
            f.write(ENTRY_TEXT)
    except OSError:
        pass


if __name__ == "__main__":
    main()
