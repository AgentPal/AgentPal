# Skill And Plugin Discovery Protocol

Atlas 在调度前应查询当前 Runtime 已安装的 Skill、插件、MCP、hooks、commands 和工具。

## Discovery Targets

- Runtime 内置 Skill。
- 已安装插件。
- MCP server 和外部连接。
- hooks / commands。
- shell、git、browser、filesystem 等工具权限。
- 外部 Runtime 自带能力。

## Rules

- 普通 Skill、插件、MCP 和工具不是 Pal，不能进入 `contacts/`。
- 外部 Developer Skill 先进入 `imports/skills/` 和 `registry/skills.index.md`。
- 第三方资源必须保留原始 License 边界。
- 未确认能力不得写成确定能力。

## Memory Writeback

- `plugins/installed-skills.md`
- `plugins/installed-plugins.md`
- `plugins/installed-mcp.md`
- `capabilities/skill-capability-matrix.md`
- `memory/runtime/skill-plugin-usage-memory.md`

