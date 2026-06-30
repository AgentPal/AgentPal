# FirstPrinciplesProductReviewerControlledWrite

This is a controlled write test artifact copied from the
FirstPrinciplesProductReviewer user custom Pal for R200. It is not an official
Pal and it is not a user-installed Pal.

Status: `controlled_write_test_artifact`

Source: `copied_from_user_custom_pal_for_R200_controlled_write_rehearsal`

Boundary flags:

- `official: false`
- `not_user_installed: true`
- `not_marketplace_listing: true`
- `not_contacts_registered: true`

This fixture exists only to rehearse controlled Pal asset writes under the Pal
Asset Execution Contract. It is not registered in central contacts, not listed
as an official Pal, not a Marketplace listing, and not a replacement for the
real user custom Pal under `workspace/resources/user-pals/FirstPrinciplesProductReviewer/`.

## R200 Boundary

Allowed write scope for this rehearsal:

- this fixture directory;
- R200 evidence files under `evals/palbench/v0.5/asset-usage/`;
- `RESOURCE_INDEX.md` and `agentpal.json` index registration.

Blocked write scope:

```text
official/pals/
workspace/organization/contacts/
workspace/resources/user-pals/FirstPrinciplesProductReviewer/
```

## How To Read This Fixture

- `PAL.md` defines the user custom Pal identity and work boundaries.
- `SKILL.md` is the entry point for loading the whole pack.
- `pal.json` records machine-readable controlled-write fixture metadata.
- `identity/` defines role, source boundary, and tone.
- `knowledge/` keeps the product-review mental models and job knowledge.
- `workflows/` contains review and complexity-compression flows.
- `skills/` maps Pal-owned skills and host Agent capability candidates.
- `runtime/` records when the host runtime may be asked to act.
- `memory/` defines approved memory candidate shapes.
- `contacts/` records collaboration boundaries.
- `evals/` defines quality gates, including R200 asset execution checks.
- `reports/` contains task-facing Asset Use Summary shapes.
- `marketplace/` contains metadata and publication boundary drafts only; it is not a public listing.

## Boundary

This controlled-write fixture is public-source-inspired in method, not a
real-person representation. It does not copy external source files, does not
claim authorization from any person or organization, and does not include
runtime code, CLI, scanner, daemon, connector, backend service, or Marketplace
backend.
