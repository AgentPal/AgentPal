# permission-boundary-review

## Purpose

Review whether a task crosses permission boundaries such as admin rights, protected paths, external services, credentials, private logs, or organization policy.

## When to use

Use before any action involving elevated privileges, system directories, registry, services, startup items, PATH, environment variables, secrets, private data, or external writes.

## Inputs

Task goal, target paths, requested commands/actions, account context if known, sensitive data involved, and rollback options.

## Required context

Least-privilege knowledge, approval-gate knowledge, user confirmation policy, and current Runtime permissions.

## Process

1. Identify the permission boundary crossed.
2. Apply least privilege: ask whether the task can be done with lower privilege or read-only checks first.
3. Identify data exposure and blast radius.
4. Classify risk.
5. Define user approval language.
6. Define evidence required after execution.

## Output

Permission boundary review with risk level, least-privilege alternative, approval requirement, blocked actions, and evidence requirements.

## Quality bar

The review must make privilege escalation visible and must not normalize admin access for convenience.

## User confirmation points

Strong confirmation is required for admin privileges, system settings, registry, services, startup items, deletion, external writes, private logs, or secrets.

## No-code boundary

The skill only reviews permissions and writes Markdown/JSON guidance. It does not request or grant privileges.

## Common mistakes

- Treating user intent as approval.
- Accepting broad permissions when narrower permissions work.
- Sharing raw secrets or logs.
- Failing to mark blocked actions.

## Example

Input: "Delete this system folder." Output: "Critical risk. Need exact path, purpose, backup status, owner confirmation, and safer alternative before any Runtime action."

