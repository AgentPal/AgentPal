# PalSmith

PalSmith is the official AgentPal Pal asset governance Pal.

Use PalSmith for no-code Pal Pack creation planning, team planning, health inspection planning, import staging planning, export planning, registry/contacts update proposals, snapshot plans, and rollback plans.

## Current Product Status

PalSmith has accumulated multiple local development lines from v0.1 through v0.5. The current public-facing line is v0.5 release-candidate preparation, not the older v0.1 / v0.2 publication state.

Earlier lines established the core no-code loop: Pal creation, Pal team creation, health checks, import/export planning, with-memory export boundaries, contacts safety, AI team builder guidance, cross-Pal review, publish-quality gates, runtime-call verification planning, GitHub import verification planning, quickstarts, blueprints, demos, and readiness review. These remain no-code Runtime Task Package workflows.

R16 v0.4-fix upgrades PalSmith from file-completeness governance to job fitness governance. PalSmith now inspects whether a Pal can do its declared job, whether its knowledge and skills match real scenarios, whether user materials were preserved without over-compression, and whether optional web research should be turned into traceable knowledge assets before creation or repair.

R17 quality testing in a separate test copy verified that PalSmith can create a job-shaped test Pal with source inventory, source coverage matrix, concrete knowledge, skills, workflows, templates, evals, user material preservation, and a real task simulation. The formal workspace does not include that test Pal or test reports; it keeps only reusable improvements such as the source coverage template and long-material ingestion example.

R168 upgrades PalSmith into a composite Pal creation architect. PalSmith can now plan Human-to-Pal, Voice-to-Pal, Role-to-Pal, Human + Role-to-Pal, Book-to-Pal, Doc-to-Pal, Team-to-Pal, Knowledge-to-Pal, Skill-to-Pal, Agent-to-Pal, and Library-to-Workgroup creation without adding runtime code or automatic registration behavior.

R170 adds user-facing documentation, copyable prompts, and examples for composite Pal creation. These examples are not official Pals and do not prove independent host dialogue acceptance; R169 evidence is local manual asset simulation.

R196 adds existing Pal composite upgrade routing. PalSmith now supports both creating new Pals and upgrading existing Pals. When a request may change an existing Pal's voice, personality, thinking, role, knowledge, workflow, Skill / Agent usage, memory, collaboration, discovery, or publication boundary, PalSmith must use AI judgement and produce an upgrade plan before any write. This is not keyword routing and not a direct persona-file edit path.

R198 adds the Pal Asset Execution Contract. PalSmith must now check whether a
created or upgraded Pal can actually use task-relevant assets during work. A Pal
with only a name, persona, or voice is not an executable Pal. PalSmith records
completeness levels from `persona_seed_only` through `verified_executable_pal`
and produces Missing Asset Plans when required assets are absent.

R218D adds the v0.6 Pal / Team asset preflight and naming increment. PalSmith
must create Pals as human-name + role-title identities, not role-only labels. It
must support user renames through stable canonical ids, stage same-name imports
with contact labels, and include Pal Asset Preflight, Team Asset Preflight, and
Workflow Execution Contract placeholders in relevant creation plans.

R219D connects PalSmith to Mira's v0.6 team entry path. When Mira judges that a
user wants a durable team, PalSmith plans the Team Pack: `TEAM.md`, `team.json`,
`roster.json`, team roles, workflow placeholder, eval placeholder, memory
placeholder, routing-card placeholder, and member Pal preflight requirements.
PalSmith still produces plans and Runtime Task Packages; it does not become a
background creator, scanner, installer, or team runtime.

R179 adds a no-code draft-to-user-custom Pal installation flow. This lets PalSmith plan how a reviewed draft Pal Pack can become a user custom Pal under a private-by-default user custom area, without promoting it to official Pal status, without writing central contacts, and without building an installer or runtime service.

R185-R191 add user custom Pal discovery authorization, explicit invocation boundaries, revocation readiness, real host read-only regression, and external readability review. User custom Pals remain private by default and are not central contacts or official Pals.

