# Technical Research Request Example

This is a non-binding example. It demonstrates one possible collaboration shape, not a fixed route.

这是非绑定示例，只展示一种可能协作形态，不是固定路由。

用户请求：

```text
帮我调研 Claude Code 是否适合接入 AgentPal 作为外部开发 Agent。
```

## Vega 输出示例

### 研究问题拆解

- Claude Code 当前能力是什么。
- 是否适合作为 AgentPal 的外部开发 Agent。
- 它与 Codex、OpenHands 等 Runtime 的边界有什么不同。
- 接入时需要哪些权限、项目访问和 evidence。
- 是否存在 License、隐私、成本或稳定性风险。

### 需要查证的来源

| 来源类型 | 目的 |
|---|---|
| 官方文档 | 当前能力、使用方式、权限边界 |
| 官方发布说明 | 最近变化和版本差异 |
| GitHub / 社区反馈 | 实际使用问题和限制 |
| AgentPal 本地标准 | Runtime / Pal / contacts 边界 |
| development-oriented docs | 开发任务 handoff 和 evidence 需求 |

### 事实 / 推断 / 建议

- 事实：只记录已由来源支持的能力、限制和版本信息。
- 推断：根据来源和 AgentPal 需求推断是否适合接入。
- 建议：如果接入，先作为外部 Runtime / Agent 记录，不进入 Pal 通讯录。

### 输出报告结构

```text
## 结论先行
## 来源与时间
## 能力清单
## 边界和风险
## 与 AgentPal 的适配方式
## 需要逐案判断的协作候选
## 不确定项
## 知识卡候选
```

### 如何生成协作候选 Context Packet

Vega 将 Claude Code 的能力、限制、来源、时间、风险和不确定项整理成 Context Packet。当前 AI 根据上下文逐案判断是否需要开发视角补充工程接入方式、开发成本和任务拆分。

