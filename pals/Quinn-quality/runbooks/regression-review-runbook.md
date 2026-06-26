# Regression Review Runbook

## Trigger

A completed change may affect existing behavior, shared assets, or previously accepted outputs.

## Inputs

Change summary, affected files, previous behavior, risk severity, available checks, test results, and not-run items.

## Steps

1. Identify preserved behavior.
2. Map changed files to affected surfaces.
3. Choose risk-prioritized checks.
4. Review Runtime returned results.
5. Record failed, partial, and not-run items.
6. Decide whether regression risk is acceptable.

## Decision points

- Are core paths covered?
- Are shared assets affected?
- Does not-run regression block acceptance?

## Outputs

Regression review report and follow-up task package if needed.

## Quality checks

Regression review must cover old behavior, not only new files.

## Required user confirmation

Required before accepting high-risk regression gaps or running broad external checks.

## Evidence to return

Affected surfaces, checks, results, not-run items, failures, and residual regression risk.
