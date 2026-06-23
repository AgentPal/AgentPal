---
name: humanizing-rewrite
description: Use this skill when you need to 减少模板腔、解释腔、过度总结、空泛形容词和对称段落，让文字更具体、更自然、更像真实编辑后的表达。
---

# humanizing-rewrite

## Purpose

减少模板腔、解释腔、过度总结、空泛形容词和对称段落，让文字更具体、更自然、更像真实编辑后的表达。

## When to use

- “这篇太像 AI 了”
- “改成人话”
- “少一点模板感”
- “更自然一点”

## Inputs

原文、读者、渠道、希望保留的意思、可删减范围、语气要求。

## Process

1. 标出模板感来源。
2. 删除空泛开头和万能结尾。
3. 把抽象表达改具体。
4. 调整句子节奏。
5. 说明改动重点。

## Outputs

Produce the structured output documented in README.md, but return it as a clean runtime-ready artifact instead of a copied template block.

## Boundaries

Not a fit:
- 规避检测或隐瞒机器生成来源。
- 把虚假内容包装得更可信。

Risk boundary:
目标是提高可读性，不是规避检测。

Do not fabricate facts, sources, quotes, or current information.

## Evidence and handoff requirements

When facts matter, require the source list or source summary. Call out unsupported claims, missing citations, and any facts that must be refreshed before publication.

Reference acceptance hints:
更自然、更具体、更符合读者需要，同时不损害事实准确性。

## Related files

- Runtime entry: skills/humanizing-rewrite/SKILL.md
- Human notes: skills/humanizing-rewrite/README.md
- Parent index: skills/index.md

对应 `runbooks/editing/humanize-and-polish.md`。

