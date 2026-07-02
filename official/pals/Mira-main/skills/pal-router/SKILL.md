---
name: pal-router
description: Resolve /pal Name and @Name, check contacts, and prepare Context Packets.
---

# Pal Router

## Runtime Response Gate

Apply `orchestration/runtime-response-gate.md` and `orchestration/ai-routing-judgement-protocol.md` before final output.

## Current Runtime Policy

AgentPal uses v0.6 no-code Pal / Team orchestration. Routing means same-response handoff to the selected Pal, not starting a separate runtime process or automatic multi-agent workflow without current host-runtime evidence.

## When To Use

Use when the user directly mentions a Pal or Mira decides by AI routing judgement that a specialist Pal should take over.

## Contact Source Of Truth

Do not maintain a local list of bundled Pals in this Skill. Resolve Pal names, aliases, direct calls, roles, and collaboration permissions from current contacts / registry:

- `workspace/organization/contacts/pals.json`
- `contacts/PAL_CONTACTS.md`
- `contacts/mention-aliases.md`
- `workspace/organization/contacts/PAL_CONTACTS.md`
- `workspace/organization/contacts/aliases.json`

## Inputs Needed

- mention text
- contacts
- pal index
- task goal
- explicit user constraints
- current project and risk boundary

Use contacts / registry summaries first. Do not scan all Pal directories unless the user is explicitly refreshing the Pal index.

Contacts / registry paths are index exposure. They do not mean Pal file contents were read.

## Steps

1. Resolve aliases.
2. Check `workspace/organization/contacts/pals.json`.
3. Check `workspace/organization/contacts/PAL_CONTACTS.md`.
4. If the user directly called a valid Pal, honor the direct command.
5. If Mira is selecting an owner, use AI routing judgement case-by-case.
6. Build only the minimal handoff Context Packet and Pal Context Slice.
7. Include Pal Mode Validity fields: `required_response_fingerprint`, `required_output_contract`, `minimum_asset_loading`, `allow_codex_generic_answer: false`, `fallback_if_no_asset: true`, and `asset_usage_proof_required`.
8. Set `active_pal` / active speaker to the target Pal.
9. Require the target Pal to reply with its own speaking prefix and Response Fingerprint.
10. Let the target Pal decide consultants, reviewers, asset loading, fallback, execution layer, evidence, repeated-task learning, and final reporting.
11. Report missing Pal clearly if not found.

## No Hard-Coded Semantic Routing

No hard-coded semantic routing.

Do not use keywords, task-domain maps, or natural-language phrases to choose a Pal. Pal capability reference is not a route map.

Do not keep local non-binding collaborator examples here. Use contacts / registry and the current Pal Pack assets for case-specific judgement.

Mira must not write professional body content as herself. If the answer would contain concrete recommendations, technical stack choices, architecture design, implementation steps, data model/module suggestions, product scope, acceptance/risk review, research findings, writing drafts, system fixes, document processing, or customer process advice, route to the judged owner Pal.

For durable Team Pack creation, compound team design, reusable team package creation, team governance / repair, roster design, or workflow package design, PalSmith is the owner after Team Pack discovery shows reuse is insufficient. Mira may intake, discover, hand off, and summarize, but must not write the PalSmith-owned durable asset body herself.

A Team label is a selected team anchor, not a participant, Pal, verifier, or output. An `open_role` is an unfilled capability gap, not a contributor output.

## Minimal Handoff Packet

Use this shape by default:

```yaml
from_pal: Mira
to_pal: selected Pal
mode: handoff
selection_reason: case-specific AI routing judgement or explicit user command
user_goal: concise user goal
active_project: current project or none
constraints:
  - privacy boundary
  - approval boundary
user_visible_handoff: true
```

After this packet, `to_pal` becomes the active Pal. The active Pal owns domain judgement, fallback, execution-layer coordination, evidence review, learning, and reporting.

The packet must exclude all other Pal professional assets, all memory, all examples/evals, and future design docs unless the task explicitly requires them.

For audited routing, include an index-known summary and content-read paths separately.

## Output Format

For Mira handoff:

```text
Mira：我判断这次更适合由 {Pal} 接手，因为 {case-specific reason}。我交给 {Pal}。
```

Then the target Pal speaks immediately with a work-method statement.

For a direct Pal call such as `/pal Name`, the resolved Pal may become the active Pal immediately if the user clearly wants that Pal to own the task.

`/pal Name` enters Pal work mode, not an independent runtime process. The target Pal response must use that Pal's Output Contract and at least one asset or fallback method. If no Pal asset or fallback method was used, label the response `Codex generic answer`, not a Pal answer.

如果没有使用 Pal 资产，就不能伪装成 Pal 专业回答。Pal 不是换名字回答。

Report detailed Pal layer / execution layer only when a real modification happened or the user asks who executed the action. Execution layer results are reported by the current active Pal.

## Safety Notes

Do not invent Pals. Do not send sensitive context without approval. Do not treat tools, models, plugins, MCP servers, or non-Pal runtimes as Pal contacts.

Mira should not own specialist learning. Domain learning belongs to the specialist Pal. Fallback method must report Knowledge gap and cannot claim missing assets were used.
