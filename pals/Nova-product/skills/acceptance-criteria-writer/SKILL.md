---
name: acceptance-criteria-writer
description: Use this skill when you need to Create testable, observable acceptance criteria for product requirements, user stories, handoffs, and runtime tasks.
---

# acceptance-criteria-writer

## Purpose

Create testable, observable acceptance criteria for product requirements, user stories, handoffs, and runtime tasks.

## When to use

- PRD is ready but completion conditions are vague.
- suitable implementation collaborator needs clear checks.
- User wants to know how to verify completion.

## Inputs

- Feature or story.
- User scenario.
- Expected behavior.
- Edge cases.
- Non-scope.
- Evidence requirements.

## Process

1. Convert each requirement into observable outcomes.
2. Add normal, edge, error, and non-scope cases.
3. Include evidence requirements: tests, screenshots, logs, artifacts, or review notes.
4. Ensure criteria are not implementation guesses unless explicitly needed.

## Outputs

Produce the structured output documented in README.md, but return it as a clean runtime-ready artifact instead of a copied template block.

## Boundaries

Not a fit:
- Requirements are not defined.
- The task asks for subjective success without observable signals.

Risk boundary:
Do not define acceptance in terms of "looks good" or "works normally" without observable detail.

Do not treat a vague idea as a build-ready spec. Keep scope, acceptance, and non-scope explicit.

## Evidence and handoff requirements

Require scope, non-scope, assumptions, acceptance evidence, and the exact handoff artifact expected from the next Runtime or Pal.

Reference acceptance hints:
A reviewer can decide pass/fail without guessing Nova's intent.

## Related files

- Runtime entry: skills/acceptance-criteria-writer/SKILL.md
- Human notes: skills/acceptance-criteria-writer/README.md
- Parent index: skills/index.md

Uses `knowledge/requirements/acceptance-criteria.md`; feeds `developer-handoff`.

