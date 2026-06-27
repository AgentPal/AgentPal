# Capability Inventory Standards

This directory is the standard source for AgentPal capability inventory documents.

It defines public, no-code profile standards and judgement inputs for runtimes, models, reasoning, Skills, plugins, MCP servers, Pal capabilities, and business systems. These files describe what can be recorded or considered; they do not scan the machine, install tools, enable plugins, or route by keywords.

R78 moved low-risk standard-like content here from the legacy root `capabilities/`, `runtime/`, `models/`, and `plugins/` directories.

Current examples live in `examples/capability-inventory/`. Current organization records live in `workspace/organization/capability-inventory/`. Copyable JSON profile templates live in `templates/capability-inventory/`, including `templates/capability-inventory/business-system-profile-template.json`. Project-level record templates live in `workspace/projects/_template/capability-inventory/`.

Business System profile rules live in `standards/capability-inventory/business-system-profile-standard.md`. Business System profile review flow rules live in `standards/capability-inventory/business-system-profile-review-flow.md`. Manual update evidence pack rules live in `standards/capability-inventory/business-system-profile-manual-update-evidence-pack.md`. Manual writeback replay record rules live in `standards/capability-inventory/business-system-profile-manual-writeback-replay-record.md`. Audit trail index rules live in `standards/capability-inventory/business-system-profile-audit-trail-index.md`. Public-safe Business System examples live in `examples/capability-inventory/business-system-profiles/`.

For manual profile creation, use `docs/03-user-guides/manual-capability-profile.md`. Fill only confirmed information, mark unknown fields as `unknown`, and keep credentials or private tokens out of profile records.

Business System profiles are external system governance inputs only. They do not implement API calls, store credentials, grant permissions, authorize external writes, create connectors, run scanners, execute background sync, or route by keywords.

Business System profile review packets can propose organization-level review from project usage memory, but they must not automatically update organization profiles, modify central Pal contacts, write into external project `.agentpal/`, store credentials, create connectors, or route by keywords. If a review packet is approved for manual update, a Manual Update Evidence Pack can document evidence, user confirmation, host Runtime evidence, rollback notes, manual writeback steps, and second verification status before any organization profile edit. After a manual writeback has happened, a Manual Writeback Replay Record can audit what changed, rollback notes, and second verification result without becoming an execution engine or automatic rollback program. When multiple review / evidence / replay records exist, an Audit Trail Index can summarize paths, statuses, risks, not-run checks, missing evidence, and next manual action suggestions without executing those actions or auto-closing evidence.

For the full source map, see `docs/00-overview/capability-inventory-navigation.md`.

External user projects should not copy this directory; they use thin binding files only.
