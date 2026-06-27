# AgentPal Standards

This directory contains public, release-facing standards for AgentPal workspace governance.

AgentPal is a no-code organization layer for existing host runtimes. These standards keep the public repository easy to inspect and keep external user projects clean.

Primary areas:

- `boundaries/`: non-negotiable repository and runtime boundaries.
- `project-binding/`: thin external project binding files and protected blocks.
- `organization/`: central Pal roster, central project records, project memory, source maps, derived knowledge, and organization workspace rules.
- `routing-and-judgement/`: AI judgement routing rules and anti-keyword-routing constraints.
- `deep-conductor/`: no-code Deep Conductor standard surface and pointers.
- `capability-inventory/`: manual capability inventory standards and pointers.
- `governance/`: governance record standards and review boundaries.
- `org-pack/`: organization pack standards and packaging boundaries.
- `schemas/`: public JSON / Markdown schema notes.

These standards are documents and JSON conventions only. They do not create a CLI, daemon, scanner, validator, installer, service, database, app, or automatic execution layer.

Related migration plans:

- `../docs/00-overview/capability-inventory-migration-plan.md`
- `../docs/00-overview/orchestration-migration-plan.md`
- `../docs/00-overview/prompts-migration-plan.md`
