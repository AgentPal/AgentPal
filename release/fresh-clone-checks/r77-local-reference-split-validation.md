# R77 Local Reference Split Validation

Date: 2026-06-28

Scope: local clean-copy validation for the R77 second-pass root reference split. No GitHub, tag, Release, pull, fetch, or push operation was used.

## Summary

Result: pass

R77 moved or archived the low-risk root reference directories and left high-risk active protocol/reference directories in place with migration plans.

## Clean-Copy Simulation

Method:

- Built a local temporary copy from `git ls-files --cached --others --exclude-standard`.
- Excluded `.git` and ignored/private runtime files.
- Checked required public paths, JSON parsing, forbidden root directories, forbidden project-binding directories, official Pal count, and routing metadata.

Results:

| Check | Result |
| --- | --- |
| required paths missing | 0 |
| JSON parse failures | 0 |
| forbidden low-risk root dirs present | 0 |
| forbidden project-binding thick dirs present | 0 |
| official Pal count | 9 |
| `routing_policy` | `ai_judgement_only` |
| `keyword_routing_allowed` | `false` |
| low-risk target dirs exist | true |
| clean-copy pass | true |

Final staged-index clean-copy check:

| Check | Result |
| --- | --- |
| required paths missing | 0 |
| JSON parse failures | 0 |
| forbidden low-risk root dirs present | 0 |
| forbidden project-binding thick dirs present | 0 |
| official Pal count | 9 |
| `routing_policy` | `ai_judgement_only` |
| `keyword_routing_allowed` | `false` |
| staged-index clean-copy pass | true |

## Low-Risk Root Directory Result

These root directories are absent after R77:

- `projects/`
- `imports/`
- `memory/`
- `state/`
- `reports/`
- `response-fingerprints/`

Current locations:

| Old root path | Current location |
| --- | --- |
| `projects/` active protocols | `standards/project-binding/` |
| `projects/` legacy records/templates | `archive/migration-from-v0.3/root-legacy/projects/` |
| `imports/` | `workspace/resources/imports/` |
| `memory/` | `workspace/organization/memory/` |
| `state/` public placeholder | `archive/migration-from-v0.3/root-legacy/state/` |
| `state/` ignored runtime state | `.agentpal/local/state/` |
| `reports/` | `archive/migration-from-v0.3/root-legacy/reports/` |
| `response-fingerprints/` | `workspace/resources/response-fingerprints/` |

## Boundary Searches

`.agentpal/(memory|state|reports|context|index|pals|workflows|evals)` hits were classified as boundary language, forbidden-default lists, template checks, release evidence, archive compatibility, or regression-test expectations. No active thick-binding default behavior was found.

`keyword_map`, `domain_map`, and `role_map` hits were classified as forbidden, boundary, template-check, archive, release evidence, or regression-test contexts. No active keyword/domain/role routing behavior was found.

Central path hits confirmed the current facts:

- `workspace/organization/contacts/`
- `official/pals/`
- `templates/project-binding/`
- `workspace/projects/`

## High-Risk Plan Artifacts

- `docs/00-overview/capability-inventory-migration-plan.md`
- `docs/00-overview/orchestration-migration-plan.md`
- `docs/00-overview/prompts-migration-plan.md`
- `archive/migration-from-v0.3/root-legacy/capability-runtime-model-plugin-map.md`
- `archive/migration-from-v0.3/root-legacy/orchestration-split-map.md`
- `archive/migration-from-v0.3/root-legacy/prompts-split-map.md`

## Not Performed

- No `git push`
- No `git pull`
- No `git fetch`
- No tag creation or modification
- No GitHub Release creation or modification
- No CLI, app, scanner, validator, installer, daemon, database, auto sync, or auto execution engine
