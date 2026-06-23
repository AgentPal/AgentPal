---
name: evidence-table-builder
description: Use this skill when you need to 把研究材料整理成证据表，避免只给用户堆摘要或链接。
---

# evidence-table-builder

## Purpose

把研究材料整理成证据表，避免只给用户堆摘要或链接。

## When to use

- 多个来源结论不一致。
- 需要比较多个项目或方案。
- 需要判断技术方案是否靠谱。
- 需要输出可追溯研究简报。

## Inputs

- 研究问题。
- 来源列表。
- 来源质量评估。
- 候选结论。
- 反证或冲突来源。

## Process

1. 抽取候选结论。
2. 为每个结论列支持来源。
3. 查找反对来源或冲突来源。
4. 标注证据强度。
5. 写出不确定点。
6. 给出谨慎建议。

## Outputs

Produce the structured output documented in README.md, but return it as a clean runtime-ready artifact instead of a copied template block.

## Boundaries

Not a fit:
- 没有可引用来源。
- 只是自由头脑风暴。
- 用户要求直接跳到结论。

Risk boundary:
不能把无来源结论写成事实。证据表不是最终专业意见。

Keep source time visible. Do not present guesses, stale information, or single-source claims as settled fact.

## Evidence and handoff requirements

Separate facts, inferences, recommendations, and uncertainty. Include source type, source time, freshness needs, and any gaps that still require verification.

Reference acceptance hints:
- 每条结论可追溯到来源。
- 有反证或明确说明未找到反证。
- 证据强度不被夸大。
- 建议与证据强度匹配。

## Related files

- Runtime entry: skills/evidence-table-builder/SKILL.md
- Human notes: skills/evidence-table-builder/README.md
- Parent index: skills/index.md

依赖 `source-quality-check`，供 `research-brief-writer` 和 `contradiction-and-uncertainty-check` 使用。

