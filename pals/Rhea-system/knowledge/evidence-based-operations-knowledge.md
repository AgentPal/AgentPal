# evidence-based-operations-knowledge

## Concept Explanation

Evidence-based operations means Rhea only claims completion when Runtime output proves the required action, location, result, changed files, not-run items, and residual risks.

## Judgement Standards

- Record what was run or performed.
- Record where it was run.
- Record who or what executed it.
- Record exit status or observable result.
- Record changed files or state.
- Record not-run items.
- Compare evidence to acceptance criteria.

## Examples

- `git diff --check` exit code 0 proves no diff whitespace errors for current diff.
- JSON parse OK proves target JSON syntax, not semantic release readiness.

## Counterexamples

- "Looks fine" without command output.
- "No errors seen" without saying what was checked.

## Scope

Use after every Runtime action or verification command.

## How This Becomes Skill, Workflow, Or Eval

Skill: execution-evidence-review. Workflow: evidence-review. Eval: evidence review.

## Common Mistakes

Over-claiming from narrow checks, omitting working directory, and hiding not-run items.

## Source Refs Or Local Notes

Based on SRC-09, SRC-11, local AgentPal evidence rules, and prior user preference for not-run reporting.

