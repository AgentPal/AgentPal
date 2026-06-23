# Example: Decision Log

## User Request

"We decided not to add team accounts in V1. Record that."

## Nova Judgment

This is a product decision. It should be recorded because it affects scope and prevents later drift.

## Execution Strategy

Use `decision-log-writer`.

## Decision Record

```text
Decision: Team accounts are excluded from V1.
Context: V1 must validate whether solo users can turn messy ideas into useful product summaries.
Options: add teams now; defer teams; reject teams permanently.
Rationale: Team accounts add permissions, invitations, billing, and support burden before core value is proven.
Assumption: Solo workflow is enough for first validation.
Risk: Some collaboration-focused users will not fit V1.
Review trigger: revisit after 10 users request collaboration or after solo workflow is validated.
```

## Acceptance Criteria

- Decision has rationale, tradeoff, assumption, risk, and review trigger.
- PRD scope and non-scope are updated.

## Model / Reasoning

Recommended model: mid-tier or strong model. Reasoning strength: low to medium.

## Evidence Required

Updated decision record and any linked PRD/scope changes.

