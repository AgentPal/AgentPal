# Test Strategy Knowledge

## Concept Explanation

Test strategy is the plan for how to gain confidence efficiently. It chooses check types and depths from risk, change size, user impact, and available Runtime capability.

## Judgement Standards

- Use small, fast checks where they provide enough confidence.
- Use broader checks for high-risk user journeys.
- Avoid relying only on end-to-end checks.
- Match test type to artifact type.
- Record not-run checks and their impact.

## Examples

- Markdown Pal assets need structure, content, JSON, anchor, and no-code checks.
- UI changes may need screenshot or browser verification.
- Runtime changes may need build, smoke, and regression checks.

## Counterexamples

- Running no checks because the change is "only docs" when docs have required contract fields.
- Demanding full E2E for every small copy edit.
- Ignoring changed shared configuration.

## Scope

Use for regression planning, release gates, completion review, and task package verification sections.

## How This Becomes Skill, Workflow, Or Eval

It supports `test-strategy-planning-skill.md`, `regression-gate-design-skill.md`, and `regression-review-runbook.md`.

## Common Mistakes

- No risk prioritization.
- No evidence definition.
- Over-testing low-risk paths and under-testing high-risk paths.

## Source Refs Or Local Notes

Sources: Google Testing Blog on test pyramid, Martin Fowler Practical Test Pyramid, Android testing strategy docs. Local adaptation: Quinn designs checks but Runtime executes them.
