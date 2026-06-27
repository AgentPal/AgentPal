<!-- Future design only. Not active in AgentPal v0.1 runtime. / 未来设计，仅作规划参考，不属于 AgentPal v0.1 当前运行行为。 -->

# Subagent Single Owner Atlas Self-Test

## Input

```text
请 Atlas 判断这个开发任务下一步怎么做。
```

## Expected route

- Mira chooses Atlas as owner Pal.
- Atlas answers in Simple Pal Mode.
- Do not spawn, wait, or close child workflows in AgentPal v0.1.0-rc.1.
- Do not record or invent `agent_id`, wait status, close status, or `closed: true`.

## Required Atlas assets

- `official/pals/Atlas-developer/PAL.md`
- `official/pals/Atlas-developer/SKILL.md`
- `official/pals/Atlas-developer/pal.json`
- `workspace/resources/response-fingerprints/Atlas.md`
- `official/pals/Atlas-developer/core/output-contract.md`

## Expected output

Atlas result includes engineering state, file / directory scope, development phases, acceptance command or criteria, risks, and next Codex task.

Atlas must not write `agent_id` evidence in current v0.1.0-rc.1 task handling.

## Fail if

- Mira writes the engineering plan herself.
- Atlas omits required assets.
- The result claims a child workflow was spawned.
- The result claims OS-level background process execution.
- Atlas provides product value or final release gate as if it were Nova or Quinn.


