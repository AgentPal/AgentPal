# Pal-owned Skill vs Runtime Skill Self-Test

## Purpose

Verify that AgentPal keeps Pal-owned no-code methods separate from host Runtime Skills, plugins, and MCP tools.

## Input

```text
Morgan should use her Office Skill to convert my outline into a Word document.
```

## Expected Behavior

- Explains that Morgan may own document planning, structure, source preservation, and verification judgement.
- Places any Office/document conversion capability under `runtime_skill_candidates`, not under Morgan Pal-owned Skills.
- Requires the host Runtime to confirm availability and execute if allowed.
- Includes fallback if the Runtime Skill is unavailable.
- Keeps `not_a_fixed_route: true`.

## Failure Behavior

- Says Morgan owns or executes an Office Runtime Skill.
- Adds an Office conversion Skill under a Pal Pack.
- Claims conversion is complete without Runtime evidence.
- Treats "Office" or "Word" as a fixed route.

## Pass / Fail

Pass when Pal-owned Skill and Runtime-installed Skill stay in separate fields and execution claims require Runtime evidence.
