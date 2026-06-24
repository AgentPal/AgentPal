# Quinn Skills Index

Each internal skill must use skills/<skill-id>/SKILL.md as the runtime entry. README.md remains human-readable notes.

| Skill | Runtime entry | Human notes | Description |
| --- | --- | --- | --- |
| [acceptance-criteria-review](acceptance-criteria-review/SKILL.md) | skills/acceptance-criteria-review/SKILL.md | [README](acceptance-criteria-review/README.md) | Use this skill when you need to 检查目标和验收标准是否清楚、可验证、覆盖关键路径。 |
| [bug-reproduction-review](bug-reproduction-review/SKILL.md) | skills/bug-reproduction-review/SKILL.md | [README](bug-reproduction-review/README.md) | Use this skill when you need to 审查 Bug 复现材料是否足以交给执行层定位和修复。 |
| [change-scope-review](change-scope-review/SKILL.md) | skills/change-scope-review/SKILL.md | [README](change-scope-review/README.md) | Use this skill when you need to 检查变更范围、影响文件、依赖变化和架构边界是否清楚。 |
| [evidence-audit](evidence-audit/SKILL.md) | skills/evidence-audit/SKILL.md | [README](evidence-audit/README.md) | Use this skill when you need to 审查 Runtime、Agent 或交付报告提供的证据是否足以支撑完成声明。 |
| [quality-report-writer](quality-report-writer/SKILL.md) | skills/quality-report-writer/SKILL.md | [README](quality-report-writer/README.md) | Use this skill when you need to 把审查结论、证据、风险、缺口和下一步整理成可交接报告。 |
| [quality-task-intake](quality-task-intake/SKILL.md) | skills/quality-task-intake/SKILL.md | [README](quality-task-intake/README.md) | Use this skill when you need to 识别审查对象、验收目标、证据缺口和应调用的 Quinn Skill。 |
| [regression-plan-writer](regression-plan-writer/SKILL.md) | skills/regression-plan-writer/SKILL.md | [README](regression-plan-writer/README.md) | Use this skill when you need to 按改动范围和风险设计核心路径、边界和回归测试计划。 |
| [release-gate-review](release-gate-review/SKILL.md) | skills/release-gate-review/SKILL.md | [README](release-gate-review/README.md) | Use this skill when you need to 检查发布前功能、证据、风险、回滚、说明和人工确认是否齐备。 |
| [risk-assessment](risk-assessment/SKILL.md) | skills/risk-assessment/SKILL.md | [README](risk-assessment/README.md) | Use this skill when you need to 识别产品、技术、安全、隐私、发布和高风险行业风险并分级。 |
| [rollback-readiness-review](rollback-readiness-review/SKILL.md) | skills/rollback-readiness-review/SKILL.md | [README](rollback-readiness-review/README.md) | Use this skill when you need to 检查发布、迁移、删除、配置和数据变更是否具备回滚或降级路径。 |
| [security-privacy-review](security-privacy-review/SKILL.md) | skills/security-privacy-review/SKILL.md | [README](security-privacy-review/README.md) | Use this skill when you need to 做基础安全、权限、敏感信息和外发隐私检查。 |
| [test-case-design](test-case-design/SKILL.md) | skills/test-case-design/SKILL.md | [README](test-case-design/README.md) | Use this skill when you need to 为功能、流程、文档或 Agent 任务生成可验收的测试用例。 |

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
