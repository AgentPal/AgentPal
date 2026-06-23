<!-- Future design only. Not active in AgentPal v0.1 runtime. / 未来设计，仅作规划参考，不属于 AgentPal v0.1 当前运行行为。 -->

# Simple Pal Mode Vs Subagent Mode Self-Test

## Purpose

Verify that AgentPal clearly distinguishes Simple Pal Mode from Codex Subagent Mode.

## Cases

### Simple Pal Mode

Input:

```text
/pal Atlas 帮我看一个开发问题
```

Expected:

- Single Atlas Pal work mode.
- No subagent claim.
- Lower token path.
- Atlas uses Response Fingerprint and Output Contract.
- User-facing explanation may say: 当前 Codex 会话按某个 Pal 的工作方式回答。

### Subagent Mode

Input:

```text
让 Nova、Atlas、Quinn 分别并行评审下一版是否值得做、怎么开发、怎么验收。
```

Expected:

- Codex Subagent Mode if tools are available.
- Nova / Atlas / Quinn results stay separate.
- Mira synthesizes.
- Completed agents are closed.
- Runtime evidence includes `agent_id`, wait status, close status.
- User-facing explanation may say: Codex 派出多个子线程，让不同 Pal 分别处理自己的部分，再由 Mira 汇总。

## Fail if

- Simple Pal Mode is described as an independent subagent thread.
- Subagent Mode is described as an OS-level background process.
- Fallback to Simple Pal Mode lacks limitation markers.
- Subagent Mode claims lack coordinator-recorded runtime evidence.


