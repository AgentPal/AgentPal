# R112 PalSmith pal.json v0.5 Dry-Run Proposal

Date: 2026-06-28

## Purpose

This is a dry-run proposal for a possible future PalSmith `pal.json` v0.5 metadata update.

It does not modify `official/pals/PalSmith-pal-governor/pal.json`, does not create `official/pals/PalSmith-pal-governor/asset-manifest.json`, and does not change central contacts.

Proposed JSON:

- `release/integration-notes/r112-palsmith-pal-json-v0.5-dry-run.proposed.json`

## Current pal.json Summary

| Field | Current value summary | Source |
| --- | --- | --- |
| `schema` | `agentpal.pal-pack.v0.1` | `official/pals/PalSmith-pal-governor/pal.json` |
| `id` | `palsmith-pal-governor` | `pal.json`, central roster |
| `name` | `PalSmith` | `pal.json` |
| `display_name` | `PalSmith / Pal Asset Governor` | `pal.json` |
| `directory_name` | `PalSmith-pal-governor` | `pal.json`, central roster |
| `role` | `pal-asset-governor` | `pal.json`, central roster |
| `type` | `pal-pack` | `pal.json` |
| `version` | `0.1.0` | `pal.json` |
| `entry` | partial: `SKILL.md`, `PAL.md`, `AGENTS.md` | `pal.json` |
| `asset_standard` | missing | R110 field mapping gap |
| v0.5 policy groups | mostly missing | R110 audit |

## Proposed v0.5 Fields

| Proposed field | Proposed value summary | Source of inference | Confidence |
| --- | --- | --- | --- |
| `schema` | `agentpal.pal.v0.5` | v0.5 standard | high |
| `asset_standard` | `agentpal-pal-asset-standard.v0.5` | v0.5 standard | high |
| `entry` | add `README.md` and future manifest reference | actual root files plus standard | high |
| `asset_dirs` | existing PalSmith directories only | directory listing | high |
| `discovery` | `/pal PalSmith`, aliases, central roster ref | central roster | high |
| `runtime_awareness` | requires runtime evidence; Pal does not execute or auto-probe | PAL.md / AGENTS.md / SKILL.md | high |
| `pal_skill_boundary` | Pal Skills are role-level; Agent Skills are runtime-level references | skills index and v0.5 standard | high |
| `agent_skill_refs_policy` | references only, no runtime skill storage in Pal `skills/` | skills index and standard | high |
| `memory_policy` | no private memory, task logs, or large report bodies in `pal.json` | memory README and standard | high |
| `external_project_write_policy` | false by default; thin binding required | PAL.md and AGENTS.md boundary | high |
| `no_keyword_routing_policy` | all false | central roster and v0.5 standard | high |
| `palsmith_governance_boundary` | no-code governance only; no automatic roster modification or runtime programs | PAL.md / AGENTS.md / SKILL.md | high |
| `compatibility` | legacy readable, manifest not required, directory fallback true | R100-D / R110 | high |

## PalSmith-Specific Governance Boundary

PalSmith can classify, create, and upgrade Pal assets as no-code governance work through proposals, task packages, and evidence review.

PalSmith cannot:

- automatically modify central roster files;
- default-write central Pal assets into external projects;
- create runtime connector, scanner, or auto-execution behavior;
- treat runtime Agent Skills as Pal-owned Skills;
- claim file operations without current execution-layer evidence.

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
- `can_automatically_modify_central_roster=false`
- `can_default_write_central_pal_assets_into_external_projects=false`
- `can_create_connector_scanner_or_auto_execution=false`

## Human Review Required

Human review is required before any real write for:

- governance capability wording;
- official registration and contacts proposal wording;
- version value;
- whether `entry.asset_manifest` should be written before a real manifest exists;
- whether missing optional `learning/` should be not applicable or a future gap.

## Fields Not Proposed

This proposal does not include:

- central roster edits;
- real asset manifest content;
- external project local Pal asset copies;
- runtime execution results;
- private memory;
- large report bodies.

## No Real Writeback Statement

R112 writes only this proposal and the proposed JSON under `release/integration-notes/`.

R112 does not write to `official/pals/PalSmith-pal-governor/`.

## Proposed Next Step

PalSmith is the recommended first real metadata update candidate for R113 because its current `pal.json` already has `name`, direct call, aliases, and strong no-code governance boundary text. R113 must still rerun R100-D / R110 gates and selected R95 groups before and after any real edit.

