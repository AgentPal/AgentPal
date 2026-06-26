# Small Bugfix Runbook

## Trigger

A narrow bug has clear symptoms, likely small scope, and enough evidence for runtime repair.

## Inputs

- Bug description.
- Reproduction steps or failure output.
- Expected behavior.
- Suspected files or module.
- Allowed edit scope.
- Required regression evidence.

## Steps

1. Confirm the bug and expected behavior.
2. Define minimal allowed files.
3. Create a small Runtime Task Package.
4. Require targeted fix only.
5. Require targeted test or manual reproduction check.
6. Review changed files and evidence.

## Decision points

- Is the issue reproducible?
- Is scope small enough?
- Does it need environment review?
- Does it need product clarification?

## Outputs

Bugfix task package and evidence review.

## Quality checks

- No unrelated refactor.
- Reproduction or blocker reported.
- Regression evidence included.
- Changed files match scope.

## Required user confirmation

Required before deleting files, changing dependencies, editing configs, or broadening scope.

## Evidence to return

Return reproduction result, changed files, tests/manual checks, failures, not-run items, and remaining risk.
