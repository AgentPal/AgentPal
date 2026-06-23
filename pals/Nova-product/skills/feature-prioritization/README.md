# feature-prioritization

运行时 Skill 入口请看 SKILL.md；README.md 仅作为人类阅读说明。


中文名：功能优先级

## Purpose

Rank candidate features by user value, product stage, development cost, risk, dependencies, and AgentPal boundary impact.

## Good Fit

- Feature list is long.
- New ideas threaten current scope.
- User needs Now / Next / Later or V1 / later split.

## Poor Fit

- No problem or user scenario has been defined.
- Feature ranking is being used to justify a predetermined answer.

## Input Information

- Candidate features.
- Product goal.
- V1 target.
- User scenario.
- Cost, risk, and dependency notes.

## Process

1. Choose a lightweight prioritization method.
2. Score or qualitatively rank each feature.
3. Identify must-build, later, icebox, and reject.
4. Explain cuts in product terms.
5. Record assumptions.

## Output Format

```text
# Feature Priority
| Feature | User Value | Cost | Risk | Dependency | Recommendation |
|---|---|---|---|---|---|

## Must Build
## Later
## Icebox
## Reject / Not Now
```

## Acceptance Standard

The ranking explains why features move in or out of the current version.

## Risk Boundary

Do not let scoring obscure judgment. If the core scenario is unclear, return to `problem-definition`.

## Related Skills / Runbooks

Uses `knowledge/prioritization/priority-methods.md`; pairs with `runbooks/product/feature-priority-review.md`.

