# Mira Knowledge Index

Mira knowledge is organized as short, usable cards.

These cards are adapted from AgentPal design requirements and Mira reference materials. Old AgChat wording has been converted to AgentPal where relevant.

Mira knowledge is not a complete encyclopedia. It helps Mira explain AgentPal, triage tasks, route Pals, protect privacy, manage project workgroups, and summarize evidence.

## R18 Leader Knowledge

- `main-pal-leadership-knowledge.md` - Mira's Main Pal / Leader Pal role model.
- `chief-of-staff-and-team-coordination-knowledge.md` - external Chief of Staff and team coordination references adapted to AgentPal.
- `task-triage-knowledge.md` - request classification standards.
- `delegation-and-handoff-knowledge.md` - consult / delegate / handoff distinction.
- `context-packet-knowledge.md` - bounded context packet design.
- `progress-reporting-knowledge.md` - progress and status report standards.
- `decision-memory-writeback-knowledge.md` - decision log and memory writeback boundaries.
- `risk-approval-boundary-knowledge.md` - approval gates and sensitive operations.
- `pal-team-roles-knowledge.md` - how to use contacts / registry without turning them into fixed routes.
- `conflict-resolution-knowledge.md` - summarizing disagreements and escalation choices.
- `default-pal-boundaries.md` - what Mira may and may not own by default.

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
