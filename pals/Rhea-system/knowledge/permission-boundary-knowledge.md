# permission-boundary-knowledge

## Concept Explanation

A permission boundary is crossed when a task needs elevated access, protected paths, external services, private data, credentials, system settings, or organization-controlled resources.

## Judgement Standards

- Use least privilege.
- Prefer read-only checks.
- Identify data exposure and blast radius.
- Require strong confirmation for elevated or destructive actions.
- Block when target or authority is unclear.

## Examples

- Editing a user project Markdown file is low or medium.
- Changing registry, services, startup items, or system directories is high or critical.

## Counterexamples

- Treating admin prompts as routine.
- Asking for secrets in raw form.

## Scope

Use for system operations, file operations, release operations, runtime setup, and Pal asset governance writes.

## How This Becomes Skill, Workflow, Or Eval

Skill: permission-boundary-review. Workflow: high-risk-operation-approval. Eval: risk approval.

## Common Mistakes

No exact target path, no approval text, and no recovery path.

## Source Refs Or Local Notes

Based on SRC-03, SRC-10, and local Rhea security assets.

