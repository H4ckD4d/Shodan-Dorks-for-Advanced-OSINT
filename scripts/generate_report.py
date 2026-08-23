#!/usr/bin/env python3
"""Generate a concise Markdown EASM report from normalized comparison output.

Project owner / original creator / primary maintainer: h4ckd4d

Offline only: no network access and no target interaction.
"""

from __future__ import annotations

import argparse
import json
from datetime import datetime, timezone
from pathlib import Path


def load_json(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def table(rows: list[dict], columns: list[tuple[str, str]]) -> list[str]:
    if not rows:
        return ["No items."]
    lines = ["| " + " | ".join(label for _, label in columns) + " |"]
    lines.append("| " + " | ".join("---" for _ in columns) + " |")
    for row in rows:
        values = []
        for key, _ in columns:
            value = row.get(key, "")
            if isinstance(value, dict):
                value = value.get("status") or value.get("confidence") or ""
            values.append(str(value).replace("|", "\\|"))
        lines.append("| " + " | ".join(values) + " |")
    return lines


def render(data: dict) -> str:
    summary = data.get("summary", {})
    now = datetime.now(timezone.utc).isoformat()
    lines = [
        "# Internet Exposure Intelligence Report",
        "",
        "> **Project owner:** h4ckd4d",
        "",
        f"**Organization:** {data.get('organization', 'Unknown')}  ",
        f"**Generated:** {now}  ",
        "**Method:** Expected-vs-observed defensive baseline comparison",
        "",
        "## Executive summary",
        "",
        f"- Expected assets observed: **{summary.get('expected_seen', 0)}**",
        f"- Expected assets not observed: **{summary.get('expected_missing', 0)}**",
        f"- Unexpected or potentially related assets: **{summary.get('unexpected_assets', 0)}**",
        f"- Unexpected services on expected assets: **{summary.get('unexpected_services', 0)}**",
        "",
        "> Observation ≠ Finding ≠ Vulnerability ≠ Exploitability ≠ Compromise",
        "",
        "## Unexpected services",
        "",
    ]
    lines.extend(table(data.get("unexpected_services", []), [("value", "Asset"), ("port", "Port"), ("protocol", "Protocol"), ("classification", "Classification")]))
    lines.extend(["", "## Unexpected or potentially related assets", ""])
    lines.extend(table(data.get("unexpected_assets", []), [("value", "Asset"), ("asset_type", "Type"), ("ownership", "Ownership"), ("classification", "Classification")]))
    lines.extend(["", "## Expected assets not observed", ""])
    lines.extend(table(data.get("expected_missing", []), [("value", "Asset"), ("asset_type", "Type")]))
    lines.extend([
        "",
        "## Analyst guidance",
        "",
        "Validate ownership, telemetry freshness, and internal configuration before escalating any observation. Public telemetry does not authorize interaction with a system.",
        "",
        "---",
        "",
        "**Internet Exposure Intelligence Framework by h4ckd4d.**",
        "",
    ])
    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser(description="Generate Markdown exposure report from comparison JSON")
    parser.add_argument("comparison", type=Path)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()

    report = render(load_json(args.comparison))
    if args.output:
        args.output.write_text(report, encoding="utf-8")
    else:
        print(report)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
