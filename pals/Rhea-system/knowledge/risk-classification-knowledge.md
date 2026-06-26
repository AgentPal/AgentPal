# risk-classification-knowledge

## Concept Explanation

Rhea classifies operational risk as low, medium, high, critical, or blocked to decide what evidence, approval, and rollback are required.

## Judgement Standards

- Low: read-only or reversible within a narrow known scope.
- Medium: local file change or bounded configuration with recovery path.
- High: destructive, privileged, external, release-impacting, or sensitive-data action.
- Critical: system-wide, irreversible, security-impacting, privacy-impacting, or unclear blast radius.
- Blocked: target, authority, evidence, safety, or user approval is insufficient.

## Examples

- Low: read a target README.
- Medium: edit a tracked Markdown file.
- High: delete a directory or change PATH.
- Critical: change services or system protection.
- Blocked: unknown target path for recursive deletion.

## Counterexamples

- Calling deletion low because the user asked quickly.
- Calling release ready without evidence.

## Scope

Use for all Rhea tasks.

## How This Becomes Skill, Workflow, Or Eval

Skill: risk-classification. Workflow: runtime-safety-intake and approval gate. Eval: risk approval.

## Common Mistakes

No rationale, no approval mapping, and no blocked state.

## Source Refs Or Local Notes

Based on SRC-04, SRC-06, and Rhea local risk assets.

