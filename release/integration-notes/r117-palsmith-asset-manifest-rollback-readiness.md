# R117 PalSmith Asset Manifest Rollback Readiness

Date: 2026-06-28

## Status

Rollback required: no.

## Rollback Target

If rollback becomes required, remove:

`official/pals/PalSmith-pal-governor/asset-manifest.json`

## Manual Rollback Action

Use a narrow delete or Git revert for only the PalSmith official manifest file, then rerun validation.

Expected manual action:

```text
Remove official/pals/PalSmith-pal-governor/asset-manifest.json
```

## Validation After Rollback

After rollback, verify:

- visible JSON parse passes;
- PalSmith `pal.json` parses;
- all official Pal `pal.json` files parse;
- central roster remains `9 / 9`;
- central roster diff remains empty;
- official Pal `pal.json` diff remains empty;
- official manifest count returns to `0`;
- PalSmith still loads by root entries and directory convention fallback;
- no external project `.agentpal/` write occurs.

## When Rollback Is Required

Rollback is required if post-writeback audit finds:

- official manifest JSON parse failure;
- route map or deterministic routing fields;
- credential or private data leak;
- raw report body or raw research dump;
- connector / scanner / API client behavior claim;
- central roster or PalSmith `pal.json` mutation;
- manifest required/fallback policy broken.

## Current Decision

Current rollback required: no.

Reason: official manifest parses, selected R95 gate passes, central roster and Pal `pal.json` files are unchanged, and no public-safety blocker was found.
