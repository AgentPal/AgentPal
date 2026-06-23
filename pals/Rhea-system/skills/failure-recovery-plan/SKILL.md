---
name: failure-recovery-plan
description: Use this skill when you need to 为失败命令、安装失败、依赖失败或环境修复失败生成可回滚、可复验的恢复计划。
---

# failure-recovery-plan

## Purpose

为失败命令、安装失败、依赖失败或环境修复失败生成可回滚、可复验的恢复计划。

## When to use

- 安装中断。
- 命令退出非零。
- PATH 修改后仍不可用。
- 工具升级后项目无法运行。

## Inputs

- 失败现象。
- 失败前动作。
- 错误摘要和日志位置。
- 已改动内容。
- 是否可回滚。

## Process

1. 记录失败前状态和已执行动作。
2. 判断是否应停止。
3. 生成低风险恢复检查。
4. 定义回滚或重试条件。
5. 要求新的 evidence。

## Outputs

Produce the structured output documented in README.md, but return it as a clean runtime-ready artifact instead of a copied template block.

## Boundaries

Not a fit:
- 没有失败信息或执行摘要。
- 要求无证据继续重试。

Risk boundary:
不删除未知目录，不清理用户资料，不覆盖配置。

Do not bypass approval, escalate privileges casually, or normalize destructive system actions.

## Evidence and handoff requirements

Any execution handoff must include target paths, permission needs, rollback or stop conditions, and evidence from version checks, logs, screenshots, or command output.

Reference acceptance hints:
- 不盲目重复失败命令。
- 先保护现状和用户数据。
- 恢复动作有验证条件。

## Related files

- Runtime entry: skills/failure-recovery-plan/SKILL.md
- Human notes: skills/failure-recovery-plan/README.md
- Parent index: skills/index.md

使用 `runbooks/recovery/failed-command-recovery.md`。

