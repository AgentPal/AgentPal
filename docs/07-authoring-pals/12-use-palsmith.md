# Use PalSmith

## Status

Current for AgentPal `v0.1.0-rc.1`.

PalSmith is the official no-code Pal asset governance Pal. Use it when you want AgentPal to help create, inspect, import, export, version, or publish Pal Packs.

For full end-to-end examples, see [PalSmith end-to-end workflows](13-palsmith-end-to-end-workflows.md). For the task package field standard, see [Runtime Task Package](../03-pal-pack-standard/14-runtime-task-package.md).

PalSmith v0.2 expands from core Pal creation into Pal quality governance and AI team-building: quality inspection, responsibility conflict detection, capability maps, team design, version governance, Eval Lab, and the [Pal lifecycle workflow](14-palsmith-pal-lifecycle.md).

PalSmith v0.3 adds AI Team Builder, team governance, cross-Pal review, publish quality gate, runtime call verification, GitHub import verification, and the [quickstart AI team guide](15-palsmith-quickstart-ai-team.md).

PalSmith v0.4 focuses on product demonstration and teaching: a 5-minute quickstart, quickstart cheatsheet, AI team blueprints, a [demo script](16-palsmith-demo-script.md), a readiness matrix, and a v0.4 regression test plan.

R16 v0.4-fix adds job fitness creation and inspection. PalSmith asks what the Pal is called, what responsibilities it owns, what goals and scenarios matter, what user materials should be used, and whether web research should supplement the materials. It then builds a job expertise model and maps material into knowledge, skill, workflow, runbook, template, eval, and governance assets with source preservation.

PalSmith is selected by AI judgement, not keyword routing. Mira is the default entry Pal, but any current Pal can consult, delegate, or hand off to PalSmith when the task belongs to Pal asset governance.

## Direct Call

```text
/pal PalSmith
```

## Conversation Examples

```text
/pal PalSmith 创建一个小红书运营 Pal
/pal PalSmith 创建一个跨境电商运营团队
/pal PalSmith 体检所有 Pal
/pal PalSmith 从 GitHub 导入这个 Pal
/pal PalSmith 导出 Research Pal，不含记忆
/pal PalSmith 给 Developer Pal 增加 Claude Code 使用知识
/pal PalSmith 将 PalSmith 登记为官方 Pal
/pal PalSmith 生成 registry 更新建议
/pal PalSmith 生成 contacts 更新建议
/pal PalSmith 我想搭建一个 AI 团队帮我做跨境电商
/pal PalSmith 这个 Pal 怎么感觉不好用
/pal PalSmith 这几个 Pal 职责是不是重复
/pal PalSmith 我有哪些 Pal 能帮我做网站运营
/pal PalSmith 这个团队可以发布吗
/pal PalSmith 这个 Pal 是否真的能被 /pal 调用
/pal PalSmith 从 GitHub 导入这个 Pal，并验证能不能用
/pal PalSmith 给我一个网站运营 AI 团队样板
/pal PalSmith 这个 Pal 可以进入 publish-ready 吗
/pal PalSmith 用这批访谈记录创建一个咨询顾问 Pal
/pal PalSmith 检查这个 Pal 是否真的懂私域运营
/pal PalSmith 把这些资料摄取成 Pal 知识和工作流，不要压缩掉关键内容
```

## What PalSmith Does First

PalSmith does not directly write files. It first decides the permission level and generates a plan:

- L0 read-only inspection
- L1 suggested change
- L2 controlled write
- L3 high-risk write
- L4 core governance

For L2 or higher, PalSmith prepares a Runtime Task Package and asks for user confirmation before the current runtime changes files.

## Creating A Pal

PalSmith first asks for the Pal name, responsibilities, goals, scenarios, user materials, and research preference. Then it prepares a job expertise model: target users, real tasks, hard decisions, required knowledge, required workflows, reusable templates, eval cases, collaboration boundary, and evidence needed to show the Pal can do the job.

PalSmith generates a Pal Creation Task Package with proposed name, id, directory, role, direct call, aliases, responsibilities, job expertise model, material ingestion plan, research plan, root files, identity files, output contract, initial indexes, evals, registry suggestion, contacts suggestion, risk notes, and confirmation questions.

After confirmation, the current Agent Runtime creates files and returns evidence. PalSmith reviews the evidence and summarizes the result.

## Creating A Pal Team

