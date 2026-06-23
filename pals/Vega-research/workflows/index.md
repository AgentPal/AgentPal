# Vega Workflows Index

Vega v0.1 内置一个正式 Workflow：

| id | path | purpose |
|---|---|---|
| research-lifecycle | `workflows/research-lifecycle/` | 从问题定义、范围划定、来源发现、来源验证、综合分析、方案对比、报告、知识卡到 Pal handoff 的研究闭环 |

Workflow 不直接执行搜索、爬虫、下载或 API 调用。真实执行交给 Runtime 或外部 Runtime，Vega 负责计划、约束、证据结构和复验。

## R3 Addition

`research-lifecycle` 已补充 multi-step research orchestration：来源发现、来源验证、综合分析、报告写作、知识卡和 Pal handoff 的分层协作规则。

