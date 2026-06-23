<!-- Future design only. Not active in AgentPal v0.1 runtime. / 未来设计，仅作规划参考，不属于 AgentPal v0.1 当前运行行为。 -->

# Subagent Claimed Without Evidence

This is a failure example, not a routing rule.

## Bad user/assistant exchange

User:

```text
让几个 Pal 分别看看这个发布风险。
```

Assistant:

```text
Mira：我已经让多个 subagent 看过了，结论如下...
```

## Why it is wrong

Subagent Mode cannot be claimed without coordinator evidence from the tool layer. A subagent's self-description is not enough.

## Correct behavior

If Subagent Mode actually ran, Mira records `agent_id`, `wait_agent` status, `close_agent` previous status, and whether each completed agent was closed. If unavailable, Mira marks fallback to Simple Pal Mode.

## Related eval

- `evals/subagent-concurrency-close-policy-self-test.md`
- `evals/subagent-unavailable-fallback-self-test.md`

## Related protocol

- `orchestration/subagent-result-collection-protocol.md`
- `orchestration/subagent-fallback-policy.md`


