# Skills Index

Pal: Quinn

## Purpose

This directory lists Quinn-owned Pal Skills for Quality / Verification Lead work.

These files are navigation and method assets only. They do not change Quinn identity, direct calls, routing, output contracts, runtime behavior, or central roster records.

## Pal Skill definition

A Pal Skill is a Pal-owned role-level work capability. It helps Quinn organize recurring quality work through acceptance criteria, Definition of Done, evidence review, risk classification, release gates, regression planning, false-completion detection, not-run handling, and verification reports.

Pal Skills may reference runtime tools, Agent Skills, workflows, runbooks, examples, and evals. The Pal Skill remains the organizational method; it does not execute tests, builds, checks, or release actions by itself.

## Agent Skill boundary

This directory stores Pal Skills, not Runtime Agent Skills.

Agent Skills are host-runtime execution capabilities such as test running, browser automation, file inspection, shell command use, package installation, screenshot capture, or GitHub check inspection. Agent Skills should be referenced as execution candidates, not copied into this directory.

Do not store raw CLI command docs as a Pal Skill unless they are rewritten as a Pal-owned method with context, approval, runtime boundary, verification, and memory writeback rules.

## What belongs here

- Quinn-owned methods for acceptance criteria, quality intake, test strategy, evidence review, false-completion detection, release quality, risk review, and quality reporting.
- Skill packages or flat skill cards that include purpose, activation conditions, required context, output expectations, verification, and writeback rules.
- References to related Quinn knowledge, workflows, runbooks, examples, evals, and Agent Skill candidates.
- Public-safe notes that help a runtime load the smallest relevant Quinn asset slice.

## What does not belong here

- Runtime Agent Skills, plugins, MCP tools, tool installers, scanner configs, validator logic, API clients, connectors, daemons, or marketplace/hub programs.
- Keyword route maps, `keyword_map`, `domain_map`, `role_map`, or deterministic dispatch tables.
- Raw command manuals, copied runtime skill files, credentials, tokens, secrets, private project data, private user memory, reports, raw research dumps, or runtime state.
- New concrete Pal Skill content that has not been reviewed as a Quinn role-level method.

## Current assets

### Flat Skill Cards

These top-level Markdown skill cards strengthen Quinn's Quality / Verification Lead job fitness. They complement the directory-based `SKILL.md` assets.

| Skill card | Purpose | Status |
| --- | --- | --- |
| `quality-intake-skill.md` | Intake quality requests and define evidence path. | present |
| `acceptance-criteria-design-skill.md` | Design clear, verifiable acceptance criteria. | present |
| `definition-of-done-design-skill.md` | Define whole-task completion standards. | present |
| `test-strategy-planning-skill.md` | Plan risk-aware test strategy. | present |
| `evidence-review-skill.md` | Map claims to proof and classify evidence. | present |
| `false-completion-detection-skill.md` | Detect incomplete work reported as complete. | present |
| `regression-gate-design-skill.md` | Design regression checks and evidence gates. | present |
| `release-quality-gate-skill.md` | Review release readiness and residual risk. | present |
| `risk-severity-classification-skill.md` | Classify quality and release risks. | present |
| `not-run-handling-skill.md` | Preserve not-run, partial, and blocked states. | present |
| `quality-report-writing-skill.md` | Write concise quality reports. | present |
| `cross-pal-review-skill.md` | Review multi-Pal results without erasing ownership. | present |

### Directory Skill Packages

| Skill | Runtime entry | Description | Status |
| --- | --- | --- | --- |
| acceptance-criteria-review | `skills/acceptance-criteria-review/SKILL.md` | Review whether criteria are clear and verifiable. | present |
| bug-reproduction-review | `skills/bug-reproduction-review/SKILL.md` | Review whether bug reproduction evidence is sufficient. | present |
| change-scope-review | `skills/change-scope-review/SKILL.md` | Review changed scope, files, dependencies, and boundaries. | present |
| evidence-audit | `skills/evidence-audit/SKILL.md` | Audit evidence for completion claims. | present |
| quality-report-writer | `skills/quality-report-writer/SKILL.md` | Produce quality review reports. | present |
| quality-task-intake | `skills/quality-task-intake/SKILL.md` | Identify review target and required Quinn skill path. | present |
| regression-plan-writer | `skills/regression-plan-writer/SKILL.md` | Write risk-prioritized regression plans. | present |
| release-gate-review | `skills/release-gate-review/SKILL.md` | Review release readiness. | present |
| risk-assessment | `skills/risk-assessment/SKILL.md` | Assess product, technical, privacy, and release risks. | present |
| rollback-readiness-review | `skills/rollback-readiness-review/SKILL.md` | Review rollback or downgrade readiness. | present |
| security-privacy-review | `skills/security-privacy-review/SKILL.md` | Review basic security and privacy boundaries. | present |
| test-case-design | `skills/test-case-design/SKILL.md` | Design test cases for features, flows, docs, and agent tasks. | present |

Supporting files:

| Asset | Purpose | Status |
| --- | --- | --- |
| `README.md` | Human-readable skills directory note. | present |
| `skill-asset-map.md` | Formal skill mapping from `pal.json` skills to flat cards or directory packages. | present |

## Candidate skills / needs review

| Candidate | Reason | Review status |
| --- | --- | --- |
| none added in R106-B | This batch is index-only and must not create new Quinn skill content. | not-run |

If future Quinn Agent Skill candidates appear in runtime registries, review them separately before referencing them here.

## Agent Skill references

Quinn Pal Skills may reference host-runtime execution capabilities such as test runners, browser checks, file inspection, GitHub check inspection, or screenshot capture only as runtime evidence candidates.

References do not install, enable, probe, or execute Agent Skills. Runtime execution requires current-runtime evidence and the allowed file/command boundary named by the active task.

## Related workflows / runbooks

- `../workflows/index.md`
- `../workflows/quality-gate-lifecycle/`
- `../runbooks/index.md`
- `../runbooks/evidence/`
- `../runbooks/release/`
- `../runbooks/risk/`
- `../runbooks/testing/`

## Verification boundary

Quinn may design verification and review evidence, but completion claims require current runtime evidence. Use `pass`, `fail`, `blocked`, `not-run`, `missing`, or an equivalent explicit status instead of smoothing weak evidence into a pass.

Do not treat directory presence, skill names, or owner claims as proof that tests, checks, builds, releases, or inspections were executed.

## Memory writeback boundary

When the user explicitly asks to save a Skill, or similar operations happen more than three times, create the formal Skill under this Pal's own `skills/<skill-id>/SKILL.md` and update this index in a separate allowed task.

Use `memory/skill-memory/` only for runtime notes before a formal trigger is met. Use `learning/` only when required inputs are missing, content is unsafe/private, or a high-risk write needs approval.

Reports are not memory until stable lessons are extracted. Do not write report text into memory wholesale.

## External project boundary

Do not copy Quinn Pal Skills into an external project `.agentpal/` directory by default.

External projects remain thin-bound. Pal Skills, Pal memory, workflows, runbooks, reports, governance notes, and reusable knowledge stay in the AgentPal central workspace or approved central records.

## Context loading rule

Read this index only after Quinn is selected as owner, consultant, reviewer, or direct `/pal Quinn` target.

Choose the smallest relevant asset slice. Do not load every Quinn asset by default.
