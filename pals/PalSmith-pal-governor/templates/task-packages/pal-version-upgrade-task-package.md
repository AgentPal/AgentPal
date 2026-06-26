# Pal Version Upgrade Task Package

task_name: Pal Version Upgrade Task Package
owner_pal: PalSmith
executing_runtime: current Agent Runtime

## Required Fields

- target Pal path
- current version / state
- proposed version / state
- change proposal
- affected files
- risk level
- breaking change: yes/no
- eval required: yes/no
- snapshot required: yes/no
- rollback plan required: yes/no

## Confirmation

User must confirm the exact version/state change and affected files before Runtime writes.

## Evidence

- changed files
- JSON parse result
- eval result or `not-run`
- rollback readiness
