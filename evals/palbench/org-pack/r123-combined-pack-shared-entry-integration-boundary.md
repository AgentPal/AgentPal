# R123 Combined Pack Shared Entry Integration Boundary Eval

## Purpose

This PalBench eval checks that R123 integrates the approved combined Org Pack +
FDE Pack example into shared entries without expanding AgentPal into a runtime,
connector, scanner, validator, marketplace, installer, credential store,
keyword router, or external project payload copier.

## Scope

In scope:

- `README.md`
- `README.zh-CN.md`
- `RESOURCE_INDEX.md`
- `agentpal.json`
- `docs/00-overview/org-pack-fde-asset-boundary-overview.md`
- R123 pre-gate, validation, and R124 readiness records.

Out of scope:

- GitHub push, pull, fetch, tag, or Release.
- Official Pal metadata rollout.
- Central roster modification.
- External project `.agentpal/` asset writes.
- Marketplace, connector, scanner, validator, installer, daemon, database,
  auto-sync, auto-discovery, auto-execution, or keyword-routing behavior.

## Required Checks

### 1. Shared Entries Mention The Combined Example

Pass when:

- `README.md` mentions the combined Org/FDE example;
- `README.zh-CN.md` mentions the combined Org/FDE example;
- `RESOURCE_INDEX.md` includes a Combined Pack Examples section;
- `docs/00-overview/org-pack-fde-asset-boundary-overview.md` includes the
  combined example.

### 2. `agentpal.json` Includes The Combined Example

Pass when `agentpal.json` parses and contains `combined_packs` metadata for
`content_ops_with_accounting_advisor` with safe false boundary fields.

### 3. R122 Review Status Retained

Pass when shared entries retain the R122 review status:
`approved_for_r123_integration_with_human_review_retained`.

### 4. Combined Example Still Valid

Pass when `combined-pack.json` parses, `org_pack_ref` exists, and all
`fde_pack_refs` exist.

### 5. No Private Or Credential Leak

Pass when R123 changed files contain no real credentials, tokens, customer data,
private project context, private meeting content, screenshots, or reversible
identifying clues.

### 6. No Behavior Expansion

Pass when R123 does not add connector, scanner, validator, installer, daemon,
database, marketplace, hub, credential-store, auto-sync, auto-discovery,
auto-execution, or active keyword-routing behavior.

### 7. Central Roster And Official Pal Unchanged

Pass when central contacts remain `9 / 9`, `routing_policy=ai_judgement_only`,
`keyword_routing_allowed=false`, official Pal dirs remain `9`, all official Pal
`pal.json` files parse, only PalSmith has `asset-manifest.json`, and protected
diffs are empty.

## Expected Result

Expected result for R123: `pass`.

Any missing evidence must be reported as `missing`, `not-run`, or `blocked`.
