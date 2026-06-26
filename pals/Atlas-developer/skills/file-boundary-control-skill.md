# File Boundary Control Skill

## Purpose

Keep development work inside the smallest useful file and behavior boundary.

## When to use

Use before implementation, during review, and whenever a runtime or user suggests "while here" cleanup, broad refactor, generated-file updates, or unrelated formatting.

## Inputs

- Original request.
- Allowed files and modules.
- Forbidden files and modules.
- Current diff or proposed change set.
- Acceptance criteria and risk notes.

## Required context

Read the task package, project instructions, and relevant diff or file list. Do not approve broad changes from a summary alone.

## Process

1. Define the intended behavior change.
2. Map the minimal likely edit surface.
3. Mark forbidden paths and unrelated concerns.
4. Require approval before widening scope.
5. During review, compare changed files with the allowed list.
6. Classify out-of-scope changes as acceptable, needs explanation, needs rollback, or needs separate task.

## Output

A file-boundary decision, allowed/forbidden list, and scope-control finding.

## Quality bar

The user and runtime should both know what will be touched and why. Unrelated churn must be visible.

## User confirmation points

Ask before broad refactors, mass formatting, generated asset regeneration, dependency lockfile changes, config edits, or touching unrelated modules.

## No-code boundary

This skill does not inspect files automatically. It guides scope decisions and review.

## Common mistakes

- Treating extra cleanup as free progress.
- Accepting a changed-file list without checking it against the task.
- Expanding scope because a test failed elsewhere.
- Changing public AgentPal no-code assets into executable tools.

## Example

If a bug fix touches both the component and unrelated release notes, Atlas asks whether release notes were authorized or should be split into another task.
