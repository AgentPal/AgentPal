# rollback-readiness-runbook

## Trigger

Before or after changes where recovery matters.

## Inputs

Change description, affected paths, tracked/untracked status, backup status, previous known-good state, and rollback authority.

## Steps

1. Identify reversible unit.
2. Identify recovery mechanism.
3. Check untracked or ignored files.
4. Check backup/archive for non-git state.
5. Define rollback evidence.
6. Mark readiness as ready, partial, missing, not-run, or blocked.

## Decision points

- Does rollback cover all changed state?
- Is backup tested?
- Is authority clear?

## Outputs

Rollback readiness report.

## Quality checks

No generic rollback claim without path-specific evidence.

## Required user confirmation

Required before proceeding when rollback is missing for high or critical operations.

## Evidence to return

Affected paths, rollback mechanism, backup status, not-run items, and remaining risk.

