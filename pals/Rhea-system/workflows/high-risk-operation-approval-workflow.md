# high-risk-operation-approval-workflow

## Trigger

An action is high, critical, destructive, privileged, external, release-impacting, or privacy-sensitive.

## Inputs

Action description, target paths/components, risk classification, rollback plan, safer alternatives, and evidence requirements.

## Steps

1. State the exact action.
2. State target and scope.
3. Explain risk and blast radius.
4. State safer read-only alternative.
5. State rollback or recovery plan.
6. Ask explicit confirmation if action remains appropriate.
7. Define post-action evidence.

## Decision points

- Can read-only evidence reduce risk?
- Is rollback ready?
- Is user authority clear?
- Is the action blocked by missing target, unclear scope, or forbidden boundary?

## Outputs

Approval request, gate status, allowed action, forbidden action, and evidence contract.

## Quality checks

Approval cannot be vague, bundled, or implied.

## Required user confirmation

Required before proceeding with high or critical actions.

## Evidence to return

Confirmation text, target scope, rollback note, executor, result, changed files/state, and not-run items.

