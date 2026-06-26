# Registry Update Task Package

## Boundary

Registry update is a controlled write. PalSmith proposes the JSON diff. The current Agent Runtime writes only the approved diff after confirmation.

## Fields

- `task_id`:
- `task_name`: registry update task package
- `requested_by`:
- `owner_pal`: PalSmith
- `executing_runtime`: current Agent Runtime
- `user_goal`:
- `context_summary`: target Pal, current registry entry state, proposed diff.
- `allowed_read_paths`: target Pal root files, `registry/pal.index.json`, optional current snapshot path.
- `forbidden_read_paths`: unrelated private memory, unapproved project files, credentials.
- `allowed_write_paths`: `registry/pal.index.json` after exact diff confirmation; approved snapshot path.
- `forbidden_write_paths`: `contacts/`, Pal source files, unrelated JSON files.
- `required_exclusions`: ordinary Skills, tools, models, plugins, Knowledge Packs, Persona Packs, raw repositories, private memory.
- `risk_checks`: standard Pal Pack validity, id conflict, path conflict, duplicate aliases, JSON structure.
- `user_confirmation_required`: yes, exact diff approval required.
- `confirmation_questions`: approve this exact registry diff, approve snapshot path, confirm target Pal identity.
- `execution_steps_for_runtime`: snapshot current registry, apply approved diff, parse JSON, report diff and parse result.
- `expected_outputs`: snapshot evidence, updated `registry/pal.index.json`, parse result.
- `verification_requirements`: show changed entry summary, JSON parse success/failure, not-run checks.
- `final_report_format`: diff summary, snapshot path, parse result, remaining contacts package if needed.

## PalSmith Acceptance

Accept only when the target is a standard Pal Pack and no ordinary Skill or raw resource enters registry as a Pal.
