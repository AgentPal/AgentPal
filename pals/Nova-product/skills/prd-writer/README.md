# prd-writer

运行时 Skill 入口请看 SKILL.md；README.md 仅作为人类阅读说明。


中文名：PRD 编写

## Purpose

Turn a defined product direction into a structured Product Requirements Document that can be reviewed, accepted, and handed off.

## Good Fit

- Problem, user, scenario, and scope are mostly known.
- User needs a PRD for suitable implementation collaborator or execution runtime.
- Product decisions need a stable artifact.

## Poor Fit

- The idea has no target user or scope.
- User wants instant development without product definition.
- High-risk decisions need specialist review first.

## Input Information

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

## Output Format

```text
# PRD
## Background
## Goal
## Target Users
## Scenarios
## Core Problem
## Solution
## Scope
## Not Doing
## User Flow
## Requirements
## Non-Functional Requirements
## Risks / Assumptions
## Acceptance Criteria
## Later Versions
```

## Acceptance Standard

The PRD is specific enough for review and contains explicit non-scope and acceptance criteria.

## Risk Boundary

Do not fill missing facts with confident invention. Mark assumptions.

## Related Skills / Runbooks

Uses `knowledge/requirements/prd-structure.md`; feeds `developer-handoff`.

