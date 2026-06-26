# Snapshot Task Package

## Boundary

Snapshot protects current state before controlled changes. PalSmith plans the scope and manifest. The current Agent Runtime creates the snapshot after confirmation.

## Fields

- `task_id`:
- `task_name`: snapshot task package
- `requested_by`:
- `owner_pal`: PalSmith
- `executing_runtime`: current Agent Runtime
- `user_goal`:
- `context_summary`: target paths, change reason, snapshot destination, restore expectation.
- `allowed_read_paths`: approved target files/directories.
- `forbidden_read_paths`: unrelated private paths, credentials, unapproved memory.
- `allowed_write_paths`: approved snapshot location and snapshot manifest path.
- `forbidden_write_paths`: source mutation, unrelated Pal Packs, public export location unless confirmed.
- `required_exclusions`: none for private backup unless user requests clean snapshot; clean snapshot excludes memory/state/reports/private data.
- `risk_checks`: target size, private data, restore path, overwrite risk, manifest completeness.
- `user_confirmation_required`: yes, before creating snapshot files.
- `confirmation_questions`: source paths, snapshot destination, clean or private snapshot, restore target expectation.
- `execution_steps_for_runtime`: copy or archive approved target, generate snapshot manifest, produce restore instructions.
- `expected_outputs`: snapshot copy/archive, snapshot manifest, restore instructions.
- `verification_requirements`: list snapshotted paths, evidence path, manifest fields, not-run checks.
- `final_report_format`: source, snapshot path, manifest path, restore note, risks.

## PalSmith Acceptance

Accept only when snapshot evidence and restore instructions are present.
