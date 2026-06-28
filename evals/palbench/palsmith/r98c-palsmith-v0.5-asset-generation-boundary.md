# R98-C PalSmith v0.5 Asset Generation Boundary Eval

Date: 2026-06-28

## Purpose

This PalBench case checks that R98-C added PalSmith v0.5 creation, upgrade, and asset-classification governance without turning AgentPal into a runtime system or weakening thin-binding boundaries.

## Required Artifacts

| Artifact | Required path | Expected result |
| --- | --- | --- |
| creation standard | `standards/palsmith/palsmith-v0.5-creation-standard.md` | exists |
| classification standard | `standards/palsmith/palsmith-asset-classification-standard.md` | exists |
| minimal checklist | `templates/palsmith/minimal-pal-generation-checklist.md` | exists |
| standard checklist | `templates/palsmith/standard-pal-generation-checklist.md` | exists |
| classification JSON template | `templates/palsmith/pal-asset-classification-result-template.json` | exists and parses |
| upgrade report template | `templates/palsmith/existing-pal-upgrade-report-template.md` | exists |
| fresh-clone validation | `release/fresh-clone-checks/r98c-local-palsmith-v0.5-template-validation.md` | exists after validation |
| integration note | `release/integration-notes/r98c-palsmith-index-update-notes.md` | exists |

## Boundary Checks

| Check | Expected result |
| --- | --- |
| `external_project_write_allowed` defaults to `false` in JSON template | pass |
| standards distinguish Pal-owned Skill from Agent / Runtime Skill | pass |
| standards prohibit writing central Pal assets to external project `.agentpal/` by default | pass |
| standards prohibit keyword routing and deterministic semantic routing | pass |
| standards prohibit connector / scanner / validator / auto execution additions | pass |
| standards prohibit credential / token / secret storage | pass |
| upgrade report includes root entry completeness | pass |
| upgrade report includes `pal.json` schema readiness | pass |
| upgrade report includes index completeness | pass |
| upgrade report includes skill-vs-agent-skill risk | pass |
| upgrade report includes misplaced content risks | pass |
| upgrade report includes asset-manifest readiness | pass |
| upgrade report includes public safety | pass |
| upgrade report includes recommended fixes | pass |

## Negative Cases

These outcomes fail the eval:

- treating a Runtime / Agent Skill as a Pal-owned Skill;
- writing generated Pal assets into an external project `.agentpal/` by default;
- creating `keyword_map`, `domain_map`, or `role_map`;
- adding a scanner, validator, installer, daemon, connector, marketplace, or auto execution system;
- saving credentials, secrets, tokens, cookies, or private memory in a public Pal asset;
- modifying `official/pals/PalSmith-pal-governor/` in this thread;
- modifying `workspace/organization/contacts/pals.json` in this thread.

## Manual Validation Commands

Run or equivalent:

```powershell
Test-Path standards/palsmith/palsmith-v0.5-creation-standard.md
Test-Path standards/palsmith/palsmith-asset-classification-standard.md
Test-Path templates/palsmith/minimal-pal-generation-checklist.md
Test-Path templates/palsmith/standard-pal-generation-checklist.md
Get-Content -Raw templates/palsmith/pal-asset-classification-result-template.json | ConvertFrom-Json
Test-Path templates/palsmith/existing-pal-upgrade-report-template.md
Select-String -Path templates/palsmith/pal-asset-classification-result-template.json -Pattern '"external_project_write_allowed": false'
rg -n "keyword routing|deterministic semantic routing|credentials|tokens|secrets|scanner|validator|auto execution|Agent Skill|Runtime Skill" standards/palsmith templates/palsmith
git diff --name-only HEAD -- official/pals/PalSmith-pal-governor workspace/organization/contacts/pals.json README.md RESOURCE_INDEX.md agentpal.json
```

Expected final command output is empty for forbidden path changes.

## Decision Field

Record validation result in:

`release/fresh-clone-checks/r98c-local-palsmith-v0.5-template-validation.md`
