# release-safety-review

## Purpose

Review whether a release or release-candidate state is safe from a system/runtime boundary perspective.

## When to use

Use before release claims, publish readiness, Pal Pack export, docs release, or any task that could imply production readiness.

## Inputs

Release scope, changed files, no-code boundary results, JSON parse results, diff check, status summary, ignored paths, private state/report boundaries, and rollback plan.

## Required context

Release safety knowledge, no-code boundary audit, evidence review, rollback readiness, and PalSmith publish governance when Pal assets are involved.

## Process

1. Confirm release scope and what is not in scope.
2. Check no-code boundary.
3. Check required JSON and index parse.
4. Check evidence for required gates.
5. Check private memory/state/report exposure.
6. Check rollback or recovery readiness.
7. Report pass, conditional pass, blocked, or not-run.

## Output

Release safety review with gate results, evidence, remaining risk, and next action.

## Quality bar

Release safety must be evidence-backed and must not hide dirty worktree or missing publish proof.

## User confirmation points

Ask before publishing, tagging, pushing, exporting with memory, or changing release scope.

## No-code boundary

This skill reviews release artifacts. It does not publish or create release tooling.

## Common mistakes

- Calling a dirty tree publish-ready.
- Treating docs consistency as complete release safety.
- Ignoring ignored private reports.
- Omitting rollback readiness.

## Example

"Content gates pass, but publishing is conditional because no remote release evidence was produced and the worktree is dirty."

