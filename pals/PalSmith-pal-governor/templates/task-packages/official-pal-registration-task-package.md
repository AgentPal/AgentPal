# Official Pal Registration Task Package

## Boundary

Official Pal registration is a controlled governance write. PalSmith prepares the registration plan, checks the target Pal boundary, asks confirmation questions, and reviews runtime evidence. The current Agent Runtime updates JSON files only after explicit user confirmation.

## Fields

- `task_id`:
- `task_name`: Official Pal Registration Task Package
- `requested_by`:
- `owner_pal`: PalSmith
- `executing_runtime`: current Agent Runtime
- `user_goal`: register a standard Pal Pack as an official Pal, registry item, and contacts item.
- `context_summary`: target Pal identity, target path, current agentpal/registry/contacts state, and any mismatch.
- `allowed_read_paths`: `agentpal.json`, `registry/pal.index.json`, `contacts/pals.json`, target `PAL.md`, target `pal.json`, target `SKILL.md`, target `AGENTS.md`.
- `forbidden_read_paths`: private memory, runtime state, unrelated Pal Packs, credentials, tokens, user-private project files.
- `allowed_write_paths`: `registry/pal.index.json`, `contacts/pals.json`, and `agentpal.json` when the workspace already has an official Pal list or capability reference.
- `forbidden_write_paths`: other Pal Pack files, ordinary Skill directories, private `memory/user/`, private `memory/project/`, `state/`, private `reports/`, and unrelated registry/contact records.
- `required_exclusions`: ordinary Skills, tools, models, plugins, raw repositories, Knowledge Packs, Persona Packs, private memory, runtime state, and executable tooling.
- `risk_checks`: standard Pal Pack shape, target path exists, `pal.json` parse, id/path consistency, duplicate registry entry, duplicate contacts entry, no-runtime-code boundary, contactability flags.
- `user_confirmation_required`: yes, before any JSON write.
- `confirmation_questions`: confirm official Pal registration, confirm contacts entry, confirm only the target Pal is changed, confirm no private memory/state/report write.
- `execution_steps_for_runtime`: inspect target files, prepare exact JSON diff, apply only approved target entry, parse changed JSON, report changed fields.
- `expected_outputs`: updated registry entry, contacts entry, optional agentpal official list update, JSON parse evidence, consistency report.
- `verification_requirements`: Pal appears in registry, Pal appears in contacts or a reason is recorded, agentpal official list is consistent, no duplicate id, no forbidden files added.
- `final_report_format`: fields changed, JSON parse result, consistency result, no-code boundary result, remaining risks.

## PalSmith Acceptance

Accept only when the registered item is a standard Pal Pack, all changed JSON parses successfully, id/path/direct call match the target `pal.json`, and no other Pal entries were rewritten.
