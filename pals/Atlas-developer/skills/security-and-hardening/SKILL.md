---
name: security-and-hardening
description: Use this skill when you need to 在开发任务进入执行前或执行结果返回后，检查命令、依赖、文件、凭据、权限、外部写入和日志脱敏等安全边界。
---

# security-and-hardening

## Purpose

在开发任务进入执行前或执行结果返回后，检查命令、依赖、文件、凭据、权限、外部写入和日志脱敏等安全边界。

## When to use

- 任务涉及安装依赖、运行脚本、删除文件、移动目录或发布到远程仓库。
- 涉及 `.env`、token、API key、账号、权限或真实用户数据。
- 涉及外部服务写入、上传、发布、部署或自动审批。
- 执行层返回的改动触及安全敏感区域。

## Inputs

- 开发任务说明。
- 修改范围和执行动作。
- 可能运行的命令、脚本或依赖安装。
- 涉及的文件、配置、凭据和外部系统。
- 执行层 evidence。

## Process

1. 标记高风险动作：delete、install、shell、push、deploy、外部写入、权限变更。
2. 检查是否需要用户审批或更强 Runtime。
3. 检查敏感文件：`.env`、密钥、token、真实数据、日志。
4. 要求最小权限、最小范围和可回滚方案。
5. 将安全禁止事项写入执行层任务。
6. 复验执行层是否越权。

## Outputs

Produce the structured output documented in README.md, but return it as a clean runtime-ready artifact instead of a copied template block.

## Boundaries

Not a fit:
- 无任何安全影响的纯文档整理。
- 用户只要求产品讨论，尚未进入开发。
- 需要专业安全审计签收的高风险系统，本 Skill 只能做初步工程检查。

Risk boundary:
不要提供自动删除、自动安装、自动上传、自动部署或自动审批规则。不要让 Core / Adapter 承担执行或审批职责。

## Evidence and handoff requirements

Require a bounded handoff with changed files, test results or reasons skipped, evidence artifacts, and a clear final verification statement.

Reference acceptance hints:
- 高风险动作被明确标出。
- 敏感文件和外部写入有保护规则。
- 需要审批的事项不会被包装成普通任务。
- Atlas 不直接执行任何危险动作。

## Related files

- Runtime entry: skills/security-and-hardening/SKILL.md
- Human notes: skills/security-and-hardening/README.md
- Parent index: skills/index.md

- `developer-task-intake` 发现高风险时调用本 Skill。
- `architecture-review` 处理 Core / Runtime / Adapter 权限边界。
- `execution-evidence-review` 检查执行层是否触碰安全禁止事项。

