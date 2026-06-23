# decision-log-writer

运行时 Skill 入口请看 SKILL.md；README.md 仅作为人类阅读说明。


中文名：决策记录

## Purpose

Record product decisions, alternatives, rationale, assumptions, tradeoffs, and follow-up review points.

## Good Fit

- User chooses a direction.
- Scope changes.
- Feature is cut or moved later.
- Business or product assumption is accepted for now.

## Poor Fit

- No decision has been made.
- The user wants private business strategy stored without approval.

## Input Information

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

## Output Format

```text
# Product Decision Record
## Decision
## Context
## Options Considered
## Rationale
## Assumptions
## Risks
## Review Trigger
```

## Acceptance Standard

Future readers understand what was decided, why, and when to revisit it.

## Risk Boundary

Do not create real private memory without authorization.

## Related Skills / Runbooks

Uses `knowledge/decision/decision-record.md`; complements all scope and PRD work.

