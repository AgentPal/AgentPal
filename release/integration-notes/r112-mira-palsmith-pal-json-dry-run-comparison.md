# R112 Mira / PalSmith pal.json Dry-Run Comparison

Date: 2026-06-28

## Scope

Comparison of proposed `pal.json` v0.5 dry-run metadata for:

- `mira-main`
- `palsmith-pal-governor`

The proposals are stored in `release/integration-notes/` only. No official Pal `pal.json` file is modified.

## Comparison Table

| pal_id | field | current value summary | proposed value summary | source | confidence | safe default | human review required | risk | ready for real update |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `mira-main` | `schema` | `agentpal.pal.v0.1` | `agentpal.pal.v0.5` | v0.5 standard | high | yes | yes | upgrade marker must be intentional | yes |
| `mira-main` | `name` | missing | `Mira` | `display_name`, central roster | medium | no | yes | Main Pal display identity needs review | yes, after review |
| `mira-main` | `asset_standard` | missing | `agentpal-pal-asset-standard.v0.5` | v0.5 standard | high | yes | no | low | yes |
| `mira-main` | `entry` | not complete v0.5 entry | root entries plus future manifest reference | actual files | high | yes | yes | future manifest is absent | yes |
| `mira-main` | `asset_dirs` | absent as v0.5 object | existing dirs only | directory listing | high | yes | yes | directory meaning needs review for reports/state | yes |
| `mira-main` | `runtime_awareness` | legacy runtime detection claims | evidence-required, no Pal execution, no auto-probe | standard, PAL.md | medium | yes | yes | wording could imply runtime behavior if copied carelessly | yes, after review |
| `mira-main` | `no_keyword_routing_policy` | central policy only | false for keyword, domain, role, route maps | central roster, standard | high | yes | no | low | yes |
| `mira-main` | `external_project_write_policy` | implicit in docs | false-by-default, thin binding required | Mira / binding docs | high | yes | no | low | yes |
| `mira-main` | `agent_skill_refs_policy` | implicit in skills boundary | references only; no Agent Skill storage | skills index | high | yes | no | low | yes |
| `mira-main` | `credentials_allowed` | absent | false | standard | high | yes | no | low | yes |
| `palsmith-pal-governor` | `schema` | `agentpal.pal-pack.v0.1` | `agentpal.pal.v0.5` | v0.5 standard | high | yes | yes | upgrade marker must be intentional | yes |
| `palsmith-pal-governor` | `name` | `PalSmith` | preserve `PalSmith` | current `pal.json` | high | no | no | low | yes |
| `palsmith-pal-governor` | `asset_standard` | missing | `agentpal-pal-asset-standard.v0.5` | v0.5 standard | high | yes | no | low | yes |
| `palsmith-pal-governor` | `entry` | partial root entry object | root entries plus future manifest reference | actual files | high | yes | yes | future manifest is absent | yes |
| `palsmith-pal-governor` | `asset_dirs` | absent as v0.5 object | existing dirs only; `learning/` recorded as optional gap | directory listing | high | yes | yes | optional gap classification | yes |
| `palsmith-pal-governor` | `runtime_awareness` | no-runtime-code boundary present | evidence-required, no Pal execution, no auto-probe | PAL.md, AGENTS.md, SKILL.md | high | yes | no | low | yes |
| `palsmith-pal-governor` | `palsmith_governance_boundary` | spread across root entries | no-code governance; no automatic roster modification or runtime programs | root entries | high | yes | yes | wording must not overpromise | yes |
| `palsmith-pal-governor` | `no_keyword_routing_policy` | central policy only | false for keyword, domain, role, route maps | central roster, standard | high | yes | no | low | yes |
| `palsmith-pal-governor` | `external_project_write_policy` | implicit in boundary text | false-by-default, thin binding required | root entries, standards | high | yes | no | low | yes |
| `palsmith-pal-governor` | `agent_skill_refs_policy` | implicit in skills boundary | references only; no Agent Skill storage | skills index | high | yes | no | low | yes |
| `palsmith-pal-governor` | `credentials_allowed` | absent | false | standard | high | yes | no | low | yes |

## Summary

PalSmith is the lower-risk first real metadata update candidate because its current `pal.json` already has `name` and strong no-code governance boundary fields.

Mira remains a valid pilot candidate but should receive a human review pass for Main Pal role wording and legacy runtime-awareness wording before a real update.

