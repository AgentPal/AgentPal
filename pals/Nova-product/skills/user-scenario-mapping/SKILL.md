---
name: user-scenario-mapping
description: Use this skill when you need to Map who will use the product, when they need it, what they are trying to accomplish, and what must be true for them to switch.
---

# user-scenario-mapping

## Purpose

Map who will use the product, when they need it, what they are trying to accomplish, and what must be true for them to switch.

## When to use

- "Many people will use this."
- User group is too broad.
- Need to choose a first user segment.
- Need a scenario for PRD or handoff.

## Inputs

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

## Outputs

Produce the structured output documented in README.md, but return it as a clean runtime-ready artifact instead of a copied template block.

## Boundaries

Not a fit:
- Internal implementation details with no user-facing decision.
- Tasks where the target user is already fixed and documented.

Risk boundary:
Do not claim market size or universal demand without evidence.

Do not treat a vague idea as a build-ready spec. Keep scope, acceptance, and non-scope explicit.

## Evidence and handoff requirements

Require scope, non-scope, assumptions, acceptance evidence, and the exact handoff artifact expected from the next Runtime or Pal.

Reference acceptance hints:
The first user and first scenario are specific enough to drive scope decisions.

## Related files

- Runtime entry: skills/user-scenario-mapping/SKILL.md
- Human notes: skills/user-scenario-mapping/README.md
- Parent index: skills/index.md

Uses `knowledge/users/user-scenario.md`; feeds `mvp-slicing` and `prd-writer`.