PalSmith first designs the team: user goal, business scenario, recommended 3-5 Pal size, member roles, owner, verifier, consultants, Context Packet rules, team-local vs global contacts, shared knowledge, shared workflow, eval, and capability map. After the user accepts the design, PalSmith generates a Pal Team Creation Task Package.

## Inspecting Quality And Conflicts

PalSmith can generate Pal Quality Inspection, Pal Conflict Detection, and Pal Capability Map task packages. Quality inspection is now a job fitness review: PalSmith reports structure, identity consistency, responsibility clarity, job expertise depth, skill coverage, knowledge coverage, workflow coverage, eval coverage, collaboration safety, release safety, research gaps, user material gaps, conflict severity, and capability gaps before proposing any write.

## Ingesting User Materials And Research

When the user supplies files, notes, transcripts, product docs, domain manuals, or examples, PalSmith creates a source inventory first. It preserves important source content, records extraction decisions, and classifies material into knowledge, skill, workflow, runbook, template, eval, output contract, and governance assets.

If the Pal needs current or domain-specific expertise beyond the user materials, PalSmith may propose web research. The current runtime performs any approved network access and returns source evidence. PalSmith keeps facts, source links, dates, uncertainty, and recommendations separate before writing Pal knowledge.

## Building And Governing AI Teams

PalSmith v0.3 can guide a normal user from "I need an AI team" to a bounded team design. It proposes team size, owner, verifier, consultants, team-local vs global-contact Pals, shared knowledge, shared workflow, Context Packet rules, capability map, Eval Lab, and publish quality gate before file creation.

Team governance and cross-Pal review keep larger teams from becoming vague or self-confirming. PalSmith defines independent review, owner review, verifier review, conflict summary, and final recommendation, while business judgement remains with the relevant Pals.

## Verifying Calls And GitHub Imports

Runtime call verification has three levels: Level 1 Static Resolution, Level 2 Runtime Simulation, and Level 3 Native Runtime Call. PalSmith must state which level was reached.

GitHub import verification also has three levels: Level 1 URL Plan, Level 2 Runtime Fetch, and Level 3 Full Import Trial. PalSmith does not implement a downloader and must not pretend local simulation is a real network fetch.

## Quickstart, Blueprints, And Demo Script

PalSmith v0.4 adds a shorter user path:

- [5-minute quickstart](15-palsmith-quickstart-ai-team.md)
- quickstart cheatsheet in `pals/PalSmith-pal-governor/examples/quickstart/`
- AI team blueprints in `pals/PalSmith-pal-governor/examples/ai-team-blueprints/`
- [10-minute demo script](16-palsmith-demo-script.md)

Blueprints are examples only. They are not installed Pals and must not be written into registry / contacts without a confirmed Runtime Task Package.

## Readiness Review

When the user asks whether a Pal can publish, PalSmith first performs readiness review instead of answering yes immediately. The review unifies lifecycle, Eval Lab, and publish quality gate evidence into one state recommendation: `idea`, `draft`, `testing`, `stable`, `publish-ready`, `published`, `deprecated`, or `archived`.

If a dimension was not checked, PalSmith reports `not-run`. If evidence is missing, PalSmith reports `missing`. `publish-ready` requires clean export safety, public-safety evidence, Eval Lab coverage, and registry / contacts consistency when relevant.

## Importing A Pal

PalSmith stages imports through a Pal Import Staging Task Package. External GitHub, local directory, and archive sources are untrusted by default.

The current runtime performs any approved download or copy into staging. PalSmith reviews the staged resource type, core files, memory/state/reports, sensitive files, executable risk, license, and ID conflicts before asking whether to install.

## Exporting A Pal

PalSmith generates a Clean Pal Export Task Package or With Memory Export Task Package.

Clean export excludes `memory/user/`, `memory/project/`, `state/`, `reports/`, logs, cache, credentials, tokens, and executable files. With-memory export requires strong confirmation and a privacy review.

## Registry, Contacts, Snapshot, And Rollback

PalSmith can generate:

- registry update task package
- contacts update task package
- Official Pal Registration Task Package
- snapshot task package
- rollback task package
- Pal version upgrade task package
- Pal version rollback task package
- Pal Eval Lab task package

Only standard Pal Packs can enter registry or contacts. Contacts also require discoverable/contactable collaboration flags and at least one allowed collaboration mode. Ordinary Skills, tools, models, plugins, raw repositories, Knowledge Packs, and Persona Packs are not contacts.

## Boundary

PalSmith is not a Runtime. The host Runtime performs real file edits, archive creation, downloads, deletion, publishing, or command execution and must provide evidence.
