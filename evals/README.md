# Evals

These are manual self-test documents for AgentPal.

They are Markdown checklists, not automated tests, scripts, scanners, validators, or runtime dependencies.

## Current Release Check Areas

| Area | Start here |
| --- | --- |
| Simple Pal Mode | `simple-pal-mode/README.md` |
| Runtime guides | `runtime-guides/README.md` |
| Pal Pack validity | `pal-pack-validity/README.md` |
| Public safety | `public-safety/README.md` |
| Release readiness | `release/README.md` |
| Orchestration workflows | `orchestration/` |
| Local fixtures | `fixtures/v0.6-team-pack/README.md` |
| v0.6 Team workflow regression | `team-workflows/v0.6-regression-checklist.md` |
| Session validation | `session-validation/v0.6-mira-palsmith/README.md` |
| Runtime validation | `runtime-validation/v0.6-team-pack/README.md` |
| PalBench Collaboration | `palbench-collaboration/README.md` |

## v0.6 Team Pack Checks

For Team Pack documentation and examples, start with:

- `team-workflows/v0.6-regression-checklist.md`
- `session-validation/v0.6-mira-palsmith/README.md`
- `runtime-validation/v0.6-team-pack/README.md`
- `../release/integration-notes/v0.6-acceptance-matrix.md`

The regression checklist is a manual anti-regression anchor. Session validation
files are conversation scripts and transcript templates. Runtime validation
files are copyable real-host task packages and evidence templates. None of
these should be reported as passed until the target checks, conversations, or
runtime sessions have actually been run.

## Existing Root Checks

Official bundled Pal checks:

- `official-pals-migration-check.md`
- `pal-contacts-boundary-check.md`
- `mira-routing-to-official-pals-self-test.md`

Release readiness checks:

- `release-readiness-check.md`
- `init-prompt-dry-run.md`
- `official-pals-index-consistency-check.md`
- `no-runtime-dependency-check.md`
- `no-internal-docs-release-check.md`

## Boundary

Current v0.1.0-rc.1 evals should keep `Simple Pal Mode only` as the active task path. Subagent Mode, Deep Conductor, parallel child workflows, and external Agent orchestration may appear only as future-design or negative-boundary checks.

Owner + Verifier evals are no-code staged workflow checks. They verify evidence handling, `pass` / `fail` / `blocked` records, and candidate-based verifier selection without creating runtime automation.

Session validation files are manual conversation scripts and transcript
templates. They are not automated tests and must not be reported as passed until
the target conversation has actually been run.

