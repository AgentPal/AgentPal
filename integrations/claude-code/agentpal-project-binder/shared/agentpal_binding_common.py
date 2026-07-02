from __future__ import annotations

import json
import os
import re
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


CODEX_BEGIN_MARKER = "<!-- BEGIN AGENTPAL BINDING: codex -->"
CODEX_END_MARKER = "<!-- END AGENTPAL BINDING: codex -->"
# Legacy markers are retained only so repair/disable can recognize and migrate
# old project bindings. New writes must use runtime-qualified markers above.
SIMPLE_BEGIN_MARKER = "<!-- AGENTPAL:BEGIN -->"
SIMPLE_END_MARKER = "<!-- AGENTPAL:END -->"
LEGACY_BEGIN_MARKER = "<!-- BEGIN AGENTPAL WORKGROUP -->"
LEGACY_END_MARKER = "<!-- END AGENTPAL WORKGROUP -->"
GITHUB_SOURCE_URL = "https://github.com/AgentPal/AgentPal"


FORBIDDEN_THICK_BINDING_DIRS = [
    ".agentpal/memory",
    ".agentpal/state",
    ".agentpal/reports",
    ".agentpal/context",
    ".agentpal/index",
    ".agentpal/pals",
    ".agentpal/workflows",
    ".agentpal/evals",
    ".agentpal/capability-inventory",
    ".agentpal/business-systems",
    ".agentpal/reviews",
    ".agentpal/evidence",
    ".agentpal/replay",
    ".agentpal/rollback",
    ".agentpal/verification",
    ".agentpal/audit-trail",
    ".agentpal/governance-decisions",
    ".agentpal/change-ledger",
    ".agentpal/change-review",
]


CORE_GATE_PATHS = [
    "core/agentpal-core-gate.md",
    "core/first-pal-gate.md",
    "core/simple-pal-mode-runtime-contract.md",
    "core/deliverable-aware-task-judgement-gate.md",
    "core/main-pal-conductor-gate.md",
    "core/runtime-adapter-shared-contract.md",
    "core/project-binding-thin-contract.md",
    "core/runtime-response-gate.md",
]


@dataclass(frozen=True)
class RuntimeBindingConfig:
    runtime: str
    host_file: str
    primary_begin: str
    primary_end: str
    compatible_pairs: tuple[tuple[str, str], ...]

    @property
    def primary_pair(self) -> tuple[str, str]:
        return (self.primary_begin, self.primary_end)


RUNTIME_BINDINGS = {
    "codex": RuntimeBindingConfig(
        runtime="codex",
        host_file="AGENTS.md",
        primary_begin=CODEX_BEGIN_MARKER,
        primary_end=CODEX_END_MARKER,
        compatible_pairs=(
            (CODEX_BEGIN_MARKER, CODEX_END_MARKER),
            (SIMPLE_BEGIN_MARKER, SIMPLE_END_MARKER),
            (LEGACY_BEGIN_MARKER, LEGACY_END_MARKER),
        ),
    ),
    "claude-code": RuntimeBindingConfig(
        runtime="claude-code",
        host_file="CLAUDE.md",
        primary_begin="<!-- BEGIN AGENTPAL BINDING: claude-code -->",
        primary_end="<!-- END AGENTPAL BINDING: claude-code -->",
        compatible_pairs=(
            ("<!-- BEGIN AGENTPAL BINDING: claude-code -->", "<!-- END AGENTPAL BINDING: claude-code -->"),
            (SIMPLE_BEGIN_MARKER, SIMPLE_END_MARKER),
            (LEGACY_BEGIN_MARKER, LEGACY_END_MARKER),
        ),
    ),
}


def utc_now() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")


def resolve_project_root(value: str | None) -> Path:
    root = Path(value or os.getcwd()).expanduser().resolve()
    if not root.exists():
        raise SystemExit(f"Project root does not exist: {root}")
    if not root.is_dir():
        raise SystemExit(f"Project root is not a directory: {root}")
    return root


def is_agentpal_source(path: Path) -> bool:
    return (path / "agentpal.json").is_file() and (path / "official" / "pals" / "Mira-main").is_dir()


def find_source_from_ancestors(start: Path) -> Path | None:
    for candidate in [start, *start.parents]:
        if is_agentpal_source(candidate):
            return candidate
    return None


def resolve_agentpal_source(explicit: str | None, project_root: Path) -> dict[str, Any]:
    candidates: list[tuple[str, str]] = []
    if explicit:
        candidates.append(("user_configured_source", explicit))
    for env_name in ("AGENTPAL_SOURCE", "AGENTPAL_HOME"):
        env_value = os.environ.get(env_name)
        if env_value:
            candidates.append(("user_configured_source", env_value))

    for source_type, raw_value in candidates:
        if raw_value.startswith("http://") or raw_value.startswith("https://"):
            return {
                "type": "github_source" if "github.com" in raw_value else source_type,
                "value": raw_value,
                "workspace_root": "",
                "available": None,
            }

        source_path = Path(raw_value).expanduser().resolve()
        return {
            "type": source_type,
            "value": str(source_path),
            "workspace_root": str(source_path),
            "available": is_agentpal_source(source_path),
        }

    for start in (Path(__file__).resolve(), project_root):
        found = find_source_from_ancestors(start)
        if found:
            return {
                "type": "central_path",
                "value": str(found),
                "workspace_root": str(found),
                "available": True,
            }

    return {
        "type": "github_source",
        "value": GITHUB_SOURCE_URL,
        "workspace_root": "",
        "available": None,
    }


