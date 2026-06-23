# acceptance-criteria-writer

运行时 Skill 入口请看 SKILL.md；README.md 仅作为人类阅读说明。


中文名：验收标准编写

## Purpose

Create testable, observable acceptance criteria for product requirements, user stories, handoffs, and runtime tasks.

## Good Fit

- PRD is ready but completion conditions are vague.
- suitable implementation collaborator needs clear checks.
- User wants to know how to verify completion.

## Poor Fit

- Requirements are not defined.
- The task asks for subjective success without observable signals.

## Input Information

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

## Output Format

```text
# Acceptance Criteria
## Story / Requirement
## Criteria
- Given ...
- When ...
- Then ...
## Edge Cases
## Evidence Required
```

## Acceptance Standard

A reviewer can decide pass/fail without guessing Nova's intent.

## Risk Boundary

Do not define acceptance in terms of "looks good" or "works normally" without observable detail.

## Related Skills / Runbooks

Uses `knowledge/requirements/acceptance-criteria.md`; feeds `developer-handoff`.

