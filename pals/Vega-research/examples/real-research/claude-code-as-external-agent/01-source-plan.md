# Source Plan

## Source Priority

| Priority | Source Type | Purpose | Status |
|---|---|---|---|
| P0 | Anthropic official Claude Code docs | Confirm current product positioning and supported surfaces | Verified |
| P0 | Claude Code official docs for MCP, SDK, hooks, subagents, skills and settings | Confirm integration and control surfaces | Verified |
| P1 | Official release notes or repository metadata | Check fast-moving feature changes | Partially verified |
| P1 | Hands-on runtime test in a sample repo | Confirm operational behavior in AgentPal workflow | Pending |
| P2 | Community reports and comparisons | Understand rough adoption and pain points | Pending |

## Verified Sources

| Topic | Source | Status | Vega Use |
|---|---|---|---|
| Product positioning | [Claude Code Overview](https://code.claude.com/docs/en/overview) | Verified | Establishes Claude Code as an agentic coding tool across terminal, IDE, desktop app and browser. |
| MCP | [Claude Code MCP docs](https://code.claude.com/docs/en/mcp) | Verified | Confirms Claude Code can connect to external tools and data sources through MCP, with trust and prompt-injection concerns. |
| Agent SDK | [Claude Agent SDK overview](https://code.claude.com/docs/en/agent-sdk/overview) | Verified | Confirms SDK access to built-in tools, hooks, subagents, MCP, permissions and sessions. |
| Subagents | [Claude Code subagents docs](https://code.claude.com/docs/en/sub-agents) | Verified | Confirms specialized subagents with separate context, tools and permissions. |
| Hooks | [Claude Code hooks docs](https://code.claude.com/docs/en/hooks) | Verified | Confirms lifecycle hooks around sessions, turns and tool calls. |
| Skills | [Claude Code skills docs](https://code.claude.com/docs/en/skills) | Verified | Confirms Skill mechanism, bundled skills and Agent Skills compatibility claims. |
| Settings / policy | [Claude Code settings docs](https://code.claude.com/docs/en/settings) | Verified | Confirms managed settings for limiting skills, agents, hooks, MCP and permission rules. |

## Search / Refresh Questions

- Claude Code 当前是否仍提供所需平台表面和 SDK 能力？
- Claude Code 的 MCP、hooks、subagents、skills 和 settings 是否在目标版本中可用？
- 目标用户是否有 Claude subscription、Anthropic Console account 或可用 third-party provider？
- 目标项目的权限模型是否允许外部 Runtime 读取、修改文件和运行项目命令？
- 合适实现协作对象是否能在任务 handoff 中明确文件范围、验收证据和失败回收机制？

## Excluded Sources

- 未核实博客、二手教程和社交媒体帖子不作为本轮事实依据。
- 第三方项目 README 不复制进公开包。
- 无明确 License 的外部资料不保存全文。

## Staleness Risk

Claude Code 是快速变化的开发工具。涉及版本、安装方式、登录方式、支持平台、模型、权限、SDK API、MCP 行为、插件机制和安全策略的事实，在真实接入前必须重新查证。

