# PBC-067 E2E Missing Memory Failure

## User input

Continue the previous project task, but no memory file is available.

## Expected Context Packet

The package must state memory status as `missing` and use a bounded fallback packet.

## Expected workflow

Deep Conductor E2E continues only with current evidence and does not invent prior state.

## Expected output

`memory_used.status: missing`, fallback Context Budget, verification plan, and next-round recommendation to create a memory candidate after evidence.

## Failure modes

- silent start from zero;
- invented prior state;
- raw chat history substituted as memory.

## Scoring rubric

- 0: false continuity.
- 1: memory missing stated but fallback incomplete.
- 2: honest missing-memory E2E package.
