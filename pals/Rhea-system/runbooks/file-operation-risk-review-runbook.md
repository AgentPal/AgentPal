# file-operation-risk-review-runbook

## Trigger

Before delete, move, overwrite, rename, recursive edit, import, export, or cleanup.

## Inputs

Target path, action type, workspace root, backup status, expected output, and user intent.

## Steps

1. Resolve exact target.
2. Classify action and reversibility.
3. Check tracked/untracked/ignored/private/system status where relevant.
4. Require listing before destructive action.
5. Require backup or recovery plan.
6. Define post-action evidence.

## Decision points

- Is the path exact?
- Is the action reversible?
- Is approval required?

## Outputs

File operation risk review.

## Quality checks

No broad glob or recursive operation without proof.

## Required user confirmation

Required for destructive, recursive, external, system, private, or unclear operations.

## Evidence to return

Target path, action, risk level, backup/recovery, changed files, and result.

