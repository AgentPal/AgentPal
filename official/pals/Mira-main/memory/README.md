# Memory

## Purpose

This directory lists public-safe durable memory records or memory policy notes
owned by Mira.

Mira memory stores extracted long-term lessons, user and Mira coordination
preferences, team-leadership continuity notes, routing lessons, and references
that help Mira remain steady across future AgentPal work. Memory is not a place
for full reports, raw research, or current mutable state.

## What Belongs Here

- Extracted long-term lessons from completed Mira-owned leadership work.
- Stable user and Mira coordination preference summaries when approved.
- Team-leadership, handoff, context-package, progress-reporting, and result
  explanation lessons with evidence references.
- Routing Reward Memory candidates after review, kept as judgement inputs only.
- Pointers to central project memory records when a lesson is project-specific.
- Public-safe memory policy notes.

## What Does Not Belong Here

- Full completion reports, audit reports, release reports, or task reports.
  Reports belong in `reports/`.
- Raw evidence, command logs, or source dumps.
- Research materials or unverified findings. Research belongs in `research/`.
- Current mutable task state. State belongs in `state/` and should usually stay
  local or uncommitted.
- Credentials, tokens, cookies, passwords, API keys, secrets, customer data, or
  private project evidence.
- Unapproved private user memory or private project memory.
- External project `.agentpal/memory/` as a default target.
- Keyword routing maps, domain maps, role maps, or deterministic dispatch rules.

## Current Assets

| Asset | Memory purpose | Status | Notes |
| --- | --- | --- | --- |
| `README.md` | Public-safe memory boundary and directory index. | present | Documentation-only; not a behavior change. |

## Candidate Memories / Needs Review

| Candidate | Source report / evidence | Review status |
| --- | --- | --- |
| Mira coordination preference summaries | Completed Mira-owned task reports or approved user instruction. | needs-review |
| Routing Reward Memory summaries | Evidence-backed routing outcomes and owner judgement results. | needs-review |
| Project-specific continuity pointers | Central project records under `workspace/projects/<project-id>/`. | needs-review |

## Relationship To Reports

Reports stay in `reports/` as task, handoff, health, or verification records. A
report may produce a memory candidate only after a stable lesson is extracted,
de-identified, and reviewed.

## Relationship To Project Records

Project-private memory belongs in the central AgentPal project record under
`workspace/projects/<project-id>/` by default. External project `.agentpal/`
folders remain thin bindings and should not receive Mira memory by default.

## Relationship To Central Operational Knowledge

Stable operational rules and reusable AgentPal knowledge belong in `knowledge/`
or central standards after review. Memory records may point to knowledge, but
they must not replace standards, output contracts, or Pal identity files.

## Public Safety Boundary

Public memory indexes must not expose private user memory, private project
memory, secrets, credentials, tokens, cookies, passwords, API keys, private
evidence, or customer identifiers.

## External Project Boundary

Do not write Mira memory into an external project `.agentpal/` directory by
default. External project binding remains minimal and should point back to the
central AgentPal Workspace or approved central project record.

## No Keyword Routing Boundary

Memory may preserve lessons that help future AI judgement, but it must not
define keyword triggers, task-domain tables, role maps, fixed Pal assignments,
or deterministic dispatch rules.

