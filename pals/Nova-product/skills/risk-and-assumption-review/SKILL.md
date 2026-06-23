---
name: risk-and-assumption-review
description: Use this skill when you need to Identify unvalidated assumptions, product risks, privacy/compliance issues, overbuild signals, technical uncertainty, and evidence gaps before development or release.
---

# risk-and-assumption-review

## Purpose

Identify unvalidated assumptions, product risks, privacy/compliance issues, overbuild signals, technical uncertainty, and evidence gaps before development or release.

## When to use

- User wants to start development.
- Product involves privacy, payment, public release, automation, or high development cost.
- Scope feels too large.

## Inputs

- Product scope.
- Target users.
- Data handled.
- Business model if any.
- Runtime/execution plan.
- Known evidence.

## Process

1. List critical assumptions.
2. Rate product, user, technical, execution, business, privacy, compliance, maintenance, and scope risks.
3. Identify must-verify items.
4. Recommend mitigation or narrower first step.

## Outputs

Produce the structured output documented in README.md, but return it as a clean runtime-ready artifact instead of a copied template block.

## Boundaries

Not a fit:
- Purely low-risk wording cleanup.
- User demands final regulated professional advice.

Risk boundary:
Do not provide final legal, medical, tax, financial, or compliance conclusions.

Do not treat a vague idea as a build-ready spec. Keep scope, acceptance, and non-scope explicit.

## Evidence and handoff requirements

Require scope, non-scope, assumptions, acceptance evidence, and the exact handoff artifact expected from the next Runtime or Pal.

Reference acceptance hints:
The review clearly separates blockers from manageable risks and states what evidence is needed.

## Related files

- Runtime entry: skills/risk-and-assumption-review/SKILL.md
- Human notes: skills/risk-and-assumption-review/README.md
- Parent index: skills/index.md

Uses `knowledge/risks/assumption-and-risk.md`; pairs with `mvp-slicing` and `developer-handoff`.

