#!/usr/bin/env python3
"""Apply the canonical Chris Cruz | h4ckd4d signature to Markdown docs.

Project owner / original creator / primary maintainer: h4ckd4d

This utility edits repository Markdown only. It does not contact Shodan,
external systems, or Internet targets.
"""

from __future__ import annotations

import pathlib
import re

ROOT = pathlib.Path(__file__).resolve().parents[1]
START = "<!-- h4ckd4d-brand-signature:start -->"
END = "<!-- h4ckd4d-brand-signature:end -->"

SIGNATURE = f'''{START}
---

**Chris Cruz | h4ckd4d**  
Cybersecurity • Red Team • Advanced Cyber Defense & Intelligence  
OSCP | CEH | CISSP | MITRE ATT&CK® Contributor

**Founder — Project h4ckd4d**  
Technology for Child Protection • OSINT • Threat Intelligence

*"Protect. Detect. Defend."*
{END}
'''

# BRANDING.md contains the source-of-truth block itself and is maintained manually.
EXCLUDED = {
    ROOT / "BRANDING.md",
}

MARKER_RE = re.compile(
    rf"\n?{re.escape(START)}.*?{re.escape(END)}\n?",
    flags=re.DOTALL,
)


def markdown_files():
    for path in sorted(ROOT.rglob("*.md")):
        if path in EXCLUDED:
            continue
        if ".git" in path.parts:
            continue
        yield path


def normalize(text: str) -> str:
    # Remove previously managed signature blocks, then append exactly one.
    text = MARKER_RE.sub("\n", text).rstrip()
    return f"{text}\n\n{SIGNATURE}"


def main() -> int:
    changed = 0
    total = 0

    for path in markdown_files():
        total += 1
        original = path.read_text(encoding="utf-8")
        updated = normalize(original)
        if updated != original:
            path.write_text(updated, encoding="utf-8")
            changed += 1
            print(f"branded: {path.relative_to(ROOT)}")

    print(f"Branding complete: {changed} changed / {total} Markdown files checked.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
