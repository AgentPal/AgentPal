# Failure: Runtime Skill Profile Used As Fixed Route

## Wrong Behavior

A Skill profile says browser inspection is useful for page checks, so every page-related task is routed to a browser Skill automatically.

## Why It Is Wrong

Profiles are judgement inputs, not route tables. The user goal, owner Pal, current Runtime, privacy, and verification needs must be judged case by case.

## Correct Behavior

Name browser capability as a candidate only when it fits the task stage. Keep `not_a_fixed_route: true`.

## Corresponding Eval

`evals/orchestration/runtime-skill-orchestration-self-test.md`
