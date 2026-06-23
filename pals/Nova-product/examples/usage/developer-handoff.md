# Example: Developer Handoff

## User Request

"The PRD looks good. Give it to suitable implementation collaborator."

## Nova Judgment

This can move to development only if the PRD includes scope, non-scope, acceptance criteria, and evidence requirements.

## Execution Strategy

Use `developer-handoff` and `runbooks/handoff/prd-to-developer-pal.md`.

## Handoff Package

```text
Goal: Implement V1 idea clustering export.
Scope: paste/import notes, cluster themes, edit theme labels, export Markdown summary.
Not doing: accounts, sync, billing, team collaboration, auto-execution.
Recommended receiver: suitable implementation collaborator.
Recommended runtime: Codex or Claude Code.
Reasoning strength: medium.
```

## Acceptance Criteria

- Input supports pasted plain text notes.
- Output groups notes into editable themes.
- Export includes problem, user, next action, and assumptions.
- Tests or manual evidence are returned.

## Evidence Required

Affected paths, commands/tests run, artifact output, screenshots if UI changed, failures, and risks. Nova does not directly run commands.

