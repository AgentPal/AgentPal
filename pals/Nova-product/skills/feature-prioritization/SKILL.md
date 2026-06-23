---
name: feature-prioritization
description: Use this skill when you need to Rank candidate features by user value, product stage, development cost, risk, dependencies, and AgentPal boundary impact.
---

# feature-prioritization

## Purpose

Rank candidate features by user value, product stage, development cost, risk, dependencies, and AgentPal boundary impact.

## When to use

- Feature list is long.
- New ideas threaten current scope.
- User needs Now / Next / Later or V1 / later split.

## Inputs

- Candidate features.
- Product goal.
- V1 target.
- User scenario.
- Cost, risk, and dependency notes.

## Process

1. Choose a lightweight prioritization method.
2. Score or qualitatively rank each feature.
3. Identify must-build, later, icebox, and reject.
4. Explain cuts in product terms.
5. Record assumptions.

## Outputs

Produce the structured output documented in README.md, but return it as a clean runtime-ready artifact instead of a copied template block.

## Boundaries

Not a fit:
- No problem or user scenario has been defined.
- Feature ranking is being used to justify a predetermined answer.

Risk boundary:
Do not let scoring obscure judgment. If the core scenario is unclear, return to `problem-definition`.

Do not treat a vague idea as a build-ready spec. Keep scope, acceptance, and non-scope explicit.

## Evidence and handoff requirements

Require scope, non-scope, assumptions, acceptance evidence, and the exact handoff artifact expected from the next Runtime or Pal.

Reference acceptance hints:
The ranking explains why features move in or out of the current version.

## Related files

- Runtime entry: skills/feature-prioritization/SKILL.md
- Human notes: skills/feature-prioritization/README.md
- Parent index: skills/index.md

Uses `knowledge/prioritization/priority-methods.md`; pairs with `runbooks/product/feature-priority-review.md`.

