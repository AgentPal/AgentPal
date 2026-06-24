# Workflows Index

Atlas Workflows 是多步骤开发流程。它们不是第三方 Skill，也不直接执行代码。

## Built-In Workflows

| id | path | purpose |
|---|---|---|
| development-lifecycle | `workflows/development-lifecycle/` | 从任务定义、计划、交接、执行回收、复验到记忆更新的开发闭环 |

## Skill Coordination

`development-lifecycle` 串联当前 12 个正式 Skill：

- `developer-task-intake`：判断任务是否准备好。
- `requirement-to-agent-task`：生成执行层任务。
- `context-engineering`：准备 Context Pack。
- `source-driven-development`：要求官方来源或本地文档。
- `multi-thread-agent-dispatch`：拆分多线程任务。
- `test-plan-writer`：定义测试和 evidence。
- `architecture-review`：检查架构边界。
- `security-and-hardening`：检查安全边界。
- `execution-evidence-review`：复验完成报告。

外部 workflow 思路必须先进入 skill-card 或内部评估，再改写为 Atlas 自有表达。


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
