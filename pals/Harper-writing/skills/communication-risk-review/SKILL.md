---
name: communication-risk-review
description: Use this skill when you need to 检查文本中的事实、来源、隐私、夸张承诺、敏感表达、版权和高风险专业边界。
---

# communication-risk-review

## Purpose

检查文本中的事实、来源、隐私、夸张承诺、敏感表达、版权和高风险专业边界。

## When to use

- 对外发布前。
- 邮件、公告、客户争议、投资人沟通。
- 产品能力、效果、价格、版本、License、API、模型能力相关表述。

## Inputs

待审文本、发布渠道、目标读者、资料来源、承诺清单、敏感信息边界。

## Process

1. 标出事实断言。
2. 检查来源和更新时间。
3. 检查隐私、版权、敏感信息。
4. 检查承诺是否过重。
5. 给出更稳表达和审查建议。

## Outputs

Produce the structured output documented in README.md, but return it as a clean runtime-ready artifact instead of a copied template block.

## Boundaries

Not a fit:
- 代替风险协作对象或法律顾问给最终风险签收。
- 没有文本或资料的抽象风险背书。

Risk boundary:
Harper 做表达风险初审，不做最终合规、法律或专业签收。

Do not fabricate facts, sources, quotes, or current information.

## Evidence and handoff requirements

When facts matter, require the source list or source summary. Call out unsupported claims, missing citations, and any facts that must be refreshed before publication.

Reference acceptance hints:
风险点可定位，替代表达更稳，需补 evidence 的项目明确。

## Related files

- Runtime entry: skills/communication-risk-review/SKILL.md
- Human notes: skills/communication-risk-review/README.md
- Parent index: skills/index.md

常作为 `draft-writer`、`announcement-writer`、`email-and-message-writer` 后置检查。

