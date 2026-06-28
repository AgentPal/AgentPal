# R106-D Official Pal Skills Index Integration Gate

Date: 2026-06-28

## Purpose

This PalBench gate defines the integration checks for the next R107 integration round after R106-A, R106-B, and R106-C complete their parallel work.

R106-D does not modify `official/pals/**`, does not depend on the final R106-A/B/C results, and does not approve any PalSmith memory / research or official Pal `skills/` index backfill by itself. It creates the gate, checklist, and issue template that the later R107 integration owner must use against the final combined worktree.

## Scope

Use this gate when integrating:

- PalSmith `memory/README.md` and `research/README.md` work, if R106-A completes it;
- Atlas, Quinn, and Morgan `skills/index.md` or approved skills README work, if R106-B completes it;
- Nova, Vega, Harper, and Rhea `skills/index.md` or approved skills README work, if R106-C completes it;
- R106-A/B/C validation records, summaries, and internal reports.

This gate is documentation and evidence policy only. It is not a scanner, validator, installer, connector, runtime, marketplace program, or auto-execution tool.

## Baseline References

Read before running this gate:

- `private completion report outside the public repository`
- `private completion report outside the public repository`
- `evals/palbench/pal-asset/r100d-pal-metadata-upgrade-compatibility-gate.md`
- `templates/pal-asset/safe-index-backfill-guide.md`
- `templates/pal-asset/index-templates/skills-index-template.md`
- `workspace/organization/contacts/pals.json`

If any reference is missing in the future R107 workspace, record it as `missing`; do not substitute unrelated evidence.

## Gate 1: R106-A / R106-B / R106-C Outputs Exist

The R107 integration round must verify the real output files from the parallel threads.

| Check | Required Result |
| --- | --- |
| R106-A public files exist | pass or documented issue |
| R106-B public files exist | pass or documented issue |
| R106-C public files exist | pass or documented issue |
| R106-A validation exists | pass or documented issue |
| R106-B validation exists | pass or documented issue |
| R106-C validation exists | pass or documented issue |
| R106-A/B/C integration notes exist | pass or documented issue |
| R106-A/B/C internal reports exist under `private completion report outside the public repository` | pass or documented issue |

Do not infer completion from branch position, commit message, or directory presence alone.

## Gate 2: PalSmith Memory / Research README Exists

If R106-A owns the PalSmith memory / research backfill, verify:

| Expected File | Required Result |
| --- | --- |
| `official/pals/PalSmith-pal-governor/memory/README.md` | present, or R106-A documents a deliberate no-write policy decision |
| `official/pals/PalSmith-pal-governor/research/README.md` | present, or R106-A documents a deliberate no-write policy decision |
| R106-A validation | records exact changed paths and not-run items |
| R106-A internal report | exists outside the public repo |

These README files must be navigation and boundary notes only. They must not write private memory, full reports, raw research dumps, credentials, or promoted knowledge.

## Gate 3: Atlas / Quinn / Morgan Skills Index Exists

If R106-B owns the first skills-index batch, verify:

| Pal | Expected File | Required Result |
| --- | --- | --- |
| Atlas | `official/pals/Atlas-developer/skills/index.md` or approved skills README | present or documented issue |
| Quinn | `official/pals/Quinn-quality/skills/index.md` or approved skills README | present or documented issue |
| Morgan | `official/pals/Morgan-document/skills/index.md` or approved skills README | present or documented issue |

Every skills index must preserve the Pal Skill / Agent Skill boundary:

- Pal Skills are role-level work capabilities.
- Agent / Runtime Skills may be referenced as execution candidates only.
- Agent Skill files, plugin metadata, MCP tools, code, dependency manifests, and tool installation docs must not be copied into Pal `skills/`.

## Gate 4: Nova / Vega / Harper / Rhea Skills Index Exists

If R106-C owns the second skills-index batch, verify:

| Pal | Expected File | Required Result |
| --- | --- | --- |
| Nova | `official/pals/Nova-product/skills/index.md` or approved skills README | present or documented issue |
| Vega | `official/pals/Vega-research/skills/index.md` or approved skills README | present or documented issue |
| Harper | `official/pals/Harper-writing/skills/index.md` or approved skills README | present or documented issue |
| Rhea | `official/pals/Rhea-system/skills/index.md` or approved skills README | present or documented issue |

If any Pal has no suitable skills directory or already has an equivalent index, the thread must document the exact evidence and decision rather than silently skipping it.

## Gate 5: No `pal.json` Diff

R106 index work is documentation-only.

| Check | Required Result |
| --- | --- |
| `git diff -- official/pals/**/pal.json` | empty |
| staged diff for `official/pals/**/pal.json` | empty |
| integrated R106 commit range changes to `official/pals/**/pal.json` | none |

