# R103-D Official Pal Index Backfill Integration Gate

Date: 2026-06-28

## Purpose

This PalBench gate defines the integration checks for the next R104 integration round after R103-A, R103-B, and R103-C complete their parallel work.

R103-D does not modify `official/pals/**`, does not read parallel-thread final output as a precondition, and does not approve any Batch 2 / Batch 3 / PalSmith pilot change by itself. It creates the gate, checklist, and issue shape that a later integration owner can use against the final combined worktree.

## Scope

Use this gate when integrating:

- Batch 2 official Pal memory README / index backfill;
- Batch 3 official Pal memory README / index backfill;
- PalSmith runbooks README pilot, if that pilot is completed and separately approved;
- the validation and integration notes produced by R103-A, R103-B, and R103-C.

The gate is documentation and evidence policy only. It is not a scanner, validator, installer, connector, runtime, or auto-execution program.

## Baseline References

Read before running this gate:

- `private completion report outside the public repository`
- `evals/palbench/pal-asset/r100d-pal-metadata-upgrade-compatibility-gate.md`
- `templates/pal-asset/safe-index-backfill-guide.md`
- `release/integration-notes/r100b-official-pal-safe-index-file-plan.md`
- `release/integration-notes/r102-official-pal-index-backfill-batch1-summary.md`
- `workspace/organization/contacts/pals.json`

If any reference is missing in a future integration workspace, record it as `missing`; do not substitute an unrelated source.

## Gate 1: R103-A / R103-B / R103-C Outputs Exist

The R104 integration round must verify that the parallel-thread outputs exist before accepting the combined batch.

| Check | Required Result |
| --- | --- |
| R103-A public files exist | pass or documented `missing` issue |
| R103-B public files exist | pass or documented `missing` issue |
| R103-C public files exist | pass or documented `missing` issue |
| R103-A validation exists | pass or documented `missing` issue |
| R103-B validation exists | pass or documented `missing` issue |
| R103-C validation exists | pass or documented `missing` issue |
| R103-A/B/C integration notes exist | pass or documented `missing` issue |
| R103-A/B/C internal reports exist under `private completion report outside the public repository` | pass or documented `missing` issue |

Do not infer completion from a commit message alone. The evidence must be the current files and validation records.

## Gate 2: Selected Pal Index / README Files Exist

For every Pal selected by R103-A, R103-B, or R103-C, verify the expected README or index file exists in the exact selected directory.

The integration owner must classify each selected file:

| Classification | Meaning |
| --- | --- |
| `present` | exact expected file exists |
| `missing` | expected file does not exist |
| `unexpected-path` | file exists in a different path than the thread claimed |
| `out-of-scope` | file exists but was not part of the allowed thread scope |
| `needs-review` | file exists but content needs human or owner-Pal review before acceptance |

At minimum, the integration round must check:

- selected Batch 2 Pal `memory/README.md` or approved index files;
- selected Batch 3 Pal `memory/README.md` or approved index files;
- PalSmith `runbooks/README.md` if the pilot thread completed it;
- each selected Pal's root entries still exist.

## Gate 3: No `pal.json` Diff

R103 index backfill is navigation-only. It must not modify official Pal metadata.

| Check | Required Result |
| --- | --- |
| `git diff -- official/pals/**/pal.json` | empty |
| staged diff for `official/pals/**/pal.json` | empty |
| committed R103 range changes to `official/pals/**/pal.json` | none |

If any official Pal `pal.json` changed, fail the integration gate unless a separate approved metadata thread is explicitly included. R103-D does not provide that approval.

## Gate 4: No Official `asset-manifest.json` Generated

R103 index backfill must not generate real official Pal manifests.

| Check | Required Result |
| --- | --- |
| official `asset-manifest.json` additions | 0 |
| official `asset-manifest.json` diffs | 0 |
| manifest-like generated indexes claiming runtime authority | 0 |

If a manifest appears, treat it as an issue against R100-D unless a separate manifest-generation thread approved it.

## Gate 5: Central Roster Unchanged

| Check | Required Result |
| --- | --- |
| `workspace/organization/contacts/pals.json` parses | pass |
| registered Pal count | 9 |
| active Pal count | 9 |
| every `pack_path` exists | pass |
| `routing_policy` | `ai_judgement_only` |
| `keyword_routing_allowed` | `false` |
| central contacts diff | empty |

Do not accept any R103 index backfill that changes central contacts, contact cards, capability cards, registry source of truth, or default receiver behavior.

