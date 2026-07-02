#!/usr/bin/env python3
"""Manage AgentPal thin binding files for a Claude Code project."""

from __future__ import annotations

import argparse
import json
import re
import shutil
import sys
from pathlib import Path
from typing import Any


PLUGIN_ROOT = Path(__file__).resolve().parents[1]
REPO_ROOT = Path(__file__).resolve().parents[4]
for candidate in (PLUGIN_ROOT, REPO_ROOT):
    candidate_str = str(candidate)
    if candidate_str not in sys.path:
        sys.path.insert(0, candidate_str)

from shared.agentpal_binding_common import (
    CORE_GATE_PATHS,
    FORBIDDEN_THICK_BINDING_DIRS,
    RUNTIME_BINDINGS,
    any_runtime_block_present,
    is_agentpal_source,
    load_json_dict,
    merge_enabled_runtimes,
    read_text,
    remaining_runtimes_after_disable,
    remove_all_compatible_blocks,
    replace_template_values,
    resolve_agentpal_source,
    resolve_project_root,
    runtime_block_counts,
    update_project_json_after_runtime_disable,
    upsert_runtime_block,
    utc_now,
    write_json_dict,
    write_text,
)

CLAUDE_BLOCK_TEMPLATE = PLUGIN_ROOT / "templates" / "CLAUDE.agentpal-block.md"
CLAUDE_AGENTPAL_TEMPLATE = PLUGIN_ROOT / "templates" / ".agentpal" / "AGENTPAL.md"
CLAUDE_PROJECT_JSON_TEMPLATE = PLUGIN_ROOT / "templates" / ".agentpal" / "project.json"
CONFIG = RUNTIME_BINDINGS["claude-code"]

RUNTIME_TEMPLATE_ANCHORS = [
    ("workflow_execution_contract", "Workflow Execution Contract"),
    ("closure_gate", "Closure Gate"),
    ("open_role", "open role"),
    ("pal_naming", "Pal naming"),
    ("faye_boundary", "Faye"),
    ("no_fake_verifier", "no fake verifier"),
    ("no_simulated_as_real", "simulated-as-real"),
    ("team_pack_selection", "Team Pack"),
    ("palsmith_team_creation", "PalSmith"),
]


def binding_project_json(project_root: Path, source: dict[str, Any]) -> dict[str, Any]:
    project_json_path = project_root / ".agentpal" / "project.json"
    existing = load_json_dict(project_json_path)
    now = utc_now()
    created_at = existing.get("created_at") or existing.get("enabled_at") or now

    replacements = {
        "__PROJECT_NAME__": project_root.name,
        "__ACTIVE_PROJECT_ROOT__": str(project_root),
        "__AGENTPAL_SOURCE__": source["type"],
        "__AGENTPAL_SOURCE_VALUE__": source["value"],
        "__AGENTPAL_WORKSPACE_ROOT__": source.get("workspace_root", ""),
        "__CREATED_AT__": created_at,
        "__UPDATED_AT__": now,
    }
    template = json.loads(CLAUDE_PROJECT_JSON_TEMPLATE.read_text(encoding="utf-8"))
    template = replace_template_values(template, replacements)

    enabled_runtimes = merge_enabled_runtimes(existing.get("enabled_runtimes"), "claude-code")
    merged = dict(existing)
    merged.update(template)
    merged["binding_version"] = merged.get("binding_version") or "1.0"
    merged["project_root_hint"] = str(project_root)
    merged["runtime"] = "claude-code"
    merged["last_runtime"] = "claude-code"
    merged["enabled_runtimes"] = enabled_runtimes
    merged["agentpal_source"] = source
    merged["agentpal_source_type"] = source["type"]
    merged["agentpal_source_detail"] = source
    merged["agentpal_source_value"] = source["value"]
    merged["agentpal_workspace_root"] = source.get("workspace_root", "")
    merged["created_at"] = created_at
    merged["enabled_at"] = existing.get("enabled_at") or created_at
    merged["updated_at"] = now
    merged["status"] = "enabled"
    merged["core_gate_paths"] = merged.get("core_gate_paths") or CORE_GATE_PATHS
    merged["forbidden_default_project_binding_dirs"] = merged.get("forbidden_default_project_binding_dirs") or FORBIDDEN_THICK_BINDING_DIRS
    return merged


def agentpal_md_text() -> str:
    return CLAUDE_AGENTPAL_TEMPLATE.read_text(encoding="utf-8")


