#!/usr/bin/env python3
"""Validate documented Shodan filter tokens used by this repository.

Project owner / original creator / primary maintainer: h4ckd4d

This validator is intentionally conservative. It scans selected Markdown files for
`filter:value`-style tokens and compares filter names against the curated allowlist
in config/official-filters.txt. It does not contact Shodan or execute searches.
"""

from __future__ import annotations

import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parents[1]
ALLOWLIST = ROOT / "config" / "official-filters.txt"
SCAN_TARGETS = [
    ROOT / "README.md",
    ROOT / "CHEATSHEET.md",
    ROOT / "docs" / "filters-reference.md",
    ROOT / "docs" / "getting-started.md",
    ROOT / "docs" / "cli-api.md",
    ROOT / "dorks",
]

TOKEN_RE = re.compile(r"(?<![\w./-])([a-z][a-z0-9_.-]*):(?=(?:\"|[A-Za-z0-9_*.-]))")


def load_allowlist() -> set[str]:
    values: set[str] = set()
    for line in ALLOWLIST.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if line and not line.startswith("#"):
            values.add(line)
    return values


def iter_markdown_files():
    for target in SCAN_TARGETS:
        if target.is_file():
            yield target
        elif target.is_dir():
            yield from sorted(target.rglob("*.md"))


def main() -> int:
    allowed = load_allowlist()
    errors: list[str] = []

    for path in iter_markdown_files():
        text = path.read_text(encoding="utf-8")
        for line_number, line in enumerate(text.splitlines(), start=1):
            for match in TOKEN_RE.finditer(line):
                token = match.group(1)
                if token not in allowed:
                    rel = path.relative_to(ROOT)
                    errors.append(f"{rel}:{line_number}: undocumented filter token '{token}'")

    if errors:
        print("Filter validation failed:\n")
        print("\n".join(errors))
        return 1

    print(f"Filter validation passed. {len(allowed)} curated filters allowed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
