---
name: maintenance-report-writer
description: Use this skill when you need to 把系统维护、安装配置、故障排查和执行层结果整理成用户可读的维护报告。
---

# maintenance-report-writer

## Purpose

把系统维护、安装配置、故障排查和执行层结果整理成用户可读的维护报告。

## When to use

- 一次系统任务结束。
- 需要记录修复路径、风险和后续建议。
- 需要从当前 contacts / registry 解析合适协作对象逐案补充 或用户继续处理。

## Inputs

- 任务目标。
- 执行层摘要。
- evidence 审查结论。
- 未完成项、风险和后续建议。

## Process

1. 概括任务和结果。
2. 列出证据。
3. 标注未完成项和风险。
4. 给出是否建议写入记忆。
5. 给出下一步或协作 handoff。

## Outputs

Produce the structured output documented in README.md, but return it as a clean runtime-ready artifact instead of a copied template block.

## Boundaries

Not a fit:
- 任务还没有 evidence。
- 高风险操作未确认。

Risk boundary:
不包含密钥、私人日志全文或敏感路径细节。

Do not bypass approval, escalate privileges casually, or normalize destructive system actions.

## Evidence and handoff requirements

Any execution handoff must include target paths, permission needs, rollback or stop conditions, and evidence from version checks, logs, screenshots, or command output.

Reference acceptance hints:
- 用户能看懂当前状态。
- 证据和结论一一对应。
- 不夸大完成程度。

## Related files

- Runtime entry: skills/maintenance-report-writer/SKILL.md
- Human notes: skills/maintenance-report-writer/README.md
- Parent index: skills/index.md

通常在 `system-evidence-review` 之后使用。

