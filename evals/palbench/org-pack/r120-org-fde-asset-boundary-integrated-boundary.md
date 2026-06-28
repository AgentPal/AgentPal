# R120 Org / FDE / Asset Boundary Integrated Boundary Eval

## Purpose

This PalBench eval checks that R119-A/B/C/D outputs are integrated into shared
navigation without expanding AgentPal's runtime, routing, external project, or
privacy boundaries.

## Scope

In scope:

- R119-A Org Pack practical structure assets.
- R119-B FDE Pack assets.
- R119-C Asset Boundary assets.
- R119-D integration gate assets.
- R120 overview, summary, validation, and R121 readiness records.
- Shared-entry navigation in `README.md`, `README.zh-CN.md`,
  `RESOURCE_INDEX.md`, `agentpal.json`, and v0.5 scope.

Out of scope:

- official Pal metadata rollout;
- central roster modification;
- external project `.agentpal/` asset writes;
- connector, scanner, validator, installer, daemon, database, marketplace, hub,
  auto-sync, auto-discovery, auto-execution, or keyword-routing programs.

## Required Checks

### 1. R119 Assets Exist

Pass when all R119-A/B/C/D required paths exist.

Fail when any required standard, template, example, eval, validation, checklist,
issue template, or integration plan is missing.

### 2. Shared Entries Point To R119/R120

Pass when:

- `README.md` and `README.zh-CN.md` mention Org Pack, FDE Pack, and Asset
  Boundary navigation.
- `RESOURCE_INDEX.md` contains Org Pack v0.5, FDE / Expert Delivery Pack, Asset
  Boundary, and Org / FDE Integration sections.
- `agentpal.json` contains `org_pack`, `fde_pack`, and `asset_boundary`
  navigation and false safety-boundary fields.

### 3. JSON Parse

Pass when:

- visible tracked `.json` files parse;
- `templates/org-pack/practical-org-pack/org.json` parses;
- `examples/org-packs/content-ops-org-pack/org.json` parses;
- `templates/fde-pack/base-fde-pack/fde.json` parses;
- `examples/fde-packs/accounting-advisor-fde-pack/fde.json` parses;
- `templates/asset-boundary/asset-classification-result-template.json` parses;
- `workspace/organization/contacts/pals.json` parses.

### 4. Central Roster Unchanged

Pass when central contacts still contain 9 registered Pals, 9 active Pals,
`routing_policy=ai_judgement_only`, and `keyword_routing_allowed=false`, with no
diff under `workspace/organization/contacts`.

### 5. Official Pal Unchanged

Pass when official Pal directories remain 9, all official Pal `pal.json` files
parse, no official Pal `pal.json` diff exists, and only PalSmith has
`asset-manifest.json`.

### 6. No Credential Or Customer-private Leak

Pass when R119/R120 public assets contain no real credentials, tokens, customer
data, private project context, private meeting content, or reversible identifying
clues. Fake bad examples must be clearly marked as forbidden examples.

### 7. No Behavior Expansion

Pass when R119/R120 additions do not introduce connector, scanner, validator,
installer, daemon, database, marketplace, hub, auto-sync, auto-discovery,
auto-execution, credential storage, or active keyword routing behavior.

### 8. Thin Binding Preserved

Pass when no active external project path receives `.agentpal/org-pack`,
`.agentpal/fde-pack`, `.agentpal/pals`, `.agentpal/skills`,
`.agentpal/workflows`, `.agentpal/runbooks`, `.agentpal/memory`,
`.agentpal/reports`, `.agentpal/asset-manifest`, or `.agentpal/pal-asset`
directories by default.

## Expected Result

Expected result for R120: `pass`.

Any missing evidence must be reported as `missing`, `not-run`, or `blocked`; it
must not be smoothed into a pass.
