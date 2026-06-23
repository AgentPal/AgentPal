# Mention Protocol

支持 `@PalName` 和 `/pal PalName` 作为协议约定。

## 默认语义

- `@PalName` 默认是 consult。
- `/pal PalName handoff` 才表示转交 owner。
- 多 Pal 回复应结构化，便于 owner Pal 汇总。

目标 Pal 不在通讯录时，应先按发现规则检查，不能把普通资源当作 Pal。

## 降级实现

- AgentPal：可通过协议层原生或适配方式支持 `@Pal`。
- Codex：可通过 Pal Router Skill、Plugin、subagent workflow 或项目约定实现。
- Claude Code：可通过 `/pal` Skill、slash command、subagent 或 hook 实现。
- 其他 Runtime：可通过命令约定或 MCP 适配实现。

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
