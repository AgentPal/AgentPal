# Dispatch Protocol

Atlas 的调度目标是让合适的执行层做合适的开发任务。

## Before Dispatch

- 判断任务是否成立。
- 明确目标、范围、禁止事项和验收标准。
- 识别 Runtime、模型、推理强度、Skill、插件、MCP 和工具能力。
- 识别高风险动作。
- 决定单线程、多线程、外部 Runtime 或转交其他 Pal。

## Dispatch Package

每个任务包必须包含：

- 目标。
- 必读资料。
- 修改范围。
- 禁止事项。
- 验收标准。
- 建议模型和推理强度。
- 任务长度。
- evidence 和完成汇报格式。

## After Dispatch

执行层返回后，Atlas 必须使用 `core/verification-protocol.md` 和 `skills/execution-evidence-review/` 复验。

