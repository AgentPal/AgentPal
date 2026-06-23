# Runtime Awareness Protocol

Atlas 在生成开发任务、调度外部 Runtime 或审查执行结果前，必须先建立当前 Runtime 认知。

## Detect

尽量识别：

- 当前 Runtime：Codex、Claude Code、OpenHands、AgentPal、DeepSeek-TUI、Gemini CLI 或 unknown。
- 当前模型。
- 当前推理强度或 thinking effort。
- 文件、shell、浏览器、MCP、插件、hooks、commands 和外部工具权限。
- 当前项目路径、工作树状态和可访问范围。

无法识别时，标记为 `unknown`，不要编造能力。

## Record

把结果写入：

- `runtime/current-runtime.md`
- `runtime/runtime-registry.md`
- `memory/runtime/runtime-memory.md`

## Use

Atlas 只基于已知能力生成调度建议。真实执行动作必须由 Runtime 自己完成。

