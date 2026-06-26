# Code Review Knowledge

## Concept explanation

Code review is an evidence-based engineering review of a change against the requested behavior, code health, maintainability, risk, and tests.

## Judgement standards

- Findings lead the review and are ordered by severity.
- Review checks behavior, scope, tests, risk, maintainability, and security.
- File/line evidence or changed-file evidence should ground findings.
- If no findings are present, report remaining risk and test gaps.

## Examples

- Good: "This change handles the happy path but not the null response path; add a regression test."
- Good: "This file is outside the allowed scope; explain or revert."
- Good: "No findings, but browser verification was not run."

## Counterexamples

- Bad: Style-only review that misses behavior risk.
- Bad: "Looks good" without tests or diff evidence.
- Bad: Treating AI review as release approval.

## Scope

Use after runtime changes, pull request summaries, patches, and release checks.

## How it becomes skill / workflow / eval

Use with `code-review-skill.md`, `code-review-workflow.md`, and `atlas-evidence-verification-eval.md`.

## Common mistakes

- Not checking original acceptance criteria.
- Missing out-of-scope changes.
- Reporting suggestions as blockers without severity.
- Skipping source and task evidence.

## Source references or local notes

External: A06, A07, A08, A13. Local: `knowledge/code-review/review-checklist.md`.
