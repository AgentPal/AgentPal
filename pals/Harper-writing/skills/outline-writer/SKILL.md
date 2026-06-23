---
name: outline-writer
description: Use this skill when you need to 把写作目标和资料整理成文章、报告、公告、产品介绍或演示大纲。
---

# outline-writer

## Purpose

把写作目标和资料整理成文章、报告、公告、产品介绍或演示大纲。

## When to use

- 先要结构再写全文。
- 资料很多，需要梳理顺序。
- 汇报、文章、PPT、说明文档。

## Inputs

目标、资料摘要、读者、渠道、长度、重点、证据、禁止事项。

## Process

1. 提炼主旨。
2. 选择结构：问题-方案、背景-发现-建议、先结论后解释等。
3. 安排章节和每节要点。
4. 标出需要证据的位置。
5. 给出后续写作任务包。

## Outputs

Produce the structured output documented in README.md, but return it as a clean runtime-ready artifact instead of a copied template block.

## Boundaries

Not a fit:
- 用户只需要一句短回复。
- 缺少目标读者和素材，且无法合理假设。

Risk boundary:
不把没有来源的判断写进结论性标题。

Do not fabricate facts, sources, quotes, or current information.

## Evidence and handoff requirements

When facts matter, require the source list or source summary. Call out unsupported claims, missing citations, and any facts that must be refreshed before publication.

Reference acceptance hints:
大纲逻辑清楚、顺序合理、证据缺口明确，可交给 `draft-writer`。

## Related files

- Runtime entry: skills/outline-writer/SKILL.md
- Human notes: skills/outline-writer/README.md
- Parent index: skills/index.md

常用于 `article-from-brief` 和 `source-based-draft` Runbook。

