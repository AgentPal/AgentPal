---
name: search-query-design
description: Use this skill when you need to 帮助 Vega 为 Runtime 或外部 Runtime 设计高质量搜索查询，而不是只搜索一个泛词。
---

# search-query-design

## Purpose

帮助 Vega 为 Runtime 或外部 Runtime 设计高质量搜索查询，而不是只搜索一个泛词。

## When to use

- 查 GitHub 项目。
- 查竞品、官方文档、最新发布、报错线索或维护状态。
- 需要反证搜索或时间限定搜索。

## Inputs

- 研究问题。
- 核心实体。
- 同义词或英文名。
- 来源类型。
- 时间范围。
- 反证方向。

## Process

1. 抽取核心实体。
2. 补充同义词、中英文关键词和版本词。
3. 拆成事实查询、对比查询、反证查询、时间查询。
4. 按来源限定站点或类型。
5. 给每组查询标注目的。

## Outputs

Produce the structured output documented in README.md, but return it as a clean runtime-ready artifact instead of a copied template block.

## Boundaries

Not a fit:
- 用户已经提供足够来源。
- 不允许使用外部搜索。
- 涉及用户隐私或内部资料，且未确认能外发。

Risk boundary:
Vega 不直接执行搜索。搜索式只是交给 Runtime 或外部 Runtime 的任务包。

Keep source time visible. Do not present guesses, stale information, or single-source claims as settled fact.

## Evidence and handoff requirements

Separate facts, inferences, recommendations, and uncertainty. Include source type, source time, freshness needs, and any gaps that still require verification.

Reference acceptance hints:
- 查询组覆盖主要来源类型。
- 每个查询有明确目的。
- 包含反证和风险方向。
- 不泄露用户敏感资料。

## Related files

- Runtime entry: skills/search-query-design/SKILL.md
- Human notes: skills/search-query-design/README.md
- Parent index: skills/index.md

由 `deep-research-plan` 调用，结果交给 `source-quality-check` 和 `evidence-table-builder`。

