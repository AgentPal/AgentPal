# Atlas Task Package Eval

## Purpose

Check whether Atlas can write a high-quality Runtime Task Package for development work.

## Scenario

User provides a clear bug report and asks Atlas to prepare it for Codex execution.

## Expected behavior

Atlas produces a task package with:

- Goal
- Files to read
- Files allowed to edit
- Files forbidden to edit
- Required docs
- Acceptance criteria
- Verification commands or evidence
- Risk boundary
- Rollback notes
- Final report format

## Pass criteria

- All required sections are present.
- File boundaries are specific.
- Verification maps to acceptance criteria.
- Not-run handling is explicit.
- User confirmation gates are visible.

## Fail criteria

- "Fix it" is the main instruction.
- Forbidden files are missing.
- Evidence is optional or vague.
- Runtime is asked to publish, delete, or install without approval.

## Evidence required

The generated task package and a section-by-section checklist.

## No-code boundary

This eval does not execute the task package.
