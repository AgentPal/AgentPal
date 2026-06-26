# file-directory-safety-knowledge

## Concept Explanation

File and directory safety is the practice of proving target scope, reversibility, privacy status, and evidence needs before any operation that changes files.

## Judgement Standards

- Resolve exact target paths.
- Avoid recursive actions without proof.
- Identify tracked, untracked, ignored, generated, public, private, and system paths.
- Require backup or recovery for medium and above.
- Report changed files after execution.

## Examples

- Safe: rename a startup shortcut to `.disabled` after confirming exact path and reversibility.
- Safe: edit a specific Markdown file under an allowed Pal directory.

## Counterexamples

- Delete all reports without listing them.
- Move computed paths across drives without target verification.

## Scope

Use for file edits, cleanup, import/export, release packaging, Pal assets, and local system files.

## How This Becomes Skill, Workflow, Or Eval

Skill: file-directory-safety-review. Runbook: file-operation-risk-review. Eval: risk approval.

## Common Mistakes

Forgetting untracked files, assuming backups exist, and treating generated files as safe to remove.

## Source Refs Or Local Notes

Based on local Windows startup memory-derived pattern, local AgentPal edit rules, SRC-04, SRC-08, and SRC-09.

