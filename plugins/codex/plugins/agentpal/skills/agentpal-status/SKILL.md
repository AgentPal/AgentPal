---
name: agentpal-status
description: Check whether the current Codex project has AgentPal enabled, disabled, incomplete, missing project.json, missing AGENTS block, or unavailable source.
---

# AgentPal Status

Use this Skill to inspect the current project's AgentPal thin binding without
modifying files.

## Procedure

1. Treat the current working directory as the target project root unless the user gives a different project path.
2. Inspect only `.agentpal/project.json`, `.agentpal/AGENTPAL.md`, and
   `AGENTS.md`.
3. If `.agentpal/project.json` points at an install-config workspace root,
   verify whether that directory still exists.
4. Count complete Codex protected blocks in `AGENTS.md`.
5. Report the binding status and issues.
6. If status reports an incomplete binding, explain that the user can say
   `Repair AgentPal` to restore missing thin-binding files.

## Status Categories

- `not_enabled`
- `enabled_complete`
- `enabled_missing_project_json`
- `enabled_missing_agents_protected_block`
- `enabled_source_unknown_or_unavailable`
- `enabled_incomplete`

## Boundary

Status check is read-only. Do not repair, remove, or create files unless the
user asks for repair, enable, or disable.
