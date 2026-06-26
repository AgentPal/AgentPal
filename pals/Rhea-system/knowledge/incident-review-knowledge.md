# incident-review-knowledge

## Concept Explanation

Incident review is a structured, evidence-based review of what happened, impact, timeline, contributing factors, mitigations, follow-ups, and learning candidates.

## Judgement Standards

- Define severity and current status.
- Use evidence, not blame.
- Record timeline and affected scope.
- Identify root-cause candidates and contributing factors.
- Create specific follow-up actions.
- Protect private logs and sensitive data.

## Examples

- Failed release check: record command, exit status, affected file, fix, and rerun.
- Broken environment: record symptom, read-only checks, repair evidence, and remaining risk.

## Counterexamples

- "The user broke it."
- "It is fixed" without rerun evidence.

## Scope

Use for failed commands, release failures, unsafe operations, data exposure, and repeated runtime failures.

## How This Becomes Skill, Workflow, Or Eval

Skill: incident-review. Workflow: incident-review. Eval: incident review.

## Common Mistakes

Skipping timeline, missing evidence, writing private logs into public assets, and no follow-up owner.

## Source Refs Or Local Notes

Based on Atlassian incident sources SRC-06 and SRC-07.

