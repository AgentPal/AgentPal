# Project Conductor Task Map Self-Test

## Purpose

Verify that project-level goals produce a bounded no-code task map.

## Input

```text
Mira, organize this project into phases, tasks, owners, runtime candidates, verification, and the next task package.
```

## Pass Criteria

- Output includes project goal, state summary, constraints, phases, tasks, priorities, risk levels, owner Pal candidates, Runtime candidates, Runtime Skill candidates, verification needs, context budget, next-round candidates, blocked items, user decisions, and Routing Memory candidates.
- Owner Pal candidates are not fixed routes.
- Runtime candidates are execution-layer candidates, not Pal-layer owners.
- Runtime Skill candidates are host Runtime capabilities.
- Pal-owned Skills are Pal methods or workflows.
- Context budget includes `cannot_read`.
- No-code boundary is explicit.
- No internal path or private project data appears.

## Fail Criteria

- The task map starts executing tasks automatically.
- A task says development must go to Atlas, research must go to Vega, or verification must go to Quinn by rule.
- Routing Memory becomes a database or route map.
