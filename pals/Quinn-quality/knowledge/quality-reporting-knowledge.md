# Quality Reporting Knowledge

## Concept Explanation

Quality reporting turns verification findings into a decision the user and next owner can act on. It should be concise, evidence-backed, and honest about uncertainty.

## Judgement Standards

- Start with decision.
- Separate evidence, risk, gaps, not-run, and next actions.
- Name residual uncertainty.
- Avoid unsupported reassurance.
- Keep technical identifiers exact.

## Examples

- "Decision: partial. JSON passed; browser QA not-run; release blocked until visual evidence or user risk acceptance."
- "Decision: fail. Required file missing and false completion detected."

## Counterexamples

- "Looks good overall."
- "Everything is fine" with no evidence.
- Long narrative that hides the decision.

## Scope

Use for completion reports, release gates, cross-Pal reviews, and final acceptance summaries.

## How This Becomes Skill, Workflow, Or Eval

It supports `quality-report-writing-skill.md`, `quality-reporting-workflow.md`, and final report review runbooks.

## Common Mistakes

- Mixing claim and evidence.
- No next owner.
- No not-run section.

## Source Refs Or Local Notes

Sources: OpenAI eval article on specify, measure, improve; AgentPal output contract and evidence policy.