## Gate 6: Official Pal Count And Loadability

| Check | Required Result |
| --- | --- |
| official Pal directory count | 9 |
| every official Pal `pal.json` parses | pass |
| every official Pal has `PAL.md` | pass |
| every official Pal has `AGENTS.md` | pass |
| every official Pal has `SKILL.md` | pass |
| selected Pal root files unchanged unless separately allowed | pass |

Missing optional asset directories are warnings. Missing root entries or broken `pal.json` files block the affected integration.

## Gate 7: No Keyword Routing

R103 files must not introduce deterministic semantic routing.

Fail if any changed R103 public file or official Pal file adds active:

- keyword route map;
- domain route map;
- hard-coded role dispatch table;
- deterministic owner selection table;
- language claiming Core performs semantic dispatch.

Documentation may mention forbidden route-map concepts only as prohibited examples or checks.

## Gate 8: No Connector / Scanner / Marketplace Program

R103 files must remain Markdown / JSON governance artifacts.

Fail if a changed file introduces:

- connector;
- external business system API client;
- scanner;
- validator;
- installer;
- daemon;
- database;
- marketplace / hub program;
- auto sync;
- auto execution;
- automatic Runtime / Skill / plugin / MCP / business-system probing;
- new dependency manifest or executable code.

## Gate 9: No Credentials Or Private Data

Fail if changed files contain:

- credentials;
- tokens;
- secrets;
- cookies;
- API keys;
- passwords;
- private customer data;
- private user memory;
- private project evidence;
- raw logs copied from private systems.

If a file only contains safety language such as "do not store credentials", record that as a non-issue.

## Gate 10: No External Project `.agentpal`

R103 integration must preserve thin binding.

| Check | Required Result |
| --- | --- |
| external project `.agentpal/pals` additions | 0 |
| external project `.agentpal/skills` additions | 0 |
| Pal README / index copied into external projects | 0 |
| external project manifest copied from official Pal | 0 |

Central Pal assets stay in the AgentPal Workspace. External projects must not become the source of truth for Pal assets.

## Gate 11: No Untracked R103 Files Left

Before integration commit, run `git status --short` and classify all R103-looking files.

| Status | Required Action |
| --- | --- |
| expected and in scope | stage in the integration commit |
| expected but missing | create issue from the R103-D issue template |
| other-thread file present | do not stage until owner and scope are confirmed |
| out-of-scope untracked file | leave untracked and record as issue |
| generated or unsafe file | remove only with explicit approval; otherwise block |

No untracked R103 files may be silently ignored in the final integration report.

## Gate 12: Clean-Copy Pass

The integration round must verify the combined committed state, not only the working tree before commit.

Clean-copy evidence may come from a fresh clone, a clean local copy, or an equivalent clean checkout when fresh clone is not available. If no clean-copy check is run, record `not-run` with reason and do not claim clean-copy pass.

Required clean-copy checks:

- required R103-A/B/C files exist;
- R103-D gate/checklist/template/validation exist;
- central roster parses and remains 9 / 9;
- official Pal count is 9;
- all official Pal `pal.json` files parse;
- no official Pal `pal.json` diff in the integrated range;
- no official `asset-manifest.json`;
- no active keyword routing;
- no connector / scanner / marketplace program;
- no credential leak;
- no external project `.agentpal` writes.

## Decision Rules

| Evidence | Decision |
| --- | --- |
| all gates pass and clean-copy pass exists | `pass` |
| all gates pass but clean-copy is not run | `pass-with-not-run-clean-copy` only if user accepts the residual risk |
| any selected file missing | `fail` or `needs-repair` |
| `pal.json` diff appears | `fail` |
| official manifest appears | `fail` |
| central roster changes | `fail` |
| keyword routing, connector, scanner, credential, or external project asset copy appears | `fail` |
| evidence cannot be collected | `blocked` or `needs-more-evidence` |

## Issue Handling

Use `release/integration-notes/r103d-official-pal-index-backfill-issue-template.md` for every missing, unsafe, ambiguous, or out-of-scope finding.

Do not fix official Pal assets during R103-D. Future integration fixes must respect the original owner thread scope and the allowed paths for the integration round.

## Non-Goals

This gate does not:

- modify official Pal assets;
- approve R103-A/B/C results before they exist;
- generate real manifests;
- edit central roster;
- create automation;
- run clean-copy checks by itself;
- push, tag, fetch, pull, or release.
