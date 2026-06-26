# Evidence Review Knowledge

## Concept Explanation

Evidence review checks whether proof actually supports a claim. It compares original objective, changed files, commands or checks, artifacts, failures, and risk notes against the completion claim.

## Judgement Standards

- Every major claim needs a source of proof.
- Command output must include where and what ran when relevant.
- Changed files must match the claimed scope.
- Manual verification must identify who or what observed the result.
- Missing evidence downgrades the conclusion.

## Examples

- `ConvertFrom-Json` output supports JSON parse.
- `git diff --check` supports whitespace validation.
- A screenshot supports rendered UI inspection only if it shows the relevant viewport.

## Counterexamples

- "Tests passed" with no command.
- "No errors seen" without a check.
- "Looks safe" without risk evidence.

## Scope

Use for all completion reports, release gates, Pal asset reviews, Runtime task packages, and cross-Pal summaries.

## How This Becomes Skill, Workflow, Or Eval

It supports `evidence-review-skill.md`, `evidence-review-workflow.md`, `review-completion-report-runbook.md`, and `quinn-evidence-review-eval.md`.

## Common Mistakes

- Checking only that evidence exists, not whether it proves the claim.
- Ignoring failure output.
- Omitting not-run evidence.

## Source Refs Or Local Notes

Sources: GitLab release evidence docs, Google Engineering Practices review guidance, OpenAI eval guidance. Local memory note: unrun verification must be reported as not-run or runtime-unavailable.
