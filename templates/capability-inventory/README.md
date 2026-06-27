# Capability Inventory Templates

This directory contains reusable JSON templates for Capability Inventory profiles.

It is a template source only. It is not a facts source, not an automatic runtime scan result, and not a routing table.

When creating a real profile, copy a template and follow `docs/03-user-guides/manual-capability-profile.md`. Fill only confirmed information and use `unknown` for unconfirmed fields.

## Template Role

| Asset kind | Template |
| --- | --- |
| Runtime profile | `runtime-profile-template.json` |
| Model profile | `model-profile-template.json` |
| Reasoning profile | `reasoning-profile-template.json` |
| Skill profile | `skill-profile-template.json` |
| Plugin profile | `plugin-profile-template.json` |
| MCP profile | `mcp-profile-template.json` |
| Business System profile | `business-system-profile-template.json` |
| Business System profile review packet | `business-system-profile-review-packet.md` |
| Business System profile manual update evidence pack | `business-system-profile-manual-update-evidence-pack.md` |
| Business System profile manual writeback replay record | `business-system-profile-manual-writeback-replay-record.md` |
| Business System profile audit trail index | `business-system-profile-audit-trail-index.md` |
| Pal capability profile | `pal-capability-profile-template.json` |

## Related Sources

| Source type | Path |
| --- | --- |
| Standards and rules | `standards/capability-inventory/` |
| Business System standard | `standards/capability-inventory/business-system-profile-standard.md` |
| Business System review flow standard | `standards/capability-inventory/business-system-profile-review-flow.md` |
| Current organization records | `workspace/organization/capability-inventory/` |
| Project record template | `workspace/projects/_template/capability-inventory/` |
| Public-safe examples | `examples/capability-inventory/` |
| Business System examples | `examples/capability-inventory/business-system-profiles/` |
| Reusable templates | `templates/capability-inventory/` |
| Manual profile guide | `docs/03-user-guides/manual-capability-profile.md` |
| Historical migration evidence | `archive/migration-from-v0.3/root-legacy/capability-inventory/` |

External project bindings should not copy this directory. Bound projects keep a thin `.agentpal/` pointer and store project-specific capability inventory under the central `workspace/projects/<project-id>/capability-inventory/` record when approved.

Business System profiles describe external system capability and governance boundaries only. They are not connectors, API clients, permission grants, credential stores, automatic scanners, background sync jobs, release tools, or automatic write access.

Capability Inventory profiles are AI judgement inputs. They must not become `keyword_map`, `domain_map`, `role_map`, or any deterministic semantic route. Do not store credentials, private tokens, API keys, cookies, passwords, or secrets in copied profiles.

Business System profile review packets are no-code review artifacts. They may recommend manual organization profile updates after user confirmation and reviewable evidence, but they must not auto-update organization truth or write into external project `.agentpal/` directories by default.

Manual update evidence packs are the next no-code artifact after an approved review packet. They record the approved change, user confirmation, host Runtime evidence, rollback note, manual writeback target, and second verification status. They still must not auto-update organization profiles, modify central Pal contacts, create connectors, store credentials, or write into external project `.agentpal/evidence/`.

Manual writeback replay records are no-code audit artifacts after a manual writeback has happened. They record changed fields, previous and updated snapshot summaries, rollback record, second verification status, not-run checks, and missing evidence. They must not execute writeback, auto-rollback, modify central Pal contacts, create connectors, store credentials, or write into external project `.agentpal/replay/`, `.agentpal/rollback/`, or `.agentpal/verification/`.

Audit trail indexes are no-code index artifacts across review packets, evidence packs, replay records, rollback records, and second verification records. They record paths, statuses, open unknowns, not-run checks, missing evidence, risks, and next manual action suggestions. They must not execute actions, auto-update organization profiles, auto-call external APIs, auto-close missing evidence, modify central Pal contacts, create connectors, store credentials, keyword-route, or write into external project `.agentpal/audit-trail/`.
