# Test And Verification Workflow

## Trigger

A development task needs proof before it can be judged complete.

## Inputs

- Acceptance criteria.
- Planned or actual changed files.
- Available test framework and commands.
- Manual verification needs.
- Risk level.

## Steps

1. Map acceptance criteria to checks.
2. Select targeted automatic tests where available.
3. Add regression checks for existing behavior.
4. Add manual or browser checks when behavior requires it.
5. Define evidence format for each check.
6. Require not-run reasons when checks cannot run.
7. Review evidence after runtime execution.

## Decision points

- Which checks are required versus optional?
- Is manual verification needed?
- Does an unavailable tool block completion or only limit confidence?
- Is Quinn review needed?

## Outputs

Verification plan, runtime test instructions, evidence checklist, and final verification judgement.

## Quality checks

- Every required criterion has evidence or not-run label.
- Tests are scoped to the task.
- Regression path is included.
- High-risk areas are not under-tested.

## Required user confirmation

Required before using real user data, production services, payment flows, destructive scenarios, or long-running external checks.

## Evidence to return

Return commands, outputs, screenshots, logs, manual steps, failures, not-run labels, and final status.
