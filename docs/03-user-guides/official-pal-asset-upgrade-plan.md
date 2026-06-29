# Official Pal Asset Upgrade Plan

Date: 2026-06-28

## Purpose

This guide summarizes the R98-B audit and upgrade plan for the 9 official Pal
Packs.

Primary references:

- `evals/palbench/pal-asset/r98b-official-pal-asset-audit.md`
- `evals/palbench/pal-asset/r98b-official-pal-upgrade-gap-table.md`
- `release/integration-notes/r98b-official-pal-upgrade-plan.md`
- `release/fresh-clone-checks/r98b-local-official-pal-asset-audit-validation.md`
- `release/integration-notes/r100b-official-pal-metadata-upgrade-batch-plan.md`
- `release/integration-notes/r100b-official-pal-safe-index-file-plan.md`
- `release/integration-notes/r100b-official-pal-asset-manifest-preview-plan.md`
- `evals/palbench/pal-asset/r100d-pal-metadata-upgrade-compatibility-gate.md`
- `release/integration-notes/r101-official-pal-upgrade-gate-freeze.md`

## Audit Result

The 9 official Pal Packs were audited against the v0.5 Pal Asset Standard
direction.

R98-B did not modify `official/pals/**`, did not modify the central roster, and
did not upgrade any specific Pal.

Current evidence:

- official Pal directories: 9
- central registered / active Pals: 9 / 9
- root entry files present: 45 / 45
- official `pal.json` parse failures: 0
- `asset-manifest.json` files present: 0

## Main Upgrade Gaps

- all 9 Pals need future v0.5 `pal.json` asset metadata after fields are settled
- all 9 Pals need future `asset-manifest.json` after manifest schema approval
- several Pals need public-safe memory index files
- PalSmith needs a decision on `memory/` and `learning/` applicability
- Mira and PalSmith contain older `.agentpal/` wording that should be reviewed
  against the central project-record and thin-binding boundary

## Suggested Phases

| Phase | Goal |
| --- | --- |
| Completed preparation | R98 audit, R100 metadata/schema/template/gate preparation, and R101 navigation freeze. |
| Next candidate | Minimal safe index / README additions for a small approved Pal batch. |
| Later metadata batch | `pal.json` v0.5 metadata update after gate baseline passes. |
| Later manifest batch | `asset-manifest.json` generation after metadata, index coverage, and schema checks pass. |
| Later review batch | PalSmith-driven bounded audit integration without creating a scanner. |

## R101 Preflight Gate

Before future edits under `official/pals/**`, run the frozen R101 preflight:

1. capture `git status --short --branch`;
2. parse the central roster and verify 10 active official Pals;
3. parse all official Pal `pal.json` files;
4. verify official Pal directory count is 10;
5. verify no central roster diff;
6. verify no route maps, scanner / connector behavior, or credential-like
   values are introduced;
7. run the R100-D compatibility gate before and after the small batch;
8. record missing and not-run evidence honestly.

The next public-safe candidate is an index/README backfill batch, not
`pal.json` metadata and not real `asset-manifest.json` generation.

## Compatibility Rule

Official Pal upgrades must preserve backward compatibility:

- do not rename or move existing assets without a compatibility note
- do not break central roster ids, aliases, direct calls, or pack paths
- preserve missing and not-run evidence
- do not claim job readiness from directory existence alone
- keep Pal Skill and Agent Skill boundaries explicit

## Boundary

This guide is a plan summary. It does not authorize direct edits to official
Pals, central contacts, remote Git state, tags, releases, or external project
`.agentpal/` directories.
