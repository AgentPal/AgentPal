# R80 Local Capability Template Navigation Validation

Date: 2026-06-28

Scope: local-only validation for Capability Inventory template naming, runtime example disambiguation, and four-source navigation after R79 root pointer archival.

No GitHub synchronization, push, pull, fetch, tag, or Release action was performed.

## Directory Evidence

| Check | Result |
| --- | --- |
| Working directory | `J:\开发\AgentPal` |
| Git top level | `J:\开发\AgentPal` |
| Root `capabilities/` exists | false |
| Root `runtime/` exists | false |
| Root `models/` exists | false |
| Root `plugins/` exists | false |
| Old `templates/capabilities/` exists | false |
| New `templates/capability-inventory/` exists | true |
| Old `examples/runtime/` exists | false |
| Runtime adapter examples `examples/runtime-adapters/` exists | true |
| Standards source `standards/capability-inventory/` exists | true |
| Current organization records `workspace/organization/capability-inventory/` exists | true |
| Examples source `examples/capability-inventory/` exists | true |
| Legacy archive `archive/migration-from-v0.3/root-legacy/capability-inventory/` exists | true |
| Thin binding templates `templates/project-binding/` exists | true |
| Central project template `workspace/projects/_template/` exists | true |
| Official Pal directory `official/pals/` exists | true |

## R80 Move Decisions

| Before | After | Decision |
| --- | --- | --- |
| `templates/capabilities/` | `templates/capability-inventory/` | renamed because it contained Capability Inventory JSON profile templates |
| `examples/runtime/README.md` | `examples/runtime-adapters/README.md` | moved because it was runtime adapter / quickstart navigation, not runtime profile examples |

No compatibility directory was left at `templates/capabilities/` or `examples/runtime/`.

## Capability Inventory Navigation

| Asset class | Current path |
| --- | --- |
| Standards and rules | `standards/capability-inventory/` |
| Current organization records / no-code profiles | `workspace/organization/capability-inventory/` |
| Examples | `examples/capability-inventory/` |
| Copyable templates | `templates/capability-inventory/` |
| Legacy archive | `archive/migration-from-v0.3/root-legacy/capability-inventory/` |

Navigation document: `docs/00-overview/capability-inventory-navigation.md`.

## Search Classification

| Check | Result | Evidence |
| --- | --- | --- |
| Active `templates/capabilities/` target | 0 active targets | remaining hits are R80 audit/history or R79 validation notes |
| Active `examples/runtime/` target | 0 active targets | remaining hits are R80 audit/history or R79 validation notes |
| Thick project binding bug | 0 active bugs | `.agentpal/memory`, `.agentpal/state`, `.agentpal/reports`, `.agentpal/context`, `.agentpal/index`, `.agentpal/pals`, `.agentpal/workflows`, and `.agentpal/evals` hits are forbidden lists, boundary language, archive records, release evidence, or regression expectations |
| Active keyword route JSON keys | 0 | exact JSON key search for `"keyword_map"`, `"domain_map"`, and `"role_map"` returned no matches |
| Active keyword routing bug | 0 active bugs | text hits are forbidden, boundary, template-check, archive, release evidence, or regression-test contexts |
| Active scanner / validator / automatic scan claim | 0 active bugs | hits are no-code boundary, known limitation, Pal boundary, example/failure, or release evidence contexts |
| Active root pointer facts source | 0 active bugs | root `capabilities/`, `runtime/`, `models/`, and `plugins/` hits are archive/history, negative guidance, non-root memory paths, or current nested capability inventory paths |

## JSON And Roster Checks

| Check | Result |
| --- | --- |
| Visible JSON files parsed | 76 |
| JSON parse failures | 0 |
| Official Pal dirs | 9 |
| Central registered Pals | 9 |
| Central active Pals | 9 |
| `routing_policy` | `ai_judgement_only` |
| `keyword_routing_allowed` | false |

## Clean Copy Check

Local clean-copy path: `C:\Users\ADMINI~1\AppData\Local\Temp\agentpal-r80-clean-copy-20260628014915`

| Check | Result |
| --- | --- |
| Copied files from `git ls-files --cached --others --exclude-standard` | 2781 |
| Required paths missing | 0 |
| Forbidden legacy/current-confusing paths present | 0 |
| Clean-copy JSON files parsed | 49 |
| Clean-copy JSON failures | 0 |
| Clean-copy JSON route key hits | 0 |
| Official Pal dirs | 9 |
| Central registered Pals | 9 |
| Central active Pals | 9 |
| `routing_policy` | `ai_judgement_only` |
| `keyword_routing_allowed` | false |

Clean-copy gates passed:

- required paths missing = 0
- JSON failures = 0
- forbidden legacy/current-confusing paths present = 0
- private/runtime leak = 0
- active thick binding bug = 0
- active keyword routing bug = 0
- active scanner/validator/auto scan claim = 0

## Boundary Summary

R80 did not add a CLI, app, scanner, validator, daemon, database, automatic sync, automatic execution engine, keyword router, deterministic semantic router, or runtime capability probe.

R80 kept external project binding thin: project-local `.agentpal/` remains an entrypoint surface only, while project memory, reports, source maps, governance records, and capability inventory belong in central AgentPal workspace records.
