# R80 Template Naming Audit

Date: 2026-06-28

Scope: `templates/capabilities/` and `templates/capability-inventory/` naming after the R79 root pointer cleanup.

## Summary

`templates/capabilities/` contained only Capability Inventory profile JSON templates. The directory name was legal because it lived under `templates/`, but it visually resembled the archived root `capabilities/` path. R80 renamed it to `templates/capability-inventory/` and added a README that distinguishes templates from standards, current records, examples, and archive evidence.

## Audit Table

| source_path | current_role | recommended_target | migrate_now | blocker | reference_count | decision |
| --- | --- | --- | --- | --- | ---: | --- |
| `templates/capabilities/` | Capability Inventory JSON profile templates | `templates/capability-inventory/` | yes | none | 3 direct text refs before update | renamed |
| `templates/capability-inventory/` | absent before R80 | Capability Inventory template source | yes | none | 0 before update | created by rename |

## Moved Files

| Old path | New path |
| --- | --- |
| `templates/capabilities/runtime-profile-template.json` | `templates/capability-inventory/runtime-profile-template.json` |
| `templates/capabilities/model-profile-template.json` | `templates/capability-inventory/model-profile-template.json` |
| `templates/capabilities/reasoning-profile-template.json` | `templates/capability-inventory/reasoning-profile-template.json` |
| `templates/capabilities/skill-profile-template.json` | `templates/capability-inventory/skill-profile-template.json` |
| `templates/capabilities/plugin-profile-template.json` | `templates/capability-inventory/plugin-profile-template.json` |
| `templates/capabilities/mcp-profile-template.json` | `templates/capability-inventory/mcp-profile-template.json` |
| `templates/capabilities/pal-capability-profile-template.json` | `templates/capability-inventory/pal-capability-profile-template.json` |

## Boundary

`templates/capability-inventory/` is a reusable template source only. It is not a current facts source, not an automatic scan output, and not a routing table.
