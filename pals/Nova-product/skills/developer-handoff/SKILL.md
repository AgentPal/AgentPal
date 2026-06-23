---
name: developer-handoff
description: Use this skill when you need to Package product decisions into a clear handoff for suitable implementation collaborator, Codex, Claude Code, OpenHands, Gemini CLI, DeepSeek-TUI, or AgentPal runtime.
---

# developer-handoff

## Purpose

Package product decisions into a clear handoff for suitable implementation collaborator, Codex, Claude Code, OpenHands, Gemini CLI, DeepSeek-TUI, or AgentPal runtime.

## When to use

- PRD and acceptance criteria are ready.
- User wants development to begin.
- Need runtime/model/reasoning recommendations.

## Inputs

- PRD or scope summary.
- Required context.
- File or module scope if known.
- Non-scope.
- Acceptance criteria.
- Evidence requirements.
- Runtime constraints.

## Process

1. Confirm readiness for handoff.
2. Identify execution target and capability needs.
3. Build a Context Packet.
4. Specify scope, non-scope, risks, evidence, and model recommendation.
5. State that Nova does not execute the task.

## Outputs

Produce the structured output documented in README.md, but return it as a clean runtime-ready artifact instead of a copied template block.

## Boundaries

Not a fit:
- Requirement is still fuzzy.
- User wants Nova to directly execute implementation.
- Sensitive or high-risk action lacks approval.

Risk boundary:
Do not omit non-scope. Do not authorize commands, deletion, publishing, payment, or production writes.

Do not treat a vague idea as a build-ready spec. Keep scope, acceptance, and non-scope explicit.

## Evidence and handoff requirements

Require scope, non-scope, assumptions, acceptance evidence, and the exact handoff artifact expected from the next Runtime or Pal.

Reference acceptance hints:
The receiving developer Pal or runtime can execute without product guessing.

## Related files

- Runtime entry: skills/developer-handoff/SKILL.md
- Human notes: skills/developer-handoff/README.md
- Parent index: skills/index.md

Uses `knowledge/handoff/product-to-developer.md`; pairs with `runbooks/handoff/prd-to-developer-pal.md`.

