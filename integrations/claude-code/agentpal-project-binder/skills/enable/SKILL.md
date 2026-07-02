---
description: Enable AgentPal thin binding for the current Claude Code project. Use when the user says enable, init, connect, or install AgentPal for this project. Create or repair only .agentpal/project.json, .agentpal/AGENTPAL.md, and the protected CLAUDE.md block.
when_to_use: Trigger on requests like “启用 AgentPal”, “把当前项目接入 AgentPal”, “Enable AgentPal for this project”, or “connect this Claude Code project to AgentPal”. If the AgentPal source path or URL is missing, ask one short question before writing files.
argument-hint: [agentpal-path-or-github-url(optional)]
---

# AgentPal Enable

Use [../../references/binding-rules.md](../../references/binding-rules.md), [../../templates/.agentpal/project.json](../../templates/.agentpal/project.json), [../../templates/.agentpal/AGENTPAL.md](../../templates/.agentpal/AGENTPAL.md), and [../../templates/CLAUDE.agentpal-block.md](../../templates/CLAUDE.agentpal-block.md).

## Goal

Enable a thin AgentPal binding for the current Claude Code project.

## Required Behavior

1. Work only inside the current project.
2. Only create or update:
   - `.agentpal/project.json`
   - `.agentpal/AGENTPAL.md`
   - the protected AgentPal block in root `CLAUDE.md`
3. Do not create `AGENTS.md`.
4. Do not create `.claude/settings.local.json`.
5. Do not copy full AgentPal assets into the project.
6. When local shell execution is available, call `python scripts/agentpal_binding.py enable --project-root <current-project-root>` from the plugin root or execute the exact same file protocol.

## Source Resolution

Resolve the AgentPal source in this order:

1. If `$ARGUMENTS` contains a local path, use it and set:
   - `agentpal_source.type: user_configured_source`
   - `agentpal_source_value: <that path>`
   - `agentpal_workspace_root: <that path>`
2. If `$ARGUMENTS` contains a GitHub URL, use it and set:
   - `agentpal_source.type: github_source`
   - `agentpal_source_value: <that URL>`
   - `agentpal_workspace_root: ""`
3. If the current session already has access to an AgentPal workspace containing `agentpal.json`, use that and set:
   - `agentpal_source.type: central_path`
   - `agentpal_source_value: <that path>`
   - `agentpal_workspace_root: <that path>`
4. Otherwise ask one short question asking for the local AgentPal workspace path or GitHub source URL, then stop until the user answers.

## File Creation Rules

### `.agentpal/project.json`

Create `.agentpal/` if needed, then write `project.json` from the template.

Fill these values:

- `__PROJECT_NAME__`: current project directory name
- `__ACTIVE_PROJECT_ROOT__`: absolute current project path
- `__AGENTPAL_SOURCE__`: resolved source type
- `__AGENTPAL_SOURCE_VALUE__`: resolved path or URL
- `__AGENTPAL_WORKSPACE_ROOT__`: path when available, otherwise empty string
- `__CREATED_AT__`: current ISO timestamp if file did not already exist
- `__UPDATED_AT__`: current ISO timestamp
- `enabled_runtimes`: preserve existing runtimes and add `claude-code`
- `last_runtime`: `claude-code`
- `status`: `enabled`

If `project.json` already exists and parses, preserve any recoverable user-approved source values and other runtime entries while updating missing canonical fields.

### `.agentpal/AGENTPAL.md`

Write the template content as a thin-binding explainer. Do not expand it into copied Pal documentation.

### `CLAUDE.md`

Insert or replace exactly one protected AgentPal block using:

```html
<!-- BEGIN AGENTPAL BINDING: claude-code -->
<!-- END AGENTPAL BINDING: claude-code -->
```

Preserve all existing `CLAUDE.md` content before and after the block.

If a legacy `<!-- AGENTPAL:BEGIN -->` or `<!-- BEGIN AGENTPAL WORKGROUP -->` block exists and no new block exists, replace the legacy block with the new runtime-qualified block.

Running enable twice must not create duplicate blocks.

## Final Report

Report:

- binding state before
- source resolution result
- changed files
- whether the block was inserted, replaced, or left unchanged
- any question still blocking full AgentPal use

## `/pal Name`

Do not implement keyword routing. Only explain that `/pal Name` is a semantic protocol interpreted after reading the binding and any accessible AgentPal registry.
