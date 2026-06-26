# Regression Debugging Skill

## Purpose

Help Atlas turn regressions and failed checks into minimal, evidence-driven repair tasks.

## When to use

Use when a previous behavior breaks, a test fails after a change, a user reports "it used to work", or a release check exposes a regression.

## Inputs

- Regression symptom.
- Previous expected behavior.
- Recent changes or suspected files.
- Reproduction steps.
- Failing tests, logs, screenshots, or user evidence.
- Allowed repair scope.

## Required context

Read the failing output, recent diff when available, relevant tests, and the smallest code path needed to reason about the regression.

## Process

1. Restate the old behavior and broken behavior.
2. Identify likely change window and impacted files.
3. Propose one to three testable hypotheses.
4. Prepare a minimal investigation and fix task.
5. Require regression tests or manual proof that the old behavior is restored.
6. Block unrelated refactor unless separately approved.

## Output

A regression task package with hypotheses, file scope, minimal fix guidance, and regression evidence requirements.

## Quality bar

The task must bias toward restoring behavior with the smallest safe change and a prevention check.

## User confirmation points

Ask before rollback, broad revert, data migration, dependency downgrade, or touching release artifacts.

## No-code boundary

Atlas diagnoses and packages. Runtime performs investigation and changes.

## Common mistakes

- Guessing a root cause without reproduction evidence.
- Fixing multiple unrelated issues in one regression task.
- Not adding a prevention check.
- Accepting "works now" without showing the old path.

## Example

A filter stopped preserving sort order after a UI change. Atlas asks runtime to compare the recent diff, add a sort-preservation regression check, and avoid rewriting the whole list component.
