---
name: system-evidence-review
description: Use this skill when you need to 审查执行层返回的安装、卸载、修复、检测或配置结果是否足以证明任务完成。
---

# system-evidence-review

## Purpose

审查执行层返回的安装、卸载、修复、检测或配置结果是否足以证明任务完成。

## When to use

- Runtime 返回“已安装”。
- 外部 Runtime 返回修复报告。
- 命令计划执行后需要判断是否可信。

## Inputs

- 原始任务和验收标准。
- 执行摘要。
- 版本、路径、退出状态、日志、截图或验证输出摘要。
- 未完成项和失败项。

## Process

1. 对照原始任务。
2. 检查 evidence 是否覆盖验收标准。
3. 判断是否触碰禁止事项。
4. 标记完成、需补证据、需返工或需人工确认。
5. 给出下一步。

## Outputs

Produce the structured output documented in README.md, but return it as a clean runtime-ready artifact instead of a copied template block.

## Boundaries

Not a fit:
- 没有任何 evidence。
- 结果只是一句“完成了”。

Risk boundary:
不伪造验证结果，不代替执行层实际检查。

Do not bypass approval, escalate privileges casually, or normalize destructive system actions.

## Evidence and handoff requirements

Any execution handoff must include target paths, permission needs, rollback or stop conditions, and evidence from version checks, logs, screenshots, or command output.

Reference acceptance hints:
- 不把完成报告当完成。
- 缺证据时明确要求补证据。
- 高风险变化保留人工确认。

## Related files

- Runtime entry: skills/system-evidence-review/SKILL.md
- Human notes: skills/system-evidence-review/README.md
- Parent index: skills/index.md

最终连接 `maintenance-report-writer`。

