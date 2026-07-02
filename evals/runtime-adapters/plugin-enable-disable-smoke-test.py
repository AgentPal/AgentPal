#!/usr/bin/env python3
"""Smoke tests for AgentPal Codex and Claude Code thin binding helpers."""

from __future__ import annotations

import json
import re
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[2]
CODEX_HELPER = REPO_ROOT / "plugins" / "codex" / "agentpal-codex-plugin" / "scripts" / "agentpal_binding.py"
CLAUDE_HELPER = REPO_ROOT / "integrations" / "claude-code" / "agentpal-project-binder" / "scripts" / "agentpal_binding.py"

CODEX_BEGIN = "<!-- BEGIN AGENTPAL BINDING: codex -->"
CODEX_END = "<!-- END AGENTPAL BINDING: codex -->"
CLAUDE_BEGIN = "<!-- BEGIN AGENTPAL BINDING: claude-code -->"
CLAUDE_END = "<!-- END AGENTPAL BINDING: claude-code -->"

RUNTIME_ENTRY_ANCHORS = {
    "workflow_execution_contract": ("workflow execution contract", "workflow_execution_contract"),
    "closure_gate": ("closure gate", "closure_gate"),
    "open_role": ("open role", "open_roles", "open_role"),
    "pal_naming": ("pal naming", "new pal proposals must use a human", "display_name"),
    "faye_boundary": ("faye boundary", "faye_boundary", "faye may", "faye is"),
    "no_fake_verifier": ("no fake verifier", "no_fake_verifier", "fake verifier"),
    "no_simulated_as_real": ("simulated-as-real", "no_simulated_as_real", "do not present simulated", "do not mark unavailable work as done"),
    "team_pack_selection": ("team pack selection", "team_pack_selection", "selected_team", "choose team pack", "inspect a fitting team pack", "existing team pack"),
    "palsmith_team_creation": ("palsmith team creation", "palsmith_team_creation", "palsmith owns", "palsmith handles", "palsmith's default team pack creation"),
}

RUNTIME_ENTRY_FILES = {
    "claude-code-template-block": REPO_ROOT / "templates" / "project-binding" / "claude-code" / "CLAUDE.agentpal-block.md",
    "claude-code-template-agentpal": REPO_ROOT / "templates" / "project-binding" / "claude-code" / ".agentpal" / "AGENTPAL.md",
    "claude-code-plugin-block": REPO_ROOT / "integrations" / "claude-code" / "agentpal-project-binder" / "templates" / "CLAUDE.agentpal-block.md",
    "claude-code-plugin-agentpal": REPO_ROOT / "integrations" / "claude-code" / "agentpal-project-binder" / "templates" / ".agentpal" / "AGENTPAL.md",
    "codex-template-agents": REPO_ROOT / "templates" / "project-binding" / "generic-codex" / "AGENTS.agentpal-block.md",
    "codex-template-agentpal": REPO_ROOT / "templates" / "project-binding" / "generic-codex" / ".agentpal" / "AGENTPAL.md",
    "codex-plugin-entry-skill": REPO_ROOT / "plugins" / "codex" / "agentpal-codex-plugin" / "skills" / "agentpal" / "SKILL.md",
    "codex-plugin-enable-skill": REPO_ROOT / "plugins" / "codex" / "agentpal-codex-plugin" / "skills" / "agentpal-enable" / "SKILL.md",
    "palsmith-team-plan-template": REPO_ROOT / "official" / "pals" / "PalSmith-pal-governor" / "templates" / "pal-team-plan.md",
    "palsmith-create-team-task-package": REPO_ROOT / "official" / "pals" / "PalSmith-pal-governor" / "templates" / "task-packages" / "create-ai-team-from-goal.md",
}

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
    "forbid",
    "negative",
    "bad pattern",
    "role-title-only",
    "agent-style",
    "such as",
    "including",
    "example",
    "violated",
    "violation",
    "禁止",
    "不要",
    "不能",
    "不得",
    "负例",
)

