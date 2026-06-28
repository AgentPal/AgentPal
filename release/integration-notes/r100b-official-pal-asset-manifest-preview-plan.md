# R100-B Official Pal Asset Manifest Preview Plan

Date: 2026-06-28

Scope: define how a future thread can generate `asset-manifest.json` for official Pals. This is a preview plan only. R100-B does not generate actual manifests under `official/pals/**`.

## Manifest Status

Current status from R98-B and R100-B preflight:

- official Pal count: 9
- existing `asset-manifest.json` files under official Pals: 0
- all official root entries complete: yes
- all official `pal.json` parse: yes
- manifest readiness: preview-ready after schema approval for all 9 Pals

Current manifest schema and template evidence is present in the worktree and was read by R100-B. R100-B does not submit those R100-A / R100-C files, but the preview plan is aligned to them:

- standard: `standards/pal-asset/asset-manifest-standard.md`
- schema: `standards/schemas/pal-asset-manifest.schema.json`
- template: `templates/pal-asset/asset-manifest-template.json`
- related root-entry standard: `standards/pal-asset/pal-root-entry-standard.md`
- related loading-order standard: `standards/pal-asset/pal-loading-order-standard.md`

## Field Sources

| Manifest field | Source | Notes |
| --- | --- | --- |
| `schema` | `standards/schemas/pal-asset-manifest.schema.json` | Use `agentpal.pal-asset-manifest.v0.5` when schema is integrated. |
| `asset_standard` | `standards/pal-asset/pal-asset-standard.md` | Expected value can reference `agentpal-pal-asset-standard.v0.5`. |
| `pal_id` | `pal.json.id` | Must match central roster `id`. |
| `display_name` | central roster and `pal.json.display_name` / `name` | Mismatches require review. |
| `manifest_version` | manifest standard / template | Start from the approved template version. |
| `generated_at` | generation run evidence | Use `not-run` in templates; real generation must record date or timestamp. |
| `generated_by` | generation run evidence | Human, Pal, or runtime evidence source. |
| `asset_root` | central roster `pack_path` | Must point under `official/pals/`. |
| `root_entries` | root file existence | `README.md`, `PAL.md`, `pal.json`, `AGENTS.md`, `SKILL.md`. |
| `assets` | directory scan plus index files | Group by identity, core, knowledge, research, skills, workflows, runbooks, learning, memory, state, reports, evals, examples. |
| asset entry `status` | schema status enum | Use `present`, `missing`, `partial`, `deprecated`, `not-applicable`, or `not-run`. |
| `public_safety` | focused search + policy | Record no credentials, no private memory, no copied external project data. |
| `skill_boundary` | Pal Skill vs Agent Skill standard | Pal `skills/` are Pal-owned work capabilities, not runtime Agent Skills. |
| `runtime_boundary` | `AGENTS.md`, `SKILL.md`, standards | No execution claim without host Runtime evidence. |
| `known_gaps` | R98-B / R100-B gap tables | Preserve missing index, metadata, and manifest gaps. |
| `not_run_checks` | manifest generation run | Record checks not executed. |
| `requires_human_review` | R100-B plans | True for metadata, manifest schema, stale `.agentpal/` wording, and misplaced asset risks. |

## Preview Shape

```json
{
  "schema": "agentpal.pal-asset-manifest.v0.5",
  "asset_standard": "agentpal-pal-asset-standard.v0.5",
  "pal_id": "REPLACE_WITH_PAL_ID",
  "display_name": "REPLACE_WITH_DISPLAY_NAME",
  "manifest_version": "0.5.0",
  "generated_at": "not-run",
  "generated_by": "planned",
  "asset_root": "official/pals/REPLACE_WITH_DIRECTORY",
  "root_entries": {
    "README.md": "present",
    "PAL.md": "present",
    "pal.json": "present",
    "AGENTS.md": "present",
    "SKILL.md": "present"
  },
  "assets": {
    "identity": [],
    "core": [],
    "knowledge": [],
    "research": [],
    "skills": [],
    "workflows": [],
    "runbooks": [],
    "learning": [],
    "memory": [],
    "state": [],
    "reports": [],
    "evals": [],
    "examples": []
  },
  "public_safety": {
    "credentials": "not_found",
    "private_project_memory": "not_found",
    "external_project_data": "not_found",
    "route_maps": "not_found"
  },
  "known_gaps": [],
  "not_run_checks": [],
  "requires_human_review": true
}
```

## Per-Pal Manifest Readiness

| pal_id | display_name | readiness | missing preconditions |
| --- | --- | --- | --- |
| mira-main | Mira | preview-ready-after-schema | needs research index review; stale `.agentpal/` boundary review |
| atlas-developer | Atlas | preview-ready-after-schema | memory index; research index review; imported Skill-card classification |
| nova-product | Nova | preview-ready-after-schema | memory index; research index review |
| vega-research | Vega | preview-ready-after-schema | memory index; research index review; research-to-knowledge boundary |
| quinn-quality | Quinn | preview-ready-after-schema | memory index; research index review |
| morgan-document | Morgan | preview-ready-after-schema | memory index; research index review |
| harper-writing | Harper | preview-ready-after-schema | memory index; research index review |
| rhea-system | Rhea | preview-ready-after-schema | memory index; research index review; state/memory boundary review |
| palsmith-pal-governor | PalSmith | preview-ready-after-schema | runbooks index; memory/learning policy decision; research index review; staging wording review |

## Manifest Forbidden Content

Future manifests must not contain:

- credentials
- tokens
- secrets
- private keys
- cookies
- API keys
- private project memory
- copied external project `.agentpal/` data
- runtime state contents
- private reports
- `keyword_map`
- `domain_map`
- `role_map`
- deterministic owner-selection logic
- claims that a Runtime Skill, plugin, MCP server, or external business system was available unless current evidence exists

## Validation For Future Generation

Future manifest generation should validate:

- official Pal dirs count = 9
- all central roster `pack_path` values resolve
- all `pal.json` parse
- no central roster modification
- no external project writes
- no credential-like values
- no route maps
- `git diff -- official/pals` contains only approved manifest files and any separately approved index/README files

## R100-B Non-Goals

R100-B does not generate `asset-manifest.json` and does not modify official Pal assets. It treats the current manifest standard / schema / template as planning evidence for a later generation round.
