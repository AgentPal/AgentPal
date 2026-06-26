# Runtime Task Package Briefing Skill

## Purpose

Help Mira brief Codex or another runtime as an execution layer under Pal-owned work.

## When to use

Use when work requires file edits, command execution, browser checks, document generation, or other evidence-producing runtime actions.

## Inputs

- Pal owner and task objective.
- Allowed files or systems.
- Forbidden actions.
- Required edits or checks.
- Acceptance criteria and report format.

## Required context

Use the owner Pal's Task Package, current workspace boundary, and user constraints. Do not let the runtime choose the Pal owner after execution begins.

## Process

1. State the Pal owner and why the runtime is only execution layer.
2. List allowed actions and forbidden actions.
3. List files to read and files allowed to edit.
4. List verification commands or honest not-run reporting.
5. Require final evidence summary.

## Output

A Runtime Task Package or execution preflight.

## Quality bar

The runtime should be able to execute the task without expanding scope, creating new dependencies, or claiming unverified success.

## User confirmation points

Ask before enabling destructive commands, installing dependencies, browsing external sites, or reading broad private directories when not already authorized.

## No-code boundary

This skill briefs a runtime. It is not a runtime, agent, plugin, or validator.

## Common mistakes

- Calling the runtime the owner.
- Omitting forbidden actions.
- Allowing implementation before Pal governance for Pal asset changes.
- Replacing evidence with confidence.

## Example

PalSmith creates a Task Package for Mira Leader deepening; Atlas executes Markdown and JSON edits only under that package and then reports validation.
