---
name: multi-thread-agent-dispatch
description: Use this skill when you need to 把中大型开发任务拆成 2-4 个互不重叠的执行线程，供 Codex、Claude Code 或其他执行层并行处理。
---

# multi-thread-agent-dispatch

## Purpose

把中大型开发任务拆成 2-4 个互不重叠的执行线程，供 Codex、Claude Code 或其他执行层并行处理。

## When to use

- 任务涉及文档、模板、测试、代码审查等多个独立面。
- 一个执行窗口上下文过大。
- 用户希望多线程并行推进。
- 不同任务适合不同模型或推理强度。

## Inputs

- 总目标。
- 仓库路径。
- 全局必读资料。
- 可修改范围和禁止范围。
- 已知依赖顺序。
- 期望线程数量。
- 可用 Runtime、模型和工具能力。

## Process

1. 判断是否适合并行。
2. 按可闭环能力拆线程，不按字段、按钮或碎片需求机械拆分。
3. 每个线程设置独立目标、文件范围、禁止事项、验收标准和完成报告格式。
4. 避免两个线程修改同一文件区域。
5. 给每个线程建议模型、推理强度和任务长度。
6. 设置最终整合与复验线程。

## Outputs

Produce the structured output documented in README.md, but return it as a clean runtime-ready artifact instead of a copied template block.

## Boundaries

Not a fit:
- 单文件小修。
- 需求还没定范围。
- 必须严格串行执行的迁移。
- 多线程会争用同一核心文件。

Risk boundary:
不要把多个线程派到同一文件同一区域。不要让弱模型承担开放式架构判断。不要把高风险命令藏在线程任务里。

## Evidence and handoff requirements

Require a bounded handoff with changed files, test results or reasons skipped, evidence artifacts, and a clear final verification statement.

## Related files

- Runtime entry: skills/multi-thread-agent-dispatch/SKILL.md
- Human notes: skills/multi-thread-agent-dispatch/README.md
- Parent index: skills/index.md

- 使用 `context-engineering` 为每个线程准备上下文。
- 使用 `test-plan-writer` 为每个线程设置验收。
- 使用 `execution-evidence-review` 汇总复验。

