---
name: writing-task-intake
description: Use this skill when you need to 判断用户要的是起草、改写、总结、翻译、润色、转格式、报告、邮件、文案还是对外沟通，并把模糊请求整理成可执行写作任务。
---

# writing-task-intake

## Purpose

判断用户要的是起草、改写、总结、翻译、润色、转格式、报告、邮件、文案还是对外沟通，并把模糊请求整理成可执行写作任务。

## When to use

- “帮我写一下”
- “帮我改一下这段话”
- “把这些资料整理成文档”
- “帮我写邮件 / 公告 / 产品介绍”

## Inputs

目标、素材、目标读者、渠道、语气、长度、截止要求、事实来源、风险边界。

## Process

1. 识别任务类型。
2. 判断目标读者和渠道。
3. 检查资料是否足够。
4. 标记事实、隐私、承诺和敏感风险。
5. 选择后续 Skill / Runbook / Pal 协作。

## Outputs

Produce the structured output documented in README.md, but return it as a clean runtime-ready artifact instead of a copied template block.

## Boundaries

Not a fit:
- 用户要求直接发送、发布或上传。
- 用户要求编造事实、数据、引用。
- 缺少资料却要求写成确定事实。

Risk boundary:
不把模糊素材写成确定事实；高风险沟通建议补 evidence 或从当前 contacts / registry 解析合适风险协作对象 类 Pal 审查。

Do not fabricate facts, sources, quotes, or current information.

## Evidence and handoff requirements

When facts matter, require the source list or source summary. Call out unsupported claims, missing citations, and any facts that must be refreshed before publication.

Reference acceptance hints:
任务类型清楚，缺口明确，后续路径可执行，风险不被隐藏。

## Related files

- Runtime entry: skills/writing-task-intake/SKILL.md
- Human notes: skills/writing-task-intake/README.md
- Parent index: skills/index.md

通常作为入口，路由到 `audience-and-tone-analysis`、`draft-writer`、`rewrite-and-edit` 或具体 Runbook。

