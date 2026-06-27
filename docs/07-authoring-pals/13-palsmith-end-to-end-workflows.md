# PalSmith End-To-End Workflows

## Status

Current for AgentPal `v0.1.0-rc.1`.

PalSmith is used through conversation, plan, Runtime Task Package, user confirmation, current Runtime execution, evidence return, and PalSmith report. PalSmith is not a tool program and does not directly operate on files.

These workflows are few-shot examples, not keyword-matching rules. AgentPal Core is not a semantic classifier or planner. The current Pal plus current Brain / AI judges whether to consult, delegate, or hand off to PalSmith. Mira is the default entry Pal, not the only Pal that can involve PalSmith.

R11 E2E testing passed PalSmith's v0.1 core loop in an independent test copy. v0.2 extends that loop toward AI team-building and Pal quality governance: quality inspection, conflict detection, capability maps, team design, version governance, Eval Lab, and lifecycle workflow. v0.3 adds AI Team Builder, team governance, cross-Pal review, publish quality gate, runtime call verification, GitHub import verification, and quickstart AI team guidance. v0.4 adds a shorter quickstart path, AI team blueprints, a demo script, readiness matrix review, and a regression test plan. R16 v0.4-fix upgrades creation and inspection with job fitness, job expertise modelling, content-preserving user material ingestion, and optional web research to knowledge.

## 1. Create A Single Pal

- 示例说法：`/pal PalSmith 创建一个小红书运营 Pal`
- 当前 Pal 如何协作：如果用户直接呼叫 PalSmith，PalSmith 接收；如果请求先到 Mira 或其他 Pal，当前 Pal 通过 AI 判断是否属于 Pal asset governance，再 consult / delegate / hand off 给 PalSmith。
- PalSmith 读取哪些文件：PalSmith identity files, Pal Pack templates, `docs/03-pal-pack-standard/`, and approved reference Pals only.
- PalSmith 生成什么计划：Pal identity, role boundary, job expertise model, material ingestion plan, optional research plan, directory plan, root files, output contract, knowledge/skill/workflow/eval assets, registry suggestion, contacts suggestion.
- 需要问用户什么确认问题：Pal 名称、职责、目标、场景、目录、语言、用户材料、是否允许材料读取、是否需要联网研究、是否需要注册、是否允许当前 Runtime 写入新目录。
- 生成哪个 Runtime Task Package：`Pal Creation Task Package`.
- 当前 Runtime 执行哪些动作：按确认创建 `official/pals/<Pal-Directory>/` Markdown/JSON assets and public-safe placeholders.
- PalSmith 如何验收：检查 required root files, `pal.json`, public/private boundary, and no unconfirmed registry or contacts write.
- 输出什么报告：created files, skipped files, missing files, not-run checks, next confirmation needed.
- 哪些动作禁止自动执行：自动写 `workspace/organization/contacts/`, 读取私人 memory, 引入代码工具。

## 1A. Create A Pal From User Materials

- 示例说法：`/pal PalSmith 用这些访谈记录创建一个咨询顾问 Pal，不要压缩掉关键内容`
- 当前 Pal 如何协作：当前 Pal 通过 AI 判断确认这是 Pal creation plus content-preserving material ingestion 后交给 PalSmith。
- PalSmith 读取哪些文件：only approved user materials, Pal creation protocol, user material ingestion protocol, content preservation protocol, and the smallest relevant templates.
- PalSmith 生成什么计划：source inventory, classification table, content preservation checklist, job expertise model, Pal Creation Task Package, and User Material Ingestion Task Package if material reading or writing is required.
- 需要问用户什么确认问题：哪些材料可读、是否含私人内容、哪些内容必须原样保留、哪些内容可改写、是否允许写入 target Pal assets。
- 当前 Runtime 执行哪些动作：read approved source files, produce evidence, write approved Pal knowledge/skills/workflows/templates/evals only after confirmation.
- PalSmith 如何验收：trace source labels to generated assets, report missing source sections, over-compression risk, and `not-run`.
- 哪些动作禁止自动执行：把长资料压成短摘要、默认公开私人材料、无来源写知识、未确认读取附件或本地目录。

## 1B. Web Research To Pal Knowledge

