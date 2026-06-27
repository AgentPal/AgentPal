# Deep Conductor E2E Package Self-Test

## Purpose

Verify that a Deep Conductor E2E Package is complete, bounded, and not presented as automatic execution.

## Passing criteria

- Includes `schema`, `package_id`, `user_goal`, `project_or_single_task`, `memory_used`, `capability_inventory_used`, `context_budget_plan`, `workflow_topology`, `context_packets`, `runtime_skill_aware_packages`, `owner_verifier_plan`, `parallel_review_plan`, `plan_execute_verify_plan`, `runtime_task_packages`, `verification_plan`, `context_usage_report_required`, `routing_memory_writeback`, `user_facing_explanation`, `no_code_boundary`, and `not_a_fixed_route: true`.
- States no-code boundary: no runtime program, service, daemon, installer, scanner, validator, UI, database, token meter, cost calculator, or automatic executor.
- Separates Pal-owned Skills from host Runtime-installed Skills.
- Uses Capability Inventory as judgement input, not fixed selection.
- Includes Context Budget and Context Usage Report requirement.
- Includes verification and Routing Memory writeback candidate.
- Uses no internal local paths, secrets, credentials, private memory, or private project facts.

## Failing patterns

- Package omits verification because the task is expensive.
- Runtime is described as the Pal-layer owner.
- A previous routing result is treated as a rule.
- The package contains local absolute paths or private report locations.

## Shared E2E regression checklist

Every Deep Conductor E2E self-test must also check no-code boundary, memory usage, Capability Inventory, Context Budget, Runtime Skill separation, verification, Routing Memory, not fixed route language, and no internal path leakage.
