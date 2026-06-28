# R117 PalSmith Asset Manifest Official Writeback Plan

Date: 2026-06-28

## Purpose

Plan the first real official Pal asset manifest writeback for PalSmith only.

## Source And Target

| Item | Path |
| --- | --- |
| source candidate | `release/integration-notes/r116-palsmith-asset-manifest-official-writeback-candidate.json` |
| target official manifest | `official/pals/PalSmith-pal-governor/asset-manifest.json` |
| owner Pal path | `official/pals/PalSmith-pal-governor` |

## Transformation Rules

The official manifest is derived from the R116 candidate with only low-risk structural changes:

| Rule | Action | Reason |
| --- | --- | --- |
| remove `candidate_type` | remove | candidate-only metadata is not part of the official manifest body |
| remove `official_writeback_performed=false` | remove | official file should not claim writeback was not performed |
| remove `requires_r117_pre_gate` | remove | R117 pre-gate is recorded in release evidence, not official manifest runtime metadata |
| remove `requires_post_writeback_audit` | remove | post-audit requirement is recorded in release evidence |
| remove `requires_selected_r95_gate` | remove | selected R95 requirement is recorded in release evidence |
| adjust `manifest_version` | set `0.5.0-official-palsmith-manifest` | distinguish official manifest from candidate |
| adjust `generated_by` | set `R117 official writeback from R116 candidate` | official file is written in R117 from reviewed candidate |
| keep schema-compatible manifest fields | preserve | manifest must remain compatible with `agentpal.pal-asset-manifest.v0.5` |
| preserve asset groups, root entries, public safety, skill boundary, runtime boundary, known gaps, and review flags | preserve | official manifest remains an honest index |
| add `writeback` metadata | add | record source candidate, R117 round, official writeback true, and runtime not required |
| keep relative paths | preserve | all asset paths stay relative to PalSmith root |

## Fields Preserved

- `schema`
- `pal_id`
- `display_name`
- `asset_standard`
- `generated_at`
- `asset_root`
- `source_proposal`
- `source_review`
- `root_entries`
- `assets`
- `public_safety`
- `skill_boundary`
- `runtime_boundary`
- `known_gaps`
- `not_run_checks`
- `requires_human_review`
- `review`

## Fields Added

`writeback`:

- `round`: `R117`
- `source_candidate`: `release/integration-notes/r116-palsmith-asset-manifest-official-writeback-candidate.json`
- `official_writeback`: `true`
- `runtime_required`: `false`
- `directory_convention_fallback_preserved`: `true`

## Rollback Action

If post-writeback audit fails, remove:

`official/pals/PalSmith-pal-governor/asset-manifest.json`

Then rerun validation and confirm PalSmith still loads by root entries and directory convention fallback.

## Post-audit Requirements

After writeback, R117 must create:

- writeback record
- candidate vs official comparison
- post-writeback audit
- selected R95 gate
- local validation
- rollback readiness
- R118 readiness decision

No remote Git, tag, or release action is allowed.
