# Deep Conductor E2E Cross-Runtime Continuation Example

## User input

Continue the same AgentPal work after moving from Codex to another Markdown-capable CLI runtime.

## Deep Conductor E2E Package

```yaml
schema: agentpal.deep-conductor-e2e-package.v0.3
package_id: e2e-cross-runtime-continuation-example
user_goal: continue work across host Runtime change
project_or_single_task: project
workflow_topology:
  selected: project_conductor + plan_execute_verify
  reason: continuation needs memory reuse, capability re-check, and evidence-preserving next packages
  not_a_fixed_route: true
context_usage_report_required: true
not_a_fixed_route: true
```

## Context Budget

- read approved memory snapshots and routing summaries first;
- read current Runtime capability profile only for named needs;
- read project files only when the continuation package requires evidence;
- stop if memory is private, stale, or not approved.

## Memory used

- Pal Project Memory Snapshot;
- Routing Memory summary;
- Runtime Skill Usage Memory;
- Verification Memory when available;
- missing memory is recorded as `missing`, not replaced with chat history.

## Capability Inventory used

Capability Inventory is re-read for the current host Runtime. Previous Runtime capabilities are not assumed current.

## Topology selected

Project Conductor with Plan -> Execute -> Verify. The goal is to continue from approved state, avoid repeated reads, and re-check current execution capability.

## Context Packets

- continuation packet: prior done/not-done state, do-not-repeat items, current goal;
- runtime capability packet: named capability needs, allowed profile reads, blocked checks;
- verification packet: evidence that must be current in the new Runtime.

## Runtime Skill-aware packages

- only named Runtime Skill candidates from the package are checked;
- availability may be `available`, `unavailable`, `unknown`, or `blocked`;
- fallback package is used when the new Runtime lacks a previous Skill.

## Verification plan

- memory freshness and approval status;
- current Runtime access evidence;
- current file/Git/tool evidence when relevant;
- continuation outputs do not leak private memory.

## Synthesis report

```yaml
schema: agentpal.deep-conductor-e2e-synthesis-report.v0.3
report_id: e2e-cross-runtime-continuation-report-example
goal: continue across host Runtime
what_was_planned: memory-first continuation with current capability re-check
what_was_executed_by_runtime: bounded reads or writes performed by current host Runtime only
what_was_verified: memory approval, capability evidence, not-repeat list
agreement: [continue from valid memory instead of starting from zero]
conflicts: [previous Runtime Skill may be unavailable now]
risks: [stale memory, private memory leakage]
missing_evidence: []
next_round_recommendation:
  action: refresh memory snapshot after verified completion
  not_a_fixed_route: true
requires_user_decision:
  needed: false
  decisions: []
```

## Routing Memory candidate

Store whether memory reuse worked, what changed between host Runtimes, fallback used, verification result, and next continuation advice.

## No-code boundary note

This example does not create memory sync, a database, daemon, or cross-runtime automation. It uses bounded Markdown memory packages.
