# Vega Knowledge Index

Vega 的知识不是世界百科，而是“如何可靠地做研究”的方法库。

## Core Knowledge

- `identity/vega-role.md`
- `identity/vega-boundary.md`
- `research/research-principles.md`
- `research/research-task-types.md`
- `research/fact-inference-opinion.md`
- `research/source-quality.md`
- `research/freshness-and-staleness.md`
- `research/evidence-strength.md`
- `search/query-design.md`
- `open-source/github-project-evaluation.md`
- `open-source/license-basics.md`
- `reports/research-report-structure.md`
- `reports/knowledge-card-format.md`
- `collaboration/research-implementation-collaboration.md`
- `collaboration/research-web-collaboration.md`
- `agent-skills/agent-skill-resource-evaluation.md`
- `academic/academic-source-review.md`

## Boundary

Vega 默认不内置论文全文、付费报告全文、新闻全文归档、用户公司内部资料、API key、爬虫脚本、投资模型、法律/医疗/财税最终判断或具体行业法规全文。

外部资料先进入 `imports/` 和 `registry/`，经过来源、时间、License、隐私和可信度检查后，才可能沉淀为知识卡候选。

## R3 Additions

- Agent Skill resource evaluation：帮助 Vega 判断外部 Skill、Tool、Knowledge、Persona、Workflow 和 Pal Pack 的区别。
- Academic source review：帮助 Vega 处理论文、预印本、学术报告和引用信息，不复制论文正文。

## R03 Research / Intelligence Lead Knowledge

- `research-role-knowledge.md`
- `research-question-framing-knowledge.md`
- `search-strategy-knowledge.md`
- `source-credibility-knowledge.md`
- `source-inventory-knowledge.md`
- `evidence-matrix-knowledge.md`
- `claim-evidence-knowledge.md`
- `research-synthesis-knowledge.md`
- `comparative-analysis-knowledge.md`
- `uncertainty-confidence-knowledge.md`
- `knowledge-distillation-knowledge.md`
- `research-ethics-and-copyright-boundary-knowledge.md`
- `default-pal-collaboration-boundaries.md`


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
