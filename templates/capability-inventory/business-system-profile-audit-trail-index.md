# Business System Profile Audit Trail Index

audit_trail_id:

business_system_id:

organization_profile_ref:

related_project_ids:

review_records:

evidence_packs:

replay_records:

rollback_records:

second_verification_records:

current_profile_status_summary:

open_unknowns:

not_run_checks:

missing_evidence:

risk_notes:

next_manual_actions:

last_reviewed_by:

last_reviewed_at:

status:

forbidden_actions:

- Do not modify central Pal roster.
- Do not write to external project .agentpal/.
- Do not store credentials.
- Do not create connector.
- Do not keyword-route.
- Do not auto-call external APIs.
- Do not convert not-run into pass.
- Do not hide missing evidence.
- Do not use this index as an execution engine.

## Status Options

- `active`
- `archived`
- `blocked_missing_evidence`
- `needs_user_confirmation`
- `needs_runtime_evidence`
- `manual_review_required`
- `second_verification_required`

## Boundary

This audit trail index summarizes review packets, manual update evidence packs, manual writeback replay records, rollback records, and second verification records. It does not execute actions, does not automatically update organization profiles, does not automatically close missing evidence, does not update central Pal contacts, does not create a connector or API client, does not store credentials, does not route by keywords, and does not write audit trail records into an external project `.agentpal/` directory by default.

`next_manual_actions` are suggestions only. If a check did not run, keep it as `not-run`. If evidence is missing, keep it as `missing`.
