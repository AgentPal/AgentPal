# AgentPal Standards

This directory contains public, release-facing standards for AgentPal workspace governance.

AgentPal is a no-code organization layer for existing host runtimes. These standards keep the public repository easy to inspect and keep external user projects clean.

Primary areas:

- `boundaries/`: non-negotiable repository and runtime boundaries.
- `project-binding/`: thin external project binding files and protected blocks.
- `organization/`: central Pal roster, central project records, project memory, source maps, derived knowledge, and organization workspace rules.
- `routing-and-judgement/`: AI judgement routing rules and anti-keyword-routing constraints.

These standards are documents and JSON conventions only. They do not create a CLI, daemon, scanner, validator, installer, service, database, app, or automatic execution layer.
