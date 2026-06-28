# Runbooks

## Purpose

Runbooks are concrete operating manuals and exception-handling guides.

In PalSmith, runbooks help describe stable checks, stop conditions, escalation rules, and verification steps for Pal creation, upgrade, classification, health review, and AI team maintenance situations.

Runbooks are no-code guidance. They do not execute actions.

## What belongs here

- concrete failure-handling steps
- operational checklists
- escalation rules
- stop conditions
- verification steps
- examples of safe handling
- blocked-state guidance
- human review triggers

## What does not belong here

- general knowledge
- Pal Skill definitions
- workflow strategy
- long task reports
- user private memory
- credentials
- raw external API instructions without approval and safety boundary
- keyword route maps
- connector settings
- automation scripts
- runtime Agent Skill files

## Current assets

| Asset | Purpose | Status |
| --- | --- | --- |
| `ai-team-health-check.md` | Runbook for checking an AI team package for capability, collaboration, and readiness gaps. | present |
| `classify-user-materials.md` | Runbook for classifying user-provided materials into Pal asset candidates with privacy boundaries. | present |
| `pal-health-check.md` | Runbook for checking a Pal Pack for structure, job fitness, public safety, and repair needs. | present |

## Candidate assets

| Candidate | Reason | Review status |
| --- | --- | --- |
| PalSmith import staging exception runbook | Could clarify when an imported Pal package is blocked before install. | needs-review |
| PalSmith publish-readiness blocked-state runbook | Could clarify when missing evidence blocks stable or publish-ready status. | needs-review |

## Runbook vs workflow

A runbook is not a workflow.

Workflows describe normal multi-step work systems with stages, participants, outputs, and handoffs.

Runbooks describe concrete operating steps, exception handling, stop conditions, escalation, and verification for a specific repeated situation.

If a file describes a broad end-to-end work system, it belongs in `workflows/`. If it describes concrete checks or exception handling, it may belong in `runbooks/`.

## Runbook vs Pal Skill

A runbook is not a Pal Skill.

Pal Skills describe Pal-owned role-level capabilities and may reference knowledge, workflows, runbooks, tools, approval rules, output contracts, verification, and writeback.

Runbooks may support a Pal Skill, but they do not replace the Skill and do not claim to execute runtime tools.

## Relationship to PalSmith

PalSmith may use runbooks to guide Pal creation / upgrade / classification, but runbooks do not execute actions.

PalSmith remains a no-code Pal asset governance Pal. The host Runtime performs approved file operations only when a task package allows them and current evidence is available.

## Blocked and human review guidance

Mark a runbook outcome as `blocked` when:

- required user approval is missing;
- the allowed read or write path is unclear;
- private memory, reports, credentials, or customer data may be involved;
- a Runtime / Agent Skill is needed but availability or permission is unknown;
- moving, deleting, renaming, or reclassifying assets would be required;
- a central roster, registry, `pal.json`, or manifest change would be required.

Human or owner-Pal review is required before:

- promoting a runbook into a Pal Skill;
- converting a workflow into a runbook or a runbook into a workflow;
- using private user material in a public Pal asset;
- changing PalSmith behavior, root files, `pal.json`, central roster, or registry;
- adding command-level instructions that could affect local files, systems, or external services.

## External project boundary

Do not copy PalSmith runbooks into external project `.agentpal/` by default.

External projects remain thin-bound. PalSmith runbooks belong in the AgentPal central workspace unless a separate approved task explicitly creates a public-safe project-local business document.

## No connector / no auto execution

Runbooks are no-code instructions, not connectors or automation scripts.

They must not:

- call external APIs;
- run CLI commands;
- probe Runtime, Skill, plugin, MCP, or business-system availability;
- start scanners, validators, daemons, installers, marketplaces, hubs, or auto execution engines;
- claim that an action was performed without current Runtime evidence.

## No credentials

Runbooks do not save credentials.

Do not store passwords, API keys, tokens, cookies, secrets, customer identifiers, private user memory, private project memory, or private evidence in this directory.

## No keyword route

Runbooks must not create keyword routes, `keyword_map`, `domain_map`, `role_map`, deterministic semantic routing tables, or fixed task-to-Pal dispatch rules.

PalSmith ownership remains case-specific AI judgement using the current request, current roster, available assets, risk, and evidence.

## Related standards

- `standards/pal-asset/pal-asset-directory-standard.md`
- `standards/pal-asset/pal-skill-vs-agent-skill-standard.md`
- `standards/palsmith/palsmith-v0.5-creation-standard.md`
- `standards/palsmith/palsmith-asset-classification-standard.md`
- `templates/pal-asset/safe-index-backfill-guide.md`
