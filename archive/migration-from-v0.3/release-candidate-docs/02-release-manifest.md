# Release Manifest

This page gives a public-readable manifest for v0.1.0-rc.1. The root [Release Manifest](../../RELEASE_MANIFEST.md) remains the release-file source.

## Identity

| Item | Value |
| --- | --- |
| Name | AgentPal v0.1.0-rc.1 |
| Version | `v0.1.0-rc.1` |
| License | MIT |
| Release status | Release candidate |
| Active runtime behavior | Simple Pal Mode only |
| Workspace format | Markdown / JSON / protocol files |

## Official Bundled Pals

| Pal | Directory | Role |
| --- | --- | --- |
| Mira | `pals/Mira-main` | Main Pal, Leader Pal, Conductor, and Pal team leader and coordinator |
| Atlas | `pals/Atlas-developer` | Development perspective |
| Vega | `pals/Vega-research` | Research and evidence perspective |
| Rhea | `pals/Rhea-system` | Local system and environment perspective |
| Quinn | `pals/Quinn-quality` | Quality, risk, evidence, and acceptance perspective |
| Morgan | `pals/Morgan-document` | Document and file workflow perspective |
| Harper | `pals/Harper-writing` | Writing and communication perspective |
| Nova | `pals/Nova-product` | Product and decision perspective |

## Release Evidence Files

- `RELEASE_NOTES.md`
- `RELEASE_CHECKLIST.md`
- `GITHUB_RELEASE_DRAFT.md`
- `RELEASE_MANIFEST.md`
- `release/v0.1.0-rc.1/docs-audit.md`
- `release/v0.1.0-rc.1/pal-pack-audit.md`
- `release/v0.1.0-rc.1/public-safe-audit.md`
- `release/v0.1.0-rc.1/release-notes-draft.md`
- `docs/06-validation-and-evidence/01-palbench-small-sample-report.md`

## Publication State

The repository state should include a local `v0.1.0-rc.1` tag pointing at the final intended release commit before publication.

No remote push or online GitHub Release was performed or verified during this documentation pass. Publish only after maintainers verify the final intended commit, tag, remote, and release page.

If additional documentation changes are accepted after a local tag is created, maintainers should create the final intended release commit and move or recreate the `v0.1.0-rc.1` tag before pushing.
