<!-- Future design only. Not active in AgentPal v0.1 runtime. / 未来设计，仅作规划参考，不属于 AgentPal v0.1 当前运行行为。 -->

# Parallel Codex Subagent Mode Regression

## Purpose

This historical regression is retained as future design material.

AgentPal v0.1 current runtime is Simple Pal Mode only. Do not run this as a current v0.1 behavior expectation.

## Input

```text
这个项目下一版值不值得继续做？如果值得，怎么开发，怎么验收？
```

## Expected Mira Decision

Mira uses AI routing judgement case-by-case.

In a future orchestration layer, Mira could choose child workflows when authorization is present and:

- the current Codex environment supports subagents
- independent Pal perspectives materially improve this case
- the selected Pal set is justified by the current context

Visible wording must not claim a fixed Pal set is required by the phrase alone.

## Expected Spawn When Subagent Mode Is Used

Spawn only the case-selected subagents.

Record for each spawned agent:

- `agent_id`
- wait status
- close status
- `closed: true`

## Required Assets

Each selected Pal must read:

- its `PAL.md`
- its `SKILL.md`
- its `pal.json`
- its Response Fingerprint
- its core Output Contract

## Required Role Boundaries

- Owner Pal owns the main answer.
- Consultant Pal(s), if any, provide bounded input.
- Reviewer Pal(s), if any, provide bounded review.
- Mira synthesizes without rewriting specialist conclusions.

## Required Mira Synthesis

Mira must include:

- selected Pal conclusions
- agreements
- conflicts
- evidence gaps
- final recommendation
- runtime evidence

## Pass

- AI routing judgement is case-by-case.
- No hard-coded semantic routing is used.
- Pal capability reference is not a route map.
- Spawned agents have recorded `agent_id` values.
- Completed results are collected.
- Completed agents are closed.
- Each Pal reports required assets and output contract.
- Role boundaries are preserved.
- Mira synthesis keeps conclusions separate.

## Fail

- Mira writes all specialist content herself.
- A fixed Pal set is required by keyword or task wording alone.
- Any completed agent remains open.
- Subagent Mode is claimed without runtime evidence.
- Simple Pal Mode fallback is used without limitation marker.
- The answer describes subagents as OS-level background processes.



