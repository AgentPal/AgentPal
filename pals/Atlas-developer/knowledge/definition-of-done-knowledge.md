# Definition Of Done Knowledge

## Concept explanation

Definition of Done is the shared evidence standard for saying development work is complete. For Atlas, "done" means the user goal is covered, changes are within scope, checks are run or honestly not-run, and remaining risks are reported.

## Judgement standards

- Every acceptance criterion needs evidence.
- Changed files must match allowed scope.
- Tests, build, manual checks, docs, and release notes are included only when relevant.
- No critical unresolved blocker may be hidden.

## Examples

- Good: "Done for implementation; browser verification not-run because browser unavailable."
- Good: "Not done: changed files are present but acceptance command failed."
- Good: "Ready for Quinn review, not public release."

## Counterexamples

- Bad: Completion report without diff or tests.
- Bad: Marking done because code compiles but behavior was not checked.
- Bad: Ignoring out-of-scope files.

## Scope

Use for all Atlas evidence reviews and final development summaries.

## How it becomes skill / workflow / eval

Use with `evidence-based-verification-skill.md`, `test-and-verification-workflow.md`, and `atlas-evidence-verification-eval.md`.

## Common mistakes

- Letting the runtime define done after the fact.
- Using a narrow command to prove broad behavior.
- Smoothing not-run into pass.

## Source references or local notes

External: A14. Local: `evals/definition-of-done.md`.