def read_text(path: Path) -> str:
    if not path.exists():
        return ""
    return path.read_text(encoding="utf-8")


def write_text(path: Path, value: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="\n") as handle:
        handle.write(value)


def load_json_dict(path: Path) -> dict[str, Any]:
    if not path.is_file():
        return {}
    try:
        loaded = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError:
        return {}
    return loaded if isinstance(loaded, dict) else {}


def write_json_dict(path: Path, data: dict[str, Any]) -> None:
    write_text(path, json.dumps(data, ensure_ascii=False, indent=2) + "\n")


def replace_template_values(value: Any, replacements: dict[str, str]) -> Any:
    if isinstance(value, str):
        return replacements.get(value, value)
    if isinstance(value, list):
        return [replace_template_values(item, replacements) for item in value]
    if isinstance(value, dict):
        return {key: replace_template_values(item, replacements) for key, item in value.items()}
    return value


def count_marked_blocks(text: str, begin: str, end: str) -> int:
    begin_count = len(re.findall(rf"(?m)^\s*{re.escape(begin)}\s*$", text))
    end_count = len(re.findall(rf"(?m)^\s*{re.escape(end)}\s*$", text))
    return min(begin_count, end_count)


def remove_marked_blocks(text: str, begin: str, end: str) -> tuple[str, int]:
    pattern = re.compile(
        rf"\n?^\s*{re.escape(begin)}\s*$[\s\S]*?^\s*{re.escape(end)}\s*$\n?",
        re.MULTILINE,
    )
    next_text, count = pattern.subn("\n", text)
    next_text = re.sub(r"\n{3,}", "\n\n", next_text).strip()
    if next_text:
        next_text += "\n"
    return next_text, count


def remove_all_compatible_blocks(text: str, pairs: tuple[tuple[str, str], ...]) -> tuple[str, int]:
    total_removed = 0
    next_text = text
    for begin, end in pairs:
        next_text, removed = remove_marked_blocks(next_text, begin, end)
        total_removed += removed
    return next_text, total_removed


def upsert_runtime_block(path: Path, block_text: str, config: RuntimeBindingConfig) -> tuple[bool, str]:
    existing = read_text(path)
    next_text, removed = remove_all_compatible_blocks(existing, config.compatible_pairs)
    stripped = next_text.rstrip()
    block = block_text.strip()
    if stripped:
        candidate = f"{stripped}\n\n{block}\n"
    else:
        candidate = f"{block}\n"
    if existing == candidate:
        return False, "unchanged"
    write_text(path, candidate)
    if removed == 0 and existing:
        return True, "inserted"
    if removed == 0 and not existing:
        return True, "created"
    return True, "replaced"


def runtime_block_counts(project_root: Path, runtime: str) -> dict[str, int]:
    config = RUNTIME_BINDINGS[runtime]
    host_path = project_root / config.host_file
    text = read_text(host_path)
    counts: dict[str, int] = {}
    total = 0
    for begin, end in config.compatible_pairs:
        count = count_marked_blocks(text, begin, end)
        counts[f"{begin}|{end}"] = count
        total += count
        if (begin, end) == config.primary_pair:
            counts["primary"] = count
    counts["total"] = total
    return counts


def any_runtime_block_present(project_root: Path, exclude_runtime: str | None = None) -> bool:
    for runtime, config in RUNTIME_BINDINGS.items():
        if runtime == exclude_runtime:
            continue
        counts = runtime_block_counts(project_root, runtime)
        if counts["total"] > 0:
            return True
        host_path = project_root / config.host_file
        if host_path.exists():
            text = read_text(host_path)
            if any(begin in text or end in text for begin, end in config.compatible_pairs):
                return True
    return False


def merge_enabled_runtimes(existing: Any, runtime: str) -> list[str]:
    merged: list[str] = []
    if isinstance(existing, list):
        for item in existing:
            if isinstance(item, str) and item not in merged:
                merged.append(item)
    if runtime not in merged:
        merged.append(runtime)
    return merged


def remaining_runtimes_after_disable(project_data: dict[str, Any], runtime: str) -> list[str]:
    existing = project_data.get("enabled_runtimes")
    runtimes = [item for item in existing if isinstance(item, str)] if isinstance(existing, list) else []
    return [item for item in runtimes if item != runtime]


def update_project_json_after_runtime_disable(project_json_path: Path, runtime: str) -> bool:
    data = load_json_dict(project_json_path)
    if not data:
        return False
    remaining = remaining_runtimes_after_disable(data, runtime)
    changed = False
    if data.get("enabled_runtimes") != remaining:
        data["enabled_runtimes"] = remaining
        changed = True
    if remaining:
        last_runtime = remaining[-1]
        if data.get("last_runtime") != last_runtime:
            data["last_runtime"] = last_runtime
            changed = True
        if data.get("runtime") != last_runtime:
            data["runtime"] = last_runtime
            changed = True
        if data.get("status") != "enabled":
            data["status"] = "enabled"
            changed = True
    else:
        if data.get("status") != "disabled":
            data["status"] = "disabled"
            changed = True
    if changed:
        data["updated_at"] = utc_now()
        write_json_dict(project_json_path, data)
    return changed