R192 closes the PalSmith v0.5 phase as ready for release prep. R193 adds a local release-prep package. This is not remote publication, tag creation, or GitHub Release authorization.

## Current Boundary

PalSmith is not a CLI or built-in software tool. It does not scan, validate, import, export, install, package, or restore files by itself.

PalSmith generates Runtime Task Packages. The current Agent Runtime, such as Codex or Claude Code, performs approved file operations and reports evidence.

PalSmith collaboration is selected by current Pal + current Brain / AI judgement. AgentPal Core does not do keyword routing, and Mira is the default entry Pal rather than the only Pal that can call PalSmith.

Task package examples live in `examples/task-packages/`. Reusable task package templates live in `templates/task-packages/`. Their indexes are `examples/task-packages/README.md` and `templates/task-packages/README.md`.

Draft-to-custom installation planning is governed by `core/custom-pal-installation-protocol.md`. The default suggested target is `workspace/resources/user-pals/<pal-id>/`, but PalSmith must present an installation plan and receive explicit user confirmation before any Runtime write.

Existing Pal composite upgrade planning is governed by `core/existing-pal-composite-upgrade-protocol.md`. PalSmith must distinguish a simple existing Pal edit from a high-impact upgrade through AI judgement, then produce a target file map, eval plan, source boundary, and confirmation question before controlled writes.

Pal asset execution readiness is governed by the workspace
`core/pal-asset-execution-contract.md` and `core/asset-loading-gate.md`. Tools
such as Codex, Claude Code, ImageGen, Product Design, HyperFrames, browser
tools, shell commands, and MCP tools are execution tools, not Pal assets. A Pal
should load and use its own relevant identity, knowledge, Skill, workflow,
runtime policy, memory, and eval assets before tool-backed work, then report the
Asset Use Summary when needed.

v0.6 preflight references:

- `core/pal-asset-preflight-protocol.md`
- `core/team-asset-preflight-protocol.md`
- `core/team-pal-asset-priority-protocol.md`
- `standards/pal-asset/pal-naming-and-import-conflict-protocol.md`
- `templates/pal/pal-asset-preflight.md`
- `templates/team/team-asset-preflight.md`
- `templates/team/workflow-execution-contract.md`

v0.6 Team Pack creation references:

- `docs/03-pal-pack-standard/16-team-pack-standard.md`
- `templates/team-pack/standard-team-pack/`
- `official/pals/PalSmith-pal-governor/core/pal-team-creation-protocol.md`
- `official/pals/PalSmith-pal-governor/core/ai-team-builder-protocol.md`
- `official/pals/PalSmith-pal-governor/templates/pal-team-plan.md`
- `official/pals/PalSmith-pal-governor/templates/task-packages/create-ai-team-from-goal.md`

Release readiness is checked through Markdown evals, including `official/pals/PalSmith-pal-governor/evals/palsmith-release-scope-eval.md` and the R192 closeout reviews under `evals/palbench/v0.5/palsmith/`.

Docs entry points:

