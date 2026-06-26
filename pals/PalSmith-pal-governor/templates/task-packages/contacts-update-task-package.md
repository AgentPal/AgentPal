# Contacts Update Task Package

## Boundary

Contacts update is a controlled write. PalSmith checks contact eligibility and proposes a JSON diff. The current Agent Runtime writes only after exact confirmation.

## Fields

- `task_id`:
- `task_name`: contacts update task package
- `requested_by`:
- `owner_pal`: PalSmith
- `executing_runtime`: current Agent Runtime
- `user_goal`:
- `context_summary`: target Pal, contactability flags, proposed contacts diff.
- `allowed_read_paths`: target Pal root files, `contacts/pals.json`, optional registry entry.
- `forbidden_read_paths`: unrelated private memory, credentials, raw user project files.
- `allowed_write_paths`: `contacts/pals.json` after exact diff confirmation; approved snapshot path.
- `forbidden_write_paths`: `registry/`, Pal source files, unrelated contacts files.
- `required_exclusions`: ordinary Skills, tools, models, plugins, Knowledge Packs, Persona Packs, raw repositories, private memory.
- `risk_checks`: standard Pal Pack, discoverable, contactable, collaboration enabled, allowed modes, duplicate alias.
- `user_confirmation_required`: yes, exact diff approval required.
- `confirmation_questions`: approve this exact contacts diff, confirm allowed modes, confirm direct call and aliases.
- `execution_steps_for_runtime`: snapshot current contacts, apply approved diff, parse JSON, report diff and parse result.
- `expected_outputs`: snapshot evidence, updated `contacts/pals.json`, parse result.
- `verification_requirements`: show changed contact entry, JSON parse result, not-run checks.
- `final_report_format`: contact eligibility, diff summary, snapshot path, parse result.

## PalSmith Acceptance

Accept only when the resource is a contactable standard Pal Pack. Ordinary Skills and support resources must not enter contacts.
