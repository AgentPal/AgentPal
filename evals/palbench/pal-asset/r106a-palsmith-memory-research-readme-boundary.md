# R106-A PalSmith Memory / Research README Boundary

Date: 2026-06-28

## Purpose

This eval checks that R106-A backfills PalSmith `memory/README.md` and
`research/README.md` without changing PalSmith behavior, central contacts,
official Pal metadata, manifests, or external project thin-binding boundaries.

## Pass Criteria

- PalSmith is resolved from `workspace/organization/contacts/pals.json`.
- PalSmith `pack_path` is `official/pals/PalSmith-pal-governor`.
- PalSmith root entries are present: `README.md`, `PAL.md`, `AGENTS.md`,
  `SKILL.md`, and `pal.json`.
- PalSmith `pal.json` parses and remains unchanged.
- `official/pals/PalSmith-pal-governor/memory/README.md` exists.
- PalSmith memory README states:
  - memory stores extracted long-term lessons about Pal creation, Pal upgrade,
    asset classification, and Pal governance;
  - memory is not full task reports;
  - reports belong in `reports/`;
  - research drafts belong in `research/`;
  - candidate asset ideas belong in `learning/` or `needs-review`;
  - credentials, tokens, cookies, passwords, API keys, secrets, and private
    customer data are forbidden;
  - deterministic routing maps are forbidden;
  - PalSmith memory must not be written into external project `.agentpal/` by
    default;
  - PalSmith memory can suggest improvements but cannot automatically rewrite
    central roster or official Pal assets.
- `official/pals/PalSmith-pal-governor/research/README.md` exists.
- PalSmith research README states:
  - research stores source materials, investigations, design notes,
    comparisons, and unverified findings about Pal creation and governance;
  - stable conclusions require review before promotion to knowledge, standards,
    templates, runbooks, workflows, skills, evals, or memory;
  - research is not memory;
  - research is not stable knowledge;
  - research is not connector implementation or runtime execution;
  - credentials, tokens, cookies, passwords, API keys, secrets, and customer
    secrets are forbidden;
  - research must not be copied into external project `.agentpal/` by default.
- Central roster parses and remains 9 registered / 9 active Pals.
- Official Pal directory count remains 9.
- All official Pal `pal.json` files parse.
- No central contacts file changes.
- No official Pal `pal.json` file changes.
- No official `asset-manifest.json` is generated or modified by the R106-A
  diff.
- No report body is copied into memory.
- No research source body is promoted directly into knowledge or memory.
- No keyword, domain, role, or deterministic routing map is introduced.
- No connector, scanner, validator program, daemon, installer, marketplace,
  hub, auto-sync, or auto-execution behavior is introduced.
- No credential, token, cookie, password, API key, secret, private project data,
  private user memory, or customer data is introduced.
- No external project `.agentpal/` thick-binding directory is created or
  modified.
- Clean-copy validation passes.

## Fail Conditions

- PalSmith cannot be resolved from the central roster.
- PalSmith memory README is missing.
- PalSmith research README or index is missing.
- Any official Pal `pal.json` changes.
- Central contacts change.
- A real `asset-manifest.json` is newly generated, modified, deleted, or made
  part of the R106-A diff.
- README files claim runtime execution, automatic routing, connector behavior,
  scanning, validation, or external system behavior.
- README files require copying PalSmith assets into external project
  `.agentpal/` directories by default.
- README files contain private data, credentials, or deterministic Pal routes.
- R106-A moves, deletes, renames, or reclassifies existing PalSmith assets.

## Required Evidence

Record evidence in:

- `release/integration-notes/r106a-palsmith-memory-research-readme-summary.md`
- `release/fresh-clone-checks/r106a-local-palsmith-memory-research-readme-validation.md`
