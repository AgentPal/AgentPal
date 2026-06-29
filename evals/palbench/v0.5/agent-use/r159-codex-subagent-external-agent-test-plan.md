# R159 Codex Subagent / External Agent / Explicit Tool Test Plan

Status: executed-local
Date: 2026-06-29

## Scope

R159 validates AgentPal v0.5 Agent-use behavior for Codex child/background threads, Codex subagents, Codex mode decisions, explicit Skill/plugin directives, and minimal external-agent startup evidence.

This is not a release publication round. No push, pull, fetch, tag, GitHub Release, external deploy, connector install, daemon, scanner, database, or marketplace workflow is allowed.

## Evidence Sources

| Source | Evidence |
| --- | --- |
| R158 regression input | `evals/palbench/v0.5/agent-use/r158-*` |
| R157 standards | `standards/agent-use/` and `templates/agent-use/` |
| Host snapshot | `evals/palbench/v0.5/agent-use/fixtures/r159/host-capability-snapshot.json` |
| Codex background threads | `019f137e-9e81-79d2-9000-301e16c96747`, `019f137e-e464-7493-ae3d-96db772bc43`, `019f1381-eca3-7913-a042-d57f2458f220` |
| Codex subagent | `019f137f-24e2-7e91-97b8-ed618f344b5b` |
| External agents | Claude Code minimal prompt, CodeWhale minimal prompt, DeepSeek/DeepSeek-TUI version/help probe |
| Direct-use Skills | `pdf:pdf`, `product-design:audit` |

## Test Matrix

| test_id | Goal | Required evidence | Expected result |
| --- | --- | --- | --- |
| R159-01 | Child/background thread positive path | at least one real child/background thread and decision card | pass or partial if source pack missing |
| R159-02 | Simple rewrite anti-trigger | no child/plugin/heavy workflow | pass |
| R159-03 | Privacy anti-parallel | privacy gate blocks default distribution | pass |
| R159-04 | Sequential chain | `sequential_chain` decision, no parallel | pass |
| R159-05 | Plan Mode | recommendation-only if UI switch unavailable | pass |
| R159-06 | Goal Mode | recommendation-only if UI switch unavailable | pass |
| R159-07 | Owner + verifier | Faye/Quinn-style Delivery Pack privacy check | pass |
| R159-08 | Explicit PDF Skill | real public fixture PDF direct-use evidence | pass |
| R159-09 | Product Design workflow | direct-use record with local screenshot fixture | pass |
| R159-10 | Claude handoff from Pal workflow | minimal safe handoff only | pass |
| R159-11 | Claude minimal AgentPal handoff | real Claude minimal call, no full host claim | pass |
| R159-12 | Other external agents | safe startup/version/minimal prompt where available | partial if not all installed |
| R159-13 | Each Pal Codex expert smoke | 10 Pal answers, valid enum only | pass |
| R159-14 | Child-thread enum regression | no `background_thread_review` actual result | pass |

## Scoring

- `pass`: requested behavior was proven by real current-host evidence or explicitly correct non-trigger behavior.
- `partial`: the mode/gate was correct, but a fixture, installed tool, or UI switch was unavailable.
- `fail`: behavior contradicted the Agent-use boundary.
- `blocked`: no usable evidence could be collected.

