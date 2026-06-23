# Official Pal No-Hardcode Routing Self-Test

## Purpose

Verify that official specialist Pal Packs describe collaborator capabilities without creating fixed semantic routes.

## Pals Under Test

- Atlas
- Nova
- Quinn
- Rhea
- Vega
- Morgan
- Harper


## Files To Sample

For each Pal:

- `PAL.md`
- `AGENTS.md`
- `SKILL.md`
- `capabilities/task-routing-matrix.md` or equivalent capability reference
- `core/dispatch-protocol.md`
- `skills/follow-up-planner/`

## Pass Criteria

- Each Pal has a collaboration boundary that forbids hard-coded semantic task routing.
- Collaborators are described as candidates or perspectives.
- Capability matrices are references, not route maps.
 dispatch is a candidate collaborator matrix, not a dispatch table.
- Examples with named Pal collaboration are marked non-binding.
- No Pal claims that a task/domain must consult, delegate, hand off, or spawn a specific Pal.

## Fail Signs

- `Task Type -> Preferred Pal`.
- `must consult Atlas/Nova/Quinn/Rhea`.
- `交给 Harper/Nova/Atlas/...` without explicit user command or non-binding example framing.
- Any Pal adds Skills, tools, models, plugins, MCP servers, or non-Pal runtimes to Pal contacts.

## Expected Result

A 类硬编码语义路由 should be `0`.


