# Rhea Workflows Index

Rhea v0.1 内置一个正式 Workflow：

| id | path | purpose |
|---|---|---|
| system-maintenance-lifecycle | `workflows/system-maintenance-lifecycle/` | 从问题接入、范围划定、只读检测、风险审查、审批、执行层交接、evidence 审查、报告和记忆候选的系统维护闭环 |

Workflow 不直接执行命令、安装、卸载、删除或系统写入。真实执行交给 Runtime 或外部 Runtime，Rhea 负责计划、边界、审批和复验。

## R04 System / Runtime Safety Lead Workflows

- `runtime-safety-intake-workflow.md`
- `no-code-boundary-review-workflow.md`
- `high-risk-operation-approval-workflow.md`
- `environment-troubleshooting-workflow.md`
- `release-safety-review-workflow.md`
- `evidence-review-workflow.md`
- `incident-review-workflow.md`
- `collaboration-with-default-pals.md`


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
