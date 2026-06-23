---
name: competitor-analysis
description: Use this skill when you need to 帮助用户比较同类产品、项目、工具或方案的定位、能力、差异、可学习点和不应照搬点。
---

# competitor-analysis

## Purpose

帮助用户比较同类产品、项目、工具或方案的定位、能力、差异、可学习点和不应照搬点。

## When to use

- 分析某个产品和 AgentPal 的区别。
- 找类似工具。
- 比较功能、用户、门槛和生态。
- 为合适产品协作对象 提供资料。

## Inputs

- 竞品对象。
- 比较目标。
- 目标用户。
- 需要关注的维度。
- 来源材料。

## Process

1. 区分官方介绍、第三方资料和用户反馈。
2. 提取目标用户、场景、功能范围、使用门槛、部署方式和商业模式。
3. 分析优点、缺点、生态能力和风险。
4. 对比 AgentPal 或用户项目。
5. 输出可学习点和不应照搬点。

## Outputs

Produce the structured output documented in README.md, but return it as a clean runtime-ready artifact instead of a copied template block.

## Boundaries

Not a fit:
- 投资级市场尽调。
- 需要商业机密或内部数据。
- 只看官网营销材料。

Risk boundary:
不提供投资、法律或商业决策最终结论。不把未经证实的用户反馈当事实。

Keep source time visible. Do not present guesses, stale information, or single-source claims as settled fact.

## Evidence and handoff requirements

Separate facts, inferences, recommendations, and uncertainty. Include source type, source time, freshness needs, and any gaps that still require verification.

Reference acceptance hints:
- 不只复述官网。
- 至少区分官方自述和第三方/用户反馈。
- 明确适用范围和不确定性。
- 给出可行动下一步。

## Related files

- Runtime entry: skills/competitor-analysis/SKILL.md
- Human notes: skills/competitor-analysis/README.md
- Parent index: skills/index.md

可调用 `source-quality-check`、`evidence-table-builder` 和 `research-brief-writer`。

