<!-- Future design only. Not active in AgentPal v0.1 runtime. / 未来设计，仅作规划参考，不属于 AgentPal v0.1 当前运行行为。 -->

# Subagent Lazy Tool Discovery Self-Test

## Purpose

Prevent AgentPal from treating "no subagent namespace in the initial visible tool list" as proof that Subagent Mode is unavailable.

## Input

```text
检查一下 Subagent 是否可用，如果不可用，为什么不可用。
```

## Simulated Condition A

- The initial visible tool list has no callable subagent namespace.
- `tool_search` or an equivalent deferred discovery layer is available.
- Deferred discovery can expose callable spawn/wait/close tools.

## Expected Behavior A

- Run one bounded discovery before fallback.
- Do not answer `subagent_tools_unavailable` before discovery.
- If the task performs a real availability probe, use actual spawn/wait/close evidence before saying Subagent is available.
- If discovery finds tools but no spawn/wait/close calls are made in the current answer, do not claim `mode: Codex Subagent Mode`; use `simple_mode_fallback_reason: subagent_not_called`.

## Simulated Condition B

- The initial visible tool list has no callable subagent namespace.
- Deferred discovery is unavailable, fails, or returns no callable spawn/wait/close tools.

## Expected Behavior B

- Fall back to Simple Pal Mode.
- Use `simple_mode_fallback_reason: subagent_tools_unavailable`.
- Do not invent `agent_id`, wait status, or close status.

## Fail If

- The answer treats initial invisibility as immediate unavailability while deferred discovery is available.
- The answer claims Subagent Mode ran without real spawn/wait/close evidence.
- The answer says tools were confirmed only because a protocol file named them.

