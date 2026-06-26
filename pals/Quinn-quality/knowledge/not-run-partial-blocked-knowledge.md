# Not-run Partial Blocked Knowledge

## Concept Explanation

not-run, partial, and blocked are distinct states. not-run means a check did not happen. partial means some requirements are met and some are not proven. blocked means progress or acceptance cannot responsibly continue without missing input, permission, capability, or external state.

## Judgement Standards

- not-run is not pass.
- not-run is not automatically fail.
- partial must list completed and incomplete requirements.
- blocked must name the blocking condition.
- A final report must preserve these states.

## Examples

- Browser verification not-run because browser binaries are unavailable.
- JSON parse passed but release export not-run, so overall status is partial.
- User confirmation missing for deleting files, so deletion is blocked.

## Counterexamples

- "Tests unavailable, so assume okay."
- "Most things done, so pass."
- "Blocked" used for an ordinary inconvenience.

## Scope

Use in all verification, release, and completion reports.

## How This Becomes Skill, Workflow, Or Eval

It supports `not-run-handling-skill.md`, `not-run-triage-runbook.md`, and false completion evals.

## Common Mistakes

- Removing not-run from summaries.
- Treating blocked as failure without explanation.
- Hiding partial completion in a positive report.

## Source Refs Or Local Notes

Local memory and user preference: when verification did not happen, report `not-run` or `runtime-unavailable`, not pass.
