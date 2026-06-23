---
name: file-task-intake
description: Use this skill when you need to 判断文件、文档、表格、PDF、归档或办公自动化请求属于哪类任务，并决定澄清、规划、转交或风险提醒。
---

# file-task-intake

## Purpose

判断文件、文档、表格、PDF、归档或办公自动化请求属于哪类任务，并决定澄清、规划、转交或风险提醒。

## When to use

整理下载目录、处理一批 PDF、汇总表格、清理重复文件、批量命名、资料归档。

## Inputs

用户目标、路径或文件集合、期望输出、是否允许读取内容、是否允许修改、禁止路径。

## Process

分类任务类型；确认路径；判断是否需要读取内容；识别敏感和高风险操作；选择相关 Skill；输出执行层需求。

## Outputs

任务类型、当前还缺、风险判断、建议处理方式、是否需要执行层、确认点。

## Boundaries

Not a fit:
路径完全未知且用户拒绝限定范围；要求直接删除、覆盖或外发文件。

Risk boundary:
不能把模糊请求直接转成全盘扫描或真实修改。

Prefer preview, backup, privacy minimization, and reversible plans over direct destructive file operations.

## Evidence and handoff requirements

Require affected paths, preview or dry-run information when available, backup or restore expectations, and privacy handling notes for any sensitive files.

Reference acceptance hints:
任务类型清楚；缺失信息不超过 1-3 个关键问题；风险和执行边界明确。

## Related files

- Runtime entry: skills/file-task-intake/SKILL.md
- Human notes: skills/file-task-intake/README.md
- Parent index: skills/index.md

入口 Skill，可路由到全部 Morgan Skill。

