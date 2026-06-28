# R100-A Local Pal Metadata Schema Validation

Date: 2026-06-28

## Scope

This validation records the local R100-A evidence for v0.5 `pal.json` field
standard, `asset-manifest.json` standard, JSON schemas, templates, eval, and
integration note.

This is a local Markdown / JSON / schema / template governance pass. It is not
GitHub sync, not a tag, and not a GitHub Release.

## Files

| File | Result |
| --- | --- |
| `standards/pal-asset/pal-json-v0.5-standard.md` | pass |
| `standards/pal-asset/asset-manifest-standard.md` | pass |
| `standards/schemas/pal.schema.json` | pass |
| `standards/schemas/pal-asset-manifest.schema.json` | pass |
| `templates/pal-asset/pal-json-template.json` | pass |
| `templates/pal-asset/asset-manifest-template.json` | pass |
| `evals/palbench/pal-asset/r100a-pal-metadata-schema-boundary.md` | pass |
| `release/integration-notes/r100a-index-update-notes.md` | pass |

## JSON Parse

| Check | Result |
| --- | --- |
| visible `.json` files parsed | 89 |
| visible JSON parse failures | 0 |
| `standards/schemas/pal.schema.json` parse | pass |
| `standards/schemas/pal-asset-manifest.schema.json` parse | pass |
| `templates/pal-asset/pal-json-template.json` parse | pass |
| `templates/pal-asset/asset-manifest-template.json` parse | pass |

JSON Schema semantic validation with Python `jsonschema` was attempted but not
run because the local Python environment does not have `jsonschema` installed.
This validation therefore claims parse success, not full schema-validator
execution.

## Template Defaults

| Default | Result |
| --- | --- |
| Pal template keyword routing allowed | `false` |
| Pal template external project write allowed by default | `false` |
| Pal template credentials allowed | `false` |
| Asset manifest template keyword routing allowed | `false` |
| Asset manifest template external project write allowed by default | `false` |
| Asset manifest template credentials allowed | `false` |

## Central Roster And Official Pal Checks

| Check | Result |
| --- | --- |
| central contacts JSON parse | pass |
| registered Pals | 9 |
| active Pals | 9 |
| `routing_policy` | `ai_judgement_only` |
| `keyword_routing_allowed` | `false` |
| official Pal directories | 9 |
| changes under `official/pals/**` | none |
| changes to `workspace/organization/contacts/pals.json` | none |
| changes to `README.md`, `RESOURCE_INDEX.md`, or `agentpal.json` | none |

## Boundary Searches

| Search | Result |
| --- | --- |
| exact route-map JSON declarations in R100-A files | none |
| credential assignment-like values in R100-A files | none |
| internal development-directory string in public repo | none |
| Pal template includes `keyword_map`, `domain_map`, or `role_map` | no |
| asset manifest template includes `keyword_map`, `domain_map`, or `role_map` | no |

R100-A standards and schemas mention route-map field names only as forbidden
fields or schema-level exclusions. Templates do not include them.

## Boundary Confirmation

R100-A did not execute or introduce:

- `git push`
- `git pull`
- `git fetch`
- tag creation or modification
- GitHub Release creation or modification
- release/tag migration
- remote overwrite
- CLI / Web App / Desktop App
- scanner / validator / installer / daemon / database
- auto sync / auto execution engine
- connector / external business system API client
- marketplace / hub program
- keyword router / deterministic semantic router
- automatic Runtime / Skill / plugin / MCP / business system probe
- external project `.agentpal/` write
- central roster modification
- official Pal manifest modification

## Decision

Pass for R100-A local metadata schema foundation.

Residual not-run: semantic JSON Schema validation against templates was not run
because the local `jsonschema` Python package is unavailable.
