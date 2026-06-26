# Acceptance Criteria Knowledge

## Concept Explanation

Acceptance criteria are task-specific conditions that define what a deliverable must satisfy before the user or reviewer can accept it. They reduce ambiguity by turning goals into observable outcomes.

## Judgement Standards

- Each criterion must be specific and testable.
- Criteria should include positive and negative conditions.
- Evidence must be named for each criterion.
- Criteria should cover user goal, boundaries, risks, and deliverable location.
- Criteria do not replace whole-task Definition of Done.

## Examples

- A Pal skill file must include required sections and no placeholder content.
- A release report must list tests run, not-run items, risks, and changed files.

## Counterexamples

- "Make it good."
- "Looks complete."
- "Use best practices" without evidence.

## Scope

Use for feature review, Pal asset upgrades, docs deliverables, release candidates, and cross-Pal task packages.

## How This Becomes Skill, Workflow, Or Eval

It supports `acceptance-criteria-design-skill.md`, `acceptance-criteria-workflow.md`, and `quinn-acceptance-criteria-eval.md`.

## Common Mistakes

- Combining many hidden assumptions into one criterion.
- Omitting forbidden outcomes.
- Not linking criteria to evidence.

## Source Refs Or Local Notes

Source: Atlassian acceptance criteria guide, accessed 2026-06-26. Local adaptation: criteria must include Runtime evidence because AgentPal is not an execution layer.
