---
name: pdf-task-plan
description: Use this skill when you need to 区分文本型、扫描型、混合型、表格密集型和表单 PDF，规划提取、OCR、转 Markdown 和复验。
---

# pdf-task-plan

## Purpose

区分文本型、扫描型、混合型、表格密集型和表单 PDF，规划提取、OCR、转 Markdown 和复验。

## When to use

PDF 转 Markdown、报告摘要、表格提取、扫描件 OCR、知识候选生成。

## Inputs

PDF 路径、目标输出、是否允许 OCR、是否需要表格、页码范围、敏感等级。

## Process

判断 PDF 类型；选择提取策略；保留页码和结构；标记低置信字段；输出候选而非正式知识。

## Outputs

PDF 类型判断、提取策略、输出结构、复验点、evidence 要求。

## Boundaries

Not a fit:
把 OCR 结果当最终事实；未经授权读取证件、合同或财税 PDF。

Risk boundary:
表格错位、OCR 误识别、页序错误和版权内容保存风险。

Prefer preview, backup, privacy minimization, and reversible plans over direct destructive file operations.

## Evidence and handoff requirements

Require affected paths, preview or dry-run information when available, backup or restore expectations, and privacy handling notes for any sensitive files.

Reference acceptance hints:
页码可追溯；扫描件标记 OCR 风险；敏感内容不长期保存。

## Related files

- Runtime entry: skills/pdf-task-plan/SKILL.md
- Human notes: skills/pdf-task-plan/README.md
- Parent index: skills/index.md

接 documents、conversion-quality-review、file-privacy-risk-check。

