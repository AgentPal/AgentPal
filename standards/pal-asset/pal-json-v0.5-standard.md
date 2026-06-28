# pal.json v0.5 Standard

Date: 2026-06-28
Standard id: `agentpal-pal-json.v0.5`

## Purpose

`pal.json` is the machine-readable manifest for one Pal Pack. It gives AgentPal
and host runtimes a compact way to identify a Pal, find root entries, find asset
directories, understand collaboration boundaries, and preserve no-code runtime
constraints.

`pal.json` is metadata. It is not the Pal's knowledge base, task log, memory
store, report body, route map, runtime executor, or private data store.

## Scope

This standard defines the v0.5 target shape for new or upgraded Pal Packs. Older
official Pals may remain readable with v0.1 manifests while they are gradually
upgraded. Missing v0.5 fields should be reported as upgrade gaps, not automatic
runtime failures, unless a task explicitly requires v0.5 metadata.

JSON Schema reference:

- `standards/schemas/pal.schema.json`

Template reference:

- `templates/pal-asset/pal-json-template.json`

## Required Identity Fields

| Field | Requirement |
| --- | --- |
| `schema` | Schema id string, such as `agentpal.pal.v0.5`. |
| `id` | Stable lowercase Pal id. |
| `name` | Human-short Pal name. |
| `role` | Stable role id or role label. |
| `type` | Pal package type, normally `pal-pack`. |
| `version` | Pal Pack metadata version. |

The v0.5 target requires `name` even when older manifests only have
`display_name`.

## Standard Fields

| Field | Purpose |
| --- | --- |
| `asset_standard` | Pal Asset standard reference, for example `agentpal-pal-asset-standard.v0.5`. |
| `entry` | Root entry file paths. |
| `asset_dirs` | Top-level Pal asset directory paths or explicit not-applicable notes. |
| `core_capabilities` | Public-safe capability labels, not routes. |
| `collaboration` | Discoverability, contactability, supported modes, approval boundary. |
| `discovery` | Alias, direct-call, and central roster lookup hints. |
| `runtime_awareness` | No-code runtime-awareness boundary and evidence needs. |
| `capability_inventory_refs` | Capability Inventory references as judgement inputs only. |
| `pal_skill_boundary` | Pal Skill vs Agent Skill separation. |
| `agent_skill_refs_policy` | How Agent Skill refs may be named without storing them as Pal Skills. |
| `memory_policy` | Memory read/write boundaries and public/private separation. |
| `external_project_write_policy` | Thin-binding default and external project write limits. |
| `no_keyword_routing_policy` | Explicit no keyword/domain/role routing policy. |
| `compatibility` | Legacy compatibility and fallback behavior. |
| `migration_notes` | Human-readable migration notes for older manifests. |

## `entry`

Recommended fields:

```json
{
  "pal": "PAL.md",
  "readme": "README.md",
  "agent": "AGENTS.md",
  "skill": "SKILL.md",
  "asset_manifest": "asset-manifest.json"
}
```

`asset_manifest` may point to a future file even when the current Pal has not
yet generated one. The absence of `asset-manifest.json` is an upgrade gap, not a
failure for legacy reads.

## `asset_dirs`

Recommended groups:

- `identity`
- `core`
- `knowledge`
- `research`
- `skills`
- `workflows`
- `runbooks`
- `learning`
- `memory`
- `state`
- `reports`
- `evals`
- `examples`

Each value should be a relative path string such as `skills/`. If a directory is
not applicable, use `compatibility.not_applicable_asset_dirs` or
`migration_notes` rather than inventing a false path.

## `collaboration`

Recommended fields:

- `discoverable`
- `contactable`
- `allowed_modes`
- `requires_user_approval_for_sensitive_context`
- `central_roster_required`

Collaboration fields are eligibility and boundary metadata. They are not
automatic dispatch rules.

## `discovery`

Recommended fields:

- `direct_call`
- `aliases`
- `central_roster_ref`
- `source_of_truth`

The central roster remains the source of truth for discoverable Pals. `pal.json`
does not modify or replace central contacts.

## `runtime_awareness`

Runtime-awareness fields may describe whether the Pal can reason about current
runtime evidence. They must not claim that the Pal detects, probes, scans, or
executes anything by itself.

Recommended boundary fields:

- `requires_runtime_evidence`
- `pal_executes_runtime_actions`
- `auto_probe_runtime`

For no-code Pal Packs, `pal_executes_runtime_actions` and `auto_probe_runtime`
should be `false`.

## `capability_inventory_refs`

Capability Inventory references are AI judgement inputs. They may point to
organization or project capability records, but they must not become scanner
output, automatic discovery, connector configuration, or route maps.

## `pal_skill_boundary`

Recommended fields:

- `pal_skills_are_role_level`
- `agent_skills_are_runtime_level`
- `pal_skills_dir_default`
- `agent_skill_refs_are_references_only`

`skills/` defaults to Pal Skills. Agent Skills may be referenced, but must not
be copied into Pal `skills/` as if they were Pal-owned capabilities.

## `agent_skill_refs_policy`

Agent Skill refs may name runtime candidates and evidence needs. They must not:

- install runtime Skills
- execute runtime Skills
- modify plugin registries
- add MCP tools
- become Pal contacts
- become routing keys

## `memory_policy`

Recommended fields:

- `private_memory_allowed_in_public_pack`
- `task_logs_allowed_in_pal_json`
- `large_report_bodies_allowed_in_pal_json`
- `memory_write_requires_approval`

Public Pal manifests must not include private memory or customer-private facts.

## `external_project_write_policy`

Recommended fields:

- `external_project_write_allowed_by_default`
- `copy_pal_assets_to_external_project_by_default`
- `thin_binding_required`

Defaults should be:

```json
{
  "external_project_write_allowed_by_default": false,
  "copy_pal_assets_to_external_project_by_default": false,
  "thin_binding_required": true
}
```

## `no_keyword_routing_policy`

Recommended fields:

- `keyword_routing_allowed`
- `domain_routing_allowed`
- `role_routing_allowed`
- `route_maps_allowed`

Defaults should be `false`. Owner selection remains AI judgement using current
task context, central roster, Pal assets, Org Pack recommendations, Capability
Inventory records, and current runtime evidence.

## Forbidden Content

`pal.json` must not store:

- large natural-language knowledge bodies
- task logs
- user private data
- customer-private data
- credentials, tokens, API keys, cookies, passwords, or secrets
- route maps
- keyword maps
- domain maps
- role maps
- report bodies
- runtime execution results

## Compatibility

For v0.1 and v0.4-era manifests:

- keep reading `id`, `display_name`, `role`, `type`, `entry`,
  `core_capabilities`, and `collaboration` when present.
- report missing `asset_standard`, `asset_dirs`, and manifest references as
  upgrade gaps.
- do not block old Pals solely because v0.5 fields are absent.
- do not infer that an asset exists only because a manifest field claims it.

## Migration Notes

Future official Pal upgrades should:

1. Add `name` when missing.
2. Add `asset_standard`.
3. Add `entry.readme` and `entry.asset_manifest`.
4. Add `asset_dirs` for real directories.
5. Add explicit no-keyword-routing and thin-binding policy fields.
6. Add `asset-manifest.json` only after the manifest schema is approved.
