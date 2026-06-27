# Capability Inventory Examples

This directory contains example capability profiles and judgement inputs.

Examples are illustrative only. They do not prove the current machine has a runtime, model, Skill, plugin, MCP server, Pal capability, or business-system integration.

Business-system examples live in `business-system-profiles/` and describe external system governance boundaries only. Business-system review examples live in `business-system-profile-reviews/` and show no-code review packets, manual update evidence packs, manual writeback replay records, and audit trail indexes that do not update organization truth by themselves. They must not include connectors, credentials, private tokens, passwords, API keys, cookies, secrets, private accounts, or unapproved write access.

Use examples as bounded AI judgement inputs, not keyword routes or deterministic task maps. Do not copy examples into external project `.agentpal/` bindings by default.

To create a real profile, start from `docs/03-user-guides/manual-capability-profile.md` and copy a template from `templates/capability-inventory/`. Save organization-level records under `workspace/organization/capability-inventory/` and project-level records under `workspace/projects/<project-id>/capability-inventory/`.

Related sources:

- Standards: `standards/capability-inventory/`
- Business System standard: `standards/capability-inventory/business-system-profile-standard.md`
- Current organization records: `workspace/organization/capability-inventory/`
- Project record template: `workspace/projects/_template/capability-inventory/`
- Templates: `templates/capability-inventory/`
- Business System template: `templates/capability-inventory/business-system-profile-template.json`
- Business System examples: `examples/capability-inventory/business-system-profiles/`
- Business System profile review examples: `examples/capability-inventory/business-system-profile-reviews/`
- Manual guide: `docs/03-user-guides/manual-capability-profile.md`
- Navigation: `docs/00-overview/capability-inventory-navigation.md`
