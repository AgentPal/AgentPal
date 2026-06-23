<!-- Future design only. Not active in AgentPal v0.1 runtime. / 未来设计，仅作规划参考，不属于 AgentPal v0.1 当前运行行为。 -->

# Codex Subagent Availability Self-Test

## Purpose

Check whether the current Codex environment supports Codex Subagent Mode.

## Minimum test

1. Spawn Subagent A.
2. Prompt Subagent A to read `README.md` only and return three bullets.
3. Spawn Subagent B.
4. Prompt Subagent B to read `pals/Mira-main/PAL.md` only and return three bullets.
5. `wait_agent` for both.
6. `close_agent` for both completed agents.
7. Record `supported`, `unsupported`, or `unclear`.

## Expected pass

- Distinct agent IDs are returned.
- Both agents return bounded read-only summaries.
- Completed agents are closed.
- The record says subagents are Codex subagent threads / workflows, not OS-level background processes.
- The coordinator records `agent_id`, wait status, close status, and `closed: true`.

## Observed Note

Subagents may not know or correctly report their own workflow status. If `spawn_agent` returned an `agent_id`, `wait_agent` returned completed output, and `close_agent` returned previous status, the coordinator may record Subagent Mode as supported even if the subagent says it cannot self-confirm.

## Pass / fail standard

Pass:

- `spawn_agent` returns two distinct `agent_id` values.
- `wait_agent` returns completed results for both.
- `close_agent` is called for both.
- No files are modified.

Fail:

- no `agent_id` is returned
- either result is fabricated without wait evidence
- completed agents are not closed
- the test claims OS-level background process execution

## Failure handling

If subagent tools are unavailable or thread limit remains after close/retry, use fallback to Simple Pal Mode.


