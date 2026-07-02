---
description: Disable AgentPal for the current Claude Code project. Use when the user asks to uninstall, remove, disconnect, or clean the current project's thin AgentPal binding.
when_to_use: Trigger on requests like “卸载 AgentPal”, “remove AgentPal from this project”, “disable AgentPal here”, or “clean the AgentPal binding”.
---

# AgentPal Disable

Use [../../references/binding-rules.md](../../references/binding-rules.md).

## Goal

Remove the current Claude Code project's AgentPal thin binding without touching unrelated project content or the central AgentPal workspace.

## Removal Scope

Only do these actions:

1. Delete `.agentpal/` only when no other runtime binding remains
2. Remove the protected AgentPal block from root `CLAUDE.md`

Do not:

- delete the central AgentPal workspace
- delete other projects' bindings
- delete any other user content in `CLAUDE.md`
- delete `.claude/settings.local.json`
- delete `AGENTS.md`

## Marker Rules

Remove the new marker block when present:

```html
<!-- BEGIN AGENTPAL BINDING: claude-code -->
<!-- END AGENTPAL BINDING: claude-code -->
```

If no new block exists but a legacy `<!-- AGENTPAL:BEGIN -->` or workgroup block exists, remove only that legacy block.

If `.agentpal/project.json` shows that Codex is still enabled, preserve `.agentpal/`, remove only `claude-code` from `enabled_runtimes`, and leave `AGENTS.md` untouched.

If `CLAUDE.md` has other content, preserve it exactly.

If `CLAUDE.md` becomes empty after block removal, leave the empty file in place rather than deleting additional files.

When local shell execution is available, call `python scripts/agentpal_binding.py disable --project-root <current-project-root>` from the plugin root or execute the exact same file protocol.

## Final Report

Report:

- whether `.agentpal/` was removed
- whether the Claude block was removed
- whether a legacy block was removed instead
- any remaining AgentPal-related content that was intentionally left untouched
