# Minimal Pal Generation Checklist

Use this checklist when PalSmith prepares a Minimal Pal creation or upgrade package.

## Target

- target Pal name:
- target human display name:
- role title:
- contact label:
- canonical id:
- user custom name:
- target Pal id:
- target path:
- intended users:
- privacy / publication status:
- Runtime evidence source:

## Required Root Files

| File | Status | Evidence / note |
| --- | --- | --- |
| `README.md` | missing | |
| `PAL.md` | missing | |
| `pal.json` | missing | |
| `AGENTS.md` | missing | |
| `SKILL.md` | missing | |

## Required Identity Files

| File | Status | Evidence / note |
| --- | --- | --- |
| `identity/persona.md` | missing | |
| `identity/voice.md` | missing | |

## Required Core Files

| File | Status | Evidence / note |
| --- | --- | --- |
| `core/task-loop.md` | missing | |
| `core/dispatch-protocol.md` | missing | |
| `core/verification-protocol.md` | missing | |
| `core/memory-protocol.md` | missing | |

## Required Indexes And Support Files

| File | Status | Evidence / note |
| --- | --- | --- |
| `knowledge/index.md` | missing | |
| `skills/index.md` | missing | |
| `workflows/index.md` | missing | |
| `runbooks/index.md` | missing | |
| `memory/index.md` | missing | |
| `evals/definition-of-done.md` | missing | |
| `reports/README.md` | missing | |
| `state/README.md` | missing | |
| Contact Capability Card placeholder or complete card | missing | |
| Pal Asset Preflight template or inheritance note | missing | |

## Boundary Checks

| Check | Status | Evidence / note |
| --- | --- | --- |
| display name is a human name, not role-only label | not-run | |
| role title is separate from display name | not-run | |
| `canonical_id` is stable and unique | not-run | |
| `contact_label` distinguishes role / conflict context | not-run | |
| aliases preserve historical names | not-run | |
| naming conflict check completed | not-run | |
| `pal.json` parses | not-run | |
| `completeness_level` uses allowed enum | not-run | Allowed: `persona_only`, `persona_plus_voice`, `role_plus_knowledge`, `role_plus_workflow`, `executable_pal`, `verified_pal`. |
| Pal Runtime Read Order present | not-run | |
| Asset Path Map present | not-run | |
| Task Asset Packet rule present | not-run | |
| Asset Use Summary rule present | not-run | |
| Missing Asset Plan rule present | not-run | |
| No Blind Tool Call Rule present | not-run | |
| `tool_vs_pal_asset_boundary` present | not-run | |
| no Agent Skill stored in Pal `skills/` | not-run | |
| no keyword routing map | not-run | |
| no credentials / tokens / secrets | not-run | |
| no private memory in public assets | not-run | |
| no write into external project `.agentpal/` by default | not-run | |
| no workflow / runbook / knowledge / report / memory mixing | not-run | |

## Decision

Use one:

- `pass`
- `partial`
- `missing`
- `not-run`
- `blocked`

Decision:

Required fixes:

Next Runtime Task Package:
