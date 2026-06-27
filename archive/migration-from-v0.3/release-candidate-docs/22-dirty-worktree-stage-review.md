# Dirty Worktree Stage Review

Date: 2026-06-26

Status: R14 maintainer stage review handoff.

This report classifies the current dirty worktree for human staging. It does not run `git add`, `git commit`, `git tag`, `git push`, or GitHub Release publishing.

## Git Evidence

Observed commands:

- `git remote -v`: `origin https://github.com/AgentPal/AgentPal.git` for fetch and push.
- `git tag --list`: `v0.1.0-rc.1`, `v0.1.0-rc.2`.
- `git log --oneline -n 10`: latest commit is `efcf4ef docs: clarify runtime subagent responsibilities`.
- `git diff --name-only`: 133 tracked modified files before R14 report writes.
- `git diff --stat`: 133 files changed, 3044 insertions, 2735 deletions before R14 report writes.
- `git diff --check`: pass with LF-to-CRLF warnings only.

## Classification Summary

Trusted R14 classification before writing this report:

| Set | Count |
| --- | ---: |
| tracked modified | 133 |
| untracked | 642 |
| combined dirty entries | 775 |

| Category | Tracked | Untracked | Combined | Stage guidance |
| --- | ---: | ---: | ---: | --- |
| A root release docs include | 11 | 0 | 11 | Include after maintainer review. |
| A release registry notes include | 3 | 0 | 3 | Include with registration review. |
| A docs include | 7 | 6 | 13 | Include with docs review. |
| A release candidate include | 2 | 30 | 32 | Include the reports and release evidence selected by maintainer. |
| B default Pal assets review include | 110 | 604 | 714 | Include after a quick sweep because this is the largest surface. |
| B docs review include | 0 | 2 | 2 | Include if maintainers accept the docs topic and filename. |
| C test assets exclude | 0 | 0 | 0 | No matching dirty entries found. |
| D runtime state exclude | 0 | 0 | 0 | No matching dirty entries found. |
| E maintainer decision | 0 | 0 | 0 | No unmatched dirty entries in trusted classification. |

## A. Recommended Stage Include

Core release assets:

- root release docs: `README.md`, `AGENTS.md`, `PAL.md`, `SKILL.md`, `RELEASE_NOTES.md`, `CHANGELOG.md`, `GITHUB_RELEASE_DRAFT.md`, `RELEASE_CHECKLIST.md`, `RELEASE_MANIFEST.md`
- workspace metadata: `agentpal.json`
- contacts and registry: `contacts/pals.json`, `registry/pal.index.json`
- release note draft: `release/v0.1.0-rc.1/release-notes-draft.md`
- public docs under `docs/03-pal-pack-standard/`, `docs/07-authoring-pals/`, `docs/08-release-candidate/`, and `docs/99-reference/`
- 9 official bundled Pal directories:
  - `pals/Mira-main/`
  - `pals/PalSmith-pal-governor/`
  - `pals/Atlas-developer/`
  - `pals/Vega-research/`
  - `pals/Rhea-system/`
  - `pals/Quinn-quality/`
  - `pals/Morgan-document/`
  - `pals/Harper-writing/`
  - `pals/Nova-product/`

R13/R14-specific include:

- `docs/03-pal-pack-standard/15-formal-skill-assets.md`
- `docs/08-release-candidate/20-formal-skill-assets-audit.md`
- `docs/08-release-candidate/21-formal-skill-assets-fix-report.md`
- `docs/08-release-candidate/official-pal-field-strategy-decision.md`
- all 9 `skills/skill-asset-map.md` files
- `docs/08-release-candidate/22-dirty-worktree-stage-review.md`
- `docs/08-release-candidate/23-commit-grouping-plan.md`
- `docs/08-release-candidate/24-maintainer-release-handoff.md`
- `docs/08-release-candidate/25-final-maintainer-stage-readiness-report.md`

## B. Include After Quick Maintainer Sweep

The largest stage bucket is 9 default Pal assets. Maintainership should quickly scan these groups before staging:

- Pal `PAL.md`, `SKILL.md`, `AGENTS.md`, `README.md`, and `pal.json` updates.
- Pal `skills/`, `knowledge/`, `workflows/`, `runbooks/`, `evals/`, and `reports/` Markdown assets.
- PalSmith source lineage:
  - `pals/PalSmith-pal-governor/research/source-inventory.md`
  - `pals/PalSmith-pal-governor/research/source-coverage-matrix.md`

## C. Recommended Stage Exclude

No dirty entries matched the current test-asset exclusion patterns:

- `pals/_test*`
- `imports/_test*`
- `exports/_test*`
- `snapshots/_test*`
- `reports/_test*`
- `docs/08-release-candidate/test-reports/*`

If such files appear before maintainer staging, exclude them unless the maintainer deliberately chooses a summary-only release evidence file.

## D. Runtime State Exclude

No dirty entries matched runtime-state paths:

- `.agentpal/`
- `exports/`
- `staging/`
- `quarantine/`
- `snapshots/`
- runtime-private memory, state, or reports paths

If they appear later, exclude them from release staging.

## E. Need Maintainer Decision

Required human decisions:

- Confirm the intended remote URL is `https://github.com/AgentPal/AgentPal.git`.
- Decide tag strategy for existing tags `v0.1.0-rc.1` and `v0.1.0-rc.2`.
- Decide whether to stage all 9 default Pal asset additions as one release-prep commit or split them into themed commits.
- Review any docs file with unusual or non-ASCII filename before staging.

## Recommended Stage Include

Use path buckets, not a blind `git add .`:

- root release docs and metadata
- `contacts/`
- `registry/`
- selected `docs/`
- selected `release/`
- 9 official `pals/` directories

## Recommended Stage Exclude

Exclude:

- runtime-private paths
- test-only assets
- local scratch files
- generated logs
- any file whose source is unclear during human review

## Need Maintainer Decision

The worktree is suitable for maintainer stage review, but not for automatic staging. The next action is human selection of files, followed by staged diff review.
