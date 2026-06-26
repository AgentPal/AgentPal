# Runbooks Index

Runbook 是 Atlas 可复用的操作流程。它指导 Atlas 如何交接任务和审查结果，不直接执行命令。

## Built-In Runbooks

| id | path | purpose |
|---|---|---|
| agent-debug-handoff | `runbooks/debugging/agent-debug-handoff.md` | 把 Debug 子任务交给 Claude Code 或其他外部 Runtime，并审查 evidence |
| browser-verification-with-playwright | `runbooks/testing/browser-verification-with-playwright.md` | 把 UI 验收交给具备 Playwright / 浏览器能力的执行层 |
| small-bugfix | `runbooks/small-bugfix-runbook.md` | Package a narrow bug fix with reproduction, scope, and regression evidence. |
| feature-implementation | `runbooks/feature-implementation-runbook.md` | Move a bounded feature from acceptance criteria to runtime implementation evidence. |
| refactor-safety | `runbooks/refactor-safety-runbook.md` | Keep refactors small, behavior-preserving, and evidence-backed. |
| release-candidate-review | `runbooks/release-candidate-review-runbook.md` | Review RC/merge/publish readiness without claiming unsupported release state. |
| failed-test-triage | `runbooks/failed-test-triage-runbook.md` | Turn failed checks into investigation or repair packages. |

## Skill Coordination

- `debugging-and-error-recovery` 判断问题、提取线索，再使用 debug handoff runbook 交给执行层。
- `context-engineering` 准备外部 Runtime 需要的最小上下文包。
- `test-plan-writer` 写清回归测试、浏览器验证和截图 evidence。
- `security-and-hardening` 检查浏览器测试、日志、账号和真实数据风险。
- `execution-evidence-review` 根据 runbook 要求复验结果。

外部候选只有经过 License、安全和使用验证后，才可能改写为 Atlas Runbook。


## Context Loading Rule

Read this index only after this Pal is selected as owner, consultant, reviewer, or direct /pal Name target.

Use this index to choose the smallest relevant asset slice. Do not load every file in this directory by default.

Read assets here when:

- the current task requires this Pal's professional method;
- the output contract needs a specific skill, knowledge card, runbook, or workflow;
- the user asks which assets were used;
- an eval or release check is inspecting this Pal.

Do not read assets here when:

- Mira is only doing initial routing;
- another Pal owns the task and no consultation was requested;
- the task is ordinary chat, Codex generic, or Mira-owned team-leadership work;
- examples, evals, reports, memory, or future design material would be enough only by curiosity rather than task need.
