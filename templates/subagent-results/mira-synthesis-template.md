<!-- Future design only. Not active in AgentPal v0.1 runtime. / 未来设计，仅作规划参考，不属于 AgentPal v0.1 当前运行行为。 -->

# Mira Synthesis Template

Use this after Codex Subagent Mode results are collected.

```text
Mira：
I collected the Codex Subagent Mode results.

Runtime evidence:
- {Pal}: agent_id={agent_id}, wait={wait_status}, close={close_status}, closed={closed}

What each Pal concluded:
- {Pal}: {conclusion}

Where they agree:
- {agreement}

Where they differ:
- {conflict_or_difference}

Evidence gaps:
- {missing_evidence}

Final recommendation:
{recommendation}

Next action:
{next_action}

Whether to proceed:
{proceed_pause_or_retry}
```

Mira must preserve each Pal's professional judgment. If a subagent was blocked or unavailable, say so.


