---
name: vega-research-intake
description: Use this skill when you need to 判断用户请求属于哪类研究任务，明确研究深度、来源需求、输出形式和是否需要其他 Pal 协作。
---

# vega-research-intake

## Purpose

判断用户请求属于哪类研究任务，明确研究深度、来源需求、输出形式和是否需要其他 Pal 协作。

## When to use

- “帮我调研这个项目。”
- “有没有类似工具？”
- “这个技术方案靠谱吗？”
- “找几个 GitHub 仓库对比一下。”
- “总结这个方向的最新趋势。”

## Inputs

- 用户问题。
- 输出用途。
- 目标对象或比较对象。
- 时间新鲜度要求。
- 风险领域。
- 是否需要知识卡或 Pal handoff。

## Process

1. 判断研究类型：事实确认、深度调研、GitHub 项目评估、竞品分析、技术方案对比、市场调研、来源核查或知识库更新。
2. 判断研究深度：快速回答、轻量调研、深度研究或长期监控。
3. 检查是否需要追问研究对象、判断标准和输出用途。
4. 判断是否需要协作：产品、工程、知识维护、风险验收等协作对象均从当前 contacts / registry 逐案解析。
5. 生成研究入口结论。

## Outputs

Produce the structured output documented in README.md, but return it as a clean runtime-ready artifact instead of a copied template block.

## Boundaries

Not a fit:
- 用户只需要执行代码修改，应转给合适协作对象。
- 用户要求高风险专业最终建议。
- 用户要求 Vega 直接联网、爬取或下载资料。

Risk boundary:
不能把研究接入写成执行计划。不能承诺当前事实正确，除非后续来源已刷新查证。

Keep source time visible. Do not present guesses, stale information, or single-source claims as settled fact.

## Evidence and handoff requirements

Separate facts, inferences, recommendations, and uncertainty. Include source type, source time, freshness needs, and any gaps that still require verification.

Reference acceptance hints:
- 研究类型清楚。
- 来源需求和时间要求明确。
- 能指出是否需要其他 Pal。
- 不把模糊问题直接丢给搜索。

## Related files

- Runtime entry: skills/vega-research-intake/SKILL.md
- Human notes: skills/vega-research-intake/README.md
- Parent index: skills/index.md

接入后通常调用 `deep-research-plan`、`search-query-design` 或对应比较 Skill。

