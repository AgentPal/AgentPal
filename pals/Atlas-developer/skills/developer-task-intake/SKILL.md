---
name: developer-task-intake
description: Use this skill when you need to 判断用户输入是否已经是合格开发任务，并决定下一步是补信息、转交其他 Pal，还是进入开发任务拆解。
---

# developer-task-intake

## Purpose

判断用户输入是否已经是合格开发任务，并决定下一步是补信息、转交其他 Pal，还是进入开发任务拆解。

## When to use

- 用户说“帮我开发一个功能”。
- 用户给出 Bug、截图、报错或失败日志。
- 用户要求“让 Codex / Claude Code 改一下”。
- 产品需求、技术问题和执行请求混在一起。

## Inputs

- 用户原始请求。
- 仓库路径或项目位置。
- 目标和期望结果。
- 修改范围和禁止事项。
- 验收标准、日志、截图或失败证据。

## Process

1. 判断输入类型：开发任务、产品需求、Bug、技术咨询、环境问题或高风险操作。
2. 检查是否有目标、范围、必读资料、禁止事项和验收标准。
3. 判断是否需要先由产品 Pal 定范围、环境 Pal 检查运行环境、QA Pal 做验收计划。
4. 标出高风险项：删除、安装、权限、凭据、发布、真实数据、Runtime Adapter 或 AgentPal Core 边界。
5. 输出是否可以进入执行层。

## Outputs

Produce the structured output documented in README.md, but return it as a clean runtime-ready artifact instead of a copied template block.

## Boundaries

Not a fit:
- 用户只是闲聊。
- 用户要求 Atlas 直接改文件或运行命令。
- 任务包含无授权高风险操作。

Risk boundary:
Atlas 不直接执行高风险动作。涉及删除、安装、权限、凭据、发布或真实数据时，必须停下并要求执行层审批或用户确认。

## Evidence and handoff requirements

Require a bounded handoff with changed files, test results or reasons skipped, evidence artifacts, and a clear final verification statement.

Reference acceptance hints:
- 判断类型明确。
- 缺口可补。
- 风险不被掩盖。
- 不把模糊产品需求直接交给执行层。

## Related files

- Runtime entry: skills/developer-task-intake/SKILL.md
- Human notes: skills/developer-task-intake/README.md
- Parent index: skills/index.md

- 任务合格后交给 `requirement-to-agent-task`。
- 高风险任务交给 `security-and-hardening` 检查。
- Debug 输入交给 `debugging-and-error-recovery`。

