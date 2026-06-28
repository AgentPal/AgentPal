# R100-C Local Pal Index Template Validation

## Decision

Pass.

## Scope

Allowed public files:

- `templates/pal-asset/index-templates/README.md`
- `templates/pal-asset/index-templates/skills-index-template.md`
- `templates/pal-asset/index-templates/workflows-index-template.md`
- `templates/pal-asset/index-templates/runbooks-index-template.md`
- `templates/pal-asset/index-templates/knowledge-index-template.md`
- `templates/pal-asset/index-templates/memory-index-template.md`
- `templates/pal-asset/index-templates/learning-index-template.md`
- `templates/pal-asset/index-templates/evals-index-template.md`
- `templates/pal-asset/index-templates/examples-index-template.md`
- `templates/pal-asset/index-templates/research-index-template.md`
- `templates/pal-asset/safe-index-backfill-guide.md`
- `evals/palbench/pal-asset/r100c-pal-index-template-boundary.md`
- `release/fresh-clone-checks/r100c-local-pal-index-template-validation.md`
- `release/integration-notes/r100c-index-update-notes.md`

Forbidden public changes:

- `official/pals/**`
- `README.md`
- `RESOURCE_INDEX.md`
- `agentpal.json`
- `workspace/organization/contacts/pals.json`

## Validation Checklist

| Check | Result | Evidence |
| --- | --- | --- |
| all index templates exist | pass | 9 `*-index-template.md` files plus package `README.md` exist under `templates/pal-asset/index-templates/` |
| each index template includes required sections | pass | every index template contains Purpose, What belongs here, What does not belong here, Current assets, Candidate assets, Review notes, Related standards, Public safety boundary, and External project boundary |
| skills template distinguishes Pal Skill vs Agent Skill | pass | `skills-index-template.md` states Pal Skills are stored here and Agent Skills should be referenced, not stored |
| skills template forbids keyword route maps | pass | `skills-index-template.md` forbids keyword route maps and route-map fields |
| memory template distinguishes Memory vs Report | pass | `memory-index-template.md` says memory stores extracted long-term lessons and reports belong in `reports/` |
| memory template keeps project-private memory in central project record | pass | `memory-index-template.md` states project-private memory remains in central project record |
| learning template is candidate asset queue | pass | `learning-index-template.md` states learning is a candidate asset queue |
| safe backfill guide forbids moving content | pass | `safe-index-backfill-guide.md` includes `Do Not Move Content` |
| safe backfill guide forbids deleting content | pass | `safe-index-backfill-guide.md` includes `Do Not Delete Content` |
| safe backfill guide forbids changing `pal.json` | pass | `safe-index-backfill-guide.md` includes `Do Not Change pal.json` |
| safe backfill guide forbids changing central roster | pass | `safe-index-backfill-guide.md` includes `Do Not Change Central Roster` |
| safe backfill guide forbids external project writes | pass | `safe-index-backfill-guide.md` includes `Do Not Write Into External Projects` |
| safe backfill guide forbids credential storage | pass | `safe-index-backfill-guide.md` includes `Do Not Save Credentials` |
| no positive keyword routing map | pass | no positive JSON-style `keyword_map`, `domain_map`, or `role_map` map definitions found in R100-C files |
| no forbidden public paths modified | pass | `git diff --name-only HEAD -- official/pals README.md RESOURCE_INDEX.md agentpal.json workspace/organization/contacts/pals.json` returned empty |

## Notes

Validation ran locally through Codex shell / PowerShell on 2026-06-28.

The validation distinguishes prohibition text from positive forbidden structures. The templates mention keyword routing, external project writes, and credentials only to forbid them.
