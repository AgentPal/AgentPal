# Memory

## Purpose

This directory lists public-safe durable memory records or memory policy notes
owned by PalSmith.

PalSmith memory stores extracted long-term lessons about Pal creation, Pal
upgrade, asset classification, Pal governance, readiness review, import/export
boundaries, and evidence discipline. Memory is not a place for full task
reports, raw research drafts, or current mutable state.

## What Belongs Here

- Extracted long-term Pal creation and Pal upgrade lessons.
- Stable asset-classification and Pal governance lessons after review.
- Durable evidence-review patterns from completed PalSmith work.
- Public-safe memory policy notes for Pal lifecycle, readiness, and controlled
  write boundaries.
- Pointers to central project memory records when a lesson is project-specific.
- Improvement suggestions that require future human or owner-Pal review before
  changing official assets.

## What Does Not Belong Here

- Full completion reports, health reports, import/export reports, release
  reports, or audit reports. Reports belong in `reports/`.
- Research drafts, source inventories, evidence matrices, design notes, or
  unverified findings. Research belongs in `research/`.
- Candidate asset ideas, unresolved improvements, and raw observations that
  still need classification. Candidate ideas belong in `learning/` when that
  directory exists, or should be recorded as `needs-review` until a learning
  area is approved.
- Current mutable task state.
- Credentials, tokens, cookies, passwords, API keys, secrets, private customer
  data, private project evidence, or private user memory.
- Keyword routing maps, domain maps, role maps, fixed Pal assignment tables, or
  deterministic dispatch rules.
- External project `.agentpal/memory/` as a default target.

## Current Assets

| Asset | Memory purpose | Status | Notes |
| --- | --- | --- | --- |
| `README.md` | Public-safe PalSmith memory boundary and directory index. | present | Documentation-only; not a behavior change. |

## Candidate Memories / Needs Review

| Candidate | Source report / evidence | Review status |
| --- | --- | --- |
| Pal creation and upgrade lessons | Completed PalSmith creation, upgrade, or readiness reports. | needs-review |
| Asset classification lessons | Evidence-backed classification outcomes and correction reports. | needs-review |
| Pal governance boundary lessons | Import/export, registration, lifecycle, or publish-quality gate reports. | needs-review |
| PalSmith self-health improvement lessons | PalSmith self-health review results and formal asset coverage audits. | needs-review |

## Relationship To Reports

Reports stay in `reports/` as task, health, import/export, release, readiness,
or evidence records. A report may produce a memory candidate only after a stable
lesson is extracted, de-identified, and reviewed.

## Relationship To Research

Research drafts and source context stay in `research/`. Research may produce a
memory candidate only after a durable PalSmith governance lesson has been
reviewed and separated from raw sources or uncertain claims.

## Relationship To Learning

Candidate asset ideas and unclassified improvement notes belong in `learning/`
when that directory is present or approved. Memory should not become a dumping
ground for unresolved ideas.

## Central Roster And Official Asset Boundary

PalSmith memory can suggest improvements, but it cannot automatically rewrite
central contacts, registry files, official Pal assets, `pal.json` files, or
asset manifests. Those changes require a separate confirmed task package,
current runtime evidence, and the relevant governance checks.

## Public Safety Boundary

Public memory indexes must not expose credentials, tokens, cookies, passwords,
API keys, secrets, private customer data, private user memory, private project
memory, private reports, or private evidence.

## External Project Boundary

Do not write PalSmith memory into an external project `.agentpal/` directory by
default. External projects remain thin-bound; PalSmith memory belongs in the
central Pal Pack or approved central records.

## No Keyword Routing Boundary

Memory may preserve lessons that inform future AI judgement, but it must not
define keyword triggers, task-domain tables, role maps, fixed Pal assignments,
or deterministic dispatch rules.
