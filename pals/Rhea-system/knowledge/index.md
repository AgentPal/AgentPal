# Rhea Knowledge Index

Rhea 的知识用于系统与应用维护任务判断，不是百科，也不是执行脚本集合。

## Built-In Knowledge

- `system/system-maintenance-principles.md`
- `system/risk-levels.md`
- `runtime/runtime-setup-basics.md`
- `runtime/agent-runtime-boundary.md`
- `environment/dev-environment-basics.md`
- `environment/path-and-version-check.md`
- `package-managers/package-manager-overview.md`
- `security/command-risk-boundary.md`
- `security/approval-required-actions.md`
- `evidence/system-evidence-format.md`
- `collaboration/system-to-code-collaboration.md`
- `collaboration/system-risk-review-collaboration.md`

## Rules

- 涉及当前版本、安装方式、价格、License、API、模型能力或平台政策时，必须刷新官方来源。
- 不保存真实用户数据、密钥、账号、私人日志或完整系统清单。
- 第三方资料保留原始 License。
- 高风险操作只进入审批请求和执行层 handoff，不进入自动执行规则。

## R04 System / Runtime Safety Lead Knowledge

- `system-runtime-role-knowledge.md`
- `runtime-capability-knowledge.md`
- `permission-boundary-knowledge.md`
- `least-privilege-knowledge.md`
- `no-code-boundary-knowledge.md`
- `file-directory-safety-knowledge.md`
- `risk-classification-knowledge.md`
- `approval-gate-knowledge.md`
- `evidence-based-operations-knowledge.md`
- `environment-troubleshooting-knowledge.md`
- `release-safety-knowledge.md`
- `incident-review-knowledge.md`
- `rollback-readiness-knowledge.md`
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
