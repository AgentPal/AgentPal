# R103-C Local PalSmith Runbooks README Policy Validation

## Decision

Pass.

## Scope

Allowed public files:

- `official/pals/PalSmith-pal-governor/runbooks/README.md`
- `release/integration-notes/r103c-palsmith-runbooks-readme-policy-pilot-summary.md`
- `evals/palbench/pal-asset/r103c-palsmith-runbooks-readme-policy-boundary.md`
- `release/fresh-clone-checks/r103c-local-palsmith-runbooks-readme-policy-validation.md`

Forbidden public changes:

- `official/pals/PalSmith-pal-governor/pal.json`
- `official/pals/PalSmith-pal-governor/asset-manifest.json`
- PalSmith directories other than `runbooks/README.md`
- other official Pals
- `workspace/organization/contacts/**`
- `README.md`
- `RESOURCE_INDEX.md`
- `agentpal.json`

## Validation Checklist

| Check | Result | Evidence |
| --- | --- | --- |
| README exists | pass | `official/pals/PalSmith-pal-governor/runbooks/README.md` exists |
| runbook vs workflow boundary clear | pass | README includes `Runbook vs workflow` and states a runbook is not a workflow |
| runbook vs Pal Skill boundary clear | pass | README includes `Runbook vs Pal Skill` and states a runbook is not a Pal Skill |
| no connector / no auto execution | pass | README includes `No connector / no auto execution` and states runbooks are no-code instructions |
| no credential storage | pass | README includes `No credentials` and states runbooks do not save credentials |
| no keyword route | pass | README includes `No keyword route` and forbids keyword routes / route maps |
| no external project `.agentpal` copy | pass | README includes `External project boundary` and says not to copy PalSmith runbooks into external project `.agentpal/` by default |
| `pal.json` unchanged | pass | `git diff --name-only HEAD -- official/pals/PalSmith-pal-governor/pal.json` returned empty |
| central roster unchanged | pass | `git diff --name-only HEAD -- workspace/organization/contacts` returned empty |
| no official Pal asset manifest generated | pass | `official/pals/PalSmith-pal-governor/asset-manifest.json` does not exist |
| no move / delete / rename of existing runbooks | pass | runbooks file set is the existing 3 runbooks plus new `README.md` |
| no forbidden public paths modified | pass | forbidden-path diff for PalSmith `pal.json`, PalSmith manifest, central contacts, `README.md`, `RESOURCE_INDEX.md`, and `agentpal.json` returned empty |

## Notes

Validation ran locally through Codex shell / PowerShell on 2026-06-28.

The validation distinguishes prohibition text from positive forbidden structures. R103-C files mention credentials, keyword routes, external project `.agentpal/`, connectors, and auto execution only to forbid them.
