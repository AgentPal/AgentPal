# Research Pal Release Readiness

## 结构是否完整

通过条件：根目录包含 README、LICENSE、CHANGELOG、CONTRIBUTING、THIRD_PARTY_NOTICES、SKILL、PAL、AGENTS、pal.json、PAL_CONTACTS、RESOURCE_INDEX 和标准目录。

## README 是否清楚

通过条件：README 能说明 Vega 是 AgentPal 官方 Research Pal，不是搜索引擎、爬虫或事实裁判，并说明 Skill、Workflow、Runbook、导入、协作、来源和 License 边界。

## 14 个正式 Skill 是否完整

通过条件：`skills/` 下 14 个正式 Skill 与 `pal.json` 一致，每个 Skill 都有 README，并包含用途、适用场景、不适合场景、输入信息、处理流程、输出格式、验收标准、风险边界和关系。

## Workflow / Runbook 是否可用

通过条件：Research Lifecycle、GitHub Project Evaluation、Technology Selection、Knowledge Card Creation、Fact Checking Workflow、Research Tool Shortlist 都能生成研究任务和 evidence 要求。

## 示例是否可用

通过条件：usage 示例覆盖技术调研、开源项目评估、方案对比、事实核查、研究工具筛选、Agent Skill 资源评估和学术来源审查。

## 真实研究任务是否可用

通过条件：`examples/real-research/claude-code-as-external-agent/` 包含 brief、source plan、findings report、knowledge card、suitable implementation collaborator handoff 和 verification notes，并能展示 Vega 如何区分事实、推断、建议和 pending verification。

## License 和第三方边界是否清楚

通过条件：LICENSE 为 MIT，THIRD_PARTY_NOTICES 明确第三方资料保留原始 License，无授权内容不进入公开包。

## Research Card 是否安全

通过条件：`imports/research-cards/` 中的 card 不含第三方源码、README 原文、SKILL.md 原文、论文正文、网页正文、安装命令或自动执行规则；card 不是正式 Skill，不进入 contacts。

## R3 方法改写是否为 Vega 自有表达

通过条件：事实核查、Agent Skill 资源评估、研究工具筛选和学术来源审查都用 Vega 自有表达写入 Runbook / Knowledge / Usage 示例，没有复制第三方原文。

## Pal 通讯录边界

通过条件：`contacts/pals.json` 为空或只包含标准 Pal Pack，不包含普通 Skill、工具、模型、MCP、插件、外部 Runtime 或资料。

## 是否可以进入 RC 候选

R3 完成后可进入真实研究任务试用准备状态。进入 RC 前建议做 R4：让 Vega 实际模拟调研一个 Agent / Runtime 是否适合 AgentPal，并输出研究报告、知识卡和 suitable implementation collaborator handoff。

R4 完成后，如真实研究示例、suitable implementation collaborator handoff、RC 报告、JSON、contacts、第三方边界和空白检查均通过，`pal-research` 可以进入 RC 候选等待统一发布状态。

R5 完成后，如 `RELEASE_NOTES_v0.1.md`、README、Skill、Workflow、Runbook、Research Card、Usage、Real Research、License、contacts、`.gitignore`、JSON 和 Markdown 检查均通过，`pal-research` 可作为未来 `AgentPal/pal-research` 独立仓库 RC 候选，等待与 AgentPal 主标准仓库和其他官方 Pal 一起统一发布。