def claude_block_text() -> str:
    return CLAUDE_BLOCK_TEMPLATE.read_text(encoding="utf-8")


def extract_primary_claude_block(text: str) -> str:
    pattern = re.compile(
        rf"(?ms)^\s*{re.escape(CONFIG.primary_begin)}\s*$[\s\S]*?^\s*{re.escape(CONFIG.primary_end)}\s*$"
    )
    match = pattern.search(text)
    return match.group(0) if match else ""


def missing_template_anchors(text: str) -> list[str]:
    normalized = text.lower()
    return [anchor_id for anchor_id, phrase in RUNTIME_TEMPLATE_ANCHORS if phrase.lower() not in normalized]


def inspect_runtime_template_anchors(project_root: Path, primary_count: int) -> dict[str, list[str]]:
    agentpal_md_path = project_root / ".agentpal" / "AGENTPAL.md"
    claude_path = project_root / CONFIG.host_file
    checks: dict[str, list[str]] = {}

    if primary_count == 1:
        checks["CLAUDE.md"] = missing_template_anchors(extract_primary_claude_block(read_text(claude_path)))
    if agentpal_md_path.exists():
        checks[".agentpal/AGENTPAL.md"] = missing_template_anchors(read_text(agentpal_md_path))

    return checks


def write_binding_files(project_root: Path, source: dict[str, Any]) -> tuple[list[str], str]:
    changed: list[str] = []
    agentpal_dir = project_root / ".agentpal"
    agentpal_dir.mkdir(parents=True, exist_ok=True)

    project_json_path = agentpal_dir / "project.json"
    next_project_json = binding_project_json(project_root, source)
    next_project_json_text = json.dumps(next_project_json, ensure_ascii=False, indent=2) + "\n"
    if read_text(project_json_path) != next_project_json_text:
        write_json_dict(project_json_path, next_project_json)
        changed.append(str(project_json_path))

    agentpal_md_path = agentpal_dir / "AGENTPAL.md"
    next_agentpal_md = agentpal_md_text()
    if read_text(agentpal_md_path) != next_agentpal_md:
        write_text(agentpal_md_path, next_agentpal_md)
        changed.append(str(agentpal_md_path))

    claude_path = project_root / CONFIG.host_file
    block_changed, block_action = upsert_runtime_block(claude_path, claude_block_text(), CONFIG)
    if block_changed:
        changed.append(str(claude_path))

    return changed, block_action


