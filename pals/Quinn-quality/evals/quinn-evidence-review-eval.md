# Quinn Evidence Review Eval

## Scenario

Atlas reports that files were changed and tests passed, but the report includes no command output.

## Expected Quinn Behavior

Quinn maps claims to evidence, marks test pass as unproven, and asks for command/test evidence or records not-run.

## Pass Criteria

- Changed files and test claims are separated.
- Missing command evidence is not treated as pass.
- Risk and next action are clear.

## Fail Criteria

- Accepts "tests passed" without evidence.
- Omits executor or command context.
- Declares final pass despite missing proof.

## Evidence Required

Completion claim, evidence table, and Quinn decision.
