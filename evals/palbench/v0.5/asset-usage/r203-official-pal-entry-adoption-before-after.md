# R203 Official Pal Entry Adoption Before / After

Status: Phase 1 before / after summary.

## Before R203

R202 found that the 10 official bundled Pals were structurally strong but had a
shared adoption gap:

- most Pals had identity, role, knowledge, Skill, workflow, boundary, and eval
  assets;
- most Pals did not explicitly name Asset Loading Gate, Task Asset Packet,
  Asset Use Summary, or Missing Asset Plan in sampled entry assets;
- PalSmith was the clearest adopter because it owns Pal asset governance and
  had R198-R201 evidence;
- other official Pals remained mostly `tool_aware_pal` or
  `workflow_capable_pal`, not fully verified for asset usage.

## What R203 Changed

R203 performed Phase 1 entry adoption:

- added a `Pal Asset Execution` section to each official Pal `SKILL.md`;
- added a short Phase 1 adoption note to each official Pal `README.md`;
- preserved lightweight path for greetings, clarifications, typo fixes, simple
  wording edits, and obvious formatting corrections;
- connected complex tasks to Asset Loading Gate and Task Asset Packet or an
  equivalent plan;
- stated that tools and Agent Runtimes are execution tools, not Pal assets;
- required Asset Use Summary or equivalent evidence when needed;
- required Missing Asset Plan or honest limited fallback when required assets
  are missing;
- kept current completeness levels unchanged.

## What R203 Did Not Do

R203 did not:

- add runtime code;
- add backend services;
- add CLI, installer, scanner, daemon, connector, or Marketplace backend;
- complete full migration for every official Pal;
- run representative per-Pal task regressions;
- modify `workspace/organization/contacts/`;
- add or remove official Pals;
- modify real user custom Pal files;
- modify the R200 controlled-write fixture;
- change any official Pal `pal.json`;
- promote draft or user custom Pals.

## After R203

After R203, the official Pals have a consistent entry rule:

```text
Substantive Pal work should use the Pal Asset Execution Contract and Asset
Loading Gate. Lightweight tasks may stay lightweight. Tools are execution
tools, not Pal assets. Missing assets require a Missing Asset Plan or honest
fallback.
```

This closes Phase 1 entry adoption only.

## Next Phases

Phase 2 should add task-specific Task Asset Packet and Asset Use Summary
examples for high-priority Pals.

Phase 3 should run representative asset usage regression for each priority task
family.

Phase 4 should review completeness labels only within the tested scope.
