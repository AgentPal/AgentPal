# no-code-boundary-audit

## Purpose

Audit whether AgentPal release assets preserve the no-code boundary.

## When to use

Use during Pal upgrades, release preflight, PalSmith governance review, or when a task could add executable assets.

## Inputs

Target paths, changed files, expected asset types, forbidden file patterns, public/private boundary, and release scope.

## Required context

AgentPal no-code standard, PalSmith governance rules, Rhea source inventory, and current file status.

## Process

1. Check for forbidden code files: `.py`, `.js`, `.ts`, `.rs`, `.ps1`, `.sh`, `.bat`, `.cmd`, `package.json`, `requirements.txt`, `Cargo.toml`.
2. Check for `tools/` directories or tool-like implementation assets.
3. Check for runtime dependencies, installer wording, daemon wording, scanner wording, and validation-tooling wording.
4. Check for private memory, state, or reports in public release paths.
5. Check that docs describe Runtime execution as external evidence, not built-in AgentPal behavior.
6. Report allowed documentation-only exceptions, such as `imports/tools/README.md` when present.

## Output

No-code boundary audit with pass/fail items, allowed exceptions, risky wording, and required fixes.

## Quality bar

The audit must be specific enough to identify paths and not hide exceptions.

## User confirmation points

Ask before removing or relocating files, changing release scope, or touching private memory/state/report paths.

## No-code boundary

This skill is documentation-only. It does not create a scanner or validation tool.

## Common mistakes

- Treating a directory named tools as harmless without checking contents.
- Ignoring runtime dependency manifests.
- Calling a manual search a built-in validator.
- Publishing private state or reports.

## Example

Result: "`imports/tools/README.md` is documentation-only and pre-existing; no executable tool files were added in Rhea paths."

