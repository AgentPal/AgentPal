# Pal Version Rollback Task Package

task_name: Pal Version Rollback Task Package
owner_pal: PalSmith
executing_runtime: current Agent Runtime

## Required Fields

- target Pal path
- rollback source
- files to restore
- files to remove
- overwrite risk
- current-state backup path
- confirmation question

## Confirmation

Rollback must not run without explicit user confirmation.

## Evidence

- before path list
- after path list
- changed files
- JSON parse result
- `done`, `missing`, and `not-run`
