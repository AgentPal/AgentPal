# Business System Profile Change Review Note

## Purpose

A Change Review / Periodic Reconciliation Note records a manual review of Business System Profile Change Ledger entries.

It is a human review note, not scheduled automation.

The note is used when one or more ledger entries need periodic reconciliation, when `next_review_date` has arrived or needs human attention, or when retained unknowns, missing evidence, not-run checks, or second verification status must be reviewed without changing organization truth.

It must not execute writeback, automatically update an organization profile, modify central contacts, close missing evidence, convert not-run to pass, call external APIs, create connectors, store credentials, write into an external project `.agentpal/change-review/`, schedule tasks, or route by keywords.

## Inputs

- source change ledger
- ledger entries under review
- current organization profile snapshot summary
- retained unknowns
- retained not-run checks
- retained missing evidence
- second verification status
- next review date status
- prior governance decision or rollback reference when relevant

## Required Fields

| Field | Meaning |
| --- | --- |
| `review_note_id` | Stable public-safe id for the review note. |
| `business_system_id` | Business System id from the organization profile. |
| `organization_profile_ref` | Organization Business System Profile or public-safe example being reviewed. |
| `source_change_ledger_ref` | Change ledger that triggered or informed this review. |
| `review_reason` | Why the manual review is being recorded. |
| `ledger_entries_under_review` | Ledger entry ids or summaries under review. |
| `next_review_date_status` | Whether next review date is due, not-set, future, or manually reviewed. |
| `unknowns_still_open` | Unknown facts still open after review. |
| `not_run_checks_still_open` | Checks still not-run after review. |
| `missing_evidence_still_open` | Evidence still missing after review. |
| `second_verification_status` | Status of second verification. |
| `recommended_manual_actions` | Human-only suggestions for next review steps. |
| `blocked_items` | Items blocked by missing evidence, not-run checks, or unresolved risk. |
| `decision` | Manual review decision status. |
| `decision_by` | Human, maintainer, or governance reviewer responsible for the decision. |
| `decision_date` | Decision date or `unknown`. |
| `recorded_by` | Person, Pal, or host Runtime summary that recorded the note. |
| `recorded_at` | Record creation date or `unknown`. |

## Allowed Statuses

- `manual_review_required`
- `blocked_missing_evidence`
- `needs_second_verification`
- `review_completed_no_change`
- `superseded_by_later_review`

## Forbidden Behavior

- `auto_update_organization_profile`
- `auto_modify_central_roster`
- `auto_close_missing_evidence`
- `convert_not_run_to_pass`
- `auto_call_external_api`
- `auto_create_connector`
- `store_credentials`
- `keyword_route`
- `write_to_external_project_change_review`
- `treat_next_review_date_as_scheduled_automation`

## Review Boundary

Change Review Notes only record manual review and reconciliation. They do not execute review, schedule review, run verification, write profiles, or close evidence.

If `next_review_date` is due, the note may say manual review is required. It must not create an automatic reminder, background task, calendar item, monitor, scanner, validator, daemon, connector, workflow, or auto-review trigger.

## Evidence Boundary

Unknown, not-run, and missing states must remain visible until reviewable evidence exists.

Do not convert:

- `unknown` to available
- `not-run` to pass
- missing evidence to complete
- recommended manual action to completed action
- due review date to automatic execution

If second verification did not run, keep `second_verification_status` as `second_verification_not_run` or `needs_second_verification`.

## Organization Profile Boundary

Change Review Notes may recommend manual review of organization-level Business System Profiles, but they must not update:

```text
workspace/organization/capability-inventory/
workspace/organization/contacts/pals.json
workspace/organization/contacts/PAL_CONTACTS.md
external-project/.agentpal/
```

They cannot change Pal roster, Pal replacement, Pal activation, routing policy, or organization truth by themselves.

## External Project Boundary

External user projects remain thin-bound. Do not write change review notes into external project `.agentpal/change-review/`, `.agentpal/change-ledger/`, `.agentpal/governance-decisions/`, `.agentpal/audit-trail/`, `.agentpal/replay/`, `.agentpal/verification/`, `.agentpal/evidence/`, `.agentpal/reviews/`, `.agentpal/business-systems/`, `.agentpal/capability-inventory/`, `.agentpal/memory/`, `.agentpal/reports/`, or `.agentpal/state/` by default.

Organization-level review notes belong in the AgentPal Workspace when explicitly maintained, not in the external project binding directory.

## Routing Boundary

Business System Profiles, Review Packets, Evidence Packs, Replay Records, Audit Trail Indexes, Governance Decision Records, Change Ledgers, and Change Review Notes are AI judgement inputs only. They must not become:

- `keyword_map`
- `domain_map`
- `role_map`
- deterministic task-to-Pal routing
- deterministic task-to-runtime routing
- deterministic system-type-to-tool routing

Explicit `/pal Name` or `@Name` remains user intent, not keyword routing.
