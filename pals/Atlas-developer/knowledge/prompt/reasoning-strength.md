# Reasoning Strength

Atlas 建议按任务风险和复杂度选择推理强度。

- low：格式清理、简单补文档、确定性替换。
- medium：常规实现、模板补齐、普通 Bug 修复。
- high：跨模块判断、失败诊断、复杂拆解、发布前复验。
- xhigh：架构边界、安全、权限、审批、重大数据风险。

推理强度建议必须写入任务提示词，并在执行后记录到 `memory/runtime/model-usage-memory.md`。

