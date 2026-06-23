---
name: metadata-indexing-plan
description: Use this skill when you need to 规划用文件名、路径、扩展名、大小、时间、hash 和摘要字段建立可重建索引。
---

# metadata-indexing-plan

## Purpose

规划用文件名、路径、扩展名、大小、时间、hash 和摘要字段建立可重建索引。

## When to use

建立资料目录索引、下载目录清单、归档目录盘点、重复候选分析。

## Inputs

授权路径、索引字段、刷新频率、是否允许 hash、是否允许摘要。

## Process

选字段；区分可缓存和不可保存内容；定义索引位置；设置敏感字段脱敏；定义刷新规则。

## Outputs

索引字段表、保存位置、刷新策略、隐私边界、evidence。

## Boundaries

Not a fit:
未经确认保存完整文件内容或完整私人文件列表。

Risk boundary:
长期保存完整路径清单可能泄露隐私。

Prefer preview, backup, privacy minimization, and reversible plans over direct destructive file operations.

## Evidence and handoff requirements

Require affected paths, preview or dry-run information when available, backup or restore expectations, and privacy handling notes for any sensitive files.

Reference acceptance hints:
索引可重建；不保存原文；敏感路径和内容受控。

## Related files

- Runtime entry: skills/metadata-indexing-plan/SKILL.md
- Human notes: skills/metadata-indexing-plan/README.md
- Parent index: skills/index.md

支持 file-search-handoff、duplicate-cleanup-plan。

