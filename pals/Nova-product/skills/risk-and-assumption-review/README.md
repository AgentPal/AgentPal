# risk-and-assumption-review

运行时 Skill 入口请看 SKILL.md；README.md 仅作为人类阅读说明。


中文名：风险与假设审查

## Purpose

Identify unvalidated assumptions, product risks, privacy/compliance issues, overbuild signals, technical uncertainty, and evidence gaps before development or release.

## Good Fit

- User wants to start development.
- Product involves privacy, payment, public release, automation, or high development cost.
- Scope feels too large.

## Poor Fit

- Purely low-risk wording cleanup.
- User demands final regulated professional advice.

## Input Information

- Product scope.
- Target users.
- Data handled.
- Business model if any.
- Runtime/execution plan.
- Known evidence.

## Process

1. List critical assumptions.
2. Rate product, user, technical, execution, business, privacy, compliance, maintenance, and scope risks.
3. Identify must-verify items.
4. Recommend mitigation or narrower first step.

## Output Format

```text
# Risk and Assumption Review
| Item | Type | Risk | Evidence Needed | Mitigation |
|---|---|---|---|---|

## Blocking Risks
## Can Proceed With Caution
## Revisit Later
```

## Acceptance Standard

The review clearly separates blockers from manageable risks and states what evidence is needed.

## Risk Boundary

Do not provide final legal, medical, tax, financial, or compliance conclusions.

## Related Skills / Runbooks

Uses `knowledge/risks/assumption-and-risk.md`; pairs with `mvp-slicing` and `developer-handoff`.

