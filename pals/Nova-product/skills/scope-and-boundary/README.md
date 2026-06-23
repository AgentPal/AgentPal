# scope-and-boundary

运行时 Skill 入口请看 SKILL.md；README.md 仅作为人类阅读说明。


中文名：范围与边界定义

## Purpose

Define what version one includes, what it excludes, what is deferred, and what would make the product overbuilt.

## Good Fit

- Feature list keeps growing.
- User wants a complete platform immediately.
- Development handoff needs boundaries.

## Poor Fit

- Tiny copy edits or simple documentation changes.
- Cases where scope is contractually fixed and Nova is not authorized to revise it.

## Input Information

- Problem statement.
- User scenario.
- Candidate features.
- Constraints, timeline, and delivery target.
- Known risks.

## Process

1. Restate the core product goal.
2. Separate must-have, can-wait, explicit non-scope, and icebox.
3. Check overbuild signals.
4. Record dependencies and evidence needs.
5. Confirm whether the scope is ready for PRD.

## Output Format

```text
# Scope and Boundary
## Core Goal
## V1 Must Include
## V1 Can Wait
## Explicitly Not Doing
## Icebox
## Dependencies
## Risks
```

## Acceptance Standard

A developer or product reviewer can tell what not to build.

## Risk Boundary

Do not hide unresolved risk inside vague "future optimization" language.

## Related Skills / Runbooks

Feeds `mvp-slicing`, `feature-prioritization`, and `runbooks/product/mvp-scope-cut.md`.

