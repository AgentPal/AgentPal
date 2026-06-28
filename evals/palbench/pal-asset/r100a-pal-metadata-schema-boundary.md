# R100-A Pal Metadata Schema Boundary Eval

Date: 2026-06-28

## Purpose

Verify that R100-A adds v0.5 `pal.json` and `asset-manifest.json` standards,
schemas, and templates without modifying official Pal assets, central roster, or
shared entry files.

## Files Under Test

| Artifact | Path | Expected |
| --- | --- | --- |
| pal.json v0.5 standard | `standards/pal-asset/pal-json-v0.5-standard.md` | exists |
| asset manifest standard | `standards/pal-asset/asset-manifest-standard.md` | exists |
| Pal schema | `standards/schemas/pal.schema.json` | exists and parses |
| Pal asset manifest schema | `standards/schemas/pal-asset-manifest.schema.json` | exists and parses |
| Pal JSON template | `templates/pal-asset/pal-json-template.json` | exists and parses |
| asset manifest template | `templates/pal-asset/asset-manifest-template.json` | exists and parses |
| R100-A validation | `release/fresh-clone-checks/r100a-local-pal-metadata-schema-validation.md` | exists after validation |
| R100-A index note | `release/integration-notes/r100a-index-update-notes.md` | exists |

## Required Checks

| Check | Expected |
| --- | --- |
| Pal JSON standard defines required v0.5 fields | pass |
| Pal JSON standard says `pal.json` is metadata, not knowledge or logs | pass |
| Pal JSON standard says no credentials or private data | pass |
| Pal JSON standard says no route maps | pass |
| Asset manifest standard says manifest is index, not asset content | pass |
| Asset manifest standard supports graceful fallback if absent | pass |
| Asset manifest standard defines identity/core/knowledge/research/skills/workflows/runbooks/learning/memory/state/reports/evals/examples groups | pass |
| Asset manifest standard defines id/type/path/status/summary/owner/last_reviewed/promotion_source/verification_ref entry fields | pass |
| Templates do not include `keyword_map`, `domain_map`, or `role_map` | pass |
| Templates default keyword routing to false | pass |
| Templates do not allow credentials | pass |
| Templates default external project write to false | pass |
| No official Pal modified | pass |
| Central roster unchanged | pass |

## Negative Cases

Fail if R100-A:

- modifies `official/pals/**`
- modifies `workspace/organization/contacts/pals.json`
- modifies `README.md`, `RESOURCE_INDEX.md`, or `agentpal.json`
- adds `keyword_map`, `domain_map`, or `role_map` to templates
- allows credentials by default
- allows external project writes by default
- treats Agent Skill refs as copied Pal Skills
- makes `asset-manifest.json` a scanner, validator, or runtime executor
- claims remote Git publication, tag, or GitHub Release work

## Expected Verdict

Pass when all target files exist, JSON files parse, templates preserve false
boundary defaults, official Pal assets remain untouched, central roster remains
9/9, and validation records no remote actions.
