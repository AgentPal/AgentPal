# R181 User Custom Pal Install Report

date: 2026-06-30
host_mode: `current_codex_thread_agentpal_mode`
installed_by: `R181 current Codex host rehearsal`
status: `user_custom_pal`

## Terminology

Here, installation is not a software installer.

Here, installation means a no-code Pal Pack enablement / placement / local-index flow.

## Source

source_draft_path:

```text
evals/palbench/v0.5/palsmith/draft-pal-packs/FirstPrinciplesProductReviewer/
```

review_evidence:

- `evals/palbench/v0.5/palsmith/r175-draft-pal-pack-quality-regression.md`
- `evals/palbench/v0.5/palsmith/r177-draft-pal-usage-regression-summary.md`
- `<agentpal-workspace-root>_dcos\开发记录\R178-FirstPrinciplesProductReviewerR177UsageRegressionLocalCommit完成报告.md`

## User Confirmation

user_confirmation_for_test: `true`

scope: `FirstPrinciplesProductReviewer draft -> user custom Pal test artifact only`

not_allowed:

- official Pal
- central contacts
- automatic discovery
- public Marketplace listing
- runtime code
- CLI
- scanner
- daemon
- connector
- backend service

confirmation_statement:

```text
For R181 test only, user confirmation is simulated by the main thread to create a user custom Pal test artifact under the approved non-official path.
```

## Target

target_path:

```text
workspace/resources/user-pals/FirstPrinciplesProductReviewer/
```

This path is not:

- `official/pals/`
- `workspace/organization/contacts/`
- official registry / roster
- public Marketplace content

## Files Copied

Copied Pal Pack assets:

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

Excluded from copied Pal runtime assets:

- R174 / R175 / R177 report files
- private memory
- private reports
- local state
- credentials
- temporary files
- external reference repositories
- generated cache files

## `pal.json` Migration

The copied `pal.json` was migrated to:

```json
{
  "schema": "agentpal.user-custom-pal-pack.v0.5",
  "status": "user_custom_pal",
  "official": false,
  "draft": false,
  "source_type": "palsmith_created_from_draft",
  "visibility": "private_by_default",
  "contact_discovery": "disabled_by_default",
  "marketplace_listing": "none"
}
```

Preserved install metadata:

- `source_draft_path`
- `installed_by`
- `installed_date`
- `installation_scope`

## Boundaries

official_boundary: `pass`

- The copied Pal remains `official: false`.
- No official Pal directory was created or modified for this user custom artifact.

contacts_boundary: `pass`

- Central contacts are not modified.
- Discovery is disabled by default.

marketplace_boundary: `pass`

- No public Marketplace listing was created.
- No Marketplace backend was introduced.

runtime_boundary: `pass`

- No runtime code, CLI, scanner, daemon, connector, backend service, or app runtime was added.

## Rollback

To undo this test artifact:

1. Remove or archive `workspace/resources/user-pals/FirstPrinciplesProductReviewer/`.
2. Remove its entry from `workspace/resources/user-pals/README.md`.
3. Remove related R181 evidence entries from `RESOURCE_INDEX.md` and `agentpal.json` if rolling back the evidence record.
4. Do not edit `official/pals/` or `workspace/organization/contacts/`.

## Not Run

- No official registration.
- No central contacts update.
- No discovery enablement.
- No Marketplace publication.
- No remote Git operation.
- No local commit in R181.
