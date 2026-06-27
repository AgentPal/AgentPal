# Failure: Runtime Skill Execution Without Verification

## Wrong Behavior

The host Runtime reports that a repo-analysis Skill ran, and AgentPal marks the task complete without checking whether the output answers the original goal.

## Why It Is Wrong

Tool execution is not verification. Runtime Skill output can be partial, stale, wrong, over-broad, or outside scope.

## Correct Behavior

The owner or verifier Pal checks returned evidence against acceptance criteria. Missing evidence remains `not-run`, `partial`, `fail`, or `blocked`.

## Corresponding Eval

`evals/orchestration/runtime-skill-aware-task-package-self-test.md`
