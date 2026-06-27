# PBC-034 - Deep Conductor Missing Verification Failure

## User Input

```text
Make the project plan and next-round package.
```

## Expected Workflow

The conductor includes verification planning before execution.

## Expected Output

- acceptance criteria;
- evidence requirements;
- verifier candidate when useful;
- result record shape;
- not-run reporting.

## Failure Modes

- task package has no verification plan;
- completion report is treated as evidence;
- planned work is marked done.

## Scoring

0 = no verification. 1 = generic verification only. 2 = concrete evidence and result-record plan.
