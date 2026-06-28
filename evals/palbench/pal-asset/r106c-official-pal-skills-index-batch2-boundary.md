# R106-C Official Pal Skills Index Batch 2 Boundary Eval

Date: 2026-06-28

## Scope

This eval covers the R106-C skills index backfill for:

- `official/pals/Nova-product/skills/index.md`
- `official/pals/Vega-research/skills/index.md`
- `official/pals/Harper-writing/skills/index.md`
- `official/pals/Rhea-system/skills/index.md`

It verifies index completeness and boundary preservation. It does not execute Pal Skills, Runtime Agent Skills, scanners, validators, connectors, plugin discovery, MCP discovery, external business-system probes, remote Git operations, tags, or GitHub Releases.

## Required Checks

| Check | Expected result |
| --- | --- |
| Selected skills indexes exist | Nova, Vega, Harper, and Rhea each have `skills/index.md` |
| Required headings exist | Every selected index includes the R107 required heading set |
| Pal Skill definition exists | Each index defines Pal Skills as role-level work capabilities |
| Agent Skill boundary exists | Each index states Runtime Agent Skills should be referenced, not copied |
| Current assets are listed | Existing skill directories, flat skill cards, or support files are listed |
| Candidate skills are separated | No new concrete Pal Skill is added in R106-C; candidates are marked as needs-review |
| Agent Skill references stay references | Runtime capabilities are execution candidates only |
| Related workflows and runbooks are referenced | Existing workflow/runbook areas are referenced without loading all content |
| Verification boundary exists | Each index requires current runtime evidence before execution claims |
| Memory writeback boundary exists | Reports, raw research, and private data are not written wholesale into memory |
| External project boundary exists | Each index forbids copying Pal Skills into external project `.agentpal/` by default |
| No keyword routing | No `keyword_map`, `domain_map`, `role_map`, or deterministic dispatch table is added |
| No credentials | No credentials, tokens, secrets, cookies, passwords, or API keys are added |
| No Agent Skill copying | No runtime skill registry files are copied into Pal `skills/` |
| No behavior change | Pal identity, direct calls, routing, output contracts, and runtime behavior are unchanged |
| No protected file diff | `pal.json`, central contacts, shared entry files, and asset manifests remain unchanged |

## Failure Cases

R106-C fails if any selected index:

- treats a Runtime Agent Skill as a Pal Skill;
- claims a Pal Skill executes commands, calls APIs, changes files, scans systems, or validates assets by itself;
- contains a keyword routing map or deterministic task-to-Pal dispatch table;
- copies raw CLI/API docs as the full Pal Skill;
- adds credentials, tokens, secrets, private project data, private user memory, full reports, or raw research dumps;
- creates or references an official `asset-manifest.json` as generated current state;
- requires external project `.agentpal/skills/` storage by default;
- removes, moves, deletes, or renames existing skill assets.

## Accepted Result Vocabulary

Use:

- `pass`
- `fail`
- `blocked`
- `not-run`
- `missing`

Do not convert `not-run`, `missing`, or weak evidence into `pass`.
