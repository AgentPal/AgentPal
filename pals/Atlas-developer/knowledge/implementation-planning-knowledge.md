# Implementation Planning Knowledge

## Concept explanation

Implementation planning turns a development request into ordered stages, allowed files, forbidden files, verification steps, risks, and rollback notes.

## Judgement standards

- The goal must be behavior-based and verifiable.
- The edit surface should be as small as the task allows.
- Each stage needs acceptance criteria and evidence.
- Risky changes need approval before runtime action.

## Examples

- Good: "Change the login error message in `LoginForm`, update its unit test, and verify the error path manually."
- Good: "Do not modify authentication middleware or database schema."
- Good: "Stop if the fix requires a dependency upgrade."

## Counterexamples

- Bad: "Improve the login flow" with no target behavior.
- Bad: Include unrelated refactor in a bug fix.
- Bad: Make release notes part of implementation when not requested.

## Scope

Use for feature work, bug fixes, refactors, and code-review repair tasks.

## How it becomes skill / workflow / eval

Use with `implementation-planning-skill.md`, `implementation-task-package-workflow.md`, `feature-implementation-runbook.md`, and `atlas-task-package-eval.md`.

## Common mistakes

- Skipping file boundaries.
- Hiding assumptions.
- Planning without verification.
- Treating design preference as acceptance criteria.

## Source references or local notes

External: A01, A05, A15. Local: `knowledge/prompt/dev-task-prompt-structure.md`.
