---
name: conversion-quality-review
description: Use this skill when you need to 审查 PDF/DOCX/XLSX/PPTX/Markdown/CSV 等转换后的结构、内容、表格和引用质量。
---

# conversion-quality-review

## Purpose

审查 PDF/DOCX/XLSX/PPTX/Markdown/CSV 等转换后的结构、内容、表格和引用质量。

## When to use

PDF 转 Markdown 后复验、DOCX 转 PDF、XLSX 转 CSV、PPT 提纲提取。

## Inputs

源文件、转换产物、目标格式、抽样页/表/段、允许误差和验收标准。

## Process

比对结构；抽样内容；检查表格、页码、图片占位、编码和丢失项；给修复建议。

## Outputs

通过/不通过、问题清单、抽样证据、需重跑项、用户注意。

## Boundaries

Not a fit:
只看转换成功退出码就判定完成；版权内容无边界长期保存。

Risk boundary:
转换可能丢格式、丢公式、乱表格或改变语义。

Prefer preview, backup, privacy minimization, and reversible plans over direct destructive file operations.

## Evidence and handoff requirements

Require affected paths, preview or dry-run information when available, backup or restore expectations, and privacy handling notes for any sensitive files.

Reference acceptance hints:
有源与产物对应；关键字段、页码、表格和编码已检查。

## Related files

- Runtime entry: skills/conversion-quality-review/SKILL.md
- Human notes: skills/conversion-quality-review/README.md
- Parent index: skills/index.md

复验 document、spreadsheet、pdf 和 template 任务。

