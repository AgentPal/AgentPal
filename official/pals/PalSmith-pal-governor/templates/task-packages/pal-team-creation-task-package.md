# Pal Team Creation Task Package

## Boundary

PalSmith designs the team and task package. The current Agent Runtime creates files only after explicit confirmation.

## Fields

- `task_id`:
- `task_name`: Pal Team Creation Task Package
- `requested_by`:
- `owner_pal`: PalSmith
- `executing_runtime`: current Agent Runtime
- `user_goal`:
- `team_pack_discovery_result`: candidate Team Packs checked, selected_team if fitting, reuse / no-fit rationale, and open_roles gaps.
- `context_summary`: team purpose, domain, expected members, owner/verifier needs, target workspace.
- `allowed_read_paths`: Pal Pack templates, Pal team examples, approved reference Pals.
- `forbidden_read_paths`: unrelated private memory, private project files, credentials, runtime state.
- `allowed_write_paths`: approved team directory and approved member Pal directories.
- `forbidden_write_paths`: `contacts/`, `registry/`, existing unrelated Pals, private memory/state/report directories without separate confirmation.
- `required_exclusions`: private memory, project memory, state, reports, logs, cache, credentials, executable files.
- `risk_checks`: duplicate Pal ids, overlapping roles, unclear owner/verifier, invalid collaboration mode, target conflicts.
- `user_confirmation_required`: yes, before creating team or member files.
- `confirmation_questions`: existing member Pal ids, open roles, owner Pal, verifier Pal, target directories, registration intent, and whether any optional new Pal proposal is approved.
- `execution_steps_for_runtime`: create or update Team Pack assets, shared workflow docs, Context Packet rules, and team creation report. Do not create member Pal drafts unless the user separately confirms a specific optional new Pal proposal.
- `expected_outputs`: selected_team reuse plan or no-fit creation rationale, existing member references, open roles, optional new Pal proposals, directory plan, created files, team collaboration rules, Workflow Execution Contract, and Closure Gate.
- `verification_requirements`: parse each `pal.json`, list created/missing files, report not-run checks.
- `final_report_format`: team summary, member table, created paths, risks, next registry/contacts package.

## PalSmith Acceptance

Accept only when every roster member references an existing or user-confirmed Pal, every missing capability is represented as an open role, and runtime evidence exists for all claimed files.
