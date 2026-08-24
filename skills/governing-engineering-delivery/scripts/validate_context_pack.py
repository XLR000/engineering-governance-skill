#!/usr/bin/env python3
"""Dependency-free structural validator for portable engineering context packs."""

from __future__ import annotations

import argparse
import json
import re
import sys
from datetime import datetime
from pathlib import Path
from typing import Any


REQUIRED_SECTIONS = [
    "## 1. Objective and scope",
    "## 2. Requirements and I/O",
    "## 3. Visual and experience baseline",
    "## 4. Technical design and architecture",
    "## 5. Coding, version and context baseline",
    "## 6. Authorization ledger",
    "## 7. Delivery slices",
    "## 8. Review gates",
    "## 9. Sandbox, security and recovery",
    "## 10. Structured debugging",
    "## 11. Verification and traceability",
    "## 12. Execution log and handoff",
    "### Governance validation",
]

AUTH_CATEGORIES = [
    "Read-only inspection",
    "Product document writes",
    "Code/test/local data writes",
    "Local lint/test/build/browser",
    "External public reads",
    "Provider calls or paid actions",
    "Commit/branch/tag/push/PR",
    "Hosted migration/deployment/secrets",
    "Publication/external message",
    "Destructive action",
]

SECURITY_FIELDS = [
    "Sandbox proof",
    "Authentication/authorization",
    "Secrets",
    "Input/injection",
    "Web security",
    "Backup/rollback",
    "Destructive behavior",
]


def finding(code: str, message: str) -> dict[str, str]:
    return {"code": code, "message": message}


def bullet(source: str, label: str) -> str | None:
    match = re.search(rf"^- {re.escape(label)}:\s*(.+?)\s*$", source, re.MULTILINE)
    return match.group(1).strip() if match else None


def section(source: str, number: int) -> str:
    match = re.search(
        rf"^## {number}\. .+?(?=^## \d+\. |\Z)", source, re.MULTILINE | re.DOTALL
    )
    return match.group(0) if match else ""


def valid_timestamp(value: str | None) -> bool:
    if not value:
        return False
    try:
        datetime.fromisoformat(value.replace("Z", "+00:00"))
    except ValueError:
        return False
    return bool(re.search(r"(?:Z|[+-]\d{2}:\d{2})$", value))


def parse_table_rows(source: str, header: str) -> list[list[str]]:
    lines = source.splitlines()
    start = next((i for i, line in enumerate(lines) if line.strip() == header), -1)
    if start < 0:
        return []
    rows: list[list[str]] = []
    for line in lines[start + 2 :]:
        stripped = line.strip()
        if not (stripped.startswith("|") and stripped.endswith("|")):
            break
        rows.append([cell.strip() for cell in stripped[1:-1].split("|")])
    return rows


def read_config(config_path: Path | None) -> tuple[dict[str, Any], Path]:
    if config_path is None:
        return {
            "schemaVersion": 1,
            "idPrefixes": ["REQ", "AC", "PLAN", "DEC", "RISK"],
            "knownIdFiles": [],
            "requiredChecks": [],
            "independentReviewRiskClasses": ["C3", "C4"],
        }, Path.cwd()
    resolved = config_path.resolve()
    config = json.loads(resolved.read_text(encoding="utf-8"))
    if config.get("schemaVersion") != 1:
        raise ValueError("Unsupported governance config schemaVersion")
    return config, resolved.parent


def known_ids(config: dict[str, Any], root: Path, pattern: re.Pattern[str]) -> set[str]:
    result: set[str] = set()
    for relative in config.get("knownIdFiles", []):
        candidate = (root / str(relative)).resolve()
        try:
            candidate.relative_to(root.resolve())
        except ValueError as error:
            raise ValueError(f"knownIdFiles path leaves config root: {relative}") from error
        if not candidate.is_file():
            raise ValueError(f"knownIdFiles entry does not exist: {relative}")
        result.update(pattern.findall(candidate.read_text(encoding="utf-8")))
    return result


