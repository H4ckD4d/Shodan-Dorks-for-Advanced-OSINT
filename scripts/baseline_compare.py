#!/usr/bin/env python3
"""Compare an expected exposure baseline with normalized observed assets.

Project owner / original creator / primary maintainer: h4ckd4d

This tool is offline. It does not contact Shodan or any external target.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path


def load_json(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def observed_service_keys(asset: dict) -> set[tuple[int, str]]:
    keys: set[tuple[int, str]] = set()
    for tag in asset.get("tags", []):
        if isinstance(tag, str) and tag.startswith("service:"):
            parts = tag.split(":", 2)
            if len(parts) == 3 and parts[1].isdigit():
                keys.add((int(parts[1]), parts[2]))
    return keys


def expected_service_keys(asset: dict) -> set[tuple[int, str]]:
    return {
        (int(service["port"]), str(service.get("protocol", "unknown")))
        for service in asset.get("expected_services", [])
    }


def compare(baseline: dict, observed: list[dict]) -> dict:
    expected_assets = {item["value"]: item for item in baseline.get("assets", [])}
    observed_assets = {item["value"]: item for item in observed}

    expected_seen: list[dict] = []
    expected_missing: list[dict] = []
    unexpected_assets: list[dict] = []
    unexpected_services: list[dict] = []

    for value, expected in expected_assets.items():
        observed_asset = observed_assets.get(value)
        if observed_asset is None:
            expected_missing.append({"value": value, "asset_type": expected.get("asset_type")})
            continue

        expected_seen.append({"value": value, "asset_type": expected.get("asset_type")})
        exp_services = expected_service_keys(expected)
        obs_services = observed_service_keys(observed_asset)
        for port, protocol in sorted(obs_services - exp_services):
            unexpected_services.append({
                "value": value,
                "port": port,
                "protocol": protocol,
                "classification": "expected_asset_unexpected_service",
            })

    for value, asset in observed_assets.items():
        if value not in expected_assets:
            unexpected_assets.append({
                "value": value,
                "asset_type": asset.get("asset_type"),
                "ownership": asset.get("ownership", {}),
                "classification": "unknown_potentially_related_asset",
            })

    return {
        "organization": baseline.get("organization"),
        "summary": {
            "expected_seen": len(expected_seen),
            "expected_missing": len(expected_missing),
            "unexpected_assets": len(unexpected_assets),
            "unexpected_services": len(unexpected_services),
        },
        "expected_seen": expected_seen,
        "expected_missing": expected_missing,
        "unexpected_assets": unexpected_assets,
        "unexpected_services": unexpected_services,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description="Offline expected-vs-observed exposure comparison")
    parser.add_argument("baseline", type=Path)
    parser.add_argument("observed", type=Path, help="JSON array of normalized asset records")
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()

    baseline = load_json(args.baseline)
    observed = load_json(args.observed)
    if not isinstance(observed, list):
        raise SystemExit("Observed input must be a JSON array of asset objects.")

    result = compare(baseline, observed)
    rendered = json.dumps(result, indent=2, sort_keys=True)
    if args.output:
        args.output.write_text(rendered + "\n", encoding="utf-8")
    else:
        print(rendered)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
