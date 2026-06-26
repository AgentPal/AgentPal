# Not-run Triage Runbook

## Trigger

A required or expected check was not executed.

## Inputs

Not-run item, reason, required evidence, affected acceptance criteria, risk, and available alternatives.

## Steps

1. Name the not-run item.
2. Record reason and executor capability.
3. Determine whether it is required for acceptance.
4. Classify impact as acceptable risk, partial, follow-up, or blocker.
5. Assign next owner and evidence needed.
6. Preserve the item in the final report.

## Decision points

- Is not-run due to unavailable runtime, user choice, blocked dependency, or out-of-scope criterion?
- Does it affect release readiness?
- Is user confirmation needed to accept the risk?

## Outputs

Not-run triage table.

## Quality checks

not-run is not pass and not automatic fail.

## Required user confirmation

Required for release, high-risk, privacy, production, or destructive checks.

## Evidence to return

Item, reason, impact, blocker status, next owner, and residual risk.
