# Asset Execution Example

## Status

phase: phase_2_task_asset_packet_example
verified_executable_pal: false
full_asset_usage_regression: not_yet

This example shows how PalSmith should prepare an existing Pal composite
upgrade. It is an example, not a completed upgrade and not a host regression.

## Example Task

User says:

```text
我想给一个已有设计 Pal 加入新的语气、思维方式和一个 logo workflow。
```

## Asset Loading Gate

target_pal: PalSmith

task_type: existing Pal composite upgrade / Pal asset governance

required_assets:

- `official/pals/PalSmith-pal-governor/PAL.md`
- `official/pals/PalSmith-pal-governor/pal.json`
- `official/pals/PalSmith-pal-governor/SKILL.md`
- `official/pals/PalSmith-pal-governor/core/existing-pal-composite-upgrade-protocol.md`
- `official/pals/PalSmith-pal-governor/core/composite-pal-distillation-protocol.md`
- `docs/06-palsmith/palsmith-pal-completeness-guide.md`
- `core/pal-asset-execution-contract.md`
- `core/asset-loading-gate.md`
- target Pal root files and relevant identity / knowledge / workflow / eval
  indexes, after the target is identified

go_no_go_decision: `blocked_user_confirmation_required` before file writes

reasoning_summary: The request may change voice, thinking, role behavior,
workflow, and future tool usage. PalSmith must produce an upgrade plan and ask
for confirmation before any controlled write.

## Task Asset Packet

task_id: palsmith-existing-design-pal-upgrade-example

target_pal: PalSmith

task_type: existing Pal composite upgrade

user_goal: add new voice, thinking style, and logo workflow to an existing
design Pal

execution_mode: no-code upgrade plan and confirmation question

required_identity_assets:

- PalSmith root identity
- target Pal identity after target is named

required_voice_assets:

- target Pal voice or tone assets if present
- source boundary for the requested new voice

required_thinking_assets:

- cognitive distillation protocol
- target Pal mental model or decision assets if present

required_knowledge_assets:

- existing Pal upgrade protocol
- completeness guide
- target Pal job knowledge or design knowledge indexes

required_skill_assets:

- PalSmith composite distillation and Pal asset governance skills

required_workflows:

- existing Pal composite upgrade flow
- target logo workflow map proposal

required_runtime_policy:

- host Runtime may write files only after user confirmation

required_memory_scope:

- no private source material is written into public assets without approval

required_eval_assets:

- voice consistency eval
- cognitive consistency eval
- workflow boundary eval
- asset usage regression plan

optional_tools:

- file reads for target Pal inventory
- no writes before confirmation

loaded_assets:

- PalSmith root entry assets
- existing Pal composite upgrade protocol
- composite distillation protocol
- completeness guide
- Pal Asset Execution Contract
- Asset Loading Gate

missing_assets:

- target Pal path if not supplied
- source material for voice and thinking
- user authorization for controlled writes

allowed_tool_calls:

- read-only target Pal inventory after target path is known

blocked_tool_calls:

- direct edits to target `PAL.md`, identity, knowledge, workflows, memory,
  contacts, discovery, or Marketplace assets before upgrade plan confirmation

go_no_go_decision: `blocked_user_confirmation_required`

## Expected Execution

PalSmith should output:

- upgrade mode judgement;
- target Pal inventory request or summary;
- source and impersonation boundary;
- cognitive distillation plan;
- voice and personality distillation plan;
- logo workflow impact plan;
- target file map;
- eval plan;
- allowed and blocked write paths;
- confirmation question.

PalSmith must not route by keyword, must not edit first, and must not claim the
target Pal is upgraded until the Runtime returns file evidence and a later
review accepts it.

## Tools / Runtime Boundary

Codex, shell, file reads, image tools, design tools, and MCP tools are host
execution tools. They may gather inventory or perform approved writes, but they
are not PalSmith assets and do not replace the upgrade plan.

## Asset Use Summary

task_id: palsmith-existing-design-pal-upgrade-example

target_pal: PalSmith

used_identity_assets:

- `official/pals/PalSmith-pal-governor/PAL.md`

used_knowledge_assets:

- `official/pals/PalSmith-pal-governor/core/existing-pal-composite-upgrade-protocol.md`
- `official/pals/PalSmith-pal-governor/core/composite-pal-distillation-protocol.md`
- `docs/06-palsmith/palsmith-pal-completeness-guide.md`

used_runtime_policy:

- controlled writes require explicit confirmation

tools_called: none in this example

quality_gate_result: example only; real target Pal upgrade regression still
required

next_asset_improvement: add a target-specific upgrade example after a real
authorized upgrade rehearsal.

## Missing Asset Plan

missing_asset: target Pal identity, source material, and write confirmation

why_needed: PalSmith cannot design a safe target file map or eval plan without
knowing the actual Pal and source boundary.

temporary_fallback_allowed: yes, as a generic upgrade plan only.

recommended_asset_path: target Pal inventory packet and source-boundary note.

priority: high before any write.

## Lightweight Path

A one-line explanation of what "existing Pal composite upgrade" means may use a
lightweight path. Any actual voice, thinking, workflow, memory, discovery, or
publication change is not lightweight.

## What This Example Does Not Claim

- This does not mark PalSmith as newly or universally verified.
- This does not upgrade any existing Pal.
- This is not a full migration.
- This is not a runtime, backend, connector, scanner, daemon, or Marketplace
  implementation.
