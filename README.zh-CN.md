# AgentPal

AgentPal 是给编程 Agent 使用的 Pal 层。

它不是 Agent 层，不是多 Agent 运行时，也不是执行层。AgentPal 给现有运行时提供一套结构化的 Pal 工作区：身份、知识、技能、上下文、记忆、输出契约、协作规则、审查习惯、总结方式和学习存储规则。

AgentPal v0.1 是 Markdown / JSON / 协议工作区。它没有桌面 UI、Web UI、守护进程、扫描器、安装器、服务，也没有必须安装的运行时依赖。

## 当前运行方式

AgentPal v0.1 只使用 Simple Pal Mode。

在 Simple Pal Mode 下：

- 普通消息由 Mira 接收。
- Mira 对实质任务逐案判断。
- 如果某个已注册 Pal 可以主责这个任务，Mira 只做简短交接，然后停止作答。
- owner Pal 在同一条回复中立即接手回答。
- owner Pal 使用自己的 `PAL.md`、`SKILL.md`、`pal.json`、相关资产、Output Contract，并在缺少资产时诚实说明 fallback。
- AgentPal 不在普通回答中展示运行模式元数据。

因为 Pal 层是普通文件和协议，AgentPal 可以配合 Codex、Claude Code、CodeWhale、Gemini CLI、DeepSeek-TUI 或其它能够读取 Markdown / JSON 的 Agent 运行时使用。

## Pal 是什么

Pal 不是独立运行进程。Pal 是面向任务的工作包，包含：

- 身份和职责
- 知识和技能
- 上下文和记忆边界
- 输出契约
- 审查和总结习惯
- 学习和 Skill 存储规则

真正读取文件、写入文件、运行命令、调用工具、发布、删除等动作仍由当前运行时完成。AgentPal 负责帮助运行时判断谁来回答、使用哪些资产、怎样诚实汇报。

## 内置 Pal

内置 Pal 包括：

- Mira：Main Pal 和秘书协调者
- Atlas：开发视角
- Vega：研究和证据视角
- Rhea：本机系统和环境视角
- Quinn：质量、风险、证据和验收视角
- Morgan：文档和文件工作流视角
- Harper：写作和沟通视角
- Nova：产品和决策视角

能力说明只是非绑定示例，不是路由表。owner 选择由 AI 根据当前请求、上下文、约束、风险、期望输出和可用 Pal 资产逐案判断。

## 快速开始

1. 在你的 Agent 运行时中打开这个工作区。
2. 运行或粘贴 `INIT_PROMPT.md`。
3. 像普通对话一样先找 Mira。
4. 用 `/pal Name` 直接点名某个 Pal。
5. 需要新增 Pal 时，把 Pal Pack 放到 `pals/` 下，并刷新 contacts / registry。

## 外部项目工作组

AgentPal 可以作为工作组引用加入外部项目。在外部项目绑定会话中：

- 外部项目是当前项目
- AgentPal 只是 Pal 来源和路由参考
- “这个项目”指外部项目，不指 AgentPal 工作区

可以使用 `prompts/join-external-project-workgroup.md` 或 `projects/project-workgroup-template/agentpal/` 下的模板绑定项目。

## Skill 存储

如果用户明确要求把方法保存成 Skill，或类似操作超过 3 次，owner Pal 会把正式 Skill 存到自己的目录：

```text
pals/<Owner-Pal-Directory>/skills/<skill-id>/SKILL.md
```

除非用户明确要求创建全局运行时 Skill，否则不要把 AgentPal Pal-owned Skill 存入全局 runtime skill 目录。

## 未来运行时编排

子工作流、外部 Runtime 运行时、MCP 托管 Agent、远程 Agent 服务等未来设计，单独记录在 `docs/future-agent-orchestration.md`。这些内容不属于 AgentPal v0.1 当前运行行为。

