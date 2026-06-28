# R100-B Official Pal Metadata Upgrade Batch Plan

Date: 2026-06-28

Owner Pal: PalSmith

Scope: prepare a small-scope v0.5 upgrade plan for the 9 official Pal Packs based on R98-B audit evidence. This file is a planning artifact only. It does not modify `official/pals/**`, central contacts, shared entry files, or release metadata.

## Evidence Inputs

- R98-B audit: `evals/palbench/pal-asset/r98b-official-pal-asset-audit.md`
- R98-B gap table: `evals/palbench/pal-asset/r98b-official-pal-upgrade-gap-table.md`
- R98-B upgrade plan: `release/integration-notes/r98b-official-pal-upgrade-plan.md`
- Pal Asset Standard: `standards/pal-asset/pal-asset-standard.md`
- Directory Standard: `standards/pal-asset/pal-asset-directory-standard.md`
- Root Entry Standard: `standards/pal-asset/pal-root-entry-standard.md`
- Pal Skill vs Agent Skill Standard: `standards/pal-asset/pal-skill-vs-agent-skill-standard.md`
- Loading Order Standard: `standards/pal-asset/pal-loading-order-standard.md`
- Resolver Standard: `standards/pal-asset/pal-asset-resolver-standard.md`
- pal.json v0.5 Standard: `standards/pal-asset/pal-json-v0.5-standard.md`
- Pal Asset Manifest Standard: `standards/pal-asset/asset-manifest-standard.md`
- pal.json schema: `standards/schemas/pal.schema.json`
- asset manifest schema: `standards/schemas/pal-asset-manifest.schema.json`
- pal.json template: `templates/pal-asset/pal-json-template.json`
- asset manifest template: `templates/pal-asset/asset-manifest-template.json`
- safe index guide: `templates/pal-asset/safe-index-backfill-guide.md`
- Central roster: `workspace/organization/contacts/pals.json`
- Official Pal roots: `official/pals/`

## Current Baseline

| Check | Result |
| --- | --- |
| Official Pal dirs | 9 |
| Central roster parse | pass |
| Registered active Pals | 9 |
| Official `pal.json` parse | 9 pass / 0 fail |
| Root entry completeness | 45 / 45 present |
| `git diff -- official/pals` before plan write | no diff |
| `keyword_map|domain_map|role_map` under official Pals | no hits |
| Focused credential-like assignment search | no hits |

## Batch Strategy

### Batch 1: Safe Index / README Preparation

Goal: add or normalize explanatory index/README files only.

Allowed in a future repair thread:

- create public-safe `index.md` or `README.md` files in existing asset directories.
- explain directory purpose, what belongs there, what must not be stored there, and privacy / credential boundaries.
- preserve `unknown`, `missing`, and `not-run`.

Not allowed:

- moving assets
- renaming directories
- deleting content
- changing Pal behavior
- writing project-private data
- writing credentials
- changing `pal.json`
- generating `asset-manifest.json`

### Batch 2: `pal.json` v0.5 Metadata

Goal: add v0.5 metadata once the target branch has the Pal Asset Standard integrated.

Candidate fields:

- `asset_standard`
- `name` when missing or when only `display_name` is present
- `entry.readme`
- `entry.asset_manifest`
- `root_entries`
- `asset_dirs`
- `discovery`
- `runtime_awareness`
- `capability_inventory_refs`
- `pal_skill_boundary`
- `agent_skill_refs_policy`
- `memory_policy`
- `external_project_write_policy`
- `no_keyword_routing_policy`
- `skill_boundary`
- `runtime_boundary`
- `public_safety_policy`
- `known_asset_gaps`
- `not_applicable_asset_dirs`

Human review required because `pal.json` is a machine-readable Pal manifest and should not silently alter Pal identity, collaboration, or capability claims.

### Batch 3: `asset-manifest.json` Preview / Generation

Goal: after schema approval, generate asset indexes from current root files, directory listings, and index files.

Rules:

- manifest is an index, not a validator.
- manifest is not a route map.
- manifest must not include `keyword_map`, `domain_map`, or `role_map`.
- manifest must preserve `missing`, `not-run`, and `requires_human_review`.
- manifest must not include private memory, runtime state, private reports, credentials, or copied external project data.
- use `standards/schemas/pal-asset-manifest.schema.json` and `templates/pal-asset/asset-manifest-template.json` when integrated into the target branch.

### Batch 4: Misplaced Asset Review

Goal: review content that may need classification before moving or rewriting.

Review targets:

- Mira old external `.agentpal/` project-memory wording.
- PalSmith `.agentpal/import-staging/` examples.
- Atlas imported Skill-card references and implementation-shaped Pal Skills.
- Vega research vs durable knowledge promotion boundary.
- Rhea state/memory boundary.
- any report-vs-memory confusion.

