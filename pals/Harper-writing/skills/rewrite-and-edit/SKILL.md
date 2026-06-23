---
name: rewrite-and-edit
description: Use this skill when you need to 保留用户原意，调整结构、语气、清晰度、长度和读者适配。
---

# rewrite-and-edit

## Purpose

保留用户原意，调整结构、语气、清晰度、长度和读者适配。

## When to use

- “这段话帮我写清楚一点”
- “改得专业一点”
- “更适合客户看”
- “保留意思但不要这么硬”

## Inputs

原文、目标读者、渠道、想保留的意思、想改变的语气、长度要求。

## Process

1. 判断原文问题。
2. 保留核心意思。
3. 调整顺序和句子。
4. 删除重复和空泛表达。
5. 说明改动理由。

## Outputs

Produce the structured output documented in README.md, but return it as a clean runtime-ready artifact instead of a copied template block.

## Boundaries

Not a fit:
- 原文事实明显缺失且用户要求强化断言。
- 用户要求把虚假内容包装成可信事实。

Risk boundary:
不替用户增强未证实承诺，不把营销语气写成事实。

Do not fabricate facts, sources, quotes, or current information.

## Evidence and handoff requirements

When facts matter, require the source list or source summary. Call out unsupported claims, missing citations, and any facts that must be refreshed before publication.

Reference acceptance hints:
原意保留，表达更清楚，读者更容易理解，风险不被放大。

## Related files

- Runtime entry: skills/rewrite-and-edit/SKILL.md
- Human notes: skills/rewrite-and-edit/README.md
- Parent index: skills/index.md

可与 `audience-and-tone-analysis`、`humanizing-rewrite`、`style-guide-applier` 连用。

