# PalSmith Self Health Review Task Package

task_name: PalSmith Self Health Review Task Package
owner_pal: PalSmith
executing_runtime: current Agent Runtime

## User Goal

Inspect PalSmith itself for formal skill alignment, knowledge support, workflow support, eval coverage, no-code boundary, and content completeness.

## Allowed Reads

- `pals/PalSmith-pal-governor/pal.json`
- `skills/`
- `knowledge/`
- `workflows/`
- `core/`
- `templates/task-packages/`
- `examples/`
- `evals/`

## Verification Requirements

- formal skill files exist
- skill files contain required sections
- knowledge supports skill packages
- workflows/protocols support repeated behavior
- evals cover critical skills
- no placeholder markers
- no executable code or tool directory
- user material preservation protocol exists
- web research protocol exists

## Expected Output

PalSmith Self Health Report with dimension scores, remaining gaps, and next task packages.