Batch 4 is not safe to auto-fix. It requires human review and owner-Pal judgement.

## Per-Pal Batch Table

| pal_id | display_name | current path | root entry completeness | missing index files | `pal.json` v0.5 gaps | asset-manifest readiness | safe auto-fix candidates | requires human review | suggested round | blocked risks |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| mira-main | Mira | `official/pals/Mira-main` | complete | `research/index.md` or `research/README.md` | missing `asset_standard`, `asset_dirs`, `root_entries`, manifest policy | preview-ready after schema | none by default; research index requires wording review | yes | Batch 4 before Batch 2/3 | old `.agentpal/` project-memory wording must be reconciled with central `agentpal_project_record` policy |
| atlas-developer | Atlas | `official/pals/Atlas-developer` | complete | `memory/index.md` or `memory/README.md`; `research/index.md` or `research/README.md` | missing `asset_standard`, `asset_dirs`, `root_entries`, manifest policy | preview-ready after schema | memory index can be drafted as public-safe placeholder | yes | Batch 1 then Batch 4 | imported Skill-card references and implementation-shaped Skills need Pal Skill vs Agent Skill review |
| nova-product | Nova | `official/pals/Nova-product` | complete | `memory/index.md` or `memory/README.md`; `research/index.md` or `research/README.md` | missing `asset_standard`, `asset_dirs`, `root_entries`, manifest policy | preview-ready after schema | memory index can be drafted as public-safe placeholder | research index yes; metadata yes | Batch 1 then Batch 2 | avoid treating examples or product notes as durable private memory |
| vega-research | Vega | `official/pals/Vega-research` | complete | `memory/index.md` or `memory/README.md`; `research/index.md` or `research/README.md` | missing `asset_standard`, `asset_dirs`, `root_entries`, manifest policy | preview-ready after schema | memory index can be drafted as public-safe placeholder | yes | Batch 1 then Batch 4 | research source notes must not become stable knowledge without review |
| quinn-quality | Quinn | `official/pals/Quinn-quality` | complete | `memory/index.md` or `memory/README.md`; `research/index.md` or `research/README.md` | missing `asset_standard`, `asset_dirs`, `root_entries`, manifest policy | preview-ready after schema | memory index can be drafted as public-safe placeholder | metadata and research index yes | Batch 1 then Batch 2 | eval/report/memory distinction should remain explicit |
| morgan-document | Morgan | `official/pals/Morgan-document` | complete | `memory/index.md` or `memory/README.md`; `research/index.md` or `research/README.md` | missing `asset_standard`, `asset_dirs`, `root_entries`, manifest policy | preview-ready after schema | memory index can be drafted as public-safe placeholder | metadata and research index yes | Batch 1 then Batch 2 | document privacy examples must not create private memory or report leakage |
| harper-writing | Harper | `official/pals/Harper-writing` | complete | `memory/index.md` or `memory/README.md`; `research/index.md` or `research/README.md` | missing `asset_standard`, `asset_dirs`, `root_entries`, manifest policy | preview-ready after schema | memory index can be drafted as public-safe placeholder | metadata and research index yes | Batch 1 then Batch 2 | style examples and user voice must not become unapproved private memory |
| rhea-system | Rhea | `official/pals/Rhea-system` | complete | `memory/index.md` or `memory/README.md`; `research/index.md` or `research/README.md` | missing `asset_standard`, `asset_dirs`, `root_entries`, manifest policy | preview-ready after schema | memory index can be drafted as public-safe placeholder | yes | Batch 1 then Batch 4 | runtime state examples must stay examples, not current machine state or memory |
| palsmith-pal-governor | PalSmith | `official/pals/PalSmith-pal-governor` | complete | `runbooks/index.md` or `runbooks/README.md`; `research/index.md` or `research/README.md`; missing `memory/`; missing `learning/` | missing `asset_standard`, `asset_dirs`, `root_entries`, manifest policy | preview-ready after schema | runbooks index can be drafted if it only describes existing runbooks | yes | Batch 1 with human review, then Batch 4 | `memory/` and `learning/` require not-applicable vs create-placeholder policy decision; staging examples need review |

## Batch Acceptance Criteria

Batch 1 passes only if:

- no asset is moved or deleted.
- no Pal behavior changes.
- no project-private data or credentials are added.
- `git diff -- official/pals` contains only approved index/README additions.
- all 9 `pal.json` files still parse.

Batch 2 passes only if:

- all metadata values are derived from current files or explicit policy.
- central roster remains unchanged.
- metadata does not create route maps or inflated capability claims.

Batch 3 passes only if:

- manifests are generated from evidence and preserve missing/not-run states.
- manifests contain no credentials, private memory, private reports, copied external project data, or route maps.

Batch 4 passes only if:

- each risky content decision has human review notes and owner-Pal judgement.
- no content is moved or rewritten without a separate allowed repair thread.
