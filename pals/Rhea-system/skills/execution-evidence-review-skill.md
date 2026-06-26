# execution-evidence-review

## Purpose

Review Runtime output to determine whether an action actually happened, what changed, what did not run, and what risk remains.

## When to use

Use after commands, file reads/writes, installs, release checks, system inspections, or troubleshooting actions.

## Inputs

Runtime output, command/action summary, working directory, exit status, changed files, logs, screenshots, not-run items, and declared goal.

## Required context

Evidence-based operations knowledge, output contract, risk classification, and expected acceptance criteria.

## Process

1. Record what was run or performed.
2. Record where it was run.
3. Record who or what executed it: current Runtime, external Runtime, user, or unknown.
4. Record exit status or observable result.
5. Record changed files or system state if any.
6. Record not-run items.
7. Compare evidence to acceptance criteria.
8. Report risks and next action.

## Output

Evidence review with what was run, where, executor, result, changed files, not-run items, risks, and next action.

## Quality bar

Completion is not proven unless evidence covers every required item.

## User confirmation points

Ask before follow-up actions that widen scope, change files, use elevated permissions, or touch sensitive data.

## No-code boundary

This skill reviews evidence and writes a report. It does not create automation.

## Common mistakes

- Treating no error output as success.
- Omitting working directory.
- Forgetting not-run items.
- Failing to name changed files.

## Example

"Runtime ran `git diff --check` in the AgentPal Workspace; exit code 0; no whitespace errors; CRLF warnings only; no files changed by this command."
