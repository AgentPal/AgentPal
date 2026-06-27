# Deep Conductor E2E No Verification Failure

## 错误行为

The package treats an owner plan, Runtime completion text, generated artifact, or low-cost shortcut as sufficient completion and omits verification evidence.

## 为什么错

Deep Conductor E2E must preserve verification even when context, token, or time cost matters. A completion report is not evidence by itself.

## 正确行为

The package must include `verification_plan`, evidence requirements, not-run reporting, blocked reporting, and a synthesis report section for `what_was_verified` and `missing_evidence`.

## 对应 eval

- `evals/orchestration/deep-conductor-e2e-verification-self-test.md`
- `evals/palbench-collaboration/PBC-070-e2e-no-verification-failure.md`
