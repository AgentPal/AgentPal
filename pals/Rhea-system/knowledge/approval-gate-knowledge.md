# approval-gate-knowledge

## Concept Explanation

An approval gate is a user-facing checkpoint that states the exact action, target, risk, reversibility, alternatives, and evidence before a risky operation.

## Judgement Standards

- Gate text must be concrete.
- High and critical require explicit confirmation.
- Multiple risky actions should be separated.
- Read-only checks can often proceed with lower friction.
- Approval must not be inferred from general task intent.

## Examples

- "Confirm Runtime may rename this exact file to `.disabled`; this is reversible."
- "Confirm Runtime may edit these two JSON files; no publish or commit will occur."

## Counterexamples

- "Can I fix it?"
- "Proceed with all needed actions."

## Scope

Use for file operations, system changes, installs, release actions, registry/contact changes, and private material handling.

## How This Becomes Skill, Workflow, Or Eval

Skill: approval-gate-design. Workflow: high-risk-operation-approval. Eval: risk approval.

## Common Mistakes

Vague approval, missing targets, hidden rollback conditions, and bundling unrelated actions.

## Source Refs Or Local Notes

Based on SRC-06, SRC-08, SRC-10, and PalSmith controlled-write policy.

