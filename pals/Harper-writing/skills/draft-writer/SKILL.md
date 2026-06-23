---
name: draft-writer
description: Use this skill when you need to 根据确认过的目标、读者、资料和大纲生成可编辑初稿。
---

# draft-writer

## Purpose

根据确认过的目标、读者、资料和大纲生成可编辑初稿。

## When to use

- 文章、报告、公告、说明文档、产品介绍、邮件正文。
- 有资料或明确假设，可以先出草稿。

## Inputs

大纲、素材、读者、语气、长度、引用要求、事实待确认项、禁用表达。

## Process

1. 核对素材边界。
2. 选择开头和结构。
3. 写初稿。
4. 标出事实待确认项。
5. 给出下一步编辑建议。

## Outputs

Produce the structured output documented in README.md, but return it as a clean runtime-ready artifact instead of a copied template block.

## Boundaries

Not a fit:
- 资料不足却要求确定事实。
- 需要直接发布的高风险文本。

Risk boundary:
Harper 只输出草稿，不声称已发布或已发送。

Do not fabricate facts, sources, quotes, or current information.

## Evidence and handoff requirements

When facts matter, require the source list or source summary. Call out unsupported claims, missing citations, and any facts that must be refreshed before publication.

Reference acceptance hints:
初稿可读、结构完整、没有伪造来源，事实风险被标出。

## Related files

- Runtime entry: skills/draft-writer/SKILL.md
- Human notes: skills/draft-writer/README.md
- Parent index: skills/index.md

之后通常进入 `rewrite-and-edit`、`humanizing-rewrite` 或 `communication-risk-review`。

