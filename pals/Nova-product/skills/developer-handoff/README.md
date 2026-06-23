# developer-handoff

运行时 Skill 入口请看 SKILL.md；README.md 仅作为人类阅读说明。


中文名：开发交接

## Purpose

Package product decisions into a clear handoff for suitable implementation collaborator, Codex, Claude Code, OpenHands, Gemini CLI, DeepSeek-TUI, or AgentPal runtime.

## Good Fit

- PRD and acceptance criteria are ready.
- User wants development to begin.
- Need runtime/model/reasoning recommendations.

## Poor Fit

- Requirement is still fuzzy.
- User wants Nova to directly execute implementation.
- Sensitive or high-risk action lacks approval.

## Input Information

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

## Output Format

```text
# Developer Handoff
## Goal
## Context
## Scope
## Not Doing
## Recommended Runtime / Model / Reasoning
## Tasks
## Acceptance Criteria
## Evidence Required
## Risks
```

## Acceptance Standard

The receiving developer Pal or runtime can execute without product guessing.

## Risk Boundary

Do not omit non-scope. Do not authorize commands, deletion, publishing, payment, or production writes.

## Related Skills / Runbooks

Uses `knowledge/handoff/product-to-developer.md`; pairs with `runbooks/handoff/prd-to-developer-pal.md`.

