<!-- Future design only. Not active in AgentPal v0.1 runtime. / 未来设计，仅作规划参考，不属于 AgentPal v0.1 当前运行行为。 -->

# Subagent Concurrency Close Policy Self-Test

## Purpose

Verify that Codex Subagent Mode respects thread limit and close policy.

## Test

1. Prepare a task requiring more than 3 Pals.
2. Spawn at most 3 subagents in the first batch.
3. Wait completed agents.
4. Close completed agents.
5. Spawn remaining subagents only after close.
6. If thread limit occurs, close completed agents and retry once.
7. If retry fails, fallback to Simple Pal Mode.

## Expected pass

- Default maximum parallel subagents is 3.
- Completed agents are closed.
- Thread limit fallback is explicit.
- Result collection marks incomplete or blocked agents.
- Coordinator records close evidence for each completed `agent_id`.

## Observed Coverage

The Nova + Atlas + Quinn regression uses exactly 3 parallel subagents and must close all three after results are collected.

## Fail if

- More than 3 subagents are spawned by default.
- Completed agents are not closed.
- Thread limit failure is hidden.
- More agents are spawned after a thread limit without closing completed agents first.


