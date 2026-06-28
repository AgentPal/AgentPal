# R107 Official Pal Skills Index Integrated Boundary

Date: 2026-06-28

## Scope

This integrated boundary eval covers the combined R106-A/B/C/D result set after R107 repair and integration.

It checks:

- PalSmith memory / research README;
- Atlas / Quinn / Morgan skills index;
- Nova / Vega / Harper / Rhea skills index;
- R106-D integration gate / checklist / issue template;
- R107 integration summary and validation.

It does not execute Pal Skills, Runtime Agent Skills, scanners, validators, connectors, plugin discovery, MCP discovery, external business-system probes, remote Git operations, tags, or GitHub Releases.

## Required Paths

| Group | Required paths |
| --- | --- |
| R106-A | `official/pals/PalSmith-pal-governor/memory/README.md`; `official/pals/PalSmith-pal-governor/research/README.md`; R106-A eval / validation / summary |
| R106-B | Atlas / Quinn / Morgan `skills/index.md`; R106-B eval / validation / summary |
| R106-C | Nova / Vega / Harper / Rhea `skills/index.md`; R106-C eval / validation / summary |
| R106-D | R106-D gate / validation / checklist / issue template |
| R107 | R107 summary / eval / validation |

## Required Checks

| Check | Expected result |
| --- | --- |
| actual directory | `J:\开发\AgentPal` |
| R106-A leftovers | processed or none |
| R106-B leftovers | processed or none |
| R106-C target | completed after R107补漏 |
| R106-D gate files | present |
| PalSmith memory README | present |
| PalSmith research README | present |
| Atlas / Quinn / Morgan skills index | present |
| Nova / Vega / Harper / Rhea skills index | present |
| R107 integration summary | present |
| R107 eval | present |
| R107 validation | present |
| central roster | parses; registered / active = 9 / 9 |
| official Pal dirs | 9 |
| all official Pal `pal.json` parse | pass |
| official Pal `pal.json` diff | empty |
| central contacts diff | empty |
| official `asset-manifest.json` generated | 0 |
| active keyword routing | 0 |
| connector / scanner / marketplace program | 0 |
| credential leak | 0 |
| external project `.agentpal` thick binding | 0 |
| visible JSON parse | pass |
| clean-copy | pass |

## Skills Index Content Checks

Every selected skills index must include:

- `# Skills Index`
- `## Purpose`
- `## Pal Skill definition`
- `## Agent Skill boundary`
- `## What belongs here`
- `## What does not belong here`
- `## Current assets`
- `## Candidate skills / needs review`
- `## Agent Skill references`
- `## Related workflows / runbooks`
- `## Verification boundary`
- `## Memory writeback boundary`
- `## External project boundary`

## Failure Cases

The integrated gate fails if:

- R106-C target evidence remains missing;
- any selected skills index is missing;
- PalSmith memory or research README is missing;
- any official Pal `pal.json` changes;
- any real official `asset-manifest.json` is generated;
- central contacts change;
- a keyword, domain, role, or deterministic route map is added;
- Agent Skill files are copied into Pal `skills/`;
- full report text is copied into memory;
- raw research is promoted directly into knowledge;
- connector, scanner, validator, daemon, installer, marketplace, hub, auto-sync, or auto-execution behavior is introduced;
- credentials, tokens, passwords, API keys, secrets, private customer data, or private project evidence are added;
- external project `.agentpal/` directories receive Pal assets by default;
- clean-copy is not run but the report claims clean-copy pass.

## Accepted Result Vocabulary

Use:

- `pass`
- `fail`
- `blocked`
- `not-run`
- `missing`

Do not convert `not-run`, `missing`, or weak evidence into `pass`.