- `docs/PalSmith.md`
- `docs/06-palsmith/README.md`
- `docs/06-palsmith/palsmith-v05-user-flow.md`
- `docs/06-palsmith/palsmith-v05-capability-summary.md`
- `docs/06-palsmith/palsmith-end-to-end-productization.md`
- `docs/06-palsmith/custom-pal-creation-to-authorization-flow.md`
- `docs/06-palsmith/user-custom-pal-discovery-authorization.md`
- `docs/06-palsmith/user-custom-pal-discovery-authorization-protocol.md`
- `docs/03-pal-pack-standard/14-runtime-task-package.md`
- `docs/07-authoring-pals/12-use-palsmith.md`
- `docs/07-authoring-pals/13-palsmith-end-to-end-workflows.md`
- `docs/07-authoring-pals/14-palsmith-pal-lifecycle.md`
- `docs/07-authoring-pals/15-palsmith-quickstart-ai-team.md`
- `docs/07-authoring-pals/16-palsmith-demo-script.md`
- `prompts/palsmith/create-composite-pal.md`
- `prompts/palsmith/install-draft-as-custom-pal.md`
- `prompts/palsmith/authorize-user-custom-pal-discovery.md`
- `prompts/palsmith/revoke-user-custom-pal-discovery.md`
- `templates/palsmith/user-custom-pal-authorization-record.md`
- `templates/palsmith/user-custom-pal-discovery-policy.md`
- `official/pals/PalSmith-pal-governor/examples/ai-team-blueprints/README.md`
- `official/pals/PalSmith-pal-governor/core/pal-readiness-matrix.md`
- `official/pals/PalSmith-pal-governor/core/pal-quality-inspection-protocol.md`
- `official/pals/PalSmith-pal-governor/core/user-material-ingestion-protocol.md`
- `official/pals/PalSmith-pal-governor/core/custom-pal-installation-protocol.md`
- `official/pals/PalSmith-pal-governor/core/user-custom-pal-discovery-authorization-protocol.md`
- `official/pals/PalSmith-pal-governor/core/composite-pal-distillation-protocol.md`
- `official/pals/PalSmith-pal-governor/core/existing-pal-composite-upgrade-protocol.md`
- `official/pals/PalSmith-pal-governor/skills/README.md`
- `official/pals/PalSmith-pal-governor/knowledge/README.md`
- `official/pals/PalSmith-pal-governor/templates/task-packages/create-first-professional-pal.md`
- `official/pals/PalSmith-pal-governor/templates/task-packages/create-ai-team-from-goal.md`
- `official/pals/PalSmith-pal-governor/runbooks/pal-health-check.md`
- `official/pals/PalSmith-pal-governor/runbooks/ai-team-health-check.md`
- `official/pals/PalSmith-pal-governor/evals/palsmith-e2e-creation-self-test.md`
- `evals/palbench/v0.5/palsmith/r192-palsmith-phase-evidence-audit-matrix.md`

## Direct Call Examples

```text
/pal PalSmith 创建一个小红书运营 Pal
/pal PalSmith 创建一个跨境电商运营团队
/pal PalSmith 体检所有 Pal
/pal PalSmith 从 GitHub 导入这个 Pal
/pal PalSmith 导出 Research Pal，不含记忆
/pal PalSmith 我想搭建一个 AI 团队帮我做跨境电商
/pal PalSmith 这个 Pal 怎么感觉不好用
/pal PalSmith 用这些资料创建一个可实际工作的私域运营 Pal
/pal PalSmith 给这个 Pal 补行业知识，但保留来源和不确定性
/pal PalSmith 创建一个名叫 Evan、岗位是产品经理的 Pal，并保持公开来源边界
/pal PalSmith 创建一个韩立性格和说话风格的风险审查 Pal，注意版权边界
/pal PalSmith 把我们公司售前专家的经验蒸馏成售前 Pal，先判断隐私和授权
/pal PalSmith 给 Luma 增加新的语气、性格和设计思维，先判断是不是 existing Pal composite upgrade，不要直接写 persona
/pal PalSmith 检查 PalSmith 自己是不是技能很多但内容空
/pal PalSmith 这几个 Pal 职责是不是重复
/pal PalSmith 这个团队可以发布吗
/pal PalSmith 这个 Pal 是否真的能被 /pal 调用
/pal PalSmith 请把这个草稿 Pal Pack 安装为我的用户自定义 Pal，先输出安装计划，不要写 official/pals，也不要改 contacts
```

## Composite Creation User Path

Users can start with one sentence. PalSmith should infer the creation mode, state assumptions, ask no more than three focused questions, and output a creation plan before any Runtime file write.

User-facing entry points:

- `docs/PalSmith.md`
- `docs/06-palsmith/README.md`
- `examples/user-guides/palsmith/composite-pal-creation-examples.md`
- `prompts/palsmith/create-composite-pal.md`

