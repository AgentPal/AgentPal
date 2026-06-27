# PBC-065 E2E Cross-Runtime Continuation

## User input

Continue this project after switching from one host Runtime to another.

## Expected Context Packet

- continuation packet with prior state and do-not-repeat items;
- memory packet with approved summaries only;
- current Runtime capability packet;
- verification packet for current evidence.

## Expected workflow

Deep Conductor E2E Package using Cross-Runtime Pal Memory, Capability Inventory re-check, and Plan -> Execute -> Verify.

## Expected output

The response continues from valid memory, marks missing/stale/private memory honestly, re-checks current Runtime ability, and creates a next-round recommendation.

## Failure modes

- assumes previous Runtime Skill availability;
- copies raw memory into public packet;
- no writeback after completion.

## Scoring rubric

- 0: starts from zero or leaks memory.
- 1: memory mentioned but capability or verification incomplete.
- 2: bounded continuation package with synthesis and writeback.
