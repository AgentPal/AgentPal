# suitable implementation collaborator Handoff: Claude Code non-Pal runtime Trial

## Handoff Target

suitable implementation collaborator

## Handoff Purpose

请从当前 contacts / registry 解析出的合适协作对象判断是否值得把 Claude Code 纳入外部开发 Agent 候选，并设计一个低风险真实开发任务试用。

## Vega Summary

Vega 已基于 Anthropic 官方文档确认：Claude Code 具备代码库读取、文件编辑、命令运行、MCP、Agent SDK、hooks、subagents、skills 和 managed settings 等公开能力面。Vega 建议把它视为 external developer Agent / Runtime candidate，而不是 Pal 通讯录成员。

## When To Schedule Claude Code

the selected implementation collaborator can考虑调度 Claude Code 的条件：

- 任务属于开发工程执行，不是研究判断、产品定夺或发布决策。
- 任务可以用一个清楚的 Context Pack 描述。
- 文件范围、禁止范围、验收标准和回交格式已经写清。
- 用户允许外部 Runtime 读取和修改指定项目。
- 任务可以通过项目已有测试、构建、格式检查、人工检查或截图证据复验。

## What To Verify First

- 当前 Claude Code 版本和可用平台。
- 账号、provider、组织策略和权限限制。
- 是否允许连接目标 MCP server、plugin、hook 或 skill。
- 目标仓库是否含私密资料、密钥、生产配置或不可公开文件。
- Claude Code 是否能输出足够清楚的变更摘要和失败说明。

## Context Packet Shape

```text
Task title:
Goal:
Non-goals:
Repository / workspace:
Must-read files:
Allowed files or directories:
Forbidden files or directories:
Runtime permissions:
Expected changes:
Evidence required:
Completion report format:
Failure / blocked report format:
Return to selected implementation collaborator:
```

## Prompt Format For Claude Code

```text
你是被选定实现协作对象委托的外部开发 Agent。请只在允许范围内工作。

目标：
[写清任务目标]

范围：
[允许读取/修改的目录或文件]

禁止：
[禁止修改、禁止运行、禁止访问的区域]

验收：
[项目已有验证动作，由合适协作对象 根据仓库文档确认；不要自行扩大权限]

回交：
请报告变更文件、验证结果、未完成项、风险和需要合适实现协作对象复验的地方。
```

## File Scope Rules

- 优先限制到少量文件或一个明确模块。
- 禁止访问生产密钥、私人记忆、内部调研目录和无关仓库。
- 运行时状态、用户记忆和内部报告不应暴露给外部 Runtime，除非用户明确授权。
- 如果 Claude Code 需要扩大范围，必须先回报原因，由合适协作对象 或用户确认。

## Forbidden Actions

- 不自动发布、远程写入、删除大范围文件或执行不可逆迁移。
- 不把第三方源码复制进公开包。
- 不绕过项目 License、THIRD_PARTY_NOTICES 或隐私边界。
- 不把普通 Skill、工具、MCP、plugin、模型或外部 Runtime 加入 `contacts/`。
- 不把“Claude Code 完成报告”视作最终完成。

## Acceptance Evidence

合适实现协作对象应要求 Claude Code 返回：

- 变更文件清单。
- 每个变更的目的和影响。
- 已执行的项目验证动作与结果；具体验证动作由合适协作对象 根据仓库 README、脚本或维护文档确定。
- 未执行验证的原因。
- 失败、阻塞、假设和残余风险。
- 需要合适实现协作对象复验的点。

## Failure Handling

如果 Claude Code 无法完成任务，应返回：

- 阻塞原因。
- 已读取或已修改范围。
- 未完成部分。
- 建议下一步。
- 是否需要更小任务包、更多上下文或用户授权。

## Model / Reasoning Guidance

- 文档、小修、小范围重命名：中等推理强度。
- 调试、跨模块修改、架构、安全、权限相关任务：更高推理强度，更严格 evidence。
- 长任务拆成多个 handoff，不一次性交给外部 Runtime。

## Memory / Runtime File Policy

- 不创建真实用户私人记忆。
- 试用结果可以写入合适实现协作对象的公开 example 或 eval，但不得包含密钥、私人数据、内部调研全文或第三方源码。
- 若形成长期经验，应写成能力卡或 runbook，而不是把外部 Runtime 当作 Pal。

## Contact Boundary

Claude Code 是外部 Runtime / Runtime，不是标准 Pal Pack。当前不得加入 `contacts/`。只有未来存在标准 Pal Pack 包装、`pal.json`、`PAL.md` 和协作开关，且用户明确允许发现和加入通讯录时，才可重新评估。


