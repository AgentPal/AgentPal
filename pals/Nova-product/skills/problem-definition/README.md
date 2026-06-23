# problem-definition

运行时 Skill 入口请看 SKILL.md；README.md 仅作为人类阅读说明。


中文名：问题定义

## Purpose

Turn "I want a feature" into a clear problem statement that explains who has the problem, when it happens, what they do now, and why it is worth solving.

## Good Fit

- Feature lists without a core problem.
- Product ideas that start from solution fantasy.
- Development requests without user value.

## Poor Fit

- Pure implementation bugs.
- Already validated requirements with clear problem statements.
- High-risk professional advice.

## Input Information

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

## Output Format

```text
# Problem Definition
## Target User
## Current Scenario
## Current Alternative
## Pain / Cost
## Problem Statement
## Worth Proceeding?
```

## Acceptance Standard

The problem can be understood without reading the original messy idea, and it avoids solution bias.

## Risk Boundary

If user, scenario, or pain is unknown, ask 1-3 questions instead of inventing them.

## Related Skills / Runbooks

Follows `idea-intake`; feeds `user-scenario-mapping`, `scope-and-boundary`, and `prd-writer`.

