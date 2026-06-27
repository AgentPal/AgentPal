# Project Usage Memory Boundary

Project usage memory records what happened in one project.

It is not organization truth.

It may suggest a future organization-level review.

It must not silently update organization capability profiles.

It must not update the central Pal roster.

It must not update no-keyword-routing policy.

It must not be copied into external project `.agentpal/` by default.

## Correct Use

Project usage memory can record project-specific evidence such as:

- a check that was not run
- a missing confirmation
- a host Runtime result for one project
- a project-specific limitation
- a recommendation to review an organization profile later

It cannot certify global access, global write permission, global API access, or central Pal ownership.

## Example

Good:

```text
In content-ops-demo, Notion write permission check was not-run.
```

Bad:

```text
Therefore Notion write access is available globally.
```

Correct:

```text
Record project-level not-run. If user later confirms access, propose an organization profile review.
```

## Organization Profile Review

When project usage memory suggests a Business System capability may be available, create a review packet instead of updating organization truth directly.

Use:

```text
standards/capability-inventory/business-system-profile-review-flow.md
templates/capability-inventory/business-system-profile-review-packet.md
```

The review packet can recommend a manual organization profile update. It must not auto-update `workspace/organization/capability-inventory/`, modify `workspace/organization/contacts/pals.json`, write into an external project `.agentpal/reviews/`, create a connector, store credentials, or route by keywords.

If a review packet is approved as `approved_for_manual_update`, create a Manual Update Evidence Pack before any profile edit:

```text
standards/capability-inventory/business-system-profile-manual-update-evidence-pack.md
templates/capability-inventory/business-system-profile-manual-update-evidence-pack.md
```

The evidence pack records the approved change, evidence summary, user confirmation, host Runtime evidence, rollback note, manual writeback target, and second verification status. It still must not auto-update the organization profile, modify central contacts, create a connector, store credentials, route by keywords, or write into an external project `.agentpal/evidence/`.

If a manual writeback has already happened, create a Manual Writeback Replay Record to audit the completed action:

```text
standards/capability-inventory/business-system-profile-manual-writeback-replay-record.md
templates/capability-inventory/business-system-profile-manual-writeback-replay-record.md
```

The replay record logs changed fields, previous and updated profile snapshot summaries, rollback record, second verification status, not-run checks, and missing evidence. It still must not execute writeback, auto-rollback, modify central contacts, create a connector, store credentials, route by keywords, or write into external project `.agentpal/replay/`, `.agentpal/rollback/`, or `.agentpal/verification/`.

When several review packets, evidence packs, replay records, rollback records, or second verification records exist, create an Audit Trail Index to summarize the chain:

```text
standards/capability-inventory/business-system-profile-audit-trail-index.md
templates/capability-inventory/business-system-profile-audit-trail-index.md
```

The audit trail index records related paths, statuses, current profile status summary, open unknowns, not-run checks, missing evidence, risks, and next manual action suggestions. It still must not execute actions, auto-call external APIs, auto-close missing evidence, modify central contacts, create a connector, store credentials, route by keywords, or write into external project `.agentpal/audit-trail/`.

## Boundary Checklist

- Keep project usage memory under the central project record.
- Keep external project `.agentpal/` thin by default.
- Do not update `workspace/organization/contacts/pals.json`.
- Do not update `workspace/organization/capability-inventory/` without explicit review.
- Do not convert `unknown`, `not-run`, or `missing` into a pass.
- Do not use project usage memory as `keyword_map`, `domain_map`, `role_map`, or deterministic routing.
- Do not convert `second_verification_not_run` into `second_verification_passed`.
- Do not treat a replay record as an execution engine or automatic rollback program.
- Do not treat an audit trail index as an execution engine, external API caller, or automatic missing-evidence closer.
