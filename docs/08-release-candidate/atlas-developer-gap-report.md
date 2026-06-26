# Atlas Developer Job Fitness Gap Report

Status: R-DefaultPal-02 PalSmith-style inspection output.

Target Pal: `pals/Atlas-developer`

Inspection date: 2026-06-26

## PalSmith-style overall judgement

Atlas already has a useful developer-Pal foundation: identity files, output contract, 12 existing formal skills, basic testing / review / evidence knowledge, a development lifecycle workflow, and several examples. It is not empty.

However, Atlas is still too close to a broad "development-oriented perspective" and not explicit enough as AgentPal's official Developer / Implementation Lead Pal. The existing assets cover task handoff and evidence review, but they do not yet provide a complete job model for implementation planning, Runtime Task Package writing, file-boundary control, release engineering, regression handling, multi-Pal collaboration, and evidence-based verification.

Current fitness estimate: 74 / 100.

Target after this upgrade: 88-92 / 100 for internal AgentPal v0.1 use.

## Dimension scores

| Dimension | Score | Reason |
| --- | ---: | --- |
| Role Fit | 4 | Atlas is clearly development-oriented, but the Implementation Lead role needs stronger wording. |
| Developer Expertise Depth | 3 | Existing knowledge covers basics, but lacks source-backed implementation planning, release engineering, and regression models. |
| Implementation Planning Coverage | 3 | Requirement-to-task exists; a full implementation planning skill and workflow are missing. |
| Runtime Task Package Skill | 3 | Existing prompt structure is useful, but the required task package fields need a stable skill and knowledge card. |
| File Boundary Control | 2 | Boundaries exist, but no dedicated skill / knowledge / eval checks scoped-file discipline. |
| Code Review Knowledge | 3 | Code review checklist exists; needs sourced review standards and evidence expectations. |
| Test Strategy Knowledge | 3 | Basic test plan exists; needs broader test strategy, regression, manual verification, and not-run handling. |
| Release Engineering Knowledge | 2 | Release readiness exists but lacks repeatable release engineering workflow and evidence model. |
| Regression Handling | 2 | Debugging exists, but regression-specific prevention and return path are shallow. |
| Evidence-based Verification | 4 | Existing evidence review is one of the stronger assets. |
| Collaboration Fit | 3 | Collaboration boundaries exist generically; default Pal collaboration needs explicit Atlas-level map. |
| No-code Boundary Understanding | 4 | Atlas already states it is not the runtime; must keep this through the upgrade. |
| Prompt / Task Package Quality | 3 | Good core shape, but incomplete for rollback, forbidden files, evidence, and final report format. |
| User Clarification Ability | 2 | Missing a dedicated clarification method for development tasks. |
| Risk and Approval Handling | 3 | Security skill exists; code-change approval gate needs a dedicated skill. |

## Current positioning problems

- Atlas is described as "development and engineering" but not consistently as Developer / Implementation Lead.
- Existing skills are mostly older directory-based `SKILL.md` assets; the R02 required role model needs explicit top-level skill cards.
- Current knowledge is useful but not source-backed enough for modern coding-agent workflows.
- Workflows and runbooks are under-covered compared with Mira's recent deepening.
- Evals test older "suitable implementation collaborator" wording and need direct Atlas Developer / Implementation Lead evals.

## Existing skills

Existing formal skills include developer task intake, requirement-to-agent-task, multi-thread dispatch, repository handoff, execution evidence review, debugging, code review, test planning, architecture review, context engineering, source-driven development, and security hardening.

## Missing skills

Required additions:

- development-intake-skill
- implementation-planning-skill
- runtime-task-package-writing-skill
- file-boundary-control-skill
- code-review-skill
- test-strategy-skill
- regression-debugging-skill
- release-engineering-skill
- evidence-based-verification-skill
- developer-handoff-skill
- risk-and-approval-for-code-changes-skill
- multi-agent-development-coordination-skill

## Existing knowledge

Existing knowledge covers Atlas role, boundary, prompt structure, context pack design, code review checklist, basic testing, debugging, security boundary, and evidence review.

## Missing knowledge

Required additions:

- developer-role-knowledge
- implementation-planning-knowledge
- runtime-task-package-knowledge
- file-boundary-knowledge
- code-review-knowledge
- test-strategy-knowledge
- regression-debugging-knowledge
- release-engineering-knowledge
- definition-of-done-knowledge
- evidence-based-verification-knowledge
- multi-agent-development-knowledge
- no-code-agentpal-boundary-knowledge
- default-pal-collaboration-boundaries

## Existing workflows

Existing workflow coverage is mainly one development lifecycle workflow.

## Missing workflows

Required additions:

- development-request-intake-workflow
- implementation-task-package-workflow
- code-review-workflow
- test-and-verification-workflow
- regression-fix-workflow
- release-readiness-workflow
- multi-agent-development-workflow
- collaboration-with-default-pals

## Missing runbooks

Required additions:

- small-bugfix-runbook
- feature-implementation-runbook
- refactor-safety-runbook
- release-candidate-review-runbook
- failed-test-triage-runbook

## Needed web research

Research should cover AI coding agent workflows, context engineering, code review, testing and regression, release engineering, definition of done, and coding-agent complacency / review risk.

## Needed evals

Required additions:

- atlas-developer-capability-eval
- atlas-task-package-eval
- atlas-file-boundary-eval
- atlas-evidence-verification-eval
- atlas-release-readiness-eval
- atlas-self-health-eval

## Priority list

### P0

- Preserve no-code AgentPal boundary.
- Prevent Atlas from being described as the runtime, test runner, CLI, scanner, validator, or keyword router.
- Require evidence for completion claims.
- Add Runtime Task Package writing and file-boundary control.

### P1

- Add source-backed developer knowledge and source inventory.
- Add implementation planning, test strategy, regression, release engineering, and review workflows.
- Add default Pal collaboration boundaries.
- Add evals and self-health report.

### P2

- Later run real task simulations after the default Pal deepening series.
- Later decide whether older Atlas examples should be refreshed to the new terminology.

## PalSmith-style upgrade task package

### Goal

Upgrade Atlas into AgentPal's official Developer / Implementation Lead Pal with complete Markdown / JSON assets and source-backed developer job knowledge.

### Files to read

- AgentPal root entry files and contacts / registry.
- PalSmith PAL / SKILL / AGENTS / pal.json / quality protocols / relevant skills and knowledge.
- Mira default boundary and PalSmith routing guidance.
- Atlas root, identity, core, skill index, knowledge index, workflow index, runbook index, existing representative skills, knowledge, and evals.

### Files allowed to edit

- `pals/Atlas-developer/**`
- `README.md`
- `docs/README.md`
- `docs/08-release-candidate/atlas-developer-gap-report.md`
- `agentpal.json`
- `registry/pal.index.json`
- `contacts/pals.json`

### Files forbidden to edit

- Other default Pal professional bodies, except no edits are planned.
- Runtime adapters, tools, scripts, packages, installers, UI, scanner, validator, and code files.
- Private memory, state, and report directories.

### Required docs and assets

- Atlas research source inventory and coverage matrix.
- Atlas skills, knowledge, workflows, runbooks, evals, and self-health report.
- Updated Atlas indexes and entry files.

### Acceptance criteria

- Atlas is clearly Developer / Implementation Lead, not runtime.
- Required skills, knowledge, workflows, runbooks, evals exist and are substantive.
- Source inventory maps sources into actual Atlas assets.
- JSON files parse.
- No-code checks find no prohibited new code files.
- Forbidden positive claims are absent or only appear as prohibitions.
- `git diff --check` and `git status --short` are reported.

### Verification commands or evidence

- JSON parse for AgentPal and target Pal files.
- `rg` checks for prohibited file types, prohibited wording, content placeholders, and required anchors.
- `git diff --check`
- `git status --short`

### Risk boundary

No stage, commit, tag, push, publish, dependency install, tool creation, or executable file creation.

### Rollback notes

All changes are Markdown / JSON and can be reviewed or reverted file-by-file. No generated runtime state is required.

### Final report format

Use the R-DefaultPal-02 final report headings from the user prompt and state not-run or ignored-file caveats honestly.
