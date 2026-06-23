# Option Comparison Example

用户请求：

```text
帮我比较 Codex、Claude Code、OpenHands 哪个更适合作为 suitable implementation collaborator 的外部执行层。
```

## Vega 输出示例

### 比较维度

- 当前能力和权限。
- 本地项目读取能力。
- 命令、浏览器、MCP、插件或 Skill 支持。
- 长上下文能力。
- Debug 和跨文件修改适配性。
- evidence 返回能力。
- 成本、稳定性和隐私风险。

### 需要查询的信息

| 来源类型 | 目的 |
|---|---|
| 官方文档 | 当前能力和限制 |
| 本地 AgentPal 标准 | Runtime / Pal / contacts 边界 |
| 实现协作材料 | suitable implementation collaborator 的执行层要求 |
| 近期发布说明 | 模型和功能变化 |
| 实际使用记录 | 成功率和失败模式 |

### 表格化对比

| 方案 | 适合任务 | 风险 | Evidence 能力 | Vega 资料结论 |
|---|---|---|---|---|
| Codex | 本地代码任务、文档和仓库内修改 | 需确认当前工具权限 | 强 | 适合作为默认本地执行层 |
| Claude Code | 长上下文 Debug、跨文件分析 | 需确认项目访问与命令权限 | 中到强 | 适合复杂 Debug 和长上下文交接 |
| OpenHands | 外部执行环境和自动化 | 权限、安全和日志需严格限定 | 取决于配置 | 适合作为受控外部执行候选 |

### 结论

如果任务是 AgentPal 官方 Pal Pack 文档和本地仓库整理，Codex 优先。复杂 Debug 可交给 Claude Code。需要外部执行环境时再评估 OpenHands。

### 不确定项

- 当前版本能力可能变化，需要刷新官方文档。
- 每个 Runtime 的本地权限、插件和模型配置可能不同。

### 下一步

将资料结论逐案请从当前 contacts / registry 解析出的合适协作对象补充，由 协作对象判断实际开发任务如何拆分给执行层。

