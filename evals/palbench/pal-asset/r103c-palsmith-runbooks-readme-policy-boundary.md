# R103-C PalSmith Runbooks README Policy Boundary

Date: 2026-06-28

## Purpose

This PalBench case checks that the PalSmith `runbooks/README.md` policy pilot explains runbook boundaries without changing PalSmith behavior, generating manifests, changing `pal.json`, or modifying central roster files.

## Required Files

| File | Expected result |
| --- | --- |
| `official/pals/PalSmith-pal-governor/runbooks/README.md` | exists |
| `release/integration-notes/r103c-palsmith-runbooks-readme-policy-pilot-summary.md` | exists |
| `release/fresh-clone-checks/r103c-local-palsmith-runbooks-readme-policy-validation.md` | exists |

## Checks

| Check | Expected result |
| --- | --- |
| README exists | pass |
| runbook vs workflow boundary clear | pass |
| runbook vs Pal Skill boundary clear | pass |
| no connector / no auto execution | pass |
| no credential storage | pass |
| no keyword route | pass |
| no external project `.agentpal` copy | pass |
| `pal.json` unchanged | pass |
| central roster unchanged | pass |
| no official Pal `asset-manifest.json` generated | pass |
| no move / delete / rename of existing runbooks | pass |

## Negative Cases

These outcomes fail the eval:

- `official/pals/PalSmith-pal-governor/pal.json` changes;
- `official/pals/PalSmith-pal-governor/asset-manifest.json` is generated;
- any PalSmith directory outside `runbooks/README.md` is modified;
- any other official Pal changes;
- `workspace/organization/contacts/**`, `README.md`, `RESOURCE_INDEX.md`, or `agentpal.json` changes;
- README claims runbooks execute actions;
- README stores credentials, tokens, secrets, private memory, or customer data;
- README creates keyword routes or deterministic semantic routes;
- README tells users to copy PalSmith runbooks into external project `.agentpal/` by default.

## Manual Validation Commands

Run or equivalent:

```powershell
Test-Path official/pals/PalSmith-pal-governor/runbooks/README.md
Select-String -Path official/pals/PalSmith-pal-governor/runbooks/README.md -Pattern "Runbook vs workflow|Runbook vs Pal Skill|No connector / no auto execution|No credentials|No keyword route|External project boundary|blocked|human review"
git diff --name-only HEAD -- official/pals/PalSmith-pal-governor/pal.json official/pals/PalSmith-pal-governor/asset-manifest.json workspace/organization/contacts README.md RESOURCE_INDEX.md agentpal.json
Test-Path official/pals/PalSmith-pal-governor/asset-manifest.json
```

Expected forbidden diff output is empty. Expected `asset-manifest.json` result is `False`.
