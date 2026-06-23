---
name: execution-evidence-review
description: Use this skill when you need to 审查执行层返回的 evidence 是否足以支持“任务完成”。完成报告不等于完成。
---

# execution-evidence-review

## Purpose

审查执行层返回的 evidence 是否足以支持“任务完成”。完成报告不等于完成。

## When to use

- Codex / Claude Code / OpenHands 返回完成汇报。
- 多线程任务需要合并判断。
- 外部 Runtime 返回了修改摘要但证据不足。
- 需要判断是否进入下一轮修复。

## Inputs

- 原始任务说明。
- 验收标准。
- 执行层完成报告。
- affected paths。
- 测试结果。
- 产物路径、截图、日志或失败说明。

## Process

1. 对照原始目标和验收标准。
2. 检查 affected paths 是否在允许范围内。
3. 检查测试是否运行，未运行是否给出合理原因。
4. 检查是否有越权修改、敏感文件修改或高风险动作。
5. 检查是否只是口头声称完成。
6. 输出通过、需补证据、需返工或需人工复验。

## Outputs

Produce the structured output documented in README.md, but return it as a clean runtime-ready artifact instead of a copied template block.

## Boundaries

Not a fit:
- 没有原始任务说明。
- 没有任何执行报告。
- 用户要求跳过验收直接宣布完成。

Risk boundary:
Atlas 不能因为执行层自称完成就宣布完成。涉及安全、发布、数据或 UI 的任务，需要人工复验时必须说明。

## Evidence and handoff requirements

Require a bounded handoff with changed files, test results or reasons skipped, evidence artifacts, and a clear final verification statement.

Reference acceptance hints:
- 结论基于证据，不基于执行层自述。
- 缺失证据具体可补。
- 高风险越界被标出。

## Related files

- Runtime entry: skills/execution-evidence-review/SKILL.md
- Human notes: skills/execution-evidence-review/README.md
- Parent index: skills/index.md

- 使用 `test-plan-writer` 的测试计划做验收依据。
- 使用 `security-and-hardening` 检查高风险行为。
- 使用 `code-review-and-quality` 补质量审查。

