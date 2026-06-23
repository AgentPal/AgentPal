# codex-completion-audit

## 用户请求

Codex 声称完成后，Quinn 审查 evidence。

## Quinn 的判断

结论：没有 evidence 时无法验收。执行策略：审查 affected files、命令输出、测试结果、失败项和风险。Handoff：退回 Codex 补充完成证据。模型建议：GPT-5.4-Codex，medium。Evidence：变更摘要、测试结果、失败/跳过项。

## 执行策略

Quinn 生成任务包、报告或 handoff，不直接执行命令。

## 验收标准

- 结论明确。
- evidence 要求明确。
- 不要求 Quinn 自己直接执行命令。
- 需要 handoff 时给出目标、范围、禁止事项和返回格式。
