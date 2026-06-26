# Pal Readiness Review Task Package Template

Status: PalSmith v0.4 template.

This template is no-code. PalSmith prepares it; the current Agent Runtime performs only approved reads or writes and returns evidence.

## Fields

- `task_id`: `palsmith-readiness-review-<target>`
- `task_name`: `Pal Readiness Review Task Package`
- `owner_pal`: `PalSmith`
- `executing_runtime`: current Agent Runtime
- `user_goal`: determine whether a Pal or team is `idea`, `draft`, `testing`, `stable`, `publish-ready`, `published`, `deprecated`, or `archived`
- `target_pal_or_team`: path, id, or user-described target
- `requested_state`: optional state the user wants to validate
- `allowed_read_paths`: target public Pal files, registry / contacts when relevant, eval files, export reports if approved
- `forbidden_read_paths`: private memory, private project state, credentials, logs, unrelated Pals, unapproved source directories
- `allowed_write_paths`: optional report path only after confirmation
- `forbidden_write_paths`: Pal source files, registry, contacts, release files, tags, remotes, package archives unless separately confirmed
- `matrix_dimensions`: Structure Completeness, Identity Consistency, Responsibility Clarity, Skill / Knowledge Coverage, Workflow Readiness, Eval Coverage, Registry / Contacts Consistency, Memory / State / Reports Safety, Collaboration Safety, Runtime Task Package Readiness, Clean Export Safety, With Memory Export Risk, Team Governance Readiness
- `user_confirmation_required`: yes for writes, private reads, registry / contacts checks beyond read-only inspection, or status changes
- `confirmation_questions`: exact questions before Runtime action
- `execution_steps_for_runtime`: bounded read/report steps
- `verification_requirements`: JSON parse if JSON is read, link/path evidence, `missing`, `not-run`, no-code boundary if publish-ready is requested
- `final_report_format`: readiness table, recommended state, blockers, next task package

## Runtime Steps

1. Read only the approved target files.
2. Parse approved JSON files if present.
3. Check each matrix dimension from available evidence.
4. Report `not-run` for any unchecked dimension.
5. Do not change lifecycle or publish status.
6. Write a report only if the user confirmed a report path.

## PalSmith Acceptance Criteria

- recommended state is supported by evidence
- no publish-ready claim without clean export and public-safety evidence
- no `published` claim without actual publication evidence
- no private memory read unless explicitly approved
- no registry / contacts write
- `missing` and `not-run` are preserved
