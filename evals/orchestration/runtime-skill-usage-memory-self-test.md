# Runtime Skill Usage Memory Self-Test

## Goal

Verify that Runtime Skill Usage Memory is recorded and reused without confusing host Runtime Skills with Pal-owned Skills.

## Input

```text
Last time Claude Code's document Skill worked well. Can we use that experience again?
```

## Expected Behavior

- Identifies previous record as Runtime Skill Usage Memory.
- Places the document Skill under `runtime_skill_candidates`.
- Places Pal methods under `pal_owned_skills_used`.
- Requires current Runtime evidence before use.
- Records `availability_confirmed`, `success`, `verification_result`, and `fallback_used`.
- Includes `not_a_fixed_route: true`.
- Produces a Runtime Skill-aware Task Package or references the template.

## Failure Behavior

- Says a Pal owns or executes the host Skill.
- Assumes the Skill is currently installed because it worked once.
- Omits availability, fallback, verification result, or privacy notes.
- Treats the memory record as a fixed route.

## Pass / Fail

Pass when Runtime Skill usage remains a host Runtime candidate and Pal-owned Skill separation is preserved.
