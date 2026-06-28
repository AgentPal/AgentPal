# Existing Pal Upgrade Report

Use this template when PalSmith reviews an existing Pal and prepares a v0.5 upgrade package.

## Target

- target Pal:
- target path:
- current version:
- intended upgrade target:
- review date:
- execution evidence:

## Decision

Use one:

- `pass`
- `partial`
- `missing`
- `not-run`
- `blocked`

Decision:

## Root Entry Completeness

| Required entry | Status | Evidence / note |
| --- | --- | --- |
| `README.md` | not-run | |
| `PAL.md` | not-run | |
| `pal.json` | not-run | |
| `AGENTS.md` | not-run | |
| `SKILL.md` | not-run | |

## `pal.json` Schema Readiness

| Check | Status | Evidence / note |
| --- | --- | --- |
| JSON parse | not-run | |
| id / name / display_name present | not-run | |
| role present | not-run | |
| direct_call present | not-run | |
| aliases present when needed | not-run | |
| no_runtime_code boundary present | not-run | |
| formal Skills listed accurately | not-run | |

## Index Completeness

| Index | Status | Evidence / note |
| --- | --- | --- |
| `knowledge/index.md` | not-run | |
| `skills/index.md` | not-run | |
| `workflows/index.md` | not-run | |
| `runbooks/index.md` | not-run | |
| `memory/index.md` | not-run | |
| `research/index.md` | not-run | |
| `learning/index.md` | not-run | |
| `examples/index.md` | not-run | |

## Skill-vs-Agent-Skill Risk

| Risk | Status | Evidence / note |
| --- | --- | --- |
| Agent Skill stored under Pal `skills/` | not-run | |
| Pal-owned Skill claims direct tool execution | not-run | |
| Runtime Skill candidate missing from task package boundary | not-run | |
| Skill availability claimed without current Runtime evidence | not-run | |

## Misplaced Content Risks

| Risk | Status | Evidence / note |
| --- | --- | --- |
| knowledge hidden inside Skill | not-run | |
| workflow hidden inside knowledge | not-run | |
| runbook mixed with report | not-run | |
| private memory in public asset | not-run | |
| report stored as durable knowledge | not-run | |
| external project `.agentpal/` used for central Pal assets | not-run | |

## Asset-Manifest Readiness

| Check | Status | Evidence / note |
| --- | --- | --- |
| required Minimal assets inventoried | not-run | |
| Standard assets inventoried when target is Standard | not-run | |
| source inventory present when user materials were used | not-run | |
| asset classification table present | not-run | |
| missing assets listed | not-run | |
| not-run checks listed | not-run | |

## Public Safety

| Check | Status | Evidence / note |
| --- | --- | --- |
| no credentials / tokens / secrets | not-run | |
| no private customer data | not-run | |
| no private user memory | not-run | |
| no private project memory | not-run | |
| no unapproved external project writes | not-run | |
| no connector / scanner / auto execution system | not-run | |
| no keyword routing map | not-run | |

## Recommended Fixes

| Priority | Fix | Target path | Confirmation needed | Evidence required |
| --- | --- | --- | --- | --- |
| P0 | | | yes | |

## Next Runtime Task Package

- allowed read paths:
- allowed write paths:
- forbidden paths:
- runtime_skill_candidates:
- pal_owned_skills_used:
- expected evidence:

## Residual Risks

- `not-run`:
- `missing`:
- `blocked`:
- unresolved user decisions:
