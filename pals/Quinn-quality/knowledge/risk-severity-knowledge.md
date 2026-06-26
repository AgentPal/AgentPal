# Risk Severity Knowledge

## Concept Explanation

Risk severity describes the potential impact and action needed when evidence is missing, behavior may break, privacy may be exposed, release may fail, or user trust may be affected.

## Judgement Standards

- Low: small impact, reversible, evidence sufficient.
- Medium: limited impact or partial evidence; acceptance may be conditional.
- High: user-visible, data, privacy, permission, release, or rollback risk.
- Critical: severe irreversible or external harm, production danger, or sensitive disclosure.
- Blocked: evidence or permission is insufficient to proceed responsibly.

## Examples

- Missing screenshot for a visual-only change is medium or high depending on release scope.
- Missing rollback for production release is high or blocked.
- Private token in public package is critical.

## Counterexamples

- Calling unknown low.
- Calling all not-run checks high without context.

## Scope

Use in all Quinn reports, release gates, not-run handling, and cross-Pal review.

## How This Becomes Skill, Workflow, Or Eval

It supports `risk-severity-classification-skill.md`, `release-quality-gate-workflow.md`, and quality report sections.

## Common Mistakes

- Mixing severity with personal confidence.
- Failing to explain impact.
- Omitting user confirmation need.

## Source Refs Or Local Notes

Source: ISTQB risk-based testing concept. Local adaptation uses AgentPal safety and privacy boundaries.
