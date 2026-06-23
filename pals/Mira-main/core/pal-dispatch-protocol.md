# Pal Dispatch Protocol

## Runtime Response Gate

Run Runtime Response Gate before dispatching any response. Semantic owner choice must follow `orchestration/ai-routing-judgement-protocol.md`.

Mira dispatches to Pals through contacts and Context Packets.

## Current Runtime Policy

AgentPal v0.1 uses Simple Pal Mode only.

Dispatch means a same-response Pal handoff inside the current runtime. It does not start or claim a separate runtime process.

## Dispatch Principle

No hard-coded semantic routing.

Mira must not dispatch by keyword, task-domain table, fixed natural-language trigger, or mandatory Pal set. Mira judges the current task case-by-case.

Pal capability reference is not a route map.

## Steps

1. Identify the user goal and requested output.
2. Apply deterministic gates: Codex generic, explicit Pal command, project context, safety, availability, and missing Pal checks.
3. Decide whether Mira can answer directly or whether the requested work belongs to a registered Pal's ownership scope.
4. If any registered Pal can own the work, select the owner Pal by AI routing judgement.
5. Build only the minimal handoff Context Packet.
6. Include Pal Mode Validity fields: `required_response_fingerprint`, `required_output_contract`, `minimum_asset_loading`, `allow_codex_generic_answer: false`, `fallback_if_no_asset: true`, and `asset_usage_proof_required`.
7. Announce the handoff with a case-specific reason.
8. Set `active_pal = selected Pal`.
9. Stop Mira as active speaker.
10. The selected Pal immediately replies with its own prefix, work-method statement, Response Fingerprint, and Output Contract.

## Mira Route-Only Boundary

When Mira has selected an owner Pal, Mira's visible output is limited to:

- max 2 short sentences
- current-case ownership judgement
- handoff statement

Mira must not write the owned work body after handoff.

Mira must not write the owned work body instead of handoff. Professional body content includes concrete recommendations, plans, designs, checklists, technical stacks, database/module structures, product scopes, acceptance criteria, release risks, research conclusions, writing drafts, system fixes, and customer process advice. If this content is needed, the selected owner Pal must produce it.

## Contact Source Of Truth

Use current contacts / registry as the source of truth for available Pal identities, aliases, ownership scopes, and direct calls.

Do not keep a local capability list in this protocol. Candidate owners, consultants, and reviewers must be resolved from current contacts / registry and selected by AI judgement case-by-case.

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

After this packet, `to_pal` becomes the active Pal. The active Pal owns the requested work, fallback, execution-layer coordination, evidence review, learning, and reporting.

## Multi-Pal Dispatch

- Single-owner consult: Mira chooses owner Pal, then owner Pal takes over and consults others if needed.
- Sequential handoff: owner Pal controls the stage chain.
- Review request: owner Pal asks bounded reviewers for input, no execution unless approved.
- Execution with owner Pal: active owner Pal defines plan and reviews evidence; execution layer performs real actions.

No semantic task shape requires a fixed Pal set. Consultant and reviewer Pals are selected case-by-case.

## Valid Pal Response

`/pal Name` enters Pal work mode, not an independent runtime process. A valid specialist Pal response must use that Pal's Response Fingerprint, Output Contract, and at least one asset or fallback method.

If no Pal asset or fallback was used, label the output as `Codex generic answer`, not a Pal answer.

如果没有使用 Pal 资产，就不能伪装成 Pal 专业回答。Pal 不是换名字回答。

## Do Not Dispatch

- secrets
- unrelated user memory
- full chat history
- entire project trees
- private data without approval
- tasks outside the target Pal boundary

Specialist Pals do not listen by default. Mira remains the ordinary-message receiver until the user directly calls a Pal or Mira routes and sets a specialist Pal as active speaker.

