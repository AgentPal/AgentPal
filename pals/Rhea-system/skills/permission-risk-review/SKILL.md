---
name: permission-risk-review
description: Use this skill when you need to 审查任务是否涉及管理员权限、sudo、系统目录、注册表、服务、启动项、安全软件、外发数据或敏感路径。
---

# permission-risk-review

## Purpose

审查任务是否涉及管理员权限、sudo、系统目录、注册表、服务、启动项、安全软件、外发数据或敏感路径。

## When to use

- 安装、卸载、删除、修改环境变量。
- 命令要求管理员权限。
- 任务涉及服务、驱动、注册表、系统目录。

## Inputs

- 计划执行动作。
- 影响路径和权限要求。
- 是否可回滚。
- 是否涉及凭据或用户数据。

## Process

1. 识别权限级别。
2. 标记影响范围。
3. 判断是否必须审批。
4. 要求备份或回滚计划。
5. 输出允许、暂停或拒绝建议。

## Outputs

Produce the structured output documented in README.md, but return it as a clean runtime-ready artifact instead of a copied template block.

## Boundaries

Not a fit:
- 纯只读检测且无敏感数据。
- 用户要求绕过审批。

Risk boundary:
不批准权限，不要求关闭安全机制，不指导破解或规避方法。

Do not bypass approval, escalate privileges casually, or normalize destructive system actions.

## Evidence and handoff requirements

Any execution handoff must include target paths, permission needs, rollback or stop conditions, and evidence from version checks, logs, screenshots, or command output.

Reference acceptance hints:
- 高风险动作被明确标记。
- 不绕过用户审批。
- 有回滚或停止条件。

## Related files

- Runtime entry: skills/permission-risk-review/SKILL.md
- Human notes: skills/permission-risk-review/README.md
- Parent index: skills/index.md

常与 `command-plan-review` 和 `approval-request-writer` 配合。

