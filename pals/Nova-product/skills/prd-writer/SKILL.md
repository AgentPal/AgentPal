---
name: prd-writer
description: Use this skill when you need to Turn a defined product direction into a structured Product Requirements Document that can be reviewed, accepted, and handed off.
---

# prd-writer

## Purpose

Turn a defined product direction into a structured Product Requirements Document that can be reviewed, accepted, and handed off.

## When to use

- Problem, user, scenario, and scope are mostly known.
- User needs a PRD for suitable implementation collaborator or execution runtime.
- Product decisions need a stable artifact.

## Inputs

- Product goal.
- Problem definition.
- Target users and scenarios.
- Scope and non-scope.
- Functional and non-functional requirements.
- Risks and evidence requirements.

## Process

1. Confirm readiness for PRD.
2. Write background, goals, users, problem, solution, scope, flows, requirements, risks, and acceptance criteria.
3. Add AgentPal-specific checks: Pal, Skill, knowledge, runtime, memory, approval, and Core boundary.
4. Mark assumptions and open questions.

## Outputs

Produce the structured output documented in README.md, but return it as a clean runtime-ready artifact instead of a copied template block.

## Boundaries

Not a fit:
- The idea has no target user or scope.
- User wants instant development without product definition.
- High-risk decisions need specialist review first.

Risk boundary:
Do not fill missing facts with confident invention. Mark assumptions.

Do not treat a vague idea as a build-ready spec. Keep scope, acceptance, and non-scope explicit.

## Evidence and handoff requirements

Require scope, non-scope, assumptions, acceptance evidence, and the exact handoff artifact expected from the next Runtime or Pal.

Reference acceptance hints:
The PRD is specific enough for review and contains explicit non-scope and acceptance criteria.

## Related files

- Runtime entry: skills/prd-writer/SKILL.md
- Human notes: skills/prd-writer/README.md
- Parent index: skills/index.md

Uses `knowledge/requirements/prd-structure.md`; feeds `developer-handoff`.

