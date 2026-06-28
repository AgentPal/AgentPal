# Business System Profile Change Review Note

review_note_id:

business_system_id:

organization_profile_ref:

source_change_ledger_ref:

review_reason:

ledger_entries_under_review:

next_review_date_status:

unknowns_still_open:

not_run_checks_still_open:

missing_evidence_still_open:

second_verification_status:

recommended_manual_actions:

blocked_items:

decision:

decision_by:

decision_date:

recorded_by:

recorded_at:

forbidden_actions:

- Do not modify central Pal roster.
- Do not write to external project `.agentpal/`.
- Do not store credentials.
- Do not create connector.
- Do not auto-call external APIs.
- Do not keyword-route.
- Do not convert not-run into pass.
- Do not hide missing evidence.
- Do not treat next_review_date as scheduled automation.

## Status Options

- `manual_review_required`
- `blocked_missing_evidence`
- `needs_second_verification`
- `review_completed_no_change`
- `superseded_by_later_review`

## Boundary

This change review note records a manual review of Change Ledger entries. It is not scheduled automation, not a reminder system, not a writeback engine, not a scanner, not a validator, not a connector, and not an API client.

Recommended manual actions are suggestions only. If second verification did not run, keep it as `not-run`. If evidence is missing, keep it as `missing`. If `next_review_date` is due, record that manual review is required; do not schedule or execute anything automatically.
