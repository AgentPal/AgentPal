---
name: requirement-to-agent-task
description: Use this skill when you need to 把需求、Bug 或技术问题转成 Codex、Claude Code、OpenHands、Kimi、DeepSeek、Gemini CLI 等执行层可复制执行的开发任务提示词。
---

# requirement-to-agent-task

## Purpose

把需求、Bug 或技术问题转成 Codex、Claude Code、OpenHands、Kimi、DeepSeek、Gemini CLI 等执行层可复制执行的开发任务提示词。

## When to use

- 用户已有清楚目标，希望交给执行层开发。
- 产品说明需要转成工程任务。
- Bug 分析后需要形成修复任务。
- 弱模型或低成本模型需要更完整的任务约束。

## Inputs

- 目标。
- 背景和必读资料。
- 仓库路径。
- 修改范围。
- 禁止事项。
- 验收标准。
- 可用 Runtime、模型、推理强度、Skill、插件和工具。

## Process

1. 压缩目标为清楚的开发目标。
2. 列出必读资料和文件范围。
3. 明确本轮只做什么、不做什么。
4. 选择建议 Runtime、模型和推理强度。
5. 写入测试建议、风险、完成报告格式和 evidence 要求。
6. 对弱模型补充更具体的步骤、文件范围和停止条件。

## Outputs

Produce the structured output documented in README.md, but return it as a clean runtime-ready artifact instead of a copied template block.

## Boundaries

Not a fit:
- 产品范围未定。
- 没有仓库或文件范围。
- 用户要求绕过审批或直接执行高风险动作。

Risk boundary:
任务提示词不得要求执行层越权、绕过审批、安装未知依赖、删除文件或直接发布到远程仓库。高风险动作必须拆成计划和审批步骤。

## Evidence and handoff requirements

Require a bounded handoff with changed files, test results or reasons skipped, evidence artifacts, and a clear final verification statement.

## Related files

- Runtime entry: skills/requirement-to-agent-task/SKILL.md
- Human notes: skills/requirement-to-agent-task/README.md
- Parent index: skills/index.md

- 使用 `context-engineering` 准备上下文。
- 使用 `test-plan-writer` 补验收。
- 使用 `security-and-hardening` 补安全边界。

