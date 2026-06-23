---
name: research-brief-writer
description: Use this skill when you need to 把调研结果压缩成结论先行、证据清楚、能支持下一步行动的研究简报。
---

# research-brief-writer

## Purpose

把调研结果压缩成结论先行、证据清楚、能支持下一步行动的研究简报。

## When to use

- 技术选型简报。
- 开源项目评估报告。
- 竞品分析摘要。
- 给 suitable implementation collaborator 的资料结论。

## Inputs

- 研究问题。
- 证据表。
- 来源摘要。
- 不确定项。
- 用户目标。
- 后续接收方。

## Process

1. 先写结论。
2. 说明背景和问题。
3. 汇总主要发现。
4. 列出证据来源和不确定点。
5. 写风险、建议和下一步。
6. 生成知识卡候选。

## Outputs

Produce the structured output documented in README.md, but return it as a clean runtime-ready artifact instead of a copied template block.

## Boundaries

Not a fit:
- 证据不足却要求强结论。
- 对外发布的正式报告未经人工审查。
- 高风险专业最终建议。

Risk boundary:
研究简报不能伪装成最终专业意见。对外发布前需要人工确认来源和版权边界。

Keep source time visible. Do not present guesses, stale information, or single-source claims as settled fact.

## Evidence and handoff requirements

Separate facts, inferences, recommendations, and uncertainty. Include source type, source time, freshness needs, and any gaps that still require verification.

Reference acceptance hints:
- 结论和证据对应。
- 不确定项单独列出。
- 建议可执行。
- 适合交给下一步 Pal 或用户决策。

## Related files

- Runtime entry: skills/research-brief-writer/SKILL.md
- Human notes: skills/research-brief-writer/README.md
- Parent index: skills/index.md

通常接收 `evidence-table-builder`、`citation-summary` 和 `contradiction-and-uncertainty-check` 的结果。

