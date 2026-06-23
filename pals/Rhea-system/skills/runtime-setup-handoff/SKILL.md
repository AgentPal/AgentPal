---
name: runtime-setup-handoff
description: Use this skill when you need to 为 Codex、Claude Code、OpenHands、Gemini CLI、DeepSeek-TUI 等 Runtime / Agent 的安装、检测和配置生成执行层 handoff。
---

# runtime-setup-handoff

## Purpose

为 Codex、Claude Code、OpenHands、Gemini CLI、DeepSeek-TUI 等 Runtime / Agent 的安装、检测和配置生成执行层 handoff。

## When to use

- 用户要准备外部 Runtime Runtime。
- Runtime 已安装但不可用。
- 需要检查登录、provider、PATH、依赖或项目目录。

## Inputs

- Runtime 名称。
- 用户系统平台。
- 目标用途。
- 官方来源或待查证来源。
- 用户允许的执行范围。

## Process

1. 确认 Runtime 和目标平台。
2. 要求优先查官方来源。
3. 检查安装前准备、权限和账号风险。
4. 生成执行层任务包。
5. 定义安装后验证和失败回收。

## Outputs

Produce the structured output documented in README.md, but return it as a clean runtime-ready artifact instead of a copied template block.

## Boundaries

Not a fit:
- 让 Rhea 直接安装 Runtime。
- 未确认官方来源或安装方式。
- 需要输入密钥、token 或账号凭据。

Risk boundary:
不保存凭据，不代替用户登录，不批准管理员权限。

Do not bypass approval, escalate privileges casually, or normalize destructive system actions.

## Evidence and handoff requirements

Any execution handoff must include target paths, permission needs, rollback or stop conditions, and evidence from version checks, logs, screenshots, or command output.

Reference acceptance hints:
- 来源优先级清楚。
- 不含未知脚本自动执行。
- 验证要求包含版本、路径、启动状态和登录/可用性说明。

## Related files

- Runtime entry: skills/runtime-setup-handoff/SKILL.md
- Human notes: skills/runtime-setup-handoff/README.md
- Parent index: skills/index.md

使用 `runbooks/runtime-setup/agent-runtime-setup.md`，必要时咨询问从当前 contacts / registry 解析出的合适协作对象 查证官方资料。

