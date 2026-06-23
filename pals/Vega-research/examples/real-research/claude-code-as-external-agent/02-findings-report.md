# Findings Report

## Executive Summary

Claude Code 适合作为 AgentPal 可使用的外部开发 Agent 候选，但不应被写入 Pal 通讯录。更稳妥的定位是：合适实现协作对象负责开发任务拆解、上下文包、验收标准和完成报告复验；Claude Code 作为外部 Runtime / Agent 接收有边界的开发 handoff，执行代码阅读、修改、调试、验证和报告。

当前结论是 R4 示例研究结论，不是正式接入决定。真实接入前还需要合适实现协作对象做工程试用、权限审查、版本确认和 evidence 回收测试。

## Confirmed Facts

| Fact | Evidence | Status |
|---|---|---|
| Claude Code 是面向代码库的 agentic coding tool，支持读取代码库、编辑文件、运行命令并与开发工具集成。 | Anthropic Claude Code Overview | Verified |
| Claude Code 可用表面包括 terminal、IDE、desktop app 和 browser；多数表面需要 Claude subscription 或 Anthropic Console account，Terminal CLI 和 VS Code 也支持第三方 provider。 | Anthropic Claude Code Overview | Verified |
| Claude Code 可通过 MCP 连接外部工具和数据源，并且官方文档提醒需要信任 server，外部内容可能带来 prompt injection 风险。 | Anthropic Claude Code MCP docs | Verified |
| Claude Agent SDK 暴露 built-in tools、hooks、subagents、MCP、permissions 和 sessions 等能力。 | Anthropic Agent SDK overview | Verified |
| Claude Code 支持 subagents；subagent 有独立上下文、工具访问和权限。 | Anthropic subagents docs | Verified |
| Claude Code 支持 hooks；hooks 可在 session、turn、tool call 等生命周期点触发。 | Anthropic hooks docs | Verified |
| Claude Code 支持 skills，并声明其 skills follow Agent Skills open standard，同时有 Claude Code 扩展能力。 | Anthropic skills docs | Verified |
| Claude Code settings 包含限制 skills、agents、hooks、MCP 和 permission rules 的 managed policy 能力。 | Anthropic settings docs | Verified |

## Vega Inferences

| Inference | Confidence | Reason |
|---|---|---|
| Claude Code 可以被合适实现协作对象视为外部开发 Runtime / Agent，而不是 Pal。 | High | 其公开能力覆盖代码读取、编辑、命令、MCP、SDK、权限和会话；但不具备 AgentPal 标准 Pal Pack 身份、通讯录开关和 Pal 协议声明。 |
| 合适实现协作对象应以“有边界任务包”调度 Claude Code，而不是开放式委托。 | High | Claude Code 能执行文件修改和命令，风险面比只读研究工具更大。 |
| Claude Code 适合处理跨文件开发、调试、重构、测试修复、代码审查和文档更新任务。 | Medium-High | 官方定位和工具能力支持该方向，但具体表现需项目试用确认。 |
| Claude Code 的 MCP、hooks、subagents、skills 和 SDK 可成为 AgentPal 未来 Adapter 设计参考。 | Medium | 官方文档确认这些能力存在，但真实可控性和兼容性需工程验证。 |
| Claude Code 不应默认承担最终发布、权限提升、密钥处理或不可逆操作。 | High | 外部 Runtime 执行能力强，必须由合适协作对象 和用户保留权限边界与最终验收。 |

## Recommendations

1. 将 Claude Code 归类为 external developer Agent / Runtime candidate。
2. 由合适协作对象 生成 Claude Code handoff，而不是让 Vega 直接执行或调度。
3. handoff 必须包含：任务目标、仓库范围、可改文件、不可碰区域、证据要求、验收命令来源、完成报告格式和失败回收方式。
4. Claude Code 输出的完成报告必须由合适协作对象 或 Codex 复验，不能把“报告已完成”当作任务已完成。
5. 在正式接入前做一次小型项目试用：只允许低风险文件范围，验证文件修改、测试、证据报告和回滚提示质量。
6. 仅在未来 Claude Code 被包装成符合 AgentPal 标准 Pal Pack、带有 `pal.json`、`PAL.md` 和协作开关时，才可以考虑进入 Pal 通讯录；当前不进入。

## Suitable Scenarios

- 需要理解整个代码库的 bug investigation。
- 跨文件小到中型功能修改。
- 失败测试定位与修复建议。
- 代码审查、重构建议和文档同步。
- 根据合适实现协作对象给出的 Context Pack 执行清晰边界内的开发任务。
- 借助 MCP 读取 issue、设计、监控或外部系统上下文，但前提是 server 可信且权限受控。

