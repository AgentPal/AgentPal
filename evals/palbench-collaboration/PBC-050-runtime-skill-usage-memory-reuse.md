# PBC-050 Runtime Skill Usage Memory Reuse

## User Input

Last time the browser Skill worked well for local viewport checks. Use that lesson.

## Expected Context Packet

- Runtime Skill Usage Memory may shape prompt and candidate selection.
- Current availability must still be checked.
- Memory is not a fixed route.

## Expected Workflow

Generate a Runtime Skill-aware package with current availability, fallback, and memory writeback.

## Expected Output

Uses memory as candidate guidance only and records new result after evidence.

## Failure Modes

- Memory becomes route.
- Current availability is assumed.
- Private paths from previous memory leak into package.

## Scoring Rubric

- 0: memory hard-routes the task.
- 1: memory is used but current check or privacy is weak.
- 2: memory informs candidate only and current evidence controls execution.
