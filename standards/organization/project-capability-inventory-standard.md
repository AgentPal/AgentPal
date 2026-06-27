# Project Capability Inventory Standard

A project capability inventory records what runtimes, models, skills, plugins, MCP servers, and business systems may be available for a bound external project.

## Location

Default location:

`workspace/projects/<project-id>/capability-inventory/`

Template location:

`workspace/projects/_template/capability-inventory/`

Project capability records may reference organization-level capability records from:

`workspace/organization/capability-inventory/`

Project records may add project-specific availability, limits, usage notes, or business-system constraints. They must not modify the central Pal roster.

## Boundary

The inventory is a no-code record. It must not claim automatic scanning, automatic sync, or automatic execution. It records current evidence supplied by the runtime or the user.

Capability records are judgement inputs. They are not keyword routes, domain routes, role maps, or deterministic owner selection tables.

Do not store credentials, private tokens, API keys, session cookies, or project secrets in project capability inventory records.
