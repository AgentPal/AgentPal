# Skills Index

Pal: Atlas

## Purpose

This directory lists Atlas-owned Pal Skills for Developer / Implementation Lead work.

These files are navigation and method assets only. They do not change Atlas identity, direct calls, routing, output contracts, runtime behavior, or central roster records.

## Pal Skill definition

A Pal Skill is a Pal-owned role-level work capability. It helps Atlas organize recurring development-shaped work through context, judgement, file boundaries, approval rules, Runtime Task Packages, verification, handoff, and memory or learning writeback.

Pal Skills may reference runtime tools, Agent Skills, workflows, runbooks, examples, and evals. The Pal Skill remains the organizational method; it does not execute commands by itself.

## Agent Skill boundary

This directory stores Pal Skills, not Runtime Agent Skills.

Agent Skills are host-runtime execution capabilities such as browser control, file editing, shell command use, package installation, GitHub CLI use, or test running. Agent Skills should be referenced as execution candidates, not copied into this directory.

Do not store raw CLI command docs as a Pal Skill unless they are rewritten as a Pal-owned method with context, approval, runtime boundary, verification, and memory writeback rules.

## What belongs here

- Atlas-owned methods for development intake, implementation planning, file boundary control, review, test strategy, regression debugging, release readiness, and Runtime Task Package writing.
- Skill packages or flat skill cards that include purpose, activation conditions, required context, output expectations, verification, and writeback rules.
- References to related Atlas knowledge, workflows, runbooks, examples, evals, and Agent Skill candidates.
- Public-safe notes that help a runtime load the smallest relevant Atlas asset slice.

## What does not belong here

- Runtime Agent Skills, plugins, MCP tools, tool installers, scanner configs, validator logic, API clients, connectors, daemons, or marketplace/hub programs.
- Keyword route maps, `keyword_map`, `domain_map`, `role_map`, or deterministic dispatch tables.
- Raw command manuals, copied runtime skill files, credentials, tokens, secrets, private project data, private user memory, reports, raw research dumps, or runtime state.
- New concrete Pal Skill content that has not been reviewed as an Atlas role-level method.

## Current assets

### Flat Skill Cards

These top-level Markdown skill cards strengthen Atlas's Developer / Implementation Lead job fitness. They complement the directory-based `SKILL.md` assets and are used for PalSmith-style inspection, task package writing, and release review.

| Skill card | Purpose | Status |
| --- | --- | --- |
| `development-intake-skill.md` | Judge whether a request is ready for development planning, needs clarification, needs another Pal, or needs approval. | present |
| `implementation-planning-skill.md` | Turn a ready request into staged implementation work with file boundaries and verification. | present |
| `runtime-task-package-writing-skill.md` | Write Runtime Task Packages with goal, allowed reads/edits, forbidden files, evidence, risk, rollback, and report format. | present |
| `file-boundary-control-skill.md` | Prevent unrelated edits, broad refactors, and hidden generated-file churn. | present |
| `code-review-skill.md` | Review runtime changes for behavior, scope, tests, maintainability, security, and risk. | present |
| `test-strategy-skill.md` | Design automatic, manual, regression, browser, and not-run verification. | present |
| `regression-debugging-skill.md` | Convert regressions into minimal repair tasks with prevention evidence. | present |
| `release-engineering-skill.md` | Prepare release-readiness checks without claiming publication. | present |
| `evidence-based-verification-skill.md` | Map completion claims to current evidence criterion by criterion. | present |
| `developer-handoff-skill.md` | Hand bounded development work to runtimes or Pals through Context Packets. | present |
| `risk-and-approval-for-code-changes-skill.md` | Stop for user approval before risky code, system, release, or data changes. | present |
| `multi-agent-development-coordination-skill.md` | Coordinate development-shaped work with default Pals without active multi-agent execution claims. | present |

### Directory Skill Packages

Each internal skill package uses `skills/<skill-id>/SKILL.md` as the runtime entry. `README.md` files remain human-readable notes.

