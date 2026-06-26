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
- `context_summary`: team purpose, domain, expected members, owner/verifier needs, target workspace.
- `allowed_read_paths`: Pal Pack templates, Pal team examples, approved reference Pals.
- `forbidden_read_paths`: unrelated private memory, private project files, credentials, runtime state.
- `allowed_write_paths`: approved team directory and approved member Pal directories.
- `forbidden_write_paths`: `contacts/`, `registry/`, existing unrelated Pals, private memory/state/report directories without separate confirmation.
- `required_exclusions`: private memory, project memory, state, reports, logs, cache, credentials, executable files.
- `risk_checks`: duplicate Pal ids, overlapping roles, unclear owner/verifier, invalid collaboration mode, target conflicts.
- `user_confirmation_required`: yes, before creating team or member files.
- `confirmation_questions`: member count, member names, owner Pal, verifier Pal, target directories, registration intent.
- `execution_steps_for_runtime`: create member Pal drafts, shared workflow docs, Context Packet rules, and team creation report.
- `expected_outputs`: member list, directory plan, created files, team collaboration rules.
- `verification_requirements`: parse each `pal.json`, list created/missing files, report not-run checks.
- `final_report_format`: team summary, member table, created paths, risks, next registry/contacts package.

## PalSmith Acceptance

Accept only when every created member has an explicit boundary and runtime evidence exists for all claimed files.
