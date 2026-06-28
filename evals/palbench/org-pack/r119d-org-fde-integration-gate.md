# R119-D Org Pack / FDE Pack Integration Gate

Date: 2026-06-28

## Purpose

This PalBench gate defines the checks for the next R120 single-thread integration round after R119-A, R119-B, and R119-C complete their parallel work.

R119-D does not modify Org Pack, FDE Pack, or asset-boundary standards. It does not depend on final R119-A/B/C results and does not approve them by itself. It creates the gate, checklist, issue template, and R120 integration plan that the later integration owner must apply to the final combined worktree.

## Scope

Use this gate when integrating:

- R119-A Org Pack practical structure work;
- R119-B FDE Pack standard work;
- R119-C reusable/private asset-boundary work;
- R119-A/B/C validation records, integration notes, examples, templates, and internal reports.

The gate is documentation and evidence policy only. It is not a scanner, validator, installer, connector, marketplace program, runtime, database, or auto-execution tool.

## Baseline References

Read before running this gate:

- `private completion report outside the public repository`
- `release/integration-notes/r118-pal-metadata-pause-and-org-pack-return-decision.md`
- `release/integration-notes/r118-r119-readiness-decision.md`
- `docs/09-roadmap/v0.5-local-development-scope.md`
- `standards/org-pack/org-pack-standard.md`
- `standards/pal-asset/pal-asset-standard.md`

If a reference is missing in R120, record it as `missing`; do not substitute unrelated evidence.

## Gate 1: R119-A Org Pack Practical Structure Exists

R120 must verify the R119-A final paths from the current worktree, not from expectation alone.

| Check | Required Result |
| --- | --- |
| R119-A public files exist | pass or documented issue |
| Org Pack practical structure exists | pass |
| Org Pack templates, if added, are public-safe | pass |
| Org Pack examples, if added, are public-safe | pass |
| R119-A validation exists | pass or documented issue |
| R119-A internal report exists under `private completion report outside the public repository` | pass or documented issue |

Org Pack files must remain no-code organization assets. They must not become a project installer, external project template, connector, marketplace package, scanner, validator, runtime, or keyword router.

## Gate 2: R119-B FDE Pack Standard Exists

| Check | Required Result |
| --- | --- |
| R119-B public files exist | pass or documented issue |
| FDE Pack standard exists | pass |
| FDE Pack templates, if added, are public-safe | pass |
| FDE Pack examples, if added, are public-safe | pass |
| R119-B validation exists | pass or documented issue |
| R119-B internal report exists under `private completion report outside the public repository` | pass or documented issue |

FDE Pack files must describe no-code delivery assets and governance. They must not become a delivery daemon, business-system connector, API client, customer-data store, marketplace program, or execution engine.

## Gate 3: R119-C Reusable / Private Boundary Exists

| Check | Required Result |
| --- | --- |
| R119-C public files exist | pass or documented issue |
| reusable vs customer-private boundary exists | pass |
| private asset handling is explicit | pass |
| public reusable asset safety is explicit | pass |
| R119-C validation exists | pass or documented issue |
| R119-C internal report exists under `private completion report outside the public repository` | pass or documented issue |

R119-C must not place customer private data, real project facts, private project memory, credentials, system identifiers, private reports, or business secrets into reusable public packs.

## Gate 4: Templates JSON Parse

R120 must parse every JSON template added or modified by R119-A/B/C.

| Check | Required Result |
| --- | --- |
| R119 template JSON parse failures | 0 |
| placeholder fields are public-safe | pass |
| no real credentials / customer identifiers | pass |
| no deterministic route maps | pass |

If a JSON template is intentionally partial, it must still be syntactically valid JSON or explicitly be a `.md` / text example rather than `.json`.

## Gate 5: Examples JSON Parse

R120 must parse every JSON example added or modified by R119-A/B/C.

| Check | Required Result |
| --- | --- |
| R119 example JSON parse failures | 0 |
| examples are public-safe | pass |
| examples are de-identified | pass |
| no real credentials / tokens / secrets | pass |
| no real customer-private facts | pass |

Examples may use obvious placeholders. They must not use live-looking credentials, private customer names, real project memory, or private system identifiers.

## Gate 6: No Credentials Or Customer-Private Leak

Fail if R119 changed files contain:

- credentials;
- tokens;
- secrets;
- cookies;
- API keys;
- passwords;
- customer-private data;
- real project private evidence;
- customer system identifiers;
- private memory;
- private reports;
- business secrets.

Safety language such as "do not store credentials" is not a credential finding.

## Gate 7: No Connector / Marketplace / Scanner

Fail if R119 changed files introduce:

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

Org Pack / FDE Pack materials may describe governance for external systems, but they must not implement or require an integration client.

## Gate 8: No Keyword Routing

Fail if R119 changed files add active:

- `keyword_map`;
- `domain_map`;
- `role_map`;
- deterministic task-domain-to-Pal routing;
- fixed language such as `sales -> PalName` as execution routing;
- any claim that Core routes semantically by keywords.

Org Pack recommendations, Pal candidates, Capability Inventory references, workflows, and runbooks are AI judgement inputs only.

## Gate 9: Central Roster Unchanged

| Check | Required Result |
| --- | --- |
| `workspace/organization/contacts/pals.json` parses | pass |
| registered Pal count | 9 |
| active Pal count | 9 |
| `routing_policy` | `ai_judgement_only` |
| `keyword_routing_allowed` | `false` |
| central contacts diff | empty |

Org Packs may recommend Pals, but they must not copy, replace, or modify the central roster.

## Gate 10: Official Pal Unchanged

| Check | Required Result |
| --- | --- |
| official Pal directory count | 9 |
| all official Pal `pal.json` parse | pass |
| official Pal `pal.json` diff | empty |
| official Pal asset diff from R119-D | empty |
| new official Pal `asset-manifest.json` count beyond existing pilot state | 0 |

R119-D must not modify official Pals. R120 must verify that R119-A/B/C did not make unauthorized official Pal edits.

## Gate 11: External Project Thin Binding Preserved

Fail if R119 changed files require or create external project directories such as:

- `.agentpal/org-pack/`
- `.agentpal/pals/`
- `.agentpal/memory/`
- `.agentpal/reports/`
- `.agentpal/workflows/`
- `.agentpal/evals/`
- `.agentpal/capability-inventory/`
- `.agentpal/business-systems/`

External projects remain thin-bound. Org Pack / FDE Pack assets stay in AgentPal central workspace, reusable templates/examples, or approved private records.

## Gate 12: Index Update Notes Exist

R120 must verify that R119 integration notes or index update notes exist for each thread:

| Thread | Required Result |
| --- | --- |
| R119-A notes | present or issue |
| R119-B notes | present or issue |
| R119-C notes | present or issue |
| R119-D notes / plan | present |
| R120 integration summary | create during R120 |

If R120 updates `README.md`, `README.zh-CN`, `RESOURCE_INDEX.md`, or `agentpal.json`, the summary must state exact changed entries and why they are navigation-only.

## Gate 13: No Untracked R119 Files Left

Before R120 integration commit, run `git status --short` and classify all R119-looking files.

| Status | Required Action |
| --- | --- |
| expected and in scope | stage in the integration commit |
| expected but missing | create issue from the R119-D issue template |
| other-thread file present | do not stage until owner and scope are confirmed |
| out-of-scope untracked file | leave untracked and record as issue |
| generated or unsafe file | remove only with explicit approval; otherwise block |

No untracked R119 file may be silently ignored in the final integration report.

## Decision Rules

| Evidence | Decision |
| --- | --- |
| all gates pass | `pass` |
| A/B/C output missing but documented as no-write decision | `pass-with-notes` only if accepted by integration owner |
| template or example JSON fails parse | `fail` |
| customer-private leak appears | `fail` |
| connector, marketplace, scanner, validator, installer, daemon, or auto-execution appears | `fail` |
| keyword routing appears | `fail` |
| central roster changes | `fail` |
| official Pal changes unexpectedly | `fail` |
| external project thick binding appears | `fail` |
| evidence cannot be collected | `blocked` or `needs-more-evidence` |

## Issue Handling

Use `release/integration-notes/r119d-org-fde-integration-issue-template.md` for every missing, unsafe, ambiguous, stale, or out-of-scope finding.

R119-D does not fix R119-A/B/C files. Future R120 fixes must respect the integration round's allowed paths.

## Non-Goals

This gate does not:

- modify Org Pack / FDE Pack / asset-boundary standards;
- approve R119-A/B/C before they exist;
- update shared entry files;
- modify official Pals;
- modify central contacts;
- create automation;
- push, tag, fetch, pull, or release.