def validate_source(source: str, config: dict[str, Any], config_root: Path) -> list[dict[str, str]]:
    findings: list[dict[str, str]] = []

    if re.search(r"\{\{[^}\n]+\}\}", source):
        findings.append(finding("UNRESOLVED_PLACEHOLDER", "Replace every template placeholder."))

    for heading in REQUIRED_SECTIONS:
        if heading not in source:
            findings.append(finding("MISSING_SECTION", f"Missing required section: {heading}"))

    status = bullet(source, "Status")
    risk = bullet(source, "Risk class")
    allowed_statuses = {"proposed", "approved", "in-progress", "implemented", "verified", "blocked"}
    if status not in allowed_statuses:
        findings.append(finding("INVALID_METADATA", "Status is missing or invalid."))
    if risk not in {"C0", "C1", "C2", "C3", "C4"}:
        findings.append(finding("INVALID_METADATA", "Risk class is missing or invalid."))
    for label in ["Lifecycle stage", "Requested target state", "Owner"]:
        if not bullet(source, label):
            findings.append(finding("INVALID_METADATA", f"{label} is required."))
    for label in ["Created", "Updated"]:
        if not valid_timestamp(bullet(source, label)):
            findings.append(finding("INVALID_METADATA", f"{label} must include an ISO-8601 timezone."))

    prefixes = [str(value) for value in config.get("idPrefixes", [])]
    if not prefixes:
        findings.append(finding("INVALID_CONFIG", "idPrefixes must not be empty."))
    else:
        alternatives = "|".join(re.escape(value) for value in prefixes)
        id_pattern = re.compile(rf"\b(?:{alternatives})-[A-Z0-9]+(?:-[A-Z0-9]+)*\b")
        referenced = set(id_pattern.findall(section(source, 2)))
        if not referenced:
            findings.append(finding("MISSING_STABLE_ID", "Requirements and I/O must cite a configured stable ID."))
        if config.get("knownIdFiles", []):
            try:
                canonical = known_ids(config, config_root, id_pattern)
            except ValueError as error:
                findings.append(finding("INVALID_CONFIG", str(error)))
            else:
                for identity in sorted(referenced - canonical):
                    findings.append(finding("UNKNOWN_STABLE_ID", f"Unknown stable ID: {identity}"))

    auth_header = "| Action category | State | Exact scope | Approver/source | Authorized at | Validity | Consumed/receipt |"
    rows = parse_table_rows(section(source, 6), auth_header)
    by_category = {row[0]: row for row in rows if row}
    for category in AUTH_CATEGORIES:
        if category not in by_category:
            findings.append(finding("AUTH_LEDGER_INCOMPLETE", f"Missing authorization category: {category}"))
    for row in rows:
        if (
            len(row) != 7
            or row[1] not in {"authorized", "not-authorized"}
            or not all(row[2:])
            or not valid_timestamp(row[4])
        ):
            findings.append(finding("AUTH_LEDGER_INCOMPLETE", "Every authorization row needs state, scope, source, timestamp, validity and receipt."))

    if risk in {"C2", "C3", "C4"}:
        commit = (bullet(source, "Commit") or "").replace("`", "")
        if not bullet(source, "Branch") or not re.fullmatch(r"[0-9a-fA-F]{40}", commit):
            findings.append(finding("BASELINE_INCOMPLETE", "C2-C4 requires branch and a full commit SHA."))
        if not valid_timestamp(bullet(source, "`git status --short` captured at")):
            findings.append(finding("BASELINE_INCOMPLETE", "C2-C4 requires a timestamped Git status baseline."))
        if bullet(source, "Worktree state") not in {"clean", "dirty-with-inventory"}:
            findings.append(finding("BASELINE_INCOMPLETE", "Worktree state must be clean or dirty-with-inventory."))

    security = section(source, 9)
    for label in SECURITY_FIELDS:
        if not bullet(security, label):
            findings.append(finding("SECURITY_FIELD_MISSING", f"Missing security field: {label}"))

    verification = section(source, 11)
    for command in config.get("requiredChecks", []):
        if str(command) not in verification:
            findings.append(finding("MISSING_REQUIRED_CHECK", f"Missing configured check: {command}"))

    independent_classes = set(config.get("independentReviewRiskClasses", ["C3", "C4"]))
    reviewer = bullet(source, "Reviewer")
    result = bullet(source, "Result/evidence") or ""
    mode = bullet(source, "Mode")
    blockers = bullet(source, "Active blockers")
    claims_pass = bool(re.match(r"^PASS\b", result, re.IGNORECASE))
    if risk in independent_classes and claims_pass and not re.search(r"(?:\bindependent\b|独立)", reviewer or "", re.IGNORECASE):
        findings.append(finding("MISSING_INDEPENDENT_REVIEW", f"{risk} PASS requires a named independent reviewer."))
    if mode == "manual/PARTIAL" and claims_pass:
        findings.append(finding("UNSUPPORTED_PASS", "manual/PARTIAL validation cannot claim PASS."))
    if claims_pass and blockers and blockers.lower() not in {"none", "无"}:
        findings.append(finding("UNRESOLVED_BLOCKER", "PASS cannot coexist with active blockers."))

    return findings


def validate_file(context_path: Path, config_path: Path | None = None) -> list[dict[str, str]]:
    path = context_path.resolve()
    if path.suffix.lower() != ".md" or not path.is_file():
        return [finding("INVALID_PATH", "Context must be an existing Markdown file.")]
    if path.stat().st_size > 2_000_000:
        return [finding("FILE_TOO_LARGE", "Context exceeds the 2 MB review limit.")]
    try:
        config, root = read_config(config_path)
    except (OSError, ValueError, json.JSONDecodeError) as error:
        return [finding("INVALID_CONFIG", str(error))]
    return validate_source(path.read_text(encoding="utf-8"), config, root)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("context", type=Path)
    parser.add_argument("--config", type=Path)
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args(argv)
    findings = validate_file(args.context, args.config)
    if args.json:
        print(json.dumps({"valid": not findings, "file": str(args.context), "findings": findings}, ensure_ascii=False))
    elif findings:
        for item in findings:
            print(f"{item['code']}: {item['message']}", file=sys.stderr)
    else:
        print(f"PASS {args.context}")
    return 1 if findings else 0


if __name__ == "__main__":
    raise SystemExit(main())
