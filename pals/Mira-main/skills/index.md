# Skills Index

This directory contains skills assets for Mira-main. Use it as a navigation index, not as a default context bundle.

## R18 Leader Skills

- `task-intake-and-triage-skill.md` - classify a request into direct answer, Mira-owned leadership work, specialist ownership, clarification, approval stop, or execution briefing.
- `ai-judgement-delegation-skill.md` - make case-specific owner judgement using contacts / registry and current evidence.
- `context-packet-design-skill.md` - prepare bounded handoff context without sweeping whole workspaces or leaking sensitive material.
- `pal-consult-delegate-handoff-skill.md` - choose consult, delegate, or handoff and preserve owner boundaries.
- `progress-summarization-skill.md` - report multi-stage progress, blockers, verification state, and next action in user language.
- `decision-log-and-memory-writeback-skill.md` - turn evidence-backed decisions into writeback candidates while respecting public/private boundaries.
- `risk-and-approval-gating-skill.md` - stop for confirmation before sensitive context sharing or risky execution.
- `conflict-summary-skill.md` - summarize competing Pal advice, tradeoffs, and unresolved choices without flattening specialist ownership.
- `runtime-task-package-briefing-skill.md` - brief Codex or another runtime as execution layer under a Pal-owned task.
- `user-clarification-skill.md` - ask focused questions only when they materially change the next safe action.

## Context Loading Rule

Read this index only after this Pal is selected as owner, consultant, reviewer, or direct /pal Name target.

Use this index to choose the smallest relevant asset slice. Do not load every file in this directory by default.

Read assets here when:

- the current task requires this Pal's professional method;
- the output contract needs a specific skill, knowledge card, runbook, or workflow;
- the user asks which assets were used;
- an eval or release check is inspecting this Pal.

Do not read assets here when:

- Mira is only doing initial routing;
- another Pal owns the task and no consultation was requested;
- the task is ordinary chat, Codex generic, or Mira-owned team-leadership work;
- examples, evals, reports, memory, or future design material would be enough only by curiosity rather than task need.

## Formal Skill Asset Map

R13 formal skill mapping lives in `skill-asset-map.md`. It maps every `pal.json` formal skill to either a Flat Skill Card or a Directory Skill Package and records missing assets as release-readiness issues.
