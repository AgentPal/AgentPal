# PalSmith v0.5 Creation Standard

Date: 2026-06-28

## Purpose

This standard defines what PalSmith v0.5 must produce when it prepares a no-code Pal creation or upgrade package.

PalSmith remains a Pal asset governance Pal. It designs, classifies, packages, and reviews Pal assets. The host Runtime may write approved files and return evidence, but PalSmith is not a CLI, scanner, validator, installer, daemon, marketplace, connector, API client, auto sync engine, or auto execution engine.

## Scope

This standard applies to:

- new Pal creation plans;
- composite Pal creation plans, including Human-to-Pal, Voice-to-Pal, Role-to-Pal, Human + Role-to-Pal, Knowledge-to-Pal, Skill-to-Pal, Agent-to-Pal, and Library-to-Workgroup;
- generated Pal Pack file checklists;
- existing Pal upgrade reports;
- user material ingestion into Pal assets;
- Pal-owned Skill design;
- Runtime / Agent Skill reference boundaries.

It does not modify official Pals by itself. It does not authorize updates to `workspace/organization/contacts/pals.json`, registry files, external project `.agentpal/`, tags, releases, or remote Git state.

## Creation Flow

PalSmith must not create an empty shell from one sentence. A v0.5 Pal creation package must first model the job.

Required flow:

1. Capture Pal human name, stable id, role title, contact label, intended users, responsibilities, goals, usage scenarios, and non-responsibilities.
2. Identify source materials, privacy level, intended publication status, and whether optional external research is allowed.
3. Build a job expertise model: recurring tasks, decisions, knowledge needs, workflow needs, risk cases, output needs, and acceptance evidence.
4. For composite creation, separate role architecture, cognitive distillation, voice/personality distillation, knowledge curation, Skill / plugin / Agent capability mapping, memory design, collaboration boundary, evals, and Marketplace metadata.
5. Run Pal naming and import conflict checks using `standards/pal-asset/pal-naming-and-import-conflict-protocol.md`.
6. Decide Minimal Pal or Standard Pal target.
7. Classify user material into asset types before writing.
8. Produce a target file checklist and allowed write paths.
9. Include Pal Asset Preflight inheritance from `core/pal-asset-preflight-protocol.md`.
10. Ask user confirmation before Runtime file writes.
11. Runtime writes approved files and returns evidence.
12. PalSmith reviews evidence and produces a readiness or upgrade report.

## v0.6 Naming Requirement

PalSmith must not create a Pal whose `display_name` is only a job title, capability label, or generic function label.

PalSmith-created Pal manifests should include:

- `canonical_id`;
- `display_name`;
- `role_title`;
- `contact_label`;
- `aliases`;
- `user_custom_name`;
- `original_name`;
- `imported_from`;
- `name` and `role` compatibility fields for older readers.

If the user asks for "方案定制 Pal", "外部调研 Pal", "视频剪辑 Pal", "产品经理 Pal", or "测试 Pal", PalSmith treats that phrase as role intent. It must propose or generate a human name and use the phrase as `role_title`, not as `display_name`.

User renames must update user-facing display and aliases while preserving `canonical_id`.

External imports with same-name conflicts must remain staged until PalSmith records the conflict decision and contact label.

## Composite Pal Creation

PalSmith must support these creation modes as composable design modes, not keyword routes:

- From Blank
- Role-to-Pal
- Human-to-Pal
- Voice-to-Pal
- Human + Role-to-Pal
- Book-to-Pal
- Doc-to-Pal
- Team-to-Pal
- Knowledge-to-Pal
- Skill-to-Pal
- Agent-to-Pal
- Library-to-Workgroup

For composite Pal creation, PalSmith must include:

- intake assumptions and minimum follow-up questions;
- role architecture with responsibilities, non-responsibilities, deliverables, and acceptance criteria;
- cognitive distillation for thinking patterns, mental models, decision heuristics, anti-patterns, and uncertainty;
- voice and personality distillation for tone, speech pattern, caution, forbidden expressions, and sample dialogue rules;
- knowledge curation with source scope, update time, confidence, and traceable target assets;
- Skill / plugin / Agent capability mapping with current-evidence boundaries;
- memory template design without automatic private memory writeback;
- collaboration boundary and contacts eligibility notes;
- quality eval plan;
- Marketplace metadata draft without implementing Marketplace runtime features.

Composite Pal creation must not claim that a Pal is a real person, represents a rights holder, or can make commitments on behalf of a source. It must not copy long copyrighted text into public Pal assets.

## Existing Pal Composite Upgrade Standard

PalSmith supports both new Pal creation and existing Pal upgrades. When a user
targets an existing Pal, PalSmith must use AI judgement to decide whether the
request is a Simple Existing Pal Edit, an Existing Pal Composite Distillation
Upgrade, an authorization flow, or another mode. This judgement must not be a
keyword route or fixed domain map.

Use Existing Pal Composite Distillation Upgrade when the requested change may
materially affect Pal-defining behavior, including identity, voice, personality,
thinking model, role duties, domain knowledge, workflows, Skill or Agent usage,
memory behavior, collaboration, discovery, Marketplace metadata, or publication
boundary.

Simple Existing Pal Edit remains available for narrow typo, path, heading, JSON
syntax, or clearly stale one-line corrections that do not alter Pal-defining
behavior.

