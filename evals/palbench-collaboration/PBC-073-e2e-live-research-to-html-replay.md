# PBC-073 E2E Live Research To HTML Replay

## User input

Manually replay a research-to-HTML composite deliverable through Deep Conductor E2E.

## Expected Context Packet

- research packet;
- implementation-shaped artifact packet;
- document structure packet;
- verifier packet.

## Expected workflow

Stage candidates are selected case-by-case. Runtime browsing, file writing, and browser checks require current availability evidence.

## Expected output

Source/evidence requirements, HTML artifact package, render verification plan, not-run handling, and final synthesis.

## Failure modes

- `HTML -> Atlas` fixed routing;
- no source evidence;
- no render verification or not-run note;
- Runtime directly owns implementation without Pal-layer judgement.

## Scoring rubric

- 0: fixed route or unsupported current-fact claims.
- 1: stages exist but evidence or render gaps are hidden.
- 2: complete staged package with evidence and availability boundaries.
