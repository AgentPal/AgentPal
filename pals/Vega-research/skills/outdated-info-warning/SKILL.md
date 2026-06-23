---
name: outdated-info-warning
description: Use this skill when you need to 判断某条信息是否可能已经过期，并提醒用户重新验证。
---

# outdated-info-warning

## Purpose

判断某条信息是否可能已经过期，并提醒用户重新验证。

## When to use

- 软件版本、安装方式、API 文档。
- GitHub 项目活跃度。
- 价格、政策法规、模型能力。
- Agent 支持方式、依赖版本、市场趋势。

## Inputs

- 信息内容。
- 来源时间。
- 变化频率。
- 影响范围。
- 用户决策用途。

## Process

1. 判断领域变化频率。
2. 检查来源发布时间和更新时间。
3. 判断过期会影响什么。
4. 建议刷新查询的来源。
5. 标注不能直接作为当前事实。

## Outputs

Produce the structured output documented in README.md, but return it as a clean runtime-ready artifact instead of a copied template block.

## Boundaries

Not a fit:
- 稳定历史事实。
- 已有最新官方来源且时间明确。
- 用户不需要当前事实。

Risk boundary:
不能用旧记忆回答当前事实、价格、License、模型能力和项目维护状态。

Keep source time visible. Do not present guesses, stale information, or single-source claims as settled fact.

## Evidence and handoff requirements

Separate facts, inferences, recommendations, and uncertainty. Include source type, source time, freshness needs, and any gaps that still require verification.

Reference acceptance hints:
- 高变化领域被识别。
- 过期原因清楚。
- 给出刷新查证方向。
- 不把旧信息写成当前事实。

## Related files

- Runtime entry: skills/outdated-info-warning/SKILL.md
- Human notes: skills/outdated-info-warning/README.md
- Parent index: skills/index.md

与 `source-quality-check`、`research-brief-writer` 和 `knowledge-card-curator` 联动。