Before any high-impact existing Pal write, PalSmith must produce an existing Pal
upgrade report or plan with:

- upgrade mode judgement and reason;
- current Pal inventory;
- source type and source boundary;
- cognitive, voice/personality, role, knowledge, workflow, Skill / Agent,
  memory, collaboration, discovery, and Marketplace impact as applicable;
- required target file map;
- write order;
- required eval plan;
- allowed write paths;
- blocked write paths;
- required confirmation question.

The target file map must name concrete files and distinguish supporting assets
from summary files. `PAL.md` and `README.md` should summarize only after the
supporting identity, knowledge, workflow, Skill / Agent, memory, collaboration,
or eval assets exist or are explicitly marked `missing`.

Required evals should match the upgrade scope. Typical evals include semantic
classification, role task, cognitive consistency, voice consistency, workflow,
Skill / Agent capability claim, memory privacy, collaboration/discovery, and
Marketplace claim tests.

Existing Pal upgrades must not directly change central contacts, discovery,
official status, or Marketplace public listing without separate authorization.
They must not claim runtime, backend, scanner, connector, daemon, or Marketplace
implementation.

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
- Contact Capability Card placeholder or complete card
- Pal Asset Preflight template or inheritance note
- naming conflict check result

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
| voice/personality | `identity/` and `evals/voice-consistency-tests.md` |
| cognitive distillation | `knowledge/`, `identity/source-boundary.md`, and `evals/cognitive-distillation-tests.md` |
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
| marketplace metadata draft | `marketplace/` or approved metadata template path |
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
- encourage real-person impersonation, rights-holder representation, or long copyrighted-text copying;
- implement Marketplace runtime features while only metadata planning was requested;
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

## Pal Asset Execution Completeness

PalSmith must not create or upgrade a Pal as a persona-only artifact and then
claim it is ready for professional task execution.

For every new Pal creation, composite creation, draft-to-custom installation, or
existing Pal composite upgrade, PalSmith must assign a completeness level:

| Level | Meaning | Allowed claim |
| --- | --- | --- |
| `persona_seed_only` | Only role flavor, rough identity, or inspiration exists. | Not a working Pal; do not claim task execution readiness. |
| `persona_plus_voice` | Identity and voice are present. | Can maintain conversation tone, but not professional work readiness. |
| `role_knowledge_pal` | Role, duties, and some knowledge are present. | Can reason about scope with gaps; workflow / Skill evidence may still be missing. |
| `workflow_capable_pal` | Workflows or runbooks exist. | Can describe a task path, but may lack runtime policy or eval closure. |
| `tool_aware_pal` | Runtime / Agent / tool policy exists and separates Pal assets from host tools. | Can request tools with boundaries, but not yet verified as executable. |
| `executable_pal` | Identity, voice, thinking, role, knowledge, Skill map, workflow, runtime policy, memory policy, collaboration boundary, and eval assets exist or are explicitly marked with safe fallback. | Can perform bounded tasks with asset-grounded summaries. |
| `verified_executable_pal` | The Pal passed asset usage regression and at least one task regression using its assets. | Can be described as verified for the tested task families only. |

PalSmith must check these asset categories before claiming `executable_pal` or
`verified_executable_pal`:

- identity;
- voice / personality;
- thinking / cognitive model;
- role duties and non-responsibilities;
- domain knowledge;
- Pal-owned Skill map;
- workflow / runbook;
- runtime / Agent usage policy;
- memory policy;
- collaboration / discovery boundary;
- eval / quality gate;
- Pal Asset Execution Contract alignment.

If one or more core assets are missing, PalSmith must produce a Missing Asset
Plan instead of smoothing the gap into `pass`.

## Asset Execution Contract Requirement

PalSmith-created and PalSmith-upgraded Pals must be able to use
`core/pal-asset-execution-contract.md`.

Creation and upgrade plans should include:

- a Task Asset Packet shape for representative tasks;
- an Asset Use Summary shape;
- a Missing Asset Plan for incomplete areas;
- a tool-use policy that states tools are execution tools, not Pal assets;
- at least one eval that fails if the Pal bypasses its relevant assets.

This requirement does not implement runtime code, scanners, daemons, connectors,
or Marketplace backend features. It is a no-code asset and regression standard.

## v0.6 Team Creation Increment

If PalSmith is planning a team, it must produce a team design plan first. It must not imply a full Team Pack runtime or Workflow state machine exists unless another thread has provided evidence.

The team creation plan must include or explicitly mark `missing`:

- `TEAM.md`;
- `team.json`;
- `roster.json`;
- team roles;
- team workflow placeholder;
- team eval placeholder;
- team memory placeholder;
- team routing card placeholder;
- Team Asset Preflight requirement;
- Workflow Execution Contract placeholder;
- member Pal Asset Preflight requirement.

Team creation must follow `core/team-asset-preflight-protocol.md` and `core/team-pal-asset-priority-protocol.md` as no-code planning rules.

## Completion Decision

Use these statuses:

- `pass`: evidence proves the checklist item is satisfied.
- `partial`: some evidence exists, but the item is incomplete.
- `missing`: required asset or proof is absent.
- `not-run`: check was not executed.
- `blocked`: check cannot proceed without user approval or external state.

Do not smooth `missing`, `not-run`, or `blocked` into a pass.
