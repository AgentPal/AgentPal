# Maintainer Release Handoff

Date: 2026-06-26

## Current Release Candidate

AgentPal v0.1.0-rc.1 is the documented release candidate line. The current local work appears to prepare a broader release candidate state that maintainers may choose to tag as `v0.1.0-rc.2` or another tag after review.

## What Is Ready

- 9 official bundled Pals are present and registered.
- Formal Skill asset standard is defined.
- 219 formal skills map to 219 actual assets; missing formal Skill assets: 0.
- PalSmith source lineage is present.
- No-code boundary checks pass.
- JSON parse checks pass.
- Release candidate reports through R14 are present or planned in this handoff set.

## What Is Not Done

- No staging was performed.
- No commit was created.
- No tag was created or moved.
- No push was performed.
- No GitHub Release was created or verified.
- Native `/pal` runtime API behavior is not-run.
- Live web fetch is not-run.
- External link checking is not-run.

## Required Manual Decisions

1. Confirm whether `origin` URL spelling is intentional.
2. Decide whether the release tag should be `v0.1.0-rc.2`, a moved `v0.1.0-rc.2`, `v0.1.0-rc.3`, or no tag yet.
3. Decide whether to use a single release commit or a three-commit series.
4. Decide whether any unusual docs filename should be renamed before staging.
5. Decide whether to publish now or keep the repository in release-review state.

## Remote Confirmation

Observed remote:

```text
origin = https://github.com/AgentPal/AgentPal.git
```

Maintainers must confirm the target repository before pushing.

## Tag Strategy

Observed local tags:

```text
v0.1.0-rc.1
v0.1.0-rc.2
```

Maintainer options:

- Use existing `v0.1.0-rc.2` if it already points to the intended final commit.
- Move/recreate `v0.1.0-rc.2` after the final commit, if repository policy allows retagging.
- Create `v0.1.0-rc.3` to avoid moving an existing tag.
- Defer tag creation until after another review.

Do not retag automatically.

## Stage Include

Suggested include buckets:

- root release docs and metadata
- `agentpal.json`
- `contacts/`
- `registry/`
- `docs/03-pal-pack-standard/`
- `docs/07-authoring-pals/`
- `evals/palbench/v0.5/documentation/archive/docs/08-release-candidate/`
- `docs/99-reference/`
- `release/v0.1.0-rc.1/`
- 9 official `pals/` directories

## Stage Exclude

Exclude:

- `.agentpal/`
- `exports/`
- `staging/`
- `quarantine/`
- `snapshots/`
- runtime-private memory, state, or reports
- test-only Pal packs or `_test` assets
- generated logs or local scratch files

## Suggested Commit Message

Single-commit option:

```text
release: prepare AgentPal v0.1.0-rc.2 Pal Pack workspace
```

Split-commit options are listed in `23-commit-grouping-plan.md`.

## Suggested Release Title

```text
AgentPal v0.1.0-rc.2
```

Adjust if maintainers choose another tag.

## GitHub Release Draft Source

Use `GITHUB_RELEASE_DRAFT.md` as the starting body. Review it manually after confirming tag, remote, and final staged diff.

## Known Limitations

- Simple Pal Mode only.
- AgentPal is no-code Markdown / JSON / protocol workspace content, not a runtime.
- Native `/pal` runtime API: not-run.
- Live web fetch: not-run.
- External link checker: not-run.
- GitHub Release: not created or verified by this handoff.

## Manual Commands Template

These are templates for maintainers. They were not executed by R14.

```text
git status --short
git diff --stat
git add <reviewed files>
git diff --cached --check
git commit -m "release: prepare AgentPal v0.1.0-rc.2 Pal Pack workspace"
git tag v0.1.0-rc.2
git push origin master
git push origin v0.1.0-rc.2
```

Adjust tag commands based on the final tag strategy.
