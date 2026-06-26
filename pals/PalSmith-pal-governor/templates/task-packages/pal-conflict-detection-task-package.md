# Pal Conflict Detection Task Package

task_name: Pal Conflict Detection Task Package
owner_pal: PalSmith
executing_runtime: current Agent Runtime

## User Goal

Find conflicts across selected Pals, a Pal team, or the current contacts / registry.

## Allowed Reads

- selected Pal root files and `pal.json`
- selected team `TEAM.md` and `team.json`
- `contacts/pals.json`
- `registry/pal.index.json`

## Verification Requirements

- detect id collisions
- detect direct call / alias collisions
- compare responsibilities and non-responsibilities
- check owner / verifier presence
- verify ordinary Skills are not contacts

## Expected Output

`Conflict Report` with severity, evidence, recommendation, and user-decision fields.

## Write Boundary

No writes. Any registry, contacts, or Pal file change requires a separate confirmed task package.
