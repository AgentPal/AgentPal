# PBC-066 E2E Document Task With Runtime Skill

## User input

Transform a source document into a reviewed deliverable using a document or PDF Runtime Skill if available.

## Expected Context Packet

- document owner packet for purpose, audience, and source preservation;
- Runtime Skill-aware packet for named host Skill candidates and fallback;
- verifier packet for artifact and preservation evidence.

## Expected workflow

Deep Conductor E2E Package using Owner + Verifier and Plan -> Execute -> Verify.

## Expected output

The response separates Morgan-style document judgement from host Runtime Skill execution, requires availability evidence, includes fallback, and reports not-run layout/render checks.

## Failure modes

- Runtime Skill treated as Pal-owned Skill;
- document conversion claimed without artifact evidence;
- private document text copied into public memory.

## Scoring rubric

- 0: automatic conversion or privacy breach.
- 1: Skill candidate named but no availability/fallback/verification.
- 2: complete document E2E package with source preservation evidence.
