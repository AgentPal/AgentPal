# R112 Mira pal.json v0.5 Dry-Run Proposal

Date: 2026-06-28

## Purpose

This is a dry-run proposal for a possible future Mira `pal.json` v0.5 metadata update.

It does not modify `official/pals/Mira-main/pal.json`, does not create `official/pals/Mira-main/asset-manifest.json`, and does not change central contacts.

Proposed JSON:

- `release/integration-notes/r112-mira-pal-json-v0.5-dry-run.proposed.json`

## Current pal.json Summary

| Field | Current value summary | Source |
| --- | --- | --- |
| `schema` | `agentpal.pal.v0.1` | `official/pals/Mira-main/pal.json` |
| `id` | `mira-main` | `pal.json`, central roster |
| `name` | missing | R110 audit identified this v0.5 required-field gap |
| `display_name` | `Mira` | `pal.json`, central roster |
| `directory_name` | `Mira-main` | `pal.json`, central roster path |
| `role` | `main-leader-conductor` | `pal.json`, central roster |
| `type` | `pal-pack` | `pal.json` |
| `version` | `0.1.0` | `pal.json` |
| `entry` | no v0.5 full entry object | root entries exist |
| `asset_standard` | missing | R110 field mapping gap |
| v0.5 policy groups | mostly missing | R110 audit |

## Proposed v0.5 Fields

| Proposed field | Proposed value summary | Source of inference | Confidence |
| --- | --- | --- | --- |
| `schema` | `agentpal.pal.v0.5` | v0.5 standard | high |
| `name` | `Mira` | existing `display_name`, central roster display name | medium, needs human review |
| `asset_standard` | `agentpal-pal-asset-standard.v0.5` | v0.5 standard | high |
| `entry` | `PAL.md`, `README.md`, `AGENTS.md`, `SKILL.md`, future manifest reference | actual root files plus standard | high |
| `asset_dirs` | existing Mira directories only | directory listing | high |
| `discovery` | `/pal Mira`, aliases, central roster ref | central roster | high |
| `runtime_awareness` | requires runtime evidence; Pal does not execute or auto-probe | v0.5 standard plus Mira boundary text | medium, needs wording review |
| `pal_skill_boundary` | Pal Skills are role-level; Agent Skills are runtime-level references | skills index and v0.5 standard | high |
| `agent_skill_refs_policy` | references only, no runtime skill storage in Pal `skills/` | skills index and standard | high |
| `memory_policy` | no private memory, task logs, or large report bodies in `pal.json` | memory README and standard | high |
| `external_project_write_policy` | false by default; thin binding required | Mira PAL.md and project-binding boundary | high |
| `no_keyword_routing_policy` | all false | central roster and v0.5 standard | high |
| `credentials_allowed` | false | v0.5 standard | high |
| `compatibility` | legacy readable, manifest not required, directory fallback true | R100-D / R110 | high |

## Safe Defaults

Safe defaults proposed only for a future real update:

- `keyword_routing_allowed=false`
- `domain_routing_allowed=false`
- `role_routing_allowed=false`
- `route_maps_allowed=false`
- `external_project_write_allowed_by_default=false`
- `copy_pal_assets_to_external_project_by_default=false`
- `credentials_allowed=false`
- `pal_executes_runtime_actions=false`
- `auto_probe_runtime=false`
- `agent_skill_refs_are_references_only=true`

## Human Review Required

Human review is required before any real write for:

- `name`: inferred from `display_name`; likely safe, but v0.5 makes it required.
- Main Pal role wording: must preserve Mira as default Main Pal / Leader Pal / Conductor without implying runtime execution.
- core capability pruning: current list is large and should be shortened for public metadata.
- runtime-awareness conversion: legacy `detect_current_runtime` wording should become evidence-aware and no-code.
- version value: R112 uses `0.5.0-dry-run-proposal`; a real update needs approved version wording.
- future manifest reference: `entry.asset_manifest` may point to a future file, but no real manifest exists.

## Fields Not Proposed

This proposal does not include:

- private memory
- task logs
- full report bodies
- runtime execution results
- central roster edits
- deterministic dispatch tables
- external project local asset sources

## Forbidden Fields And Defaults

The real update must not add:

- deterministic route maps
- fixed domain or role dispatch maps
- external project Pal asset copying by default
- credential storage
- runtime probing by the Pal
- Agent Skill files stored as Pal Skills

## No Real Writeback Statement

R112 writes only this proposal and the proposed JSON under `release/integration-notes/`.

R112 does not write to `official/pals/Mira-main/`.

## Proposed Next Step

Mira can be a second pilot candidate after PalSmith or after a focused human review of Main Pal wording. If R113 chooses Mira first, rerun R100-D / R110 gates and selected R95 groups before and after the real `pal.json` edit.

