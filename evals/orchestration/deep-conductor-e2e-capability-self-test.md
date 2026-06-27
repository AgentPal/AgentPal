# Deep Conductor E2E Capability Self-Test

## Purpose

Verify that Deep Conductor E2E uses Capability Inventory without turning it into routing automation.

## Passing criteria

- `capability_inventory_used` records profile status, profile reads, and unavailable or not-read profiles.
- Runtime, model, reasoning, Skill, plugin, MCP, and Pal profiles are read only when relevant.
- Runtime Skill candidates require current availability evidence before use.
- Pal-owned Skills and Runtime-installed Skills are separate fields.
- Capability profiles inform candidate judgement but do not force owners, reviewers, runtimes, Skills, or model choices.
- No internal local paths or private runtime notes appear in public examples.

## Failing patterns

- Candidate selection is made without profile evidence or fallback.
- Previous Runtime capability is assumed current after a host Runtime switch.
- A profile becomes an automatic route.

## Related failure example

- `examples/failures/deep-conductor-e2e-skips-capability-inventory.md`

## Shared E2E regression checklist

Every Deep Conductor E2E self-test must also check no-code boundary, memory usage, Capability Inventory, Context Budget, Runtime Skill separation, verification, Routing Memory, not fixed route language, and no internal path leakage.
