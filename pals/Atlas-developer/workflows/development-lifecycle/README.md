# Development Lifecycle Workflow

这是 Atlas 自有开发生命周期 Workflow，用于把开发请求从模糊输入推进到可执行、可验证、可记忆的任务闭环。

## When To Use

- 用户提出新功能、Bug 修复、重构或发布前收口。
- 任务涉及多个文件、多个执行层或多个验收点。
- 用户希望 Atlas 生成 Codex / Claude Code / OpenHands 等执行层任务。

## Workflow

### 1. Intake

判断输入是否是开发任务。检查目标、仓库路径、修改范围、禁止事项、验收标准和风险。

如果需求不清，先补需求或转给产品 Pal。环境问题转给环境 Pal。高风险动作必须先停下并要求审批。

### 2. Define

把目标写成一段可验收的工程描述：

- 这轮要完成什么。
- 哪些文件、模块或行为在范围内。
- 哪些事情明确不做。
- 如何判断完成。

### 3. Plan

选择单线程、并行线程或外部 Runtime 交接。拆分时按可闭环能力拆，不按按钮、字段或零散文件机械拆。

每个子任务必须有独立目标、文件范围、禁止事项、验收标准、建议模型、推理强度和完成汇报格式。

### 4. Handoff

生成执行层任务包：

```text
目标
必读资料
修改范围
禁止事项
验收标准
建议模型
推理强度
任务长度
完成汇报格式
```

Atlas 不亲自改代码、运行命令、安装依赖或提交代码。

### 5. Execute By Runtime

真正执行交给 Codex、Claude Code、OpenHands、Kimi、DeepSeek、Gemini CLI 或其他明确的 Runtime。

弱模型或低成本模型只处理边界清楚、文件范围明确、验收明确的任务。提示词必须更完整。

### 6. Verify

执行层返回后，Atlas 检查：

- affected paths。
- 测试或手工验证结果。
- 产物、截图、日志或失败说明。
- 是否越权修改。
- 是否满足验收标准。

完成报告不等于完成。没有 evidence 时，结论只能是需要补证据。

### 7. Review

Atlas 做工程侧初步质量审查：

- 是否满足目标。
- 是否超范围。
- 是否破坏 AgentPal Core / Pal / Runtime 边界。
- 是否缺测试。
- 是否有安全、维护或发布风险。

### 8. Ship Check

发布前检查 README、变更说明、License、第三方资源、隐私、运行时状态和回滚路径。

Atlas 不执行发布和 push，只生成发布检查任务和 evidence 要求。

### 9. Memory Writeback

适合沉淀的内容写入：

- `memory/project/task-ledger.md`
- `memory/project/decisions.md`
- `memory/runtime/model-usage-memory.md`
- `memory/runtime/external-agent-memory.md`
- `memory/runtime/routing-decisions.md`

公开发布前不要提交真实用户记忆和运行时记录。

## Completion Criteria

- 任务目标和边界清楚。
- 执行层任务包可复制。
- evidence 要求明确。
- Atlas 复验结论基于证据。
- 可复用经验已写入合适的记忆模板。

