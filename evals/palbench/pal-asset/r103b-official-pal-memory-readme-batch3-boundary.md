# R103-B Official Pal Memory README Batch 3 Boundary

Date: 2026-06-28

## Purpose

This eval checks that the Harper / Rhea memory README Batch 3 adds only safe
memory README files and does not expand official Pal behavior.

## Pass Criteria

- Harper and Rhea paths are resolved from central roster.
- `official/pals/Harper-writing/memory/README.md` exists.
- `official/pals/Rhea-system/memory/README.md` exists.
- The added README files include:
  - Purpose
  - What belongs here
  - What does not belong here
  - Current assets
  - Candidate memories / needs review
  - Relationship to reports
  - Project-private memory boundary
  - Related standards
  - Public safety boundary
  - External project boundary
- Harper and Rhea root entries still exist.
- Harper and Rhea `pal.json` files still parse.
- Central roster still parses.
- Central registered / active Pals remain 9 / 9.
- Official Pal directory count remains 9.
- No official Pal `pal.json` changes.
- No real official `asset-manifest.json` files are generated.
- No existing official Pal assets are moved, deleted, renamed, or rewritten.
- No keyword, domain, role, or deterministic route map is introduced.
- No scanner, validator program, daemon, connector, installer, marketplace, hub,
  auto-sync, or auto-execution behavior is introduced.
- No credentials, tokens, cookies, passwords, API keys, secrets, customer data,
  private project data, or private memory are introduced.
- No external project `.agentpal/` thick binding is introduced.
- Local clean-copy check passes.

## Fail Conditions

- Any `pal.json` file changes.
- Any `asset-manifest.json` file appears under `official/pals/**`.
- Central contacts change.
- Added README files claim runtime execution, routing behavior, or external
  project asset copying.
- Added files contain real credentials or private project data.

## Required Evidence

Record evidence in:

- `release/fresh-clone-checks/r103b-local-official-pal-memory-readme-batch3-validation.md`
- `release/integration-notes/r103b-official-pal-memory-readme-batch3-summary.md`
