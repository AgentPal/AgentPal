# File Workflow Design Skill

## Purpose

Design safe file workflows for document sets, folders, naming, archives, and handoff packages.

## When to use

Use for organizing documents, creating folder structures, planning renames, archiving, preparing evidence folders, or file delivery processes.

## Inputs

Folder scope, file types, naming rules, retention needs, output destination, privacy boundary, and allowed operations.

## Required context

File safety principles, backup expectations, dry-run requirement, and affected-path evidence.

## Process

1. Define source, destination, and forbidden paths.
2. Classify file groups and naming taxonomy.
3. Require dry-run or candidate list before mutation.
4. Add backup, rollback, and conflict rules.
5. Specify evidence and user approval gates.

## Output

File workflow plan with inventory, taxonomy, operation sequence, confirmation gates, and evidence requirements.

## Quality bar

The workflow must be reversible where possible and must not hide destructive or broad operations.

## User confirmation points

Confirm deletion, overwrite, bulk move, rename, compression, upload, and retention decisions.

## No-code boundary

This skill plans workflows only and does not add file operation tools.

## Common mistakes

Skipping dry-run, treating "old" files as disposable, or losing original paths.

## Example

Morgan designs a folder cleanup workflow with candidate list, rename preview, backup location, conflict policy, and affected-path report.

