# R108-D Official Pal Index Integration Gate

Date: 2026-06-28

## Purpose

This PalBench gate defines the integration checks for the next R109 integration round after R108-A, R108-B, and R108-C complete their parallel work.

R108-D does not modify `official/pals/**`, does not depend on final R108-A/B/C results, and does not approve any official Pal index or audit work by itself. It creates the gate, checklist, and issue template that R109 must use against the final combined worktree.

## Scope

Use this gate when integrating:

- R108-A Mira skills index work, if completed;
- R108-B PalSmith skills index work, if completed;
- R108-C Mira root-entry wording audit, if completed;
- all validation records, integration notes, and internal reports produced by R108-A/B/C.

This gate is documentation and evidence policy only. It is not a scanner, validator, installer, connector, runtime, marketplace program, or auto-execution tool.

## Baseline References

Read before running this gate:

- `private completion report outside the public repository`
- `private completion report outside the public repository`
- `evals/palbench/pal-asset/r100d-pal-metadata-upgrade-compatibility-gate.md`
- `templates/pal-asset/safe-index-backfill-guide.md`
- `workspace/organization/contacts/pals.json`

If any reference is missing in the future R109 workspace, record it as `missing`; do not substitute unrelated evidence.

## Gate 1: R108-A / R108-B / R108-C Outputs Exist

The R109 integration round must verify the real output files from the parallel threads.

| Check | Required Result |
| --- | --- |
| R108-A public files exist | pass or documented issue |
| R108-B public files exist | pass or documented issue |
| R108-C audit exists | pass or documented issue |
| R108-A validation exists | pass or documented issue |
| R108-B validation exists | pass or documented issue |
| R108-C validation or audit evidence exists | pass or documented issue |
| R108-A/B/C integration notes exist | pass or documented issue |
| R108-A/B/C internal reports exist under `private completion report outside the public repository` | pass or documented issue |

Do not infer completion from branch position, commit message, or directory presence alone.

## Gate 2: Mira Skills Index Exists If R108-A Complete

If R108-A completes Mira skills index work, verify:

| Expected File | Required Result |
| --- | --- |
| `official/pals/Mira-main/skills/index.md` or approved equivalent | present |
| R108-A validation | records exact changed paths and not-run items |
| R108-A internal report | exists outside the public repo |

Mira is the Main Pal / Leader Pal / Conductor. The skills index must preserve Mira's owner-routing boundary and must not create keyword routing, deterministic role maps, automatic execution, or external project asset copies.

## Gate 3: PalSmith Skills Index Exists If R108-B Complete

If R108-B completes PalSmith skills index work, verify:

| Expected File | Required Result |
| --- | --- |
| `official/pals/PalSmith-pal-governor/skills/index.md` or approved equivalent | present |
| R108-B validation | records exact changed paths and not-run items |
| R108-B internal report | exists outside the public repo |

PalSmith skills index work must preserve the Pal Skill / Agent Skill boundary. Agent Skill files, plugin metadata, MCP tools, code, dependency manifests, scanner configs, validator logic, connector configs, and tool installation docs must not be copied into Pal `skills/`.

## Gate 4: Mira Root-Entry Wording Audit Exists

If R108-C audits Mira root-entry wording, verify:

| Expected Evidence | Required Result |
| --- | --- |
| Mira root-entry wording audit note | present |
| exact audited root-entry files | recorded |
| old `.agentpal` wording findings | recorded as pass / issue / accepted-risk |
| no unapproved root-entry rewrite | pass |

If R108-C changes root-entry wording, the integration must verify the change was explicitly in scope and did not alter Mira behavior, routing, direct calls, output contracts, or runtime claims.

## Gate 5: Prior Backfilled Indexes Still Exist

R109 must verify that earlier index / README backfills are still present:

| Prior Backfill Area | Required Result |
| --- | --- |
| R102/R103 memory README backfills | still present for accepted Pals |
| R103-C PalSmith runbooks README | still present |
| R105 Mira memory / research README | still present |
| R106-A PalSmith memory / research README | still present |
| R106-B Atlas / Quinn / Morgan skills index | still present |
| R106-C Nova / Vega / Harper / Rhea skills index | still present |
| R106-D skills integration gate files | still present |
| R107 integration summary / eval / validation | still present |

If a prior file is missing, record an issue before accepting R108 integration.

## Gate 6: No `pal.json` Diff

R108 index and audit work is documentation-only.

| Check | Required Result |
| --- | --- |
| `git diff -- official/pals/**/pal.json` | empty |
| staged diff for `official/pals/**/pal.json` | empty |
| integrated R108 commit range changes to `official/pals/**/pal.json` | none |

Any official Pal `pal.json` diff fails the integration gate unless a separate metadata task explicitly authorizes it. R108-D does not grant that authorization.

## Gate 7: No Official `asset-manifest.json` Generated

R108 must not generate real official Pal manifests.

| Check | Required Result |
| --- | --- |
| official `asset-manifest.json` additions | 0 |
| official `asset-manifest.json` diffs | 0 |
| manifest-like generated files claiming runtime authority | 0 |

