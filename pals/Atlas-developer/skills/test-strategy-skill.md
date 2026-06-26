# Test Strategy Skill

## Purpose

Design the verification approach for development tasks, including automated tests, manual checks, regression paths, and evidence requirements.

## When to use

Use before implementation and when runtime results lack enough proof.

## Inputs

- Development goal and affected behavior.
- Risk level.
- Available test framework or verification tools.
- Changed files or planned edit surface.
- User acceptance needs.

## Required context

Read local testing docs, package scripts, CI notes, existing tests, and relevant feature behavior only when needed. Mark unknown test infrastructure honestly.

## Process

1. Identify behavior to prove.
2. Choose test levels: unit, integration, end-to-end, manual, browser, visual, accessibility, or release checks.
3. Define regression paths for existing behavior.
4. Specify commands, manual steps, screenshots, logs, or artifact evidence.
5. Define acceptable not-run reasons.
6. Link evidence requirements back to acceptance criteria.

## Output

A test plan with required checks, optional checks, not-run handling, and evidence format.

## Quality bar

The plan must show how the task will be proven, not only which command might run.

## User confirmation points

Ask before using production data, external services, payment flows, real messages, destructive operations, or long-running tests.

## No-code boundary

This skill designs verification. It does not run tests.

## Common mistakes

- Treating a build pass as full acceptance.
- Omitting manual verification for UI behavior.
- Hiding skipped tests.
- Testing only the new behavior and not regressions.

## Example

For a checkout UI change, Atlas requires component/unit checks, browser happy path, error path, screenshot evidence, and a not-run note for payment sandbox checks.
