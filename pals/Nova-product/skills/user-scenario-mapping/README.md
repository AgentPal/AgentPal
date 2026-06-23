# user-scenario-mapping

运行时 Skill 入口请看 SKILL.md；README.md 仅作为人类阅读说明。


中文名：用户场景整理

## Purpose

Map who will use the product, when they need it, what they are trying to accomplish, and what must be true for them to switch.

## Good Fit

- "Many people will use this."
- User group is too broad.
- Need to choose a first user segment.
- Need a scenario for PRD or handoff.

## Poor Fit

- Internal implementation details with no user-facing decision.
- Tasks where the target user is already fixed and documented.

## Input Information

- Candidate user groups.
- Trigger moments.
- Current tools or workarounds.
- User ability level.
- Frequency and urgency.

## Process

1. Split primary and secondary users.
2. Define the first-use scenario.
3. Identify trigger, goal, current alternative, and switching reason.
4. Note constraints and user capability.
5. Recommend first target scenario.

## Output Format

```text
# User Scenario Map
## Primary User
## Secondary Users
## Trigger Moment
## Current Alternative
## First Scenario
## Switching Reason
## Scenario Not Covered Yet
```

## Acceptance Standard

The first user and first scenario are specific enough to drive scope decisions.

## Risk Boundary

Do not claim market size or universal demand without evidence.

## Related Skills / Runbooks

Uses `knowledge/users/user-scenario.md`; feeds `mvp-slicing` and `prd-writer`.

