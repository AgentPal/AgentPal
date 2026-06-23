# Context Packet Protocol

Context Packet is the controlled handoff format for Pal collaboration.

AgentPal v0.1 uses same-response handoff in Simple Pal Mode only.

## Mira Handoff Fields

When Mira hands off to a specialist Pal, use the minimum task packet:

- `from_pal`
- `to_pal`
- `mode`
- `user_goal`
- `task_type`
- `active_project`
- `constraints`
- `user_visible_handoff`
- `required_response_fingerprint`
- `required_output_contract`
- `minimum_asset_loading`
- `allow_codex_generic_answer`
- `fallback_if_no_asset`
- `asset_usage_proof_required`

## Principles

- Share the minimum useful context.
- Do not forward complete chat history by default.
- Do not share unrelated memory.
- Do not include secrets or credentials.
- Do not grant whole-project access unless task scope requires it.
- Tell the target Pal the user goal, task type, active project, and constraints.
- Set `mode: handoff` for owned tasks by default.
- Set `user_visible_handoff: true`.
- Set `allow_codex_generic_answer: false` for specialist handoff packets. If the target Pal cannot use any Pal asset or fallback method, the response must be labeled `Codex generic answer` rather than a valid Pal response.
- Set `fallback_if_no_asset: true`, because missing specialist assets should use explicit fallback instead of fake asset claims.
- Require the target Pal's Response Fingerprint and Output Contract.
- Require a light work-method statement in the target Pal's first answer.
- Require the owner Pal to answer immediately after Mira handoff.
- After handoff, the target Pal becomes active speaker and decides whether to add assets used, Knowledge gap, fallback method, execution layer, evidence, repeated task record, formal Skill trigger, or formal Skill target.
- Mira should not fill all specialist fields before handoff.

Mira route-only applies before the Context Packet is handed off: max 2 short sentences, only ownership judgment and handoff, no owned work body.

Use `templates/context-packet/context-packet-template.md` when creating a packet.

## Minimal Handoff Example

```text
from_pal: Mira
to_pal: selected_pal_from_contacts_registry
mode: handoff
user_goal: 检查系统启动项都有哪些
task_type: system-startup-audit
active_project: none
constraints:
  - read-only first
  - do not modify startup items without user confirmation
user_visible_handoff: true
required_response_fingerprint: selected Pal response fingerprint from registry / response-fingerprints
required_output_contract: selected Pal output contract from registry / Pal Pack
minimum_asset_loading:
  - selected Pal PAL.md
  - selected Pal output contract
  - selected Pal response fingerprint
  - selected Pal asset or fallback method
allow_codex_generic_answer: false
fallback_if_no_asset: true
asset_usage_proof_required: true
```

## Specialist Expansion After Handoff

After the active specialist Pal takes over, that Pal may add:

- `asset_loading_level`
- `known_assets_used`
- `response_fingerprint_used`
- `output_contract_used`
- `asset_usage_proof`
- `knowledge_gap`
- `fallback_allowed`
- `fallback_method`
- `execution_layer`
- `evidence_required`
- `repeated_task_record`
- `formal_skill_trigger`
- `formal_skill_target`
- `consultant_pals`
- `reviewer_pals`

The active Pal owns these fields, not Mira.

## Pal Mode Validity Fields

`required_response_fingerprint` points to `response-fingerprints/{Pal}.md`.

`required_output_contract` points to `pals/{Pal-role}/core/output-contract.md`.

`minimum_asset_loading` states the minimum identity, contract, fingerprint, and domain asset or fallback that must be used before a specialist Pal answer is valid.

`allow_codex_generic_answer: false` means a generic Codex answer must not be disguised as Pal work.

`fallback_if_no_asset: true` means missing assets are allowed only when the active specialist Pal names fallback method and does not claim a missing asset was used.

`asset_usage_proof_required` is required for complex tasks, release gates, evals, and reports.

## Ownership Content

For owned tasks, the Context Packet should name why the owner Pal is required:

- selected owner Pal id and display name from current contacts / registry
- case-specific ownership reason
- relevant ownership scope or output contract reason
- why Mira should not answer directly
- whether consultant or reviewer Pals are needed, resolved from current contacts / registry

## Project Context

For external project work, include only task-relevant project files. Do not include credentials, private files, secrets, unrelated personal memory, or the whole project tree by default.

If the target Pal needs more context, ask the user or request a narrower file scope.

## Learning And Fallback Fields After Handoff

`known_assets_used` lists actual specialist assets read. Do not claim an asset was used unless it was read.

`knowledge_gap` states missing Skill, Knowledge Card, Runbook, or Workflow assets.

`fallback_allowed` says whether fallback method is safe for this task.

`fallback_method` names the method, such as traditional professional method, read-only query, user-provided information, or execution-layer evidence.

`repeated_task_record` points to the owner Pal's `learning/repeated-tasks.md`.

`formal_skill_trigger` is `explicit_user_request` or `similar_operation_count_gt_3`.

`formal_skill_target` points to the owner Pal's `skills/<skill-id>/SKILL.md`.

Mira should not own specialist learning. Domain learning belongs to the specialist Pal. The active specialist Pal reports fallback and learning details directly.

