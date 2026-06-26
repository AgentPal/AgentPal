# PalSmith

PalSmith is the official AgentPal Pal asset governance Pal.

Use PalSmith for no-code Pal Pack creation planning, team planning, health inspection planning, import staging planning, export planning, registry/contacts update proposals, snapshot plans, and rollback plans.

## Current Product Status

PalSmith E2E testing passed the core functional loop in an independent test copy. v0.1 can create Pals, create Pal teams, maintain a test Pal, stage imports, create clean exports, enforce with-memory export boundaries, reject ordinary Skills from contacts, and preserve the no-code boundary.

PalSmith is now entering v0.2 product enhancement. v0.2 strengthens PalSmith as an AI team-building entry point and Pal quality governance Pal: Pal quality inspection, responsibility conflict detection, capability maps, team design, version governance, Eval Lab, and lifecycle workflow.

This is not a final release state; v0.1 publication is paused while v0.2 is developed.

v0.3 extends PalSmith into an AI Team Builder, team governance guide, cross-Pal review coordinator, publish quality gate, runtime call verification workflow, and GitHub import verification workflow. These remain no-code Runtime Task Package workflows.

v0.4 improves the user-facing path with a 5-minute quickstart, quickstart cheatsheet, AI team blueprints, a 10-minute demo script, a readiness matrix, and a v0.4 regression test plan.

R16 v0.4-fix upgrades PalSmith from file-completeness governance to job fitness governance. PalSmith now inspects whether a Pal can do its declared job, whether its knowledge and skills match real scenarios, whether user materials were preserved without over-compression, and whether optional web research should be turned into traceable knowledge assets before creation or repair.

R17 quality testing in a separate test copy verified that PalSmith can create a job-shaped test Pal with source inventory, source coverage matrix, concrete knowledge, skills, workflows, templates, evals, user material preservation, and a real task simulation. The formal workspace does not include that test Pal or test reports; it keeps only reusable improvements such as the source coverage template and long-material ingestion example.

## Current Boundary

PalSmith is not a CLI or built-in software tool. It does not scan, validate, import, export, install, package, or restore files by itself.

PalSmith generates Runtime Task Packages. The current Agent Runtime, such as Codex or Claude Code, performs approved file operations and reports evidence.

PalSmith collaboration is selected by current Pal + current Brain / AI judgement. AgentPal Core does not do keyword routing, and Mira is the default entry Pal rather than the only Pal that can call PalSmith.

Task package examples live in `examples/task-packages/`. Reusable task package templates live in `templates/task-packages/`. Their indexes are `examples/task-packages/README.md` and `templates/task-packages/README.md`.

Release readiness is checked through Markdown evals, including `evals/palsmith-release-scope-eval.md`.

Docs entry points:

- `docs/PalSmith.md`
- `docs/03-pal-pack-standard/14-runtime-task-package.md`
- `docs/07-authoring-pals/12-use-palsmith.md`
- `docs/07-authoring-pals/13-palsmith-end-to-end-workflows.md`
- `docs/08-release-candidate/05-no-code-release-checklist.md`
- `docs/08-release-candidate/06-palsmith-release-scope-review.md`
- `docs/08-release-candidate/11-palsmith-e2e-test-summary.md`
- `docs/07-authoring-pals/14-palsmith-pal-lifecycle.md`
- `docs/07-authoring-pals/15-palsmith-quickstart-ai-team.md`
- `docs/07-authoring-pals/16-palsmith-demo-script.md`
- `docs/08-release-candidate/12-palsmith-v0.4-regression-test-plan.md`
- `pals/PalSmith-pal-governor/examples/ai-team-blueprints/README.md`
- `pals/PalSmith-pal-governor/core/pal-readiness-matrix.md`
- `pals/PalSmith-pal-governor/core/pal-quality-inspection-protocol.md`
- `pals/PalSmith-pal-governor/core/user-material-ingestion-protocol.md`
- `pals/PalSmith-pal-governor/core/content-preservation-protocol.md`
- `pals/PalSmith-pal-governor/core/web-research-to-knowledge-protocol.md`
- `pals/PalSmith-pal-governor/skills/README.md`
- `pals/PalSmith-pal-governor/knowledge/README.md`
- `pals/PalSmith-pal-governor/templates/source-coverage-report-template.md`
- `pals/PalSmith-pal-governor/examples/task-packages/example-long-user-material-ingestion.md`

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
/pal PalSmith 检查 PalSmith 自己是不是技能很多但内容空
/pal PalSmith 这几个 Pal 职责是不是重复
/pal PalSmith 这个团队可以发布吗
/pal PalSmith 这个 Pal 是否真的能被 /pal 调用
```

## Safety Boundary

Controlled writes require explicit user confirmation. With-memory export requires strong confirmation and a privacy report. Imported scripts are never executed as part of PalSmith planning. Registry and contacts changes are separate proposals, and ordinary Skills cannot enter contacts.
