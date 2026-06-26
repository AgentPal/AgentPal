# file-directory-safety-review

## Purpose

Review file and directory operations for deletion, move, overwrite, path traversal, scope errors, backups, and recovery options.

## When to use

Use before deleting, moving, renaming, overwriting, recursively editing, exporting, importing, or cleaning directories.

## Inputs

Target path, operation type, expected files, workspace root, backup plan, ignored/generated paths, and user intent.

## Required context

File-directory-safety knowledge, permission boundary review, approval gate, and current Runtime filesystem evidence.

## Process

1. Resolve the intended target path and owner scope.
2. Identify whether the operation is read-only, reversible, destructive, recursive, or external.
3. Check for private data, secrets, system paths, generated artifacts, or public release files.
4. Require listing or dry evidence before destructive action.
5. Require backup or recovery path when risk is medium or above.
6. Define after-action evidence.

## Output

File/directory safety review with action type, risk, confirmation requirement, backup/recovery notes, and evidence to return.

## Quality bar

No destructive or recursive operation should proceed without exact target, scope proof, and user confirmation.

## User confirmation points

Strong confirmation is required for recursive deletion, overwrite, move outside workspace, system paths, private data, and public release files.

## No-code boundary

This skill creates a review artifact. Runtime performs any approved filesystem operation.

## Common mistakes

- Using broad path globs.
- Assuming generated output is safe to delete.
- Forgetting backups.
- Treating rename/move as risk-free.

## Example

Input: "Clean old reports." Output: "Need exact directory listing, confirmation of public/private status, archive plan, and post-action status."

