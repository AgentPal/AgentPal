# Model Routing Protocol

Pal 应根据任务复杂度、风险、成本、上下文需求和工具能力选择模型与推理强度。

## Routing Factors

- complexity：任务是否需要复杂判断。
- risk：是否涉及安全、权限、发布、数据损坏或架构边界。
- cost：是否需要控制成本。
- context_need：是否需要读取大量上下文。
- tool_need：是否需要特定 Skill、插件、MCP 或工具。
- verification_need：是否需要强复验。

## Model Levels

- 强模型：规划、复杂判断、提示词补强、失败诊断、最终复验。
- 普通模型：常规实现、文档整理、模板补齐、普通 bug 修复。
- 弱模型或低成本模型：边界明确、验收清楚、重复性强的执行任务。

## Reasoning Strength

- low：格式、简单清理、确定性修改。
- medium：常规实现、模板补齐、普通文档和测试修复。
- high：复杂规划、跨模块判断、失败诊断、发布复验。
- xhigh：重大架构、安全边界或深度故障分析。

## Avoid

- 不要所有任务都用最强模型。
- 不要让弱模型承担开放式复杂判断。
- 不要把模型能力记忆当作永久准确。

## Record Decision

关键路由写入 `memory/runtime/routing-decisions.md`，包含任务、可选方案、选择理由、模型/强度、提示词策略、结果和下次建议。

