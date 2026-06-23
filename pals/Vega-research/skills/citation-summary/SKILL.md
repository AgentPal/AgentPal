---
name: citation-summary
description: Use this skill when you need to 把多个来源的关键事实整理成可引用摘要，保留来源、时间、支持程度和局限。
---

# citation-summary

## Purpose

把多个来源的关键事实整理成可引用摘要，保留来源、时间、支持程度和局限。

## When to use

- 写研究报告。
- 更新知识卡。
- 比较多个方案。
- 需要把来源交给其他 Pal。

## Inputs

- 来源标题。
- URL 或出处。
- 发布时间 / 更新时间 / 访问时间。
- 关键事实摘要。
- 支持的结论。

## Process

1. 提取关键事实。
2. 标注来源和时间。
3. 判断支持程度。
4. 记录局限和不确定性。
5. 避免复制版权全文。

## Outputs

Produce the structured output documented in README.md, but return it as a clean runtime-ready artifact instead of a copied template block.

## Boundaries

Not a fit:
- 保存全文。
- 复制长篇付费内容。
- 来源不明或不可引用。

Risk boundary:
引用摘要不等于取得再分发授权。不要保存版权资料全文。

Keep source time visible. Do not present guesses, stale information, or single-source claims as settled fact.

## Evidence and handoff requirements

Separate facts, inferences, recommendations, and uncertainty. Include source type, source time, freshness needs, and any gaps that still require verification.

Reference acceptance hints:
- 每条事实都有来源。
- 摘要短而清楚。
- 长引用和全文复制被避免。
- 时间和局限被标注。

## Related files

- Runtime entry: skills/citation-summary/SKILL.md
- Human notes: skills/citation-summary/README.md
- Parent index: skills/index.md

服务 `research-brief-writer`、`knowledge-card-curator` 和 handoff。

