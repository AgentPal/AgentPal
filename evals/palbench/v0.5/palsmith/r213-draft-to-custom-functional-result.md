# R213 Draft To Custom Functional Result

## Status

result: `pass`

execution_mode: `real_host_thread_plus_file_level_fixture`

real_host_thread_id: `019f1c91-9fcc-7511-be62-fdcd740c77f7`

Real host note: the follow-up thread completed Case 2 and Case 3 as read-only
host dialogue. It produced a draft Pal Pack file map, Runtime Task Package
shape, user custom fixture install plan, default private `pal.json` fields, and
an explicit invocation simulation. It did not edit files.

## Case 2: Draft Pal Pack

Draft fixture:

```text
evals/palbench/v0.5/palsmith/r213-functional-fixtures/MiaCrossBorderCoachDraft/
```

Required root files:

- `pal.json`
- `PAL.md`
- `SKILL.md`
- `README.md`
- `metadata-draft.md`

Required directories:

- `identity/`
- `knowledge/`
- `workflows/`
- `memory/`
- `prompts/`
- `evals/`

Draft defaults:

- `official=false`
- `status=draft_test_artifact`
- not in `official/pals/`
- not in `workspace/organization/contacts/`
- not a public Marketplace listing
- no runtime/backend/CLI/scanner/daemon/connector

## Case 3: User Custom Pal Fixture

User custom fixture:

```text
evals/palbench/v0.5/palsmith/r213-functional-fixtures/user-pals/MiaCrossBorderCoach/
```

Fixture defaults:

- `official=false`
- `pal_type=user_custom_pal`
- `contact_discovery=disabled_by_default`
- `contacts_registration=false`
- `delegation_enabled=false`
- `marketplace_listing=none`
- `memory_access=minimal`

The fixture is intentionally not written to:

```text
workspace/resources/user-pals/
```

## Explicit Invocation Rehearsal

Input:

```text
/pal MiaCrossBorderCoach
请帮我给一个刚起步的跨境独立站新手制定 7 天行动计划。
```

Expected Pal-shaped output:

1. Stage judgement: beginner with insufficient operational baseline.
2. Day 1: define target market, category, budget, and margin guard.
3. Day 2: reject products with weak shipping, supply, or trust fit.
4. Day 3: choose one offer and one buyer pain.
5. Day 4: draft product page promise, FAQ, trust section, and checkout path.
6. Day 5: prepare three traffic angles and stop-loss rule.
7. Day 6: run readiness checklist before any ad spend.
8. Day 7: review metrics, customer questions, and next action.

Required data:

- target market;
- product category;
- product cost and selling price;
- shipping model;
- available weekly budget;
- store status.

Risks:

- spending before store trust is ready;
- weak margin after traffic test;
- product selected only by trend without buyer pain;
- no stop-loss rule.

Private memory candidate:

- seller stage;
- active product hypothesis;
- weekly budget;
- next checkpoint.

## Decision

`pass`

The draft-to-custom path is ready for user testing as a controlled workflow.
