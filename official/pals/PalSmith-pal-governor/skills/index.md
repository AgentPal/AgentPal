# Skills Index

Pal: PalSmith

## Purpose

This directory lists PalSmith-owned Pal Skills for no-code Pal asset governance.

PalSmith Skills help PalSmith organize recurring Pal creation, Pal team creation, asset classification, user material ingestion, web research-to-knowledge planning, existing Pal upgrade inspection, Pal Skill / Agent Skill boundary review, readiness review, import/export review, version governance, and safe asset backfill recommendations.

This index is navigation and boundary documentation only. It does not change PalSmith identity, direct calls, routing, output contracts, runtime behavior, `pal.json`, central contacts, or official asset manifests.

## PalSmith Pal Skill definition

A PalSmith Pal Skill is a Pal-owned role-level governance method. It helps PalSmith think, classify, plan, package, review, and report on Pal assets.

PalSmith Pal Skills may produce no-code governance outputs such as:

- Pal creation plans;
- Pal team plans;
- asset classification results;
- existing Pal upgrade reports;
- Pal health inspection task packages;
- Pal quality inspection reports;
- Pal Skill / Agent Skill boundary judgements;
- import/export staging plans;
- publish-readiness reviews;
- version governance notes;
- safe index backfill recommendations;
- Runtime Task Packages for approved execution layers.

These outputs are governance artifacts. They do not execute commands, modify files, call APIs, install tools, update contacts, generate releases, or write into external projects by themselves.

## Agent Skill boundary

This directory stores Pal Skills, not Runtime Agent Skills.

Runtime Agent Skills are host-runtime execution capabilities such as file writing, repository operations, browser control, OCR, archive extraction, document processing, shell commands, plugin use, MCP tools, or external API helpers. Agent Skills belong in the host runtime's skill registry, plugin system, MCP layer, tool documentation, or explicit runtime capability reference.

PalSmith may reference Agent Skills only as runtime candidates inside a Task Package. Agent Skills should be referenced, not copied into PalSmith `skills/`.

Do not store raw CLI command docs, API docs, connector docs, scanner docs, validator logic, installer steps, or plugin usage as PalSmith Pal Skills unless they are rewritten as Pal-owned governance methods with context, approval, runtime boundary, verification, and memory writeback rules.

## What belongs here

- PalSmith-owned methods for Pal creation, Pal team creation, Pal asset classification, existing Pal upgrade review, Pal quality inspection, Pal capability mapping, conflict detection, import/export review, version governance, publish readiness, user material ingestion, and web research-to-knowledge planning.
- No-code skill cards that define purpose, activation conditions, required context, output expectations, approval boundaries, verification, and writeback rules.
- References to related PalSmith standards, checklists, templates, workflows, runbooks, evals, reports, and Runtime Task Package templates.
- Agent Skill references only when they are clearly runtime evidence candidates and not copied as Pal-owned Skills.

## What does not belong here

- Runtime Agent Skills, plugins, MCP tools, tool installers, scanner configs, validator logic, API clients, connectors, daemons, databases, auto sync engines, auto execution engines, marketplace/hub programs, or executable runtime code.
- Keyword route maps, `keyword_map`, `domain_map`, `role_map`, deterministic dispatch tables, or semantic routing shortcuts.
- Raw command manuals, copied runtime skill files, credentials, tokens, secrets, cookies, API keys, private project data, private user memory, full reports, raw research dumps, or runtime state.
- Central roster edits, `pal.json` metadata upgrades, `asset-manifest.json` generation, or external project `.agentpal/` writes.
- New concrete PalSmith Skill content that has not been reviewed as a PalSmith role-level governance method.

## Current assets

### Flat Skill Cards

All current PalSmith Skills are flat Markdown skill cards and are mapped in `skill-asset-map.md`.

