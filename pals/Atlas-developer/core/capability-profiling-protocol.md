# Capability Profiling Protocol

Atlas 调度外部 Runtime 前，应建立能力卡片，而不是凭印象派任务。

## Capability Card

记录：

- runtime_id / runtime。
- 可用模型和推理强度。
- 可访问项目范围。
- 可用 Skill、插件、MCP、工具。
- 适合任务类型。
- 不适合任务类型。
- 风险和审批要求。
- last_checked。
- confidence。

## Placement

外部 Runtime 能力写入：

- `capabilities/agent-capability-matrix.md`
- `orchestration/execution-role-profiles.md`
- `memory/runtime/external-agent-memory.md`

外部 Runtime 不进入 Pal 通讯录。只有标准 Pal Pack 且开启协作开关，才能进入 `contacts/`。


