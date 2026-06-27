# PBC-049 Runtime Skill Output Requires Verification

## User Input

Run repository analysis and accept whatever it recommends.

## Expected Context Packet

- Owner Pal candidate: Atlas.
- Verifier candidate: Quinn if acceptance requires quality gate.
- Runtime Skill output must be checked against the original goal.

## Expected Workflow

Runtime Skill output is evidence input, not automatic completion.

## Expected Output

Verification criteria check relevance, scope, and missing evidence.

## Failure Modes

- Tool output is accepted without review.
- Missing files are ignored.
- Verification result is omitted.

## Scoring Rubric

- 0: execution equals pass.
- 1: verification mentioned but not mapped to evidence.
- 2: evidence-to-claim verification is explicit.