- 示例说法：`/pal PalSmith 给这个行业顾问 Pal 补最新行业知识，并保留来源`
- 当前 Pal 如何协作：当前 Pal 通过 AI 判断确认这是 source-backed Pal knowledge construction 后交给 PalSmith；若只是普通研究报告，可能由研究 Pal 负责。
- PalSmith 读取哪些文件：web research protocol, target Pal assets, approved source plan, and Runtime-returned source evidence.
- PalSmith 生成什么计划：research questions, source scope, freshness boundary, citation expectations, uncertainty notes, and proposed asset updates.
- 需要问用户什么确认问题：是否允许联网、允许哪些来源、是否写入 Pal assets、是否只产出研究建议。
- 当前 Runtime 执行哪些动作：only approved network access and file writes; PalSmith reviews the evidence.
- PalSmith 如何验收：facts/inferences/recommendations/uncertainty separated, citations retained, and derived assets mapped to job fitness gaps.
- 哪些动作禁止自动执行：假装联网、无来源事实、把研究网页内容当作 Pal 私人记忆、跳过用户确认。

## 2. Create A Pal Team

- 示例说法：`/pal PalSmith 创建一个跨境电商运营团队`
- 当前 Pal 如何协作：普通入口通常先到 Mira，但任何当前 Pal 都可在 AI 判断后生成 Context Packet 并交给 PalSmith；直接呼叫时 PalSmith 接收。
- PalSmith 读取哪些文件：team request, Pal Pack standard, approved templates, optional approved reference Pals.
- PalSmith 先生成什么设计：team purpose, business scenario, recommended 3-5 Pal count, member names, owner/verifier/consultants, global contacts candidates, team-local candidates, Context Packet rules, shared knowledge, shared workflow, team eval, and team capability map.
- 需要问用户什么确认问题：是否接受团队设计、是否复用已有 Pal、哪些 Pal 进入 global contacts、是否允许生成创建任务包。
- 生成哪个 Runtime Task Package：先生成 `Pal Team Design Task Package`; 用户接受后再生成 `Pal Team Creation Task Package`.
- 当前 Runtime 执行哪些动作：创建团队目录、成员 Pal drafts、shared workflow/knowledge placeholders.
- PalSmith 如何验收：检查 member boundaries, duplicate ids, owner/verifier clarity, and evidence for each created file.
- 输出什么报告：team structure, created paths, missing member assets, not-run checks.
- 哪些动作禁止自动执行：把普通 Skill 当 Pal、自动注册成员、读取未授权私人记忆。

## 3. GitHub Import

- 示例说法：`/pal PalSmith 从 https://github.com/example/legal-pal-pack 导入 Pal`
- 当前 Pal 如何协作：当前 Pal 通过 AI 判断确认这是 external-source Pal import governance 后，交给 PalSmith 并标注 external source risk。
- PalSmith 读取哪些文件：import protocol, staging policy, source URL text, current central roster only if registration is requested.
- PalSmith 生成什么计划：staging target, source trust boundary, risk checks, quarantine rules, install decision points.
- 需要问用户什么确认问题：是否允许当前 Runtime 访问该 URL、staging 位置、是否允许读取 memory、是否只是评估还是准备安装。
- 生成哪个 Runtime Task Package：`Pal Import Staging Task Package`.
- 当前 Runtime 执行哪些动作：下载或复制到 staging, list files, do not execute imported scripts, produce risk report.
- PalSmith 如何验收：classify resource, check core files, scripts, credentials, memory/user, memory/project, state/, reports/, license, conflicts.
- 输出什么报告：staged path, resource type, risk list, quarantine list, install recommendation.
- 哪些动作禁止自动执行：直接安装到 `official/pals/`, 执行脚本, 自动写中央 roster, 导入私人记忆到公开包。

## 4. Local Import

