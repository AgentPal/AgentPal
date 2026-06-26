# Pal Creation Task Package

## Boundary

PalSmith owns the plan, questions, job model, risk checks, and acceptance review. PalSmith does not directly create files. The executor is the current Agent Runtime after user confirmation.

## Fields

- `task_id`:
- `task_name`: Pal Creation Task Package
- `requested_by`:
- `owner_pal`: PalSmith
- `executing_runtime`: current Agent Runtime
- `user_goal`:
- `pal_name`:
- `pal_id`:
- `role`:
- `responsibilities`:
- `not_responsible_for`:
- `usage_scenarios`:
- `job_expertise_model`: required knowledge, skills, workflows, templates, evals, and risks
- `suggested_user_uploads`:
- `suggested_web_research`:
- `context_summary`: requested Pal identity, role, language, target workspace, approved user materials, research status, and approved reference Pals.
- `allowed_read_paths`: Pal Pack templates, Pal Pack standard docs, approved reference Pal Packs, approved user materials, approved research reports.
- `forbidden_read_paths`: unrelated private Pal memory, external private directories, credentials, tokens, runtime-private logs.
- `allowed_write_paths`: approved new `pals/<Pal-Directory>/` target only.
- `forbidden_write_paths`: `contacts/`, `registry/`, existing Pal directories, `memory/user/`, `memory/project/`, `state/`, `reports/` unless a separate package confirms them.
- `required_exclusions`: private memory, project memory, state, reports, cache, logs, credentials, tokens, executable files.
- `risk_checks`: duplicate id, duplicate directory, invalid Pal Pack shape, public/private boundary, ordinary Skill accidentally treated as Pal, expertise gaps, over-compressed material.
- `user_confirmation_required`: yes, before creating any files.
- `confirmation_questions`: exact Pal name, id, target directory, language, responsibilities, user material handling, research status, and whether registry/contacts suggestions are drafts.
- `execution_steps_for_runtime`: create root files, output contract, skill files, knowledge files, workflow/runbook files, evals, examples, placeholders, and creation report.
- `expected_outputs`: job-capable Pal Pack draft plus creation report if requested.
- `verification_requirements`: list created paths, parse `pal.json`, report skipped/missing/not-run checks, run Pal Job Fitness Report.
- `final_report_format`: files created, files skipped, missing expertise assets, risks, next suggested task packages.

## PalSmith Acceptance

Accept only when runtime evidence shows a standard Pal Pack draft with role model, knowledge, skills, workflows, evals, no unconfirmed registry/contact write, and no private memory copied into public files.
