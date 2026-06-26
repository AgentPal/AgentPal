# Implementation Task Package Workflow

## Trigger

Development intake confirms that a task is ready for runtime implementation.

## Inputs

- Goal.
- Files to read.
- Files allowed to edit.
- Files forbidden to edit.
- Required docs and local patterns.
- Acceptance criteria.
- Verification evidence.
- Risk and rollback notes.

## Steps

1. Convert the goal into verifiable behavior.
2. List required reads and allowed edits.
3. List forbidden files, actions, and non-goals.
4. Add implementation stages.
5. Add verification commands or manual evidence.
6. Add risk boundary, approval gates, rollback notes, and stop conditions.
7. Define final report format.
8. Hand the package to the runtime.

## Decision points

- Are acceptance criteria observable?
- Is the file scope narrow enough?
- Does the runtime need source research or environment checks first?
- Is the task too broad for one pass?

## Outputs

Runtime Task Package ready for execution.

## Quality checks

- Goal and non-goals are both present.
- Allowed and forbidden files are present.
- Verification maps to acceptance criteria.
- Not-run reporting is required.

## Required user confirmation

Required before expanding scope, installing dependencies, destructive actions, publishing, or changing release state.

## Evidence to return

Runtime must return changed files, diff summary, checks run, not-run checks, artifacts, risks, and next steps.
