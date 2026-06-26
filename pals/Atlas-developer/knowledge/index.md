# Atlas Knowledge Index

Atlas 的知识不是“所有编程知识百科”。它服务于开发任务如何被说清楚、交给执行层、验证结果并守住边界。

## R02 Developer / Implementation Lead Knowledge

- `developer-role-knowledge.md` - Atlas as Developer / Implementation Lead, not runtime.
- `implementation-planning-knowledge.md` - staged implementation planning and acceptance.
- `runtime-task-package-knowledge.md` - high-quality Runtime Task Package standards.
- `file-boundary-knowledge.md` - allowed/forbidden file discipline and scope control.
- `code-review-knowledge.md` - code review findings, severity, scope, and evidence.
- `test-strategy-knowledge.md` - automatic/manual/regression verification design.
- `regression-debugging-knowledge.md` - old behavior, broken behavior, minimal repair, prevention.
- `release-engineering-knowledge.md` - release readiness, evidence, artifacts, rollback.
- `definition-of-done-knowledge.md` - completion as evidence, not completion report.
- `evidence-based-verification-knowledge.md` - criterion-by-criterion evidence review.
- `multi-agent-development-knowledge.md` - case-specific Pal collaboration for development-shaped tasks.
- `no-code-agentpal-boundary-knowledge.md` - AgentPal no-code release boundary.
- `default-pal-collaboration-boundaries.md` - Atlas with Mira / PalSmith / Vega / Rhea / Quinn / Morgan / Harper / Nova.

## Core Knowledge

- `identity/atlas-role.md`
- `identity/atlas-boundary.md`
- `agentpal-boundary/core-is-not-agent.md`
- `agentpal-architecture/pal-brain-runtime.md`
- `runtime/evidence-review-checklist.md`
- `agents/codex-dev-task-format.md`
- `agents/claude-code-handoff.md`
- `prompt/dev-task-prompt-structure.md`
- `prompt/model-selection.md`
- `prompt/reasoning-strength.md`
- `parallel-dev/multi-thread-agent-dispatch.md`
- `testing/manual-test-plan.md`
- `code-review/review-checklist.md`
- `debugging/debugging-process.md`
- `collaboration/default-pal-map.md`

## D4 Skill Support Knowledge

- `testing/test-plan-basics.md`
- `architecture/architecture-review-checklist.md`
- `context/context-pack-design.md`
- `source-driven/official-source-rules.md`
- `security/development-security-boundary.md`

## Boundary

深入框架、语言、依赖版本和第三方库资料，应在任务时由 Runtime、外部调研 Pal 或官方文档补充，不默认塞入 Atlas。


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
