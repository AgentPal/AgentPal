# Specialist Pal Fallback Learning Protocol

Use this protocol when a specialist Pal has no dedicated asset for the requested task family.

## Core Rule

Missing a knowledge card, Skill, Runbook, or Workflow is not a task failure.

The specialist Pal may proceed with fallback method, but must not pretend that a missing specialist asset exists.

## When Fallback Is Allowed

Fallback method is allowed when:

- the task belongs to the Pal's domain
- no relevant specialist asset is found
- the task can be handled safely with general professional method, read-only checks, user-provided context, or execution layer evidence
- risks and uncertainty are reported

Fallback is not enough for high-risk write actions. High-risk changes still require user confirmation and execution-layer evidence.

## Fallback Cannot

- impersonate a missing Skill or knowledge card
- claim a Runbook was used when none was read
- store specialist learning under Mira by default
- skip privacy or approval boundaries
- execute system, file, or command changes without an execution layer

## Required Fallback Report

Use this pattern:

```text
Rhea：
This task belongs to my domain.
I did not find a dedicated startup-item knowledge card or Runbook.
Fallback method is allowed for this read-only audit.

Specialist assets used:
- Rhea/PAL.md
- Rhea/SKILL.md
- Rhea/pal.json

Knowledge gap:
- No dedicated startup-item audit knowledge card found.

Fallback method:
- traditional startup-item audit approach
- current Codex read-only query
- evidence review by Rhea rules

Learning:
- Task family: startup-item-audit
- Repeated task record: pals/Rhea-system/learning/repeated-tasks.md
- Formal Skill trigger: similar operation count > 3 or explicit user request
- Formal Skill target: pals/Rhea-system/skills/<skill-id>/SKILL.md
```

## Learning Destination

Mira cannot own specialist learning.

Specialist learning belongs to the specialist Pal.

The owner Pal records:

- knowledge gaps
- repeated task family count
- formal Skill under its own `skills/` directory when triggered
- Runbook under its own `runbooks/` directory when requested or needed
- Workflow under its own `workflows/` directory when requested or needed
- Knowledge Card under its own `knowledge/` directory when requested or needed

Mira records only:

- route chosen
- collaboration summary
- user preference, if approved
- reminder that the owner Pal should consider capability crystallization

## Repeated Task Threshold

When similar operations happen more than 3 times, the owner Pal must create the formal Skill under its own `skills/` directory and update `skills/index.md`.

Formal Skill path: `pals/<Owner-Pal-Directory>/skills/<skill-id>/SKILL.md`.

Use `learning/` only as an exception when required inputs are missing, content is unsafe/private, or a high-risk write needs approval.

## Explicit User Request Trigger

This is the Repeated Task Skill Creation Gate.

Formal Skill creation is also triggered by explicit user request, even when historical count is unknown.

Explicit trigger examples:

- 以后能不能形成固定流程？
- 这个能不能做成固定检查？
- 下次能不能按同样方式执行？
- 能不能沉淀成 Skill / Runbook？

When the user explicitly asks to save a Skill, the owner Pal creates a formal Skill under its own `skills/` directory and updates `skills/index.md`. When the user explicitly asks for a Runbook, Workflow, or Knowledge Card, the owner Pal stores it under its own `runbooks/`, `workflows/`, or `knowledge/` directory.

The owner Pal should say:

```text
即使我现在不能确认历史计数，只要你明确要求保存为 Skill，我也会把它创建到我的 skills 目录。
```

For Rhea startup item audits, repeated fixed procedures may become a Runbook named `windows-startup-item-audit-runbook` when the user asks for a Runbook or the workflow is better represented as a Runbook than a Skill.

Required creation response fields:

- asset name
- task family
- trigger reason: explicit user request
- draft steps
- safety boundary
- storage target

If these fields are absent, repeated task Skill creation gate fails.

## Evidence Review

Execution layer produces evidence.

Owner Pal reviews evidence.

Mira summarizes evidence and next step.

