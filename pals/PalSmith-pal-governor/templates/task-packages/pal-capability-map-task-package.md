# Pal Capability Map Task Package

task_name: Pal Capability Map Task Package
owner_pal: PalSmith
executing_runtime: current Agent Runtime

## User Goal

Generate a Markdown capability map for selected Pals or a Pal team.

## Allowed Reads

- selected `PAL.md`, `pal.json`, `skills/index.md`, `knowledge/index.md`, and `workflows/index.md`
- contacts / registry when global capability visibility is requested

## Expected Output

- Markdown table: Pal x role x skills x knowledge x workflows x collaboration modes x release safety
- capability gaps
- overlap notes
- next suggested PalSmith action

## Write Boundary

Read-only unless the user separately confirms a report file write.
