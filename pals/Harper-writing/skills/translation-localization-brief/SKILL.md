---
name: translation-localization-brief
description: Use this skill when you need to 把翻译或本地化需求整理成可执行交接包，并在能力范围内提供自然化表达草稿。
---

# translation-localization-brief

## Purpose

把翻译或本地化需求整理成可执行交接包，并在能力范围内提供自然化表达草稿。

## When to use

- 中英互译。
- 产品文案本地化。
- 技术说明面向普通用户自然化。
- 需要保留术语和品牌语气。

## Inputs

源文本、源语言、目标语言、目标地区、读者、渠道、术语表、保留词、语气。

## Process

1. 判断直译风险。
2. 保留原意和关键术语。
3. 生成自然表达版。
4. 标出术语和文化适配点。
5. 给出审校清单。

## Outputs

Produce the structured output documented in README.md, but return it as a clean runtime-ready artifact instead of a copied template block.

## Boundaries

Not a fit:
- 法律合同、医疗说明、财税文件等需专业翻译审校的最终文本。
- 未提供上下文却要求强本地化判断。

Risk boundary:
高风险专业文本需要专业审校，不由 Harper 直接定稿。

Do not fabricate facts, sources, quotes, or current information.

## Evidence and handoff requirements

When facts matter, require the source list or source summary. Call out unsupported claims, missing citations, and any facts that must be refreshed before publication.

Reference acceptance hints:
意思准确、语气自然、术语一致、风险已提示。

## Related files

- Runtime entry: skills/translation-localization-brief/SKILL.md
- Human notes: skills/translation-localization-brief/README.md
- Parent index: skills/index.md

可与 `style-guide-applier` 和 `communication-risk-review` 连用。