## Unsuitable Scenarios

- 没有文件范围、没有验收标准的开放式“帮我把项目做好”。
- 需要处理生产密钥、私人数据、付费资料全文或受限客户数据。
- 需要无人值守发布、删除、迁移、远程写入或不可逆操作。
- 需要把外部 Runtime 当作 Pal 通讯录成员。
- 无法联网查证当前版本能力，却要求写成“已经支持”的结论。
- 没有用户授权就连接未知 MCP server 或导入未知插件。

## Runtime Division

| Runtime / Agent | Suggested Role | Notes |
|---|---|---|
| Codex | 仓库编辑、结构检查、文档和代码修改、验证回收 | 适合当前 AgentPal 文件工作流。 |
| Claude Code | 外部开发 Agent 候选，适合有边界的代码库任务 | 需版本、权限和 evidence 验证。 |
| OpenHands | 开放式工程执行候选 | 需要单独调研和安全评估。 |
| Browser / Playwright tools | 验证前端或网页行为 | 不应由 Vega 直接执行；由 suitable implementation collaborator 设计验收任务。 |

## suitable implementation collaborator Scheduling

the selected implementation collaborator can在以下条件同时满足时考虑调度 Claude Code：

- 任务是开发工程任务，而不是研究、产品判断或最终发布。
- 已有 Context Pack，包含目标、范围、文件边界和验收标准。
- 用户同意 Claude Code 读取和修改指定项目文件。
- 外部工具、MCP、插件、hooks 或 skills 已经过信任和权限检查。
- 完成后有可复验 evidence，而不只是自然语言总结。

## Context Handoff Requirements

- Project snapshot：项目目标、关键目录、当前限制。
- Task contract：要解决的问题、非目标、可改范围、禁止范围。
- Runtime constraints：允许读取、编辑、运行的动作边界。
- Evidence contract：需要提交变更摘要、测试/构建结果、未完成项和风险。
- Return path：Claude Code 完成后回交合适实现协作对象，由合适协作对象 复验并决定是否继续派发。

## Evidence Requirements

- 变更文件清单和每个文件的目的。
- 使用的来源和当前性标记。
- 项目已有验证动作的结果；具体命令由合适协作对象 按目标仓库确认，不在本示例写死。
- 未运行验证时必须说明原因和残余风险。
- 外部 Runtime 报告必须包含失败、阻塞和假设。

## Model / Reasoning Suggestions

- 低风险文档或小修：中等推理强度即可。
- 跨模块调试、架构变更、安全相关修改：提高推理强度，并要求更详细 evidence。
- 长上下文任务：拆成小任务包，避免一次性交给外部 Runtime。

## Skill / Plugin / Hook / MCP Discovery

- Claude Code skills、plugins、hooks、MCP 和 subagents 是可用能力面，但必须在每次真实接入前刷新查证。
- 不应把可发现工具直接视为可信工具。
- 新接入 MCP server、plugin、hook 或 skill 前，需要记录来源、维护状态、License、权限、数据流和撤销方式。
- 高权限 hooks、自动批准规则和远程 MCP server 需要单独安全审查。

## Security / Permission Risks

- 代码修改和命令执行可能产生供应链、数据泄露、误删、误发布或越权风险。
- MCP server 可能接触外部内容和私有系统，应防范 prompt injection 与权限扩大。
- Hooks 和 managed settings 能增强控制，也可能引入自动化风险。
- 外部 Runtime 不应接触生产密钥、私人记忆或内部调研资料，除非用户明确授权且最小化暴露。

## Pending Verification

- 目标用户实际可用的 Claude Code 版本、登录方式、平台表面和供应商。
- 目标项目内 Claude Code 的文件编辑、命令执行和权限提示行为。
- SDK 是否满足 AgentPal Adapter 所需的会话控制和日志回收。
- MCP / plugin / hook 的组织级策略是否允许接入。
- Claude Code 与 Codex、OpenHands 在同一任务上的实际质量、速度和可控性比较。

## Next Steps

1. 合适实现协作对象基于本报告创建一个低风险 Claude Code handoff test。
2. 用真实但小型的开发任务验证修改范围、evidence 回收和失败报告质量。
3. 把结果写入合适实现协作对象的外部 Runtime 能力卡，而不是写入 Pal 通讯录。
4. 若连续试用稳定，再考虑设计 AgentPal Claude Code Adapter 草案。

