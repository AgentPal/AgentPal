---
name: app-installation-handoff
description: Use this skill when you need to 为软件安装生成安全、可审批、可验证的执行层任务包。
---

# app-installation-handoff

## Purpose

为软件安装生成安全、可审批、可验证的执行层任务包。

## When to use

- 用户要安装开发工具或普通应用。
- 需要选择 WinGet、Scoop、Homebrew、官方安装包等方式。
- 安装前需要说明影响范围。

## Inputs

- 软件名称。
- 操作系统。
- 推荐来源或需要查证的来源。
- 是否允许包管理器、管理员权限或重启。

## Process

1. 确认软件和来源。
2. 检查是否已安装和可能冲突。
3. 选择低风险安装方式。
4. 说明会影响什么。
5. 生成执行层安装任务和验证要求。

## Outputs

Produce the structured output documented in README.md, but return it as a clean runtime-ready artifact instead of a copied template block.

## Boundaries

Not a fit:
- 破解软件、未知来源安装包、驱动自动安装或关闭安全软件。
- 用户要求 Rhea 直接安装。

Risk boundary:
不直接下载、安装、升级或覆盖旧版本。

Do not bypass approval, escalate privileges casually, or normalize destructive system actions.

## Evidence and handoff requirements

Any execution handoff must include target paths, permission needs, rollback or stop conditions, and evidence from version checks, logs, screenshots, or command output.

Reference acceptance hints:
- 安装方式有来源或待查证标记。
- 风险和审批点清楚。
- 验证包括版本、路径、启动状态或程序列表。

## Related files

- Runtime entry: skills/app-installation-handoff/SKILL.md
- Human notes: skills/app-installation-handoff/README.md
- Parent index: skills/index.md

使用 `runbooks/app-installation/safe-installation-handoff.md`，必要时调用 `permission-risk-review`。

