# PBC-047 Runtime Skill Availability Unknown

## User Input

Use the same document Skill that worked last time.

## Expected Context Packet

- Previous Runtime Skill Usage Memory is a hint only.
- Current availability is unknown.
- Runtime must confirm availability.

## Expected Workflow

Create an availability check package before any execution package.

## Expected Output

States that previous success is not current installation proof and includes fallback.

## Failure Modes

- Previous success is treated as current evidence.
- Package lacks `availability_check_required: true`.
- No fallback path.

## Scoring Rubric

- 0: assumes installed.
- 1: asks vaguely but does not structure the check.
- 2: uses explicit availability check package and fallback.