| Skill | Runtime entry | Human notes | Description | Status |
| --- | --- | --- | --- | --- |
| [architecture-review](architecture-review/SKILL.md) | `skills/architecture-review/SKILL.md` | [README](architecture-review/README.md) | Use this skill when you need to 检查开发方案、任务拆分或执行层结果是否破坏 AgentPal 的职责边界、模块分层和可维护性。 | present |
| [code-review-and-quality](code-review-and-quality/SKILL.md) | `skills/code-review-and-quality/SKILL.md` | [README](code-review-and-quality/README.md) | Use this skill when you need to 对执行层提交的改动做工程侧代码审查，关注行为、风险、边界和测试缺口。 | present |
| [context-engineering](context-engineering/SKILL.md) | `skills/context-engineering/SKILL.md` | [README](context-engineering/README.md) | Use this skill when you need to 为 Codex、Claude Code、OpenHands 或其他外部 Runtime 准备刚好够用的 Context Pack，避免把全部文档和无关记忆塞给执行层。 | present |
| [debugging-and-error-recovery](debugging-and-error-recovery/SKILL.md) | `skills/debugging-and-error-recovery/SKILL.md` | [README](debugging-and-error-recovery/README.md) | Use this skill when you need to 把错误日志、失败截图、测试失败和用户描述转成可执行的最小修复任务。 | present |
| [developer-task-intake](developer-task-intake/SKILL.md) | `skills/developer-task-intake/SKILL.md` | [README](developer-task-intake/README.md) | Use this skill when you need to 判断用户输入是否已经是合格开发任务，并决定下一步是补信息、转交其他 Pal，还是进入开发任务拆解。 | present |
| [execution-evidence-review](execution-evidence-review/SKILL.md) | `skills/execution-evidence-review/SKILL.md` | [README](execution-evidence-review/README.md) | Use this skill when you need to 审查执行层返回的 evidence 是否足以支持“任务完成”。完成报告不等于完成。 | present |
| [multi-thread-agent-dispatch](multi-thread-agent-dispatch/SKILL.md) | `skills/multi-thread-agent-dispatch/SKILL.md` | [README](multi-thread-agent-dispatch/README.md) | Use this skill when you need to 把中大型开发任务拆成 2-4 个互不重叠的执行线程，供 Codex、Claude Code 或其他执行层并行处理。 | present |
| [repository-handoff](repository-handoff/SKILL.md) | `skills/repository-handoff/SKILL.md` | [README](repository-handoff/README.md) | Use this skill when you need to 为执行层准备仓库级开发交接包，让 Codex、Claude Code、OpenHands 或外部 Runtime 快速理解项目上下文和边界。 | present |
| [requirement-to-agent-task](requirement-to-agent-task/SKILL.md) | `skills/requirement-to-agent-task/SKILL.md` | [README](requirement-to-agent-task/README.md) | Use this skill when you need to 把需求、Bug 或技术问题转成 Codex、Claude Code、OpenHands、Kimi、DeepSeek、Gemini CLI 等执行层可复制执行的开发任务提示词。 | present |
| [security-and-hardening](security-and-hardening/SKILL.md) | `skills/security-and-hardening/SKILL.md` | [README](security-and-hardening/README.md) | Use this skill when you need to 在开发任务进入执行前或执行结果返回后，检查命令、依赖、文件、凭据、权限、外部写入和日志脱敏等安全边界。 | present |
| [source-driven-development](source-driven-development/SKILL.md) | `skills/source-driven-development/SKILL.md` | [README](source-driven-development/README.md) | Use this skill when you need to 要求涉及第三方库、框架、API、Runtime 能力或项目内部约定时，先查可靠来源，避免凭记忆开发。 | present |
| [test-plan-writer](test-plan-writer/SKILL.md) | `skills/test-plan-writer/SKILL.md` | [README](test-plan-writer/README.md) | Use this skill when you need to 把开发任务转成可执行的测试计划、回归路径和 evidence 要求，让执行层知道怎么证明任务完成。 | present |

Supporting files:

| Asset | Purpose | Status |
| --- | --- | --- |
| `README.md` | Human-readable skills directory note. | present |
| `skill-asset-map.md` | Formal skill mapping from `pal.json` skills to flat cards or directory packages. | present |

## Candidate skills / needs review

| Candidate | Reason | Review status |
| --- | --- | --- |
| none added in R106-B | This batch is index-only and must not create new Atlas skill content. | not-run |

If future Atlas Agent Skill candidates appear in runtime registries, review them separately before referencing them here.

## Agent Skill references

Atlas Pal Skills may reference host-runtime execution capabilities such as file editing, test running, package management, Git commands, browser checks, or GitHub CLI commands only as runtime evidence candidates.

References do not install, enable, probe, or execute Agent Skills. Runtime execution requires current-runtime evidence and the allowed file/command boundary named by the active task.

## Related workflows / runbooks

- `../workflows/index.md`
- `../workflows/development-lifecycle/`
- `../runbooks/index.md`
- `../runbooks/debugging/`
- `../runbooks/testing/`

## Verification boundary

Atlas may organize development verification, but completion claims require current runtime evidence. Use `pass`, `fail`, `blocked`, `not-run`, `missing`, or an equivalent explicit status instead of smoothing weak evidence into a pass.

Do not treat directory presence, skill names, or owner claims as proof that a runtime action was executed.

## Memory writeback boundary

When the user explicitly asks to save a Skill, or similar operations happen more than three times, create the formal Skill under this Pal's own `skills/<skill-id>/SKILL.md` and update this index in a separate allowed task.

Use `memory/skill-memory/` only for runtime notes before a formal trigger is met. Use `learning/` only when required inputs are missing, content is unsafe/private, or a high-risk write needs approval.

Reports are not memory until stable lessons are extracted. Do not write report text into memory wholesale.

## External project boundary

Do not copy Atlas Pal Skills into an external project `.agentpal/` directory by default.

External projects remain thin-bound. Pal Skills, Pal memory, workflows, runbooks, reports, governance notes, and reusable knowledge stay in the AgentPal central workspace or approved central records.

## Context loading rule

Read this index only after Atlas is selected as owner, consultant, reviewer, or direct `/pal Atlas` target.

Use this index to choose the smallest relevant asset slice. Do not load every file in this directory by default.

Read assets here when:

- the current task requires Atlas's professional method;
- the output contract needs a specific skill, knowledge card, runbook, or workflow;
- the user asks which assets were used;
- an eval or release check is inspecting Atlas.

Do not read assets here when:

- Mira is only doing initial routing;
- another Pal owns the task and no consultation was requested;
- the task is ordinary chat, Codex generic, or Mira-owned team-leadership work;
- examples, evals, reports, memory, or future design material would be enough only by curiosity rather than task need.
