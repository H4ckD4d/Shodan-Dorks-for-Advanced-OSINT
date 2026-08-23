#!/usr/bin/env python3
"""Validate documented Shodan filter tokens used by this repository.

Project owner / original creator / primary maintainer: h4ckd4d

The validator scans code examples and inline-code snippets in selected Markdown
files, then compares concrete `filter:value` tokens against the curated allowlist
in config/official-filters.txt. Prose is intentionally ignored so labels such as
"Project owner:" or "Current milestone:" are not misclassified as Shodan
filters. Generic teaching placeholders are ignored as well. The validator does
not contact Shodan or execute searches.
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
INLINE_CODE_RE = re.compile(r"`([^`]+)`")
FENCE_RE = re.compile(r"^\s*(```|~~~)")
GENERIC_PLACEHOLDERS = {"filter", "example", "title"}


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


def code_fragments(text: str):
    """Yield (line_number, code_fragment) from fenced and inline Markdown code."""
    in_fence = False
    fence_marker: str | None = None

    for line_number, line in enumerate(text.splitlines(), start=1):
        fence_match = FENCE_RE.match(line)
        if fence_match:
            marker = fence_match.group(1)
            if not in_fence:
                in_fence = True
                fence_marker = marker
            elif marker == fence_marker:
                in_fence = False
                fence_marker = None
            continue

        if in_fence:
            yield line_number, line
            continue

        for match in INLINE_CODE_RE.finditer(line):
            yield line_number, match.group(1)


def main() -> int:
    allowed = load_allowlist()
    errors: list[str] = []

    for path in iter_markdown_files():
        text = path.read_text(encoding="utf-8")
        for line_number, fragment in code_fragments(text):
            for match in TOKEN_RE.finditer(fragment):
                token = match.group(1)
                if token in GENERIC_PLACEHOLDERS:
                    continue
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
