# R148 Legacy Entry / Wording / File Audit

Status: executed
Date: 2026-06-29

## Scope

R148 audited the public AgentPal workspace for legacy entry points, legacy wording, and obsolete-file candidates before R149 manual test plan preparation.

This round is not manual testing, not README rewriting, not release preparation, not GitHub synchronization, and not a feature expansion round.

## Source Baseline

| Baseline | Evidence |
| --- | --- |
| R143-R146 automatic behavior tests | 184 executed, 184 pass |
| R147 fix decision | `no_r148_needed_ready_for_manual_test_plan` |
| R147 readiness | `ready_for_manual_test_plan` |
| R148 true scope | legacy entry / legacy wording / obsolete file cleanup before manual testing |

## Scan Scope

The scan covered the public workspace, including:

- root files: `README.md`, `README.zh-CN.md`, `START_HERE.md`, `AGENTS.md`, `INIT_PROMPT.md`, `agentpal.json`, `RESOURCE_INDEX.md`, `PAL.md`, `SKILL.md`
- `prompts/`
- `core/`
- `standards/`
- `templates/`
- `official/pals/`
- `workspace/`
- `examples/`
- `docs/`
- `release/`
- `evals/`
- `archive/`

Directories requested but not present as active public roots were recorded as absent rather than created: `imports/`, `scripts/`, and `tools/`.

## Search Pattern Groups

| Group | Patterns |
| --- | --- |
| Brand / old project names | `AgChat`, `AgPal`, `AgentPal1`, `desktop pet`, `桌宠`, `宠物`, `pet`, `QQ`, `微信` |
| Old mode / routing | `Simple Pal Mode only`, `simple mode only`, `simple-pal-mode-only`, `route it to`, `route to`, `auto route`, `自动路由`, `keyword route`, `keyword routing`, `关键词路由`, `development = Atlas`, `docs = Morgan`, `tests = Quinn` |
| Program expansion | `installer`, `CLI`, `command line`, `scanner`, `daemon`, `background service`, `connector`, `API client`, `marketplace`, `hub`, `database`, `runtime scanner`, `自动扫描`, `scan installed`, `detect installed` |
| External project pollution | `copy Pal`, `copy pals`, `copy memory`, `copy knowledge`, `copy workflows`, `.agentpal/pals`, `.agentpal/memory`, `.agentpal/knowledge`, `.agentpal/workflows` |
| Remote publication | `git push`, `git pull`, `git fetch`, `tag`, `GitHub Release`, `release API`, `GitHub API`, `remote publish` |
| Old version / old stage | `v0.1`, `v0.2`, `v0.3`, `v0.4`, `rc.1`, `MVP`, `release-ready`, `已可发布`, `发布准备` |

## Scan Counts

| Metric | Count |
| --- | ---: |
| Search patterns | 69 |
| Matched lines | 5,271 |
| Matched files | 1,548 |
| Current entry Simple-only hits after cleanup | 0 |
| Current entry deterministic route hits after cleanup | 0 |

## Category Counts

| Category | Count | Notes |
| --- | ---: | --- |
| `keep_current` | 969 | Current standards, examples, Pal docs, and boundary language that remains valid. |
| `update_required` | 16 | Current entry/source files updated in this round. |
| `obsolete_remove` | 0 | No file was safe enough to delete without risking historical evidence or references. |
| `archive_or_review` | 14 | Mainly older roadmap / release-candidate docs that may remain useful as design history. |
| `historical_test_record_keep` | 549 | Release, eval, archive, validation, issue, readiness, and history records kept as evidence. |
| `generated_or_duplicate_cleanup` | 0 | No clear generated duplicate was removed. |
| `forbidden_public_leak` | 0 | No internal path, credential, or real customer data leak requiring deletion was found. |

## High-Risk Findings

| Finding | Status |
| --- | --- |
| `agentpal.json` still presented top-level active mode as `simple-pal-mode-only` | fixed |
| root `AGENTS.md` still said current runtime policy was Simple Pal Mode only | fixed |
| runtime guides still described active paths as Simple-only | fixed |
| root README / README.zh-CN / PAL / SKILL still used `v0.3.0-rc.1` as current positioning | fixed |
| `INIT_PROMPT.md` referenced old `contacts/`, `registry/`, and `pals/` paths instead of current central contacts / official Pals | fixed |

## User-Facing Entry Findings

| Area | Finding | Action |
| --- | --- | --- |
| Root entry | outdated version and Simple-only wording | updated to v0.5 Pal collaboration |
| Runtime guides | outdated v0.1/v0.3 and Simple-only wording | updated to v0.5, simple path available, Deep Conductor no-code mode decision |
| Prompt index | diagnostic subagent prompt still framed as old v0.1 task handling | updated to host-evidence diagnostic wording |
| Metadata | `agentpal.json` top-level mode contradicted R147/R148 v0.5 state | updated mode, allowed paths, and Deep Conductor no-code flags |

## Obsolete File Candidates

No files were classified as safe `obsolete_remove` in R148. Older roadmap, archive, release, and eval files are either historical evidence or ambiguous design history.

## Files Requiring Update

The current-entry files updated in R148 are listed in `r148-legacy-entry-wording-file-cleanup-summary.md`.

## Files Requiring Deletion

None.

## Historical Records Kept

R142-R147 automatic behavior test evidence, validation files, readiness decisions, issue tables, summaries, older release notes, and archive records were kept. They may contain old version terms by design and should not be deleted only because they match legacy keywords.
