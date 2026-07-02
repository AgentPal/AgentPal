# Binding Rules

Use these rules for every binder action.

## Allowed Writes

- `.agentpal/project.json`
- `.agentpal/AGENTPAL.md`
- root `CLAUDE.md` block between `<!-- BEGIN AGENTPAL BINDING: claude-code -->` and `<!-- END AGENTPAL BINDING: claude-code -->`

## Allowed Deletes

- `.agentpal/` only when no other runtime binding remains
- the protected AgentPal block in root `CLAUDE.md`

## Forbidden Writes In V1

- `AGENTS.md`
- `.claude/settings.local.json`
- `.gitignore`
- copied Pal assets
- central contacts or registry files
- memory, state, reports, evals, or workflow folders under `.agentpal/`

## Marker Policy

Write new Claude blocks only with:

```html
<!-- BEGIN AGENTPAL BINDING: claude-code -->
<!-- END AGENTPAL BINDING: claude-code -->
```

Recognize older markers for migration and cleanup:

```html
<!-- AGENTPAL:BEGIN -->
<!-- AGENTPAL:END -->
```

```html
<!-- BEGIN AGENTPAL WORKGROUP -->
<!-- END AGENTPAL WORKGROUP -->
```

For multi-runtime coexistence:

- `disable claude-code` must not remove the Codex block in `AGENTS.md`
- `disable claude-code` must not delete `.agentpal/` while another runtime still uses it

## Routing Policy

- default Pal: `Mira`
- owner selection: `ai_judgement_only`
- keyword routing: forbidden
- `/pal Name` is a semantic protocol, not a plugin route table
