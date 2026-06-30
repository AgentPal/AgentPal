# R203 Official Pal Entry Adoption Matrix

Status: Phase 1 entry adoption evidence.

R203 applied minimal Pal Asset Execution entry adoption across the 10 official
bundled Pals. This is not a full migration, not a per-Pal asset usage
regression, and not a verified-readiness promotion.

## Scope

- Official Pal count: 10
- Entry files updated per Pal: `SKILL.md` and `README.md`
- Files not changed: official `pal.json`, central contacts, real user custom
  Pal, R200 controlled-write fixture
- Contract baseline: `core/pal-asset-execution-contract.md` and
  `core/asset-loading-gate.md`

## Adoption Matrix

| Pal | Path | Entry files updated | Complex task path | Lightweight path | Tool boundary | Missing asset handling | Asset Use Summary requirement | No overclaim statement | Completeness level after R203 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Atlas | `official/pals/Atlas-developer` | `SKILL.md`, `README.md` | yes | yes | yes | yes | yes | yes | unchanged: `tool_aware_pal` |
| Faye | `official/pals/Faye-delivery` | `SKILL.md`, `README.md` | yes | yes | yes | yes | yes | yes | unchanged: `workflow_capable_pal` |
| Harper | `official/pals/Harper-writing` | `SKILL.md`, `README.md` | yes | yes | yes | yes | yes | yes | unchanged: `tool_aware_pal` |
| Mira | `official/pals/Mira-main` | `SKILL.md`, `README.md` | yes | yes | yes | yes | yes | yes | unchanged: `tool_aware_pal` |
| Morgan | `official/pals/Morgan-document` | `SKILL.md`, `README.md` | yes | yes | yes | yes | yes | yes | unchanged: `tool_aware_pal` |
| Nova | `official/pals/Nova-product` | `SKILL.md`, `README.md` | yes | yes | yes | yes | yes | yes | unchanged: `tool_aware_pal` |
| PalSmith | `official/pals/PalSmith-pal-governor` | `SKILL.md`, `README.md` | yes | yes | yes | yes | yes | yes | unchanged: scoped `verified_executable_pal` for Pal asset governance evidence only |
| Quinn | `official/pals/Quinn-quality` | `SKILL.md`, `README.md` | yes | yes | yes | yes | yes | yes | unchanged: `tool_aware_pal` |
| Rhea | `official/pals/Rhea-system` | `SKILL.md`, `README.md` | yes | yes | yes | yes | yes | yes | unchanged: `tool_aware_pal` |
| Vega | `official/pals/Vega-research` | `SKILL.md`, `README.md` | yes | yes | yes | yes | yes | yes | unchanged: `tool_aware_pal` |

## Entry Content Shape

Each official Pal received a short `SKILL.md` section named
`Pal Asset Execution`. The section says that substantive tasks must:

- apply the workspace Pal Asset Execution Contract and Asset Loading Gate;
- identify task type;
- load task-relevant Pal identity, knowledge, Skill, workflow, runtime-policy,
  memory, and eval assets;
- form a Task Asset Packet or equivalent plan;
- treat external tools and Agent Runtimes as execution tools, not Pal-owned
  capability assets;
- produce an Asset Use Summary or equivalent evidence when needed;
- use a Missing Asset Plan or honest limited fallback if required assets are
  missing.

Each official Pal also received a short `README.md` note stating that Phase 1
entry adoption is enabled and does not complete full verified migration for
every task family.

## Decision

Decision: `official_pal_entry_adoption_phase_1_complete_with_future_regression_required`.

R203 closes the entry-declaration gap found in R202. It does not close Phase 2
Task Asset Packet examples or Phase 3 per-Pal representative regressions.
