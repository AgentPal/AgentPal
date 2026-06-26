# Rhea Runbooks Index

Runbook 指导 Rhea 如何组织系统与应用任务，不直接执行命令、安装、卸载或系统写入。

## Built-In Runbooks

| id | path | purpose |
|---|---|---|
| agent-runtime-setup | `runbooks/runtime-setup/agent-runtime-setup.md` | 生成 Runtime / Agent 安装配置交接 |
| diagnose-dev-environment | `runbooks/environment/diagnose-dev-environment.md` | 生成开发环境只读诊断任务 |
| safe-installation-handoff | `runbooks/app-installation/safe-installation-handoff.md` | 生成安全软件安装 handoff |
| failed-command-recovery | `runbooks/recovery/failed-command-recovery.md` | 生成失败命令或安装失败后的恢复计划 |

所有 Runbook 都要求来源、时间、可信度、权限、回滚和 evidence。

## R04 System / Runtime Safety Lead Runbooks

- `no-code-boundary-check-runbook.md`
- `runtime-capability-check-runbook.md`
- `file-operation-risk-review-runbook.md`
- `release-preflight-risk-runbook.md`
- `rollback-readiness-runbook.md`
- `not-run-evidence-reporting-runbook.md`


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
