---
description: Repair the current Claude Code project's AgentPal thin binding when files or the protected CLAUDE.md block are missing, malformed, or still on legacy markers.
when_to_use: Trigger on requests like “修复 AgentPal”, “repair AgentPal binding”, “fix the AgentPal block”, or “recover the current project's AgentPal setup”.
---

# AgentPal Repair

Use [../../references/binding-rules.md](../../references/binding-rules.md), [../../references/status-model.md](../../references/status-model.md), [../../templates/.agentpal/project.json](../../templates/.agentpal/project.json), [../../templates/.agentpal/AGENTPAL.md](../../templates/.agentpal/AGENTPAL.md), and [../../templates/CLAUDE.agentpal-block.md](../../templates/CLAUDE.agentpal-block.md).

## Goal

Repair an existing AgentPal thin binding for the current Claude Code project.

## Repair Scope

Only repair:

- `.agentpal/project.json`
- `.agentpal/AGENTPAL.md`
- the protected AgentPal block in root `CLAUDE.md`

Do not create `AGENTS.md`, `.claude/settings.local.json`, or any extra `.agentpal/` folders.

## Process

1. When local shell execution is available, call `python scripts/agentpal_binding.py repair --project-root <current-project-root>` from the plugin root before reading or manually editing possibly stale binding files.
2. If local shell execution is not available, run the same checks as `/agentpal:status`.
3. If the project is `unbound`, do not silently enable it. Tell the user there is nothing to repair and recommend `/agentpal:enable`.
4. If `project.json` is missing, recreate it from the latest template.
5. If `project.json` exists but is invalid, recover any clearly readable source values when possible, then rewrite a valid v1 file.
6. Always rewrite `.agentpal/AGENTPAL.md` from the latest template when repairing an existing binding.
7. Always replace the root `CLAUDE.md` AgentPal protected block with the latest `templates/CLAUDE.agentpal-block.md` content when repairing an existing binding, even if a block already exists.
8. If root `CLAUDE.md` lacks the runtime-qualified Claude Code block, insert it once.
9. If only the legacy `<!-- AGENTPAL:BEGIN -->` or workgroup block exists, replace it with the new runtime-qualified marker block.
10. If multiple AgentPal blocks exist, keep one correct new block and remove duplicates while preserving all non-AgentPal content.
11. After repair, run status again or perform the same status checks.

## Required Runtime Anchor Check

After repair, the `CLAUDE.md` protected block and `.agentpal/AGENTPAL.md` must include these current v0.6 anchors:

- `Workflow Execution Contract`
- `Closure Gate`
- `open role`
- `Pal naming`
- `Faye`
- `no fake verifier`
- `simulated-as-real`

If any anchor is missing, do not report the binding as complete. Run the helper repair again if possible, or report `partial` and list the missing anchors.

## Data Preservation

Preserve if recoverable:

- existing `project_name`
- existing path or URL source values
- original `created_at`

Always update:

- `updated_at`
- `last_runtime`
- `enabled_runtimes`
- `status`

## Final Report

Report:

- starting status
- repaired items
- unrecoverable items
- final status
