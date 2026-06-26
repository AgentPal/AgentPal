# File Boundary Knowledge

## Concept explanation

File-boundary control keeps implementation work within the agreed edit surface and prevents unrelated churn.

## Judgement standards

- Define allowed files and forbidden files before execution.
- New discoveries may justify scope expansion only with explanation and approval.
- Generated files, lockfiles, configs, and release assets need explicit mention.
- Review changed files against the original task.

## Examples

- Good: A CSS bug fix changes one component stylesheet and one visual test.
- Good: A dependency lockfile change is called out and justified.
- Good: A broad refactor is split into a separate task.

## Counterexamples

- Bad: "While here" formatting across unrelated files.
- Bad: Moving directories during a small bug fix.
- Bad: Editing release metadata during implementation without approval.

## Scope

Use before runtime edits, during code review, and in evidence review.

## How it becomes skill / workflow / eval

Use with `file-boundary-control-skill.md`, `refactor-safety-runbook.md`, and `atlas-file-boundary-eval.md`.

## Common mistakes

- Treating no failing tests as proof that unrelated changes are acceptable.
- Ignoring hidden generated files.
- Allowing multi-thread work to modify overlapping files.

## Source references or local notes

External: A03 and A15. Local: AgentPal context slicing and Atlas boundary files.
