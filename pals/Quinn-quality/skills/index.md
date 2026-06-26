# Quinn Skills Index

Status: R-DefaultPal-05.

Quinn has two skill layers:

- legacy directory skills under `skills/<skill-id>/SKILL.md`;
- R05 Quality / Verification Lead skill cards under `skills/*.md`.

## R05 Quality / Verification Lead Skill Cards

| Skill | Path | Description |
| --- | --- | --- |
| quality-intake-skill | `skills/quality-intake-skill.md` | Intake quality requests and define evidence path. |
| acceptance-criteria-design-skill | `skills/acceptance-criteria-design-skill.md` | Design clear, verifiable acceptance criteria. |
| definition-of-done-design-skill | `skills/definition-of-done-design-skill.md` | Define whole-task completion standards. |
| test-strategy-planning-skill | `skills/test-strategy-planning-skill.md` | Plan risk-aware test strategy. |
| evidence-review-skill | `skills/evidence-review-skill.md` | Map claims to proof and classify evidence. |
| false-completion-detection-skill | `skills/false-completion-detection-skill.md` | Detect incomplete work reported as complete. |
| regression-gate-design-skill | `skills/regression-gate-design-skill.md` | Design regression checks and evidence gates. |
| release-quality-gate-skill | `skills/release-quality-gate-skill.md` | Review release readiness and residual risk. |
| risk-severity-classification-skill | `skills/risk-severity-classification-skill.md` | Classify quality and release risks. |
| not-run-handling-skill | `skills/not-run-handling-skill.md` | Preserve not-run, partial, and blocked states. |
| quality-report-writing-skill | `skills/quality-report-writing-skill.md` | Write concise quality reports. |
| cross-pal-review-skill | `skills/cross-pal-review-skill.md` | Review multi-Pal results without erasing ownership. |

## Legacy Directory Skills

| Skill | Runtime entry | Description |
| --- | --- | --- |
| acceptance-criteria-review | `skills/acceptance-criteria-review/SKILL.md` | Review whether criteria are clear and verifiable. |
| bug-reproduction-review | `skills/bug-reproduction-review/SKILL.md` | Review whether bug reproduction evidence is sufficient. |
| change-scope-review | `skills/change-scope-review/SKILL.md` | Review changed scope, files, dependencies, and boundaries. |
| evidence-audit | `skills/evidence-audit/SKILL.md` | Audit evidence for completion claims. |
| quality-report-writer | `skills/quality-report-writer/SKILL.md` | Produce quality review reports. |
| quality-task-intake | `skills/quality-task-intake/SKILL.md` | Identify review target and required Quinn skill path. |
| regression-plan-writer | `skills/regression-plan-writer/SKILL.md` | Write risk-prioritized regression plans. |
| release-gate-review | `skills/release-gate-review/SKILL.md` | Review release readiness. |
| risk-assessment | `skills/risk-assessment/SKILL.md` | Assess product, technical, privacy, and release risks. |
| rollback-readiness-review | `skills/rollback-readiness-review/SKILL.md` | Review rollback or downgrade readiness. |
| security-privacy-review | `skills/security-privacy-review/SKILL.md` | Review basic security and privacy boundaries. |
| test-case-design | `skills/test-case-design/SKILL.md` | Design test cases for features, flows, docs, and agent tasks. |

## Context Loading Rule

Read this index only after Quinn is selected as owner, consultant, reviewer, or direct `/pal Quinn` target. Choose the smallest relevant asset slice. Do not load every Quinn asset by default.

## Formal Skill Asset Map

R13 formal skill mapping lives in `skill-asset-map.md`. It maps every `pal.json` formal skill to either a Flat Skill Card or a Directory Skill Package and records missing assets as release-readiness issues.
