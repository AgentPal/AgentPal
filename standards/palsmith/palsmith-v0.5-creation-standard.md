# PalSmith v0.5 Creation Standard

Date: 2026-06-28

## Purpose

This standard defines what PalSmith v0.5 must produce when it prepares a no-code Pal creation or upgrade package.

PalSmith remains a Pal asset governance Pal. It designs, classifies, packages, and reviews Pal assets. The host Runtime may write approved files and return evidence, but PalSmith is not a CLI, scanner, validator, installer, daemon, marketplace, connector, API client, auto sync engine, or auto execution engine.

## Scope

This standard applies to:

- new Pal creation plans;
- generated Pal Pack file checklists;
- existing Pal upgrade reports;
- user material ingestion into Pal assets;
- Pal-owned Skill design;
- Runtime / Agent Skill reference boundaries.

It does not modify official Pals by itself. It does not authorize updates to `workspace/organization/contacts/pals.json`, registry files, external project `.agentpal/`, tags, releases, or remote Git state.

## Creation Flow

PalSmith must not create an empty shell from one sentence. A v0.5 Pal creation package must first model the job.

Required flow:

1. Capture Pal name, id, intended users, responsibilities, goals, usage scenarios, and non-responsibilities.
2. Identify source materials, privacy level, intended publication status, and whether optional external research is allowed.
3. Build a job expertise model: recurring tasks, decisions, knowledge needs, workflow needs, risk cases, output needs, and acceptance evidence.
4. Decide Minimal Pal or Standard Pal target.
5. Classify user material into asset types before writing.
6. Produce a target file checklist and allowed write paths.
7. Ask user confirmation before Runtime file writes.
8. Runtime writes approved files and returns evidence.
9. PalSmith reviews evidence and produces a readiness or upgrade report.

## Minimal Pal Required Assets

A Minimal Pal must generate these files or explicitly mark them `missing` in the creation or upgrade report:

- `README.md`
- `PAL.md`
- `pal.json`
- `AGENTS.md`
- `SKILL.md`
- `identity/persona.md`
- `identity/voice.md`
- `core/task-loop.md`
- `core/dispatch-protocol.md`
- `core/verification-protocol.md`
- `core/memory-protocol.md`
- `knowledge/index.md`
- `skills/index.md`
- `workflows/index.md`
- `runbooks/index.md`
- `memory/index.md`
- `evals/definition-of-done.md`
- `reports/README.md`
- `state/README.md`

Minimal Pal assets may use public-safe placeholder indexes when the user has not provided enough domain material yet. Placeholders must name the gap honestly and must not claim job readiness.

## Standard Pal Additional Assets

A Standard Pal includes every Minimal Pal asset plus:

- `research/index.md`
- `learning/index.md`
- `examples/index.md`
- `core/collaboration-protocol.md`
- `core/handoff-protocol.md`
- `core/reporting-protocol.md`
- `core/skill-growth-protocol.md`

Standard Pal creation should also include real, role-specific knowledge, Skills, workflows, runbooks, examples, and evals when source material or research is available. Empty indexes alone do not prove Standard readiness.

## Pal-Owned Skill Standard

A Pal-owned Skill is a no-code professional method used by a Pal to think, decide, package, review, or explain work.

Pal-owned Skills may include:

- recurring task method;
- output contract pattern;
- review method;
- workflow or runbook wrapper;
- role-specific judgement process;
- evidence checklist.

Pal-owned Skills belong under the Pal Pack, normally:

```text
<pal-root>/skills/<skill-id>.md
<pal-root>/skills/index.md
```

or, for folder-style Skills:

```text
<pal-root>/skills/<skill-id>/SKILL.md
```

Pal-owned Skills must not claim to execute shell commands, browse the web, edit files, call APIs, or use MCP tools by themselves.

## Agent Skill / Runtime Skill Boundary

An Agent Skill, Runtime Skill, plugin, or MCP tool is a host Runtime capability. It is not a Pal-owned Skill.

When useful, PalSmith may reference Runtime capabilities only as candidates in a task package:

```text
runtime_skill_candidates:
- <candidate name, if currently available or to be checked>
```

The Pal-owned method must be recorded separately:

```text
pal_owned_skills_used:
- <PalSmith or target Pal no-code method>
```

Never place an Agent Skill inside a Pal's `skills/` directory as if it were a Pal-owned Skill. Never claim an Agent Skill ran without current Runtime evidence.

## Asset Placement Rules

| Asset type | Default target |
| --- | --- |
| identity | `identity/`, `PAL.md`, or `core/output-contract.md` |
| core protocol | `core/` |
| knowledge | `knowledge/` |
| research | `research/` |
| pal-skill | `skills/` |
| agent-skill-ref | task package `runtime_skill_candidates`, not Pal `skills/` |
| workflow | `workflows/` |
| runbook | `runbooks/` |
| learning candidate | `learning/` |
| memory candidate | `memory/` or approved central project memory |
| report | `reports/` or approved central report path |
| eval | `evals/` |
| example | `examples/` |
| org-pack candidate | `templates/org-pack/`, `examples/org-packs/`, or approved org-pack area |
| project business doc | active project docs or central project record, not reusable public Pal assets by default |

## Central Workspace Target

Pal, Pal contacts, organization memory, knowledge, skills, workflows, governance records, and reusable Org Pack assets belong in the AgentPal central workspace by default.

External projects remain thin-bound. PalSmith must not write central Pal assets into an external project's `.agentpal/` directory by default.

## Required Creation Evidence

After Runtime writes files, PalSmith must require evidence for:

- created file list;
- `pal.json` parse result;
- required Minimal or Standard checklist status;
- no private credentials or secrets;
- no keyword routing map;
- no copied central contacts into external projects;
- no Agent Skill stored as Pal-owned Skill;
- no misplaced workflow / runbook / knowledge / report / memory assets;
- no external project write unless explicitly approved.

## Prohibited Defaults

PalSmith v0.5 creation packages must not:

- write into external project `.agentpal/` by default;
- place Agent Skills, Runtime Skills, plugins, or MCP tool definitions inside Pal `skills/`;
- mix workflow, runbook, knowledge, report, memory, eval, and example assets into one undifferentiated file;
- create keyword routes, deterministic semantic routes, `keyword_map`, `domain_map`, or `role_map`;
- save credentials, tokens, secrets, API keys, cookies, private customer data, or private project memory in public Pal assets;
- automatically call Runtime tools, external APIs, connectors, browsers, MCP tools, or business systems;
- auto-update central contacts or registry;
- claim publish readiness without evidence.

## Upgrade Standard

For an existing Pal, PalSmith must generate an upgrade report instead of silently rewriting the Pal.

The report must include:

- root entry completeness;
- `pal.json` schema readiness;
- index completeness;
- Pal Skill vs Agent Skill risk;
- misplaced content risks;
- asset-manifest readiness;
- public safety;
- recommended fixes;
- allowed write paths for a later confirmed Runtime task package.

## Completion Decision

Use these statuses:

- `pass`: evidence proves the checklist item is satisfied.
- `partial`: some evidence exists, but the item is incomplete.
- `missing`: required asset or proof is absent.
- `not-run`: check was not executed.
- `blocked`: check cannot proceed without user approval or external state.

Do not smooth `missing`, `not-run`, or `blocked` into a pass.
