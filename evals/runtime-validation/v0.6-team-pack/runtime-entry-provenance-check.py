#!/usr/bin/env python3
"""Check v0.6 runtime result provenance and validation boundaries."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[3]
PACKAGE_ROOT = REPO_ROOT / "evals" / "runtime-validation" / "v0.6-team-pack"

REQUIRED_FIELDS = (
    "entry_source",
    "entry_chain",
    "binding_scope",
    "result_status",
    "fixture_boundary",
    "verifier_status",
    "closure_gate_status",
    "known_limitations",
)

ALLOWED_RESULT_STATUSES = {
    "installed-plugin-direct-pass",
    "installed-plugin-enabled-thin-binding-pass",
    "project-thin-binding-pass",
    "runtime-with-fixture-pass",
    "runtime-with-fixture-partial",
    "needs-runtime-validation",
    "host-surface-unavailable",
    "blocked",
    "partial",
    "fail",
    "not-run",
}

RESULT_FILES = {
    "r225c-installed-plugin": PACKAGE_ROOT
    / "results"
    / "r225c-codex-installed-plugin-thin-binding"
    / "installed-plugin-invocation.md",
    "r226b-installed-plugin": PACKAGE_ROOT
    / "results"
    / "r226b-codex-installed-plugin-fresh-session"
    / "installed-plugin-fresh-session.md",
    "r227b-full-regression": PACKAGE_ROOT
    / "results"
    / "r227b-codex-installed-plugin-full-regression"
    / "installed-plugin-full-regression.md",
    "r227b-scenario-01": PACKAGE_ROOT
    / "results"
    / "r227b-codex-installed-plugin-full-regression"
    / "scenario-01-create-marketing-growth-team.md",
    "r227b-scenario-02": PACKAGE_ROOT
    / "results"
    / "r227b-codex-installed-plugin-full-regression"
    / "scenario-02-use-marketing-growth-team-weekly-content.md",
    "r227b-scenario-03": PACKAGE_ROOT
    / "results"
    / "r227b-codex-installed-plugin-full-regression"
    / "scenario-03-create-after-sales-service-team.md",
    "r227b-scenario-04": PACKAGE_ROOT
    / "results"
    / "r227b-codex-installed-plugin-full-regression"
    / "scenario-04-existing-after-sales-team-feedback.md",
    "r228a-enable-entry": PACKAGE_ROOT
    / "results"
    / "r228a-codex-installed-plugin-scenario-02-03"
    / "enable-entry-result.md",
    "r228a-scenario-02": PACKAGE_ROOT
    / "results"
    / "r228a-codex-installed-plugin-scenario-02-03"
    / "scenario-02-use-marketing-growth-team-weekly-content-raw.md",
    "r228a-scenario-03": PACKAGE_ROOT
    / "results"
    / "r228a-codex-installed-plugin-scenario-02-03"
    / "scenario-03-create-after-sales-service-team-raw.md",
    "r228b-scenario-04-verifier-closure": PACKAGE_ROOT
    / "results"
    / "r228b-codex-scenario-04-verifier-closure"
    / "r228b-scenario04-result.md",
    "r229c-scenario-01": PACKAGE_ROOT
    / "results"
    / "r229c-codex-installed-plugin-four-task-unified-regression"
    / "scenario-01-result.md",
    "r229c-scenario-02": PACKAGE_ROOT
    / "results"
    / "r229c-codex-installed-plugin-four-task-unified-regression"
    / "scenario-02-result.md",
    "r229c-scenario-03": PACKAGE_ROOT
    / "results"
    / "r229c-codex-installed-plugin-four-task-unified-regression"
    / "scenario-03-result.md",
    "r229c-scenario-04": PACKAGE_ROOT
    / "results"
    / "r229c-codex-installed-plugin-four-task-unified-regression"
    / "scenario-04-result.md",
}

JSON_FILES = (
    REPO_ROOT / "evals" / "fixtures" / "v0.6-team-pack" / "after-sales-feedback-20.synthetic.json",
    REPO_ROOT / "evals" / "fixtures" / "v0.6-team-pack" / "workbuddy-expert-group.synthetic.json",
)

STATE_FILES = (
    REPO_ROOT / "release" / "integration-notes" / "v0.6-acceptance-matrix.md",
    PACKAGE_ROOT / "result-summary-template.md",
)

ROSTER_GLOBS = (
    "examples/team-packs/*/roster.json",
    "templates/team-pack/**/roster.json",
    "evals/team-workflows/**/roster.json",
)

FORBIDDEN_ROLE_NAME_PATTERNS = (
    "ServiceAgent",
    "选题策略 Pal",
    "推广方案 Pal",
    "文案 Pal",
    "设计 Pal",
    "售后处理 Pal",
    "客服 Pal",
)

NEGATIVE_CONTEXT_MARKERS = (
    "do not",
    "don't",
    "forbidden",
    "bad pattern",
    "role-title-only",
    "agent-style",
    "negative",
    "example",
    "禁止",
    "不要",
    "不能",
    "不得",
    "负例",
    "not used",
)


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def normalize(text: str) -> str:
    return re.sub(r"\s+", " ", text.lower())


def parse_first_fenced_mapping(text: str) -> dict[str, str]:
    match = re.search(r"```(?:yaml|yml)\s*\n(.*?)\n```", text, flags=re.DOTALL | re.IGNORECASE)
    if not match:
        return {}
    fields: dict[str, str] = {}
    for raw_line in match.group(1).splitlines():
        line = raw_line.strip()
        if not line or line.startswith("#") or ":" not in line:
            continue
        key, value = line.split(":", 1)
        fields[key.strip()] = value.strip().strip('"').strip("'")
    return fields


def require(condition: bool, message: str, errors: list[str]) -> None:
    if not condition:
        errors.append(message)


def has_negative_context(lines: list[str], index: int) -> bool:
    start = max(0, index - 2)
    end = min(len(lines), index + 3)
    window = " ".join(lines[start:end]).lower()
    return any(marker in window for marker in NEGATIVE_CONTEXT_MARKERS)


def check_forbidden_role_names(label: str, text: str, errors: list[str]) -> None:
    lines = text.splitlines()
    for index, line in enumerate(lines):
        for pattern in FORBIDDEN_ROLE_NAME_PATTERNS:
            if pattern in line and not has_negative_context(lines, index):
                errors.append(f"{label}: forbidden role-name Pal pattern `{pattern}` on line {index + 1}")


def check_template(errors: list[str]) -> None:
    template = read_text(PACKAGE_ROOT / "result-summary-template.md")
    for field in REQUIRED_FIELDS:
        require(f"{field}:" in template, f"template missing `{field}`", errors)
    for status in ALLOWED_RESULT_STATUSES - {"not-run"}:
        require(status in template, f"template missing result status `{status}`", errors)


def check_json_parse(errors: list[str]) -> None:
    json_paths = list(JSON_FILES)
    for pattern in ROSTER_GLOBS:
        json_paths.extend(REPO_ROOT.glob(pattern))

    for path in sorted(set(json_paths)):
        try:
            json.loads(read_text(path))
        except Exception as exc:  # noqa: BLE001 - surface exact local parse failure.
            errors.append(f"{path.relative_to(REPO_ROOT)}: JSON parse failed: {exc}")


def check_result_file(label: str, path: Path, errors: list[str]) -> None:
    text = read_text(path)
    fields = parse_first_fenced_mapping(text)
    normalized = normalize(text)

    for field in REQUIRED_FIELDS:
        require(fields.get(field), f"{label}: missing provenance field `{field}`", errors)

    result_status = fields.get("result_status", "")
    require(
        result_status in ALLOWED_RESULT_STATUSES,
        f"{label}: invalid result_status `{result_status}`",
        errors,
    )

    entry_source = fields.get("entry_source", "")
    entry_chain = fields.get("entry_chain", "")
    fixture_boundary = fields.get("fixture_boundary", "")
    verifier_status = fields.get("verifier_status", "")

    if result_status == "installed-plugin-direct-pass":
        require("plugin cache" in normalized and "skill.md" in normalized, f"{label}: plugin direct pass lacks plugin Skill evidence", errors)

    if result_status == "installed-plugin-enabled-thin-binding-pass":
        require("enable" in normalize(entry_chain) and "thin binding" in normalize(entry_chain), f"{label}: plugin-enabled thin binding lacks enable chain", errors)
        require("plugin" in normalize(entry_source), f"{label}: plugin-enabled thin binding lacks plugin entry_source", errors)

    if result_status == "project-thin-binding-pass":
        require("plugin direct" not in normalized and "installed-plugin-direct-pass" not in normalized, f"{label}: project thin binding is mixed with plugin direct pass", errors)

    if result_status in {"runtime-with-fixture-pass", "runtime-with-fixture-partial"}:
        fixture_text = normalize(fixture_boundary)
        require(
            "synthetic" in fixture_text or "local fixture" in fixture_text or "not live" in fixture_text,
            f"{label}: fixture result lacks synthetic/local/not-live boundary",
            errors,
        )
        require("live customer" not in normalized or "not live customer" in normalized, f"{label}: fixture result may overclaim live customer validation", errors)
        require("live web validation" not in normalized or "not live web validation" in normalized, f"{label}: fixture result may overclaim live web validation", errors)

    if "scenario-04" in label and result_status.endswith("pass"):
        require(
            verifier_status in {"pass", "legally-skipped-with-reason", "not-required-with-reason"},
            f"{label}: Scenario 04 pass requires verifier_status pass or explicit legal skip",
            errors,
        )

    if "slash" in normalized and "host surface" in normalized:
        require(
            "host-surface-unavailable" in normalized or "not-run" in normalized,
            f"{label}: slash command host surface unavailable must be not-run or host-surface-unavailable",
            errors,
        )

    check_forbidden_role_names(label, text, errors)


def check_state_files(errors: list[str]) -> None:
    for path in STATE_FILES:
        text = read_text(path)
        check_forbidden_role_names(str(path.relative_to(REPO_ROOT)), text, errors)

    for pattern in ROSTER_GLOBS:
        for path in REPO_ROOT.glob(pattern):
            check_forbidden_role_names(str(path.relative_to(REPO_ROOT)), read_text(path), errors)


def main() -> int:
    errors: list[str] = []

    check_template(errors)
    check_json_parse(errors)
    for label, path in RESULT_FILES.items():
        check_result_file(label, path, errors)
    check_state_files(errors)

    if errors:
        print("runtime entry provenance check: FAIL")
        for error in errors:
            print(f"- {error}")
        return 1

    print("runtime entry provenance check: PASS")
    print(f"checked result files: {len(RESULT_FILES)}")
    print(f"checked required fields: {', '.join(REQUIRED_FIELDS)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
