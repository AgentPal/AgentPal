# Pal Asset Standards

Date: 2026-06-28

This directory contains the AgentPal Pal Asset Standard foundation for v0.5.

The standard aligns Pal Packs with the v0.5 Org Pack foundation while keeping
the two asset families separate:

- A Pal Pack defines one long-term working companion in the AgentPal
  organization.
- An Org Pack defines a reusable organization or work-system package.
- External user projects remain thin-bound business sites, not AgentPal asset
  warehouses.

## Files

- `pal-asset-standard.md`: main Pal Asset Standard v0.5.
- `pal-skill-vs-agent-skill-standard.md`: boundary between Pal Skills and
  runtime Agent Skills.
- `pal-asset-directory-standard.md`: directory responsibilities and promotion
  rules.
- `pal-root-entry-standard.md`: root entry file responsibilities.
- `pal-naming-and-import-conflict-protocol.md`: v0.6 Pal human-name,
  role-title, user rename, and same-name import conflict protocol.

## Related v0.6 Preflight Protocols

- `core/pal-asset-preflight-protocol.md`: Pal-level asset preflight before
  substantive work.
- `core/team-asset-preflight-protocol.md`: Team-level asset preflight before
  member Pal work.
- `core/team-pal-asset-priority-protocol.md`: priority rules between user
  instruction, project constraints, Team assets, Pal boundaries, and memory.
- `templates/pal/pal-asset-preflight.md`: Pal preflight evidence template.
- `templates/team/team-asset-preflight.md`: Team preflight evidence template.
- `templates/orchestration/workflow-execution-contract.md`: canonical Workflow
  Execution Contract template used after Team Asset Preflight.
- `orchestration/workflow-closure-gate-protocol.md`: Closure Gate used before
  final reports that claim Workflow completion.

## Boundary

These standards are Markdown / JSON / protocol documentation. They do not add a
runtime, scanner, connector, installer, daemon, marketplace, API client, or
automatic dispatch system.
