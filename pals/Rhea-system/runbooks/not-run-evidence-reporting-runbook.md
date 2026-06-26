# not-run-evidence-reporting-runbook

## Trigger

Any verification, command, check, or evidence request cannot be performed or was intentionally skipped.

## Inputs

Requested check, reason not run, required evidence, impact, alternative evidence, and next action.

## Steps

1. Name the exact not-run item.
2. State why it was not run.
3. State what requirement it would have covered.
4. State impact on completion claim.
5. Offer safe next action or fallback.

## Decision points

- Does not-run block completion?
- Is there alternative evidence?
- Is user approval needed for the check?

## Outputs

Not-run report.

## Quality checks

Do not hide skipped checks inside a pass.

## Required user confirmation

Required if running the skipped check would involve high-risk action, private data, external access, or scope expansion.

## Evidence to return

Not-run item, reason, requirement affected, completion impact, and next action.

