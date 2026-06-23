---
name: decision-log-writer
description: Use this skill when you need to Record product decisions, alternatives, rationale, assumptions, tradeoffs, and follow-up review points.
---

# decision-log-writer

## Purpose

Record product decisions, alternatives, rationale, assumptions, tradeoffs, and follow-up review points.

## When to use

- User chooses a direction.
- Scope changes.
- Feature is cut or moved later.
- Business or product assumption is accepted for now.

## Inputs

- Decision.
- Options considered.
- Reasoning.
- Evidence or lack of evidence.
- Owner and date.
- Review trigger.

## Process

1. Restate the decision.
2. List options and rationale.
3. Capture assumptions and risks.
4. Define review trigger and evidence to revisit.
5. Keep sensitive details out unless approved.

## Outputs

Produce the structured output documented in README.md, but return it as a clean runtime-ready artifact instead of a copied template block.

## Boundaries

Not a fit:
- No decision has been made.
- The user wants private business strategy stored without approval.

Risk boundary:
Do not create real private memory without authorization.

Do not treat a vague idea as a build-ready spec. Keep scope, acceptance, and non-scope explicit.

## Evidence and handoff requirements

Require scope, non-scope, assumptions, acceptance evidence, and the exact handoff artifact expected from the next Runtime or Pal.

Reference acceptance hints:
Future readers understand what was decided, why, and when to revisit it.

## Related files

- Runtime entry: skills/decision-log-writer/SKILL.md
- Human notes: skills/decision-log-writer/README.md
- Parent index: skills/index.md

Uses `knowledge/decision/decision-record.md`; complements all scope and PRD work.

