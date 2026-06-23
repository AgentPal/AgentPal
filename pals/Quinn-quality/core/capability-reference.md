# Capability Reference

This embedded Pal capability reference is not a route map.

No hard-coded semantic routing. Owner selection, collaborator selection, runtime selection, and collaboration-shape decisions are made case-by-case by AI judgement from the current request, context, registered Pal ownership scopes, available assets, risk, and user constraints.

## Source: agent-capability-matrix.md

# Agent Capability Matrix

外部 Runtime 使用前必须建立能力卡片。未确认能力时只生成候选任务包，不假设可执行。

## Source: model-capability-matrix.md

# Model Capability Matrix

记录模型适合的审查类型、推理强度、成本、上下文限制和已验证表现。

## Source: plugin-capability-matrix.md

# Plugin Capability Matrix

记录插件、MCP、Skill、hooks、commands 的用途、权限、风险和 last_checked。

## Source: README.md

# capabilities

这里维护 Agent、模型、Skill、插件和能力选择画像。能力画像不是路由表，协作对象必须由当前 AI 逐案判断。

能力画像需要 `best_for`、`not_suitable_for`、`prompt_style`、`refresh_rule`、`confidence`，不能永久假设准确。

## Source: skill-capability-matrix.md

# Skill Capability Matrix

| Skill | Runtime | Best for | Not suitable for | Trigger | Refresh rule | Confidence |
| --- | --- | --- | --- | --- | --- | --- |
| unknown | unknown | unknown | unknown | unknown | plugin scan | unknown |

## Source: task-routing-matrix.md

# Capability Consideration Matrix

This file is a capability reference, not a route map.

No hard-coded semantic routing. AI judgement is required case-by-case before selecting a runtime, Pal collaborator, model, or execution path.

| situation | possible capability to consider | model strength | evidence |
|---|---|---|---|
| 发布门禁 | quality evidence review capability | high/medium | 测试、风险、回滚 |
| 开发修复 | development or execution capability may be considered | medium | affected files、测试 |
| 来源核查 | research or source-check capability may be considered | medium/high | 来源、时间、可信度 |
| 清单整理 | quality checklist capability | low/medium | 输入材料和输出表 |



