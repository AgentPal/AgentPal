# Vega Workflows Index

Vega v0.1 内置一个正式 Workflow：

| id | path | purpose |
|---|---|---|
| research-lifecycle | `workflows/research-lifecycle/` | 从问题定义、范围划定、来源发现、来源验证、综合分析、方案对比、报告、知识卡到 Pal handoff 的研究闭环 |

Workflow 不直接执行搜索、爬虫、下载或 API 调用。真实执行交给 Runtime 或外部 Runtime，Vega 负责计划、约束、证据结构和复验。

## R3 Addition

`research-lifecycle` 已补充 multi-step research orchestration：来源发现、来源验证、综合分析、报告写作、知识卡和 Pal handoff 的分层协作规则。

## R03 Research / Intelligence Lead Workflows

- `research-request-intake-workflow.md`
- `web-research-task-package-workflow.md`
- `source-inventory-workflow.md`
- `evidence-matrix-workflow.md`
- `research-synthesis-workflow.md`
- `comparative-analysis-workflow.md`
- `knowledge-distillation-workflow.md`
- `collaboration-with-default-pals.md`


## Context Loading Rule

Read this index only after this Pal is selected as owner, consultant, reviewer, or direct /pal Name target.

Use this index to choose the smallest relevant asset slice. Do not load every file in this directory by default.

Read assets here when:

- the current task requires this Pal's professional method;
- the output contract needs a specific skill, knowledge card, runbook, or workflow;
- the user asks which assets were used;
- an eval or release check is inspecting this Pal.

Do not read assets here when:

- Mira is only doing initial routing;
- another Pal owns the task and no consultation was requested;
- the task is ordinary chat, Codex generic, or Mira-owned team-leadership work;
- examples, evals, reports, memory, or future design material would be enough only by curiosity rather than task need.
