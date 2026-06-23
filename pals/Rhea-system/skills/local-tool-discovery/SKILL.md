---
name: local-tool-discovery
description: Use this skill when you need to 识别当前机器或 Runtime 可用的包管理器、开发工具、Agent、Skill、插件、MCP、hooks 和 commands。
---

# local-tool-discovery

## Purpose

识别当前机器或 Runtime 可用的包管理器、开发工具、Agent、Skill、插件、MCP、hooks 和 commands。

## When to use

- 需要判断该用哪个执行层。
- 安装前要看是否已有工具。
- 需要建立能力卡片或路由建议。

## Inputs

- 当前 Runtime。
- 目标系统范围。
- 允许检查的工具类型。
- 用户隐私边界。

## Process

1. 生成只读发现任务。
2. 区分工具、Runtime、Skill、插件、MCP 和 Pal。
3. 建立能力摘要。
4. 写入 runtime/capabilities 相关记忆候选。
5. 不把外部 Runtime 加入 contacts。

## Outputs

Produce the structured output documented in README.md, but return it as a clean runtime-ready artifact instead of a copied template block.

## Boundaries

Not a fit:
- 要求 Rhea 直接扫描私密目录。
- 要求保存完整系统清单或私人软件列表。

Risk boundary:
不保存完整用户软件清单，不读取敏感路径。

Do not bypass approval, escalate privileges casually, or normalize destructive system actions.

## Evidence and handoff requirements

Any execution handoff must include target paths, permission needs, rollback or stop conditions, and evidence from version checks, logs, screenshots, or command output.

Reference acceptance hints:
- 发现任务不越权。
- 能区分 Pal 通讯录和外部工具。
- 只记录必要摘要。

## Related files

- Runtime entry: skills/local-tool-discovery/SKILL.md
- Human notes: skills/local-tool-discovery/README.md
- Parent index: skills/index.md

连接 runtime、models、plugins、capabilities、orchestration 和 memory/runtime。

