# rollback-readiness-review

## Purpose

Check whether a change can be safely reversed or recovered from before it is attempted or before release is claimed.

## When to use

Use for release tasks, file edits, dependency changes, environment changes, install/uninstall plans, registry/contact updates, imports, exports, and high-risk operations.

## Inputs

Change description, affected paths/components, backup status, version control status, previous known-good state, rollback authority, and evidence required.

## Required context

Rollback readiness knowledge, release safety knowledge, file/directory safety, and approval gates.

## Process

1. Identify the reversible unit.
2. Identify the previous known-good state or backup.
3. Identify who can perform rollback and under what approval.
4. Identify rollback test or evidence.
5. Mark irreversible or unclear rollback as high or blocked.
6. Record recovery steps without executing them.

## Output

Rollback readiness review with status: ready, partial, missing, not-run, or blocked.

## Quality bar

Rollback readiness must be specific to the affected files/system, not a generic "use git" claim.

## User confirmation points

Ask before proceeding if rollback is missing for high-risk or critical operations.

## No-code boundary

This skill writes a readiness review only. It does not perform rollback.

## Common mistakes

- Assuming version control covers untracked files.
- Forgetting generated or ignored outputs.
- Ignoring service or environment state.
- Treating backup existence as tested recovery.

## Example

"Rollback partial: tracked files can be reverted by git, but new untracked files need explicit removal or archive plan."

