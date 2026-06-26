# release-preflight-risk-runbook

## Trigger

Before claiming release readiness, publish readiness, or export readiness.

## Inputs

Release scope, changed paths, no-code check, JSON parse, diff check, status, privacy boundary, and rollback status.

## Steps

1. Confirm release scope.
2. Run no-code boundary check.
3. Parse required JSON files.
4. Run diff whitespace check.
5. Inspect status for dirty/untracked files.
6. Check private/public boundary.
7. Check rollback readiness.
8. Report pass, conditional pass, blocked, or not-run.

## Decision points

- Does evidence cover every gate?
- Is publish action requested?
- Is rollback ready?

## Outputs

Release preflight risk report.

## Quality checks

No release claim beyond evidence.

## Required user confirmation

Required before tag, push, publish, export, or release-scope change.

## Evidence to return

Gate outputs, changed paths, status summary, privacy findings, rollback status, and not-run items.

