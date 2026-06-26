# Definition Of Done Knowledge

## Concept Explanation

Definition of Done is a shared completion standard for an increment or task. In AgentPal, it prevents a Pal or Runtime from calling work complete until artifacts, evidence, review, risk, and reporting are all handled.

## Judgement Standards

- DoD applies across the whole deliverable.
- It includes artifact completeness, verification, documentation, risk, and evidence.
- It states what does not count as done.
- It must preserve not-run and partial status.
- It should be known before final reporting.

## Examples

- A Pal deepening task is done only when identity, skills, knowledge, workflows, runbooks, evals, research inventory, indexes, and validation checks are complete.
- A docs update is done when requested files are updated and unrelated docs are untouched.

## Counterexamples

- "All files exist" without content quality.
- "Report says finished" without checks.
- "Tests not available" treated as pass.

## Scope

Use for completion audits, release candidate review, implementation handoffs, and Pal upgrade tasks.

## How This Becomes Skill, Workflow, Or Eval

It supports `definition-of-done-design-skill.md`, `quality-reporting-workflow.md`, and self-health evals.

## Common Mistakes

- Confusing DoD with a checklist that can be waived silently.
- Ignoring evidence owner.
- Treating not-run as complete.

## Source Refs Or Local Notes

Source: Atlassian Definition of Done guide, accessed 2026-06-26. Local adaptation: AgentPal DoD requires no-code boundary and Runtime evidence.
