# Orchestration

Orchestration files describe Pal routing, Simple Pal Mode handoff, context control, task packaging, future workflow topology, execution roles, Runtime Skill-aware packaging, cross-runtime memory, and cost-quality tradeoffs.

No non-Pal runtime is assumed available until explicitly provided by the current execution environment.

## Core Protocol Map

AgentPal shared gates live under `core/`. Orchestration-specific protocols live here:

| Area | File | Status |
| --- | --- | --- |
| Runtime response gate | `runtime-response-gate.md` | active v0.1 |
| Fast Route | `fast-route-protocol.md` | active as Simple Pal Mode pattern |
| Deep Conductor | `deep-conductor-protocol.md` | no-code future pattern, not execution |
| Project Conductor | `project-conductor-workflow.md` | no-code project-level task map and next-round package workflow |
| Pal Skill vs Runtime Skill | `pal-skill-vs-runtime-skill-protocol.md` | active separation rule |
| AI routing judgement | `ai-routing-judgement-protocol.md` | active v0.1 |
| Pal context slicing | `pal-context-slicing-protocol.md` | active v0.1 |
| Asset loading budget | `pal-asset-loading-budget.md` | active v0.1 |
| Task package output | `task-package-output-contract.md` | active v0.1 |
| Context Access List | `context-access-list-protocol.md` | design foundation; usable as documentation/template |
| Context Packet | `context-packet-protocol.md` | v0.3 no-code handoff prototype |
| Mention / Direct Pal | `mention-and-direct-pal-protocol.md` | v0.3 no-code collaboration prototype |
| Owner + Verifier | `owner-verifier-workflow-protocol.md` | v0.3 no-code staged workflow |
| Parallel Independent Review | `parallel-independent-review-protocol.md` | v0.3 no-code staged workflow |
| Plan -> Execute -> Verify | `plan-execute-verify-protocol.md` | v0.3 no-code staged workflow |
| Pal isolation and shared memory | `pal-isolation-and-shared-memory-protocol.md` | future design only |
| Routing Reward Memory | `routing-reward-memory-protocol.md` | design foundation/template only |
| Routing Memory Writeback | `routing-memory-writeback-protocol.md` | v0.3 no-code manual writeback prototype |
| Token / Cost-aware Conductor | `token-cost-aware-conductor-policy.md` | no-code context and verification policy |

Current task handling uses Simple Pal Mode. Research, templates, and future-design files do not activate Subagent Mode, external Agent calls, Runtime Skill execution, or Deep Conductor execution.


