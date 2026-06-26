# Pal Import Staging Task Package

## Boundary

All imports are untrusted by default. PalSmith prepares staging instructions. The current Agent Runtime may copy, download, or extract into staging only after confirmation and must not execute imported files.

## Fields

- `task_id`:
- `task_name`: Pal Import Staging Task Package
- `requested_by`:
- `owner_pal`: PalSmith
- `executing_runtime`: current Agent Runtime
- `user_goal`:
- `context_summary`: source type, source path or URL, intended import purpose, staging target.
- `allowed_read_paths`: approved source URL, approved local source, import protocol, staging policy.
- `forbidden_read_paths`: unrelated local private paths, unrelated Pals, credentials, tokens, private memory not explicitly approved.
- `allowed_write_paths`: approved staging path and approved quarantine/report path.
- `forbidden_write_paths`: formal `pals/`, `contacts/`, `registry/`, existing Pal directories.
- `required_exclusions`: script execution, automatic installation, private memory import to public Pal Pack, credentials, tokens.
- `risk_checks`: resource type, required root files, license, scripts, private memory, `state/`, `reports/`, id conflicts, path traversal risk.
- `user_confirmation_required`: yes, before network access, local copy, extraction, or staging writes.
- `confirmation_questions`: source trust level, staging path, whether memory read is allowed, whether this is evaluation only.
- `execution_steps_for_runtime`: stage source, list files, quarantine risky files, produce import risk report, do not run scripts.
- `expected_outputs`: staged path, file inventory, quarantine list, risk report.
- `verification_requirements`: evidence that no imported script ran, list staged files, mark missing/not-run checks.
- `final_report_format`: source, staging path, classification, risks, install recommendation.

## PalSmith Acceptance

Accept staging only when risky files are reported, scripts are not executed, and formal install/registry/contacts writes remain separate.
