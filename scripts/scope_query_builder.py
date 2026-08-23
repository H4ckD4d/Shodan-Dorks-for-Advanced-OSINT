#!/usr/bin/env python3
"""Generate defensive Shodan query templates from an explicitly authorized scope.

Project owner: h4ckd4d

This tool does not contact Shodan and does not execute searches. It only reads a
local JSON scope file and prints query templates for analyst review.
"""

from __future__ import annotations

import argparse
import ipaddress
import json
from pathlib import Path


def load_scope(path: Path) -> dict:
    data = json.loads(path.read_text(encoding="utf-8"))
    auth = data.get("authorization", {})
    if auth.get("confirmed") is not True:
        raise ValueError("authorization.confirmed must be true")
    return data


def validate_scope(data: dict) -> None:
    scope = data.get("scope", {})

    for cidr in scope.get("cidrs", []):
        ipaddress.ip_network(cidr, strict=False)

    for asn in scope.get("asns", []):
        if not (isinstance(asn, str) and asn.startswith("AS") and asn[2:].isdigit()):
            raise ValueError(f"invalid ASN: {asn}")


def quote(value: str) -> str:
    escaped = value.replace('"', '\\"')
    return f'"{escaped}"'


def build_queries(data: dict) -> list[tuple[str, str]]:
    scope = data.get("scope", {})
    queries: list[tuple[str, str]] = []

    for org in scope.get("organizations", []):
        queries.extend([
            ("Organization inventory", f"org:{quote(org)}"),
            ("Organization HTTPS", f"org:{quote(org)} port:443"),
            ("Organization TLS", f"org:{quote(org)} has_ssl:true"),
        ])

    for cidr in scope.get("cidrs", []):
        queries.extend([
            ("Network inventory", f"net:{quote(cidr)}"),
            ("Network HTTPS", f"net:{quote(cidr)} port:443"),
            ("Network SSH review", f"net:{quote(cidr)} port:22"),
        ])

    for asn in scope.get("asns", []):
        queries.extend([
            ("ASN inventory", f"asn:{quote(asn)}"),
            ("ASN HTTPS", f"asn:{quote(asn)} port:443"),
        ])

    for domain in scope.get("domains", []):
        queries.extend([
            ("Hostname relationship", f"hostname:{quote(domain)}"),
            ("Certificate subject relationship", f"ssl.cert.subject.cn:{quote(domain)}"),
        ])

    return queries


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Generate defensive Shodan queries from an authorized JSON scope."
    )
    parser.add_argument("scope_file", type=Path)
    args = parser.parse_args()

    try:
        data = load_scope(args.scope_file)
        validate_scope(data)
    except (OSError, json.JSONDecodeError, ValueError) as exc:
        print(f"scope error: {exc}")
        return 2

    print("Authorized-scope query templates\n")
    for title, query in build_queries(data):
        print(f"[{title}]\n{query}\n")

    print("Review every query against the approved assessment scope before use.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
