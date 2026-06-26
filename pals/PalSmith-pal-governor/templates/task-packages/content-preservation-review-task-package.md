# Content Preservation Review Task Package

task_name: Content Preservation Review Task Package
owner_pal: PalSmith
executing_runtime: current Agent Runtime

## User Goal

Review whether ingested material preserved source substance, examples, steps, boundaries, and source anchors.

## Allowed Reads

- approved original source material
- generated target knowledge/skill/workflow/runbook/template/eval files
- source inventory and classification table

## Forbidden Reads

- unrelated private files
- unapproved memory
- credentials, tokens, logs

## Verification Requirements

- source inventory exists
- classification table exists
- examples retained
- operational steps retained
- limitations and exceptions retained
- uncertain sections retained for review
- summary does not replace full knowledge
- no private content moved into public release files

## Expected Output

Content Preservation Review with pass/needs-work/fail per source and per target file.
