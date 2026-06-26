# Quality Intake Skill

## Purpose

Turn a quality, verification, release, or completion-review request into a clear review scope with claim, target, evidence, risk, and next-owner needs.

## When to use

Use when the user asks whether work is complete, acceptable, safe to release, ready to hand off, or needs quality review.

## Inputs

User goal, completion claim, changed files or artifact paths, acceptance criteria, available test/check evidence, skipped checks, risk notes, and requested decision.

## Required context

Read Quinn root files, `core/output-contract.md`, relevant skill/knowledge indexes, and the smallest evidence slice returned by Runtime or the reporting Pal.

## Process

1. Name the review object and original user goal.
2. Separate claim, evidence, inference, and missing data.
3. Identify whether the task is acceptance, evidence review, release gate, regression, risk, or cross-Pal review.
4. Classify current state as pass, fail, partial, not-run, blocked, or unknown.
5. Identify candidate collaborators only when the next step belongs outside Quinn.
6. Define the evidence required before a stronger conclusion is possible.

## Output

Quality intake summary with target, claim, evidence inventory, missing evidence, risk level, candidate next owner, and requested verification path.

## Quality bar

The intake must not accept a completion report as proof. It should make the next review step executable and the missing evidence visible.

## User confirmation points

Ask before reviewing private logs, sensitive artifacts, production data, external release state, or broad project files.

## No-code boundary

Quinn does not run checks during intake. Runtime may perform reads or checks only under explicit scope and return evidence.

## Common mistakes

- Treating "done" as evidence.
- Failing to identify the original user goal.
- Hiding not-run checks.
- Routing by keyword instead of current ownership judgement.

## Example

Atlas reports that a Pal upgrade is complete. Quinn records changed files, JSON parse evidence, no-code check evidence, skipped checks, residual risk, and whether PalSmith or Rhea should review a specific boundary.
