# evidence-review-workflow

## Trigger

Runtime or another Pal reports that checks, commands, file edits, release gates, or troubleshooting actions were performed.

## Inputs

Runtime output, action summary, working directory, exit status, changed files, logs, not-run list, risk level, and acceptance criteria.

## Steps

1. Record what was run or performed.
2. Record where it ran.
3. Record executor.
4. Record exit status or observable result.
5. Record changed files/state.
6. Record not-run items.
7. Compare evidence to acceptance criteria.
8. Report completion, incomplete, blocked, or not-run.

## Decision points

- Does evidence prove each requirement?
- Is evidence too narrow?
- Are follow-up actions safe?

## Outputs

Evidence review report and next action recommendation.

## Quality checks

No broad claim from narrow evidence; not-run items remain visible.

## Required user confirmation

Required before follow-up actions that write, delete, publish, install, or widen scope.

## Evidence to return

Action, executor, location, result, changed files/state, not-run items, risks, and next action.

