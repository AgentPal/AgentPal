# R100-C Pal Index Template Boundary Eval

Date: 2026-06-28

## Purpose

This PalBench case checks that the Pal asset index template package supports safe, lightweight index / README backfills without modifying official Pals, changing behavior, confusing Pal Skills with Agent Skills, or writing assets into external projects.

## Required Files

| File | Expected result |
| --- | --- |
| `templates/pal-asset/index-templates/README.md` | exists |
| `templates/pal-asset/index-templates/skills-index-template.md` | exists |
| `templates/pal-asset/index-templates/workflows-index-template.md` | exists |
| `templates/pal-asset/index-templates/runbooks-index-template.md` | exists |
| `templates/pal-asset/index-templates/knowledge-index-template.md` | exists |
| `templates/pal-asset/index-templates/memory-index-template.md` | exists |
| `templates/pal-asset/index-templates/learning-index-template.md` | exists |
| `templates/pal-asset/index-templates/evals-index-template.md` | exists |
| `templates/pal-asset/index-templates/examples-index-template.md` | exists |
| `templates/pal-asset/index-templates/research-index-template.md` | exists |
| `templates/pal-asset/safe-index-backfill-guide.md` | exists |

## Required Template Sections

Each index template must include:

- Purpose
- What belongs here
- What does not belong here
- Current assets
- Candidate assets
- Review notes
- Related standards
- Public safety boundary
- External project boundary

## Boundary Checks

| Check | Expected result |
| --- | --- |
| skills template distinguishes Pal Skill vs Agent Skill | pass |
| skills template says Agent Skills should be referenced, not stored | pass |
| skills template forbids keyword route maps | pass |
| skills template warns raw CLI command docs need Pal Skill wrapping | pass |
| memory template distinguishes Memory vs Report | pass |
| memory template says project-private memory remains central project record | pass |
| learning template is a candidate asset queue | pass |
| learning template requires promotion review | pass |
| safe backfill guide forbids moving content | pass |
| safe backfill guide forbids deleting content | pass |
| safe backfill guide forbids changing `pal.json` | pass |
| safe backfill guide forbids central roster changes | pass |
| safe backfill guide forbids external project writes | pass |
| no keyword routing maps | pass |
| no credential / token / secret storage | pass |

## Negative Cases

These outcomes fail the eval:

- editing `official/pals/**` in this thread;
- changing `README.md`, `RESOURCE_INDEX.md`, or `agentpal.json`;
- changing `workspace/organization/contacts/pals.json`;
- adding keyword route maps, `keyword_map`, `domain_map`, or `role_map`;
- storing credentials, tokens, secrets, or private customer data;
- writing Pal assets to external project `.agentpal/` by default;
- presenting index backfill as behavior change, schema upgrade, manifest generation, scanner, validator, or auto execution.

## Manual Validation Commands

Run or equivalent:

```powershell
Test-Path templates/pal-asset/index-templates/README.md
Get-ChildItem templates/pal-asset/index-templates -Filter *-index-template.md
Select-String -Path templates/pal-asset/index-templates/*-index-template.md -Pattern "## Purpose|## What Belongs Here|## What Does Not Belong Here|## Current Assets|## Candidate Assets|## Review Notes|## Related Standards|## Public Safety Boundary|## External Project Boundary"
Select-String -Path templates/pal-asset/index-templates/skills-index-template.md -Pattern "Pal Skills|Agent Skills should be referenced|keyword route|raw CLI command docs"
Select-String -Path templates/pal-asset/index-templates/memory-index-template.md -Pattern "Memory stores extracted long-term lessons|Reports belong in `reports/`|central project record"
Select-String -Path templates/pal-asset/index-templates/learning-index-template.md -Pattern "candidate asset queue|promotion review"
Select-String -Path templates/pal-asset/safe-index-backfill-guide.md -Pattern "Do Not Move Content|Do Not Delete Content|Do Not Change `pal.json`|Do Not Change Central Roster|Do Not Write Into External Projects|Do Not Save Credentials|Human Review Required"
git diff --name-only HEAD -- official/pals README.md RESOURCE_INDEX.md agentpal.json workspace/organization/contacts/pals.json
```

Expected forbidden path diff output is empty.