- 示例说法：`/pal PalSmith 从本地目录导入这个 Pal`
- 当前 Pal 如何协作：当前 Pal 通过 AI 判断确认这是 local import governance 后，询问或传递本地路径边界并交给 PalSmith。
- PalSmith 读取哪些文件：approved local source path, import protocol, staging policy.
- PalSmith 生成什么计划：source classification, staging copy plan, excluded private sections, follow-up install package if valid.
- 需要问用户什么确认问题：本地源路径、staging 目标、是否允许读取 memory、是否允许复制文件。
- 生成哪个 Runtime Task Package：`Pal Import Staging Task Package`, then optionally `Pal Install Task Package`.
- 当前 Runtime 执行哪些动作：copy approved files into staging, quarantine risky sections, report file inventory.
- PalSmith 如何验收：verify staged package shape, exclusions, conflict status, and not-run checks.
- 输出什么报告：local import report, install readiness, blocked reasons if any.
- 哪些动作禁止自动执行：越界读取本地私人目录、直接覆盖现有 Pal、自动登记中央 roster。

## 5. Clean Export

- 示例说法：`/pal PalSmith 导出 Research Pal，不含记忆`
- 当前 Pal 如何协作：当前 Pal 通过 AI 判断确认这是 clean public-safe export 后，交给 PalSmith 并说明公开安全边界。
- PalSmith 读取哪些文件：target Pal public files, export policy, privacy policy.
- PalSmith 生成什么计划：included files, required exclusions, manifest fields, export report format, privacy checks.
- 需要问用户什么确认问题：目标 Pal、导出位置、公开分享还是私用、是否允许当前 Runtime 创建包。
- 生成哪个 Runtime Task Package：`Clean Pal Export Task Package`.
- 当前 Runtime 执行哪些动作：copy approved public files, exclude private/runtime data, create `export-manifest.json` and `export-report.md`.
- PalSmith 如何验收：confirm no `memory/user/`, `memory/project/`, `state/`, `reports/`, credentials, tokens, logs, or executable files.
- 输出什么报告：included files, excluded files, manifest path, privacy result, not-run checks.
- 哪些动作禁止自动执行：包含私人记忆、修改源 Pal、发布到远端、忽略 privacy report。

## 6. With Memory Export

- 示例说法：`/pal PalSmith 导出 Research Pal，包含记忆`
- 当前 Pal 如何协作：当前 Pal 通过 AI 判断确认这是 with-memory export 后，交给 PalSmith 并标注 high privacy risk。
- PalSmith 读取哪些文件：target Pal public files and only explicitly approved memory/state/report sections.
- PalSmith 生成什么计划：private export purpose, allowed memory scope, privacy review, restore instructions.
- 需要问用户什么确认问题：导出目的、是否公开发布、memory/user 和 memory/project 范围、是否包含 state/ 和 reports/、二次强确认。
- 生成哪个 Runtime Task Package：`With Memory Export Task Package`.
- 当前 Runtime 执行哪些动作：after strong confirmation, copy approved private sections into private export target and generate privacy report.
- PalSmith 如何验收：privacy report present, public release blocked or converted to clean export, sensitive exclusions honored.
- 输出什么报告：private-data warning first, included private sections, excluded sections, restore notes.
- 哪些动作禁止自动执行：公开发布含私人记忆包、默认读取所有 memory、包含 credentials/tokens。

## 7. Pal Health Inspection

- 示例说法：`/pal PalSmith 体检所有 Pal`
- 当前 Pal 如何协作：当前 Pal 通过 AI 判断确认这是 Pal health / quality governance 后，可交给 PalSmith；如果用户只问方法，可先解释再建议 PalSmith。
- PalSmith 读取哪些文件：`official/pals/`, `workspace/organization/contacts/pals.json`, `workspace/organization/contacts/PAL_CONTACTS.md`, `agentpal.json`, excluding private memory content.
- PalSmith 生成什么计划：inspection scope, health checklist, allowed reads, report path, repair follow-up boundary.
- 需要问用户什么确认问题：体检范围、是否生成报告文件、是否允许读中央 roster。
- 生成哪个 Runtime Task Package：`Pal Health Inspection Task Package`.
- 当前 Runtime 执行哪些动作：read approved files, summarize missing files, parse JSON, produce health report.
- PalSmith 如何验收：separate index-known count from content-read count, report missing/not-run, avoid repair claims.
- 输出什么报告：health status table, risks, suggested fixes, not-run checks.
- 哪些动作禁止自动执行：自动修复、读取私人 memory 内容、把 health score 当注册批准。

