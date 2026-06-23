---
name: system-task-intake
description: Use this skill when you need to 判断用户请求属于系统、应用、Runtime、依赖、权限、PATH、进程、磁盘、包导入还是故障恢复问题，并确定下一步是否只能先做只读检测。
---

# system-task-intake

## Purpose

判断用户请求属于系统、应用、Runtime、依赖、权限、PATH、进程、磁盘、包导入还是故障恢复问题，并确定下一步是否只能先做只读检测。

## When to use

- “软件打不开 / 装不上 / 删不掉。”
- “Codex / Claude Code / Gemini CLI 不可用。”
- “Node / Python / Git / .NET / Flutter 找不到。”
- “电脑变慢、磁盘满、某个进程占用高。”

## Inputs

- 用户描述。
- 操作系统和版本，如果可得。
- 软件、Runtime、命令、项目或错误摘要。
- 是否允许只读检测、管理员权限和外部 Runtime。

## Process

1. 识别问题类型。
2. 标记风险等级：只读、低风险、需要权限、高风险。
3. 判断缺失信息。
4. 决定下一步 Skill 或 Runbook。
5. 输出只读优先的建议。

## Outputs

Produce the structured output documented in README.md, but return it as a clean runtime-ready artifact instead of a copied template block.

## Boundaries

Not a fit:
- 用户要求 Rhea 直接运行命令。
- 纯代码实现、测试失败或架构问题，应由当前 owner 从 contacts / registry 逐案解析合适协作对象。
- 事实查证或工具来源研究，应咨询问从当前 contacts / registry 解析出的合适协作对象。

Risk boundary:
不能承诺已经检测或修复。不能要求用户直接复制危险命令。

Do not bypass approval, escalate privileges casually, or normalize destructive system actions.

## Evidence and handoff requirements

Any execution handoff must include target paths, permission needs, rollback or stop conditions, and evidence from version checks, logs, screenshots, or command output.

Reference acceptance hints:
- 问题类型明确。
- 没有把模糊问题直接变成修复命令。
- 风险等级和下一步检测路径清楚。

## Related files

- Runtime entry: skills/system-task-intake/SKILL.md
- Human notes: skills/system-task-intake/README.md
- Parent index: skills/index.md

通常作为入口，后续连接 `environment-diagnosis-plan`、`permission-risk-review`、`runtime-setup-handoff` 或 `app-installation-handoff`。