STRUCTURAL_BOUNDARY_CHECKS = {
    "roster_members_only_existing": (
        "roster.members may reference only existing registered pals",
        "roster.members` may reference only",
        "roster_members_rule: `existing pal ids only`",
        "existing pal ids from current contacts",
        "existing registered pals or user-confirmed pals",
        "registered pals or user-confirmed pals",
    ),
    "missing_roles_go_to_open_roles": (
        "missing durable roles",
        "missing seats must be represented in `open_roles`",
        "missing capabilities",
        "open_roles",
    ),
    "optional_new_pal_proposals_not_roster": (
        "new_pal_proposals` are proposal-only, separate from `roster.members`",
        "optional_new_pal_proposals` are proposal-only",
        "proposal-only, not roster",
        "optional_new_pal_proposal_rule",
        "not roster members",
        "proposals are not installed",
    ),
    "no_install_without_confirmation": (
        "requires explicit user confirmation",
        "require explicit user confirmation",
        "before any pal is created or inserted into",
        "before creation or roster insertion",
        "user explicitly confirms",
        "explicit confirmation before writes",
    ),
}

VALIDATION_BOUNDARY_FILES = {
    "acceptance-matrix": (
        REPO_ROOT / "release" / "integration-notes" / "v0.6-acceptance-matrix.md",
        ("fixture_not_live_customer", "workbuddy_not_live_web", "needs_runtime_validation_present"),
    ),
    "after-sales-session-scenario": (
        REPO_ROOT / "evals" / "session-validation" / "v0.6-mira-palsmith" / "scenarios" / "04-existing-after-sales-team-handle-feedback.md",
        ("fixture_not_live_customer",),
    ),
    "workbuddy-session-scenario": (
        REPO_ROOT / "evals" / "session-validation" / "v0.6-mira-palsmith" / "scenarios" / "05-research-team-workbuddy-expert-group.md",
        ("workbuddy_not_live_web",),
    ),
    "after-sales-runtime-fixture": (
        REPO_ROOT / "evals" / "runtime-validation" / "v0.6-team-pack" / "scenario-04-existing-after-sales-team-feedback.md",
        ("fixture_not_live_customer",),
    ),
    "workbuddy-runtime-fixture": (
        REPO_ROOT / "evals" / "runtime-validation" / "v0.6-team-pack" / "scenario-05-research-team-workbuddy-fixture.md",
        ("workbuddy_not_live_web",),
    ),
}

VALIDATION_BOUNDARY_CHECKS = {
    "fixture_not_live_customer": (
        "not live customer",
        "not real customer",
        "live customer-data validation remains",
        "real customer-data",
    ),
    "workbuddy_not_live_web": (
        "not a live web",
        "not live web",
        "not live external",
        "not live web evidence",
        "live external source validation remains",
    ),
    "needs_runtime_validation_present": (
        "needs-runtime-validation",
    ),
}


def read_text(path: Path) -> str:
    if not path.exists():
        return ""
    return path.read_text(encoding="utf-8")


def write_text(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="\n") as handle:
        handle.write(text)


def read_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def count_block(text: str, begin: str, end: str) -> int:
    begin_count = len(re.findall(rf"(?m)^\s*{re.escape(begin)}\s*$", text))
    end_count = len(re.findall(rf"(?m)^\s*{re.escape(end)}\s*$", text))
    return min(begin_count, end_count)


def missing_runtime_entry_anchors(text: str) -> list[str]:
    normalized = re.sub(r"\s+", " ", text.lower())
    missing = []
    for anchor_id, phrases in RUNTIME_ENTRY_ANCHORS.items():
        if not any(phrase in normalized for phrase in phrases):
            missing.append(anchor_id)
    return missing


def line_has_allowed_negative_context(lines: list[str], index: int) -> bool:
    start = max(0, index - 2)
    end = min(len(lines), index + 3)
    window = " ".join(lines[start:end]).lower()
    return any(marker in window for marker in NEGATIVE_CONTEXT_MARKERS)


