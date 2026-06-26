# Create Pal Request Runbook

## Trigger

The user asks to create, improve, import, export, audit, package, version, roll back, or modify a Pal or Pal Pack.

## Inputs

- User material and desired Pal purpose.
- Target Pal name or directory.
- Source files and constraints.
- Contacts / registry status.
- PalSmith governance requirement.

## Steps

1. Confirm this is Pal asset lifecycle work.
2. Prepare a Context Packet for PalSmith with source material, target surface, preservation needs, and exclusions.
3. Request or simulate PalSmith gap report and task package.
4. Let the runtime edit only approved Markdown / JSON assets.
5. Run PalSmith-style review against quality, preservation, no-code boundary, and empty-shell risks.
6. Report what changed and what remains.

## Decision points

- Is the task creation, modification, audit, or packaging?
- Are contacts / registry edits requested or excluded?
- Is source material complete?
- Is a direct PalSmith handoff possible?

## Outputs

PalSmith gap report, upgrade package, edited assets, review report, and remaining issue list.

## Quality checks

- No Pal asset is created as an empty shell.
- User material is preserved and traceable.
- No runtime dependency is added.
- Contacts / registry are not changed without permission.

## Required user confirmation

Required for contacts / registry changes, identity changes outside requested scope, private source ingestion, or publishing.

## Evidence to return

Return PalSmith assets read, source materials used, files changed, validation checks, and not-run checks.
