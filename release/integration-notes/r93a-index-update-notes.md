# R93-A Index Update Notes

This file records shared-entry updates that should be integrated after parallel R93 threads are reconciled.

R93-A intentionally did not modify shared entry files such as:

- `README.md`
- `RESOURCE_INDEX.md`
- `agentpal.json`
- `docs/00-overview/capability-inventory-navigation.md`
- `docs/03-user-guides/manual-capability-profile.md`
- `docs/03-user-guides/project-usage-memory-boundary.md`

## Suggested Additions

Add Change Review / Periodic Reconciliation Note references to the shared navigation surfaces:

- standard: `standards/capability-inventory/business-system-profile-change-review-note.md`
- template: `templates/capability-inventory/business-system-profile-change-review-note.md`
- example: `examples/capability-inventory/business-system-profile-reviews/notion-read-access-change-review-note.example.md`
- eval: `evals/palbench/capability-inventory/r93a-business-system-profile-change-review-note-boundary.md`
- validation: `release/fresh-clone-checks/r93a-local-business-system-profile-change-review-note-validation.md`

Suggested `agentpal.json` metadata after integration:

- `business_system_profile_change_review_note_standard`
- `business_system_profile_change_review_note_template`
- `business_system_profile_change_review_note_examples`
- `business_system_profile_change_review_note_notion_read_access_example`
- `business_system_profile_change_review_note_eval`
- `change_review_note_executes_writeback: false`
- `change_review_note_can_modify_central_roster: false`
- `change_review_note_can_write_external_project_agentpal_by_default: false`
- `change_review_note_can_auto_call_external_api: false`
- `change_review_note_can_auto_close_missing_evidence: false`
- `change_review_note_next_review_is_scheduled_automation: false`
- `change_review_note_requires_manual_review: true`

Suggested thin-binding forbidden directory addition after integration:

- `.agentpal/change-review`

## Boundary Notes

Change Review Notes are manual review records only. They are not scheduled automation, automatic reminders, scanners, validators, writeback engines, connectors, API clients, central roster updates, or keyword routes.
