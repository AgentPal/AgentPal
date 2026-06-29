# R159 Local Codex Subagent / External Agent Validation

Status: executed-local
Date: 2026-06-29

## Validation Checklist

| Check | Result | Evidence |
| --- | --- | --- |
| R159 files exist | pass | `evals/palbench/v0.5/agent-use/r159-*`, `release/fresh-clone-checks/r159-*`, `release/integration-notes/r159-r160-*` |
| `agentpal.json` parses | pass | PowerShell `ConvertFrom-Json -AsHashtable` |
| central contacts parse | pass | `workspace/organization/contacts/pals.json` |
| official Pal directories count | pass | 10 |
| all official `pal.json` parse | pass | local parse check |
| Codex background threads created | pass | `019f137e-9e81-79d2-9000-301e16c96747`, `019f137e-e464-7493-ae3d-96db772bc43`, `019f1381-eca3-7913-a042-d57f2458f220` |
| Codex subagent created and closed | pass | `019f137f-24e2-7e91-97b8-ed618f344b5b` |
| child-thread enum compliance | pass | no actual child result used `background_thread_review` |
| Claude Code minimal handoff | pass | `fixtures/r159/claude-minimal-handoff-evidence.json` |
| CodeWhale minimal startup | pass | `fixtures/r159/codewhale-minimal-startup-evidence.json` |
| DeepSeek probe | partial | version/help only |
| explicit PDF direct-use | pass | `fixtures/r159/pdf-direct-use-evidence.json` |
| explicit Product Design direct-use | pass | `fixtures/r159/product-design-direct-use-evidence.json` |
| `New1/.agentpal` thin binding | pass | only `AGENTPAL.md` and `project.json` |
| source/public privacy scan | pass | no customer-private fixture written |
| remote operations | pass | no push, pull, fetch, tag, GitHub Release |

## Host Snapshot

Host snapshot path: `evals/palbench/v0.5/agent-use/fixtures/r159/host-capability-snapshot.json`

Key statuses:

- Codex CLI: available, `codex-cli 0.137.0`
- Codex background thread: available
- Codex subagent: available
- Claude Code: available, minimal handoff pass
- CodeWhale: available, minimal prompt pass
- DeepSeek / DeepSeek-TUI: available by version/help only
- OpenCode / Gemini: unavailable
- `gh`, `wrangler`, HyperFrames CLI: unavailable

## Verdict

R159 is locally valid as a Codex-first Agent-use evidence round with partial non-Codex host coverage. It is not a remote release or publication action.

