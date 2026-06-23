---
name: file-privacy-risk-check
description: Use this skill when you need to 判断文件任务是否涉及证件、合同、财税、医疗、客户资料、凭据、私钥、账号和外发风险。
---

# file-privacy-risk-check

## Purpose

判断文件任务是否涉及证件、合同、财税、医疗、客户资料、凭据、私钥、账号和外发风险。

## When to use

敏感目录整理、合同发票处理、压缩包外发、文件摘要和索引。

## Inputs

文件类型、路径、任务动作、是否外发、是否压缩、是否长期保存、授权范围。

## Process

识别敏感类别；判断动作风险；最小化读取；建议排除/脱敏/单独确认；定义 evidence。

## Outputs

风险等级、敏感类别、受影响范围、建议做法、审批需求。

## Boundaries

Not a fit:
用户要求忽略隐私风险或保存敏感原文。

Risk boundary:
路径名、文件名、摘要本身也可能泄露隐私。

Prefer preview, backup, privacy minimization, and reversible plans over direct destructive file operations.

## Evidence and handoff requirements

Require affected paths, preview or dry-run information when available, backup or restore expectations, and privacy handling notes for any sensitive files.

Reference acceptance hints:
高风险操作有明确停点；敏感内容不进入长期记忆。

## Related files

- Runtime entry: skills/file-privacy-risk-check/SKILL.md
- Human notes: skills/file-privacy-risk-check/README.md
- Parent index: skills/index.md

所有高风险文件任务的前置或复验 Skill。

