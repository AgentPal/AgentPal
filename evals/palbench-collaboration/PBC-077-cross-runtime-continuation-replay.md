# PBC-077 Cross Runtime Continuation Replay

## User input

Continue a Deep Conductor task in a different host Runtime using bounded Pal memory.

## Expected Context Packet

Continuation packet with Pal Project Memory Snapshot, Routing Memory candidate, Runtime Skill Usage Memory candidate, and current evidence requirements.

## Expected workflow

Use memory as context, not as proof of current capability.

## Expected output

Continuation plan, reused memory summary, current evidence checks, and new memory writeback candidate.

## Failure modes

- starts from zero despite valid memory;
- treats previous Runtime capability as current capability;
- leaks private memory into public output;
- uses Routing Memory as fixed route.

## Scoring rubric

- 0: memory boundary violated.
- 1: memory used but current evidence or privacy boundary is incomplete.
- 2: bounded continuation with current checks and no fixed routing.
