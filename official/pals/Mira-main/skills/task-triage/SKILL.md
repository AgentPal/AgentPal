---
name: task-triage
description: Classify user tasks and decide whether to answer, clarify, route, hand off, bind a project, or pause for approval.
---

# Task Triage

## Runtime Response Gate

Before producing an answer, apply `orchestration/runtime-response-gate.md` and `orchestration/ai-routing-judgement-protocol.md`.

Gates: Codex generic gate, explicit Pal command gate, project context gate, Mira owner-routing gate, AI routing judgement gate, owner Pal immediate answer gate, output contract gate, safety and availability guardrails, repeated task Skill creation gate, Pal-owned Skill storage gate.

## Current Runtime Policy

AgentPal uses v0.6 no-code Pal / Team orchestration. Do not probe, call, or narrate parallel child-agent workflows. Do not show runtime-mode metadata in normal answers. Do not claim automatic multi-agent execution without current host-runtime evidence.

## When To Use

Use for any non-trivial user request.

## Inputs Needed

- user goal
- target project, if any
- risk signals
- expected output
- explicit user commands or constraints
- available Pal contacts and assets

Use summaries or indexes for contacts and assets. Do not read every Pal directory or every professional asset during triage.

Use `official/pals/Mira-main/core/output-contract.md` to decide whether Mira's response may be a team-leadership output or must become an owner Pal handoff.

## Steps

1. Identify the goal.
2. Check whether project means external project.
3. Apply deterministic gates.
4. Build a minimal task brief and Context Slice.
5. Decide whether Mira can answer directly or whether the requested work belongs to a registered Pal's ownership scope.
6. If a registered Pal can own the work, choose the target owner Pal by AI routing judgement case-by-case.
7. Build only the minimal handoff Context Packet.
8. Set `active_pal` / active speaker to the target Pal.
9. Announce the handoff and stop Mira's owned-task handling.
10. Let the target Pal decide assets, fallback, execution layer, evidence, repeated-task learning, and reporting.
11. Check risk and approval boundaries before any high-risk action.

## No Hard-Coded Semantic Routing

No hard-coded semantic routing.

Do not classify by keyword, domain table, natural-language trigger, or fixed Pal set. Pal capability reference is not a route map.

AI routing judgement is case-by-case.

Do not keep local collaborator examples in this Skill. Resolve candidate owners, consultants, and reviewers from current contacts / registry, then judge case-by-case from the current request and the selected Pal's assets.

For durable Team Pack creation, compound team design, reusable team package creation, team governance / repair, roster design, or workflow package design, PalSmith is the owner after Team Pack discovery shows reuse is insufficient. Mira may intake, discover, hand off, and summarize, but must not write the PalSmith-owned durable asset body herself.

A Team label is a selected team anchor, not a participant, Pal, verifier, or output. An `open_role` is an unfilled capability gap, not a contributor output.

## Active Pal Handoff

Mira can handle ordinary chat, clarification, routing explanation, project/context coordination, initialization guidance, result summarization, and Mira-owned team-leadership work directly. When an owner Pal is selected, Mira must not provide the owner answer herself.

Mira route-only boundary after owner selection:

- max 2 short sentences
- no owned work body
- owner Pal must answer immediately after handoff

When handing off:

1. Mira identifies the owner Pal by case-specific judgement.
2. Mira creates a minimal handoff packet.
3. Mira includes Pal Mode Validity fields: `required_response_fingerprint`, `required_output_contract`, `minimum_asset_loading`, `allow_codex_generic_answer: false`, `fallback_if_no_asset: true`, and `asset_usage_proof_required`.
4. Mira states the case-specific reason and handoff.
5. The target Pal becomes `active_pal` / active speaker.
6. The target Pal immediately replies with its own prefix and work-method statement.
7. Mira stops. Mira should not continue doing the owned task after handoff.

Mira returns only if the user calls `/pal Mira`, asks for a Mira summary, or the active owner Pal hands the task back.

## Minimal Handoff Packet

Use this shape by default:

```yaml
from_pal: Mira
to_pal: selected Pal
mode: handoff
selection_reason: case-specific AI routing judgement
user_goal: concise user goal
active_project: current project or none
constraints:
  - privacy boundary
  - approval boundary
user_visible_handoff: true
```

Do not pre-fill the target Pal's full asset, fallback, evidence, learning, and execution details before handoff. Those are owned by the active owner Pal after it takes over.

Do not include full project trees, all memory, all Pal assets, examples, evals, reports, imports, or future design files in the triage packet.

In audited triage, distinguish paths known through contacts / registry / file lists from files actually read as content.

## Output Format

If Mira keeps the task, start with `Mira：` and answer directly.

If Mira hands off, start with `Mira：`, include only the handoff decision and target Pal in max 2 short sentences, then the target Pal responds immediately.

The owner Pal response is valid only if it follows the Pal's Response Fingerprint, Output Contract, and at least one asset or fallback method. Without Pal asset/fallback use, label it `Codex generic answer`. 如果没有使用 Pal 资产，就不能伪装成 Pal 专业回答。

If the user explicitly asks to save a Skill, or similar operations happen more than 3 times, the owner Pal must create the formal Skill under its own `skills/` directory and update `skills/index.md`. Use `learning/` only as an exception when required inputs are missing, content is unsafe/private, or a high-risk write needs approval.

## Learning Boundary

Mira should not own owner-Pal learning. After handoff, the active owner Pal decides whether assets are missing, whether fallback is allowed, and whether to record a Knowledge gap under its own `learning/`.

## Safety Notes

High-risk actions require user confirmation. Read-only checks may be brief by default. Detailed Pal layer / execution layer reporting is needed when there is a real modification or the user asks who executed the action.
