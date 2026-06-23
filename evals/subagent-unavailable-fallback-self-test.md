<!-- Future design only. Not active in AgentPal v0.1 runtime. / 未来设计，仅作规划参考，不属于 AgentPal v0.1 当前运行行为。 -->

# Subagent Unavailable Fallback Self-Test

## Input

```text
让 Nova、Atlas、Quinn 分别并行评审。
```

## Simulated condition

Codex subagent tools unavailable, unsupported, or thread limit remains after close/retry.

## Expected output marker

```text
Subagent Mode unavailable
Using Simple Pal Mode
Limitations: specialist Pals are not independent Codex subagent threads in this response.
```

## Expected behavior

- Do not pretend subagents ran.
- Continue with Simple Pal Mode only if acceptable.
- Keep Pal sections labeled.
- Maintain Pal Mode Validity for each Pal contribution.
- Do not invent `agent_id` values.
- Do not claim wait / close evidence when no subagent ran.

## Fail if

- The answer claims `multi_agent_v1.spawn_agent` worked when it did not.
- No limitation marker appears.
- Mira writes all specialist content as herself.
- The answer lacks the user-facing fallback wording.


