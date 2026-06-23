---
name: announcement-writer
description: Use this skill when you need to 撰写产品更新公告、用户通知、变更说明、延期说明、社区公告和内部通知。
---

# announcement-writer

## Purpose

撰写产品更新公告、用户通知、变更说明、延期说明、社区公告和内部通知。

## When to use

- 产品更新、功能发布、维护通知。
- 延期、变更、限制说明。
- 对用户或团队的正式说明。

## Inputs

公告对象、事件、影响范围、时间、用户需要做什么、来源、限制、风险审查要求。

## Process

1. 明确事实和影响范围。
2. 先说结论，再补背景。
3. 写清用户需要做什么。
4. 避免过度承诺。
5. 标出发布前检查项。

## Outputs

Produce the structured output documented in README.md, but return it as a clean runtime-ready artifact instead of a copied template block.

## Boundaries

Not a fit:
- 未确认的发布时间、范围、影响和承诺。
- 危机公关最终定稿。

Risk boundary:
对外公告建议经事实来源和风险审查后再发布。

Do not fabricate facts, sources, quotes, or current information.

## Evidence and handoff requirements

When facts matter, require the source list or source summary. Call out unsupported claims, missing citations, and any facts that must be refreshed before publication.

Reference acceptance hints:
公告准确、可读、行动清楚、没有未确认事实或夸张承诺。

## Related files

- Runtime entry: skills/announcement-writer/SKILL.md
- Human notes: skills/announcement-writer/README.md
- Parent index: skills/index.md

与 `communication-risk-review` 和 `source-grounded-writing` 常连用。

