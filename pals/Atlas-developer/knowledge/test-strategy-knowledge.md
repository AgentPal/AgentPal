# Test Strategy Knowledge

## Concept explanation

Test strategy defines how a development change will be proven. It includes automatic tests, manual checks, regression paths, and evidence requirements.

## Judgement standards

- Tests should map to behavior and acceptance criteria.
- New behavior, old behavior, error paths, and high-risk paths should be considered.
- Not-run checks must be labeled and explained.
- Manual evidence may be required for UI, browser, document, or external-system behavior.

## Examples

- Good: "Run targeted unit tests, then manual browser check for the edited flow."
- Good: "If Playwright is unavailable, report runtime-unavailable and provide manual steps."
- Good: "Add a regression test for the failing case."

## Counterexamples

- Bad: Build pass treated as full verification.
- Bad: Test plan with no expected result.
- Bad: No regression path for a bug fix.

## Scope

Use for planning, task packages, evidence review, and release readiness.

## How it becomes skill / workflow / eval

Use with `test-strategy-skill.md`, `test-and-verification-workflow.md`, `failed-test-triage-runbook.md`, and `atlas-evidence-verification-eval.md`.

## Common mistakes

- Testing only what changed and not what might break.
- Ignoring test data isolation.
- Hiding unavailable test infrastructure.
- Using broad tests to hide missing targeted checks.

## Source references or local notes

External: A09 and A10. Local: `knowledge/testing/test-plan-basics.md`.
