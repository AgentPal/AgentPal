# Runbooks And Workflows

## Status

Current for AgentPal `v0.1.0-rc.1`.

Runbooks and workflows help a Pal repeat good work without turning AgentPal into an execution engine.

## Minimum

```text
runbooks/index.md
workflows/index.md
```

Both indexes may be empty placeholders at first.

## Runbooks

A runbook is a repeatable procedure for a known task family. It should include:

- when to use it
- required inputs
- read-only checks first
- approval gates
- evidence required
- what the Pal reports

## Workflows

A workflow is a larger lifecycle that may combine Skills, knowledge, runbooks, and handoffs. It should include:

- stages
- owner Pal responsibilities
- optional collaborators resolved from central contacts
- evidence and completion rules

## Boundary

Runbooks and workflows guide the current host runtime. They do not create active Subagent Mode, Deep Conductor, parallel child workflows, or external Agent orchestration in `v0.1.0-rc.1`.
