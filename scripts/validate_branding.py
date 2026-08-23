#!/usr/bin/env python3
"""Validate the canonical Chris Cruz | h4ckd4d signature in Markdown docs.

Project owner / original creator / primary maintainer: h4ckd4d
"""

from __future__ import annotations

import pathlib
import sys

ROOT = pathlib.Path(__file__).resolve().parents[1]
START = "<!-- h4ckd4d-brand-signature:start -->"
END = "<!-- h4ckd4d-brand-signature:end -->"
REQUIRED = (
    "**Chris Cruz | h4ckd4d**",
    "Cybersecurity • Red Team • Advanced Cyber Defense & Intelligence",
    "OSCP | CEH | CISSP | MITRE ATT&CK® Contributor",
    "**Founder — Project h4ckd4d**",
    "Technology for Child Protection • OSINT • Threat Intelligence",
    '*"Protect. Detect. Defend."*',
)

EXCLUDED = {
    ROOT / "BRANDING.md",
}


def markdown_files():
    for path in sorted(ROOT.rglob("*.md")):
        if path in EXCLUDED or ".git" in path.parts:
            continue
        yield path


def main() -> int:
    errors: list[str] = []
    checked = 0

    for path in markdown_files():
        checked += 1
        text = path.read_text(encoding="utf-8")
        rel = path.relative_to(ROOT)

        if text.count(START) != 1 or text.count(END) != 1:
            errors.append(f"{rel}: expected exactly one managed branding block")
            continue

        start = text.index(START)
        end = text.index(END, start) + len(END)
        block = text[start:end]
        for required in REQUIRED:
            if required not in block:
                errors.append(f"{rel}: missing branding element: {required}")

    if errors:
        print("Branding validation failed:\n")
        print("\n".join(errors))
        return 1

    print(f"Branding validation passed for {checked} Markdown documents.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
