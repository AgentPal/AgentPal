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
| Pal capability profile | `pal-capability-profile-template.json` |

## Related Sources

| Source type | Path |
| --- | --- |
| Standards and rules | `standards/capability-inventory/` |
| Current organization records | `workspace/organization/capability-inventory/` |
| Project record template | `workspace/projects/_template/capability-inventory/` |
| Public-safe examples | `examples/capability-inventory/` |
| Reusable templates | `templates/capability-inventory/` |
| Manual profile guide | `docs/03-user-guides/manual-capability-profile.md` |
| Historical migration evidence | `archive/migration-from-v0.3/root-legacy/capability-inventory/` |

External project bindings should not copy this directory. Bound projects keep a thin `.agentpal/` pointer and store project-specific capability inventory under the central `workspace/projects/<project-id>/capability-inventory/` record when approved.

Capability Inventory profiles are AI judgement inputs. They must not become `keyword_map`, `domain_map`, `role_map`, or any deterministic semantic route. Do not store credentials, private tokens, API keys, or secrets in copied profiles.
