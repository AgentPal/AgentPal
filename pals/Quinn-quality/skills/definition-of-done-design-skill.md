# Definition Of Done Design Skill

## Purpose

Design a Definition of Done that applies across a task, Pal upgrade, or release candidate and prevents premature completion claims.

## When to use

Use when a task has multiple artifacts, reviewers, or gates, or when a completion report needs a shared standard.

## Inputs

Task scope, deliverables, acceptance criteria, required checks, evidence paths, risk boundary, release intent, and not-run allowances.

## Required context

Read `definition-of-done-knowledge.md`, target task package, relevant output contract, and any release or no-code boundary requirements.

## Process

1. Define the finished state for the whole deliverable.
2. Include artifact, evidence, review, risk, and report requirements.
3. State what does not count as done.
4. Define acceptable not-run conditions and when they block completion.
5. Assign evidence owners.
6. Add final audit questions.

## Output

Definition of Done table with required condition, evidence, owner, pass rule, and blocker rule.

## Quality bar

The DoD must be stronger than file presence and must prevent partial work from being reported as complete.

## User confirmation points

Ask before relaxing a DoD for time, cost, release pressure, missing tools, or user-accepted risk.

## No-code boundary

DoD design does not create automation. It defines review standards for Runtime evidence.

## Common mistakes

- Confusing Definition of Done with a single story's acceptance criteria.
- Treating unverified checks as passed.
- Omitting rollback, privacy, or release evidence.
- Failing to record partial completion.

## Example

A Pal deepening DoD requires updated identity, complete skills/knowledge/workflows/runbooks/evals, registry consistency, no-code validation, JSON parse, key anchor search, and final report.
