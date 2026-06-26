# Acceptance Criteria Workflow

## Trigger

A task, Pal upgrade, implementation request, or release candidate lacks clear acceptance criteria.

## Inputs

Goal, deliverable, users, constraints, non-goals, risks, expected artifacts, and available examples.

## Steps

1. Restate the goal in verifiable language.
2. List functional, evidence, boundary, privacy, release, and quality criteria.
3. Add negative criteria for forbidden outcomes.
4. Connect each criterion to required evidence.
5. Identify criteria that need user decision.
6. Produce a criteria table for the owner Pal or Runtime.

## Decision points

- Are criteria observable?
- Does any criterion depend on private policy or user preference?
- Which criteria block final acceptance?

## Outputs

Acceptance criteria table with pass/fail evidence and blocker status.

## Quality checks

No vague criteria. Each criterion must be reviewable or clearly marked as user decision.

## Required user confirmation

Required for acceptance tradeoffs, release risk, privacy-sensitive conditions, or waived criteria.

## Evidence to return

Criteria list, source goal, assumptions, user decisions, and required verification evidence.
