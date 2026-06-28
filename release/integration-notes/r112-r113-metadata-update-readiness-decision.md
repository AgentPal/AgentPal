# R112 R113 Metadata Update Readiness Decision

Date: 2026-06-28

## Decision

Decision: `ready_for_one_pal_real_metadata_update`

Recommended first Pal: `palsmith-pal-governor`

## Rationale

PalSmith is the safest first real metadata update candidate because:

- current `pal.json` already contains `name`;
- current root entries strongly state no-code governance and Runtime Task Package boundaries;
- proposed v0.5 overlay has clear false defaults for routing, external project writes, runtime execution, and credential storage;
- proposed JSON parses;
- the proposal keeps central roster edits as proposals only.

Mira remains a valid second candidate, but should receive a focused human review of Main Pal role wording and legacy runtime-awareness wording before a real write.

## R113 Allowed Scope

R113 may, if explicitly approved:

- update only the selected Pal `pal.json`;
- start with PalSmith only;
- keep the update metadata-only;
- rerun R100-D and R110 gates before and after the edit;
- rerun selected R95 groups if public loading, roster, no-routing, official Pal integrity, or public-safety surfaces are affected;
- produce a postflight validation and clean-copy record;
- avoid push, pull, fetch, tag, or release.

## R113 Forbidden Scope

R113 must not:

- generate real official Pal `asset-manifest.json`;
- update all 9 official Pals;
- modify central roster files;
- copy Pal assets into external projects;
- add deterministic routing maps;
- add connector, scanner, installer, daemon, marketplace, hub, or auto-execution behavior;
- store credentials or private memory in metadata;
- publish, tag, push, or create a GitHub Release.

## Not Ready Items Before Mira Real Update

Before Mira receives a real metadata update:

- review `name` inference from `display_name`;
- review Main Pal / Leader Pal / Conductor wording;
- convert legacy runtime-awareness wording into no-code, evidence-required wording;
- prune the large capability list into public-safe metadata labels.

