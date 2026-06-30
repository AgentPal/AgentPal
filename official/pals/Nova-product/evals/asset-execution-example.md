# Asset Execution Example

## Status

phase: phase_2_task_asset_packet_example
verified_executable_pal: false
full_asset_usage_regression: not_yet

This example shows how Nova should handle a product decision with privacy and
adoption trade-offs. It is not a real product acceptance test.

## Example Task

User says:

```text
AgentPal 要不要默认自动发现所有 user custom Pal？
```

## Asset Loading Gate

target_pal: Nova

task_type: product decision / privacy boundary / scope control

required_assets:

- `official/pals/Nova-product/PAL.md`
- `official/pals/Nova-product/pal.json`
- `official/pals/Nova-product/SKILL.md`
- `official/pals/Nova-product/core/output-contract.md`
- `official/pals/Nova-product/skills/scope-control-skill.md`
- `official/pals/Nova-product/knowledge/risk-assumption-knowledge.md`
- `core/pal-asset-execution-contract.md`
- `core/asset-loading-gate.md`
- current user custom Pal authorization docs when available

go_no_go_decision: `go_asset_grounded`

reasoning_summary: The task is a product decision with privacy, trust,
configuration, and governance risk. Nova should not default to convenience only
and must separate product recommendation from implementation.

## Task Asset Packet

task_id: nova-user-custom-pal-discovery-default-example

target_pal: Nova

task_type: product decision

user_goal: decide whether AgentPal should automatically discover all user
custom Pals by default

execution_mode: no-code product judgement

required_identity_assets:

- Nova root identity and product role

required_knowledge_assets:

- product risk and assumption knowledge
- privacy / authorization docs for user custom Pals if available

required_skill_assets:

- scope control skill

required_workflows:

- product decision or scope-control workflow when needed

required_runtime_policy:

- no runtime discovery behavior should be claimed or added by this product
  decision

required_memory_scope:

- user custom Pal privacy and authorization preferences are private unless
  explicitly approved

required_eval_assets:

- acceptance criteria for safe discovery defaults

optional_tools:

- none required for product judgement unless current docs must be checked

loaded_assets:

- Nova root entry assets
- output contract
- scope control skill
- risk assumption knowledge
- Pal Asset Execution Contract
- Asset Loading Gate

missing_assets:

- current user custom Pal authorization policy if not supplied

allowed_tool_calls:

- read-only documentation lookup if needed and scoped

blocked_tool_calls:

- changing discovery defaults
- modifying contacts
- enabling delegation
- adding backend discovery behavior

go_no_go_decision: `go_asset_grounded`

## Expected Execution

Nova should output a product decision such as:

- recommendation: do not auto-discover all user custom Pals by default;
- product reason: user trust, privacy, surprise minimization, and reversible
  control matter more than zero-configuration convenience;
- trade-off: discovery friction increases, but explicit authorization protects
  user intent;
- safer alternative: opt-in discovery per Pal, with separate invocation,
  delegation, contacts registration, and publication controls;
- evidence gaps: mark unknowns or `not-run` for user testing, implementation
  feasibility, and release safety if not checked.

Nova keeps the final product decision with the user.

## Tools / Runtime Boundary

Documentation lookup, shell commands, config writes, and any discovery
mechanism are execution-layer actions. They are not Nova assets. Nova can define
the product judgement and acceptance boundary; the current Runtime would execute
only after a separate approved task.

## Asset Use Summary

task_id: nova-user-custom-pal-discovery-default-example

target_pal: Nova

used_identity_assets:

- `official/pals/Nova-product/PAL.md`

used_knowledge_assets:

- `official/pals/Nova-product/knowledge/risk-assumption-knowledge.md`

used_skill_assets:

- `official/pals/Nova-product/skills/scope-control-skill.md`

used_runtime_policy:

- product judgement does not implement runtime discovery

tools_called: none in this example

quality_gate_result: example only; user research and host regression still
required

next_asset_improvement: add a Phase 3 real product-decision regression using
current authorization docs.

## Missing Asset Plan

missing_asset: current user custom Pal authorization policy and user evidence

why_needed: Nova cannot fully validate default discovery without knowing the
current authorization model and user expectations.

temporary_fallback_allowed: yes, use privacy-first product reasoning and mark
research/validation as not-run.

recommended_asset_path: user custom Pal authorization docs and product decision
record.

priority: medium-high before changing defaults.

## Lightweight Path

If the user asks for a short definition of user custom Pal discovery,
lightweight path may be enough. Default discovery policy, privacy boundary, or
product-roadmap decisions are not lightweight.

## What This Example Does Not Claim

- This does not mark Nova as fully verified.
- This is not a full migration.
- This does not change any discovery default.
- This is not a runtime, backend, connector, or Marketplace implementation.
