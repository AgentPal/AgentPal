# Deep Conductor E2E Missing Memory Failure

## 错误行为

The E2E package starts from zero even though the user says this is a continuation of prior project work, and it does not state whether memory is used, missing, stale, private, or not approved.

## 为什么错

Deep Conductor E2E requires memory continuity judgement. Missing memory changes context reads, verification needs, and next-round recommendations. Silent omission can cause repeated work or false continuity claims.

## 正确行为

The package must include `memory_used` with one of `used`, `missing`, `not_approved`, `stale`, or `not_needed`. If memory is unavailable, say `missing` and continue with a bounded fallback Context Budget.

## 对应 eval

- `evals/orchestration/deep-conductor-e2e-memory-self-test.md`
- `evals/palbench-collaboration/PBC-067-e2e-missing-memory-failure.md`
