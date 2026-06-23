---
name: architecture-review
description: Use this skill when you need to 检查开发方案、任务拆分或执行层结果是否破坏 AgentPal 的职责边界、模块分层和可维护性。
---

# architecture-review

## Purpose

检查开发方案、任务拆分或执行层结果是否破坏 AgentPal 的职责边界、模块分层和可维护性。

## When to use

- 任务涉及 Core、Pal、Runtime、Adapter、工具或通讯录边界。
- 执行层计划大范围重构。
- 用户要求把调度、执行、审批或记忆写入某个不合适层级。
- 代码审查中发现改动范围异常大。

## Inputs

- 方案或执行层完成报告。
- 相关目录和模块职责。
- 修改范围、禁止事项和验收标准。
- 任何涉及 Core / Pal / Runtime / Adapter 的改动说明。

## Process

1. 判断涉及哪些边界：Core、Pal、Runtime、Adapter、Skill、工具、通讯录。
2. 检查是否把 Core 做成 Planner、Router、Executor 或审批者。
3. 检查是否把 Pal 做成直接执行器。
4. 检查 Runtime / Adapter 是否越权写记忆、做规划或审批。
5. 检查是否过度设计、过度抽象或跨范围重构。
6. 给出风险、替代方案和验收建议。

## Outputs

Produce the structured output documented in README.md, but return it as a clean runtime-ready artifact instead of a copied template block.

## Boundaries

Not a fit:
- 纯文案或小格式修改。
- 没有架构影响的小范围补丁。
- 用户只需要测试计划或浏览器验证。

Risk boundary:
架构审查不能变成无边界重构建议。Atlas 应优先保护最小可验证改动和可回滚路径。

## Evidence and handoff requirements

Require a bounded handoff with changed files, test results or reasons skipped, evidence artifacts, and a clear final verification statement.

## Related files

- Runtime entry: skills/architecture-review/SKILL.md
- Human notes: skills/architecture-review/README.md
- Parent index: skills/index.md

- `code-review-and-quality` 发现结构风险时调用本 Skill。
- `security-and-hardening` 处理权限、凭据和高风险操作。
- `development-lifecycle` 在计划和 review 阶段调用本 Skill。

