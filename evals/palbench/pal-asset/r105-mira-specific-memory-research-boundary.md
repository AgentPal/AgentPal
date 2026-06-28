# R105 Mira-Specific Memory / Research Boundary

Date: 2026-06-28

## Purpose

This eval checks that R105 backfills Mira `memory/` and `research/` indexes
without changing Mira behavior, central contacts, official Pal manifests, or
external project thin-binding boundaries.

## Pass Criteria

- Mira is resolved from `workspace/organization/contacts/pals.json`.
- Mira `pack_path` is `official/pals/Mira-main`.
- Mira root entries are present: `README.md`, `PAL.md`, `AGENTS.md`,
  `SKILL.md`, and `pal.json`.
- Mira `pal.json` parses and remains unchanged.
- `official/pals/Mira-main/memory/README.md` exists.
- Mira memory README states:
  - memory stores extracted long-term lessons and user / Mira coordination
    preferences;
  - full reports belong in `reports/`;
  - project-private memory belongs in central project records by default;
  - research dumps belong in `research/`;
  - credentials, tokens, cookies, passwords, API keys, and secrets are
    forbidden;
  - keyword routing maps and deterministic dispatch rules are forbidden;
  - external project `.agentpal/memory/` is not a default target.
- `official/pals/Mira-main/research/README.md` exists.
- Mira research README states:
  - research stores source materials, investigations, and unverified findings;
  - stable conclusions require review before promotion;
  - research is not memory, stable knowledge, connector implementation, or
    runtime execution;
  - credentials, tokens, cookies, passwords, API keys, and secrets are
    forbidden;
  - external project `.agentpal/research/` is not a default target.
- Central roster parses and remains 9 registered / 9 active Pals.
- Official Pal directory count remains 9.
- All official Pal `pal.json` files parse.
- No central contacts file changes.
- No official Pal `pal.json` file changes.
- No official `asset-manifest.json` is generated.
- No report body is copied into memory.
- No research source body is promoted directly into knowledge or memory.
- No keyword, domain, role, or deterministic routing map is introduced.
- No credential, token, cookie, password, API key, secret, private project data,
  private user memory, or customer data is introduced.
- No external project `.agentpal/` thick-binding directory is created or
  modified.
- Clean-copy validation passes.

## Fail Conditions

- Mira cannot be resolved from the central roster.
- Any official Pal `pal.json` changes.
- Central contacts change.
- A real `asset-manifest.json` appears under `official/pals/**`.
- The README files claim runtime execution, automatic routing, connector
  behavior, scanning, validation, or external system behavior.
- The README files require copying Mira assets into external project
  `.agentpal/` directories by default.
- The README files contain private data, credentials, or deterministic Pal
  routes.
- R105 moves, deletes, renames, or reclassifies existing Mira assets.

## Required Evidence

Record evidence in:

- `release/integration-notes/r105-mira-specific-pal-asset-review.md`
- `release/fresh-clone-checks/r105-local-mira-specific-memory-research-validation.md`
