# R108-B PalSmith Skills Index Boundary Eval

Date: 2026-06-28

## Scope

This eval covers the R108-B PalSmith skills index backfill:

- `official/pals/PalSmith-pal-governor/skills/index.md`

It verifies index completeness and boundary preservation. It does not execute PalSmith Skills, Runtime Agent Skills, scanners, validators, connectors, plugin discovery, MCP discovery, external business-system probes, official Pal edits, central roster edits, or remote Git operations.

## Required checks

| Check | Expected result |
| --- | --- |
| PalSmith path resolved from central roster | `palsmith-pal-governor` resolves to `official/pals/PalSmith-pal-governor` |
| PalSmith skills index exists | `official/pals/PalSmith-pal-governor/skills/index.md` exists |
| Required headings exist | All R108-B required headings are present |
| PalSmith Pal Skill definition clear | PalSmith Skills are no-code Pal asset governance methods |
| Agent Skill boundary clear | Runtime Agent Skills are referenced as candidates, not copied into Pal `skills/` |
| Current assets listed | The 15 mapped PalSmith skill cards and support files are listed |
| Asset classification relationship clear | Classification result is a no-code governance output |
| Existing Pal upgrade relationship clear | Upgrade reports are no-code reports and task-package inputs, not automatic edits |
| No external project default write | Index forbids copying central Pal assets into external project `.agentpal/` by default |
| No central roster mutation | Index states central roster changes require explicit gated work |
| No direct official Pal edits by default | Index states official Pal edits require exact user request and corresponding gate |
| No connector / scanner / auto execution | Index forbids connector, scanner, validator, daemon, marketplace, and auto-execution assets |
| No keyword routing | No active `keyword_map`, `domain_map`, `role_map`, or deterministic dispatch table is added |
| No credential storage | No credentials, tokens, secrets, cookies, passwords, or API keys are added |
| PalSmith `pal.json` unchanged | No diff to `official/pals/PalSmith-pal-governor/pal.json` |
| Central roster unchanged | No diff to `workspace/organization/contacts/**` |
| No `asset-manifest.json` generated | No PalSmith `asset-manifest.json` exists |

## Failure cases

The batch fails if the PalSmith skills index:

- treats Runtime Agent Skills as PalSmith Pal Skills;
- claims PalSmith Skills execute commands, call APIs, write files, or change systems by themselves;
- creates or implies a connector, scanner, validator, daemon, marketplace/hub program, auto sync engine, or auto execution engine;
- writes central Pal assets into external project `.agentpal/` by default;
- directly mutates central roster or `pal.json`;
- creates a keyword routing map or deterministic task-to-Pal dispatch table;
- stores credentials, tokens, secrets, private project data, private user memory, reports, raw research dumps, or runtime state;
- moves, deletes, renames, or rewrites existing PalSmith skill cards.

## Accepted result vocabulary

Use:

- `pass`
- `fail`
- `blocked`
- `not-run`
- `missing`

Do not convert `not-run`, `missing`, or weak evidence into `pass`.
