#!/usr/bin/env python3
"""Unified offline CLI for the h4ckd4d Internet Exposure Intelligence framework.

Project owner / original creator / primary maintainer: h4ckd4d

The CLI validates local scope files, generates scoped query templates, compares
expected-vs-observed local datasets, and renders local reports. It does not
contact Shodan or any external target.
"""

from __future__ import annotations

import argparse
import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def run_script(script: str, args: list[str]) -> int:
    command = [sys.executable, str(ROOT / "scripts" / script), *args]
    return subprocess.call(command)


def validate_scope(path: Path) -> int:
    data = json.loads(path.read_text(encoding="utf-8"))
    auth = data.get("authorization", {})
    if auth.get("confirmed") is not True:
        print("Scope authorization is not confirmed.", file=sys.stderr)
        return 2
    assets = data.get("scope", {})
    print("Authorization: confirmed")
    print(f"Organization: {data.get('organization', 'Unknown')}")
    print(f"Domains: {len(assets.get('domains', []))}")
    print(f"CIDRs: {len(assets.get('cidrs', []))}")
    print(f"ASNs: {len(assets.get('asns', []))}")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(prog="h4ckd4d-osint", description="Offline defensive Internet Exposure Intelligence CLI")
    sub = parser.add_subparsers(dest="command", required=True)

    scope = sub.add_parser("scope", help="Validate an authorized local scope file")
    scope.add_argument("file", type=Path)

    queries = sub.add_parser("queries", help="Generate scoped Shodan query templates")
    queries.add_argument("scope_file", type=Path)

    baseline = sub.add_parser("baseline", help="Compare expected baseline with normalized observed assets")
    baseline.add_argument("baseline_file", type=Path)
    baseline.add_argument("observed_file", type=Path)
    baseline.add_argument("--output", type=Path)

    report = sub.add_parser("report", help="Generate Markdown report from comparison JSON")
    report.add_argument("comparison_file", type=Path)
    report.add_argument("--output", type=Path)

    args = parser.parse_args()

    if args.command == "scope":
        return validate_scope(args.file)
    if args.command == "queries":
        return run_script("scope_query_builder.py", [str(args.scope_file)])
    if args.command == "baseline":
        command_args = [str(args.baseline_file), str(args.observed_file)]
        if args.output:
            command_args += ["--output", str(args.output)]
        return run_script("baseline_compare.py", command_args)
    if args.command == "report":
        command_args = [str(args.comparison_file)]
        if args.output:
            command_args += ["--output", str(args.output)]
        return run_script("generate_report.py", command_args)
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
