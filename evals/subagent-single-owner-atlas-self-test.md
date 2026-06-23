<!-- Future design only. Not active in AgentPal v0.1 runtime. / 未来设计，仅作规划参考，不属于 AgentPal v0.1 当前运行行为。 -->

# Subagent Single Owner Atlas Self-Test

## Input

```text
请 Atlas 判断这个开发任务下一步怎么做。
```

## Expected route

- Mira chooses Atlas as owner Pal.
- Use Codex Subagent Mode only if independent Atlas judgment is useful and tools are available.
- Spawn Atlas subagent.
- Wait result.
- Close completed agent.
- Coordinator records `agent_id`, wait status, close status, and `closed: true`.

## Required Atlas assets

- `pals/Atlas-developer/PAL.md`
- `pals/Atlas-developer/SKILL.md`
- `pals/Atlas-developer/pal.json`
- `response-fingerprints/Atlas.md`
- `pals/Atlas-developer/core/output-contract.md`

## Expected output

Atlas result includes engineering state, file / directory scope, development phases, acceptance command or criteria, risks, and next Codex task.

Atlas may write `agent_id: coordinator_fills_after_spawn`; this is acceptable because the coordinator owns runtime evidence.

## Fail if

- Mira writes the engineering plan herself.
- Atlas omits required assets.
- Completed agent is not closed.
- The result claims OS-level background process execution.
- Atlas provides product value or final release gate as if it were Nova or Quinn.


