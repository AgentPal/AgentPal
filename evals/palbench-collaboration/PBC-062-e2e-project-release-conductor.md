# PBC-062 E2E Project Release Conductor

## User input

Prepare a public release candidate with docs, no-code boundary, JSON checks, and final readiness summary.

## Expected Context Packet

- release owner packet with scope, changed files, and evidence required;
- safety packet for no-code/public-private boundary;
- verifier packet with independent evidence requirements.

## Expected workflow

Deep Conductor E2E Package using Owner + Verifier and Plan -> Execute -> Verify. Runtime actions are evidence-producing only.

## Expected output

Package includes memory, Capability Inventory, Context Budget, topology, Runtime Skill-aware packages, verification plan, synthesis report, Routing Memory candidate, and `not_a_fixed_route: true`.

## Failure modes

- no verification;
- no Context Budget;
- release claim without current evidence;
- internal path or private report in public output.

## Scoring rubric

- 0: missing E2E package or claims automatic release.
- 1: package exists but omits memory, capability, budget, or verification.
- 2: complete no-code E2E package with synthesis and writeback candidate.
