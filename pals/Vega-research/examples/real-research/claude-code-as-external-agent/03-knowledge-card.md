# Knowledge Card Candidate: Claude Code as External Developer Agent

## Card Status

Candidate only. Not promoted to formal Vega knowledge yet.

## Title

Claude Code 作为 AgentPal 外部开发 Agent 候选

## Theme

External Developer Agent / Runtime Evaluation

## Applicable Pal

- Primary: suitable implementation collaborator
- Supporting: Vega / Research Pal

## Scenarios

- 合适实现协作对象需要把边界清楚的代码库任务交给外部开发 Agent。
- AgentPal 需要评估 Claude Code 是否适合作为 Runtime / Agent 候选。
- 用户需要区分 Claude Code、Codex、OpenHands 和 Pal Pack 通讯录成员。

## Core Conclusion

Claude Code 适合作为 适合由实现协作对象调度的外部开发 Agent 候选，但当前不应进入 AgentPal Pal 通讯录。它应被视为 Runtime / Agent：接收合适实现协作对象的有边界任务包，完成后返回 evidence，由合适协作对象 或 Codex 复验。

## Confirmed Facts

- Claude Code 官方定位为可读取代码库、编辑文件、运行命令并与开发工具集成的 agentic coding tool。
- Claude Code 官方文档说明其可通过 MCP 连接外部工具和数据源，并提示信任与 prompt injection 风险。
- Claude Agent SDK 暴露 built-in tools、hooks、subagents、MCP、permissions 和 sessions。
- Claude Code 支持 subagents、hooks、skills 和 managed settings / policy 相关控制面。

## Inferences

- Claude Code 的能力面足以作为 AgentPal 外部开发 Agent 候选。
- 由于其可修改文件和运行命令，implementation collaborator handoff 必须限制范围并要求 evidence。
- Claude Code 的 MCP、hooks、skills、subagents 和 SDK 可以为未来 Adapter 设计提供参考，但需要真实工程验证。

## Usage Suggestions

- 由 Vega 负责调研来源、能力边界和不确定项。
- 由合适协作对象 负责工程可行性判断、任务拆解、外部 Runtime handoff 和完成报告复验。
- 每次使用前刷新版本、权限、平台、SDK、MCP、插件和 hooks 信息。
- 不把 Claude Code 写进 `contacts/`，除非未来它被包装成标准 Pal Pack 并声明协作开关。

## Risks

- 产品能力变化快，旧资料容易过期。
- 外部 Runtime 可读写代码和运行命令，权限风险高。
- MCP、plugin、hook 和 skill 可能引入供应链、数据流和 prompt injection 风险。
- 完成报告可能不等于真实完成，必须复验。

## Refresh Conditions

- Claude Code 发布重要版本更新。
- AgentPal 准备设计 Claude Code Adapter。
- 合适实现协作对象准备真实调度 Claude Code 执行开发任务。
- MCP、SDK、hooks、plugins、skills 或 permission policy 发生变化。
- 用户运行环境、账号、平台或权限策略变化。

## Related Vega Skills / Runbooks

- `technical-option-comparison`
- `source-quality-check`
- `evidence-table-builder`
- `contradiction-and-uncertainty-check`
- `knowledge-card-curator`
- `runbooks/source-verification/fact-checking-workflow.md`
- `runbooks/technical-research/technology-selection.md`

## Related Agent / Runtime

- suitable implementation collaborator
- Codex
- Claude Code
- OpenHands
- MCP servers

## Last Checked

2026-06-22 (Asia/Shanghai)

## Source Status

Primary source status: Verified from Anthropic official Claude Code documentation.

Pending: hands-on task trial, SDK behavior validation, target project permission behavior, cross-runtime quality comparison.

