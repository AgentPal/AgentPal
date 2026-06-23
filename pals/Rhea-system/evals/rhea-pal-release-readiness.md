# Rhea Pal Release Readiness

## 结构是否完整

通过条件：根目录包含 README、LICENSE、CHANGELOG、CONTRIBUTING、THIRD_PARTY_NOTICES、SKILL、PAL、AGENTS、pal.json、PAL_CONTACTS、RESOURCE_INDEX 和标准目录。

## README 是否清楚

通过条件：README 能说明 Rhea 是 AgentPal 官方系统与应用管家 Pal，不是系统执行器，并包含快速开始、场景、Skill、Workflow、Runbook、导入、协作、evidence、contacts 和 License 边界。

## 12 个正式 Skill 是否完整

通过条件：`skills/` 下 12 个正式 Skill 与 `pal.json` 一致，每个 Skill 都有 README，并包含用途、适用场景、不适合场景、输入信息、处理流程、输出格式、验收标准、风险边界和关系。

## Workflow / Runbook 是否可用

通过条件：System Maintenance Lifecycle、Agent Runtime Setup、Diagnose Development Environment、Safe Installation Handoff、Failed Command Recovery 都能生成可交接、可审批、可验收的任务。

## 示例是否可用

通过条件：usage 示例覆盖 Runtime 配置、环境错误诊断、安全安装和 evidence 审查。

## License 和第三方边界是否清楚

通过条件：LICENSE 为 MIT，THIRD_PARTY_NOTICES 明确第三方资源保留原始 License，无授权内容不进入公开包。

## Pal 通讯录边界

通过条件：`contacts/pals.json` 只包含标准 Pal Pack，不包含普通 Skill、工具、模型、MCP、插件、软件或外部 Runtime。

## 是否可以进入 RC 候选

如果结构、README、Skill、Workflow、Runbook、Knowledge、Examples、Evals、License、contacts、JSON、Markdown 和隐私边界均通过，`pal-rhea` 可以进入独立仓库 RC 候选等待统一发布状态。

