# Regression Gate Workflow

## Trigger

A change may affect existing behavior, shared assets, release readiness, or previously accepted workflows.

## Inputs

Changed files, affected surfaces, known fragile paths, existing behavior to preserve, risk severity, and available checks.

## Steps

1. Identify existing behavior that must remain true.
2. Identify neighboring and shared assets.
3. Choose smoke, targeted, and broader regression checks.
4. Prioritize by user impact and reversibility.
5. Define evidence required for each check.
6. Record not-run regression items.

## Decision points

- Which old behavior is in scope?
- Are core paths unverified?
- Does missing regression evidence block acceptance?

## Outputs

Regression gate matrix and required evidence list.

## Quality checks

Gate covers old behavior, not only the changed artifact.

## Required user confirmation

Required for broad, external, production, destructive, or long-running checks.

## Evidence to return

Checks planned, checks run by Runtime, results, not-run items, and residual regression risk.
