---
name: batch-file-organization
description: Use this skill when you need to 为批量分类、复制、移动、归档和目录整理生成低风险计划。
---

# batch-file-organization

## Purpose

为批量分类、复制、移动、归档和目录整理生成低风险计划。

## When to use

整理下载目录、桌面、项目资料、发票合同、素材库。

## Inputs

授权目录、目标结构、分类维度、是否保留原件、禁止目录、输出目录。

## Process

建立候选清单；分类；设计目录；生成 dry-run；列冲突和跳过项；等待确认。

## Outputs

目录结构、分类规则、迁移计划、预演清单字段、确认点。

## Boundaries

Not a fit:
直接全盘整理；直接删除或移动原文件；用户未指定禁止目录。

Risk boundary:
批量移动会破坏引用、项目结构和用户习惯，必须可回滚。

Prefer preview, backup, privacy minimization, and reversible plans over direct destructive file operations.

## Evidence and handoff requirements

Require affected paths, preview or dry-run information when available, backup or restore expectations, and privacy handling notes for any sensitive files.

Reference acceptance hints:
不直接改原件；有 old_path/new_path；冲突和敏感项单列。

## Related files

- Runtime entry: skills/batch-file-organization/SKILL.md
- Human notes: skills/batch-file-organization/README.md
- Parent index: skills/index.md

常接 naming-taxonomy-builder、file-privacy-risk-check。

