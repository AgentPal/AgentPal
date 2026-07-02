# <Team Display Name>

## Team Identity

- team_id: `<team-id>`
- type: `team-pack`
- version: `0.6.0`
- status: `draft`

## Team Mission

Describe the stable work this team exists to handle.

## Suitable Tasks

- `<task type this team should handle>`
- `<repeatable task family>`

## Unsuitable Tasks

- `<task type this team should not handle>`
- `<work that belongs to one owner Pal instead>`

## Member Overview

This team references Pals by ID in `roster.json`. It does not copy Pal Packs or
Pal private assets into the Team Pack.

| Role | Pal reference | Notes |
| --- | --- | --- |
| coordinator | `<pal-id>` | Entry and user brief coordination |
| owner | `<pal-id or open role>` | Main delivery owner |
| verifier | `<pal-id or open role>` | Quality review when needed |

## Team Roles

List the reusable roles in this team. A role is not the Pal itself. One Pal may
hold different roles in different teams.

## Default Workflow

1. Understand the user goal.
2. Select the matching team workflow.
3. Assign roles through `roster.json`.
4. Load the minimum required team assets.
5. Let selected Pals perform their own asset preflight.
6. Review against team evals.
7. Report completed, skipped, blocked, and follow-up items.

## Team Acceptance

Describe how the team decides whether work is good enough. Link to
`evals/definition-of-done.md` or another team eval.

## Collaboration Boundary

- The team is selected by AI judgement, not keyword routing.
- Team routing cards are judgement inputs, not route maps.
- Pal boundaries override team role assignment.
- Runtime execution requires current host evidence.

## User Invocation

Examples:

```text
Mira, use <Team Display Name> for this task.
Mira, ask the <team type> team to prepare the workflow.
```
