# Organization Capability Inventory

This directory is the central AgentPal organization location for current capability records.

It may hold public-safe runtime, model, reasoning, Skill, plugin, MCP, business-system, and usage-memory placeholders or maintained records. It is not an automatic scan result and does not prove any capability is available in a host runtime.

Records here may be maintained manually by a user, organized by a Pal from user-confirmed facts, or updated from current host Runtime evidence. Unconfirmed fields should be marked `unknown`; do not invent model access, installed plugins, Skill availability, business-system permissions, or runtime controls.

Do not store private credentials, private tokens, API keys, private machine paths, or external project secrets here. External projects should keep only thin binding files and should not receive copied organization capability records.

Organization records can be referenced by project records under `workspace/projects/<project-id>/capability-inventory/`. Project records may add project-specific availability, limits, or usage notes without changing the central Pal roster.

Capability Inventory records are AI judgement inputs only. They must not become keyword routes, domain routes, automatic scans, automatic validation claims, or automatic runtime selection.

Related sources:

- Standards: `standards/capability-inventory/`
- Examples: `examples/capability-inventory/`
- Templates: `templates/capability-inventory/`
- Project record template: `workspace/projects/_template/capability-inventory/`
- Manual guide: `docs/03-user-guides/manual-capability-profile.md`
- Navigation: `docs/00-overview/capability-inventory-navigation.md`
