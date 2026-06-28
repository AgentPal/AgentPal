# Skills Index

Pal: Morgan

## Purpose

This directory lists Morgan-owned Pal Skills for Document / File Workflow Lead work.

These files are navigation and method assets only. They do not change Morgan identity, direct calls, routing, output contracts, runtime behavior, or central roster records.

## Pal Skill definition

A Pal Skill is a Pal-owned role-level work capability. It helps Morgan organize recurring document and file workflow work through context, preservation rules, file privacy review, output planning, handoff, quality review, verification, and memory or learning writeback.

Pal Skills may reference runtime tools, Agent Skills, workflows, runbooks, examples, and evals. The Pal Skill remains the organizational method; it does not parse, convert, export, upload, download, or edit files by itself.

## Agent Skill boundary

This directory stores Pal Skills, not Runtime Agent Skills.

Agent Skills are host-runtime execution capabilities such as PDF processing, spreadsheet editing, document rendering, OCR, archive extraction, browser download, shell command use, or file conversion. Agent Skills should be referenced as execution candidates, not copied into this directory.

Do not store raw CLI command docs as a Pal Skill unless they are rewritten as a Pal-owned method with context, approval, runtime boundary, verification, and memory writeback rules.

## What belongs here

- Morgan-owned methods for document intake, information architecture, source material organization, content preservation, Markdown documentation, office/PDF output task packages, file workflow design, document quality review, release notes, and privacy-sensitive document review.
- Skill packages or flat skill cards that include purpose, activation conditions, required context, output expectations, verification, and writeback rules.
- References to related Morgan knowledge, workflows, runbooks, examples, evals, and Agent Skill candidates.
- Public-safe notes that help a runtime load the smallest relevant Morgan asset slice.

## What does not belong here

- Runtime Agent Skills, plugins, MCP tools, tool installers, scanner configs, validator logic, API clients, connectors, daemons, or marketplace/hub programs.
- Keyword route maps, `keyword_map`, `domain_map`, `role_map`, or deterministic dispatch tables.
- Raw command manuals, copied runtime skill files, credentials, tokens, secrets, private project data, private user memory, reports, raw research dumps, runtime state, or full source documents.
- New concrete Pal Skill content that has not been reviewed as a Morgan role-level method.

## Current assets

### Directory Skill Packages

| Skill | Runtime entry | Purpose | Status |
| --- | --- | --- | --- |
| batch-file-organization | `skills/batch-file-organization/SKILL.md` | Batch file organization planning. | present |
| conversion-quality-review | `skills/conversion-quality-review/SKILL.md` | Conversion quality review planning. | present |
| document-processing-plan | `skills/document-processing-plan/SKILL.md` | Document processing task planning. | present |
| duplicate-cleanup-plan | `skills/duplicate-cleanup-plan/SKILL.md` | Duplicate cleanup candidate planning. | present |
| file-privacy-risk-check | `skills/file-privacy-risk-check/SKILL.md` | File privacy risk checks. | present |
| file-search-handoff | `skills/file-search-handoff/SKILL.md` | Metadata-first file search handoff. | present |
| file-task-intake | `skills/file-task-intake/SKILL.md` | File task intake. | present |
| metadata-indexing-plan | `skills/metadata-indexing-plan/SKILL.md` | File metadata indexing plan. | present |
| naming-taxonomy-builder | `skills/naming-taxonomy-builder/SKILL.md` | Naming taxonomy design. | present |
| office-template-fill | `skills/office-template-fill/SKILL.md` | Office template fill task package. | present |
| pdf-task-plan | `skills/pdf-task-plan/SKILL.md` | PDF task planning. | present |
| spreadsheet-task-plan | `skills/spreadsheet-task-plan/SKILL.md` | Spreadsheet task planning. | present |

### Flat Skill Cards

| Skill card | Purpose | Status |
| --- | --- | --- |
| `document-intake-skill.md` | Document role intake. | present |
| `information-architecture-skill.md` | Information architecture planning. | present |
| `source-material-organization-skill.md` | Source material organization. | present |
| `content-preservation-skill.md` | Content preservation review. | present |
| `markdown-documentation-skill.md` | Markdown documentation planning and review. | present |
| `office-output-task-package-skill.md` | Office output task package planning. | present |
| `pdf-output-task-package-skill.md` | PDF output task package planning. | present |
| `file-workflow-design-skill.md` | File workflow design. | present |
| `document-quality-review-skill.md` | Document quality review. | present |
| `versioned-documentation-skill.md` | Versioned documentation planning. | present |
| `release-notes-documentation-skill.md` | Release notes documentation planning. | present |
| `document-handoff-skill.md` | Document handoff. | present |
| `privacy-sensitive-document-review-skill.md` | Privacy-sensitive document review. | present |

Supporting files:

| Asset | Purpose | Status |
| --- | --- | --- |
| `README.md` | Human-readable skills directory note. | present |
| `skill-asset-map.md` | Formal skill mapping from `pal.json` skills to flat cards or directory packages. | present |

Formal skill count recorded by the prior index: 25.

## Candidate skills / needs review

| Candidate | Reason | Review status |
| --- | --- | --- |
| none added in R106-B | This batch is index-only and must not create new Morgan skill content. | not-run |

If future Morgan Agent Skill candidates appear in runtime registries, review them separately before referencing them here.

## Agent Skill references

Morgan Pal Skills may reference host-runtime execution capabilities such as PDF processing, document rendering, spreadsheet editing, OCR, archive extraction, file conversion, or browser download only as runtime evidence candidates.

References do not install, enable, probe, or execute Agent Skills. Runtime execution requires current-runtime evidence and the allowed file/command boundary named by the active task.

## Related workflows / runbooks

- `../workflows/index.md`
- `../workflows/office-file-lifecycle/`
- `../runbooks/index.md`
- `../runbooks/documents/`
- `../runbooks/files/`
- `../runbooks/pdf/`
- `../runbooks/spreadsheets/`

## Verification boundary

Morgan may organize document and file verification, but completion claims require current runtime evidence. Use `pass`, `fail`, `blocked`, `not-run`, `missing`, or an equivalent explicit status instead of smoothing weak evidence into a pass.

Do not treat directory presence, skill names, or owner claims as proof that files were parsed, converted, exported, rendered, uploaded, downloaded, or modified.

## Memory writeback boundary

When the user explicitly asks to save a Skill, or similar operations happen more than three times, create the formal Skill under this Pal's own `skills/<skill-id>/SKILL.md` and update this index in a separate allowed task.

Use `memory/skill-memory/` only for runtime notes before a formal trigger is met. Use `learning/` only when required inputs are missing, content is unsafe/private, or a high-risk write needs approval.

Reports are not memory until stable lessons are extracted. Do not write report text into memory wholesale.

## External project boundary

Do not copy Morgan Pal Skills into an external project `.agentpal/` directory by default.

External projects remain thin-bound. Pal Skills, Pal memory, workflows, runbooks, reports, governance notes, and reusable knowledge stay in the AgentPal central workspace or approved central records.
