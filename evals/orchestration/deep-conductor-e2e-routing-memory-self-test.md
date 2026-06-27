# Deep Conductor E2E Routing Memory Self-Test

## Purpose

Verify that E2E closes the loop with public-safe routing memory candidates.

## Passing criteria

- `routing_memory_writeback` is present in the package.
- Synthesis report includes `memory_writeback_summary` and `next_round_recommendation`.
- Writeback candidate includes task type, topology, candidate owners or gaps, Runtime Skill availability, verification result, rework count when known, and next-time guidance.
- Private project facts, raw user memory, credentials, secrets, and internal local paths are excluded.
- Routing Memory guides future AI judgement but does not force selection.
- `not_a_fixed_route: true` remains present.

## Failing patterns

- No writeback candidate after a complex verified result.
- The recommendation says future similar tasks must use the same Pal, Runtime, Skill, model, or topology.
- Public memory stores private project details.

## Related failure example

- `examples/failures/deep-conductor-e2e-no-routing-memory.md`

## Shared E2E regression checklist

Every Deep Conductor E2E self-test must also check no-code boundary, memory usage, Capability Inventory, Context Budget, Runtime Skill separation, verification, Routing Memory, not fixed route language, and no internal path leakage.
