# User Material Ingestion Task Package

task_name: User Material Ingestion Task Package
owner_pal: PalSmith
executing_runtime: current Agent Runtime

## User Goal

Convert user-approved material into Pal knowledge, skills, workflows, runbooks, templates, evals, examples, references, persona/voice, boundaries, or decisions without losing substantive content.

## Allowed Reads

- explicitly approved user material paths or pasted text
- target Pal public files
- target Pal existing indexes

## Forbidden Reads

- unapproved private memory
- unrelated project files
- credentials, tokens, logs

## Execution Steps For Runtime

1. Read approved sources.
2. Produce source inventory.
3. Classify content sections.
4. Draft target file plan.
5. Write confirmed files only if the user approved write paths.
6. Return evidence and preservation checklist.

## Expected Output

- Material Ingestion Plan
- Source Inventory
- Classification Table
- file plan
- unclassified review list
- Content Preservation Checklist

## Verification Requirements

- no source dropped silently
- private/public boundary recorded
- long sources split when needed
- `not-run` for unread sections