def forbidden_role_name_violations(text: str) -> list[str]:
    lines = text.splitlines()
    violations = []
    for index, line in enumerate(lines):
        for pattern in FORBIDDEN_ROLE_NAME_PATTERNS:
            if pattern in line and not line_has_allowed_negative_context(lines, index):
                violations.append(f"line {index + 1}: {pattern}")
    return violations


def missing_structural_boundaries(text: str) -> list[str]:
    normalized = re.sub(r"\s+", " ", text.lower())
    missing = []
    for boundary_id, phrases in STRUCTURAL_BOUNDARY_CHECKS.items():
        if not any(phrase in normalized for phrase in phrases):
            missing.append(boundary_id)
    return missing


def missing_validation_boundaries(text: str, required_checks: tuple[str, ...]) -> list[str]:
    normalized = re.sub(r"\s+", " ", text.lower())
    missing = []
    for boundary_id in required_checks:
        phrases = VALIDATION_BOUNDARY_CHECKS[boundary_id]
        if not any(phrase in normalized for phrase in phrases):
            missing.append(boundary_id)
    return missing


def run_helper(helper: Path, action: str, project_root: Path, include_source: bool = False) -> dict:
    command = [
        sys.executable,
        str(helper),
        action,
        "--project-root",
        str(project_root),
        "--json",
    ]
    if include_source:
        command.extend(["--agentpal-source", str(REPO_ROOT)])

    completed = subprocess.run(command, cwd=REPO_ROOT, text=True, capture_output=True, check=False)
    if completed.returncode != 0:
        raise AssertionError(
            "helper failed\n"
            f"command: {' '.join(command)}\n"
            f"stdout: {completed.stdout}\n"
            f"stderr: {completed.stderr}"
        )
    return json.loads(completed.stdout)


def run_codex(action: str, project_root: Path) -> dict:
    return run_helper(CODEX_HELPER, action, project_root, include_source=action in {"enable", "repair"})


def run_claude(action: str, project_root: Path) -> dict:
    return run_helper(CLAUDE_HELPER, action, project_root, include_source=action in {"enable", "repair"})


