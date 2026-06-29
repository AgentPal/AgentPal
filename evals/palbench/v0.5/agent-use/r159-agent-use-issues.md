# R159 Agent-use Issues

Status: executed-local
Date: 2026-06-29

## Summary

No blocker, high, or medium issue was found. Three partial/note items remain for future evidence tightening.

## Issues

| issue_id | severity | area | evidence | impact | recommended_fix | blocks_codex_first_release |
| --- | --- | --- | --- | --- | --- | --- |
| R159-LOW-01 | low | Child review fixture | R159-01 child thread could not verify Delivery Pack A content because the pack body was not provided | Child-thread mechanics are proven, but content review is partial | In R160, provide two small public fixture Delivery Packs so child review can pass content-level checks | no |
| R159-LOW-02 | low | Codex UI modes | Plan Mode and Goal Mode were recorded as recommendation-only; UI switching was not programmatically proven | Mode judgement is documented, but host-mode operation is not fully evidenced | Add an operator-captured Plan/Goal UI evidence note if required | no |
| R159-NOTE-01 | note | DeepSeek | DeepSeek/DeepSeek-TUI were checked by version/help only, not a model prompt | Startup availability is known, but no handoff behavior was tested | Keep as version/help-only unless user authorizes a prompt run | no |
| R159-NOTE-02 | note | OpenCode/Gemini | OpenCode and Gemini were unavailable on PATH | No support claim can be made for these hosts | Mark unavailable, not blocking Codex-first release | no |

## Negative Checks

- No fake subagent or fake Claude full-host pass claim detected.
- No unavailable external agent was upgraded to pass.
- No unauthorized external write was performed.
- No push, pull, fetch, tag, GitHub Release, or external deploy was performed.
- No customer-private data was written into public examples, Pal Packs, or global knowledge.
- `New1/.agentpal` remained thin.

