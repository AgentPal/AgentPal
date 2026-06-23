---
name: risk-assessment
description: Use this skill when you need to 识别产品、技术、安全、隐私、发布和高风险行业风险并分级。
---

# risk-assessment

## Purpose

识别产品、技术、安全、隐私、发布和高风险行业风险并分级。

## When to use

- 用户要求 Quinn 判断结果是否可以接受、发布、发送或交付。
- Agent / Runtime 返回完成声明，需要质量、风险或 evidence 复验。
- 需要把模糊风险、测试或验收要求整理成可执行清单。

## Inputs

原始目标、验收标准、交付物或完成报告、evidence、影响范围、风险约束、用户希望 Quinn 判断的问题。

## Process

1. 确认审查对象和任务边界。
2. 检查输入证据是否足以支持结论。
3. 识别风险、隐私、安全、回归和回滚缺口。
4. 输出结论、证据、风险、缺口和下一步。

## Outputs

Produce the structured output documented in README.md, but return it as a clean runtime-ready artifact instead of a copied template block.

## Boundaries

Not a fit:
- 要求 Quinn 直接修改代码、运行命令、安装依赖或发布上线。
- 要求 Quinn 替用户批准高风险动作。
- 没有目标、交付物或任何 evidence，且用户拒绝补充材料。

Risk boundary:
Quinn 只能审查、建议和生成任务包。涉及真实执行、修复、测试、发布、删除、外发或审批，应交给目标 Runtime、外部 Runtime、用户或专业 Pal，并要求返回 evidence。

## Evidence and handoff requirements

Do not accept a completion claim without evidence. Require acceptance criteria coverage, risk notes, affected scope, and missing proof if the claim is incomplete.

Reference acceptance hints:
- 结论明确，不把完成声明当作 evidence。
- 风险等级和原因可追溯。
- 缺口可被执行层补齐。
- 输出没有要求 Quinn 自己直接执行高风险动作。

## Related files

- Runtime entry: skills/risk-assessment/SKILL.md
- Human notes: skills/risk-assessment/README.md
- Parent index: skills/index.md

可调用 security-privacy-review、rollback-readiness-review 和 change-scope-review 的结果。

