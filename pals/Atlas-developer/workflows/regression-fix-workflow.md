# Regression Fix Workflow

## Trigger

Existing behavior breaks after a recent or suspected change.

## Inputs

- Old expected behavior.
- Broken current behavior.
- Reproduction steps.
- Failing tests or user evidence.
- Recent changes.
- Allowed fix scope.

## Steps

1. Confirm the regression statement.
2. Identify change window and likely files.
3. Create testable hypotheses.
4. Prepare a minimal investigation task.
5. Require minimal fix and prevention check.
6. Run or request regression evidence.
7. Review changed files for scope creep.

## Decision points

- Can the regression be reproduced?
- Is the suspected cause in allowed scope?
- Is rollback safer than repair?
- Does the fix require environment or data owner review?

## Outputs

Regression repair task package, evidence checklist, review findings, and remaining risk.

## Quality checks

- Old and broken behavior are distinct.
- Fix is minimal.
- Prevention check exists.
- Unrelated refactor is excluded.

## Required user confirmation

Required before rollback, data migration, dependency downgrade, broad revert, or release state changes.

## Evidence to return

Return reproduction result, root cause, changed files, regression test/manual proof, and not-run checks.
