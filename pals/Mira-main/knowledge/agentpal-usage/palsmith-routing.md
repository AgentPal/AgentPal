# PalSmith Delegation And Handoff Guidance

This file is guidance for deciding whether PalSmith should be consulted, delegated to, or receive a handoff. It is not a keyword route table.

## Core Rule

AgentPal does not do keyword routing. AgentPal Core is not a semantic classifier or planner.

Every user message is judged by the current Pal plus the current Brain / AI from:

- user goal
- expected deliverable
- risk
- available contacts / registry
- selected Pal assets
- whether the task concerns Pal asset governance

Mira is the default entry Pal and default Main Pal, but Mira is not the only Pal that can call PalSmith. Any Pal that receives a request may, after AI judgement, consult, delegate, or hand off to PalSmith.

## When PalSmith Is A Candidate

PalSmith is a candidate when AI judgement says the request belongs to Pal asset governance, for example:

- creating a Pal
- creating a Pal team
- designing an AI team
- maintaining a Pal Pack
- inspecting Pal health or quality
- checking whether a Pal has real job fitness and job expertise for its declared role
- ingesting user materials into Pal knowledge, skill, workflow, runbook, template, or eval assets
- preserving source content while converting material into Pal assets
- planning optional web research to supplement a Pal's domain knowledge
- detecting Pal responsibility conflicts
- generating a Pal capability map
- deciding whether a Pal or team can be published
- importing or exporting a Pal
- preparing registry / contacts update suggestions
- planning snapshot or rollback
- checking a publish quality gate
- verifying direct-call readiness

These are capability examples, not keyword rules.

## Context Packet To PalSmith

When any Pal hands work to PalSmith, pass only the needed context:

- user goal
- target Pal, source, team, or directory
- whether memory read is allowed
- whether output is for public release or private backup
- requested PalSmith output: plan, confirmation questions, Runtime Task Package, report, diff suggestion, or review
- risk boundary, including forbidden reads/writes

Do not pass all user memory by default. PalSmith should ask before any memory read, controlled write, with-memory export, registry write, contacts write, snapshot restore, rollback, or publish-quality status change.

For registry, contacts, official Pal list, release consistency, or publish readiness requests, the receiving Pal should not add ordinary Skills to contacts and should not bypass PalSmith's standard Pal Pack eligibility judgement.

## Handoff Shape

If the current Pal judges that PalSmith owns the task, that Pal states the case-specific reason and hands off. PalSmith answers immediately with its own prefix, plan, questions, and Runtime Task Package boundary.

## Few-Shot Examples

These examples show judgement patterns. They are not keyword-matching rules.

### Create Single Pal

User example: `帮我创建一个小红书运营 Pal。`

Judgement: the deliverable is a Pal Pack asset.

PalSmith should produce: `Pal Creation Task Package`, confirmation questions, target directory plan, registry/contacts suggestions only.

### Create Or Design Pal Team

User example: `帮我创建一个跨境电商运营团队。`

Judgement: the deliverable is a Pal team package. PalSmith should design the team before creating it.

PalSmith should produce first: `AI Team Builder Task Package` or `Pal Team Design Task Package`, recommended 3-5 Pal structure, owner/verifier/consultants, Context Packet rules, global contacts candidates, team-local candidates, shared knowledge/workflow/eval, and acceptance question.

### Pal Quality Inspection

User example: `我这个 Pal 怎么感觉不好用？`

Judgement: the deliverable is Pal quality governance.

PalSmith should produce: `Pal Quality Inspection Task Package`, A/B/C/D quality report, structure, identity consistency, responsibility clarity, capability completeness, collaboration safety, release safety, and suggested fixes.

### Job Fitness Inspection

User example: `这个私域运营 Pal 是不是只是文件齐了，实际不懂业务？`

Judgement: the deliverable is real-work Pal quality governance.

PalSmith should produce: `Pal Quality Inspection Task Package`, job fitness scoring, job expertise depth review, skill/knowledge/workflow/eval gap list, research gap, material gap, and repair plan.

### User Material Ingestion

User example: `把这些访谈记录和SOP变成 Pal 的知识和工作流，不要把细节压没了。`

Judgement: the deliverable is content-preserving Pal asset ingestion.

PalSmith should produce: `User Material Ingestion Task Package`, source inventory, classification table, content preservation checklist, asset mapping, privacy boundary, and confirmation questions before Runtime reads or writes private material.

### Web Research To Pal Knowledge

User example: `这个行业我资料不够，帮这个 Pal 补充最新知识。`

Judgement: the deliverable is source-backed Pal knowledge construction.

PalSmith should produce: `Web Research To Knowledge Task Package`, research questions, approved source scope, freshness boundary, citation expectations, uncertainty notes, and proposed knowledge/skill/workflow/eval updates.

### Pal Conflict Detection

User example: `这几个 Pal 职责是不是重复？`

Judgement: the deliverable is Pal responsibility governance.

PalSmith should produce: `Pal Conflict Detection Task Package`, conflict types, involved Pals, severity, and recommendations such as keep, clarify, merge, split, rename alias, update contacts, or ask user.

### Capability Map

User example: `我有哪些 Pal 能帮我做网站运营？`

Judgement: the deliverable is a readable map of Pal capabilities.

PalSmith should produce: `Pal Capability Map Task Package`, Pal x role x skills x knowledge x workflows x collaboration modes x release safety table, capability gaps, and overlap notes.

### Team Governance

User example: `这个团队设计合理吗？`

Judgement: the deliverable is team governance and review.

PalSmith should produce: `Pal Team Governance Task Package`, and may combine it with conflict detection or cross-Pal review if needed.

### Publish Quality Gate

User example: `这个团队可以发布吗？`

Judgement: the deliverable is publish-readiness judgement.

PalSmith should produce: `Pal Publish Quality Gate Task Package`, quality inspection, Eval Lab status, conflict detection for teams, Clean Export safety, and status recommendation.

### Runtime Call Verification

User example: `这个 Pal 是否真的能被 /pal 调用？`

Judgement: the deliverable is call-readiness evidence.

PalSmith should produce: `Pal Runtime Call Verification Task Package` and clearly label Level 1 Static Resolution, Level 2 Runtime Simulation, or Level 3 Native Runtime Call.

### GitHub Import Verification

User example: `从 GitHub 导入这个 Pal，并验证能不能用。`

Judgement: the deliverable is external-source import governance.

PalSmith should produce: `GitHub Import Verification Task Package`; staging first, no script execution, no automatic install, no automatic registry/contacts writes, and honest Level 1/2/3 reporting.

### Skill Contact Request

User example: `把这个 Skill 加入通讯录。`

Judgement: the target might not be a Pal Pack.

PalSmith should classify the resource and explain that ordinary Skills cannot enter contacts. If the resource is not a standard Pal Pack, PalSmith stops at a resource classification report or suggests a Pal Pack creation path.
