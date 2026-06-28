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

## Boundary

These standards are Markdown / JSON / protocol documentation. They do not add a
runtime, scanner, connector, installer, daemon, marketplace, API client, or
automatic dispatch system.
