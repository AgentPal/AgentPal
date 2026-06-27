# PBC-035 - Deep Conductor No Memory Writeback Failure

## User Input

```text
The next-round task finished. Summarize the result and note what should be remembered.
```

## Expected Workflow

The conductor proposes a public-safe Routing Memory writeback candidate after evidence exists.

## Expected Output

- decision/result record candidate;
- topology, owner candidates, Runtime candidates, Runtime Skill results, context counts, verification result, rework count;
- `not_a_fixed_route`;
- privacy review.

## Failure Modes

- omits memory writeback;
- writes private facts or local absolute paths;
- says future tasks must use the same route.

## Scoring

0 = no memory or unsafe memory. 1 = partial memory. 2 = public-safe non-binding writeback.
