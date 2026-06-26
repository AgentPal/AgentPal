# least-privilege-knowledge

## Concept Explanation

Least privilege means granting only the minimum access needed for the task. For Rhea, it means recommending the narrowest safe Runtime action and avoiding broad admin or write access.

## Judgement Standards

- Minimize scope, privilege, and data exposure.
- Prefer path-specific operations over broad globs.
- Prefer read-only evidence before write operations.
- Prefer summaries over raw sensitive logs.
- Escalate only when lower privilege cannot achieve the task.

## Examples

- Read a directory listing before deleting files.
- Parse only target JSON files instead of sweeping the whole disk.

## Counterexamples

- Run as administrator because it might help.
- Share a full log when one error line is enough.

## Scope

Use for permission review, runtime task package briefing, release checks, and evidence review.

## How This Becomes Skill, Workflow, Or Eval

Skill: permission-boundary-review and approval-gate-design. Eval: risk approval.

## Common Mistakes

Confusing convenience with necessity, using broad access, and failing to reduce context.

## Source Refs Or Local Notes

Based on NIST least privilege (SRC-03), Microsoft least privilege (SRC-10), and Zero Trust verification ideas (SRC-11).

