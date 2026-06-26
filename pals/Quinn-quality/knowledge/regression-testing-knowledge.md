# Regression Testing Knowledge

## Concept Explanation

Regression testing checks whether existing behavior still works after a change. It is chosen by impact and risk, not by a generic desire to test everything.

## Judgement Standards

- Identify affected and neighboring paths.
- Prioritize high-user-impact and shared components.
- Include smoke checks for critical paths.
- Record skipped regression checks.
- Use project evidence to choose depth.

## Examples

- Registry edits require contacts/registry consistency checks.
- Documentation contract edits require placeholder and required-section scans.
- Frontend layout edits require viewport checks.

## Counterexamples

- Testing only new files when shared indexes changed.
- Running unrelated broad checks while ignoring touched assets.

## Scope

Use for code changes, Pal asset changes, docs changes, registry changes, release candidates, and bug fixes.

## How This Becomes Skill, Workflow, Or Eval

It supports `regression-gate-design-skill.md`, `regression-gate-workflow.md`, and `regression-review-runbook.md`.

## Common Mistakes

- No impact analysis.
- No evidence per regression item.
- Treating low-risk as no-risk.

## Source Refs Or Local Notes

Sources: ISTQB risk-based testing glossary, Google Testing Blog, Martin Fowler Practical Test Pyramid.
