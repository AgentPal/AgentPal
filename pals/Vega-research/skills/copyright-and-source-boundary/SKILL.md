---
name: copyright-and-source-boundary
description: Use this skill when you need to 防止 Vega 把外部资料全文、付费内容、未授权材料或敏感资料直接写入公开包或长期知识库。
---

# copyright-and-source-boundary

## Purpose

防止 Vega 把外部资料全文、付费内容、未授权材料或敏感资料直接写入公开包或长期知识库。

## When to use

- 用户上传 PDF、报告、网页保存或文章。
- 准备把研究资料放进 `imports/`。
- 生成知识卡或研究简报。
- 准备公开发布 Pal Pack。

## Inputs

- 资料来源。
- License 或授权方式。
- 内容类型。
- 是否付费或私密。
- 保存目标。

## Process

1. 判断是否可公开再分发。
2. 区分可保存摘要与不可保存全文。
3. 标注原始 License、NOTICE 或来源要求。
4. 检查是否涉及隐私、凭据或商业机密。
5. 给出保存、索引、摘要或拒绝建议。

## Outputs

Produce the structured output documented in README.md, but return it as a clean runtime-ready artifact instead of a copied template block.

## Boundaries

Not a fit:
- 用户只问公开来源的简短摘要。
- 来源已经明确允许再分发，且仍需保留 License。

Risk boundary:
不能把第三方资料因为被 Vega 摘要就视为 MIT。无 License 或协议不明内容不应公开打包。

Keep source time visible. Do not present guesses, stale information, or single-source claims as settled fact.

## Evidence and handoff requirements

Separate facts, inferences, recommendations, and uncertainty. Include source type, source time, freshness needs, and any gaps that still require verification.

Reference acceptance hints:
- 无授权全文不进入公开包。
- 第三方 License 边界清楚。
- 私密资料不会发给外部 Runtime。
- 摘要和引用不过量。

## Related files

- Runtime entry: skills/copyright-and-source-boundary/SKILL.md
- Human notes: skills/copyright-and-source-boundary/README.md
- Parent index: skills/index.md

为 `knowledge-card-curator`、`imports/` 和 `THIRD_PARTY_NOTICES.md` 提供边界。

