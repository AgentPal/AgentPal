# PalSmith v0.5 Pal Creation And Upgrade

Date: 2026-06-28

## Purpose

This guide summarizes how PalSmith v0.5 standards create, classify, and upgrade
Pal assets without becoming an execution system.

Primary references:

- `standards/palsmith/palsmith-v0.5-creation-standard.md`
- `standards/palsmith/palsmith-asset-classification-standard.md`
- `templates/palsmith/minimal-pal-generation-checklist.md`
- `templates/palsmith/standard-pal-generation-checklist.md`
- `templates/palsmith/pal-asset-classification-result-template.json`
- `templates/palsmith/existing-pal-upgrade-report-template.md`

## Minimal Pal

A Minimal Pal should have:

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

Placeholders are acceptable only when they state the gap honestly and do not
claim full job readiness.

## Standard Pal

A Standard Pal includes the Minimal Pal set plus:

- `research/index.md`
- `learning/index.md`
- `examples/index.md`
- `core/collaboration-protocol.md`
- `core/handoff-protocol.md`
- `core/reporting-protocol.md`
- `core/skill-growth-protocol.md`

It should also include real role-specific knowledge, Pal Skills, workflows,
runbooks, examples, and evals when source material or approved research exists.

## Classification

PalSmith classifies content before writing it.

Typical categories:

- identity
- core protocol
- knowledge
- research
- Pal Skill
- Agent Skill ref
- workflow
- runbook
- learning candidate
- memory candidate
- report
- eval
- example
- Org Pack candidate
- project business doc

Pal Skill is a role-level no-code work capability. Agent Skill is a host Runtime
tool-level execution capability. Agent Skill refs must not be stored as
Pal-owned Skills.

## Existing Pal Upgrade

For an existing Pal, PalSmith should prepare an upgrade report before edits. The
report should cover:

- root entry completeness
- `pal.json` schema readiness
- index completeness
- Pal Skill vs Agent Skill risk
- misplaced content risks
- asset-manifest readiness
- public safety
- recommended fixes
- allowed write paths for a later task package

## Write Boundary

PalSmith defaults to AgentPal central workspace targets for Pal and organization
assets. It must not write central Pal assets into an external project's
`.agentpal/` directory by default.

External project writes are only appropriate when the user explicitly asks for a
project-local business document or approved project file.

## Runtime Boundary

PalSmith is a no-code asset creator and governor. It is not a CLI, scanner,
validator, installer, daemon, database, connector, API client, marketplace, hub,
auto sync engine, or auto execution engine.

Host runtimes may perform real writes only after a bounded task package and must
return evidence. Missing, not-run, blocked, or unknown evidence must stay visible.
