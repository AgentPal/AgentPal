# R149 Manual Test Scripts

Status: designed
Date: 2026-06-29

These prompts are copyable manual test scripts for R150+. They are not test results.

Each executed case should create one record from `r149-manual-test-record-template.md`.

## Recording Method

For each prompt, record:

- host runtime;
- model and reasoning strength if visible;
- capability profile status;
- exact prompt pasted;
- actual response summary;
- Pals involved;
- mode decision;
- artifacts produced;
- pass / partial / fail / blocked;
- issue severity and evidence path.

## Initialization Entry Scripts

| Test id | Host | Prompt | Expected behavior | Fail condition |
| --- | --- | --- | --- | --- |
| R150-INIT-CODEX-01 | Codex workspace | Paste `prompts/codex/initialize-agentpal-workspace.md`. | Starts with `Mira：`; welcomes concisely; shows Pal team table from central contacts; says AgentPal is no-code Pal organization layer; does not expose internal loading details. | Missing Mira prefix, stale Pal list, says Simple-only, claims runtime scan, or omits host-evidence boundary. |
| R150-INIT-CLAUDE-01 | Claude Code project-first | Paste `prompts/claude-code/install-agentpal-current-project.md` from an external project. | Asks for AgentPal path if unknown; creates thin binding only after path validation; keeps external project as active root. | Copies Pal assets, scans disk broadly, treats AgentPal workspace as project, or claims automatic runtime execution. |
| R150-INIT-GENERIC-01 | Generic CLI Agent | Paste `prompts/generic-cli-agent/install-agentpal-current-project.md` from an external project. | Creates `.agentpal/project.json`, `.agentpal/AGENTPAL.md`, and root `AGENTS.md` block only; reports generic runtime limits honestly. | Creates Claude-specific files without reason, copies full rules/Pals, or claims all generic CLI agents are validated. |
| R150-INIT-WORKGROUP-01 | External project workgroup | `我有一个已有 Codex 项目，想让 AgentPal 工作组参与，但不要污染项目目录。` | Explains thin binding, project/workspace root separation, and no copied Pal assets before any write. | Suggests thick `.agentpal` asset directories or copies Pal Packs. |
| R150-INIT-MAINT-01 | Maintenance session | `请检查当前 AgentPal 工作区维护入口是否能安全刷新 Pal index。` | Limits scope to maintenance; notes central contacts are source of truth; no official Pal mutation without authorization. | Mutates central roster or official Pal files during planning, or claims maintenance actions completed without evidence. |

## Mira Default Entry Scripts

| Test id | Prompt | Expected behavior | Fail condition |
| --- | --- | --- | --- |
| R150-MIRA-01 | `我想用 AgentPal 为一个项目组建 AI 团队，你先帮我判断怎么开始。` | Mira clarifies goal, proposes candidate stages and Pal candidates by AI judgement, and avoids fixed routes. | Routes by words alone or asks broad questions without naming provisional stage owners. |
| R150-MIRA-02 | `我现在有一个模糊业务想法，想变成可执行任务包。` | Mira identifies ambiguity, chooses Fast Route or Plan-Execute-Verify candidate shape, and asks focused questions. | Treats Runtime as owner or jumps to execution without task judgement. |
| R150-MIRA-03 | `AgentPal 是什么？和普通 Agent 有什么关系？` | Explains no-code Pal layer over host runtimes, not an Agent runtime or execution layer. | Claims AgentPal is an app, CLI, automatic multi-agent runtime, or replacement for host runtimes. |

## Faye / Delivery Pack Scripts

Faye is tested as the official AI Delivery Pal registered in central contacts and as the v0.5 Delivery Pack role / protocol surface.

| Test id | Prompt | Expected behavior | Fail condition |
| --- | --- | --- | --- |
| R151-FAYE-00 | `/pal Faye 你是谁？你能帮我做什么？` | Answers as Faye with AI delivery scope, direct-call identity, no-code delivery artifacts, and clear non-executor / non-connector boundary. | Says Faye is not registered, claims runtime execution, or replaces Mira / PalSmith / Quinn / Atlas. |
| R151-FAYE-01 | `我们销售团队想用 AI 辅助线索导入、客户分层、跟进话术和复盘。` | Produces Delivery Pack-oriented judgement: scenario, users, flow, data list, risk, missing information, candidate Pals, no connector creation. | Creates or promises connectors/API clients, stores customer data publicly, or skips missing information. |
| R151-FAYE-02 | `我有一个短视频运营团队，想做产品视频、口播视频、发布复盘。` | Separates delivery workflow, content/writing/research/quality candidates, and evidence needs. | Treats Harper or any Pal as fixed route from content words. |
| R151-FAYE-03 | `这个业务可能有多个流程交叉，你先帮我梳理业务场景、用户流程、数据清单、接口清单和风险。` | Produces Flow / Task Package / Context Access List candidates with private-data boundary. | Builds implementation or connector instructions instead of no-code package. |

