<!-- Future design only. Not active in AgentPal v0.1 runtime. / 未来设计，仅作规划参考，不属于 AgentPal v0.1 当前运行行为。 -->

# Simple Pal Mode Vs Subagent Mode

## User input

```text
这个任务应该用 /pal Atlas 还是多 Pal 协作？
```

## Mira routing decision

Use Simple Pal Mode when one Pal can answer cheaply and clearly. Use Codex Subagent Mode when independent Pal separation matters.

## Subagents spawned

None for Simple Pal Mode.

For Subagent Mode, spawn only the required owner Pal / consultant Pal / reviewer Pal set, usually at most 3.

## Required files each subagent reads

Each subagent reads the required files in `registry/pal-subagent-map.json`.

## Expected result

- Simple Pal Mode: one active Pal, lower token cost, file-driven Pal work mode.
- Codex Subagent Mode: separate Codex subagent thread / workflow per specialist Pal, higher token cost, thread limit, close completed agents.
- Simple Pal Mode user wording: 当前 Codex 会话按某个 Pal 的工作方式回答。
- Subagent Mode user wording: Codex 派出多个子线程，让不同 Pal 分别处理自己的部分，再由 Mira 汇总。

## Runtime evidence in Subagent Mode

Mira records:

- `agent_id`
- `wait_agent` status
- `close_agent` status
- whether completed agents were closed

## Mira synthesis

Mira recommends the simplest mode that preserves role quality.

## Fallback if unavailable

Fallback to Simple Pal Mode and mark limitations.


