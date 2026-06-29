# R143 Local Mira / PalSmith / Faye Auto Behavior Validation

Status: pass.

Validation date: 2026-06-29.

Scope: local validation for the R143 Mira / PalSmith / Faye auto behavior test execution artifacts. This validation does not prove all AgentPal behavior tests are complete; it only validates the R143 first staged slice.

## Artifact Checks

| check | result | evidence |
| --- | --- | --- |
| Mira results exist | pass | `evals/palbench/v0.5/behavior/r143-mira-auto-behavior-results.md` |
| PalSmith results exist | pass | `evals/palbench/v0.5/behavior/r143-palsmith-auto-behavior-results.md` |
| Faye results exist | pass | `evals/palbench/v0.5/behavior/r143-faye-auto-behavior-results.md` |
| summary exists | pass | `evals/palbench/v0.5/behavior/r143-mira-palsmith-faye-auto-behavior-summary.md` |
| issues exists | pass | `evals/palbench/v0.5/behavior/r143-mira-palsmith-faye-auto-behavior-issues.md` |
| all required tests executed | pass | Mira 12, PalSmith 12, Faye 12, total 36 |
| JSON parse pass | pass | 105 / 105 visible `.json` files parsed |
| `agentpal.json` parse pass | pass | `agentpal.json` parsed |
| central roster unchanged | pass | 9 registered / 9 active; no `workspace/organization/contacts/` diff |
| official Pal unchanged | pass | 9 official Pal dirs; 9 / 9 official `pal.json` parsed; no `official/pals/` diff |
| no keyword routing | pass | no active route map added; raw exact-key hits are existing schema prohibition examples or old validation text |
| no connector / scanner / marketplace program | pass | no executable code added; forbidden feature flags remain false |
| no credential / customer-private leak | pass | credential-shaped raw hits are the documented fake `DO_NOT_USE_EXAMPLE_TOKEN` negative example and prior validation notes |
| no internal path leak | pass | internal development path scan returned 0 hits |
| no external project `.agentpal/delivery-pack` write | pass | scan from parent workspace returned 0 delivery-pack directories under external `.agentpal` |
| clean-copy pass | pass | `agentpal-r143-clean-ab9dd9c16c2f479cb383776af1ad589b`; required R143 paths missing 0; JSON 105 / 105 parsed |

## Test Counts

| target | expected | observed | result |
| --- | ---: | ---: | --- |
| Mira | 12 | 12 | pass |
| PalSmith | 12 | 12 | pass |
| Faye role | 12 | 12 | pass |
| Total | 36 | 36 | pass |

## Scan Classification

| scan | raw_hits | classification | result |
| --- | ---: | --- | --- |
| internal path leak | 0 | no public repo hit | pass |
| hidden release claim | 1 | historical negative line: `tag created in R74: no`; no positive release claim | pass |
| exact route-map JSON key strings | 11 | existing schema `not` prohibitions plus old validation text; no active route-map data added | pass |
| forbidden true flags | 0 | none | pass |
| credential-shaped strings | 8 | fake `DO_NOT_USE_EXAMPLE_TOKEN` negative example plus old validation notes | pass |

## Git / Protected Surface Check

| protected surface | result | evidence |
| --- | --- | --- |
| central roster | pass | `git status --porcelain=v1 workspace/organization/contacts` returned no changed files |
| official Pal files | pass | `git status --porcelain=v1 official/pals` returned no changed files |
| README / README.zh-CN | pass | not modified |
| runtime code / executable program | pass | no code, connector, scanner, validator, daemon, app, CLI, or installer added |

## Boundary

Not performed:

- no manual testing;
- no R144/R145/R146 test execution;
- no push, pull, fetch, tag, GitHub Release, or GitHub API;
- no remote publication;
- no connector, scanner, validator, marketplace, installer, daemon, database, API client, auto-sync engine, or auto-execution engine;
- no central roster mutation;
- no official Pal mutation;
- no external project `.agentpal/delivery-pack` write;
- no real customer data or credential write.

## Result

R143 local validation passed. R143 is ready for local checkpoint commit and the R144 readiness decision is `ready_for_official_pal_asset_behavior_tests`.
