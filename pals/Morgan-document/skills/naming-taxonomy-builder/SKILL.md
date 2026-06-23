---
name: naming-taxonomy-builder
description: Use this skill when you need to 设计文件命名模板、分类法、版本规则、状态规则和冲突处理。
---

# naming-taxonomy-builder

## Purpose

设计文件命名模板、分类法、版本规则、状态规则和冲突处理。

## When to use

发票、合同、项目文件、图片、扫描件、报告统一命名。

## Inputs

文件类型、可用字段、日期来源、项目/客户/状态维度、示例文件名。

## Process

确定命名字段；保留扩展名；检查非法字符和长度；生成 old->new 对照表；标记冲突。

## Outputs

命名规则、分类法、改名前后对照字段、冲突处理、待确认项。

## Boundaries

Not a fit:
文件内容未知却要求从正文抽取敏感字段命名；要求直接改名。

Risk boundary:
名称可能泄露隐私；从文件内容抽字段需授权。

Prefer preview, backup, privacy minimization, and reversible plans over direct destructive file operations.

## Evidence and handoff requirements

Require affected paths, preview or dry-run information when available, backup or restore expectations, and privacy handling notes for any sensitive files.

Reference acceptance hints:
规则可解释；不会丢扩展名；冲突、空字段和敏感字段有处理策略。

## Related files

- Runtime entry: skills/naming-taxonomy-builder/SKILL.md
- Human notes: skills/naming-taxonomy-builder/README.md
- Parent index: skills/index.md

支撑 batch-file-organization、duplicate-cleanup-plan。

