---
name: problem-definition
description: Use this skill when you need to Turn "I want a feature" into a clear problem statement that explains who has the problem, when it happens, what they do now, and why it is worth solving.
---

# problem-definition

## Purpose

Turn "I want a feature" into a clear problem statement that explains who has the problem, when it happens, what they do now, and why it is worth solving.

## When to use

- Feature lists without a core problem.
- Product ideas that start from solution fantasy.
- Development requests without user value.

## Inputs

- Target user or suspected user.
- Current scenario.
- Current workaround.
- Pain, cost, frequency, urgency.
- Desired outcome.

## Process

1. Identify the target user.
2. Describe the current situation and trigger moment.
3. Separate user-stated feature from underlying need.
4. Write a problem statement.
5. Decide whether the problem is worth the next product step.

## Outputs

Produce the structured output documented in README.md, but return it as a clean runtime-ready artifact instead of a copied template block.

## Boundaries

Not a fit:
- Pure implementation bugs.
- Already validated requirements with clear problem statements.
- High-risk professional advice.

Risk boundary:
If user, scenario, or pain is unknown, ask 1-3 questions instead of inventing them.

Do not treat a vague idea as a build-ready spec. Keep scope, acceptance, and non-scope explicit.

## Evidence and handoff requirements

Require scope, non-scope, assumptions, acceptance evidence, and the exact handoff artifact expected from the next Runtime or Pal.

Reference acceptance hints:
The problem can be understood without reading the original messy idea, and it avoids solution bias.

## Related files

- Runtime entry: skills/problem-definition/SKILL.md
- Human notes: skills/problem-definition/README.md
- Parent index: skills/index.md

Follows `idea-intake`; feeds `user-scenario-mapping`, `scope-and-boundary`, and `prd-writer`.

