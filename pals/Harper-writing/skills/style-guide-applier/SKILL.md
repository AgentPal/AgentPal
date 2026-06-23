---
name: style-guide-applier
description: Use this skill when you need to 根据用户或项目提供的风格指南、术语表、禁用词和品牌语气统一文本。
---

# style-guide-applier

## Purpose

根据用户或项目提供的风格指南、术语表、禁用词和品牌语气统一文本。

## When to use

- 品牌文案统一。
- README、公告、邮件和说明文档风格一致。
- 用户提供样文或风格规则。

## Inputs

文本、风格指南、术语表、禁用词、目标读者、渠道、保留程度。

## Process

1. 读取风格规则。
2. 提取必须遵守的术语和禁用表达。
3. 改写文本。
4. 生成变更说明。
5. 标出无法判断的风格冲突。

## Outputs

Produce the structured output documented in README.md, but return it as a clean runtime-ready artifact instead of a copied template block.

## Boundaries

Not a fit:
- 未授权学习私人风格样本。
- 模仿特定在世作者或受版权保护的独特风格。

Risk boundary:
用户样文必须由用户提供或明确授权。

Do not fabricate facts, sources, quotes, or current information.

## Evidence and handoff requirements

When facts matter, require the source list or source summary. Call out unsupported claims, missing citations, and any facts that must be refreshed before publication.

Reference acceptance hints:
术语一致、语气一致、原意保留、未越过授权边界。

## Related files

- Runtime entry: skills/style-guide-applier/SKILL.md
- Human notes: skills/style-guide-applier/README.md
- Parent index: skills/index.md

常在 `rewrite-and-edit` 后使用，或与 `humanizing-rewrite` 合并执行。

