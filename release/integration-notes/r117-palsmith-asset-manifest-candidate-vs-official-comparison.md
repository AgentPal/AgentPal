# R117 PalSmith Asset Manifest Candidate vs Official Comparison

Date: 2026-06-28

## Purpose

Compare the R116 writeback candidate with the R117 official PalSmith asset manifest.

## Comparison

| Field | Candidate value summary | Official value summary | Match / adjusted / removed | Reason | Risk | Follow-up needed |
| --- | --- | --- | --- | --- | --- | --- |
| `schema` | `agentpal.pal-asset-manifest.v0.5` | same | match | schema-compatible manifest | low | no |
| `candidate_type` | `official-writeback-candidate` | absent | removed | candidate-only field | low | no |
| `official_writeback_performed` | `false` | absent | removed | official file should not say writeback was not performed | low | no |
| `used_by_runtime_by_default` | `false` | absent | removed | runtime boundary is represented by `writeback.runtime_required=false` and runtime boundary flags | low | no |
| `requires_r117_pre_gate` | `true` | absent | removed | R117 pre-gate is recorded in release evidence | low | no |
| `requires_post_writeback_audit` | `true` | absent | removed | post-audit is recorded in release evidence | low | no |
| `requires_selected_r95_gate` | `true` | absent | removed | selected R95 gate is recorded in release evidence | low | no |
| `pal_id` | `palsmith-pal-governor` | same | match | stable owner id | low | no |
| `display_name` | PalSmith display name | same | match | stable human label | low | no |
| `asset_standard` | `agentpal-pal-asset-standard.v0.5` | same | match | matches PalSmith `pal.json` | low | no |
| `manifest_version` | `0.5.0-writeback-candidate` | `0.5.0-official-palsmith-manifest` | adjusted | distinguish official manifest from candidate | low | no |
| `generated_at` | `2026-06-28` | same | match | same writeback date | low | no |
| `generated_by` | `R116 official writeback review gate` | `R117 official writeback from R116 candidate` | adjusted | official file was written in R117 from the reviewed candidate | low | no |
| `asset_root` | PalSmith official path | same | match | stable relative owner root | low | no |
| `source_proposal` | R115 proposed manifest path | same | match | provenance retained | low | no |
| `source_review` | R116 proposal review path | same | match | provenance retained | low | no |
| `writeback` | absent | present | added | records R117 source candidate, official writeback, and fallback boundary | low | no |
| `root_entries.README.md` | present | present | match | root entry remains valid | low | no |
| `root_entries.PAL.md` | present | present | match | root entry remains valid | low | no |
| `root_entries.pal.json` | present | present | match | root entry remains valid | low | no |
| `root_entries.AGENTS.md` | present | present | match | root entry remains valid | low | no |
| `root_entries.SKILL.md` | present | present | match | root entry remains valid | low | no |
| `root_entries.asset-manifest.json` | missing, candidate note | present, R117 official writeback note | adjusted | official manifest now exists | low | no |
| `assets` | candidate asset groups with review flags | same groups and item-level review flags | match | asset index content preserved | medium | later item-level review |
| `public_safety` | false-default safety flags | same | match | no credentials/private data/report bodies | low | no |
| `skill_boundary` | Pal Skill vs Agent Skill boundary | same | match | references remain references | low | no |
| `runtime_boundary` | no execution/scanning/API/tool install | same | match | no behavior expansion | low | no |
| `known_gaps` | candidate includes pre-writeback and R117 gate notes | official keeps remaining post-writeback gaps only | adjusted | remove stale candidate/pre-gate notes | low | no |
| `not_run_checks` | no writeback/post-audit/R95 in R116 | official notes only audits not performed as full batches | adjusted | remove stale R116-only statements | low | no |
| `review` | R116 review decision and needs-review list | same | match | preserves human review state | low | no |

## Summary

The official manifest is a conservative transformation of the R116 candidate. Candidate-only gate fields were removed, official writeback provenance was added, and `asset-manifest.json` root-entry status was updated from `missing` to `present`.

No asset group was newly invented. No PalSmith `pal.json`, central roster, or other official Pal file was changed.
