---
name: command-plan-review
description: Use this skill when you need to 把执行层计划运行的命令或动作翻译成人能理解的影响、风险、审批点和证据要求。
---

# command-plan-review

## Purpose

把执行层计划运行的命令或动作翻译成人能理解的影响、风险、审批点和证据要求。

## When to use

- Runtime 准备运行命令。
- 用户贴来脚本或命令想判断是否安全。
- 需要比较只读检测和写入修复。

## Inputs

- 命令摘要或动作计划。
- 目标系统和工作目录。
- 预计影响路径。
- 来源和执行理由。

## Process

1. 解释命令大概做什么。
2. 区分只读、写入、安装、删除、外发数据。
3. 标记风险和审批需求。
4. 建议更低风险替代方案。
5. 定义执行后 evidence。

## Outputs

Produce the structured output documented in README.md, but return it as a clean runtime-ready artifact instead of a copied template block.

## Boundaries

Not a fit:
- 要求 Rhea 生成危险命令并鼓励直接执行。
- 混淆、未知、不可解释的脚本。

Risk boundary:
不直接运行、不代替审批、不输出一键破坏性命令。

Do not bypass approval, escalate privileges casually, or normalize destructive system actions.

## Evidence and handoff requirements

Any execution handoff must include target paths, permission needs, rollback or stop conditions, and evidence from version checks, logs, screenshots, or command output.

Reference acceptance hints:
- 用户能理解命令影响。
- 高风险动作不被轻描淡写。
- 未知来源脚本默认不建议执行。

## Related files

- Runtime entry: skills/command-plan-review/SKILL.md
- Human notes: skills/command-plan-review/README.md
- Parent index: skills/index.md

与 `permission-risk-review`、`approval-request-writer`、`system-evidence-review` 连用。