## 8. Registry / Contacts Update Suggestion

- 示例说法：`/pal PalSmith 生成 central roster 更新建议`
- 当前 Pal 如何协作：当前 Pal 通过 AI 判断确认这是 central roster governance 后，交给 PalSmith and includes target Pal/path in Context Packet.
- PalSmith 读取哪些文件：target Pal root files, `workspace/organization/contacts/pals.json`, `workspace/organization/contacts/PAL_CONTACTS.md`.
- PalSmith 生成什么计划：JSON diff proposal, eligibility checks, contactability checks, separate write packages.
- 需要问用户什么确认问题：是否只是建议、是否写入 registry、是否写入 contacts、exact diff approval。
- 生成哪个 Runtime Task Package：`central roster update task package`.
- 当前 Runtime 执行哪些动作：only after confirmation, snapshot current JSON, apply approved diff, parse JSON.
- PalSmith 如何验收：valid Pal Pack only, no duplicate id, contacts only for discoverable/contactable Pal with allowed modes.
- 输出什么报告：diff summary, changed JSON paths, parse result, snapshot path.
- 哪些动作禁止自动执行：把普通 Skill 加入 contacts、一次确认写多个未知目标、跳过 JSON parse。

## 9. Snapshot / Rollback

- 示例说法：`/pal PalSmith 为这个修改生成快照和回滚计划`
- 当前 Pal 如何协作：当前 Pal 通过 AI 判断确认目标是 Pal asset versioning or rollback 后，交给 PalSmith.
- PalSmith 读取哪些文件：approved target paths, versioning protocol, audit policy.
- PalSmith 生成什么计划：snapshot scope, manifest fields, rollback target, overwrite risk, evidence requirements.
- 需要问用户什么确认问题：snapshot source, snapshot destination, rollback target, overwrite acknowledgement.
- 生成哪个 Runtime Task Package：`snapshot task package` and, if needed, `rollback task package`.
- 当前 Runtime 执行哪些动作：create snapshot, generate manifest, optionally restore only after explicit confirmation.
- PalSmith 如何验收：snapshot exists, restore instructions exist, pre-rollback current-state backup exists.
- 输出什么报告：snapshot path, manifest path, rollback readiness, not-run checks.
- 哪些动作禁止自动执行：无确认覆盖、删除 current state、恢复到未确认路径。

## 10. Mira + PalSmith Collaboration

- 示例说法：`帮我做一个新 Pal` or `把这个 Pal 发布前检查一下`
- 当前 Pal 如何协作：Mira is the default ordinary entry, but any current Pal judges ownership case-by-case and may hand off to PalSmith when Pal asset lifecycle governance fits.
- PalSmith 读取哪些文件：Mira Context Packet plus smallest relevant PalSmith protocol/template/checklist.
- PalSmith 生成什么计划：stage judgement, permission boundary, confirmation questions, Runtime Task Package.
- 需要问用户什么确认问题：goal, target Pal/path, memory read permission, public release intent, desired output, write permission.
- 生成哪个 Runtime Task Package：the relevant creation, import, export, health, registry, contacts, snapshot, or rollback package.
- 当前 Runtime 执行哪些动作：only the actions explicitly allowed by the package and user confirmation.
- PalSmith 如何验收：review runtime evidence and report `done`, `missing`, `not-run`, and risk.
- 输出什么报告：PalSmith task report, with execution layer evidence separated from Pal judgement.
- 哪些动作禁止自动执行：Mira doing the specialist body after handoff, Runtime bypassing PalSmith package, unbounded memory reads.

## 11. Official Pal Registration

