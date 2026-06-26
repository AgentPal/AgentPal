# Regression Gate Design Skill

## Purpose

Define the regression checks required before accepting changes that may affect existing behavior, assets, workflows, or release readiness.

## When to use

Use after code changes, Pal asset upgrades, documentation standard changes, registry updates, release candidate work, or bug fixes.

## Inputs

Affected files, changed behavior, dependencies, user-visible surfaces, known fragile areas, prior failures, risk severity, and available verification methods.

## Required context

Read `regression-testing-knowledge.md`, change scope evidence, and relevant workflow/runbook indexes.

## Process

1. Identify old behavior that must remain true.
2. Identify neighboring areas affected by the change.
3. Choose smoke, targeted, and broad regression checks.
4. Assign priority based on risk and reversibility.
5. Define evidence required for each check.
6. Mark checks that are not-run and their impact.

## Output

Regression gate matrix with area, risk, check, expected result, evidence, owner, and blocker rule.

## Quality bar

The gate must protect real existing behavior, not only the new feature.

## User confirmation points

Ask before broad test runs, external service checks, production data reads, or long-running verification.

## No-code boundary

Quinn designs the gate. Runtime executes approved checks and returns evidence.

## Common mistakes

- Checking only the new path.
- Ignoring changed shared files.
- Letting not-run core checks disappear.
- Treating all regressions as equal severity.

## Example

For a Pal registry update, regression gate includes JSON parse, direct-call consistency, contacts/registry id/path match, and no ordinary Skill added as contact.
