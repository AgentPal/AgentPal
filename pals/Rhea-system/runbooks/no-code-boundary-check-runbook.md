# no-code-boundary-check-runbook

## Trigger

Before release, Pal upgrade completion, or PalSmith governance review.

## Inputs

Target scope, forbidden file list, changed paths, and public/private boundary.

## Steps

1. Check forbidden code/runtime file types.
2. Check tool directories.
3. Check runtime dependency manifests.
4. Check installer, daemon, scanner, and validation-tooling wording.
5. Check memory/state/report privacy.
6. Record allowed documentation-only exceptions.

## Decision points

- Is the item executable or documentation?
- Is the item new or pre-existing?
- Is private material exposed?

## Outputs

No-code boundary report.

## Quality checks

Path-specific evidence, no hidden exceptions, and no execution claims.

## Required user confirmation

Required before deleting, moving, or rewriting files.

## Evidence to return

Matched paths, exceptions, pass/fail status, and not-run items.

