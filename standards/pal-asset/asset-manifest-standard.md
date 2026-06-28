# Pal Asset Manifest Standard

Date: 2026-06-28
Standard id: `agentpal-pal-asset-manifest.v0.5`

## Purpose

`asset-manifest.json` is an optional asset index for one Pal Pack. It helps a
runtime or maintainer find Pal-owned assets without scanning or reading every
file.

The manifest is an index, not asset content. It does not prove job fitness by
itself, does not execute checks, and does not replace actual asset files.

JSON Schema reference:

- `standards/schemas/pal-asset-manifest.schema.json`

Template reference:

- `templates/pal-asset/asset-manifest-template.json`

## Fallback If Absent

If `asset-manifest.json` is absent:

1. Read `pal.json`.
2. Read root entries by the loading-order standard.
3. List known asset directories.
4. Read directory indexes when present.
5. Report manifest evidence as `missing`.

Absence of the manifest is an upgrade gap, not an automatic blocker for legacy
Pals.

## Top-Level Fields

| Field | Purpose |
| --- | --- |
| `schema` | Manifest schema id. |
| `pal_id` | Owner Pal id. |
| `display_name` | Human-readable Pal name. |
| `asset_standard` | Pal Asset standard reference. |
| `manifest_version` | Manifest format version. |
| `generated_at` | Date or timestamp if generated. |
| `generated_by` | Human, Pal, or runtime evidence source. |
| `asset_root` | Pal Pack root path. |
| `root_entries` | Root entry paths and status. |
| `assets` | Grouped asset entries. |
| `public_safety` | Public/private and secret boundaries. |
| `skill_boundary` | Pal Skill vs Agent Skill boundary summary. |
| `runtime_boundary` | No-code runtime boundary summary. |
| `known_gaps` | Missing or partial evidence. |
| `not_run_checks` | Checks not performed. |
| `requires_human_review` | Whether human review remains required. |

## Asset Groups

`assets` should group entries by:

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

Groups may be empty arrays. Empty group does not mean the asset type is
forbidden; it means the manifest has no indexed item for that group.

## Asset Entry Fields

Each asset entry should include:

| Field | Purpose |
| --- | --- |
| `id` | Stable local asset id. |
| `type` | Asset type, usually matching the group or a subtype. |
| `path` | Relative file or directory path. |
| `status` | `present`, `missing`, `partial`, `deprecated`, `not-applicable`, or `not-run`. |
| `summary` | Short public-safe summary. |
| `owner` | Owner Pal id or approved owner record. |
| `last_reviewed` | Date or `not-run`. |
| `promotion_source` | Source asset or `none`. |
| `verification_ref` | Eval, report, or validation reference. |

## Root Entry Records

Root entry records should include paths and status for:

- `README.md`
- `PAL.md`
- `pal.json`
- `AGENTS.md`
- `SKILL.md`

They may also include `asset-manifest.json` itself.

## Public Safety

The manifest must preserve public/private boundaries. It may summarize private
asset existence only when approved, but must not include private content.

Recommended flags:

- `credentials_allowed: false`
- `private_memory_in_public_manifest: false`
- `customer_private_data_allowed: false`
- `large_report_bodies_allowed: false`

## Forbidden

The manifest must not contain:

- credentials, tokens, API keys, cookies, passwords, or secrets
- keyword maps, domain maps, role maps, or deterministic routes
- copied external project local Pal assets
- large report bodies
- private memory bodies
- runtime state dumps
- external system connection strings
- connector configuration

## Relationship To Pal Loading

The loading-order standard may use the manifest as a navigation aid after root
entry files. The manifest should help select the smallest relevant asset slice.
It should not cause full asset loading by default.

## Relationship To Official Pal Upgrades

Future official Pal upgrades should generate manifests only after:

1. v0.5 `pal.json` fields are settled.
2. directory index coverage is reviewed.
3. public-safety policy is reviewed.
4. missing and not-run fields are preserved honestly.