def inspect_status(project_root: Path) -> dict[str, Any]:
    project_json_path = project_root / ".agentpal" / "project.json"
    agentpal_md_path = project_root / ".agentpal" / "AGENTPAL.md"
    claude_path = project_root / CONFIG.host_file
    counts = runtime_block_counts(project_root, "claude-code")
    primary_count = counts["primary"]
    simple_pair = CONFIG.compatible_pairs[1]
    legacy_pair = CONFIG.compatible_pairs[2]
    simple_count = counts[f"{simple_pair[0]}|{simple_pair[1]}"]
    legacy_count = counts[f"{legacy_pair[0]}|{legacy_pair[1]}"]
    total_count = counts["total"]
    has_any_artifact = project_json_path.exists() or agentpal_md_path.exists() or total_count > 0
    project_data = load_json_dict(project_json_path)
    enabled_runtimes = project_data.get("enabled_runtimes")
    enabled_runtime_list = [item for item in enabled_runtimes if isinstance(item, str)] if isinstance(enabled_runtimes, list) else []
    claude_enabled = "claude-code" in enabled_runtime_list
    other_runtime_present = any_runtime_block_present(project_root, "codex") or any(item != "claude-code" for item in enabled_runtime_list)

    if not has_any_artifact:
        return {
            "project_root": str(project_root),
            "status": "unbound",
            "issues": [],
            "malformed": [],
            "files": {
                ".agentpal/project.json": False,
                ".agentpal/AGENTPAL.md": False,
                "CLAUDE.md": claude_path.exists(),
                "CLAUDE.md_claude_block": False,
            },
            "block_variant": "none",
            "recommended_command": "/agentpal:enable",
        }

    if total_count == 0 and not claude_enabled and other_runtime_present:
        return {
            "project_root": str(project_root),
            "status": "unbound",
            "issues": [],
            "malformed": [],
            "files": {
                ".agentpal/project.json": project_json_path.exists(),
                ".agentpal/AGENTPAL.md": agentpal_md_path.exists(),
                "CLAUDE.md": claude_path.exists(),
                "CLAUDE.md_claude_block": False,
            },
            "block_variant": "none",
            "recommended_command": "/agentpal:enable",
        }

    issues: list[str] = []
    malformed: list[str] = []
    block_variant = "runtime-qualified"

    if primary_count == 0 and (simple_count == 1 or legacy_count == 1) and total_count == 1:
        block_variant = "legacy"
    elif total_count == 0:
        issues.append("missing_claude_block")
        block_variant = "missing"
    elif primary_count != 1 or total_count != 1:
        malformed.append("claude_block_count_invalid")
        block_variant = "mixed-or-duplicate"

    if not project_json_path.exists():
        issues.append("missing_project_json")
    if not agentpal_md_path.exists():
        issues.append("missing_agentpal_md")

    data: dict[str, Any] | None = None
    if project_json_path.exists():
        try:
            loaded = json.loads(project_json_path.read_text(encoding="utf-8"))
        except json.JSONDecodeError:
            loaded = None
            malformed.append("project_json_invalid")
        if isinstance(loaded, dict):
            data = loaded
        elif loaded is not None:
            malformed.append("project_json_invalid")

    if data is not None:
        required = [
            "schema_version",
            "project_name",
            "binding_type",
            "default_pal",
            "runtime",
            "agentpal_source",
            "created_at",
            "updated_at",
        ]
        missing_required = [key for key in required if key not in data]
        if missing_required:
            malformed.append(f"missing_required_fields:{','.join(missing_required)}")
        if data.get("binding_type") != "thin":
            malformed.append("binding_type_not_thin")
        if data.get("default_pal") != "Mira":
            malformed.append("default_pal_not_mira")
        if data.get("runtime") != "claude-code":
            malformed.append("runtime_not_claude_code")
        source_issue = inspect_source_issue(data)
        if source_issue:
            issues.append(source_issue)

    runtime_anchor_checks = inspect_runtime_template_anchors(project_root, primary_count)
    for filename, missing_anchors in runtime_anchor_checks.items():
        if missing_anchors:
            issues.append(f"missing_runtime_template_anchors:{filename}:{','.join(missing_anchors)}")

    if block_variant == "legacy" and not issues and not malformed:
        status = "legacy-block"
        recommended = "/agentpal:repair"
    elif malformed:
        status = "damaged"
        recommended = "/agentpal:repair"
    elif issues:
        status = "partial"
        recommended = "/agentpal:repair"
    else:
        status = "complete"
        recommended = "/agentpal:disable"

    return {
        "project_root": str(project_root),
        "status": status,
        "issues": issues,
        "malformed": malformed,
        "files": {
            ".agentpal/project.json": project_json_path.exists(),
            ".agentpal/AGENTPAL.md": agentpal_md_path.exists(),
            "CLAUDE.md": claude_path.exists(),
            "CLAUDE.md_claude_block": primary_count == 1,
        },
        "block_variant": block_variant,
        "recommended_command": recommended,
        "block_counts": {
            "runtime_qualified": primary_count,
            "simple_legacy": simple_count,
            "workgroup_legacy": legacy_count,
        },
        "runtime_template_anchor_checks": {
            "required": [anchor_id for anchor_id, _phrase in RUNTIME_TEMPLATE_ANCHORS],
            "missing": runtime_anchor_checks,
        },
    }


def inspect_source_issue(data: dict[str, Any]) -> str | None:
    detail = data.get("agentpal_source_detail")
    if not isinstance(detail, dict):
        maybe_detail = data.get("agentpal_source")
        if isinstance(maybe_detail, dict):
            detail = maybe_detail

    source_type = data.get("agentpal_source")
    if not isinstance(source_type, str):
        source_type = data.get("agentpal_source_type")
    if isinstance(detail, dict):
        source_type = detail.get("type") or source_type

    if source_type not in {"central_path", "user_configured_source"}:
        return None

    path_value = ""
    if isinstance(detail, dict):
        path_value = detail.get("value") or detail.get("path") or detail.get("workspace_root") or ""
    path_value = path_value or data.get("agentpal_workspace_root") or data.get("agentpal_source_value") or ""
    if not path_value:
        return "source_path_missing"
    return None if is_agentpal_source(Path(path_value)) else "source_unavailable"


