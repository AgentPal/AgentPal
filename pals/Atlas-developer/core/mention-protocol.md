# Mention Protocol

Atlas 支持 `@PalName` 和 `/pal PalName` 作为协议层协作约定。

## Default Semantics

- `@PalName` 默认表示咨询。
- `/pal PalName handoff` 才表示转交 owner。
- 多 Pal 回复应结构化，便于 owner Pal 汇总。

目标 Pal 不在通讯录时，应先按发现规则检查。普通 Skill、工具、MCP、插件、模型、外部 Runtime 和资料包不能被当作 Pal。

## Degraded Implementation

- AgentPal：未来可原生支持 `@Pal` / `/pal`。
- Codex：可通过 Pal Router Skill、Plugin、subagent workflow 或项目约定实现。
- Claude Code：可通过 Skill、slash command、subagent 或 hook 实现。
- OpenHands、Gemini CLI、DeepSeek-TUI、Kimi、CodeWhale：可通过命令约定、交接包或 MCP 适配实现。

不要假设当前 Runtime 原生支持群聊式多 Pal 对话。不支持时，Atlas 应生成 Context Packet，由用户或 Runtime 手动转交。

## Context Packet

协作前生成受控上下文包：

- from_pal
- to_pal
- mode
- user_goal
- current_state
- constraints
- relevant_files
- attempted_actions
- needed_output
- privacy_policy
- verification_requirements

不要无脑转交完整聊天上下文。敏感上下文需要用户批准。

