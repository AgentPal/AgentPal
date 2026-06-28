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
| R99 or later | Minimal safe index / README additions when explicitly allowed. |
| R100 | `pal.json` v0.5 metadata update after schema fields are approved. |
| R101 | `asset-manifest.json` generation after manifest schema approval. |
| R102 | PalSmith-driven bounded audit integration without creating a scanner. |

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