If a manifest appears, fail against the R100-D compatibility boundary unless a separate manifest-generation thread approved it.

## Gate 8: Central Roster Unchanged

| Check | Required Result |
| --- | --- |
| `workspace/organization/contacts/pals.json` parses | pass |
| registered Pal count | 9 |
| active Pal count | 9 |
| every `pack_path` exists | pass |
| `routing_policy` | `ai_judgement_only` |
| `keyword_routing_allowed` | `false` |
| central contacts diff | empty |

Do not accept any R108 result that changes central contacts, contact cards, capability cards, default receiver, or roster source of truth.

## Gate 9: Official Pal Count And Loadability

| Check | Required Result |
| --- | --- |
| official Pal directory count | 9 |
| every official Pal `pal.json` parses | pass |
| every official Pal has `PAL.md` | pass |
| every official Pal has `AGENTS.md` | pass |
| every official Pal has `SKILL.md` | pass |
| selected Pal root files unchanged unless separately allowed | pass |

Missing optional asset directories are warnings. Missing root entries or broken `pal.json` files block the affected integration.

## Gate 10: No Keyword Routing

R108 files must not introduce deterministic semantic routing.

Fail if changed R108 files add active:

- keyword route map;
- domain route map;
- hard-coded role dispatch table;
- deterministic owner selection table;
- language claiming Core performs semantic dispatch.

Documentation may mention route-map concepts only as prohibited examples or checks.

## Gate 11: No Connector / Scanner / Marketplace Program

R108 files must remain Markdown / JSON governance artifacts.

Fail if a changed file introduces:

- connector;
- external business system API client;
- scanner;
- validator;
- installer;
- daemon;
- database;
- marketplace or hub program;
- auto sync;
- auto execution;
- automatic Runtime / Skill / plugin / MCP / business-system probing;
- executable code or dependency manifest.

## Gate 12: No Credentials Or Private Data

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
- full report bodies copied into memory;
- raw research content promoted directly to knowledge.

Safety language such as "do not store credentials" is not a credential finding.

## Gate 13: No External Project `.agentpal`

R108 integration must preserve thin binding.

| Check | Required Result |
| --- | --- |
| external project `.agentpal/pals` additions | 0 |
| external project `.agentpal/skills` additions | 0 |
| external project `.agentpal/workflows` additions | 0 |
| external project `.agentpal/runbooks` additions | 0 |
| external project `.agentpal/memory` additions | 0 |
| external project `.agentpal/reports` additions | 0 |
| external project `.agentpal/asset-manifest` additions | 0 |
| external project `.agentpal/pal-asset` additions | 0 |

Central Pal assets stay in the AgentPal Workspace. External projects must not become the Pal asset source of truth.

## Gate 14: No Untracked R108 Files Left

Before integration commit, run `git status --short` and classify all R108-looking files.

| Status | Required Action |
| --- | --- |
| expected and in scope | stage in the integration commit |
| expected but missing | create issue from the R108-D issue template |
| other-thread file present | do not stage until owner and scope are confirmed |
| out-of-scope untracked file | leave untracked and record as issue |
| generated or unsafe file | remove only with explicit approval; otherwise block |

No untracked R108 file may be silently ignored in the final integration report.

## Gate 15: Clean-Copy Pass

The R109 integration owner must verify the combined committed state, not only a pre-commit working tree.

Clean-copy evidence may come from a fresh clone, clean local copy, or equivalent clean checkout. If no clean-copy check is run, record `not-run` with reason and do not claim clean-copy pass.

Required clean-copy checks:

- required R108-A/B/C files exist;
- R108-D gate/checklist/template/validation exist;
- all prior accepted backfilled memory / skills / runbooks README/index files still exist;
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
| all gates pass but clean-copy is not run | `pass-with-not-run-clean-copy` only if user accepts residual risk |
| any expected R108-A/B/C file missing without a documented no-write decision | `fail` or `needs-repair` |
| prior accepted backfill file missing | `fail` or `needs-repair` |
| Agent Skill content is copied into Pal `skills/` | `fail` |
| report body is copied into memory | `fail` |
| raw research is promoted directly to knowledge | `fail` |
| `pal.json` diff appears | `fail` |
| official manifest appears | `fail` |
| central roster changes | `fail` |
| keyword routing, connector, scanner, credential, or external project asset copy appears | `fail` |
| evidence cannot be collected | `blocked` or `needs-more-evidence` |

## Issue Handling

Use `release/integration-notes/r108d-official-pal-index-integration-issue-template.md` for every missing, unsafe, ambiguous, stale, or out-of-scope finding.

Do not fix official Pal assets during R108-D. Future R109 fixes must respect the owner thread scope and the integration round's allowed paths.

## Non-Goals

This gate does not:

- modify official Pal assets;
- approve R108-A/B/C results before they exist;
- generate real manifests;
- edit central roster;
- create automation;
- run clean-copy checks by itself;
- push, tag, fetch, pull, or release.