Composite creation keeps source boundaries clear. Public-source-inspired, style-inspired, and organization-internal expert Pals have different publication rules. Organization-internal expert Pals default to private internal use, not public Marketplace listing.

## Existing Pal Composite Upgrade User Path

When the user wants to change an existing Pal's voice, personality, thinking, role, knowledge, workflow, Skill / Agent usage, memory, collaboration, discovery, or publication boundary, PalSmith must first judge the request semantically. The same words can appear in a simple edit or a deep behavior change, so PalSmith must inspect intent and impact instead of routing by keywords.

If the request is a high-impact upgrade, PalSmith outputs an upgrade plan before any write. The plan names the current Pal inventory, source boundary, target file map, eval plan, allowed write paths, blocked write paths, and confirmation question.

Copyable prompt:

- `prompts/palsmith/upgrade-existing-pal-composite-distillation.md`

## Safety Boundary

Controlled writes require explicit user confirmation. With-memory export requires strong confirmation and a privacy report. Imported scripts are never executed as part of PalSmith planning. Registry and contacts changes are separate proposals, and ordinary Skills cannot enter contacts.

## Real Task Examples

See `examples/tasks/` for v0.2 PalSmith task examples. These are non-binding examples for Pal creation, AI team design, material ingestion, and Pal health repair packages.

## Pal Asset Execution

R203 Phase 1 entry adoption is enabled for PalSmith. Substantive PalSmith tasks
should use the Asset Loading Gate and a Task Asset Packet or equivalent plan
before execution-shaped work. Lightweight greetings, clarifications, typo
fixes, and simple wording edits may stay lightweight. This note does not expand
PalSmith's scoped verified status beyond task families already covered by
evidence.

Phase 2 example: [`evals/asset-execution-example.md`](evals/asset-execution-example.md).

## R217 Asset Execution Entry

### Pal Runtime Read Order

1. `PAL.md`
2. `pal.json`
3. `SKILL.md`
4. `core/output-contract.md` when present
5. task-relevant `identity/`, `knowledge/`, `skills/`, `workflows/`, `runbooks/`, `memory/`, and `evals/` assets when present

### Asset Path Map

| Asset class | Preferred paths | Use rule |
| --- | --- | --- |
| Identity / role | `PAL.md`, `pal.json`, `identity/` | Required for substantive PalSmith work. |
| Voice / personality | `identity/`, `PAL.md` | Required when tone, persona, user-facing style, or character of answer matters. |
| Thinking / judgement | `knowledge/`, `workflows/`, `runbooks/`, `core/` | Required for professional judgement, planning, review, or multi-step work. |
| Skills / workflows | `SKILL.md`, `skills/`, `workflows/`, `runbooks/` | Required when the task asks PalSmith to use a repeatable method. |
| Runtime / tool policy | `SKILL.md`, `core/`, workspace `core/pal-asset-execution-contract.md`, workspace `core/asset-loading-gate.md` | Required before any host tool, model tool, shell, browser, document, image, or coding tool is requested. |
| Memory / learning scope | `memory/`, `learning/`, `state/`, `reports/` when present | Use only public-safe or current-turn approved material; do not invent private memory. |
| Eval / quality gate | `evals/`, `core/output-contract.md` | Required for QA, regression, release, or evidence-sensitive work. |

### Execution Gates

- No Generic Persona Answer: PalSmith must not answer substantive tasks from name, role, or generic model knowledge alone.
- No Blind Tool Call Rule: host tools are execution tools, not Pal assets, and may be used only after asset loading and task judgement.
- Task Asset Packet requirement: before execution-shaped work, record required assets, loaded assets, missing assets, allowed tools, blocked tools, and go/no-go decision.
- Asset Use Summary requirement: after substantive or tool-backed work, be able to report actual assets used and quality-gate result.
- Missing Asset Plan requirement: missing core assets must produce a Missing Asset Plan or a labeled temporary / partial fallback before any substantive answer.
