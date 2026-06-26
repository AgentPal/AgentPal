# Risk Severity Classification Skill

## Purpose

Classify quality, release, evidence, privacy, regression, and delivery risks so the user can decide what to accept, fix, or block.

## When to use

Use in quality reviews, completion audits, release gates, regression plans, high-risk operations, and cross-Pal reviews.

## Inputs

Risk description, affected users/files/data, evidence strength, reversibility, privacy/security exposure, release impact, and not-run items.

## Required context

Read `risk-severity-knowledge.md`, Rhea safety findings when relevant, and the target acceptance criteria.

## Process

1. Identify risk category.
2. Determine impact, likelihood, reversibility, and evidence quality.
3. Classify severity as low, medium, high, critical, or blocked.
4. State whether user confirmation is required.
5. Define mitigation or next owner.
6. Record residual risk after mitigation.

## Output

Risk table with severity, reason, impact, evidence, required action, confirmation need, and residual risk.

## Quality bar

Severity must be explainable and proportional. Missing evidence should increase uncertainty, not fabricate failure.

## User confirmation points

Required for high, critical, blocked, irreversible, external, destructive, privacy-sensitive, or production-affecting decisions.

## No-code boundary

Quinn classifies risk and asks for evidence. Quinn does not approve risky execution.

## Common mistakes

- Calling unknown risk low.
- Treating all missing tests as high risk.
- Failing to separate severity from likelihood.
- Approving user-risk on behalf of the user.

## Example

No tests run for a small docs typo is medium or low depending on scope; no tests run for release packaging is high or blocked.
