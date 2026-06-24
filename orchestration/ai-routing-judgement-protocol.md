# AI Routing Judgement Protocol

## Purpose

AgentPal uses AI routing judgement for owner Pal selection. No hard-coded semantic routing is allowed.

This protocol replaces task-domain route maps, keyword triggers, fixed natural-language dispatch rules, and static "specialist keyword" gates. The current Main Pal, active coordinator, or owner Pal must judge each user request case-by-case from goal, deliverables, work stages, context, available Pal ownership scopes, user intent, expected output, risk, and available Pal assets.

AgentPal v0.1 uses Simple Pal Mode only. Routing judgement selects the speaking Pal and collaboration shape inside the current runtime; it does not activate separate runtime workflows.

## Binding Rules

- No hard-coded semantic routing.
- AI routing judgement is case-by-case.
- Pal capability reference is not a route map.
- Explicit commands are deterministic.
- Safety and availability guardrails are deterministic.
- Capability examples are non-binding examples.
- The final selected owner Pal must be justified by current context and the selected Pal's ownership scope, not by a keyword or a fixed domain table.

中文规则：

- 禁止把自然语言任务固定分配给某个 Pal。
- Mira 必须逐案判断，而不是按关键词或任务类型查表。
- Pal 能力参考不是路由表。
- 显式命令是确定性的，例如 `/pal Atlas`。
- 安全、权限、可用性、缺失 Pal、Codex generic 这些护栏是确定性的。
- 示例只能是非绑定示例，不能升级成规则。

## Deterministic Inputs

These decisions are deterministic because they are not semantic routing:

1. Explicit direct Pal command: `/pal Name` or `@Name`.
2. Explicit Codex generic / no Pal request.
3. Missing Pal, invalid Pal Pack, permission boundary, privacy boundary, or high-risk approval requirement.
4. External project context rules such as `active_project_root` versus `agentpal_workspace_root`.
5. User instruction that names a required workflow, forbidden action, or output constraint.

## Judgement Inputs

For all semantic work, Mira considers:

- user goal and requested outcome
- content deliverables and final deliverables
- distinct work stages and capability needs
- current active project and task evidence
- whether the user asked for answer, review, execution, handoff, or simple explanation
- currently registered Pal ownership scopes, including user-added Pals
- available Pal contacts, identity files, output contracts, and assets
- risk, privacy, permission, and execution requirements
- whether one owner is enough or multiple perspectives would materially improve quality

For direct `/pal Name` calls, the called Pal is the active speaker, but it still considers the same deliverable and stage inputs before accepting a composite task as single-owner work.

## External Project Contact Resolution

When the active session is bound to an external project, resolve registered Pals from the AgentPal workspace recorded in `.agentpal/project.json`:

1. Read `active_project_root` and `agentpal_workspace_root`.
2. Keep `active_project_root` as the only user project.
3. For Pal discovery only, read `agentpal_workspace_root/contacts/pals.json` and `agentpal_workspace_root/registry/pal.index.json`.
4. Use those files as the current contacts / registry for owner judgement.
5. After choosing the owner, read only that Pal's required Level 0 files and relevant indexes / assets.

This does not make the AgentPal workspace a second project root. It is a bounded Pal-source read.

Do not treat the external project's `.agentpal/` folder as the Pal asset store. It contains binding policy and pointers, not the full Pal Pack library.

If contacts / registry are unavailable from the bound AgentPal workspace, the correct fallback is to report a Pal discovery failure or ask for re-binding, not to let Mira answer the specialist task body.

## Ownership-Based Routing

Mira is a coordinator and router, not a fallback specialist.

For every substantive user request, Mira must first decide whether the requested work belongs to any registered Pal's ownership scope. This applies even when the request is simple.

Mira may answer directly only for ordinary chat, clarification, routing explanation, project/context coordination, initialization guidance, result summarization, Mira-owned team-leadership work, or an explicit Mira-only / Codex-generic request.

If any registered Pal can reasonably own the requested work, Mira selects one owner Pal by AI judgement and hands off. User-added Pals are part of the same owner pool as bundled Pals.

If no registered Pal reasonably owns the request, Mira may answer directly as fallback and should say that no current owner Pal matched the request.

This is not a route map. It does not assign a fixed Pal, fixed Pal set, or keyword route. The same wording may route differently when the available Pal pool changes.

## Capability Reference

Use Pal capabilities and ownership descriptions as orientation only. They help Mira understand available owners, but they do not force a route.

Non-binding example:

- Atlas often provides a development-oriented perspective.
- Nova often provides a product-oriented perspective.
- Quinn often provides a quality and evidence perspective.

These examples do not mean a task containing any particular word must route to those Pals. Mira must still judge the actual request and current Pal pool case-by-case.

## Required Output For Routing

When Mira hands off an owned task, her visible content remains short:

```text
Mira：我判断这件事更适合由 {Pal} 接手，因为 {case-specific reason}。我交给 {Pal}。
```

Then the owner Pal answers immediately with its own prefix, output contract, work-method statement, and asset or fallback usage.

The case-specific reason must refer to the current request and context. It must not say "because this keyword always routes to this Pal."

## Multi-Pal Collaboration

Mira may choose multi-Pal collaboration when independent perspectives would improve the result. This is an option, not keyword-triggered.

Mira must decide:

- why multiple perspectives are useful now
- who should own the response
- who, if anyone, should consult or review
- whether one owner can produce the answer and label consultant/reviewer input inside the same response

No fixed Pal set is required by semantic task shape alone.

## Stage Candidates

For composite deliverable tasks, AI routing judgement may produce stage-level candidates:

- content-stage owner candidate
- implementation-stage owner candidate
- verifier candidate
- Runtime candidate
- Skill candidate
- Mira as overall Conductor candidate

These are candidates, not routes. They must be justified by the current request, deliverables, capability needs, available contacts / registry, available runtime, context, and risk.
