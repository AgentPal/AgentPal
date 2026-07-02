# Status Model

The binder should report one of these states for the current project:

## `unbound`

No AgentPal thin-binding files are present and no AgentPal Claude block is present.

## `complete`

All of these are true:

- `.agentpal/project.json` exists
- `.agentpal/project.json` parses as JSON
- `.agentpal/project.json` includes the canonical project thin-binding fields
- `.agentpal/AGENTPAL.md` exists
- root `CLAUDE.md` contains exactly one runtime-qualified Claude Code AgentPal block
- `.agentpal/AGENTPAL.md` and the runtime-qualified Claude Code block contain the current v0.6 runtime anchors: `Workflow Execution Contract`, `Closure Gate`, `Owner Assignment Integrity`, `Team label is not participant`, `open role`, `Pal naming`, `Faye`, `no fake verifier`, and `simulated-as-real`

## `partial`

The project has a thin binding, but one or more required artifacts are missing.

Examples:

- `project.json` exists but `AGENTPAL.md` is missing
- `.agentpal/` exists but `CLAUDE.md` has no AgentPal block
- the binding exists but `.agentpal/AGENTPAL.md` or the Claude Code block is missing current v0.6 runtime anchors

## `damaged`

The project has a thin binding, but one or more required artifacts are malformed.

Examples:

- `project.json` is invalid JSON
- required fields are missing
- multiple or mixed Claude AgentPal blocks exist

## `legacy-block`

The project still uses the old Claude marker block and should be migrated to:

```html
<!-- BEGIN AGENTPAL BINDING: claude-code -->
<!-- END AGENTPAL BINDING: claude-code -->
```
