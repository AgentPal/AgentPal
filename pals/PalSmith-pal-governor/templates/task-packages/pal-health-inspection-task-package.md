# Pal Health Inspection Task Package

## Boundary

Health inspection is read-first. PalSmith defines the checklist and reviews evidence. The current Agent Runtime reads approved files and may write only an approved report.

## Fields

- `task_id`:
- `task_name`: Pal Health Inspection Task Package
- `requested_by`:
- `owner_pal`: PalSmith
- `executing_runtime`: current Agent Runtime
- `user_goal`:
- `context_summary`: inspection scope, target Pals, registry/contacts check intent, report target.
- `allowed_read_paths`: `pals/`, `contacts/pals.json`, `registry/pal.index.json`, `agentpal.json`, selected Pal root files.
- `forbidden_read_paths`: private user files outside workspace, private memory content unless explicitly approved.
- `allowed_write_paths`: approved health report path only.
- `forbidden_write_paths`: Pal source files, `contacts/`, `registry/`, `memory/user/`, `memory/project/`, `state/`, `reports/` except approved report path.
- `required_exclusions`: private memory content from public reports, credentials, tokens, runtime logs.
- `risk_checks`: required root files, `pal.json` parse, collaboration flags, contacts/registry consistency, memory/state/reports boundary.
- `user_confirmation_required`: yes, if writing a report file; read-only summary may proceed within approved scope.
- `confirmation_questions`: inspection scope, report path, whether repair should be a separate follow-up task.
- `execution_steps_for_runtime`: read approved files, separate index-known from content-read, parse JSON, produce health report.
- `expected_outputs`: health report, risk list, suggested fixes, missing/not-run checks.
- `verification_requirements`: list content-read paths, JSON parse results, missing files, checks not performed.
- `final_report_format`: evidence, findings, risks, suggested task packages, not-run.

## PalSmith Acceptance

Accept only when the report avoids repair claims and separates read evidence from suggested fixes.
