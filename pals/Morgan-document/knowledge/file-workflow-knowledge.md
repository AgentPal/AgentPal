# File Workflow Knowledge

## Concept Explanation

File workflow design organizes file sets safely with source scope, destination scope, naming, dry-run, backup, rollback, and evidence.

## Judgement Standards

- Define allowed and forbidden paths.
- Prefer candidate lists before mutation.
- Preserve original names and locations in evidence.
- Ask approval for destructive or broad operations.

## Examples

- Rename preview with old path, new path, reason, and conflict status.
- Archive plan with retention and recovery note.

## Counterexamples

- Moving files because they look unused.
- No backup or affected-path record.

## Scope

Folder organization, naming, archiving, file delivery, and document evidence sets.

## How This Becomes Skill, Workflow, Or Eval

Use in `file-workflow-design-skill.md` and file workflow eval checks.

## Common Mistakes

Broad path access, weak rollback, and unconfirmed deletion.

## Source Refs Or Local Notes

S08, S09, S13; local Morgan file safety assets.

