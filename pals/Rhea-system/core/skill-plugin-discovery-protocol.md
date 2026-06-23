# Skill Plugin Discovery Protocol

Pal 应识别当前 Runtime 和外部 Runtime 可用的 Skill、插件、MCP、hooks、commands 和工具。

## Discovery Steps

1. 读取 Runtime 暴露的能力清单。
2. 检查本地 registry 或配置文件。
3. 搜索常见 Skill / plugin / MCP 目录。
4. 如果 Runtime 支持查询命令，要求 Runtime 列出可用能力。
5. 无法自动识别时询问用户。
6. 写入 `plugins/installed-skills.md`、`plugins/installed-plugins.md`、`plugins/installed-mcp.md`。
7. 记录 `last_checked`、`scan_method`、`confidence`。

## non-Pal runtime Discovery

调度外部 Runtime 前，先确认：

- 可用模型。
- 推理强度。
- Skill、插件、MCP、hooks、commands。
- 项目访问范围。
- 工具权限。

结果写入 `memory/runtime/external-agent-memory.md` 和 `capabilities/agent-capability-matrix.md`。

普通 Skill、插件、MCP 和工具不是 Pal，不能进入 Pal 通讯录。


