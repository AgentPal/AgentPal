# Pal Skill Design Skill

## Purpose

Design practical Pal skill packages that describe how a Pal performs a recurring capability.

## When To Use

Use when a Pal needs a stable ability such as intake, review, export planning, research planning, drafting, or evidence audit.

## Inputs

- target Pal role
- recurring task type
- required inputs and outputs
- existing knowledge/workflows
- quality expectations

## Required Context

Read target Pal role files, `pal-skill-vs-knowledge-vs-workflow.md`, related knowledge, and any existing skill index.

## Process

1. Define the skill purpose and trigger conditions.
2. Identify required inputs and context.
3. Specify step-by-step process.
4. Define outputs and quality bar.
5. Add confirmation points and no-code/runtime boundaries.
6. Add common mistakes and one concrete example.
7. Link supporting knowledge, workflow, and eval files.

## Output

- skill file plan or draft
- supporting knowledge/workflow/eval needs
- Runtime Task Package for writing approved skill files

## Quality Bar

A skill file should let the Pal perform or guide the task repeatedly. It should not be only a capability label.

## User Confirmation Points

- creating or modifying skill files
- reading private examples
- changing target Pal behavior

## No-Code Boundary

Skills are Markdown instructions, not executable plugins or tools.

## Common Mistakes

- confusing Skill with Knowledge
- omitting process steps
- omitting quality bar
- using vague future language instead of concrete behavior

## Example

For a Research Pal, a source-quality skill includes inputs, source checks, citation output, uncertainty labels, and refusal boundaries.
