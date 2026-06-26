# Pal Install Task Package

## Boundary

Installation happens only after a staging review. PalSmith recommends and reviews. The current Agent Runtime copies approved files into the formal target after confirmation.

## Fields

- `task_id`:
- `task_name`: Pal Install Task Package
- `requested_by`:
- `owner_pal`: PalSmith
- `executing_runtime`: current Agent Runtime
- `user_goal`:
- `context_summary`: staged resource, classification, target Pal directory, conflict decision.
- `allowed_read_paths`: approved staging directory, staging report, quarantine report.
- `forbidden_read_paths`: unrelated private paths, unrelated Pal memory, credentials.
- `allowed_write_paths`: approved install target, approved quarantine/report paths.
- `forbidden_write_paths`: `contacts/`, `registry/`, unrelated Pal Packs, private memory folders unless explicitly approved.
- `required_exclusions`: `memory/user/`, `memory/project/`, `state/`, `reports/`, scripts, credentials, tokens, logs.
- `risk_checks`: overwrite risk, id conflict, resource type, quarantined files, public/private boundary.
- `user_confirmation_required`: yes, before installing or overwriting any file.
- `confirmation_questions`: install target, overwrite policy, quarantined-file handling, registration intent.
- `execution_steps_for_runtime`: snapshot target if needed, copy approved files, leave excluded files in quarantine, produce install report.
- `expected_outputs`: installed files, skipped files, quarantine list, install report.
- `verification_requirements`: parse installed `pal.json`, list overwrite/skipped/not-run checks.
- `final_report_format`: installed paths, quarantined paths, conflicts, registry/contacts next steps.

## PalSmith Acceptance

Accept only when installed content is a valid Pal Pack draft and risk files did not enter the public Pal target.
