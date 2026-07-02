<!-- Future design only. Not active in AgentPal v0.1 runtime. / 未来设计，仅作规划参考，不属于 AgentPal v0.1 当前运行行为。 -->

# Simple Pal Mode Vs Subagent Mode

## User input

```text
这个任务应该用 /pal Atlas 还是多 Pal 协作？
```

## Mira routing decision

Use Simple Pal Mode for AgentPal v0.1.0-rc.1 task handling. Treat Codex Subagent Mode as future design material only.

## Subagents spawned

None for Simple Pal Mode.

For future Subagent Mode design, a later release may define bounded owner Pal / consultant Pal / reviewer Pal child workflows.

## Required files each subagent reads

In v0.1, no subagent files are loaded for current task handling. Future design notes may reference `registry/pal-subagent-map.json`.

## Expected result

- Simple Pal Mode: one active Pal, lower token cost, file-driven Pal work mode.
- Future Codex Subagent Mode: separate Codex subagent thread / workflow per specialist Pal, higher token cost, thread limit, close completed agents.
- Simple Pal Mode user wording: 当前 Codex 会话按某个 Pal 的工作方式回答。
- Future Subagent Mode wording: 未来版本可能派出多个子线程；当前 v0.1 不会这样执行。

## Runtime evidence in Subagent Mode

Mira does not record these fields in v0.1 because no subagent is started. A future design may record:

- `agent_id`
- `wait_agent` status
- `close_agent` status
- whether completed agents were closed

## Mira synthesis

Mira recommends the simplest mode that preserves role quality.

## Fallback if unavailable

Use Simple Pal Mode and mark limitations if the user expected independent runtime execution.