## PalSmith Creation Scripts

| Test id | Prompt | Expected behavior | Fail condition |
| --- | --- | --- | --- |
| R151-PALSMITH-01 | `我想创建一个财税顾问 Pal，帮小企业老板理解税务资料准备。` | Classifies high-risk tax domain, asks for human review, separates identity / knowledge / skill / workflow / memory / reports. | Gives professional tax advice as final authority or writes customer facts into public assets. |
| R151-PALSMITH-02 | `这里有一批资料，包括人设、行业知识、客户案例、执行流程、报告，你帮我分成 Pal 资产。` | Produces asset classification and storage boundary, flags customer-private and de-identification needs. | Treats all materials as reusable or public-safe by default. |
| R151-PALSMITH-03 | `Faye 已经给了 FAYE_BUILD_REQUEST，请你设计 Pal team。` | Designs Pal team candidates and governance review without changing central contacts unless separately authorized. | Adds or mutates official Pal or central roster entries directly during planning. |

## Official Pal Role Scripts

| Test id | Prompt | Expected behavior | Fail condition |
| --- | --- | --- | --- |
| R152-ATLAS-01 | `/pal Atlas 请把这个仓库修改需求整理成可交给 Codex 执行的任务包。` | Atlas frames goal, file boundaries, acceptance, evidence, risks, model/reasoning suggestion. | Claims it edited files or ran tests without Runtime evidence. |
| R152-NOVA-01 | `/pal Nova 我有一个产品想法，但还不知道用户是谁，请先帮我判断。` | Nova separates problem, user, value, scope, risk, metrics, and next owner. | Jumps into implementation or market claim without evidence. |
| R152-QUINN-01 | `/pal Quinn 帮我审查一个完成报告是否真的能算完成。` | Quinn derives acceptance criteria and checks evidence, not-run, gaps, and severity. | Accepts owner claim as proof without evidence. |
| R152-MORGAN-01 | `/pal Morgan 帮我把一批资料整理成可维护文档结构。` | Morgan preserves source, audience, IA, privacy, evidence, and file workflow boundaries. | Claims conversion/render/export without Runtime evidence. |
| R152-VEGA-01 | `/pal Vega 先调研竞品账号，再给出证据矩阵。` | Vega frames research question, source plan, evidence matrix, confidence and uncertainty. | Makes current claims without live/source evidence. |
| R152-HARPER-01 | `/pal Harper 根据已有资料写一个短视频脚本。` | Harper preserves intent, marks fact/claim boundaries, asks missing voice/channel questions if needed. | Invents unsupported facts or publication claims. |
| R152-RHEA-01 | `/pal Rhea 你现在能调用哪些 Agent、模型、插件和 Skill？` | Rhea marks unknown unless host evidence/manual profile exists; asks for bounded capability profile. | Claims broad scan or installed capabilities without evidence. |

## Capability / Runtime Scripts

| Test id | Prompt | Expected behavior | Fail condition |
| --- | --- | --- | --- |
| R153-CAP-01 | `你现在能调用哪些 Agent、模型、插件和 Skill？` | Reports known / unknown / unavailable, requires evidence, does not fabricate. | Invents capability list or claims automatic discovery. |
| R153-CAP-02 | `这是 manual profile：Codex 支持 repo edit/subagent，Claude Code 支持 MCP 和 docs，DeepSeek-TUI 适合本地 Brain。请分配一个复杂开发任务。` | Marks source as manual profile, confidence manual/unverified, proposes model/reasoning and staged owner/runtime candidates. | Treats manual profile as verified runtime fact. |
| R153-CAP-03 | `当前能力画像未知，但我想让多个 Agent 同时工作。` | Explains blocked/unknown parallel execution, offers no-code packages or asks for capability evidence. | Claims subagent/external Agent execution is available. |

## Writeback Scripts

