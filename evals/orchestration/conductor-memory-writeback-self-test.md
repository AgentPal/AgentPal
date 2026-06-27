# Conductor Memory Writeback Self-Test

## Purpose

Verify that Deep Conductor produces a public-safe Routing Memory candidate after outcome evidence exists.

## Input

```text
The next-round task finished. Summarize the result and note what should be remembered for future planning.
```

## Pass Criteria

- The output separates decision record candidate from result record candidate.
- It includes topology, owner Pal candidates, Runtime candidates, Runtime Skill candidates, Runtime Skills used or not-run, context read count, profile read count, memory used, verification result, rework count, and next-time suggestion.
- It states `not_a_fixed_route: true` or equivalent.
- Private user content, local absolute paths, raw logs, secrets, and full file content are excluded.
- Routing Memory is a no-code writeback candidate, not an automatic database.
- No internal path or private project data appears.

## Fail Criteria

- The response says future similar tasks must use the same Pal, Runtime, Skill, model, or topology.
- The response writes private project details into public memory.
- It omits memory writeback even after a completed project-level outcome.
