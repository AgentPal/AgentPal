# Failure: Deep Conductor Missing Memory Writeback

## Wrong Behavior

After a project-level task finishes, the conductor summarizes the result but omits any Routing Memory or Runtime Skill usage candidate, so future judgement cannot learn from the outcome.

## Why Wrong

Deep Conductor's final step is a Routing Memory writeback candidate. The writeback must remain public-safe and non-binding, but the absence of a candidate loses useful evidence.

## Correct Behavior

The final report proposes a writeback candidate with topology, owner candidates, Runtime candidates, Runtime Skill candidates used or not-run, context counts, verification result, rework count, and a next-time suggestion marked `not_a_fixed_route`.

## Corresponding Eval

`evals/orchestration/conductor-memory-writeback-self-test.md`
