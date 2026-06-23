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

