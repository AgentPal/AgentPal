# R79 Local Capability Root Pointer Cleanup Validation

Date: 2026-06-28

Scope: local-only validation for archiving the remaining root `capabilities/`, `runtime/`, `models/`, and `plugins/` README pointer directories after R78.

Remote actions: not run. This validation did not use `git push`, `git pull`, `git fetch`, tag commands, or GitHub Release commands.

## Directory Evidence

| Check | Result |
| --- | --- |
| Working directory | `J:\开发\AgentPal` |
| Git branch state before commit | `master...origin/master [ahead 4]` |
| Root `capabilities/` exists | false |
| Root `runtime/` exists | false |
| Root `models/` exists | false |
| Root `plugins/` exists | false |
| Archived `capabilities/README.md` pointer exists | true |
| Archived `runtime/README.md` pointer exists | true |
| Archived `models/README.md` pointer exists | true |
| Archived `plugins/README.md` pointer exists | true |

Archived pointer root:

`archive/migration-from-v0.3/root-legacy/capability-inventory/root-pointers/`

## Active Capability Inventory Sources

| Source | Status |
| --- | --- |
| `standards/capability-inventory/` | exists |
| `workspace/organization/capability-inventory/` | exists |
| `examples/capability-inventory/` | exists |
| `archive/migration-from-v0.3/root-legacy/capability-inventory/` | exists as historical migration evidence |

## Validation Results

| Check | Result | Evidence |
| --- | --- | --- |
| Required paths missing | 0 | 15 required paths checked in working tree; 16 required paths checked in clean-copy validation including this report |
| Visible JSON parse failures | 0 | 76 visible `.json` files parsed with PowerShell `ConvertFrom-Json` |
| Official Pal directories | 9 | `official/pals/` directory count |
| Central roster registered Pals | 9 active / 9 registered | `workspace/organization/contacts/pals.json` `registered_pals` |
| Roster routing policy | pass | `routing_policy=ai_judgement_only` |
| Keyword routing allowed | pass | `keyword_routing_allowed=false` |
| Active keyword route JSON keys | 0 | recursive JSON key search for `keyword_map`, `domain_map`, `role_map` |
| Thick project binding bug | 0 active bugs found | `.agentpal/memory`, `.agentpal/state`, `.agentpal/reports`, `.agentpal/context`, `.agentpal/index`, `.agentpal/pals`, `.agentpal/workflows`, and `.agentpal/evals` hits are forbidden lists, boundary language, archive records, release evidence, or regression expectations |
| Private/runtime leak | 0 confirmed leaks | 5 tracked `memory/runtime` candidates were public-safe README/protocol placeholders, not private runtime state |
| Active scanner / validator / auto scan claim | 0 active claims found | hits are no-code boundary, forbidden scope, known limitation, or regression/failure examples |
| Root capability pointer dirs | absent | `capabilities=False; runtime=False; models=False; plugins=False` |
| Capability inventory target dirs | present | standards, workspace organization records, examples, and archive target all exist |

## Reference Classification

Search hits for `capabilities/`, `runtime/`, `models/`, and `plugins/` after R79 are classified as:

- historical migration or release validation evidence,
- archive pointer explanations,
- negative tests or Pal Pack cleanup examples,
- R79-era non-root paths that R80 later renamed, such as `templates/capabilities/` and `examples/runtime/`,
- non-root paths such as `memory/runtime/` or `workspace/organization/memory/runtime/`,
- current active paths under `workspace/organization/capability-inventory/plugins/` and `workspace/organization/capability-inventory/models/`.

No active entrance document now uses root `capabilities/`, `runtime/`, `models/`, or `plugins/` as a current facts source.

## Clean-Copy Result

Local clean-copy style verification: pass.

R79 used a temporary local copy of the current Git-visible file set rather than remote clone, pull, fetch, push, tag, or GitHub Release actions. The clean copy included 2776 files and returned:

- missing required paths: 0
- forbidden root dirs present: 0
- JSON failures: 0
- official Pal dirs: 9
- registered Pals: 9
- active registered Pals: 9
- `routing_policy=ai_judgement_only`
- `keyword_routing_allowed=false`

Required public paths are present, deprecated root pointer directories are absent, JSON parses, central roster count and routing policy pass, and boundary searches show no active thick binding, keyword routing, or automatic scanner behavior.

## Non-Goals

R79 did not add a CLI, Web App, Desktop App, scanner, validator, installer, daemon, database, automatic sync, automatic execution engine, keyword router, deterministic semantic router, tag, GitHub Release, or remote synchronization.