- 示例说法：`/pal PalSmith 将 PalSmith 登记为官方 Pal` or `/pal PalSmith 生成官方登记建议`
- 当前 Pal 如何协作：当前 Pal 通过 AI 判断确认这是 Pal asset governance / central roster consistency work 后，hands off to PalSmith.
- PalSmith 读取哪些文件：`agentpal.json`, `workspace/organization/contacts/pals.json`, `workspace/organization/contacts/PAL_CONTACTS.md`, target `PAL.md`, target `pal.json`, target `SKILL.md`, target `AGENTS.md`.
- PalSmith 生成什么计划：official bundled list update, registry entry, contacts entry, id/path/direct call consistency checks, no-code boundary checks.
- 需要问用户什么确认问题：是否确认登记为 official Pal、是否确认加入 contacts、是否确认只写目标 Pal 条目、是否确认不写私人 memory/state/reports。
- 生成哪个 Runtime Task Package：`Official Pal Registration Task Package`.
- 当前 Runtime 执行哪些动作：inspect target files, apply approved JSON diff to `agentpal.json` and `workspace/organization/contacts/pals.json`, then parse JSON.
- PalSmith 如何验收：target appears in agentpal official list, registry, and contacts; id/path/direct call match; no duplicate id; JSON parse OK.
- 输出什么报告：changed fields, parse evidence, consistency result, no-code boundary result, remaining risk.
- 失败时如何回滚：use a pre-change snapshot or `git diff` to restore only the changed PalSmith entries, then parse JSON again.
- 什么情况不能登记：missing target root files, invalid `pal.json`, ordinary Skill or raw resource, path conflict, private memory dependency, or Pal described as a built-in tool.

## 12. Pal Quality Inspection

- 示例说法：`/pal PalSmith 这个 Pal 怎么感觉不好用`
- PalSmith 生成什么计划：Pal Quality Inspection Task Package.
- 检查什么：structure, identity consistency, responsibility clarity, job fitness, job expertise depth, knowledge depth, skill depth, workflow readiness, template readiness, eval coverage, runtime usability, collaboration safety, release safety, registry consistency, user material gap, and research gap.
- 输出什么报告：Pal Job Fitness Report with dimension scores, overall grade, suggested fixes, required confirmations, `missing`, `not-run`, and risks.
- 禁止什么：未经确认自动修复文件或读取私人 memory 内容。

## 13. Conflict Detection

- 示例说法：`/pal PalSmith 这几个 Pal 职责是不是重复`
- PalSmith 生成什么计划：Pal Conflict Detection Task Package.
- 检查什么：id, direct call, alias, responsibility overlap/gap, owner/verifier problems, Mira/PalSmith responsibility confusion, ordinary Skill contact mistakes.
- 输出什么报告：Conflict Report with severity and recommendations: keep, clarify, merge, split, rename alias, update contacts, or ask user.
- 禁止什么：自动修改中央 roster.

## 14. Capability Map

- 示例说法：`/pal PalSmith 我有哪些 Pal 能帮我做网站运营`
- PalSmith 生成什么计划：Pal Capability Map Task Package.
- 输出什么：Markdown table showing Pal, role, skills, knowledge, workflows, Runtime Task Packages, collaboration modes, owner/verifier/consultant role, release safety, and notes.
- 用途：help users, Mira, and team design understand current capabilities and gaps.

## 15. Eval Lab And Lifecycle

- 示例说法：`/pal PalSmith 这个新 Pal 可以用了么`
- PalSmith 生成什么计划：Pal Eval Lab Task Package.
- 检查什么：identity, responsibility boundary, non-responsibility, risky request, output format, collaboration, import/export safety, central roster consistency.
- 输出什么：passed items, failed items, files needing changes, suggested lifecycle state.
- 生命周期：idea -> design -> confirmation -> Runtime creation -> central roster suggestion -> quality inspection -> Eval Lab -> testing -> trial -> versioned changes -> stable -> clean export/share/team collaboration -> deprecated/archived.

## 16. AI Team Builder

- 示例说法：`/pal PalSmith 帮我搭建一个跨境电商 AI 团队`
- 判断方式：AI 判断该请求是否属于 Pal team design / Pal asset governance；不是关键词规则。
- PalSmith 先输出什么：goal understanding, scenario, team size, Pal list, responsibilities, non-responsibilities, owner, verifier, consultants, team-local/global-contact boundary, shared knowledge, shared workflow, Context Packet, capability map, Eval Lab, and confirmation questions.
- 团队规模：simple 2-3, default 3-5, standard 4-5, complex 6-8, over 8 requires reason and user confirmation.
- 禁止什么：一句话创建 10+ Pals, all global contacts, all handoff, or all user memory access.

## 17. Team Governance And Cross-Pal Review

