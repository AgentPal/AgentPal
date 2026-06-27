# Capability Inventory Standards

This directory is the standard source for AgentPal capability inventory documents.

It defines public, no-code profile standards and judgement inputs for runtimes, models, reasoning, Skills, plugins, MCP servers, Pal capabilities, and business systems. These files describe what can be recorded or considered; they do not scan the machine, install tools, enable plugins, or route by keywords.

R78 moved low-risk standard-like content here from the legacy root `capabilities/`, `runtime/`, `models/`, and `plugins/` directories.

Current examples live in `examples/capability-inventory/`. Current organization records live in `workspace/organization/capability-inventory/`. Copyable JSON profile templates live in `templates/capability-inventory/`. Project-level record templates live in `workspace/projects/_template/capability-inventory/`.

For manual profile creation, use `docs/03-user-guides/manual-capability-profile.md`. Fill only confirmed information, mark unknown fields as `unknown`, and keep credentials or private tokens out of profile records.

For the full source map, see `docs/00-overview/capability-inventory-navigation.md`.

External user projects should not copy this directory; they use thin binding files only.
