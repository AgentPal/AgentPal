# Clean Pal Export Task Package

## Boundary

Clean export is for public-safe sharing. PalSmith plans and reviews. The current Agent Runtime copies approved public files and creates manifest/report evidence.

## Fields

- `task_id`:
- `task_name`: Clean Pal Export Task Package
- `requested_by`:
- `owner_pal`: PalSmith
- `executing_runtime`: current Agent Runtime
- `user_goal`:
- `context_summary`: target Pal, export purpose, export location, public/private intent.
- `allowed_read_paths`: target Pal public files and approved license/readme files.
- `forbidden_read_paths`: unrelated Pals, private user files, private project folders, credentials.
- `allowed_write_paths`: approved export location only.
- `forbidden_write_paths`: source Pal mutation, `contacts/`, `registry/`, public release upload locations unless separately confirmed.
- `required_exclusions`: `memory/user/`, `memory/project/`, `state/`, `reports/`, logs, cache, credentials, tokens, executable files, private contacts history.
- `risk_checks`: private data, license, required root files, manifest completeness, export report completeness.
- `user_confirmation_required`: yes, before creating export files or archive.
- `confirmation_questions`: target Pal, export destination, sharing intent, whether archive creation is allowed.
- `execution_steps_for_runtime`: copy only public-safe files, generate `export-manifest.json`, generate `export-report.md`, list inclusions/exclusions.
- `expected_outputs`: clean export directory or archive, manifest, export report.
- `verification_requirements`: report included/excluded paths, confirm excluded private sections, mark not-run checks.
- `final_report_format`: clean export summary, included files, excluded files, privacy result, manifest path.

## PalSmith Acceptance

Accept only when private runtime data is excluded and the report explicitly mentions `memory/user/`, `memory/project/`, `state/`, and `reports/`.
