<!-- Future design only. Not active in AgentPal v0.1 runtime. / 未来设计，仅作规划参考，不属于 AgentPal v0.1 当前运行行为。 -->

# Subagent Single Owner Atlas

## User input

```text
请 Atlas 评估这个开发任务下一步怎么做。
```

## Mira routing decision

Mira chooses Codex Subagent Mode only if the task needs independent Atlas judgment and Codex exposes subagent tools directly or through allowed deferred discovery. For a simple `/pal Atlas` consult, Simple Pal Mode is enough.

## Subagents spawned

- Atlas as owner Pal

## Required files Atlas reads

- `pals/Atlas-developer/PAL.md`
- `pals/Atlas-developer/SKILL.md`
- `pals/Atlas-developer/pal.json`
- `response-fingerprints/Atlas.md`
- `pals/Atlas-developer/core/output-contract.md`

## Expected result

Atlas returns engineering state, file / directory scope, development phases, acceptance command or criteria, risks, and next Codex task.

## Mira synthesis

Mira summarizes Atlas's conclusion without rewriting it as Mira's own engineering advice.

## Fallback if unavailable

```text
Subagent Mode unavailable
Using Simple Pal Mode
Limitations: Atlas is not an independent Codex subagent thread in this response.
```



