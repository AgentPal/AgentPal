# Morgan Document / File Workflow Lead Gap Report

Date: 2026-06-26

## PalSmith-style fitness conclusion

Morgan has a credible file and office steward base, but the previous asset set does not yet prove official Document / File Workflow Lead job fitness. Existing assets cover file safety, naming, PDF planning, spreadsheet planning, and office template handoff. The missing layer is document leadership: information architecture, source-material organization, content preservation, Markdown documentation, Office/PDF output task packaging, document quality review, versioned documentation, release notes, privacy-sensitive document handling, and cross-Pal document handoff.

Fitness decision before upgrade: partial.

Upgrade decision: proceed with bounded no-code asset repair under Morgan-owned files plus workspace contacts and registry consistency updates.

## Gap report

| Area | Current evidence | Gap | Required repair |
| --- | --- | --- | --- |
| Identity | Morgan is described as a file and office steward. | Role does not clearly say Document / File Workflow Lead. | Update `PAL.md`, `SKILL.md`, `AGENTS.md`, `README.md`, and `pal.json`. |
| Skills | 12 existing file-oriented skill folders. | Missing document leadership skills and exact section contract. | Add 13 formal document workflow skills. |
| Knowledge | Existing cards cover file safety, PDF, office, conversion, privacy. | Missing source-backed documentation knowledge and document QA standards. | Add 13 knowledge cards with source refs and local notes. |
| Workflows | One office-file lifecycle workflow. | Missing request intake, source-to-doc, Markdown, Office, PDF, release notes, quality review, and handoff workflows. | Add 8 workflow cards and a default-Pal collaboration workflow. |
| Runbooks | 4 existing runbooks. | Missing long-material preservation, README review, release notes, Office export package, PDF export package, sensitive document review. | Add 6 runbooks. |
| Evals | Existing release/self-test notes are broad. | Missing capability-specific evals. | Add 6 Morgan evals plus self-health eval/report. |
| Research | No Morgan-specific source inventory. | Required web research not captured. | Add source inventory and coverage matrix. |
| Collaboration | Existing collaboration is generic. | Needs explicit consult / delegate / handoff boundary with Mira, PalSmith, Atlas, Vega, Rhea, Quinn, Harper, and Nova. | Add collaboration knowledge and workflow. |
| Boundaries | No-code boundary exists but is file-operation focused. | Needs explicit no_runtime_code and no direct Office/PDF/conversion claims. | Update identity and validation assets. |
| Registry | Workspace metadata still says document/file oriented. | Official role and capability anchors missing. | Update root README, docs README, agentpal, contacts, registry. |

## Upgrade task package

### Goal

Upgrade Morgan into AgentPal's official Document / File Workflow Lead Pal while preserving no-code release boundaries and evidence discipline.

### Allowed edit scope

- `pals/Morgan-document/**`
- `evals/palbench/v0.5/documentation/archive/docs/08-release-candidate/morgan-document-workflow-gap-report.md`
- `evals/palbench/v0.5/documentation/archive/docs/08-release-candidate/morgan-self-health-report.md`
- `README.md`
- `docs/README.md`
- `agentpal.json`
- `contacts/pals.json`
- `registry/pal.index.json`

### Required assets

- Root and registry files for official Pal consistency.
- PalSmith job fitness, content preservation, and web-research governance assets.
- Mira, Atlas, Vega, Rhea, and Quinn default collaboration boundary assets.
- Current Morgan identity, output contract, skills, knowledge, workflows, runbooks, and evals.
- Live web research sources recorded in Morgan research inventory.

### Work stages

1. Create this gap report and explicit task package.
2. Record source inventory and source coverage matrix.
3. Upgrade Morgan identity and metadata.
4. Add the required skill, knowledge, workflow, runbook, collaboration, and eval cards.
5. Update indexes and root discovery files.
6. Run no-code, JSON, anchor, forbidden-phrase, section completeness, diff, and status checks.
7. Produce a PalSmith-style review result.

### Acceptance criteria

- Morgan can truthfully be described as official Document / File Workflow Lead.
- All required files exist with non-empty, job-specific content.
- All required skill, knowledge, workflow, and runbook section contracts are present.
- Research files cite source-backed documentation, documentation architecture, accessibility, privacy, Markdown, Office, PDF, docs-as-code, release-notes, and content-quality sources.
- Root contacts, registry, and workspace metadata are consistent.
- No runtime code, tool, UI, installer, daemon, scanner, or validator is added.
- Completion report labels not-run or blocked checks honestly.

### Do-not-do list

- Do not add code files, scripts, runtime dependencies, UI, scanner, validator, installer, daemon, or automated document converter.
- Do not make Morgan a direct Office/PDF executor or file operation executor.
- Do not use fixed routes, keyword-based ownership, Mira-only calling, or Core-as-router wording.
- Do not copy private user materials or long copyrighted text into public assets.
- Do not stage, commit, tag, push, publish, or release.

### Evidence required

- Changed path list.
- JSON parse status.
- Required file and section completeness checks.
- Anchor checks.
- Forbidden phrase and placeholder scan.
- No-code boundary scan.
- `git diff --check`.
- scoped `git status --short`.

## PalSmith-style initial review

This task should be executed by the current Runtime as a file-editing layer after PalSmith-style governance judgement. Atlas-style implementation execution is acceptable only as the editing layer; it must not independently redesign Morgan without this task package. Morgan remains the target Pal. PalSmith remains the governance reviewer.

