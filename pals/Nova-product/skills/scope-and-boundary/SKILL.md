---
name: scope-and-boundary
description: Use this skill when you need to Define what version one includes, what it excludes, what is deferred, and what would make the product overbuilt.
---

# scope-and-boundary

## Purpose

Define what version one includes, what it excludes, what is deferred, and what would make the product overbuilt.

## When to use

- Feature list keeps growing.
- User wants a complete platform immediately.
- Development handoff needs boundaries.

## Inputs

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

## Outputs

Produce the structured output documented in README.md, but return it as a clean runtime-ready artifact instead of a copied template block.

## Boundaries

Not a fit:
- Tiny copy edits or simple documentation changes.
- Cases where scope is contractually fixed and Nova is not authorized to revise it.

Risk boundary:
Do not hide unresolved risk inside vague "future optimization" language.

Do not treat a vague idea as a build-ready spec. Keep scope, acceptance, and non-scope explicit.

## Evidence and handoff requirements

Require scope, non-scope, assumptions, acceptance evidence, and the exact handoff artifact expected from the next Runtime or Pal.

Reference acceptance hints:
A developer or product reviewer can tell what not to build.

## Related files

- Runtime entry: skills/scope-and-boundary/SKILL.md
- Human notes: skills/scope-and-boundary/README.md
- Parent index: skills/index.md

Feeds `mvp-slicing`, `feature-prioritization`, and `runbooks/product/mvp-scope-cut.md`.

