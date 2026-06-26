# False Completion Knowledge

## Concept Explanation

False completion happens when work is presented as finished even though the requested end state is missing, unverified, contradicted, or only planned.

## Judgement Standards

- Derive requirements from the original request, not from the report.
- File creation alone is insufficient if content requirements are unmet.
- A plan is not execution.
- Not-run checks cannot support pass.
- Partial work must stay partial.

## Examples

- A Pal report claims "release-ready" without clean export evidence.
- A task claims tests passed when no test command ran.
- A migration is described but no files changed.

## Counterexamples

- A report says partial and lists exact missing checks.
- A check is not-run and accepted by the user as residual risk.

## Scope

Use for completion audits, release review, Pal upgrades, imports/exports, and AI-agent task reviews.

## How This Becomes Skill, Workflow, Or Eval

It supports `false-completion-detection-skill.md`, `false-completion-check-runbook.md`, and `quinn-false-completion-eval.md`.

## Common Mistakes

- Accepting a polished final report as evidence.
- Only checking the easiest requirement.
- Redefining success around what was done.

## Source Refs Or Local Notes

Sources: OpenAI eval framing and Anthropic agent eval guidance. Local AgentPal completion audit rules require requirement-by-requirement evidence.
