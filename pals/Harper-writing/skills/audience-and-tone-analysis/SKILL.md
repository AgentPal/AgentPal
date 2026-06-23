---
name: audience-and-tone-analysis
description: Use this skill when you need to 判断文字写给谁、发到哪里、读者已知什么、希望读者读完后做什么，以及适合的语气强度。
---

# audience-and-tone-analysis

## Purpose

判断文字写给谁、发到哪里、读者已知什么、希望读者读完后做什么，以及适合的语气强度。

## When to use

- 对外公告、商务邮件、客户回复、产品介绍。
- 用户要求“更专业 / 更自然 / 更温和 / 更坚定”。
- 原文像内部说明，需要转成读者可理解表达。

## Inputs

目标读者、渠道、读者背景、沟通目标、原文、禁用表达、品牌或术语要求。

## Process

1. 定义读者与背景知识。
2. 定义沟通目标和行动号召。
3. 选择语气：正式、温和、坚定、自然、克制、外部发布。
4. 标出不适合的写法。
5. 给出写作策略。

## Outputs

Produce the structured output documented in README.md, but return it as a clean runtime-ready artifact instead of a copied template block.

## Boundaries

Not a fit:
- 事实来源不明但要求强结论。
- 需要法律、医疗、财税、金融最终判断。

Risk boundary:
不使用操控性话术、夸张承诺或假装了解读者未提供的背景。

Do not fabricate facts, sources, quotes, or current information.

## Evidence and handoff requirements

When facts matter, require the source list or source summary. Call out unsupported claims, missing citations, and any facts that must be refreshed before publication.

Reference acceptance hints:
读者、渠道、语气和风险边界清楚，能指导后续成稿。

## Related files

- Runtime entry: skills/audience-and-tone-analysis/SKILL.md
- Human notes: skills/audience-and-tone-analysis/README.md
- Parent index: skills/index.md

为 `outline-writer`、`draft-writer`、`email-and-message-writer`、`announcement-writer` 提供语气约束。

