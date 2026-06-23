---
name: duplicate-cleanup-plan
description: Use this skill when you need to 生成重复文件候选和审查流程，不直接删除。
---

# duplicate-cleanup-plan

## Purpose

生成重复文件候选和审查流程，不直接删除。

## When to use

查找重复下载、重复图片、同名文档、多份导出表。

## Inputs

授权目录、候选规则、是否允许 hash、是否允许内容抽样、保留策略。

## Process

按名称/大小弱候选；hash 强候选；内容相似仅标弱候选；生成保留建议；等待确认。

## Outputs

候选表、证据强度、建议保留项、删除前备份/隔离方案、确认点。

## Boundaries

Not a fit:
仅凭文件名或大小判断并删除；清理系统目录或项目依赖。

Risk boundary:
相似文件可能是不同版本；删除不可逆。

Prefer preview, backup, privacy minimization, and reversible plans over direct destructive file operations.

## Evidence and handoff requirements

Require affected paths, preview or dry-run information when available, backup or restore expectations, and privacy handling notes for any sensitive files.

Reference acceptance hints:
不自动删除；证据强度清楚；每组候选有保留理由。

## Related files

- Runtime entry: skills/duplicate-cleanup-plan/SKILL.md
- Human notes: skills/duplicate-cleanup-plan/README.md
- Parent index: skills/index.md

必须接 file-privacy-risk-check 和 verification。

