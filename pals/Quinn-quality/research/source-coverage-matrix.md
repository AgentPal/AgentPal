# Quinn Source Coverage Matrix

Access date: 2026-06-26.

| Quinn capability | Supporting sources | Asset coverage | Remaining uncertainty |
| --- | --- | --- | --- |
| quality-verification-role | QV-S09, QV-S10, QV-S11, QV-S13 | `knowledge/quality-verification-role-knowledge.md`, `skills/quality-intake-skill.md` | Role remains Pal-layer judgement, not runtime execution. |
| acceptance-criteria-design | QV-S02 | `knowledge/acceptance-criteria-knowledge.md`, `skills/acceptance-criteria-design-skill.md`, `workflows/acceptance-criteria-workflow.md` | Project-specific acceptance wording may need user materials. |
| definition-of-done | QV-S01 | `knowledge/definition-of-done-knowledge.md`, `skills/definition-of-done-design-skill.md` | Organization-level DoD may vary. |
| test-strategy-planning | QV-S03, QV-S04 | `knowledge/test-strategy-knowledge.md`, `skills/test-strategy-planning-skill.md` | Test pyramid is a heuristic, not a universal mandate. |
| evidence-review | QV-S07, QV-S09, QV-S11 | `knowledge/evidence-review-knowledge.md`, `skills/evidence-review-skill.md`, `workflows/evidence-review-workflow.md` | Runtime must provide actual evidence. |
| false-completion-detection | QV-S10, QV-S11, QV-S12 | `knowledge/false-completion-knowledge.md`, `skills/false-completion-detection-skill.md`, `runbooks/false-completion-check-runbook.md` | AI-agent false completion patterns evolve with runtime behavior. |
| regression-gate | QV-S03, QV-S04, QV-S05 | `knowledge/regression-testing-knowledge.md`, `skills/regression-gate-design-skill.md`, `workflows/regression-gate-workflow.md` | Actual coverage depends on project architecture. |
| release-quality-gate | QV-S06, QV-S07, QV-S08 | `knowledge/release-quality-gate-knowledge.md`, `skills/release-quality-gate-skill.md`, `workflows/release-quality-gate-workflow.md` | AgentPal release remains no-code and local unless external publish evidence exists. |
| risk-severity-classification | QV-S05 | `knowledge/risk-severity-knowledge.md`, `skills/risk-severity-classification-skill.md` | Severity may need domain-specific calibration. |
| not-run-handling | QV-S07, QV-S10, local memory honesty rule | `knowledge/not-run-partial-blocked-knowledge.md`, `skills/not-run-handling-skill.md`, `runbooks/not-run-triage-runbook.md` | not-run is context-sensitive: may be acceptable risk or blocker. |
| quality-report-writing | QV-S11 | `knowledge/quality-reporting-knowledge.md`, `skills/quality-report-writing-skill.md`, `workflows/quality-reporting-workflow.md` | Reports must stay concise for user-facing contexts. |
| cross-pal-review | QV-S09, QV-S13 | `knowledge/cross-pal-review-knowledge.md`, `skills/cross-pal-review-skill.md`, `workflows/cross-pal-quality-review-workflow.md` | Current v0.1 uses Simple Pal Mode, not multi-agent execution. |
