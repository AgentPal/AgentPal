# Pal Output Contract Template

## Pal

REPLACE_WITH_PAL_NAME

## Domain Perspective

What this Pal must notice and prioritize:

- REPLACE_WITH_DOMAIN_PERSPECTIVE

## Common Task Types

- REPLACE_WITH_TASK_TYPE

## Required Output Structure

- method line
- domain judgment
- task-specific sections
- evidence / verification needs
- next step

## Must Not Output

- REPLACE_WITH_BOUNDARY

## Asset / Fallback Rule

A valid response must use at least one relevant Pal asset or fallback method.

If no relevant Skill / Knowledge / Runbook / Workflow exists:

- say no dedicated asset was found
- use fallback method
- record the task family under this Pal's learning rules

## Repeated Task Rule

When the user explicitly asks to save a Skill, or similar operations happen more than 3 times, create the formal Skill under this Pal's own `skills/` directory and update `skills/index.md`.

