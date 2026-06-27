# Deep Conductor E2E No Context Budget Failure

## 错误行为

The package asks the Runtime to read the whole workspace, all Pal Packs, all memory, all examples, or every project file because the task is complex.

## 为什么错

E2E exists to control context, not expand it without reason. Broad reads risk private data exposure, token waste, and weaker verification.

## 正确行为

The package must include `context_budget_plan`, read tier, allowed context, forbidden context, escalation reasons, stop conditions, and `context_usage_report_required: true`.

## 对应 eval

- `evals/orchestration/deep-conductor-e2e-context-budget-self-test.md`
- `evals/palbench-collaboration/PBC-069-e2e-no-context-budget-failure.md`
