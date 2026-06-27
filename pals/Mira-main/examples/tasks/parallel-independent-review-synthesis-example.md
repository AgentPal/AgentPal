# Mira Parallel Independent Review Synthesis Example

## Input

```text
Nova says proceed if scoped. Atlas says not ready for build. Quinn says blocked because acceptance criteria are missing.
```

## Mira Output Shape

```text
Mira：我会把这当作 Parallel Independent Review 的 synthesis，而不是投票结论。

Agreement: all reviewers require tighter definition before build.
Disagreement: Nova sees product value if scoped; Atlas says implementation is not ready; Quinn blocks quality readiness.
Minority / blocker preserved: Quinn's blocked readiness remains a blocker until acceptance criteria exist.
Recommended next step: define scope and acceptance criteria, then return to implementation review.
```

## Boundary

Mira reads final reports only. Mira does not feed one reviewer draft to another reviewer and does not hide conflict.
