# Existing Pal Upgrade Asset Execution Guide

Existing Pal upgrades are not just edits to `PAL.md` or persona text. If the
requested change affects how a Pal thinks, speaks, works, remembers,
collaborates, uses tools, appears in discovery, or may be published, PalSmith
should use the composite upgrade path.

## When This Applies

Use this guide when a user asks to add or change:

- voice, tone, or personality;
- thinking style or cognitive model;
- role duties or job boundary;
- knowledge or source material;
- workflow, runbook, Skill, or Agent use;
- memory or learning rules;
- collaboration, discovery, contacts, or Marketplace boundary;
- quality gates or release-readiness evidence.

## Upgrade Flow

1. Judge the request with AI judgement, not keyword routing.
2. Read the current target Pal inventory.
3. Classify impact: simple typo, documentation note, composite upgrade, or
   blocked request.
4. Produce a Task Asset Packet.
5. Produce a target file map.
6. List allowed write paths and blocked write paths.
7. Ask a confirmation question before any core write.
8. Let the host runtime perform approved writes.
9. Produce Asset Use Summary and eval evidence.

## What Not To Do

- Do not directly edit core identity assets before an upgrade plan.
- Do not make persona-only changes and call the Pal executable.
- Do not treat ImageGen, shell, Codex, Claude Code, MCP tools, or plugins as
  Pal assets.
- Do not modify central contacts or official status as part of an ordinary
  upgrade.
- Do not write private memory or customer data into public Pal assets.

## Luma-Style Example

Suppose the user says:

```text
Upgrade Luma into a better visual design Pal and let it generate images.
```

Safe handling:

- state whether a real Luma Pal exists in the current workspace;
- if absent, mark the work as a Luma-style example or fixture only;
- do not claim real Luma was changed;
- do not copy character lines, protected text, or real-person likeness;
- do not call ImageGen before design assets, workflow, tool policy, and quality
  gate are defined;
- produce a Missing Asset Plan if design assets are absent.

The correct goal is not "make the tool run." The goal is to make the Pal's
identity, design judgement, workflow, tool boundary, and quality review strong
enough that a later tool request is well formed and reviewable.

## Write Evidence

After an approved write, the report should state:

- files changed;
- why each file belongs to the upgrade;
- assets used;
- missing assets;
- tests or evals run;
- blocked paths preserved;
- whether contacts, official status, Marketplace, runtime, backend, scanner,
  daemon, connector, and release state stayed unchanged.
