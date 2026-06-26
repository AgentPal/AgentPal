---
name: source-quality-check
description: Use this skill when you need to 判断资料来源是否可信、是否新鲜、是否有偏见、是否适合引用。
---

# source-quality-check

## Purpose

判断资料来源是否可信、是否新鲜、是否有偏见、是否适合引用。

## When to use

- 多个来源结论不一致。
- 需要引用资料写报告。
- 来源可能是营销页、转载页或无日期内容。
- 涉及当前事实、价格、API、License 或项目状态。

## Inputs

- 来源标题。
- URL 或出处。
- 发布时间和更新时间。
- 作者或机构。
- 来源内容摘要。
- 支持的结论。

## Process

1. 分类来源：官方、一手、第三方评测、社区、营销、转载、未知。
2. 检查时间与版本适用性。
3. 检查作者身份和商业利益。
4. 检查是否提供证据。
5. 与其他来源交叉验证。
6. 标注支持什么结论和局限。

## Outputs

Produce the structured output documented in README.md, but return it as a clean runtime-ready artifact instead of a copied template block.

## Boundaries

Not a fit:
- 无来源材料。
- 用户要求无视来源。
- 要求保存版权全文。

Risk boundary:
来源质量评估不能替代专业审计。高风险领域只做资料整理和问题清单。

Keep source time visible. Do not present guesses, stale information, or single-source claims as settled fact.

## Evidence and handoff requirements

Separate facts, inferences, recommendations, and uncertainty. Include source type, source time, freshness needs, and any gaps that still require verification.

Reference acceptance hints:
- 每个来源有类型、时间和可信度。
- 不把营销材料当事实证据。
- 单一来源结论被标记为弱证据。
- 过期风险被指出。

## Related files

- Runtime entry: skills/source-quality-check/SKILL.md
- Human notes: skills/source-quality-check/README.md
- Parent index: skills/index.md

为 `evidence-table-builder`、`research-brief-writer` 和 `citation-summary` 提供来源评级。

