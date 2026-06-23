---
name: office-template-fill
description: Use this skill when you need to 把用户数据和办公模板填充需求整理成可执行、可验收的任务包。
---

# office-template-fill

## Purpose

把用户数据和办公模板填充需求整理成可执行、可验收的任务包。

## When to use

用模板生成报告、合同草稿、会议纪要、发票清单或表单文档。

## Inputs

模板路径、数据来源、字段映射、输出目录、是否允许读取内容、审查人。

## Process

识别模板字段；映射数据；标记缺失字段；生成新文件计划；定义人工复核点。

## Outputs

字段映射表、缺失项、输出文件命名、复核清单、evidence。

## Boundaries

Not a fit:
自动生成法律/财税最终文件且无需人工审查；覆盖原模板。

Risk boundary:
错填姓名、金额、日期、条款会造成严重后果。

Prefer preview, backup, privacy minimization, and reversible plans over direct destructive file operations.

## Evidence and handoff requirements

Require affected paths, preview or dry-run information when available, backup or restore expectations, and privacy handling notes for any sensitive files.

Reference acceptance hints:
不覆盖模板；字段可追溯；敏感字段有最小化处理。

## Related files

- Runtime entry: skills/office-template-fill/SKILL.md
- Human notes: skills/office-template-fill/README.md
- Parent index: skills/index.md

接 document-processing-plan、spreadsheet-task-plan。

