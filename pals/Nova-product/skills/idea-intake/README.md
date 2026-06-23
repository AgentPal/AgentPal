# idea-intake

运行时 Skill 入口请看 SKILL.md；README.md 仅作为人类阅读说明。


中文名：想法接入

## Purpose

Classify an incoming user idea, feature request, product direction, project, automation request, Pal/Agent request, or development request before Nova chooses the next Skill.

## Good Fit

- "I have an idea."
- "I want to build a tool/product/Pal."
- "Can we add this feature?"
- "Give this to development" when the request is still fuzzy.

## Poor Fit

- The user already provides a complete PRD with acceptance criteria.
- The user only asks for direct code execution.
- The request requires final legal, medical, tax, financial, or compliance judgment.

## Input Information

- Raw user request.
- Intended output if known.
- Target users if known.
- Constraints, deadline, and risk notes if known.

## Process

1. Classify the request as idea, problem, feature, product, project, automation, Pal/Agent need, or development task.
2. Judge maturity: inspiration, goal without boundary, function without user, requirement without version, or ready for development.
3. Identify missing product definition.
4. Select the next Skill or handoff path.

## Output Format

```text
## My Judgment
Type:
Maturity:

## Missing Product Definition
- [missing item]

## Recommended Next Step
Skill / runbook:
Reason:
```

## Acceptance Standard

The output clearly states what kind of request this is, what is missing, and what Nova should do next.

## Risk Boundary

Do not convert a vague idea into a development task. Do not promise commercial success.

## Related Skills / Runbooks

Feeds `problem-definition`, `scope-and-boundary`, `mvp-slicing`, and `runbooks/product/idea-to-prd.md`.

