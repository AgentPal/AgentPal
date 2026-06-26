# Risk And Approval For Code Changes Skill

## Purpose

Help Atlas recognize risky engineering actions and stop for the correct approval before runtime work proceeds.

## When to use

Use for deletes, broad moves, dependency changes, schema/data migrations, credentials, deployment, publishing, generated files, security settings, production data, or release state.

## Inputs

- Proposed code or config action.
- Scope and reversibility.
- Affected data or users.
- Runtime permissions.
- User's explicit approvals.

## Required context

Read current task boundary, repository instructions, and relevant risk notes. Do not inspect or change sensitive files unless allowed.

## Process

1. Classify the risk.
2. Check whether user permission covers the exact action.
3. If not, stop and ask a focused confirmation question.
4. If yes, add safety boundary and evidence requirements to the task package.
5. Require rollback notes for risky changes.
6. Report what was not attempted.

## Output

A risk and approval decision, approval question, or guarded task package clause.

## Quality bar

The approval request must name the exact action, scope, reversibility, and evidence needed.

## User confirmation points

Always ask before destructive operations, dependency installs, migration, deployment, publishing, real-data access, secret handling, staging/commit/push, or registry/contact edits.

## No-code boundary

This skill does not perform risky actions; it only gates them.

## Common mistakes

- Treating prior general approval as permission for new risk.
- Hiding risky side effects inside a normal task package.
- Forgetting rollback notes.
- Running tests against real external services by default.

## Example

For a dependency upgrade, Atlas asks for approval, requires lockfile evidence, build/test output, rollback path, and forbids unrelated package updates.
