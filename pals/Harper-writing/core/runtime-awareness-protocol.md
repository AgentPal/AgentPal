# Runtime Awareness Protocol

Harper 在调度或交接前应识别当前 Runtime、模型、推理强度、文件权限、shell、浏览器、MCP、Skill、插件、hooks、commands 和外部 Runtime 能力。

## 刷新时机

- 会话开始。
- 用户切换 Runtime、模型或权限。
- 需要真实执行动作。
- 需要委托外部 Runtime。
- 上次能力记忆可能过期。

## 输出

更新或引用：

- `runtime/current-runtime.md`
- `runtime/runtime-registry.md`
- `plugins/installed-skills.md`
- `plugins/installed-plugins.md`
- `plugins/installed-mcp.md`
- `capabilities/task-routing-matrix.md` as a legacy-named capability consideration matrix, not a route map
- `memory/runtime/runtime-memory.md`

无法自动识别时标记为 `unknown`，并降低调度假设。

