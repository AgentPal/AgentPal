# False Completion Check Runbook

## Trigger

A completion claim feels too broad, unverified, or inconsistent with the original request.

## Inputs

Original objective, completion report, actual changed files, evidence outputs, not-run items, and current status.

## Steps

1. Reconstruct the required end state.
2. Compare each requirement to current evidence.
3. Identify plan-only work, missing files, missing checks, and unsupported claims.
4. Check whether partial was reported as pass.
5. Assign severity and next owner.
6. Report corrected status.

## Decision points

- Is the missing item required or optional?
- Is evidence absent, weak, or contradictory?
- Does false completion block final report?

## Outputs

False completion findings and correction task package.

## Quality checks

The runbook proves completion requirement by requirement.

## Required user confirmation

Required before broadening read scope or accepting unsupported residual risk.

## Evidence to return

Requirement, claim, evidence, true status, severity, and correction owner.
