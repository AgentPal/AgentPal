# Agent Skill Resource Evaluation

Vega 评估外部 Runtime Skill 资源时，目标不是“安装更多能力”，而是判断它是什么、能不能公开记录、是否适合改写为 AgentPal / Vega 自有资源。

## How To Identify A Skill Package

检查：

- 是否有 `SKILL.md`。
- 是否有 README、manifest、examples、templates 或 scripts。
- 是否声明用途、触发场景、输入、输出和边界。
- 是否包含命令、脚本、外部服务、MCP、插件或模型依赖。
- 是否说明 License。

## Classify The Resource

Vega 应区分：

- Skill：说明如何做某类任务。
- Tool：执行动作的软件、脚本、CLI、MCP 或插件。
- Knowledge：文档、资料、清单、模板或方法。
- Persona：语气、人设或角色设定。
- Workflow：多步骤流程。
- Pal Pack：包含 `PAL.md`、`pal.json`、`type: pal-pack` 和协作开关。

普通 Skill 不是 Pal Pack，不能进入 contacts。

## Import Decision

| Decision | When To Use |
|---|---|
| reference-only | 有参考价值，但不能或不应打包 |
| public-card | License 清楚，适合公开记录来源、用途、风险 |
| convert-to-runbook | 方法可改写为 Vega 自有流程 |
| convert-to-knowledge-card | 方法可沉淀为 Vega 知识 |
| rewrite-as-vega-skill | 长期稳定、边界清楚、与 Vega 核心能力强相关 |
| reject | License、安全、隐私、质量或边界不可接受 |

## License And Safety Checks

- 无 License 或 License 不明：不复制内容。
- 强执行能力：检查命令、安装、删除、上传、部署、账号和 API key。
- 来源材料：不复制大段 README、SKILL.md、教程、网页或论文正文。
- 隐私材料：不能发送给外部 Runtime，除非用户明确批准。

## Skill Card Minimum Fields

- source URL。
- License。
- resource type。
- capability。
- risk。
- Vega handling。
- last checked。
- public package boundary。

## Promotion Rule

外部 Skill 的思路只有经过使用验证、License 清楚、安全边界清楚，并被改写为 Vega 自有表达后，才可能提升为 Runbook、Workflow、Knowledge 或 Formal Skill。

