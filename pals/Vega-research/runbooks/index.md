# Vega Runbooks Index

Runbook 指导 Vega 如何组织研究任务和复验结果，不直接执行搜索、下载、命令或代码修改。

## Built-In Runbooks

| id | path | purpose |
|---|---|---|
| github-project-evaluation | `runbooks/open-source-evaluation/github-project-evaluation.md` | 评估 GitHub 项目是否适合导入、reference-only 或逐案请从当前 contacts / registry 解析出的合适协作对象补充 |
| technology-selection | `runbooks/technical-research/technology-selection.md` | 组织技术选型研究和多方案比较 |
| knowledge-card-creation | `runbooks/knowledge/knowledge-card-creation.md` | 将研究结果转成知识卡候选 |
| fact-checking-workflow | `runbooks/source-verification/fact-checking-workflow.md` | 拆分待核查断言、寻找来源、处理冲突并输出事实核查结论 |
| research-tool-shortlist | `runbooks/tool-evaluation/research-tool-shortlist.md` | 从研究工具目录或候选列表中筛选 reference-only、public-card、reject 等处理方式 |

## R3 Boundary

新增 Runbook 是 Vega 自有表达，不复制第三方原文。它们指导 Vega 如何组织研究任务，不执行搜索、下载、安装、上传或外部写入。

## R03 Research / Intelligence Lead Runbooks

- `quick-research-runbook.md`
- `deep-research-runbook.md`
- `source-quality-review-runbook.md`
- `competitive-research-runbook.md`
- `technical-option-research-runbook.md`
- `research-to-pal-knowledge-runbook.md`


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
