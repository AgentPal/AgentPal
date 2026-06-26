# incident-review-workflow

## Trigger

A runtime action, release, environment repair, file operation, or system task fails or creates unexpected risk.

## Inputs

Incident summary, evidence, impact, timeline, actions taken, affected paths/systems, mitigation status, and open risks.

## Steps

1. State current status and severity.
2. Build evidence-backed timeline.
3. Identify affected scope.
4. Identify root-cause candidates and contributing factors.
5. Identify mitigations and rollback/recovery status.
6. Define follow-up actions and owner candidates.
7. Distill public-safe learning if appropriate.

## Decision points

- Is the incident active, mitigated, resolved, or unknown?
- Is sensitive material involved?
- Does another Pal own follow-up?

## Outputs

Incident review with impact, timeline, evidence, root-cause candidates, mitigations, follow-up actions, and not-run items.

## Quality checks

Blameless tone, evidence-backed claims, private data minimized, and concrete follow-up.

## Required user confirmation

Required before sharing sensitive logs, writing durable memory, or performing recovery action.

## Evidence to return

Timeline evidence, affected paths/systems, current status, mitigation evidence, and open risks.

