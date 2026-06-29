# R148 Legacy Entry / Wording / File Cleanup Summary

Status: executed
Date: 2026-06-29

## Summary

R148 cleaned current user-facing entries and source-of-truth metadata so AgentPal v0.5 presents itself as a no-code Pal organization layer with Deep Conductor as no-code collaboration / mode-decision protocol. Historical evidence was preserved.

## Changed Files

| File | Change type |
| --- | --- |
| `agentpal.json` | updated top-level version, release status, active mode, runtime policy, Deep Conductor no-code flags, and allowed current paths |
| `AGENTS.md` | updated current workspace positioning and runtime policy |
| `README.md` | updated current version and Deep Conductor wording |
| `README.zh-CN.md` | updated current version and Deep Conductor wording |
| `PAL.md` | updated current version positioning |
| `SKILL.md` | updated current version metadata and description |
| `INIT_PROMPT.md` | updated source-of-truth read list to current workspace paths and v0.5 standards/templates |
| `docs/04-runtime-guides/00-runtime-compatibility.md` | updated current version |
| `docs/04-runtime-guides/01-use-with-codex.md` | updated Codex path to v0.5 and no-code Deep Conductor boundary |
| `docs/04-runtime-guides/02-use-with-claude-code.md` | updated Claude Code path to v0.5 and capability boundary |
| `docs/04-runtime-guides/03-use-with-generic-cli-agent.md` | updated Generic CLI path to v0.5 and capability boundary |
| `docs/04-runtime-guides/99-future-runtime-adapters.md` | updated future-adapter wording to v0.5 current boundary |
| `docs/04-runtime-guides/runtime-adapter-stability-guide.md` | updated adapter goal and source-of-truth pointers |
| `docs/04-runtime-guides/runtime-adapter-troubleshooting-prompt-cards.md` | updated direct Pal call card mode wording |
| `docs/04-runtime-guides/upgrade-existing-binding-to-thin-binding.md` | updated thin-binding mode fields |
| `prompts/README.md` | updated diagnostic subagent prompt boundary wording |

## Deleted Files

No files deleted in R148.

## Updated Prompts

R148 kept the host prompt alignment from the prior prompt-initialization pass and additionally updated `prompts/README.md` to remove old v0.1 normal-task wording. Current host prompts remain aligned for:

- Codex
- Claude Code
- CLI Agent compatibility entry
- Generic CLI Agent
- Maintenance
- Project Workgroup

## Updated Docs

R148 updated current runtime guides and root entry docs only. Older roadmaps, release records, evals, archive docs, and historical readiness files were preserved as evidence or design history.

## Updated Indexes

`RESOURCE_INDEX.md` and `agentpal.json` were updated to include the R148 cleanup audit, cleanup summary, deletion manifest, residual review list, validation, and readiness decision.

## Boundary Fixes

| Boundary | Result |
| --- | --- |
| No-code boundary | Current entries now state AgentPal v0.5 is a no-code Pal organization layer, not runtime execution. |
| Thin binding | Runtime guides continue to require thin binding and no copied Pal assets. |
| Capability unknown | Current runtime guides require host evidence or manual profile for subagent/external Agent/MCP/plugin/Skill use. |
| Routing wording | Current entry scans show 0 deterministic route hits. |
| Release boundary | Current entries preserve explicit no push/pull/fetch/tag/GitHub Release without current-session authorization. |

## Residual Risks

Older roadmap, release, eval, archive, and example files still contain old version terms and historical language. They are not current user entry points and do not block R149, but they should remain visible on the residual review list for future archive labeling if the project wants a stricter public package.
