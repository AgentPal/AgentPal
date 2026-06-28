# R100-B Official Pal Metadata Preflight Eval

Date: 2026-06-28

Purpose: verify that R100-B produced official Pal metadata upgrade preparation artifacts while preserving R100-B boundaries.

## Required Artifacts

| Check | Expected |
| --- | --- |
| Batch plan exists | `release/integration-notes/r100b-official-pal-metadata-upgrade-batch-plan.md` |
| Safe index file plan exists | `release/integration-notes/r100b-official-pal-safe-index-file-plan.md` |
| Asset manifest preview plan exists | `release/integration-notes/r100b-official-pal-asset-manifest-preview-plan.md` |
| Eval exists | `evals/palbench/pal-asset/r100b-official-pal-metadata-preflight.md` |
| Validation exists | `release/fresh-clone-checks/r100b-local-official-pal-metadata-preflight-validation.md` |

## Coverage Assertions

1. Plans cover exactly 9 official Pals: Mira, Atlas, Nova, Vega, Quinn, Morgan, Harper, Rhea, and PalSmith.
2. Plans use `workspace/organization/contacts/pals.json` and `official/pals/` as evidence.
3. Plans do not modify `official/pals/**`.
4. Plans do not modify `workspace/organization/contacts/pals.json`.
5. Plans do not modify `README.md`, `RESOURCE_INDEX.md`, or `agentpal.json`.
6. Safe auto-fix candidates include only public-safe index/README/metadata documentation plans.
7. Risky changes are marked as requiring human review.
8. `pal.json` v0.5 metadata is planned, not applied.
9. `asset-manifest.json` generation is planned, not applied.
10. Misplaced asset review is separated from safe index/README additions.

## Required Preflight Checks

| Check | Expected Result |
| --- | --- |
| Official Pal dirs count | 9 |
| Central roster parse | pass |
| Official `pal.json` parse | 9 pass / 0 fail |
| `git diff -- official/pals` | no diff |
| `keyword_map|domain_map|role_map` under official Pals | no hits |
| Focused credential-like assignment search | no hits |

## Boundary Assertions

R100-B must not:

- run `git push`, `git pull`, or `git fetch`
- create or modify tags
- create or modify GitHub Releases
- modify `official/pals/**`
- modify central contacts
- modify shared entry files
- add scanners, validators, daemons, connectors, API clients, marketplace or hub programs, auto sync, or auto execution
- probe Runtime / Skill / plugin / MCP / business systems automatically
- write into external project `.agentpal/`
- add keyword routing, deterministic semantic routing, `keyword_map`, `domain_map`, or `role_map`
- add credentials, tokens, secrets, customer data, or private project memory

## Pass Condition

Pass when all required artifacts exist, all 9 official Pals are covered, no protected files are modified, safe auto-fix candidates remain documentation-only, and risky changes are explicitly marked for human review.

