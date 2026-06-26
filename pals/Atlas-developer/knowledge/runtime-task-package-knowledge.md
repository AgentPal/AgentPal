# Runtime Task Package Knowledge

## Concept explanation

A Runtime Task Package is the bridge between Pal-layer judgement and execution-layer work. It tells the runtime what to read, what it may edit, what it must not edit, how to verify, and how to report.

## Judgement standards

- Include goal, files to read, files allowed to edit, files forbidden to edit, required docs, acceptance criteria, verification commands or evidence, risk boundary, rollback notes, and final report format.
- State that Codex or another runtime executes and returns evidence.
- Use current project instructions and local patterns.
- Require not-run labels for skipped checks.

## Examples

- Good: "Allowed edits: `src/auth/LoginForm.tsx` and matching tests. Forbidden: auth middleware, migrations, package files."
- Good: "Verification: run `npm test -- LoginForm` or report why unavailable."
- Good: "Final report: changed files, checks run, not-run checks, risks."

## Counterexamples

- Bad: "Fix the bug and tell me when done."
- Bad: No forbidden files.
- Bad: Runtime decides owner Pal after execution starts.

## Scope

Use for all real file or command work under AgentPal.

## How it becomes skill / workflow / eval

Use with `runtime-task-package-writing-skill.md`, `developer-handoff-skill.md`, `implementation-task-package-workflow.md`, and `atlas-task-package-eval.md`.

## Common mistakes

- Over-specifying implementation details while under-specifying evidence.
- Missing rollback notes.
- Forgetting approval gates.
- Treating a task package as execution evidence.

## Source references or local notes

External: A01, A05. Local: AgentPal task package contracts and Atlas prompt structure.