class PluginEnableDisableSmokeTests(unittest.TestCase):
    maxDiff = None

    def setUp(self) -> None:
        self.tmp = tempfile.TemporaryDirectory(prefix="agentpal-plugin-smoke-")
        self.root = Path(self.tmp.name)

    def tearDown(self) -> None:
        self.tmp.cleanup()

    def project(self, name: str) -> Path:
        path = self.root / name
        path.mkdir(parents=True, exist_ok=True)
        return path

    def test_codex_empty_project_enable_status_disable(self) -> None:
        project = self.project("codex-empty")

        enable_result = run_codex("enable", project)
        self.assertEqual(enable_result["status"], "enabled")
        self.assertEqual(run_codex("status", project)["status"], "enabled_complete")
        self.assertEqual(count_block(read_text(project / "AGENTS.md"), CODEX_BEGIN, CODEX_END), 1)
        self.assertTrue((project / ".agentpal" / "project.json").is_file())
        self.assertTrue((project / ".agentpal" / "AGENTPAL.md").is_file())

        data = read_json(project / ".agentpal" / "project.json")
        self.assertEqual(data["binding_type"], "thin")
        self.assertEqual(data["default_pal"], "Mira")
        self.assertEqual(data["runtime"], "codex")
        self.assertEqual(data["schema_version"], "agentpal.project_binding.v1")
        self.assertIsInstance(data["agentpal_source"], dict)
        self.assertIn("codex", data["enabled_runtimes"])

        disable_result = run_codex("disable", project)
        self.assertEqual(disable_result["status"], "disabled")
        self.assertFalse((project / ".agentpal").exists())
        self.assertEqual(count_block(read_text(project / "AGENTS.md"), CODEX_BEGIN, CODEX_END), 0)

    def test_claude_empty_project_enable_status_disable(self) -> None:
        project = self.project("claude-empty")

        enable_result = run_claude("enable", project)
        self.assertEqual(enable_result["status_after"], "complete")
        self.assertEqual(run_claude("status", project)["status"], "complete")
        self.assertEqual(count_block(read_text(project / "CLAUDE.md"), CLAUDE_BEGIN, CLAUDE_END), 1)
        self.assertFalse((project / "AGENTS.md").exists())
        self.assertFalse((project / ".claude" / "settings.local.json").exists())

        data = read_json(project / ".agentpal" / "project.json")
        self.assertEqual(data["binding_type"], "thin")
        self.assertEqual(data["default_pal"], "Mira")
        self.assertEqual(data["runtime"], "claude-code")
        self.assertEqual(data["schema_version"], "agentpal.project_binding.v1")
        self.assertIsInstance(data["agentpal_source"], dict)
        self.assertEqual(data["agentpal_source"]["type"], "user_configured_source")
        self.assertIn("claude-code", data["enabled_runtimes"])

        disable_result = run_claude("disable", project)
        self.assertEqual(disable_result["status_after"], "unbound")
        self.assertFalse((project / ".agentpal").exists())
        self.assertEqual(count_block(read_text(project / "CLAUDE.md"), CLAUDE_BEGIN, CLAUDE_END), 0)

    def test_existing_instruction_files_are_preserved_and_idempotent(self) -> None:
        codex_project = self.project("codex-existing-agents")
        write_text(codex_project / "AGENTS.md", "# User rules\nKeep this line.\n")

        run_codex("enable", codex_project)
        run_codex("enable", codex_project)
        self.assertEqual(count_block(read_text(codex_project / "AGENTS.md"), CODEX_BEGIN, CODEX_END), 1)
        self.assertIn("Keep this line.", read_text(codex_project / "AGENTS.md"))

        claude_project = self.project("claude-existing-claude")
        write_text(claude_project / "CLAUDE.md", "# Project Claude rules\nPreserve me.\n")

        run_claude("enable", claude_project)
        run_claude("enable", claude_project)
        self.assertEqual(count_block(read_text(claude_project / "CLAUDE.md"), CLAUDE_BEGIN, CLAUDE_END), 1)
        self.assertIn("Preserve me.", read_text(claude_project / "CLAUDE.md"))

    def test_repair_restores_missing_project_json_and_missing_blocks(self) -> None:
        codex_project = self.project("codex-repair")
        write_text(codex_project / "AGENTS.md", "# User rules\n")
        run_codex("enable", codex_project)

        (codex_project / ".agentpal" / "project.json").unlink()
        self.assertEqual(run_codex("status", codex_project)["status"], "enabled_missing_project_json")
        self.assertEqual(run_codex("repair", codex_project)["status_after"], "enabled_complete")

        write_text(codex_project / "AGENTS.md", "# User rules\n")
        self.assertEqual(run_codex("status", codex_project)["status"], "enabled_missing_agents_protected_block")
        self.assertEqual(run_codex("repair", codex_project)["status_after"], "enabled_complete")
        self.assertEqual(count_block(read_text(codex_project / "AGENTS.md"), CODEX_BEGIN, CODEX_END), 1)
        self.assertIn("# User rules", read_text(codex_project / "AGENTS.md"))

        claude_project = self.project("claude-repair")
        write_text(claude_project / "CLAUDE.md", "# Claude user rules\n")
        run_claude("enable", claude_project)

        (claude_project / ".agentpal" / "project.json").unlink()
        self.assertEqual(run_claude("status", claude_project)["status"], "partial")
        self.assertEqual(run_claude("repair", claude_project)["status_after"], "complete")

        write_text(claude_project / "CLAUDE.md", "# Claude user rules\n")
        self.assertEqual(run_claude("status", claude_project)["status"], "partial")
        self.assertEqual(run_claude("repair", claude_project)["status_after"], "complete")
        self.assertEqual(count_block(read_text(claude_project / "CLAUDE.md"), CLAUDE_BEGIN, CLAUDE_END), 1)
        self.assertIn("# Claude user rules", read_text(claude_project / "CLAUDE.md"))

    def test_codex_repair_directly_restores_missing_project_json(self) -> None:
        project = self.project("codex-repair-direct")
        run_codex("enable", project)

        project_json_path = project / ".agentpal" / "project.json"
        project_json_path.unlink()

        repair_result = run_codex("repair", project)
        self.assertEqual(repair_result["status_before"], "enabled_missing_project_json")
        self.assertEqual(repair_result["status_after"], "enabled_complete")
        self.assertTrue(project_json_path.is_file())
        changed_paths = {str(Path(item).resolve()).lower() for item in repair_result["changed"]}
        self.assertIn(str(project_json_path.resolve()).lower(), changed_paths)

    def test_disable_removes_only_agentpal_content(self) -> None:
        codex_project = self.project("codex-disable-preserve")
        write_text(codex_project / "AGENTS.md", "# User AGENTS\nDo not delete me.\n")
        run_codex("enable", codex_project)
        run_codex("disable", codex_project)
        self.assertFalse((codex_project / ".agentpal").exists())
        self.assertEqual(count_block(read_text(codex_project / "AGENTS.md"), CODEX_BEGIN, CODEX_END), 0)
        self.assertIn("Do not delete me.", read_text(codex_project / "AGENTS.md"))

        claude_project = self.project("claude-disable-preserve")
        write_text(claude_project / "CLAUDE.md", "# User CLAUDE\nDo not delete me either.\n")
        run_claude("enable", claude_project)
        run_claude("disable", claude_project)
        self.assertFalse((claude_project / ".agentpal").exists())
        self.assertEqual(count_block(read_text(claude_project / "CLAUDE.md"), CLAUDE_BEGIN, CLAUDE_END), 0)
        self.assertIn("Do not delete me either.", read_text(claude_project / "CLAUDE.md"))

    def test_codex_and_claude_bindings_can_coexist_and_disable_one_runtime(self) -> None:
        project = self.project("coexist")
        write_text(project / "AGENTS.md", "# User AGENTS\nCodex user content.\n")
        write_text(project / "CLAUDE.md", "# User CLAUDE\nClaude user content.\n")

        run_codex("enable", project)
        run_claude("enable", project)

        self.assertEqual(count_block(read_text(project / "AGENTS.md"), CODEX_BEGIN, CODEX_END), 1)
        self.assertEqual(count_block(read_text(project / "CLAUDE.md"), CLAUDE_BEGIN, CLAUDE_END), 1)
        data = read_json(project / ".agentpal" / "project.json")
        self.assertIn("codex", data["enabled_runtimes"])
        self.assertIn("claude-code", data["enabled_runtimes"])

        run_codex("disable", project)
        self.assertTrue((project / ".agentpal").exists())
        self.assertEqual(count_block(read_text(project / "AGENTS.md"), CODEX_BEGIN, CODEX_END), 0)
        self.assertEqual(count_block(read_text(project / "CLAUDE.md"), CLAUDE_BEGIN, CLAUDE_END), 1)
        self.assertIn("Codex user content.", read_text(project / "AGENTS.md"))
        self.assertIn("Claude user content.", read_text(project / "CLAUDE.md"))
        data = read_json(project / ".agentpal" / "project.json")
        self.assertNotIn("codex", data["enabled_runtimes"])
        self.assertIn("claude-code", data["enabled_runtimes"])

        disable_result = run_claude("disable", project)
        self.assertEqual(disable_result["codex_block_still_present"], False)
        self.assertFalse((project / ".agentpal").exists())
        self.assertEqual(count_block(read_text(project / "CLAUDE.md"), CLAUDE_BEGIN, CLAUDE_END), 0)
        self.assertIn("Claude user content.", read_text(project / "CLAUDE.md"))

    def test_status_reports_source_unavailable(self) -> None:
        missing_source = str(self.root / "missing-agentpal-source")

        codex_project = self.project("codex-source-unavailable")
        run_codex("enable", codex_project)
        codex_json_path = codex_project / ".agentpal" / "project.json"
        codex_data = read_json(codex_json_path)
        codex_data["agentpal_source"] = "central_path"
        codex_data["agentpal_source_detail"] = {
            "type": "central_path",
            "value": missing_source,
            "workspace_root": missing_source,
        }
        write_text(codex_json_path, json.dumps(codex_data, ensure_ascii=False, indent=2) + "\n")
        self.assertEqual(run_codex("status", codex_project)["status"], "enabled_source_unknown_or_unavailable")

        claude_project = self.project("claude-source-unavailable")
        run_claude("enable", claude_project)
        claude_json_path = claude_project / ".agentpal" / "project.json"
        claude_data = read_json(claude_json_path)
        claude_data["agentpal_source"] = "central_path"
        claude_data["agentpal_source_detail"] = {
            "type": "central_path",
            "value": missing_source,
            "workspace_root": missing_source,
        }
        write_text(claude_json_path, json.dumps(claude_data, ensure_ascii=False, indent=2) + "\n")
        claude_status = run_claude("status", claude_project)
        self.assertEqual(claude_status["status"], "partial")
        self.assertIn("source_unavailable", claude_status["issues"])

    def test_runtime_entry_anchor_coverage(self) -> None:
        failures = {}

        for label, path in RUNTIME_ENTRY_FILES.items():
            self.assertTrue(path.is_file(), f"missing runtime entry file: {label}: {path}")
            missing = missing_runtime_entry_anchors(read_text(path))
            if missing:
                failures[label] = missing

        codex_project = self.project("codex-anchor-generated")
        run_codex("enable", codex_project)
        for label, path in {
            "codex-generated-agents": codex_project / "AGENTS.md",
            "codex-generated-agentpal": codex_project / ".agentpal" / "AGENTPAL.md",
        }.items():
            missing = missing_runtime_entry_anchors(read_text(path))
            if missing:
                failures[label] = missing

        claude_project = self.project("claude-anchor-generated")
        run_claude("enable", claude_project)
        for label, path in {
            "claude-generated-claude": claude_project / "CLAUDE.md",
            "claude-generated-agentpal": claude_project / ".agentpal" / "AGENTPAL.md",
        }.items():
            missing = missing_runtime_entry_anchors(read_text(path))
            if missing:
                failures[label] = missing

        if failures:
            self.fail("runtime entry anchor drift detected: " + json.dumps(failures, ensure_ascii=False, indent=2))

    def test_runtime_entry_forbidden_behavior_boundaries(self) -> None:
        failures = {}

        entries_to_check = dict(RUNTIME_ENTRY_FILES)

        codex_project = self.project("codex-forbidden-boundary-generated")
        run_codex("enable", codex_project)
        entries_to_check.update(
            {
                "codex-generated-agents": codex_project / "AGENTS.md",
                "codex-generated-agentpal": codex_project / ".agentpal" / "AGENTPAL.md",
            }
        )

        claude_project = self.project("claude-forbidden-boundary-generated")
        run_claude("enable", claude_project)
        entries_to_check.update(
            {
                "claude-generated-claude": claude_project / "CLAUDE.md",
                "claude-generated-agentpal": claude_project / ".agentpal" / "AGENTPAL.md",
            }
        )

        for label, path in entries_to_check.items():
            text = read_text(path)
            file_failures = {}

            forbidden_names = forbidden_role_name_violations(text)
            if forbidden_names:
                file_failures["forbidden_role_name_output"] = forbidden_names

            structural = missing_structural_boundaries(text)
            if structural:
                file_failures["missing_structural_boundaries"] = structural

            if file_failures:
                failures[label] = file_failures

        if failures:
            self.fail("runtime forbidden behavior boundary regression: " + json.dumps(failures, ensure_ascii=False, indent=2))

    def test_fixture_live_validation_boundaries(self) -> None:
        failures = {}

        for label, (path, required_checks) in VALIDATION_BOUNDARY_FILES.items():
            self.assertTrue(path.is_file(), f"missing validation boundary file: {label}: {path}")
            missing = missing_validation_boundaries(read_text(path), required_checks)
            if missing:
                failures[label] = missing

        if failures:
            self.fail("fixture/live validation boundary regression: " + json.dumps(failures, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    unittest.main(verbosity=2)
