---
name: spreadsheet-task-plan
description: Use this skill when you need to 为 XLSX、CSV、TSV 的清洗、汇总、合并、校验和报告生成任务包。
---

# spreadsheet-task-plan

## Purpose

为 XLSX、CSV、TSV 的清洗、汇总、合并、校验和报告生成任务包。

## When to use

销售汇总、订单清洗、发票统计、多个 CSV 合并、异常值检查。

## Inputs

表格路径、表头样例、关键字段、汇总维度、输出格式、是否允许修改。

## Process

读取表头和样例行；识别字段类型；列出缺失/重复/异常；设计清洗与汇总；定义新产物。

## Outputs

表格结构、关键字段、数据质量问题、处理计划、产物和验收。

## Boundaries

Not a fit:
要求直接修改唯一原表；公式和金额结果无需复核。

Risk boundary:
编码、日期格式、公式、合并单元格和隐私字段可能造成误判。

Prefer preview, backup, privacy minimization, and reversible plans over direct destructive file operations.

## Evidence and handoff requirements

Require affected paths, preview or dry-run information when available, backup or restore expectations, and privacy handling notes for any sensitive files.

Reference acceptance hints:
保留原表；字段映射明确；金额、日期和公式有复核要求。

## Related files

- Runtime entry: skills/spreadsheet-task-plan/SKILL.md
- Human notes: skills/spreadsheet-task-plan/README.md
- Parent index: skills/index.md

常与 conversion-quality-review、file-privacy-risk-check 配合。