Any official Pal `pal.json` diff fails the integration gate unless a separate metadata task explicitly authorizes it. R106-D does not grant that authorization.

## Gate 6: No Official `asset-manifest.json` Generated

R106 must not generate real official Pal manifests.

| Check | Required Result |
| --- | --- |
| official `asset-manifest.json` additions | 0 |
| official `asset-manifest.json` diffs | 0 |
| manifest-like generated files claiming runtime authority | 0 |

If a manifest appears, fail against the R100-D compatibility boundary unless a separate manifest-generation thread approved it.

## Gate 7: Central Roster Unchanged

| Check | Required Result |
| --- | --- |
| `workspace/organization/contacts/pals.json` parses | pass |
| registered Pal count | 9 |
| active Pal count | 9 |
| every `pack_path` exists | pass |
| `routing_policy` | `ai_judgement_only` |
| `keyword_routing_allowed` | `false` |
| central contacts diff | empty |

Do not accept any R106 result that changes central contacts, contact cards, capability cards, default receiver, or roster source of truth.

## Gate 8: Official Pal Count And Loadability

| Check | Required Result |
| --- | --- |
| official Pal directory count | 9 |
| every official Pal `pal.json` parses | pass |
| every official Pal has `PAL.md` | pass |
| every official Pal has `AGENTS.md` | pass |
| every official Pal has `SKILL.md` | pass |
| selected Pal root files unchanged unless separately allowed | pass |

Missing optional asset directories are warnings. Missing root entries or broken `pal.json` files block the affected integration.

## Gate 9: No Keyword Routing

R106 files must not introduce deterministic semantic routing.

Fail if changed R106 files add active:

- keyword route map;
- domain route map;
- hard-coded role dispatch table;
- deterministic owner selection table;
- language claiming Core performs semantic dispatch.

Documentation may mention route-map concepts only as prohibited examples or checks.

## Gate 10: No Connector / Scanner / Marketplace Program

R106 files must remain Markdown / JSON governance artifacts.

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

## Gate 11: No Credentials Or Private Data

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

## Gate 12: No External Project `.agentpal`

R106 integration must preserve thin binding.

| Check | Required Result |
| --- | --- |
| external project `.agentpal/pals` additions | 0 |
| external project `.agentpal/skills` additions | 0 |
| Pal skills indexes copied into external projects | 0 |
| external project manifest copied from official Pal | 0 |

Central Pal assets stay in the AgentPal Workspace. External projects must not become the Pal asset source of truth.

## Gate 13: No Untracked R106 Files Left

Before integration commit, run `git status --short` and classify all R106-looking files.

| Status | Required Action |
| --- | --- |
| expected and in scope | stage in the integration commit |
| expected but missing | create issue from the R106-D issue template |
| other-thread file present | do not stage until owner and scope are confirmed |
| out-of-scope untracked file | leave untracked and record as issue |
| generated or unsafe file | remove only with explicit approval; otherwise block |

No untracked R106 file may be silently ignored in the final integration report.

## Gate 14: Clean-Copy Pass

The R107 integration owner must verify the combined committed state, not only a pre-commit working tree.

Clean-copy evidence may come from a fresh clone, clean local copy, or equivalent clean checkout. If no clean-copy check is run, record `not-run` with reason and do not claim clean-copy pass.

Required clean-copy checks:

- required R106-A/B/C files exist;
- R106-D gate/checklist/template/validation exist;
- PalSmith memory / research README outcome is verified;
- Atlas / Quinn / Morgan skills index outcome is verified;
- Nova / Vega / Harper / Rhea skills index outcome is verified;
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
| any expected R106-A/B/C file missing without a documented no-write decision | `fail` or `needs-repair` |
| Agent Skill content is copied into Pal `skills/` | `fail` |
| report body is copied into memory | `fail` |
| raw research is promoted directly to knowledge | `fail` |
| `pal.json` diff appears | `fail` |
| official manifest appears | `fail` |
| central roster changes | `fail` |
| keyword routing, connector, scanner, credential, or external project asset copy appears | `fail` |
| evidence cannot be collected | `blocked` or `needs-more-evidence` |

## Issue Handling

Use `release/integration-notes/r106d-official-pal-skills-index-issue-template.md` for every missing, unsafe, ambiguous, or out-of-scope finding.

Do not fix official Pal assets during R106-D. Future R107 fixes must respect the owner thread scope and the integration round's allowed paths.

## Non-Goals

This gate does not:

- modify official Pal assets;
- approve R106-A/B/C results before they exist;
- generate real manifests;
- edit central roster;
- create automation;
- run clean-copy checks by itself;
- push, tag, fetch, pull, or release.
