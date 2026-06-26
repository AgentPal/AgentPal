# Pal Runtime Call Verification Task Package

task_name: Pal Runtime Call Verification Task Package
owner_pal: PalSmith
executing_runtime: current Agent Runtime

## User Goal

Verify whether a Pal can be called by `/pal Name`.

## Levels

- Level 1: Static Resolution
- Level 2: Runtime Simulation
- Level 3: Native Runtime Call

## Required Evidence

- contacts entry
- registry entry
- `pal.json`
- `PAL.md`
- direct call string
- simulated or native response evidence
- verification level reached
- `not-run` for unavailable levels

## Boundary

Do not claim Level 3 unless the current runtime actually supports and executes a native `/pal` call.
