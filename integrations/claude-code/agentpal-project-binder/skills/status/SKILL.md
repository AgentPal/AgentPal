---
description: Inspect the current Claude Code project's AgentPal thin binding state. Use when the user asks whether AgentPal is enabled, healthy, complete, missing, or broken in this project.
when_to_use: Trigger on requests like “AgentPal 状态”, “检查当前项目的 AgentPal”, “is AgentPal enabled here”, or “show AgentPal binding status”.
---

# AgentPal Status

Use [../../references/binding-rules.md](../../references/binding-rules.md) and [../../references/status-model.md](../../references/status-model.md).

## Goal

Classify the current project's AgentPal thin binding without editing files.

## Checks

Inspect only:

- `.agentpal/project.json`
- `.agentpal/AGENTPAL.md`
- root `CLAUDE.md`

## Required Validation

### `project.json`

Check whether:

- the file exists
- it parses as JSON
- it includes:
  - `schema_version`
  - `binding_version`
  - `project_name`
  - `project_root_hint`
  - `binding_type`
  - `default_pal`
  - `runtime`
  - `agentpal_source`
  - `enabled_at`
  - `updated_at`
  - `status`
  - `last_runtime`
  - `enabled_runtimes`
- `binding_type` is `thin`
- `default_pal` is `Mira`
- `runtime` is `claude-code`

### `AGENTPAL.md`

Check whether:

- the file exists
- it still describes a thin Claude Code binding
- it contains the current v0.6 runtime anchors listed below

### `CLAUDE.md`

Check whether:

- exactly one runtime-qualified block exists between `<!-- BEGIN AGENTPAL BINDING: claude-code -->` and `<!-- END AGENTPAL BINDING: claude-code -->`
- or only a legacy `<!-- AGENTPAL:BEGIN -->` or workgroup block exists
- or multiple blocks exist
- when the runtime-qualified block exists, it contains the current v0.6 runtime anchors listed below

### Current v0.6 Runtime Anchors

Report `partial` and recommend `/agentpal:repair` if the current `CLAUDE.md`
protected block or `.agentpal/AGENTPAL.md` is missing any of:

- `Workflow Execution Contract`
- `Closure Gate`
- `Owner Assignment Integrity`
- `Team label is not participant`
- `open role`
- `Pal naming`
- `Faye`
- `no fake verifier`
- `simulated-as-real`

## Status Output

Return one of:

- `unbound`
- `complete`
- `partial`
- `damaged`
- `legacy-block`

Then list:

- missing items
- malformed items
- next recommended command: `/agentpal:enable`, `/agentpal:repair`, or `/agentpal:disable`

When local shell execution is available, `status` should call `python scripts/agentpal_binding.py status --project-root <current-project-root>`.

Do not repair automatically in this skill.
