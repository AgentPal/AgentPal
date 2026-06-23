---
name: mvp-slicing
description: Use this skill when you need to Choose the right first release shape: validation version, lightweight complete working version, complete platform version, or long-term productized version.
---

# mvp-slicing

## Purpose

Choose the right first release shape: validation version, lightweight complete working version, complete platform version, or long-term productized version.

## When to use

- User asks how much to build first.
- Product is valuable but too broad.
- Need to avoid a broken demo and also avoid premature platformization.

## Inputs

- Product goal.
- User scenario.
- Candidate features.
- Development budget.
- Validation needs.
- Risk tolerance.

## Process

1. Compare version paths.
2. Identify the smallest complete user loop.
3. Cut anything that does not prove the core value.
4. State the recommended V1 and why.
5. Define V1 acceptance evidence.

## Outputs

Produce the structured output documented in README.md, but return it as a clean runtime-ready artifact instead of a copied template block.

## Boundaries

Not a fit:
- Fully constrained client delivery with fixed scope.
- Pure research or copywriting work.

Risk boundary:
Do not call an unusable fragment an MVP. Do not recommend a platform when the core scenario is unproven.

Do not treat a vague idea as a build-ready spec. Keep scope, acceptance, and non-scope explicit.

## Evidence and handoff requirements

Require scope, non-scope, assumptions, acceptance evidence, and the exact handoff artifact expected from the next Runtime or Pal.

Reference acceptance hints:
The recommended V1 is small enough to build and complete enough to validate user value.

## Related files

- Runtime entry: skills/mvp-slicing/SKILL.md
- Human notes: skills/mvp-slicing/README.md
- Parent index: skills/index.md

Uses `knowledge/scope/mvp-and-v1.md`; pairs with `runbooks/product/mvp-scope-cut.md`.

