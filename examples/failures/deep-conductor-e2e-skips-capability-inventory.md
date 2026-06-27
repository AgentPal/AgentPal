# Deep Conductor E2E Skips Capability Inventory Failure

## 错误行为

The conductor names Pal, Runtime, model, reasoning, Skill, plugin, or MCP candidates without checking any current Capability Inventory profile or explaining why it was unavailable.

## 为什么错

Capability Inventory is a judgement input for E2E planning. Without it, the package may assume unavailable host Runtime abilities or turn old experience into a hidden route.

## 正确行为

The package must include `capability_inventory_used` with profile reads, not-read profiles, and an honest fallback when profiles are missing. Profiles inform current judgement but do not force owner or Skill selection.

## 对应 eval

- `evals/orchestration/deep-conductor-e2e-capability-self-test.md`
- `evals/palbench-collaboration/PBC-068-e2e-skipped-capability-inventory-failure.md`
