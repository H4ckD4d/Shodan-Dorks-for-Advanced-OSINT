#!/usr/bin/env python3
"""Validate structured framework files without contacting external services.

Project owner: h4ckd4d
"""

from __future__ import annotations

import json
import pathlib
import py_compile
import sys

ROOT = pathlib.Path(__file__).resolve().parents[1]
JSON_FILES = [
    ROOT / "schemas" / "scope.schema.json",
    ROOT / "catalog" / "index.json",
    ROOT / "catalog" / "exposure-categories.json",
    ROOT / "examples" / "authorized-scope.json",
]


def validate_json() -> list[str]:
    errors: list[str] = []
    for path in JSON_FILES:
        try:
            json.loads(path.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError) as exc:
            errors.append(f"{path.relative_to(ROOT)}: {exc}")
    return errors


def validate_scope_example() -> list[str]:
    errors: list[str] = []
    path = ROOT / "examples" / "authorized-scope.json"
    data = json.loads(path.read_text(encoding="utf-8"))
    if data.get("authorization", {}).get("confirmed") is not True:
        errors.append("examples/authorized-scope.json: authorization.confirmed must be true")
    if not data.get("scope"):
        errors.append("examples/authorized-scope.json: scope must not be empty")
    return errors


def validate_python() -> list[str]:
    errors: list[str] = []
    for relative in ["scripts/validate_filters.py", "scripts/scope_query_builder.py"]:
        path = ROOT / relative
        try:
            py_compile.compile(str(path), doraise=True)
        except py_compile.PyCompileError as exc:
            errors.append(f"{relative}: {exc.msg}")
    return errors


def main() -> int:
    errors = validate_json() + validate_scope_example() + validate_python()
    if errors:
        print("Framework validation failed:\n")
        print("\n".join(errors))
        return 1
    print("Framework validation passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