- 示例说法：`这个团队设计合理吗？`
- 判断方式：AI 判断该请求是否需要 PalSmith team governance, conflict detection, or cross-Pal review.
- PalSmith 输出什么：owner/verifier/consultant boundaries, handoff permissions, shared knowledge access, memory access boundary, team-local/global contacts, conflict handling, reporting workflow, lifecycle state, independent review, owner review, verifier review, conflict summary, and final recommendation.
- 禁止什么：pretending hidden parallel execution happened without Runtime evidence.

## 18. Publish Quality Gate

- 示例说法：`这个团队可以发布吗？`
- 判断方式：AI 判断该请求是否是 publish readiness / Pal asset governance.
- PalSmith 输出什么：Publish Quality Gate Report with recommended status, must-fix items, should-fix items, acceptable risks, user confirmations, and `not-run`.
- 状态：draft, testing, stable, publish-ready, published, deprecated, archived.

## 19. Runtime Call Verification

- 示例说法：`这个 Pal 是否真的能被 /pal 调用？`
- 判断方式：AI 判断该请求是否需要 direct-call evidence.
- PalSmith 输出什么：Level 1 Static Resolution, Level 2 Runtime Simulation, or Level 3 Native Runtime Call.
- 当前边界：do not claim Level 3 unless a native `/pal` runtime call actually happened.

## 20. GitHub Import Verification

- 示例说法：`从 GitHub 导入这个 Pal，并验证能不能用。`
- 判断方式：AI 判断该请求是否 needs external-source import governance.
- PalSmith 输出什么：Level 1 URL Plan, Level 2 Runtime Fetch, or Level 3 Full Import Trial.
- 安全边界：do not execute imported scripts, auto-install, auto-write the central roster, import private memory, trust unknown license, or treat ordinary Skill as Pal.

## 21. AI Team Blueprint

- 示例说法：`/pal PalSmith 给我一个网站运营 AI 团队样板`
- 判断方式：AI 判断该请求是否需要 PalSmith blueprint guidance；不是关键词规则。
- PalSmith 读取哪些文件：`examples/ai-team-blueprints/README.md` and the smallest relevant blueprint.
- PalSmith 输出什么：blueprint summary, recommended 3-5 Pal list, owner/verifier/consultants, shared knowledge, shared workflows, Context Packet rules, quality gate, and confirmation questions.
- 生成哪个 Runtime Task Package：if the user accepts, `AI Team Builder Task Package` or `Pal Team Creation Task Package`.
- 禁止什么：treating the blueprint as an installed Pal, writing the central roster, or creating files without confirmation.

## 22. Readiness Matrix Review

- 示例说法：`/pal PalSmith 这个 Pal 可以进入 publish-ready 吗？`
- 判断方式：AI 判断该请求是否 needs lifecycle / Eval Lab / publish gate convergence.
- PalSmith 读取哪些文件：target public Pal files, evals, central roster if relevant, clean export evidence if approved.
- PalSmith 输出什么：readiness matrix with Structure Completeness, Identity Consistency, Responsibility Clarity, Skill / Knowledge Coverage, Workflow Readiness, Eval Coverage, Registry / Contacts Consistency, Memory / State / Reports Safety, Collaboration Safety, Runtime Task Package Readiness, Clean Export Safety, With Memory Export Risk, and Team Governance Readiness.
- 生成哪个 Runtime Task Package：`Pal Readiness Review Task Package`.
- 状态：idea, draft, testing, stable, publish-ready, published, deprecated, archived.
- 禁止什么：calling something `publish-ready` without evidence, claiming `published` without publication evidence, or smoothing missing checks into pass.

## 23. v0.4 Demo Path

- 示例说法：`演示一下 PalSmith 怎么帮我创建 AI 团队。`
- 判断方式：AI 判断该请求是否 asks for teaching/demo support.
- PalSmith 读取哪些文件：quickstart, demo script, and optionally one blueprint.
- PalSmith 输出什么：a short 10-minute flow covering personal Pal creation, AI team design, and publish readiness.
- 生成哪个 Runtime Task Package：none unless the user confirms real file creation or report writing.
- 禁止什么：presenting the demo as fixed routing, claiming runtime execution, or creating a test directory during the demo explanation.
