# Atlas Skills Index

Each internal skill must use skills/<skill-id>/SKILL.md as the runtime entry. README.md remains human-readable notes.

## R02 Developer / Implementation Lead Skill Cards

These top-level Markdown skill cards strengthen Atlas's Developer / Implementation Lead job fitness. They complement the older directory-based `SKILL.md` assets and are used for PalSmith-style inspection, task package writing, and release review.

| Skill card | Purpose |
| --- | --- |
| `development-intake-skill.md` | Judge whether a request is ready for development planning, needs clarification, needs another Pal, or needs approval. |
| `implementation-planning-skill.md` | Turn a ready request into staged implementation work with file boundaries and verification. |
| `runtime-task-package-writing-skill.md` | Write Runtime Task Packages with goal, allowed reads/edits, forbidden files, evidence, risk, rollback, and report format. |
| `file-boundary-control-skill.md` | Prevent unrelated edits, broad refactors, and hidden generated-file churn. |
| `code-review-skill.md` | Review runtime changes for behavior, scope, tests, maintainability, security, and risk. |
| `test-strategy-skill.md` | Design automatic, manual, regression, browser, and not-run verification. |
| `regression-debugging-skill.md` | Convert regressions into minimal repair tasks with prevention evidence. |
| `release-engineering-skill.md` | Prepare release-readiness checks without claiming publication. |
| `evidence-based-verification-skill.md` | Map completion claims to current evidence criterion by criterion. |
| `developer-handoff-skill.md` | Hand bounded development work to runtimes or Pals through Context Packets. |
| `risk-and-approval-for-code-changes-skill.md` | Stop for user approval before risky code, system, release, or data changes. |
| `multi-agent-development-coordination-skill.md` | Coordinate development-shaped work with default Pals without active multi-agent execution claims. |

| Skill | Runtime entry | Human notes | Description |
| --- | --- | --- | --- |
| [architecture-review](architecture-review/SKILL.md) | skills/architecture-review/SKILL.md | [README](architecture-review/README.md) | Use this skill when you need to 检查开发方案、任务拆分或执行层结果是否破坏 AgentPal 的职责边界、模块分层和可维护性。 |
| [code-review-and-quality](code-review-and-quality/SKILL.md) | skills/code-review-and-quality/SKILL.md | [README](code-review-and-quality/README.md) | Use this skill when you need to 对执行层提交的改动做工程侧代码审查，关注行为、风险、边界和测试缺口。 |
| [context-engineering](context-engineering/SKILL.md) | skills/context-engineering/SKILL.md | [README](context-engineering/README.md) | Use this skill when you need to 为 Codex、Claude Code、OpenHands 或其他外部 Runtime 准备刚好够用的 Context Pack，避免把全部文档和无关记忆塞给执行层。 |
| [debugging-and-error-recovery](debugging-and-error-recovery/SKILL.md) | skills/debugging-and-error-recovery/SKILL.md | [README](debugging-and-error-recovery/README.md) | Use this skill when you need to 把错误日志、失败截图、测试失败和用户描述转成可执行的最小修复任务。 |
| [developer-task-intake](developer-task-intake/SKILL.md) | skills/developer-task-intake/SKILL.md | [README](developer-task-intake/README.md) | Use this skill when you need to 判断用户输入是否已经是合格开发任务，并决定下一步是补信息、转交其他 Pal，还是进入开发任务拆解。 |
| [execution-evidence-review](execution-evidence-review/SKILL.md) | skills/execution-evidence-review/SKILL.md | [README](execution-evidence-review/README.md) | Use this skill when you need to 审查执行层返回的 evidence 是否足以支持“任务完成”。完成报告不等于完成。 |
| [multi-thread-agent-dispatch](multi-thread-agent-dispatch/SKILL.md) | skills/multi-thread-agent-dispatch/SKILL.md | [README](multi-thread-agent-dispatch/README.md) | Use this skill when you need to 把中大型开发任务拆成 2-4 个互不重叠的执行线程，供 Codex、Claude Code 或其他执行层并行处理。 |
| [repository-handoff](repository-handoff/SKILL.md) | skills/repository-handoff/SKILL.md | [README](repository-handoff/README.md) | Use this skill when you need to 为执行层准备仓库级开发交接包，让 Codex、Claude Code、OpenHands 或外部 Runtime 快速理解项目上下文和边界。 |
| [requirement-to-agent-task](requirement-to-agent-task/SKILL.md) | skills/requirement-to-agent-task/SKILL.md | [README](requirement-to-agent-task/README.md) | Use this skill when you need to 把需求、Bug 或技术问题转成 Codex、Claude Code、OpenHands、Kimi、DeepSeek、Gemini CLI 等执行层可复制执行的开发任务提示词。 |
| [security-and-hardening](security-and-hardening/SKILL.md) | skills/security-and-hardening/SKILL.md | [README](security-and-hardening/README.md) | Use this skill when you need to 在开发任务进入执行前或执行结果返回后，检查命令、依赖、文件、凭据、权限、外部写入和日志脱敏等安全边界。 |
| [source-driven-development](source-driven-development/SKILL.md) | skills/source-driven-development/SKILL.md | [README](source-driven-development/README.md) | Use this skill when you need to 要求涉及第三方库、框架、API、Runtime 能力或项目内部约定时，先查可靠来源，避免凭记忆开发。 |
| [test-plan-writer](test-plan-writer/SKILL.md) | skills/test-plan-writer/SKILL.md | [README](test-plan-writer/README.md) | Use this skill when you need to 把开发任务转成可执行的测试计划、回归路径和 evidence 要求，让执行层知道怎么证明任务完成。 |

## Skill Memory Default

When the user explicitly asks to save a Skill, or similar operations happen more than 3 times, create the formal Skill under this Pal's own skills/<skill-id>/SKILL.md and update skills/index.md. Use memory/skill-memory/ only for runtime notes before either formal trigger is met; use learning/ only as an exception when required inputs are missing, content is unsafe/private, or a high-risk write needs approval.


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

## Formal Skill Asset Map

R13 formal skill mapping lives in `skill-asset-map.md`. It maps every `pal.json` formal skill to either a Flat Skill Card or a Directory Skill Package and records missing assets as release-readiness issues.
