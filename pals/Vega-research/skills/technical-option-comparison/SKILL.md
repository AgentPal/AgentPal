---
name: technical-option-comparison
description: Use this skill when you need to 比较多个技术方案或工具的适用场景、证据、风险和推荐方向。
---

# technical-option-comparison

## Purpose

比较多个技术方案或工具的适用场景、证据、风险和推荐方向。

## When to use

- 选择 Runtime、Agent、框架、数据库、桌面技术或搜索方案。
- 比较 Codex、Claude Code、OpenHands 等外部执行层。
- 为合适协作对象提供事实材料。

## Inputs

- 候选方案。
- 项目目标。
- 约束条件。
- 已有来源。
- 决策维度。

## Process

1. 定义比较维度。
2. 为每个方案收集官方资料和第三方资料。
3. 标注适用场景、优点、缺点、复杂度、维护成本和安全风险。
4. 检查 License、依赖、版本变化和边界冲突。
5. 给出 Vega 的资料判断。
6. 标注需要合适协作对象继续判断的工程问题。

## Outputs

Produce the structured output documented in README.md, but return it as a clean runtime-ready artifact instead of a copied template block.

## Boundaries

Not a fit:
- 直接做工程最终决策。
- 不查官方资料就下结论。
- 要求 Vega 生成实现方案或改代码。

Risk boundary:
Vega 负责来源和方案事实，不替合适协作对象做工程最终判断。

Keep source time visible. Do not present guesses, stale information, or single-source claims as settled fact.

## Evidence and handoff requirements

Separate facts, inferences, recommendations, and uncertainty. Include source type, source time, freshness needs, and any gaps that still require verification.

Reference acceptance hints:
- 每个方案有来源和时间。
- 事实判断与工程判断分开。
- 不确定项被列出。
- 能请从 contacts / registry 解析出的合适协作对象逐案补充下一步工程判断。

## Related files

- Runtime entry: skills/technical-option-comparison/SKILL.md
- Human notes: skills/technical-option-comparison/README.md
- Parent index: skills/index.md

对应 `runbooks/technical-research/technology-selection.md`，通常接 `research-brief-writer`。

