# Example: Idea to PRD

## User Request

"I want to make an AI tool that organizes my scattered project ideas."

## Nova Judgment

This is a product direction, not a development task. The first missing pieces are target user, first scenario, and what "organized" means.

## Execution Strategy

Use `idea-intake`, `problem-definition`, `user-scenario-mapping`, `scope-and-boundary`, `prd-writer`, and `acceptance-criteria-writer`.

## Task Package

- Target user: solo builder with many unfinished ideas.
- Core problem: ideas are scattered, hard to compare, and rarely become next actions.
- V1: import/paste ideas, cluster by product direction, mark next action, export summary.
- Not V1: team workspace, marketplace, automatic execution, complex roadmap board.

## Acceptance Criteria

- User can paste at least 10 idea notes.
- Nova can group them into themes and identify duplicates.
- Each theme has problem, target user, and next action.
- Export includes assumptions and non-scope.

## Model / Reasoning

Recommended model: GPT-5.4-Codex or equivalent strong reasoning model. Reasoning strength: medium.

## Evidence Required

If handed to development, require affected paths, test result, generated artifact path, and unresolved risks. Nova does not execute commands.

