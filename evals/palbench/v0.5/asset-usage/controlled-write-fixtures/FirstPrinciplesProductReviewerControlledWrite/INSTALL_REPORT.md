# R200 Controlled Write Fixture Copy Report

date: 2026-07-01
host_mode: `current_codex_thread_agentpal_mode`
status: `controlled_write_test_artifact`

## Terminology

This is not a software install and not a user custom Pal installation.

Here, copy means a test-scoped fixture creation under:

```text
evals/palbench/v0.5/asset-usage/controlled-write-fixtures/FirstPrinciplesProductReviewerControlledWrite/
```

## Source

The fixture was copied from the existing user custom Pal test artifact:

```text
workspace/resources/user-pals/FirstPrinciplesProductReviewer/
```

The source path was read-only during R200 and must remain unchanged.

## Fixture Boundary

This fixture is:

- `official: false`
- `not_user_installed: true`
- `not_marketplace_listing: true`
- `not_contacts_registered: true`
- `source: copied_from_user_custom_pal_for_R200_controlled_write_rehearsal`

It is not:

- an official Pal;
- a central contacts entry;
- a real user-installed Pal;
- a Marketplace listing;
- runtime code, CLI, scanner, daemon, connector, backend service, or app runtime.

## Files Copied

The fixture copied the source Pal asset shape for controlled write rehearsal:

- `README.md`
- `PAL.md`
- `SKILL.md`
- `pal.json`
- `identity/`
- `knowledge/`
- `workflows/`
- `skills/`
- `runtime/`
- `memory/`
- `contacts/`
- `evals/`
- `marketplace/`

R200 then added fixture-only asset execution files under this fixture path.

## Rollback

To remove this test fixture, remove or archive only:

```text
evals/palbench/v0.5/asset-usage/controlled-write-fixtures/FirstPrinciplesProductReviewerControlledWrite/
```

Do not edit `official/pals/`, `workspace/organization/contacts/`, or the real
`workspace/resources/user-pals/FirstPrinciplesProductReviewer/` unless a
separate task explicitly authorizes that work.
