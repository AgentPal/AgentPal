# Pal Publish Quality Gate Task Package

task_name: Pal Publish Quality Gate Task Package
owner_pal: PalSmith
executing_runtime: current Agent Runtime

## User Goal

Check whether a Pal or Pal team can move toward testing, stable, or publish-ready.

## Allowed Reads

- target Pal / team public files
- registry and contacts when consistency is in scope
- export manifest or export report when present

## Required Checks

- structure completeness
- identity and responsibility clarity
- no private memory / state / private reports in public content
- no-code boundary
- contacts / registry consistency
- Clean Export safety
- With Memory Export confirmation boundary
- Eval Lab result or `not-run`
- conflict detection result for teams

## Expected Output

`Publish Quality Gate Report` with recommended status, must-fix, should-fix, acceptable risks, user confirmations, and evidence.
