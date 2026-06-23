---
name: file-search-handoff
description: Use this skill when you need to 生成元数据优先的文件搜索任务包，先找候选路径，不默认读取文件内容。
---

# file-search-handoff

## Purpose

生成元数据优先的文件搜索任务包，先找候选路径，不默认读取文件内容。

## When to use

按文件名、扩展名、时间、大小、目录范围搜索合同、发票、图片、下载文件。

## Inputs

搜索目标、授权目录、关键词、文件类型、时间范围、是否允许读取内容。

## Process

先路径和文件名；再扩展名、大小、时间；生成候选列表字段；必要时请求内容读取确认。

## Outputs

搜索目标、搜索范围、筛选条件、候选结果字段、下一步建议。

## Boundaries

Not a fit:
用户要求理解文件正文但未授权读取；全盘搜索敏感内容。

Risk boundary:
文件名相似不等于内容相关；搜索结果不得自动外发。

Prefer preview, backup, privacy minimization, and reversible plans over direct destructive file operations.

## Evidence and handoff requirements

Require affected paths, preview or dry-run information when available, backup or restore expectations, and privacy handling notes for any sensitive files.

Reference acceptance hints:
候选字段包含路径、文件名、类型、大小、修改时间和置信度；不越权。

## Related files

- Runtime entry: skills/file-search-handoff/SKILL.md
- Human notes: skills/file-search-handoff/README.md
- Parent index: skills/index.md

常与 metadata-indexing-plan、file-privacy-risk-check 配合。

