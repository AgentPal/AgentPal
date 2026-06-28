# Safe Index Backfill Guide

Date: 2026-06-28

## Purpose

This guide explains how to add lightweight `index.md` or `README.md` files to existing Pal asset directories without changing Pal behavior.

Use it for small official Pal v0.5 navigability upgrades after the allowed paths are explicitly approved.

## What Safe Backfill Means

Safe index backfill means:

- add a public-safe index or README file;
- describe the directory purpose;
- list assets already present;
- list candidate assets separately;
- mark uncertainty as `unknown` or `needs-review`;
- preserve all existing content exactly where it is.

It does not mean upgrading the Pal's behavior, changing schema, or repairing content.

## Backfill Steps

1. Confirm the thread or task explicitly allows editing the target Pal path.
2. Read the relevant standard:
   - `standards/pal-asset/pal-asset-standard.md`
   - `standards/pal-asset/pal-asset-directory-standard.md`
   - `standards/pal-asset/pal-skill-vs-agent-skill-standard.md`
3. Choose the matching template from `templates/pal-asset/index-templates/`.
4. Inspect only the target directory needed for the index.
5. List existing files under `Current assets`.
6. Put possible future files under `Candidate assets`.
7. Mark unclear items as `unknown` or `needs-review`.
8. Add review notes for human or owner-Pal follow-up.
9. Run a boundary check before committing.

## Do Not Move Content

Do not move files between `knowledge/`, `skills/`, `workflows/`, `runbooks/`, `memory/`, `reports/`, `learning/`, `examples/`, `research/`, or `evals/` during an index-only backfill.

If a file appears misplaced, record it in `Review notes` as `needs-review` and leave the file in place.

## Do Not Delete Content

Do not delete, prune, rewrite, deduplicate, or archive existing assets during an index-only backfill.

If content appears stale, unsafe, or ambiguous, mark the issue and require human review.

## Do Not Change Behavior

Do not change:

- `PAL.md`
- `AGENTS.md`
- `SKILL.md`
- core protocols
- output contracts
- direct calls
- owner routing behavior
- examples in a way that changes current claims

An index backfill is navigation and boundary documentation only.

## Do Not Change `pal.json`

Do not add v0.5 metadata, asset manifests, directory lists, status fields, or version changes to `pal.json` during safe index backfill.

`pal.json` updates require a separate schema-focused thread with its own validation.

## Do Not Change Central Roster

Do not modify:

- `workspace/organization/contacts/pals.json`
- `workspace/organization/contacts/PAL_CONTACTS.md`
- `workspace/resources/registry/`
- `agentpal.json`

Central roster and registry changes require a separate confirmed governance task.

## Do Not Write Into External Projects

Do not write Pal indexes into external project `.agentpal/` folders.

External projects remain thin-bound. Central Pal assets, Pal memory, Pal workflows, Pal runbooks, reports, governance records, and reusable knowledge stay in the AgentPal central workspace or approved central records by default.

## Do Not Save Credentials

Never add credentials, tokens, secrets, cookies, API keys, passwords, private customer data, private user memory, or private project evidence to an index or README.

If an existing file name suggests sensitive content, do not open broad private material unless the task explicitly permits it. Mark the index note as `needs-review`.

## Marking Unknown And Needs-Review

Use `unknown` when evidence is not available.

Use `needs-review` when:

- the file may be in the wrong directory;
- the content may be private or stale;
- a Pal Skill may actually be an Agent Skill;
- a report may need memory extraction;
- a research note may need promotion to knowledge;
- a workflow and runbook boundary is unclear;
- human judgement is required before promotion.

Do not infer capability from directory presence alone.

## Human Review Required

Human or owner-Pal review is required when a backfill would:

- reclassify an asset;
- move or delete files;
- change `pal.json`;
- change central contacts or registry;
- change behavior or routing;
- touch private memory, reports, state, or customer data;
- decide whether an Agent Skill should be rewritten as a Pal Skill;
- decide whether public examples derived from user material are safe.

## Boundary Check

Before committing, run or equivalent:

```powershell
git diff --name-only -- official/pals
git diff --name-only -- README.md RESOURCE_INDEX.md agentpal.json workspace/organization/contacts/pals.json
rg -n "keyword_map|domain_map|role_map|password|secret|token|api_key|credential" <changed-files>
```

Expected result:

- only allowed target paths changed;
- no central roster or shared entry change;
- no keyword routing map;
- no credential or secret content.
