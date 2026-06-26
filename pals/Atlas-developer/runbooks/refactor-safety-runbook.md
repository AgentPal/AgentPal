# Refactor Safety Runbook

## Trigger

User requests refactor, cleanup, restructuring, or an implementation task threatens to expand into refactor.

## Inputs

- Refactor goal.
- Behavior that must remain unchanged.
- Allowed files.
- Forbidden files.
- Test and regression evidence.
- Rollback plan.

## Steps

1. Define why refactor is needed.
2. Define behavior that must not change.
3. Limit file scope and batch size.
4. Require pre/post checks or snapshots where available.
5. Forbid feature changes unless explicitly included.
6. Review diff for behavior drift.

## Decision points

- Is the refactor necessary for the user goal?
- Can it be split into smaller batches?
- Are tests sufficient to protect behavior?
- Is the risk too high without Quinn review?

## Outputs

Refactor task package, safety checklist, and review report.

## Quality checks

- No behavior change hidden inside refactor.
- Small scope.
- Regression evidence.
- Rollback path.

## Required user confirmation

Required for broad refactors, generated-file churn, public API changes, migration, or dependency changes.

## Evidence to return

Return before/after checks, changed files, test results, behavior assurance, and not-run items.
