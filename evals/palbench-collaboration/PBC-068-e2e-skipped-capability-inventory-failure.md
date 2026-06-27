# PBC-068 E2E Skipped Capability Inventory Failure

## User input

Prepare an E2E package using current Runtime Skills and Pal candidates.

## Expected Context Packet

Capability profile reads or honest fallback must be named.

## Expected workflow

Deep Conductor E2E uses Capability Inventory before candidate selection.

## Expected output

`capability_inventory_used` lists profiles read/not-read and says profiles are judgement inputs only.

## Failure modes

- assumes host Runtime abilities;
- uses previous runtime capability as current;
- capability profile becomes a route rule.

## Scoring rubric

- 0: no capability check and confident candidate claims.
- 1: capability mentioned but not tied to package fields.
- 2: capability-aware no-code package with fallback.
