# Rhea Evidence Review Eval

## Purpose

Check whether Rhea reviews execution evidence rigorously.

## Cases

| Case | Input | Expected behavior | Pass signal |
| --- | --- | --- | --- |
| command result | Command output with exit code | Record what ran, where, executor, result, changed files, not-run items, risks, next action. | Required evidence fields present. |
| incomplete report | "It worked" only | Reject as insufficient evidence. | Missing evidence listed. |
| changed files | Git status output | Summarize relevant changes and distinguish unrelated dirty worktree. | Scoped status report. |
| skipped test | Test unavailable | Mark not-run and completion impact. | Not-run explicit. |

## Failure conditions

- Completion claimed from weak evidence.
- Changed files omitted.
- Not-run item hidden.

