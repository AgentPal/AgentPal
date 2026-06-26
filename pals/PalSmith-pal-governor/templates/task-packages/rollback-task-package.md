# Rollback Task Package

## Boundary

Rollback overwrites or restores files and is high risk. PalSmith plans and reviews. The current Agent Runtime restores only after explicit confirmation.

## Fields

- `task_id`:
- `task_name`: rollback task package
- `requested_by`:
- `owner_pal`: PalSmith
- `executing_runtime`: current Agent Runtime
- `user_goal`:
- `context_summary`: snapshot source, current target, restore scope, overwrite decision.
- `allowed_read_paths`: approved snapshot, approved current target.
- `forbidden_read_paths`: unrelated private paths, unrelated Pal Packs, credentials, unapproved memory.
- `allowed_write_paths`: approved restore target after confirmation and approved pre-rollback backup path.
- `forbidden_write_paths`: unrelated Pal Packs, contacts/registry unless they are explicitly named restore targets, deletion outside restore scope.
- `required_exclusions`: forced overwrite without confirmation, unapproved private memory, credentials, tokens.
- `risk_checks`: snapshot compatibility, target overwrite, current-state backup, JSON parse after restore if JSON changed.
- `user_confirmation_required`: yes, explicit overwrite acknowledgement required.
- `confirmation_questions`: restore source, restore target, overwrite approval, pre-rollback backup destination.
- `execution_steps_for_runtime`: snapshot current target, restore approved files, parse JSON if applicable, produce rollback report.
- `expected_outputs`: pre-rollback snapshot, restored files, rollback report, parse evidence.
- `verification_requirements`: list restored paths, backup path, parse result, not-run checks.
- `final_report_format`: restored paths, backup path, parse result, remaining risks.

## PalSmith Acceptance

Accept only when pre-rollback backup evidence exists and no restore occurred outside confirmed paths.
