#!/usr/bin/env python3
"""Claude Code binder helper smoke tests."""

from __future__ import annotations

import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[2]
CLAUDE_HELPER = REPO_ROOT / "integrations" / "claude-code" / "agentpal-project-binder" / "scripts" / "agentpal_binding.py"
CODEX_HELPER = REPO_ROOT / "plugins" / "codex" / "agentpal-codex-plugin" / "scripts" / "agentpal_binding.py"
CLAUDE_BEGIN = "<!-- BEGIN AGENTPAL BINDING: claude-code -->"
CLAUDE_END = "<!-- END AGENTPAL BINDING: claude-code -->"
RUNTIME_ANCHORS = [
    "Workflow Execution Contract",
    "Closure Gate",
    "open role",
    "Pal naming",
    "Faye",
    "no fake verifier",
    "simulated-as-real",
]


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


def count_claude_block(text: str) -> int:
    return int(CLAUDE_BEGIN in text and CLAUDE_END in text)


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


def run_claude(action: str, project_root: Path) -> dict:
    return run_helper(CLAUDE_HELPER, action, project_root, include_source=action in {"enable", "repair"})


def run_codex(action: str, project_root: Path) -> dict:
    return run_helper(CODEX_HELPER, action, project_root, include_source=action in {"enable", "repair"})


class ClaudeCodeBinderSmokeTests(unittest.TestCase):
    def setUp(self) -> None:
        self.tmp = tempfile.TemporaryDirectory(prefix="agentpal-claude-smoke-")
        self.root = Path(self.tmp.name)

    def tearDown(self) -> None:
        self.tmp.cleanup()

    def project(self, name: str) -> Path:
        path = self.root / name
        path.mkdir(parents=True, exist_ok=True)
        return path

    def test_empty_project_enable(self) -> None:
        project = self.project("empty-enable")
        result = run_claude("enable", project)
        self.assertEqual(result["status_after"], "complete")
        self.assertTrue((project / ".agentpal" / "project.json").is_file())
        self.assertTrue((project / ".agentpal" / "AGENTPAL.md").is_file())
        self.assertEqual(count_claude_block(read_text(project / "CLAUDE.md")), 1)

    def test_existing_claude_md_enable(self) -> None:
        project = self.project("existing-claude")
        write_text(project / "CLAUDE.md", "# Existing\nPreserve me.\n")
        run_claude("enable", project)
        text = read_text(project / "CLAUDE.md")
        self.assertIn("Preserve me.", text)
        self.assertEqual(count_claude_block(text), 1)

    def test_repeated_enable_is_idempotent(self) -> None:
        project = self.project("repeat-enable")
        run_claude("enable", project)
        run_claude("enable", project)
        self.assertEqual(count_claude_block(read_text(project / "CLAUDE.md")), 1)

    def test_status_reports_complete(self) -> None:
        project = self.project("status")
        run_claude("enable", project)
        result = run_claude("status", project)
        self.assertEqual(result["status"], "complete")
        self.assertEqual(result["recommended_command"], "/agentpal:disable")

    def test_repair_after_project_json_deleted(self) -> None:
        project = self.project("repair")
        run_claude("enable", project)
        (project / ".agentpal" / "project.json").unlink()
        self.assertEqual(run_claude("status", project)["status"], "partial")
        self.assertEqual(run_claude("repair", project)["status_after"], "complete")

    def test_status_flags_stale_template_and_repair_refreshes_it(self) -> None:
        project = self.project("repair-stale-template")
        run_claude("enable", project)
        write_text(
            project / "CLAUDE.md",
            "# Existing Claude Notes\nPreserve me.\n\n"
            f"{CLAUDE_BEGIN}\n"
            "This is an old AgentPal Claude Code block without the v0.6 anchors.\n"
            f"{CLAUDE_END}\n",
        )
        write_text(
            project / ".agentpal" / "AGENTPAL.md",
            "# Old AgentPal Binding\nThis old file does not include the current runtime anchors.\n",
        )

        stale_status = run_claude("status", project)
        self.assertEqual(stale_status["status"], "partial")
        self.assertTrue(
            any(issue.startswith("missing_runtime_template_anchors:") for issue in stale_status["issues"])
        )

        repair_result = run_claude("repair", project)
        self.assertEqual(repair_result["status_after"], "complete")
        final_status = run_claude("status", project)
        self.assertEqual(final_status["status"], "complete")
        self.assertFalse(any(final_status["runtime_template_anchor_checks"]["missing"].values()))

        claude_text = read_text(project / "CLAUDE.md")
        agentpal_text = read_text(project / ".agentpal" / "AGENTPAL.md")
        self.assertIn("Preserve me.", claude_text)
        for anchor in RUNTIME_ANCHORS:
            self.assertIn(anchor, claude_text)
            self.assertIn(anchor, agentpal_text)

    def test_disable(self) -> None:
        project = self.project("disable")
        run_claude("enable", project)
        result = run_claude("disable", project)
        self.assertEqual(result["status_after"], "unbound")
        self.assertFalse((project / ".agentpal").exists())
        self.assertEqual(count_claude_block(read_text(project / "CLAUDE.md")), 0)

    def test_disable_claude_with_codex_coexistence(self) -> None:
        project = self.project("coexist-disable")
        write_text(project / "AGENTS.md", "# User AGENTS\n")
        write_text(project / "CLAUDE.md", "# User CLAUDE\n")
        run_codex("enable", project)
        run_claude("enable", project)

        result = run_claude("disable", project)
        self.assertTrue((project / ".agentpal").exists())
        self.assertEqual(result["status_after"], "unbound")
        self.assertEqual(count_claude_block(read_text(project / "CLAUDE.md")), 0)
        data = read_json(project / ".agentpal" / "project.json")
        self.assertIn("codex", data["enabled_runtimes"])
        self.assertNotIn("claude-code", data["enabled_runtimes"])


if __name__ == "__main__":
    unittest.main(verbosity=2)
