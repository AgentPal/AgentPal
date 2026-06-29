# R159 Explicit Tool Directive Records

Status: executed-local
Date: 2026-06-29

## Rule

When the user explicitly names a Skill, plugin, tool, workflow, or external agent, AgentPal must treat that as a directive to evaluate direct-use first. Direct-use is allowed only when capability evidence, privacy boundary, input sufficiency, and safety gates are satisfied.

## Records

| record_id | directive_source | requested tool/agent | owner Pal judgement | invocation_type | real invocation | evidence_path | safety result | score |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| R159-DIR-01 | user_directive | `pdf:pdf` | Morgan direct-use after public fixture check | real local parse | yes | `evals/palbench/v0.5/agent-use/fixtures/r159/pdf-direct-use-evidence.json` | public fixture only | pass |
| R159-DIR-02 | workflow_directive | `product-design:audit` | Nova direct-use after screenshot fixture check | local audit evidence | yes | `evals/palbench/v0.5/agent-use/fixtures/r159/product-design-direct-use-evidence.json` | public local screenshot | pass |
| R159-DIR-03 | Pal workflow directive | Claude Code handoff | Atlas external-agent handoff, not full host acceptance | minimal handoff | yes | `evals/palbench/v0.5/agent-use/fixtures/r159/claude-minimal-handoff-evidence.json` | no write, no full-host claim | pass |
| R159-DIR-04 | external agent probe | CodeWhale | Rhea capability snapshot, safe no-write prompt | minimal prompt | yes | `evals/palbench/v0.5/agent-use/fixtures/r159/codewhale-minimal-startup-evidence.json` | no write | pass |
| R159-DIR-05 | external agent probe | DeepSeek / DeepSeek-TUI | Rhea capability snapshot | version/help only | partial | `evals/palbench/v0.5/agent-use/fixtures/r159/deepseek-tui-startup-evidence.json` | no prompt/model call | partial |
| R159-DIR-06 | external agent probe | OpenCode / Gemini | Rhea capability snapshot | unavailable | no | `evals/palbench/v0.5/agent-use/fixtures/r159/host-capability-snapshot.json` | unavailable, not claimed | partial |

## Negative Checks

- No directive was converted into a hard-coded route.
- No unavailable external agent was reported as pass.
- No Skill/plugin was invoked without reading its current Skill instructions when required.

