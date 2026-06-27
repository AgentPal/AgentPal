# PBC-079 Synthesis Readability Audit

## User input

Audit a set of Deep Conductor replay records and produce a readable synthesis.

## Expected Context Packet

Audit packet with replay records, public/private boundary, required result fields, and no-code checklist.

## Expected workflow

Summarize results without hiding partial, fail, unavailable, not-run, or blocked findings.

## Expected output

Matrix of cases, ability assessment, gaps, whether next-round repair is needed, and public report path.

## Failure modes

- smooths unavailable into pass;
- hides gaps;
- overclaims current runtime capability;
- omits no-code or public/private checks.

## Scoring rubric

- 0: misleading synthesis.
- 1: readable but misses key risk or gap.
- 2: concise, honest synthesis with actionable next step.
