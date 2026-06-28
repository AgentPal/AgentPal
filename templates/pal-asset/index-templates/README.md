# Pal Asset Index Templates

Date: 2026-06-28

## Purpose

This package provides reusable public-safe `index.md` / `README.md` templates for Pal asset directories.

Use these templates when a Pal directory exists but needs a lightweight navigation file before deeper v0.5 upgrades. The templates improve discoverability without changing Pal behavior, moving content, generating manifests, or modifying `pal.json`.

## Templates

- `skills-index-template.md`
- `workflows-index-template.md`
- `runbooks-index-template.md`
- `knowledge-index-template.md`
- `memory-index-template.md`
- `learning-index-template.md`
- `evals-index-template.md`
- `examples-index-template.md`
- `research-index-template.md`

## Use Rules

1. Copy the relevant template into the target Pal asset directory as `index.md` or `README.md`.
2. Replace bracketed placeholders with public-safe directory-specific notes.
3. List only assets that are actually present under `Current assets`.
4. Put possible future additions under `Candidate assets`.
5. Mark uncertain items as `unknown` or `needs-review`.
6. Do not move, delete, rename, or reclassify existing assets during an index-only backfill.
7. Do not edit `pal.json`, central contacts, registry, or external project `.agentpal/` from this template package.

## Related Standards

- `standards/pal-asset/pal-asset-standard.md`
- `standards/pal-asset/pal-asset-directory-standard.md`
- `standards/pal-asset/pal-skill-vs-agent-skill-standard.md`
- `templates/pal-asset/safe-index-backfill-guide.md`

## Public Safety Boundary

These templates are public-safe shells. Do not include credentials, tokens, secrets, private user memory, private project memory, customer identifiers, private evidence, or current runtime state in a public index.

## External Project Boundary

Pal asset indexes belong in Pal Packs inside the AgentPal central workspace or an approved central organization record. They must not be written into an external project's `.agentpal/` directory by default.
