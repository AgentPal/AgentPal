# Memory Protocol

Public releases must not contain private memory.

## Allowed To Record

- Public reusable methods.
- De-identified task patterns.
- Long-term preferences explicitly approved by the user.
- Repeated task candidates.
- Knowledge gaps.

## Not Allowed To Record

- Secrets, tokens, accounts, or passwords.
- Full private conversations.
- Customer data.
- Sensitive project state.
- Long-term memory without user approval.

## Skill Trigger

When the user explicitly asks to save a Skill, or when a similar task appears more than three times:

1. Prefer creating a formal Skill under this Pal's `skills/` directory.
2. Update `skills/index.md`.
3. If information is incomplete or sensitive, record a candidate in `learning/` first.
