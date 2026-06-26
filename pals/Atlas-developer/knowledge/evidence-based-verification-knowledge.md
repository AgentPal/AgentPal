# Evidence Based Verification Knowledge

## Concept explanation

Evidence-based verification maps claims to current proof: changed files, command output, test results, manual checks, artifacts, screenshots, logs, and explicit not-run labels.

## Judgement standards

- Claims without evidence are unproven.
- Evidence must match the requirement's scope.
- Not-run checks are not failures by default, but they limit the final judgement.
- Completion requires every explicit requirement to be proven or explicitly accepted as not-run risk.

## Examples

- Good: "JSON parse OK for listed files; browser test not-run."
- Good: "Changed files match allowed scope."
- Good: "Task incomplete because the required command failed."

## Counterexamples

- Bad: "Looks complete" from a summary only.
- Bad: Treating no search hits as proof of all behavior.
- Bad: Claiming tests passed when the command was not run.

## Scope

Use after any runtime-backed development task or release check.

## How it becomes skill / workflow / eval

Use with `evidence-based-verification-skill.md`, `code-review-workflow.md`, `test-and-verification-workflow.md`, and self-health eval.

## Common mistakes

- Accepting AI-generated code without review.
- Treating confidence as proof.
- Not checking file boundary.
- Forgetting user-required final report fields.

## Source references or local notes

External: A16 and A06. Local: `knowledge/runtime/evidence-review-checklist.md`.
