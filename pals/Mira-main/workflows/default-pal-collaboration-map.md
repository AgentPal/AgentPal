# Default Pal Collaboration Map

## Trigger

Mira needs to explain or choose how default Pal collaboration should work for a task.

## Inputs

- User request.
- Current contacts / registry.
- Candidate owner Pals.
- Collaboration mode needed.
- Risk and context boundary.

## Steps

1. Check contacts / registry for available Pals.
2. Use AI judgement to identify owner candidates.
3. Choose direct answer, consult, delegate, handoff, review, or owner-gap fallback.
4. Prepare Context Packet if another Pal participates.
5. Keep final synthesis labeled by source Pal when multiple outputs are combined.

## Decision points

- Is there a clear registered owner?
- Is Mira only coordinating?
- Is review needed after execution?
- Does the user need to approve context sharing?

## Outputs

Collaboration judgement, Context Packet, handoff statement, review request, or fallback explanation.

## Quality checks

- Contacts / registry are source of available Pals.
- Capability notes are judgement inputs, not fixed routes.
- Specialist ownership is preserved.
- Mira is neither secretary-only nor universal owner.

## Required user confirmation

Required when collaboration expands shared context or changes durable assets.

## Evidence to return

Return contacts / registry paths used, owner reason, context sent, and review evidence when applicable.
