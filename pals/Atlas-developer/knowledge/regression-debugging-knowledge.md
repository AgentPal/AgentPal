# Regression Debugging Knowledge

## Concept explanation

Regression debugging focuses on behavior that used to work and now fails. It requires a previous expected behavior, a reproduction path, a suspected change window, minimal repair, and prevention evidence.

## Judgement standards

- Identify old behavior and broken behavior separately.
- Prefer minimal repair over broad rewrite.
- Require reproduction or a clear blocker if reproduction is unavailable.
- Add or run a prevention check.

## Examples

- Good: "The save button no longer preserves draft text after the modal rewrite."
- Good: "Check the recent modal diff and add a draft-preservation test."
- Good: "Stop if repair needs schema migration."

## Counterexamples

- Bad: Fixing many unrelated issues in one regression task.
- Bad: No proof the old behavior is restored.
- Bad: Blaming environment without checking recent changes.

## Scope

Use for bug fixes, failed tests, release regressions, and user-reported broken behavior.

## How it becomes skill / workflow / eval

Use with `regression-debugging-skill.md`, `regression-fix-workflow.md`, `small-bugfix-runbook.md`, and `failed-test-triage-runbook.md`.

## Common mistakes

- Guessing root cause too early.
- Forgetting rollback or prevention.
- Turning debugging into refactor.
- Not recording not-run checks.

## Source references or local notes

External: A10. Local: Atlas debugging skill and debug handoff runbook.
