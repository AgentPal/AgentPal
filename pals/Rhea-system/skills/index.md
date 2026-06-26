# Rhea Skills Index

Each internal skill must use skills/<skill-id>/SKILL.md as the runtime entry. README.md remains human-readable notes.

| Skill | Runtime entry | Human notes | Description |
| --- | --- | --- | --- |
| [app-installation-handoff](app-installation-handoff/SKILL.md) | skills/app-installation-handoff/SKILL.md | [README](app-installation-handoff/README.md) | Use this skill when you need to 为软件安装生成安全、可审批、可验证的执行层任务包。 |
| [approval-request-writer](approval-request-writer/SKILL.md) | skills/approval-request-writer/SKILL.md | [README](approval-request-writer/README.md) | Use this skill when you need to 把需要用户确认的安装、卸载、删除、权限、环境变量或系统写入动作，写成清楚、可判断的审批请求。 |
| [command-plan-review](command-plan-review/SKILL.md) | skills/command-plan-review/SKILL.md | [README](command-plan-review/README.md) | Use this skill when you need to 把执行层计划运行的命令或动作翻译成人能理解的影响、风险、审批点和证据要求。 |
| [dependency-version-check](dependency-version-check/SKILL.md) | skills/dependency-version-check/SKILL.md | [README](dependency-version-check/README.md) | Use this skill when you need to 检查开发任务所需依赖、版本、PATH 和项目配置是否匹配。 |
| [environment-diagnosis-plan](environment-diagnosis-plan/SKILL.md) | skills/environment-diagnosis-plan/SKILL.md | [README](environment-diagnosis-plan/README.md) | Use this skill when you need to 把环境异常整理成只读诊断任务，帮助执行层检查命令是否存在、版本是否正确、PATH 是否可用、依赖是否缺失。 |
| [failure-recovery-plan](failure-recovery-plan/SKILL.md) | skills/failure-recovery-plan/SKILL.md | [README](failure-recovery-plan/README.md) | Use this skill when you need to 为失败命令、安装失败、依赖失败或环境修复失败生成可回滚、可复验的恢复计划。 |
| [local-tool-discovery](local-tool-discovery/SKILL.md) | skills/local-tool-discovery/SKILL.md | [README](local-tool-discovery/README.md) | Use this skill when you need to 识别当前机器或 Runtime 可用的包管理器、开发工具、Agent、Skill、插件、MCP、hooks 和 commands。 |
| [maintenance-report-writer](maintenance-report-writer/SKILL.md) | skills/maintenance-report-writer/SKILL.md | [README](maintenance-report-writer/README.md) | Use this skill when you need to 把系统维护、安装配置、故障排查和执行层结果整理成用户可读的维护报告。 |
| [permission-risk-review](permission-risk-review/SKILL.md) | skills/permission-risk-review/SKILL.md | [README](permission-risk-review/README.md) | Use this skill when you need to 审查任务是否涉及管理员权限、sudo、系统目录、注册表、服务、启动项、安全软件、外发数据或敏感路径。 |
| [runtime-setup-handoff](runtime-setup-handoff/SKILL.md) | skills/runtime-setup-handoff/SKILL.md | [README](runtime-setup-handoff/README.md) | Use this skill when you need to 为 Codex、Claude Code、OpenHands、Gemini CLI、DeepSeek-TUI 等 Runtime / Agent 的安装、检测和配置生成执行层 handoff。 |
| [system-evidence-review](system-evidence-review/SKILL.md) | skills/system-evidence-review/SKILL.md | [README](system-evidence-review/README.md) | Use this skill when you need to 审查执行层返回的安装、卸载、修复、检测或配置结果是否足以证明任务完成。 |
| [system-task-intake](system-task-intake/SKILL.md) | skills/system-task-intake/SKILL.md | [README](system-task-intake/README.md) | Use this skill when you need to 判断用户请求属于系统、应用、Runtime、依赖、权限、PATH、进程、磁盘、包导入还是故障恢复问题，并确定下一步是否只能先做只读检测。 |

## R04 System / Runtime Safety Lead Skill Cards

- `runtime-capability-assessment-skill.md`
- `permission-boundary-review-skill.md`
- `no-code-boundary-audit-skill.md`
- `file-directory-safety-review-skill.md`
- `risk-classification-skill.md`
- `approval-gate-design-skill.md`
- `execution-evidence-review-skill.md`
- `environment-troubleshooting-skill.md`
- `release-safety-review-skill.md`
- `rollback-readiness-review-skill.md`
- `incident-review-skill.md`
- `runtime-task-package-safety-briefing-skill.md`

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
