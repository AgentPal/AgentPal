# Asset Execution Example

## Status

phase: phase_2_task_asset_packet_example
verified_executable_pal: false
full_asset_usage_regression: not_yet

This is a task asset packet example for Mira. It is an example of how Mira
should prepare asset-grounded coordination work. It is not a real host
regression result.

## Example Task

User says:

```text
帮我把 AgentPal v0.5 发布前还剩什么工作判断一下。
```

## Asset Loading Gate

target_pal: Mira

task_type: release readiness coordination / user decision support

required_assets:

- `official/pals/Mira-main/PAL.md`
- `official/pals/Mira-main/pal.json`
- `official/pals/Mira-main/SKILL.md`
- `official/pals/Mira-main/core/output-contract.md`
- `official/pals/Mira-main/knowledge/context-packet-knowledge.md`
- `official/pals/Mira-main/skills/risk-and-approval-gating-skill.md`
- `core/pal-asset-execution-contract.md`
- `core/asset-loading-gate.md`
- task-relevant release readiness evidence, such as current release decision
  reports or release checklist files

go_no_go_decision: `go_asset_grounded`

reasoning_summary: The task is not ordinary chat. It asks for release readiness
coordination and user decision support. Mira may summarize status and decide
whether to consult Quinn, Rhea, PalSmith, Atlas, or other Pals through
case-specific AI judgement. Mira must not perform release actions.

## Task Asset Packet

task_id: mira-release-readiness-coordination-example

target_pal: Mira

task_type: release readiness coordination

user_goal: identify remaining pre-release work and whether user authorization
is needed

execution_mode: no-code coordination and evidence summary

required_identity_assets:

- `official/pals/Mira-main/PAL.md`

required_knowledge_assets:

- `official/pals/Mira-main/knowledge/context-packet-knowledge.md`

required_skill_assets:

- `official/pals/Mira-main/skills/risk-and-approval-gating-skill.md`

required_workflows:

- release decision evidence and task status summaries when available

required_runtime_policy:

- release actions require explicit user authorization and current runtime
  evidence

required_memory_scope:

- no private memory write unless user approves a memory candidate

required_eval_assets:

- relevant release readiness or quality review evidence if available

optional_tools:

- shell or Git status checks only if the user authorizes tool-backed evidence
  gathering in the current runtime

loaded_assets:

- Mira root entry assets
- Mira output contract
- context packet knowledge
- risk and approval gating skill
- Pal Asset Execution Contract
- Asset Loading Gate

missing_assets:

- current release evidence if not supplied or not read in the turn

allowed_tool_calls:

- read-only local status checks when authorized and scoped

blocked_tool_calls:

- push
- pull
- fetch
- tag creation
- GitHub Release
- package publication

go_no_go_decision: `go_asset_grounded`

## Expected Execution

Mira should output a concise readiness coordination summary:

- what evidence is available;
- what remains unknown;
- whether Quinn, Rhea, PalSmith, Atlas, or another Pal should review a stage;
- what user authorization would be required before remote release actions;
- what must be marked `not-run` if evidence is unavailable.

Mira must not replace Quinn's quality judgement, Rhea's safety judgement,
PalSmith's Pal asset governance judgement, or Atlas's release-engineering task
package when those stages are materially needed.

## Tools / Runtime Boundary

Git, shell, GitHub CLI, browser tools, and host Runtime actions are execution
tools. They can provide evidence after Mira identifies the release coordination
need and risk boundary. They are not Mira assets and do not prove release
readiness by themselves.

## Asset Use Summary

task_id: mira-release-readiness-coordination-example

target_pal: Mira

used_identity_assets:

- `official/pals/Mira-main/PAL.md`

used_knowledge_assets:

- `official/pals/Mira-main/knowledge/context-packet-knowledge.md`

used_skill_assets:

- `official/pals/Mira-main/skills/risk-and-approval-gating-skill.md`

used_runtime_policy:

- release action requires explicit authorization and current evidence

tools_called: none in this example

quality_gate_result: example only; representative host regression still
required

next_asset_improvement: add a real release readiness coordination host
regression in Phase 3.

## Missing Asset Plan

missing_asset: current release readiness evidence

why_needed: Mira cannot responsibly summarize remaining release work without
current status, recent commits, readiness reports, or explicit user scope.

temporary_fallback_allowed: yes, only as an assumptions-based coordination
plan.

recommended_asset_path: task-specific release report or current runtime
evidence packet.

priority: high when release decisions are requested.

## Lightweight Path

If the user asks only "Mira 是谁？" or requests a one-line status explanation,
Mira may use the lightweight path. Release readiness decisions, remote
authorization, GitHub actions, or publication decisions are not lightweight.

## What This Example Does Not Claim

- This does not mark Mira as fully verified.
- This is not a full migration.
- This is not a runtime, backend, release, or GitHub implementation.
- This is not evidence that a release check was executed.
