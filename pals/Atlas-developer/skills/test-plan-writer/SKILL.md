---
name: test-plan-writer
description: Use this skill when you need to 把开发任务转成可执行的测试计划、回归路径和 evidence 要求，让执行层知道怎么证明任务完成。
---

# test-plan-writer

## Purpose

把开发任务转成可执行的测试计划、回归路径和 evidence 要求，让执行层知道怎么证明任务完成。

## When to use

- 开发任务进入执行前，需要明确验收方式。
- Bug 修复需要回归测试。
- UI 或浏览器流程需要截图、trace 或手工步骤。
- 执行层返回结果但测试证据不足。

## Inputs

- 开发目标。
- 修改范围和禁止事项。
- 目标 Runtime 和可用测试工具。
- 已知风险、Bug 现象或用户路径。
- 需要自动测试、手工测试或浏览器验证的范围。

## Process

1. 明确要验证的行为。
2. 区分单元测试、集成测试、端到端测试、手工测试和浏览器验证。
3. 为每类测试写出输入、步骤、期望结果和失败记录方式。
4. 标出必须回归的旧行为。
5. 写清 evidence：命令结果、截图、日志、trace、changed files 或未运行测试原因。
6. 将测试任务交给 Runtime，不由合适协作对象 执行。

## Outputs

Produce the structured output documented in README.md, but return it as a clean runtime-ready artifact instead of a copied template block.

## Boundaries

Not a fit:
- 用户只在讨论产品方向，尚未形成开发目标。
- 没有仓库、模块、行为或验收目标。
- 用户要求 Atlas 自己运行测试。

Risk boundary:
不要把生产写操作、真实支付、真实消息发送、真实删除或真实用户数据测试写成默认动作。涉及外部系统时必须要求测试环境和用户确认。

## Evidence and handoff requirements

Require a bounded handoff with changed files, test results or reasons skipped, evidence artifacts, and a clear final verification statement.

Reference acceptance hints:
- 测试计划覆盖新行为、旧行为和失败路径。
- evidence 要求具体可检查。
- 没有要求 Atlas 直接运行命令。
- 未能测试的部分必须要求执行层说明原因。

## Related files

- Runtime entry: skills/test-plan-writer/SKILL.md
- Human notes: skills/test-plan-writer/README.md
- Parent index: skills/index.md

- `requirement-to-agent-task` 生成开发任务时调用本 Skill 补验收。
- `browser-verification-with-playwright` 处理浏览器路径。
- `execution-evidence-review` 根据本 Skill 的 evidence 要求复验结果。

