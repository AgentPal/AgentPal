# Business System Profile Audit Trail Index

## Purpose

An audit trail index summarizes review packets, evidence packs, replay records, rollback records, and second verification results.

It is not an execution system.

The index is a no-code governance artifact. It records where related Business System Profile review materials live, what their current statuses are, what remains unknown, which checks did not run, which evidence is missing, and which manual actions may be considered next. It must not execute writeback, automatically call external APIs, close missing evidence, modify central contacts, create connectors, store credentials, write into external project `.agentpal/`, or route by keywords.

## Inputs

- organization profile ref
- review packet refs
- manual update evidence pack refs
- manual writeback replay refs
- rollback record refs
- second verification refs
- risk notes
- open questions
- missing evidence

## Required Fields

| Field | Meaning |
| --- | --- |
| `audit_trail_id` | Stable public-safe audit trail id. |
| `business_system_id` | Business System id from the organization profile. |
| `organization_profile_ref` | Organization Business System Profile or public-safe example being indexed. |
| `related_project_ids` | Project ids that produced review, evidence, or replay records. |
| `review_records` | Review packet refs, statuses, and narrow summaries. |
| `evidence_packs` | Manual update evidence pack refs, statuses, and evidence summaries. |
| `replay_records` | Manual writeback replay record refs, statuses, and changed-field summaries. |
| `rollback_records` | Rollback record refs or summaries, usually inside replay records. |
| `second_verification_records` | Second verification refs, statuses, evidence, and not-run / missing notes. |
| `current_profile_status_summary` | Current public-safe profile status summary; not an automatic profile update. |
| `open_unknowns` | Facts that remain unknown and must not be invented. |
| `not_run_checks` | Checks that did not run and must not be reported as pass. |
| `missing_evidence` | Evidence required but absent. |
| `risk_notes` | Privacy, permission, credential, routing, external-write, and scope risks. |
| `next_manual_actions` | Suggested human actions only; not automatic execution. |
| `last_reviewed_by` | Person, Pal, or host Runtime summary that last reviewed the index. |
| `last_reviewed_at` | Review date or `unknown`. |
| `status` | Current index status. |

## Allowed Statuses

- `active`
- `archived`
- `blocked_missing_evidence`
- `needs_user_confirmation`
- `needs_runtime_evidence`
- `manual_review_required`
- `second_verification_required`

## Forbidden Behavior

- `auto_writeback_organization_profile`
- `auto_modify_central_roster`
- `auto_create_connector`
- `auto_call_external_api`
- `store_credentials`
- `keyword_route`
- `write_to_external_project_agentpal`
- `hide_missing_evidence`
- `convert_not_run_to_pass`

## Index Boundary

Audit Trail Index only summarizes. It does not execute.

It may point to review packets, manual update evidence packs, manual writeback replay records, rollback records, second verification records, and organization profile refs. Pointing to those records does not update organization truth by itself.

## Status Boundary

An index status is a review aid. It does not automatically change the organization Business System Profile.

If a status says `active`, `manual_review_required`, or `second_verification_required`, that status records the index state only. It must not be treated as permission to write profile fields, modify central contacts, call external systems, or close missing evidence.

## Manual Action Boundary

`next_manual_actions` are suggestions only.

They can say things like:

- ask the user whether to run second verification
- request host Runtime evidence if the user approves
- review whether missing evidence blocks the audit trail
- prepare a manual update or rollback note for user approval

They must not execute automatically, call external APIs, create connectors, update organization profiles, update central contacts, or write to external project `.agentpal/`.

## Evidence Boundary

`not-run` is not pass. Missing evidence is not completion.

not-run is not pass.

Do not say `verified`, `complete`, `closed`, or `passed` when evidence is absent, stale, indirect, not inspected, or not run.

The index must preserve:

- open unknowns as `unknown`
- not-run checks as `not-run`
- missing evidence as `missing`
- blocked status as blocked until evidence or user confirmation is reviewed

## Organization Profile Boundary

Audit Trail Index records may reference organization-level Business System Profiles under:

```text
workspace/organization/capability-inventory/business-systems/
```

The index must not update:

```text
workspace/organization/contacts/pals.json
workspace/organization/contacts/PAL_CONTACTS.md
external-project/.agentpal/
```

## Credential Boundary

Audit Trail Index records must not store real credentials, private tokens, passwords, API keys, cookies, integration secrets, private workspace ids, customer exports, or session values.

If an underlying evidence pack or replay record depends on authenticated host Runtime evidence, the index may record only a public-safe summary or path reference. Do not paste credential values.

## External Project Boundary

External user projects remain thin-bound. Do not write audit trail indexes into external project `.agentpal/audit-trail/`, `.agentpal/replay/`, `.agentpal/rollback/`, `.agentpal/verification/`, `.agentpal/evidence/`, `.agentpal/reviews/`, `.agentpal/business-systems/`, `.agentpal/capability-inventory/`, `.agentpal/memory/`, `.agentpal/reports/`, or `.agentpal/state/` by default.

Organization-level audit trail indexes belong in the AgentPal Workspace when explicitly maintained, not in the external project binding directory.

## Routing Boundary

Business System Profiles, Review Packets, Evidence Packs, Replay Records, and Audit Trail Indexes are AI judgement inputs only. They must not become:

- `keyword_map`
- `domain_map`
- `role_map`
- deterministic task-to-Pal routing
- deterministic task-to-runtime routing
- deterministic system-type-to-tool routing

Explicit `/pal Name` or `@Name` remains user intent, not keyword routing.