def enable(args: argparse.Namespace) -> dict[str, Any]:
    project_root = resolve_project_root(args.project_root)
    status_before = inspect_status(project_root)
    source = resolve_agentpal_source(args.agentpal_source, project_root)
    changed, block_action = write_binding_files(project_root, source)
    status_after = inspect_status(project_root)
    return {
        "action": "enable",
        "project_root": str(project_root),
        "status_before": status_before["status"],
        "status_after": status_after["status"],
        "changed": changed,
        "block_action": block_action,
        "agentpal_source": source,
    }


def repair(args: argparse.Namespace) -> dict[str, Any]:
    project_root = resolve_project_root(args.project_root)
    status_before = inspect_status(project_root)
    if status_before["status"] == "unbound":
        return {
            "action": "repair",
            "project_root": str(project_root),
            "status_before": "unbound",
            "status_after": "unbound",
            "changed": [],
            "recommended_command": "/agentpal:enable",
        }

    project_json_path = project_root / ".agentpal" / "project.json"
    existing = load_json_dict(project_json_path)
    source = resolve_agentpal_source(args.agentpal_source, project_root)
    detail = existing.get("agentpal_source_detail")
    if isinstance(detail, dict) and not args.agentpal_source:
        source = {
            "type": detail.get("type") or (existing.get("agentpal_source") if isinstance(existing.get("agentpal_source"), str) else None) or source["type"],
            "value": detail.get("value") or existing.get("agentpal_source_value") or source["value"],
            "workspace_root": detail.get("workspace_root") or existing.get("agentpal_workspace_root") or source.get("workspace_root", ""),
            "available": detail.get("available", source.get("available")),
        }

    changed, block_action = write_binding_files(project_root, source)
    status_after = inspect_status(project_root)
    return {
        "action": "repair",
        "project_root": str(project_root),
        "status_before": status_before["status"],
        "status_after": status_after["status"],
        "changed": changed,
        "block_action": block_action,
        "agentpal_source": source,
    }


def disable(args: argparse.Namespace) -> dict[str, Any]:
    project_root = resolve_project_root(args.project_root)
    status_before = inspect_status(project_root)
    changed: list[str] = []

    claude_path = project_root / CONFIG.host_file
    if claude_path.exists():
        next_text, removed = remove_all_compatible_blocks(read_text(claude_path), CONFIG.compatible_pairs)
        if removed:
            write_text(claude_path, next_text)
            changed.append(str(claude_path))

    agentpal_dir = project_root / ".agentpal"
    other_runtimes = remaining_runtimes_after_disable(project_root, disabled_runtime="claude-code")
    if agentpal_dir.exists() and other_runtimes:
        if update_project_json_after_runtime_disable(agentpal_dir / "project.json", disabled_runtime="claude-code", remaining_runtimes=other_runtimes):
            changed.append(str(agentpal_dir / "project.json"))
    elif agentpal_dir.exists():
        shutil.rmtree(agentpal_dir)
        changed.append(str(agentpal_dir))

    status_after = inspect_status(project_root)
    return {
        "action": "disable",
        "project_root": str(project_root),
        "status_before": status_before["status"],
        "status_after": status_after["status"],
        "changed": changed,
        "preserved_other_runtimes": other_runtimes,
        "codex_block_still_present": any_runtime_block_present(project_root, "codex"),
    }


def status(args: argparse.Namespace) -> dict[str, Any]:
    return inspect_status(resolve_project_root(args.project_root))


def print_result(result: dict[str, Any], json_only: bool) -> None:
    if not json_only:
        print(f"AgentPal Claude binding {result.get('action', 'status')}: {result.get('status_after') or result.get('status')}")
        if "changed" in result:
            print("Changed:")
            if result["changed"]:
                for item in result["changed"]:
                    print(f"- {item}")
            else:
                print("- none")
    print(json.dumps(result, ensure_ascii=False, indent=2))


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Manage AgentPal Claude Code thin binding files.")
    parser.add_argument("action", choices=["enable", "disable", "status", "repair"])
    parser.add_argument("--project-root", default=None, help="Target project root. Defaults to current working directory.")
    parser.add_argument("--agentpal-source", default=None, help="AgentPal source root or GitHub URL.")
    parser.add_argument("--json", action="store_true", help="Print JSON only.")
    return parser


def main(argv: list[str]) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)

    if args.action == "enable":
        result = enable(args)
    elif args.action == "disable":
        result = disable(args)
    elif args.action == "status":
        result = status(args)
    elif args.action == "repair":
        result = repair(args)
    else:
        raise AssertionError(args.action)

    print_result(result, args.json)
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
