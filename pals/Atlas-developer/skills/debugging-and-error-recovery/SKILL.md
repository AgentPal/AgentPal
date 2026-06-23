---
name: debugging-and-error-recovery
description: Use this skill when you need to 把错误日志、失败截图、测试失败和用户描述转成可执行的最小修复任务。
---

# debugging-and-error-recovery

## Purpose

把错误日志、失败截图、测试失败和用户描述转成可执行的最小修复任务。

## When to use

- 构建失败。
- 测试失败。
- 页面或命令报错。
- 外部 Runtime 修复失败。
- 回归问题需要防复发。

## Inputs

- 失败现象。
- 错误日志、截图或堆栈。
- 最近修改范围。
- 复现步骤。
- 运行环境和依赖版本。
- 期望行为。

## Process

1. 复述失败现象。
2. 提取关键错误线索。
3. 判断可能影响范围。
4. 给出最小定位步骤。
5. 生成最小修复任务，不顺手重构。
6. 要求回归测试和防复发检查。
7. 如果环境不明，转交环境 Pal 或要求 Runtime 补环境信息。

## Outputs

Produce the structured output documented in README.md, but return it as a clean runtime-ready artifact instead of a copied template block.

## Boundaries

Not a fit:
- 没有任何错误信息且无法复现。
- 用户要求盲改。
- 问题本质是产品范围未定。

Risk boundary:
Atlas 不直接插入日志、运行程序或修改文件。需要真实调试时，生成 Debug Handoff 交给 Runtime，并要求 evidence。

## Evidence and handoff requirements

Require a bounded handoff with changed files, test results or reasons skipped, evidence artifacts, and a clear final verification statement.

Reference acceptance hints:
- 修复任务范围最小。
- 有复现和回归路径。
- 不把不相关重构混入修复。

## Related files

- Runtime entry: skills/debugging-and-error-recovery/SKILL.md
- Human notes: skills/debugging-and-error-recovery/README.md
- Parent index: skills/index.md

- 可转入 `runbooks/debugging/agent-debug-handoff.md`。
- 使用 `test-plan-writer` 补回归路径。
- 使用 `execution-evidence-review` 复验调试结果。

