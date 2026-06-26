# Pal Eval Lab Task Package

task_name: Pal Eval Lab Task Package
owner_pal: PalSmith
executing_runtime: current Agent Runtime

## User Goal

Generate and optionally run Markdown eval cases for a Pal.

## Required Eval Cases

- identity consistency
- responsibility boundary
- non-responsibility
- risky request
- output format
- collaboration request
- import / export safety
- registry / contacts consistency

## Allowed Reads

- target Pal public files
- contacts / registry when consistency is requested

## Expected Output

- eval file path
- pass/fail table
- files needing changes
- recommended lifecycle state
- `not-run` items
