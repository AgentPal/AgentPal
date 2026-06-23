---
name: source-grounded-writing
description: Use this skill when you need to 只基于用户提供资料或经当前 contacts / registry 解析出的合适协作对象提供的来源摘要写作，避免凭空补事实。
---

# source-grounded-writing

## Purpose

只基于用户提供资料或经当前 contacts / registry 解析出的合适协作对象提供的来源摘要写作，避免凭空补事实。

## When to use

- 基于调研简报写文章。
- 基于会议记录写报告。
- 基于产品方案写介绍。
- 基于资料生成用户说明。

## Inputs

资料清单、来源摘要、更新时间、可信度、可引用范围、目标文本类型、读者。

## Process

1. 区分资料事实、推断和建议。
2. 只使用可用资料写作。
3. 标出未覆盖问题。
4. 给出引用或来源提示。
5. 输出成稿和事实待确认清单。

## Outputs

Produce the structured output documented in README.md, but return it as a clean runtime-ready artifact instead of a copied template block.

## Boundaries

Not a fit:
- 无资料却要求当前事实、价格、版本、License、API 或模型能力判断。
- 要求伪造引用。

Risk boundary:
当前事实和可变信息必须刷新查询或标注可能过期。

Do not fabricate facts, sources, quotes, or current information.

## Evidence and handoff requirements

When facts matter, require the source list or source summary. Call out unsupported claims, missing citations, and any facts that must be refreshed before publication.

Reference acceptance hints:
所有关键事实可追溯，不伪造来源，不把推断写成事实。

## Related files

- Runtime entry: skills/source-grounded-writing/SKILL.md
- Human notes: skills/source-grounded-writing/README.md
- Parent index: skills/index.md

对应 `runbooks/source-grounded/source-based-draft.md`。

