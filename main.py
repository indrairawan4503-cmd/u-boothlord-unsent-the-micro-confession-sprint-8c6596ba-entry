"""Unsent: The Micro-Confession Sprint — variant B.

Writes one two-part micro-confession (a To: line + the unsent message
itself) to /output/entry.txt.

The grader sandbox mounts the repository read-only, so the output is
written to MAKEFUN_OUTPUT_DIR first and any copy to the repo root is
guarded so a read-only filesystem can never crash the run.

The work is split into small helpers: get_output_dir() resolves the
destination, write_entry() writes the text, copy_to_repo_root() does
the best-effort local copy, and main() wires them together.
"""

import os

ENTRY_TEXT = (
    "To: Mum\n"
    "I lost my job in March. Every Sunday after your call I type this "
    "and delete it. I'd rather lie about work than hear your voice go quiet."
)


def get_output_dir() -> str:
    """Output directory: MAKEFUN_OUTPUT_DIR, defaulting to /output."""
    return os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")


def write_entry(out_dir: str) -> str:
    """Write ENTRY_TEXT to <out_dir>/entry.txt; return the path."""
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.txt")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(ENTRY_TEXT)
    return out_path


def copy_to_repo_root() -> None:
    """Best-effort copy of ENTRY_TEXT next to the program.

    The grader repo is read-only, so a failure here must never abort
    the run.
    """
    try:
        root_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "entry.txt")
        with open(root_path, "w", encoding="utf-8") as f:
            f.write(ENTRY_TEXT)
    except OSError:
        pass


def main() -> None:
    write_entry(get_output_dir())
    copy_to_repo_root()


if __name__ == "__main__":
    main()
