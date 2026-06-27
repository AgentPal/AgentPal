# Mira Deep Conductor E2E Package Example

## User input

Coordinate a project-level release readiness task and prepare the next round.

## Mira output shape

```text
Mira：这是一个需要 Deep Conductor E2E 的项目级任务，因为它同时需要记忆延续、Capability Inventory、Context Budget、Runtime Skill-aware packages、验证、综合报告和下一轮建议。

我会输出 Deep Conductor E2E Package，并说明当前调度理由。候选 Pal、Runtime、Skill 和 topology 都是本案判断，不是固定路由；Runtime 只有在当前执行层有权限和证据时才执行。
```

## Required package pieces

- `memory_used`
- `capability_inventory_used`
- `context_budget_plan`
- `workflow_topology`
- `context_packets`
- `runtime_skill_aware_packages`
- `verification_plan`
- `routing_memory_writeback`
- `user_facing_explanation.scheduling_reason`
- `user_facing_explanation.next_round_recommendation`
- `not_a_fixed_route: true`

## Boundary

Mira explains and packages the work. The host Runtime executes real file reads, writes, commands, or tool calls only with current evidence.
