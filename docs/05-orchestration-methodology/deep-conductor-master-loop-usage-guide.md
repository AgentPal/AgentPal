# Deep Conductor Master Loop Usage Guide

Deep Conductor is AgentPal's no-code master loop for complex goals and project-level coordination.

It connects existing v0.3 components into one usable path:

```text
project goal -> memory -> capability inventory -> context budget -> topology -> context packets -> Runtime Skill-aware packages -> verification -> synthesis -> routing memory writeback -> next-round task pool
```

## What Deep Conductor Is

Deep Conductor is a Pal-layer planning, allocation, context-control, verification, and memory-writeback method.

It helps Mira or the current owner Pal:

- decide whether a goal is a single task or a project-level continuing task;
- identify deliverables, phases, and task pools;
- read bounded Pal memory, project memory, Routing Memory, and Capability Inventory;
- create a complete E2E package when the work needs end-to-end project-level closure;
- choose workflow topology candidates;
- create Context Packets and Runtime Skill-aware Task Packages;
- plan verification before claiming completion;
- prepare Routing Memory candidates and next-round packages.

## What Deep Conductor Is Not

Deep Conductor is not:

- an executor;
- a background project manager;
- a CLI, scanner, validator, installer, daemon, service, database, desktop app, or web app;
- a native slash-command runtime;
- an automatic external Agent caller;
- automatic multi-runtime scheduling;
- a route table or keyword dispatcher.

The host Runtime performs file reads, writes, commands, tool calls, publishing, rendering, browsing, and other execution only when it is available, authorized, and able to return evidence.

## The 12-Step Master Loop

1. Goal Intake.
2. Project / Pal Memory Loading.
3. Deliverable and Stage Judgement.
4. Capability Inventory Read.
5. Runtime Skill / Plugin / MCP Awareness.
6. Workflow Topology Selection.
7. Context Access Planning.
8. Prompt Shaping and Context Budgeting.
9. Runtime Task Package Generation.
10. Verification Planning.
11. Synthesis and User-facing Explanation.
12. Routing Memory Writeback Candidate.

For full-loop work, these steps are represented together in `templates/orchestration/deep-conductor-e2e-package.md`. The post-work summary uses `templates/orchestration/deep-conductor-e2e-synthesis-report.md`.

## How It Combines Existing Assets

- Pal memory: carries Pal-owned continuity, user preferences, accepted project direction, and repeated task lessons.
- Project memory: summarizes current project state when available and approved.
- Routing Memory: provides previous routing outcomes as evidence, never as fixed routes.
- Capability Inventory: provides Runtime / Model / Reasoning / Runtime Skill / Plugin / MCP / Pal capability candidates.
- Runtime-installed Skills / Plugins / MCP: appear only as host Runtime candidates and require current availability, fallback, execution evidence, and verification before completion claims.
- Pal-owned Skills: Pal methods, workflows, runbooks, and output contracts used to judge and package work.
- Context Packet: bounds what a Pal, verifier, reviewer, or Runtime package receives.
- Workflow Topology: chooses Fast Route, Owner + Verifier, Plan -> Execute -> Verify, Parallel Independent Review, project conductor workflow, or another no-code pattern.
- Verification: states evidence, result records, not-run handling, and repair package needs.
- Token / Cost policy: controls read depth, profile loading, memory reuse, model/reasoning suggestions, and verification tradeoffs.

## When To Use Deep Conductor

Use Deep Conductor when:

- the user gives a project-level goal;
- the task has multiple stages or deliverables;
- the work must produce next-round Runtime packages;
- Capability Inventory, memory, or Runtime Skill candidates materially affect the plan;
- verification must be planned before execution;
- context bloat or cost risk is high;
- multiple Pal perspectives may be useful but must stay bounded.

## When Not To Use Deep Conductor

Do not use it when:

- a single owner Pal can safely answer directly;
- the user wants a short ordinary answer;
- there is no meaningful project state, memory, capability, or verification decision;
- the user explicitly asks not to enter Pal Mode or asks for a generic runtime answer;
- using the loop would add ceremony without improving outcome quality.

## Typical Outputs

Deep Conductor may output:

- Deep Conductor E2E package;
- project task map;
- workflow topology recommendation;
- context budget plan;
- Runtime Skill-aware task packages;
- Runtime Skill availability check and fallback packages when needed;
- verification package;
- E2E synthesis report;
- next-round runtime task package;
- conductor decision record;
- routing memory candidate;
- user-facing explanation.

## No-Code Boundary

All outputs are Markdown / JSON-like no-code artifacts for the host Runtime to read and act on. The presence of a plan, task map, package, record, example, or eval does not prove that execution happened.

Completion claims require evidence returned by the host Runtime or another approved evidence source.

The E2E package is not automatic execution. A host Runtime may follow its task packages by stage and must return evidence, not just completion text.