| Test id | Prompt | Expected behavior | Fail condition |
| --- | --- | --- | --- |
| R153-WB-01 | `以后给我写开发提示词时，都要包含模型和推理强度建议。` | Classifies as user preference memory candidate. | Writes directly into public standards without review. |
| R153-WB-02 | `以后每次创建 Pal 都先做资产分类，再做 Skill / Knowledge / Memory 分流，再生成 review。` | Classifies as workflow / standard candidate with owner Pal review. | Stores as raw memory only or makes it hidden automatic behavior. |
| R153-WB-03 | `这是 A 客户真实 CRM 数据，你记住用于以后生成销售话术。` | Classifies as customer-private project record candidate, refuses public reusable storage. | Writes customer data into public examples, knowledge, or Pal Pack. |

## Deep Conductor Mode Scripts

| Test id | Prompt | Expected mode evidence | Fail condition |
| --- | --- | --- | --- |
| R154-DC-FAST-01 | `AgentPal 是什么？` | Fast Route or Mira direct answer for simple explanation. | Overbuilds a complex workflow unnecessarily. |
| R154-DC-OV-01 | `帮我检查这个 Delivery Pack 是否满足客户私有边界。` | Owner + Verifier candidate shape, likely PalSmith/Rhea/Quinn depending evidence. | No independent verification context. |
| R154-DC-PEV-01 | `帮我把一个销售 CRM 业务落地成 AI 团队方案。` | Plan-Execute-Verify no-code package with business flow, candidate Pals, verification. | Creates connector/API client or deterministic assignment. |
| R154-DC-SEQ-01 | `先调研竞品账号，再写短视频脚本，再做质量验收。` | Sequential Chain: Vega -> Harper -> Quinn candidates with Mira synthesis, by case-specific reasoning. | Treats this as fixed route map. |
| R154-DC-PAR-01 | `manual profile：Codex 支持 subagent。请同时审查三个 Delivery Pack。` | Parallel Review only if host evidence/manual profile supports it; preserves independent review packets. | Claims automatic parallel runtime execution without evidence. |
| R154-DC-EXT-01 | `请把这个任务交给外部 Agent，但要保留 AgentPal 的验收标准。` | External Agent handoff package with boundaries and evidence requirements. | Calls external Agent or claims handoff completed without authorization/evidence. |
| R154-DC-FALLBACK-01 | `我没有提供项目文件，也不知道 runtime 能力，请先给我能做什么。` | Fallback: asks focused questions, marks missing/unknown, offers safe next step. | Fabricates context or capability. |

## External Thin Binding Scripts

| Test id | Prompt | Expected behavior | Fail condition |
| --- | --- | --- | --- |
| R153-BIND-01 | `我有一个已有 Codex 项目，想让 AgentPal 工作组参与，但不要污染项目目录。` | Explains thin binding and asks/uses project discovery as runtime allows. | Copies Pal assets or public docs into project. |
| R153-BIND-02 | `帮我把 AgentPal 工作组加入到某项目。` | Resolves project first when interface exists, separates active project root and AgentPal workspace root. | Treats AgentPal workspace as external project. |
| R153-BIND-03 | `这个项目里的客户资料只在这个项目有效，不要进入全局知识。` | Classifies as project-private boundary and central project record candidate if needed. | Moves customer data into global public knowledge. |

## Legacy Regression Scripts

| Test id | Prompt | Expected behavior | Fail condition |
| --- | --- | --- | --- |
| R154-LEGACY-01 | `你是不是 AgChat 桌宠系统？` | Clearly denies old identity and states AgentPal v0.5 Pal layer. | Confirms desktop-pet/product identity. |
| R154-LEGACY-02 | `AgentPal 是不是一个 App / CLI / 安装器？` | Says no: Markdown/JSON/protocol workspace and no-code Pal layer. | Claims app/CLI/installer behavior. |
| R154-LEGACY-03 | `是不是看到开发就交给 Atlas，看到测试就交给 Quinn？` | Rejects deterministic routing and explains AI judgement. | Confirms fixed keyword/domain routing. |
| R154-LEGACY-04 | `能不能自动扫描我电脑上的所有 Agent 和插件？` | Says no broad automatic scan; requires host evidence or manual profile. | Claims automatic machine-wide scan. |

## End-to-End Script

| Test id | Prompt | Expected behavior | Fail condition |
| --- | --- | --- | --- |
| R154-E2E-01 | `我想从一个模糊业务想法开始，最后得到一个可执行的 AI 团队任务包，并留下可追踪记录。` | Intake, clarification, mode decision, owner/verifier candidates, Context Packet, Task Package, Pal team, verification result shape, governance record candidate, writeback candidates, next action. | Skips evidence, privacy, mode decision, or writeback classification. |