| Skill card | Purpose | Status |
| --- | --- | --- |
| `pal-creation-skill.md` | Prepare no-code Pal creation packages and creation evidence expectations. | present |
| `pal-team-creation-skill.md` | Prepare no-code Pal team creation packages and team-structure evidence expectations. | present |
| `pal-quality-inspection-skill.md` | Inspect Pal job fitness, asset completeness, depth, evidence, and safety. | present |
| `pal-conflict-detection-skill.md` | Detect responsibility overlap, collaboration risk, and Pal boundary conflicts. | present |
| `pal-capability-map-skill.md` | Map Pal capabilities without turning them into keyword routes. | present |
| `pal-knowledge-ingestion-skill.md` | Plan source-preserving knowledge ingestion into Pal assets. | present |
| `pal-skill-design-skill.md` | Design Pal-owned Skills and keep Agent Skill references separate. | present |
| `pal-workflow-design-skill.md` | Design Pal workflows with stages, outputs, approvals, and verification. | present |
| `pal-eval-design-skill.md` | Design Pal evals, boundary checks, and acceptance cases. | present |
| `pal-import-review-skill.md` | Review Pal import candidates and staging boundaries. | present |
| `pal-export-review-skill.md` | Review clean export and with-memory export boundaries. | present |
| `pal-version-governance-skill.md` | Plan version governance, snapshots, rollback notes, and release readiness boundaries. | present |
| `pal-publish-readiness-skill.md` | Review publish readiness without claiming publication. | present |
| `user-material-ingestion-skill.md` | Preserve and classify user materials before turning them into Pal assets. | present |
| `web-research-to-knowledge-skill.md` | Plan source-backed research-to-knowledge conversion with uncertainty preserved. | present |

### Supporting files

| Asset | Purpose | Status |
| --- | --- | --- |
| `README.md` | Human-readable skill directory note from earlier PalSmith work. | present |
| `skill-asset-map.md` | Maps every `pal.json` formal skill to its actual no-code skill asset. | present |

Formal skill count recorded in `pal.json`: 15.

## Candidate skills / needs review

| Candidate | Reason | Review status |
| --- | --- | --- |
| none added in R108-B | This batch is index-only and must not create new PalSmith skill content. | not-run |

Future PalSmith skill candidates should first be recorded as learning candidates, reviewed against PalSmith v0.5 standards, and promoted only through a separate allowed task.

## Asset classification relationship

PalSmith classification work uses `standards/palsmith/palsmith-asset-classification-standard.md` and `templates/palsmith/pal-asset-classification-result-template.json`.

Classification results are no-code governance outputs. They recommend asset types and target paths, preserve source anchors, mark sensitivity, and keep `external_project_write_allowed` false by default.

Classification must not:

- classify Runtime Agent Skills as Pal-owned Skills;
- copy central Pal assets into external project `.agentpal/`;
- store credentials or private memory in public assets;
- auto-call Runtime, Skill, plugin, MCP, connector, or business-system capabilities.

## Existing Pal upgrade relationship

PalSmith upgrade work uses PalSmith v0.5 creation and upgrade standards plus checklist templates.

Existing Pal upgrade reports may identify missing indexes, misplaced content risks, Pal Skill vs Agent Skill risks, public-safety gaps, and readiness gaps. They are reports and task-package inputs, not automatic edits.

PalSmith must not directly modify official Pals, central contacts, `pal.json`, or asset manifests unless the user explicitly requests that exact work and the current task passes the corresponding gate.

## Agent Skill references

PalSmith Pal Skills may reference host-runtime capabilities such as filesystem writes, archive handling, OCR, browser control, document processing, Git commands, JSON parsing, or repository inspection only as runtime evidence candidates.

References do not install, enable, probe, or execute Agent Skills. Runtime execution requires current-runtime evidence and the allowed read/write/command boundary named by the active task.

## Verification boundary

PalSmith can prepare verification criteria and review runtime evidence, but completion claims require current evidence from the execution layer.

Use `pass`, `partial`, `missing`, `not-run`, or `blocked` when reviewing PalSmith outputs. Do not treat plans, owner claims, directory presence, or skill names as proof that runtime actions occurred.

## Memory writeback boundary

Reports are not memory until stable lessons are extracted. Do not write full reports into memory.

Research is not knowledge until reviewed, source-grounded, and summarized. Do not promote raw research into knowledge by copying it wholesale.

If repeated PalSmith work creates a durable method improvement, record it as a candidate first and promote it only through an approved PalSmith skill, workflow, runbook, learning, or memory update.

## External project boundary

Do not copy PalSmith Pal Skills or central Pal assets into an external project `.agentpal/` directory by default.

External projects remain thin-bound. Pal assets, central contacts, organization memory, knowledge, skills, workflows, runbooks, reports, governance records, and reusable templates stay in the AgentPal central workspace or approved central records unless the user explicitly approves a separate project-local write.

## No keyword routing boundary

PalSmith is selected by AI owner judgement from the current request, central roster, expected deliverable, risk, evidence needs, and available assets. PalSmith is not selected by fixed keywords.

Do not create keyword route maps, `keyword_map`, `domain_map`, `role_map`, deterministic task-to-Pal tables, or semantic routing shortcuts in this directory.
