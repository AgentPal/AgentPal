# Deep Conductor E2E Memory Self-Test

## Purpose

Verify that Deep Conductor E2E uses approved memory when relevant and reports missing memory honestly.

## Passing criteria

- `memory_used` states `used`, `missing`, `not_approved`, `stale`, or `not_needed`.
- Cross-runtime continuation reads only named memory summaries or snapshots within the Context Budget.
- Private memory, raw chat history, secrets, and local paths are excluded from public packages.
- Missing memory triggers fallback planning and does not become invented continuity.
- Memory guides current judgement but does not become fixed routing.
- Synthesis report includes `memory_writeback_summary`.

## Failing patterns

- The package silently starts from zero during a continuation task.
- Raw private memory is copied into Context Packets.
- Routing Memory is treated as a command for future selection.

## Related failure example

- `examples/failures/deep-conductor-e2e-missing-memory.md`

## Shared E2E regression checklist

Every Deep Conductor E2E self-test must also check no-code boundary, memory usage, Capability Inventory, Context Budget, Runtime Skill separation, verification, Routing Memory, not fixed route language, and no internal path leakage.
