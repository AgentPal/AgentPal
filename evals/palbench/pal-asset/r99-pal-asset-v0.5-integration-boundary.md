# R99 Pal Asset v0.5 Integration Boundary Eval

Date: 2026-06-28

## Purpose

Verify that R99 integrates the R98-A/B/C/D Pal Asset foundation into shared
navigation without changing runtime boundaries, central roster, or official Pal
assets.

## Files Under Test

Shared entries:

- `README.md`
- `README.zh-CN.md`
- `RESOURCE_INDEX.md`
- `agentpal.json`
- `docs/09-roadmap/v0.5-local-development-scope.md`

R99 docs:

- `docs/00-overview/pal-asset-and-org-pack-relationship.md`
- `docs/03-user-guides/palsmith-v0.5-pal-creation-and-upgrade.md`
- `docs/03-user-guides/official-pal-asset-upgrade-plan.md`

R99 evidence:

- `release/fresh-clone-checks/r99-r98-parallel-integration-validation.md`

## Required Integration Assertions

| Assertion | Expected |
| --- | --- |
| R98-A Pal Asset Standard assets exist | pass |
| R98-B official Pal audit assets exist | pass |
| R98-C PalSmith v0.5 standards and templates exist | pass |
| R98-D Pal loading order / resolver standards and example exist | pass |
| README points to v0.5 Pal Asset / Org Pack navigation | pass |
| README.zh-CN points to v0.5 Pal Asset / Org Pack navigation | pass |
| RESOURCE_INDEX has Pal Asset Standards section | pass |
| RESOURCE_INDEX has PalSmith v0.5 section | pass |
| RESOURCE_INDEX has Official Pal Asset Audit section | pass |
| RESOURCE_INDEX has Pal Asset / Org Pack Integration section | pass |
| `agentpal.json` parses | pass |
| `agentpal.json` contains Pal Asset key paths and false boundary flags | pass |
| `agentpal.json` contains PalSmith key paths and false boundary flags | pass |

## Boundary Assertions

R99 must preserve:

- central roster unchanged
- official Pal directories count remains 9
- no direct `official/pals/**` edits
- no keyword routing
- no deterministic semantic routing
- no external project thick binding
- no connector, scanner, marketplace, installer, daemon, database, auto sync, or
  auto execution program
- no credential, token, password, API key, cookie, or secret leak
- Pal Skill remains distinct from Agent Skill
- Pal Asset Resolver remains a no-code standard, not runtime code
- PalSmith remains a no-code asset creator/governor, not an automatic executor

## Negative Cases

Fail if R99 introduces:

- `keyword_map`, `domain_map`, or `role_map`
- direct mappings such as development to Atlas, testing to Quinn, writing to
  Harper, Org Pack type to Pal, or Pal Skill to route
- external project `.agentpal/pals/`, `.agentpal/skills/`,
  `.agentpal/workflows/`, `.agentpal/runbooks/`, `.agentpal/memory/`,
  `.agentpal/reports/`, `.agentpal/capability-inventory/`,
  `.agentpal/business-systems/`, `.agentpal/org-pack/`, or
  `.agentpal/pal-asset/` as required default writes
- connector or API client implementation claims
- scanner, validator, installer, marketplace, hub, daemon, database, auto sync,
  or auto execution implementation claims
- central roster modification
- official Pal asset upgrade execution

## Pass Condition

Pass only when all R98 assets are present, shared navigation points to them,
validation passes, and forbidden behavior appears only as boundary, eval,
template, example, or archive wording.
