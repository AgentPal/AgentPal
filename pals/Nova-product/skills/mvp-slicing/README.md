# mvp-slicing

运行时 Skill 入口请看 SKILL.md；README.md 仅作为人类阅读说明。


中文名：首版范围切片

## Purpose

Choose the right first release shape: validation version, lightweight complete working version, complete platform version, or long-term productized version.

## Good Fit

- User asks how much to build first.
- Product is valuable but too broad.
- Need to avoid a broken demo and also avoid premature platformization.

## Poor Fit

- Fully constrained client delivery with fixed scope.
- Pure research or copywriting work.

## Input Information

- Product goal.
- User scenario.
- Candidate features.
- Development budget.
- Validation needs.
- Risk tolerance.

## Process

1. Compare version paths.
2. Identify the smallest complete user loop.
3. Cut anything that does not prove the core value.
4. State the recommended V1 and why.
5. Define V1 acceptance evidence.

## Output Format

```text
# Version Path
## Option A: Validation Version
## Option B: Lightweight Complete Working Version
## Option C: Complete Platform Version
## Nova Recommendation
## V1 Slice
## Not in V1
```

## Acceptance Standard

The recommended V1 is small enough to build and complete enough to validate user value.

## Risk Boundary

Do not call an unusable fragment an MVP. Do not recommend a platform when the core scenario is unproven.

## Related Skills / Runbooks

Uses `knowledge/scope/mvp-and-v1.md`; pairs with `runbooks/product/mvp-scope-cut.md`.

