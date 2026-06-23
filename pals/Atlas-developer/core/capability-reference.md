# Capability Reference

This embedded Pal capability reference is not a route map.

No hard-coded semantic routing. Owner selection, collaborator selection, runtime selection, and collaboration-shape decisions are made case-by-case by AI judgement from the current request, context, registered Pal ownership scopes, available assets, risk, and user constraints.

## Source: agent-capability-matrix.md

# non-Pal runtime Capability Matrix

| agent | runtime | good for | not good for | last_checked | confidence |
|---|---|---|---|---|---|
| Codex thread | codex | 仓库级开发、多文件修改、测试修复 | 产品范围定义、无边界大重构 | unknown | unknown |
| Claude Code session | claude-code | 长上下文理解、复杂项目交接 | 无验收标准的直接执行 | unknown | unknown |
| OpenHands worker | openhands | 自动化开发执行 | 高风险无审批任务 | unknown | unknown |
| Gemini CLI | gemini-cli | 命令行辅助、代码检查 | 未确认工具权限任务 | unknown | unknown |
| DeepSeek-TUI | deepseek-tui | 低成本明确任务 | 开放式架构判断 | unknown | unknown |

外部 Runtime 不是 Pal，不进入 `contacts/`。

## Source: model-capability-matrix.md

# Model Capability Matrix

| level | use | avoid |
|---|---|---|
| strong | 规划、拆分、架构判断、失败诊断、最终复验 | 简单机械任务默认使用 |
| medium | 常规实现、文档、测试补齐、普通 Bug 修复 | 重大安全和架构决策 |
| low-cost | 明确范围、重复性、格式整理 | 开放式复杂判断 |

Atlas 记录的是能力画像，不是永久事实。模型能力随 Runtime 和配置变化，需要刷新。

## Source: plugin-capability-matrix.md

# Plugin Capability Matrix

本文件记录当前 Runtime 的插件、MCP、hooks、commands 和工具能力。

```text
name:
type: skill / plugin / mcp / hook / command / tool
runtime:
capability:
risk:
last_checked:
notes:
```

插件和 MCP 是执行资源，不是 Pal。

## Source: README.md

# Capabilities

本目录用于记录 Atlas 对 Runtime、模型、Skill、插件、MCP、工具和外部 Runtime 的能力画像。

能力画像用于调度，不等于授权。真实执行仍由目标 Runtime 在其权限和审批流程内完成。

## Source: skill-capability-matrix.md

# Skill Capability Matrix

| skill | capability |
|---|---|
| developer-task-intake | 判断开发任务是否成立 |
| requirement-to-agent-task | 生成执行层任务提示词 |
| multi-thread-agent-dispatch | 拆分多线程开发任务 |
| repository-handoff | 准备仓库交接 |
| execution-evidence-review | 复验执行层 evidence |
| debugging-and-error-recovery | Bug 分析与错误恢复 |
| code-review-and-quality | 工程侧质量审查 |

外部 Skill 先进入 `imports/skills/`，经过索引和风险检查后再考虑提升。

## Source: task-routing-matrix.md

# Atlas Capability Consideration Matrix

This file is a capability reference, not a route map.

No hard-coded semantic routing. AI judgement is required case-by-case before selecting a runtime, Pal collaborator, model, or execution path.

| situation | possible capability to consider | model / reasoning | evidence |
|---|---|---|---|
| 需求转开发任务 | development-oriented planning capability | high | 任务提示词、验收标准 |
| 明确文件范围实现 | coding runtime or non-Pal runtime candidate | medium | changed files、测试结果 |
| 多线程拆分 | development planning plus strong reasoning | high | 线程边界、冲突检查 |
| Bug 定位 | development perspective plus execution evidence | medium/high | 复现、日志、修复测试 |
| 架构边界判断 | strong reasoning and evidence review | high/xhigh | 风险说明、替代方案 |
| evidence 复验 | development evidence review | high | evidence 结论 |
| 格式整理 | bounded low-cost execution candidate | low/medium | diff、抽样检查 |

真实执行前必须确认 Runtime 权限和工具能力。



