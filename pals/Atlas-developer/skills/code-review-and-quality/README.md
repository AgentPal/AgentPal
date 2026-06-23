# code-review-and-quality

运行时 Skill 入口请看 SKILL.md；README.md 仅作为人类阅读说明。


中文名：代码审查与质量

## 用途

对执行层提交的改动做工程侧代码审查，关注行为、风险、边界和测试缺口。

## 适用场景

- 执行层返回 diff、摘要或 PR。
- 多线程结果需要质量收口。
- 用户希望判断是否可以进入发布前检查。
- 需要识别越界实现或过度复杂化。

## 不适合场景

- 没有 diff、文件清单或 evidence。
- 用户只需要产品文案润色。
- 高风险发布需要专门发布审查 Pal 最终签收。

## 输入信息

- 原始任务说明。
- diff 或 changed files。
- 测试结果。
- 项目规范和架构边界。
- 执行层完成报告。

## 处理流程

1. 先找可能的 bug、回归、越界和测试缺口。
2. 检查改动是否符合原始目标。
3. 检查是否超范围修改。
4. 检查复杂度、安全、性能和维护风险。
5. 给出按严重度排序的 findings。
6. 如果没有问题，说明剩余风险和未覆盖测试。

## 输出格式

```text
## Findings
## Open Questions
## Test Gaps
## Summary
```

## 验收标准

- findings 有文件或证据依据。
- 严重问题优先。
- 不把风格偏好伪装成 bug。
- 不因执行层自述而跳过测试缺口。

## 风险边界

Atlas 做工程侧初步审查，不替代最终 QA、发布审批或安全审计。没有 changed files 或 evidence 时不能判定通过。

## 与 Atlas 其他 Skill / Runbook 的关系

- `architecture-review` 处理结构边界。
- `security-and-hardening` 处理安全风险。
- `execution-evidence-review` 处理完成证据。

