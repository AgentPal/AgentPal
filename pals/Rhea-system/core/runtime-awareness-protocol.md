# Runtime Awareness Protocol

Pal 在执行或调度任务前，应识别当前 Agent Runtime、模型、推理强度和可用能力。

## Identify Current Runtime

记录：

- runtime_name
- runtime_type
- host_context
- detected_at
- confidence

如果无法自动识别，先询问用户；仍无法确认时写 `unknown`，不要猜测。

## Identify Current Model

记录：

- model
- provider
- supports_reasoning_strength
- reasoning_strength
- context_window_if_known
- cost_or_speed_notes_if_known

不要硬编码某个模型为永久默认。用户可能切换模型、升级 Runtime 或调整推理强度。

## Identify Runtime Capabilities

检查当前 Runtime 可用的：

- Skill
- 插件
- MCP
- hooks
- commands
- tools
- file access
- shell access
- browser access

## Refresh Rules

以下情况需要刷新：

- 新会话开始。
- 用户切换 Runtime、模型或推理强度。
- 用户安装、删除或更新 Skill、插件、MCP、hooks、commands。
- 准备调度外部 Runtime。
- 关键任务、风险任务或发布前复验。
- 上次记录 confidence 低或 last_checked 过旧。

## Write Back

- `runtime/current-runtime.md`
- `runtime/runtime-refresh-log.md`
- `memory/runtime/runtime-memory.md`

外部 Runtime 记录在 runtime/capabilities/orchestration/memory/runtime，不进入 Pal 通讯录。只有标准 Pal Pack 才能进入 `contacts/`。

