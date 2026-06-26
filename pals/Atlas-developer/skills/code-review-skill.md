# Code Review Skill

## Purpose

Help Atlas review implementation evidence for behavior, risk, boundary control, maintainability, and test coverage.

## When to use

Use after a runtime returns a diff, changed-file list, pull request, patch, or completion report.

## Inputs

- Original task and acceptance criteria.
- Diff or changed files.
- Test/build/check results.
- Project conventions and risk notes.
- Runtime final report.

## Required context

Read the changed files or diff, relevant tests, and project instructions. If only a summary exists, classify review as evidence-limited.

## Process

1. Start with findings ordered by severity.
2. Check correctness against the original task.
3. Check file boundary and unrelated changes.
4. Check tests, regression paths, and not-run items.
5. Check maintainability, security, performance, and rollback risk.
6. If no issues are found, state remaining test gaps and residual risk.

## Output

A review report with findings first, then open questions, verification state, and brief summary.

## Quality bar

The review must be grounded in file paths, evidence, and task requirements. Style opinions should not be framed as bugs.

## User confirmation points

Ask before approving risky work, accepting missing tests, publishing, or moving from review to release.

## No-code boundary

Atlas reviews; the runtime or human author makes changes and runs checks.

## Common mistakes

- Saying "looks good" without evidence.
- Reviewing only style while missing behavior risk.
- Treating AI-generated output as trusted.
- Ignoring scope creep.

## Example

A patch changes login validation and theme colors. Atlas reviews login behavior against tests and flags theme edits as out of scope unless authorized.
