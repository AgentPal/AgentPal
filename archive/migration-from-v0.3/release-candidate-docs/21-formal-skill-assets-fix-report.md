# Formal Skill Assets Fix Report

Date: 2026-06-26

Status: R13 release-readiness fix report.

## Before R13

R12 reported:

- Total formal skills: 219.
- Missing under old directory-only check: 115.
- Cause: old check did not count Flat Skill Cards such as `skills/runtime-task-package-writing-skill.md`.

## R13 Standard

R13 defines `docs/03-pal-pack-standard/15-formal-skill-assets.md`.

Valid representations:

- Flat Skill Card: `skills/<formal-skill-id>.md`.
- Directory Skill Package: `skills/<formal-skill-id>/SKILL.md` or `skills/<formal-skill-id>/README.md`.
- Index mapping: `skills/skill-asset-map.md` records the formal ID to actual asset path.

Invalid representations:

- `pal.json` declaration only.
- index-only mention with no actual skill file.
- empty directory or empty README created only to satisfy a check.

## Fix Result

| Metric | Result |
| --- | ---: |
| Total formal skills | 219 |
| Mapped skills under R13 standard | 219 |
| Missing skills under R13 standard | 0 |
| Flat Skill Cards mapped | 115 |
| Directory Skill Packages mapped | 104 |
| New skill files created | 0 |
| New skill asset maps created | 9 |
| Mapping-only index / README fixes | 9 |
| Empty placeholder skill files created | 0 |
| Deferred formal-skill P2 issues | 0 |

## Per-Pal Result

| Pal path | formal_skill_count | formal_skills count | mapped assets | missing assets | new skill files | mapping-only fixes |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| `pals/Mira-main` | 28 | 28 | 28 | 0 | 0 | 1 map + index entry |
| `pals/PalSmith-pal-governor` | 15 | 15 | 15 | 0 | 0 | 1 map + README entry |
| `pals/Atlas-developer` | 24 | 24 | 24 | 0 | 0 | 1 map + index entry |
| `pals/Vega-research` | 27 | 27 | 27 | 0 | 0 | 1 map + index entry |
| `pals/Rhea-system` | 24 | 24 | 24 | 0 | 0 | 1 map + index entry |
| `pals/Quinn-quality` | 24 | 24 | 24 | 0 | 0 | 1 map + index entry |
| `pals/Morgan-document` | 25 | 25 | 25 | 0 | 0 | 1 map + index entry |
| `pals/Harper-writing` | 25 | 25 | 25 | 0 | 0 | 1 map + index entry |
| `pals/Nova-product` | 27 | 27 | 27 | 0 | 0 | 1 map + index entry |

## PalSmith Source Lineage

PalSmith now has:

- `pals/PalSmith-pal-governor/research/source-inventory.md`
- `pals/PalSmith-pal-governor/research/source-coverage-matrix.md`
- `pals/PalSmith-pal-governor/skills/skill-asset-map.md`
- `pals/PalSmith-pal-governor/skills/README.md`
- `pals/PalSmith-pal-governor/pal.json`

PalSmith's formal skills for job fitness, content preservation, user-material ingestion, web-research-to-knowledge, quality inspection, import/export, version governance, and readiness review all map to actual flat skill cards.

## Official Field Strategy

R13 adds `evals/palbench/v0.5/documentation/archive/docs/08-release-candidate/official-pal-field-strategy-decision.md`.

Decision: for v0.1.0-rc.1, the official bundled Pal set is determined by `agentpal.json`, `registry/pal.index.json`, and `contacts/pals.json`. Individual Pal `pal.json` files may keep existing `official` metadata, but R13 does not perform broad schema churn.

## No-Code Boundary

R13 created only Markdown assets and updated Markdown documentation. It did not create scripts, tools, CLIs, scanners, validators, installers, daemons, UIs, package manifests, or runtime dependencies.

## Verification Snapshot

R13 local verification:

| Check | Result |
| --- | --- |
| JSON parse | 12 JSON files passed |
| `agentpal.json` official bundled Pals | 9 |
| `contacts/pals.json` registered Pals | 9 |
| `registry/pal.index.json` items | 9 |
| formal skills total | 219 |
| mapped formal skills | 219 |
| flat cards | 115 |
| directory packages | 104 |
| missing formal Skill assets | 0 |
| Pal maps present | 9 |
| forbidden code/package files | 0 |
| tool-like directories | 1, `imports/tools` documentation-resource exception |
| runtime output paths in Git status | 0 |
| content-depth sample | 5 sampled flat cards had 11 required method headings and 0 TODO-like placeholders |
| `git diff --check` | Pass; LF-to-CRLF warnings only |
| `git status --short` visible entries | 593 |
| `git ls-files --others --exclude-standard` untracked files | 641 |
| `git diff --stat` | 133 files changed, 3044 insertions, 2735 deletions |

## Release-Readiness Judgement

The R12 formal Skill asset P2 is handled under the R13 standard. AgentPal can enter a more reliable maintainer stage / commit review, with publish readiness still dependent on manual dirty-worktree staging, remote confirmation, tag strategy, and GitHub Release review.
