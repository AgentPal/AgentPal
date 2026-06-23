---
name: approval-request-writer
description: Use this skill when you need to 把需要用户确认的安装、卸载、删除、权限、环境变量或系统写入动作，写成清楚、可判断的审批请求。
---

# approval-request-writer

## Purpose

把需要用户确认的安装、卸载、删除、权限、环境变量或系统写入动作，写成清楚、可判断的审批请求。

## When to use

- 需要管理员权限。
- 需要安装或卸载软件。
- 需要修改 PATH、服务、启动项、系统设置。
- 需要连接外部工具或上传数据。

## Inputs

- 计划动作。
- 影响范围。
- 风险等级。
- 替代方案。
- 回滚方式。
- evidence 要求。

## Process

1. 用短句解释动作。
2. 写清会影响什么。
3. 写清为什么需要确认。
4. 写清可选方案。
5. 写清同意后执行层要返回什么。

## Outputs

Produce the structured output documented in README.md, but return it as a clean runtime-ready artifact instead of a copied template block.

## Boundaries

Not a fit:
- 试图绕过审批。
- 风险无法解释或来源不明。

Risk boundary:
不替用户点击、批准或输入凭据。

Do not bypass approval, escalate privileges casually, or normalize destructive system actions.

## Evidence and handoff requirements

Any execution handoff must include target paths, permission needs, rollback or stop conditions, and evidence from version checks, logs, screenshots, or command output.

Reference acceptance hints:
- 用户能看懂并做决定。
- 不诱导同意。
- 拒绝也有安全替代路径。

## Related files

- Runtime entry: skills/approval-request-writer/SKILL.md
- Human notes: skills/approval-request-writer/README.md
- Parent index: skills/index.md

通常由 `permission-risk-review` 或 `command-plan-review` 触发。

