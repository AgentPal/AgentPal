# Routing Memory Writeback Self-Test

## Purpose

Check that v0.3 Routing Memory records decisions and outcomes without becoming fixed routing or leaking private context.

## Required Assets

- `orchestration/routing-memory-writeback-protocol.md`
- `templates/orchestration/routing-decision-record.md`
- `templates/orchestration/routing-result-record.md`
- `workspace/organization/memory/routing/README.md`
- `workspace/organization/memory/routing/routing-decisions.example.jsonl.md`
- `examples/orchestration/routing-memory-reuse-example.md`

## Pass Criteria

- decision and result records exist;
- examples are synthetic and public-safe;
- records include task type, owner candidate, runtime candidate, reasoning level, context counts, verification result, and rework count;
- protocol says memory informs future candidates but does not create fixed routes;
- no local absolute paths, secrets, or private content appear.

## Failure Modes

- public example stores private project facts;
- next-time recommendation says future tasks must use one Pal;
- automatic database or scanner is implied;
- verification result is missing.

## Expected Result

Pass when writeback is manual, public-safe, and non-binding.
