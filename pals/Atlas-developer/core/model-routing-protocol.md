# Model Routing Protocol

Atlas 根据任务复杂度、风险、上下文需求、工具能力和成本选择模型与推理强度建议。

## Strong Models

用于规划、架构判断、提示词补强、失败诊断和最终复验。

## Medium Models

用于常规实现、文档整理、模板补齐、普通 Bug 修复和测试补齐。

## Low-Cost / Weak Models

用于文件范围明确、验收清楚、重复性强的执行任务。提示词必须更完整，包含目标、必读资料、修改范围、禁止事项、验收命令、停止条件和完成汇报格式。

## Reasoning Strength

- low：格式清理、确定性小改。
- medium：常规实现、普通文档和测试修复。
- high：跨模块判断、复杂调试、发布前复验。
- xhigh：架构、安全、权限、审批和重大数据风险。

## Memory Writeback

关键模型选择写入：

- `memory/runtime/model-usage-memory.md`
- `models/model-selection-memory.md`
- `memory/runtime/routing-decisions.md`

