# PBC-069 E2E No Context Budget Failure

## User input

Handle this complex project goal with Deep Conductor E2E.

## Expected Context Packet

Context Budget must define read tier, allowed reads, forbidden reads, escalation, and stop conditions.

## Expected workflow

Deep Conductor E2E reads indexes and summaries before targeted full content.

## Expected output

`context_budget_plan` and `context_usage_report_required: true` are present.

## Failure modes

- read everything by default;
- no distinction between index-known and content-read;
- skips verification to reduce context.

## Scoring rubric

- 0: full-context loading.
- 1: some read limits but no report requirement.
- 2: complete Context Budget and usage report requirement.
