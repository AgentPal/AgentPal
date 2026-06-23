---
name: deep-research-plan
description: Use this skill when you need to 把复杂研究任务拆成可执行的研究问题、子问题、来源计划、搜索计划和验证计划。
---

# deep-research-plan

## Purpose

把复杂研究任务拆成可执行的研究问题、子问题、来源计划、搜索计划和验证计划。

## When to use

- 全面了解一个领域。
- 比较多个方案。
- 判断某个项目是否值得接入 AgentPal。
- 做竞品分析或市场资料整理。

## Inputs

- 研究目标。
- 背景。
- 研究对象。
- 输出用途。
- 时间新鲜度。
- 必须验证的关键事实。

## Process

1. 定义研究问题。
2. 拆成子问题。
3. 设计来源类型：官方、GitHub、论文、媒体、用户反馈、社区、文档。
4. 设计搜索关键词和反证方向。
5. 设置信息新鲜度要求。
6. 设置必须验证的事实。
7. 规定输出形式。

## Outputs

Produce the structured output documented in README.md, but return it as a clean runtime-ready artifact instead of a copied template block.

## Boundaries

Not a fit:
- 单一事实确认且来源明确。
- 用户不需要研究，只需要执行。
- 研究目标、对象和用途完全不清。

Risk boundary:
研究计划不是结论。不能在来源执行前直接给强结论。

Keep source time visible. Do not present guesses, stale information, or single-source claims as settled fact.

## Evidence and handoff requirements

Separate facts, inferences, recommendations, and uncertainty. Include source type, source time, freshness needs, and any gaps that still require verification.

Reference acceptance hints:
- 子问题能被逐项查证。
- 来源类型覆盖一手、第三方、社区和反证。
- 明确哪些信息需要刷新。
- 明确最终产物。

## Related files

- Runtime entry: skills/deep-research-plan/SKILL.md
- Human notes: skills/deep-research-plan/README.md
- Parent index: skills/index.md

通常连接 `search-query-design`、`source-quality-check`、`evidence-table-builder` 和 `research-brief-writer`。

