---
name: contradiction-and-uncertainty-check
description: Use this skill when you need to 防止 Vega 只找支持自己结论的来源，检查反证、来源冲突、时间冲突和过度推断。
---

# contradiction-and-uncertainty-check

## Purpose

防止 Vega 只找支持自己结论的来源，检查反证、来源冲突、时间冲突和过度推断。

## When to use

- 研究结论看起来过于单一。
- 多来源说法不一致。
- 资料时间跨度大。
- 需要给用户稳健建议。

## Inputs

- 候选结论。
- 证据表。
- 来源列表。
- 时间范围。
- 关键定义。

## Process

1. 查找反对证据。
2. 检查来源冲突。
3. 检查时间、地区、版本、平台差异。
4. 检查定义不一致。
5. 标记营销话术和过度推断。
6. 输出不确定项和继续验证建议。

## Outputs

Produce the structured output documented in README.md, but return it as a clean runtime-ready artifact instead of a copied template block.

## Boundaries

Not a fit:
- 没有来源可查。
- 用户只要创意发散。
- 用户要求无视反证。

Risk boundary:
不能为了让报告好看而隐藏不确定性。

Keep source time visible. Do not present guesses, stale information, or single-source claims as settled fact.

## Evidence and handoff requirements

Separate facts, inferences, recommendations, and uncertainty. Include source type, source time, freshness needs, and any gaps that still require verification.

Reference acceptance hints:
- 至少检查反证方向。
- 不确定性明确。
- 冲突来源不被强行合并。
- 给出下一步查证建议。

## Related files

- Runtime entry: skills/contradiction-and-uncertainty-check/SKILL.md
- Human notes: skills/contradiction-and-uncertainty-check/README.md
- Parent index: skills/index.md

通常在 `research-brief-writer` 前使用。

