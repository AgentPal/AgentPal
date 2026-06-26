# Runtime Task Package Writing Skill

## Purpose

Help Atlas write high-quality task packages for Codex, Claude Code, OpenHands, CodeWhale, or another execution runtime.

## When to use

Use whenever real file edits, command execution, tests, builds, browser checks, or release checks are needed.

## Inputs

- Goal.
- Files to read.
- Files allowed to edit.
- Files forbidden to edit.
- Required docs or sources.
- Acceptance criteria.
- Verification commands or evidence.
- Risk boundary.
- Rollback notes.
- Final report format.

## Required context

Use project instructions, local patterns, and owner Pal requirements. Do not let the runtime invent the Pal owner or expand the allowed file surface.

## Process

1. Name the Pal owner and execution runtime role.
2. State the exact goal and non-goals.
3. List files to read and files allowed to edit.
4. List forbidden files, commands, and scope expansions.
5. Provide implementation guidance without over-constraining local discovery.
6. Define acceptance criteria and verification evidence.
7. Add risk boundary, rollback notes, and stop conditions.
8. Define final report headings: changed files, verification, not-run checks, risks, and next steps.

## Output

A Runtime Task Package that can be copied into the execution layer.

## Quality bar

The package must make success and failure observable. It must require evidence, not a completion claim.

## User confirmation points

Ask before writing outside the current scope, installing dependencies, deleting files, publishing, staging/committing, or using sensitive data.

## No-code boundary

This skill writes Markdown instructions only. It does not become a CLI, tool, scanner, validator, or test runner.

## Common mistakes

- Omitting forbidden files.
- Letting "fix it" stand in for acceptance criteria.
- Failing to request changed files and test output.
- Asking the runtime to publish or delete without confirmation.

## Example

A task package for a bug fix lists the failing test, allowed module files, forbidden config files, expected passing command, and final report sections.
