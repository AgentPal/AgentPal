# R132-D Faye Deep Conductor Boundary Eval

## Purpose

This eval checks that R132-D adds Faye-specific Deep Conductor / governance loop
protocol assets without creating runtime automation, connector behavior, keyword
routing, customer-private leaks, or external project thick binding.

## Required Files

- `standards/deep-conductor/faye-deep-conductor-protocol.md`
- `standards/deep-conductor/delivery-pack-governance-loop.md`
- `standards/deep-conductor/context-access-list-for-delivery-pack.md`
- `templates/deep-conductor/faye-task-judgement-packet.md`
- `templates/deep-conductor/delivery-workflow-plan.md`
- `templates/deep-conductor/context-access-list.md`
- `templates/deep-conductor/verification-result.md`
- `templates/deep-conductor/routing-memory-record.json`
- `examples/deep-conductor/faye-video-growth-task-judgement.example.md`
- `examples/deep-conductor/faye-delivery-context-access-list.example.md`
- `examples/deep-conductor/faye-delivery-governance-loop.example.md`
- `release/fresh-clone-checks/r132d-local-faye-deep-conductor-validation.md`
- `release/integration-notes/r132d-index-update-notes.md`

## Checks

### 1. Protocols Exist

Pass when all three standard files exist and define Faye Delivery ownership,
Delivery Pack governance loop, Context Access List fields, and no-code
boundaries.

### 2. Templates Exist

Pass when all templates exist and the routing-memory JSON template parses.

### 3. Examples Exist

Pass when all examples exist and the video-growth task includes research,
script, brand check, video QA, placeholder-only private context, candidate Pals
as AI judgement inputs, and `not-run` / `missing` evidence states.

### 4. No Keyword Routing

Pass when R132-D files contain no active route map, deterministic dispatch table,
or fixed Pal assignment.

### 5. No Behavior Expansion

Pass when R132-D adds no connector, scanner, validator, installer, daemon,
database, marketplace, hub, auto-sync, auto-execution engine, external business
system API client, or credential store.

### 6. Public Safety

Pass when R132-D files contain no real credentials, tokens, customer data,
customer project facts, private business secrets, or internal development paths.

### 7. Thin Binding

Pass when R132-D does not create or authorize external project `.agentpal/`
asset directories by default.

### 8. Protected Paths

Pass when there is no diff under:

- `workspace/organization/contacts/**`
- `official/pals/**`
- `README.md`
- `README.zh-CN.md`
- `RESOURCE_INDEX.md`
- `agentpal.json`

## Expected Result

Expected R132-D result: `pass`.

If evidence is unavailable, report `missing`, `not-run`, or `blocked`; do not
smooth it into a pass.
