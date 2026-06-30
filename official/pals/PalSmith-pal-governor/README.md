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

R179 adds a no-code draft-to-user-custom Pal installation flow. This lets PalSmith plan how a reviewed draft Pal Pack can become a user custom Pal under a private-by-default user custom area, without promoting it to official Pal status, without writing central contacts, and without building an installer or runtime service.

R185-R191 add user custom Pal discovery authorization, explicit invocation boundaries, revocation readiness, real host read-only regression, and external readability review. User custom Pals remain private by default and are not central contacts or official Pals.

R192 closes the PalSmith v0.5 phase as ready for release prep. R193 adds a local release-prep package. This is not remote publication, tag creation, or GitHub Release authorization.

## Current Boundary

PalSmith is not a CLI or built-in software tool. It does not scan, validate, import, export, install, package, or restore files by itself.

PalSmith generates Runtime Task Packages. The current Agent Runtime, such as Codex or Claude Code, performs approved file operations and reports evidence.

PalSmith collaboration is selected by current Pal + current Brain / AI judgement. AgentPal Core does not do keyword routing, and Mira is the default entry Pal rather than the only Pal that can call PalSmith.

Task package examples live in `examples/task-packages/`. Reusable task package templates live in `templates/task-packages/`. Their indexes are `examples/task-packages/README.md` and `templates/task-packages/README.md`.

Draft-to-custom installation planning is governed by `core/custom-pal-installation-protocol.md`. The default suggested target is `workspace/resources/user-pals/<pal-id>/`, but PalSmith must present an installation plan and receive explicit user confirmation before any Runtime write.

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
/pal PalSmith 创建一个马斯克思维的产品经理 Pal，并保持公开来源边界
/pal PalSmith 创建一个韩立性格和说话风格的风险审查 Pal，注意版权边界
/pal PalSmith 把我们公司售前专家的经验蒸馏成售前 Pal，先判断隐私和授权
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
- `examples/palsmith/composite-pal-creation-examples.md`
- `prompts/palsmith/create-composite-pal.md`

Composite creation keeps source boundaries clear. Public-source-inspired, style-inspired, and organization-internal expert Pals have different publication rules. Organization-internal expert Pals default to private internal use, not public Marketplace listing.

## Safety Boundary

Controlled writes require explicit user confirmation. With-memory export requires strong confirmation and a privacy report. Imported scripts are never executed as part of PalSmith planning. Registry and contacts changes are separate proposals, and ordinary Skills cannot enter contacts.

## Real Task Examples

See `examples/tasks/` for v0.2 PalSmith task examples. These are non-binding examples for Pal creation, AI team design, material ingestion, and Pal health repair packages.
