# Commit Grouping Plan

Date: 2026-06-26

Status: R14 maintainer handoff recommendation.

This plan suggests how maintainers can commit the current release-prep work. It does not stage or commit anything.

## Option A: Single Release Commit

Suggested commit message:

```text
release: prepare AgentPal v0.1.0-rc.2 Pal Pack workspace
```

Use this if maintainers want one auditable release-prep snapshot.

Pros:

- Simple history for release candidate handoff.
- Easier to tag one intended release commit.
- Avoids splitting interdependent Pal, registry, and release-report changes.

Cons:

- Large diff.
- Harder to review individual Pal deepening changes in isolation.

## Option B: Three Commit Series

### Commit 1: PalSmith And Pal Pack Standards

Suggested message:

```text
docs: add PalSmith governance and Pal Pack skill standards
```

Include:

- PalSmith assets and source lineage.
- Runtime Task Package docs.
- `docs/03-pal-pack-standard/15-formal-skill-assets.md`.
- PalSmith release and governance docs.

### Commit 2: Default Pals Deepening

Suggested message:

```text
docs: deepen official bundled Pal assets
```

Include:

- `pals/Mira-main/`
- `pals/Atlas-developer/`
- `pals/Vega-research/`
- `pals/Rhea-system/`
- `pals/Quinn-quality/`
- `pals/Morgan-document/`
- `pals/Harper-writing/`
- `pals/Nova-product/`
- `contacts/pals.json`
- `registry/pal.index.json`
- `agentpal.json`

### Commit 3: Release Candidate Docs And Verification Reports

Suggested message:

```text
docs: add AgentPal release candidate verification handoff
```

Include:

- `RELEASE_MANIFEST.md`
- `RELEASE_CHECKLIST.md`
- `RELEASE_NOTES.md`
- `CHANGELOG.md`
- `GITHUB_RELEASE_DRAFT.md`
- `release/v0.1.0-rc.1/release-notes-draft.md`
- `evals/palbench/v0.5/documentation/archive/docs/08-release-candidate/`
- `docs/99-reference/official-pals.md`

## Recommendation

Prefer the single release commit if maintainers plan to publish one release candidate tag from this workspace state. Prefer the three-commit series if maintainers want more review granularity before tagging.

In both strategies:

- Run `git diff --cached --check` after staging.
- Re-run JSON parse checks after staging.
- Confirm remote spelling and tag strategy before tagging.
- Do not use `git add .`; use explicit path buckets.

