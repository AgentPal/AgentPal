# no-code-boundary-review-workflow

## Trigger

AgentPal Pal assets, release docs, or PalSmith-governed files may add executable assets or tool-like behavior.

## Inputs

Changed paths, allowed file types, forbidden file patterns, public/private boundary, and release scope.

## Steps

1. Confirm the target scope.
2. Check forbidden code and runtime dependency file types.
3. Check tool directories and executable-like assets.
4. Check installer, daemon, scanner, and validation-tooling wording.
5. Check private memory, state, reports, logs, tokens, or credentials.
6. Record allowed documentation-only exceptions.

## Decision points

- Is a file documentation-only or executable?
- Is private data exposed?
- Does wording imply AgentPal executes tools by itself?

## Outputs

No-code boundary review with pass/fail items, exceptions, and required fixes.

## Quality checks

Specific paths are named; exceptions are justified; not-run items are explicit.

## Required user confirmation

Required before deleting, moving, or rewriting files outside the approved Rhea scope.

## Evidence to return

Forbidden file scan result, risky wording result, exception list, and status summary.

