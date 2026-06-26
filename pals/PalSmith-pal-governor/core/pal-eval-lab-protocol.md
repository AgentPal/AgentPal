# Pal Eval Lab Protocol

Status: PalSmith v0.2 no-code protocol.

The Eval Lab helps a new or changed Pal prove identity, boundary, collaboration, and release safety before moving toward testing or stable.

## Eval Types

- identity consistency test
- responsibility boundary test
- non-responsibility test
- dangerous request test
- output format test
- collaboration request test
- import / export safety test
- registry / contacts consistency test

## Creation Flow

After creating or modifying a Pal, PalSmith should ask:

"Should I generate and run a Pal Eval Lab pass for this Pal?"

## Runtime Execution

The current Runtime may execute the Markdown eval by reading the target Pal files and recording pass/fail evidence. PalSmith reviews the evidence and recommends draft, testing, stable, or further edits.

## Output

- passed items
- failed items
- files needing changes
- suggested status: draft, testing, stable, deprecated, or archived
- `not-run` items
