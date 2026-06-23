---
name: product-feedback-synthesis
description: Use this skill when you need to Turn raw feedback, user comments, bug-like complaints, feature requests, and stakeholder opinions into themes, product signals, decisions, and next actions.
---

# product-feedback-synthesis

## Purpose

Turn raw feedback, user comments, bug-like complaints, feature requests, and stakeholder opinions into themes, product signals, decisions, and next actions.

## When to use

- Multiple feedback items conflict.
- User wants to know what feedback means for product direction.
- Need to update PRD, scope, or roadmap.

## Inputs

- Feedback items or summaries.
- Source type and recency.
- User segment.
- Product version.
- Current scope and goals.

## Process

1. Normalize feedback into themes.
2. Separate bugs, usability issues, feature requests, and strategic signals.
3. Check frequency, severity, and target-user fit.
4. Recommend product actions: fix, investigate, prioritize, icebox, reject.
5. Update decision or handoff artifacts when needed.

## Outputs

Produce the structured output documented in README.md, but return it as a clean runtime-ready artifact instead of a copied template block.

## Boundaries

Not a fit:
- Feedback contains private customer data that cannot be summarized safely.
- User asks for sentiment mining without source permission.

Risk boundary:
Do not store raw private feedback by default. Summarize and anonymize.

Do not treat a vague idea as a build-ready spec. Keep scope, acceptance, and non-scope explicit.

## Evidence and handoff requirements

Require scope, non-scope, assumptions, acceptance evidence, and the exact handoff artifact expected from the next Runtime or Pal.

Reference acceptance hints:
The output helps decide what to change, not just what users said.

## Related files

- Runtime entry: skills/product-feedback-synthesis/SKILL.md
- Human notes: skills/product-feedback-synthesis/README.md
- Parent index: skills/index.md

Feeds `feature-prioritization`, `decision-log-writer`, and `prd-writer`.

