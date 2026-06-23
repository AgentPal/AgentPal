---
name: idea-intake
description: Use this skill when you need to Classify an incoming user idea, feature request, product direction, project, automation request, Pal/Agent request, or development request before Nova chooses the next Skill.
---

# idea-intake

## Purpose

Classify an incoming user idea, feature request, product direction, project, automation request, Pal/Agent request, or development request before Nova chooses the next Skill.

## When to use

- "I have an idea."
- "I want to build a tool/product/Pal."
- "Can we add this feature?"
- "Give this to development" when the request is still fuzzy.

## Inputs

- Raw user request.
- Intended output if known.
- Target users if known.
- Constraints, deadline, and risk notes if known.

## Process

1. Classify the request as idea, problem, feature, product, project, automation, Pal/Agent need, or development task.
2. Judge maturity: inspiration, goal without boundary, function without user, requirement without version, or ready for development.
3. Identify missing product definition.
4. Select the next Skill or handoff path.

## Outputs

Produce the structured output documented in README.md, but return it as a clean runtime-ready artifact instead of a copied template block.

## Boundaries

Not a fit:
- The user already provides a complete PRD with acceptance criteria.
- The user only asks for direct code execution.
- The request requires final legal, medical, tax, financial, or compliance judgment.

Risk boundary:
Do not convert a vague idea into a development task. Do not promise commercial success.

Do not treat a vague idea as a build-ready spec. Keep scope, acceptance, and non-scope explicit.

## Evidence and handoff requirements

Require scope, non-scope, assumptions, acceptance evidence, and the exact handoff artifact expected from the next Runtime or Pal.

Reference acceptance hints:
The output clearly states what kind of request this is, what is missing, and what Nova should do next.

## Related files

- Runtime entry: skills/idea-intake/SKILL.md
- Human notes: skills/idea-intake/README.md
- Parent index: skills/index.md

Feeds `problem-definition`, `scope-and-boundary`, `mvp-slicing`, and `runbooks/product/idea-to-prd.md`.

