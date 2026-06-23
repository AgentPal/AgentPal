<!-- Future design only. Not active in AgentPal v0.1 runtime. / 未来设计，仅作规划参考，不属于 AgentPal v0.1 当前运行行为。 -->

# Multi-Pal Parallel Prompt

Use this template when Mira starts parallel Codex Subagent Mode work.

## Coordinator Brief

Mira remains coordinator and final summarizer. Specialist Pals run as separate Codex subagent threads. Subagents are not OS-level background processes.

## Task

`{task_goal}`

## Batch Limit

Default maximum parallel subagents: 3.

If more than 3 Pals are required, run batches and close completed agents before spawning the next batch.

## Suggested Roles

- owner Pal: `{owner_pal}`
- consultant Pal(s): `{consultant_pals}`
- reviewer Pal(s): `{reviewer_pals}`

## Prompt Requirements For Each Subagent

Each subagent prompt must include:

- Pal identity
- "You are not Mira"
- required asset list
- output contract
- permission boundary
- no project file modification unless authorized
- structured result fields

## Result Collection

Collect each result using `templates/subagent-results/subagent-result-template.md`.

Mira synthesis must use `templates/subagent-results/mira-synthesis-template.md`.



