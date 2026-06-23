---
name: knowledge-card-curator
description: Use this skill when you need to 把研究结果转成可写入系统层、Pal 层或项目层的知识卡候选。
---

# knowledge-card-curator

## Purpose

把研究结果转成可写入系统层、Pal 层或项目层的知识卡候选。

## When to use

- 调研结果未来会复用。
- 技术选型结论需要保留。
- GitHub 项目评估可作为后续参考。
- 研究结果需要由当前 AI / Mira / Brain 从 contacts / registry 解析合适审核对象。

## Inputs

- 研究简报。
- 来源摘要。
- 适用范围。
- 不确定项。
- 建议写入层级。

## Process

1. 判断写入位置：系统层、Pal 层或项目层。
2. 写标题和摘要。
3. 记录来源、更新时间、适用范围。
4. 写关键结论和不确定性。
5. 标注维护建议和审核人。

## Outputs

Produce the structured output documented in README.md, but return it as a clean runtime-ready artifact instead of a copied template block.

## Boundaries

Not a fit:
- 临时搜索结果。
- 未验证单一来源。
- 版权资料全文。
- 用户私人资料或敏感资料。

Risk boundary:
知识卡候选不是自动写入正式知识库。系统知识建议由当前 AI / Mira / Brain 按 contacts / registry 逐案选择审核对象。

Keep source time visible. Do not present guesses, stale information, or single-source claims as settled fact.

## Evidence and handoff requirements

Separate facts, inferences, recommendations, and uncertainty. Include source type, source time, freshness needs, and any gaps that still require verification.

Reference acceptance hints:
- 不保存版权全文。
- 来源和更新时间清楚。
- 适用范围明确。
- 不确定性未被抹掉。

## Related files

- Runtime entry: skills/knowledge-card-curator/SKILL.md
- Human notes: skills/knowledge-card-curator/README.md
- Parent index: skills/index.md

对应 `runbooks/knowledge/knowledge-card-creation.md`。

