# Pal Delegation Workflow

## Trigger

Mira determines that another registered Pal should consult, own a stage, or take over the task.

## Inputs

- User request.
- Owner judgement.
- Contacts / registry.
- Context Packet.
- Risk and approval constraints.

## Steps

1. Decide collaboration mode: consult, delegate, or handoff.
2. State the selected owner and case-specific reason.
3. Prepare a Context Packet with objective, scope, evidence, forbidden actions, and acceptance criteria.
4. Ask for approval if sensitive context must be shared.
5. Let the owner Pal answer immediately when supported.
6. If Mira later summarizes, label specialist output and avoid replacing it.

## Decision points

- Does Mira keep final ownership or transfer it?
- Does the task need PalSmith governance?
- Does the runtime support same-response handoff?
- Is user approval needed for context transfer?

## Outputs

Visible owner judgement, Context Packet, owner Pal answer, or owner-gap fallback.

## Quality checks

- Handoff is explicit.
- The receiving Pal has enough context.
- Mira stops performing specialist work after handoff.
- PalSmith access is not restricted to Mira.

## Required user confirmation

Required before sharing private, sensitive, or broad context with another Pal.

## Evidence to return

Return the selected owner, reason, context sent, files read, files excluded, and remaining owner gaps.
