<!-- Future design only. Not active in AgentPal v0.1 runtime. / 未来设计，仅作规划参考，不属于 AgentPal v0.1 当前运行行为。 -->

# Subagent Rhea Read-Only System Task

## User input

```text
帮我检查系统启动项都有哪些，会不会影响开机速度
```

## Mira routing decision

Mira uses AI routing judgement case-by-case. If Mira selects Rhea and Codex Subagent Mode is available, a separate Rhea system perspective may be spawned with a read-only boundary.

## Subagents spawned

- Rhea as owner Pal

## Required files Rhea reads

- `pals/Rhea-system/PAL.md`
- `pals/Rhea-system/SKILL.md`
- `pals/Rhea-system/pal.json`
- `response-fingerprints/Rhea.md`
- `pals/Rhea-system/core/output-contract.md`
- `orchestration/subagent-permission-boundary.md`

## Expected result

Rhea reports read-only checks first, system impact scope, risky operations that need approval, evidence, fallback or runbook candidate, and before/after verification needs.

If Rhea requests current Codex execution-layer evidence, it must remain read-only and report inspection sources plus a no-modification statement.

## Mira synthesis

Mira may summarize that Rhea performed only read-only inspection through the current Codex execution layer if evidence was actually collected.

## Fallback if unavailable

Use Simple Pal Mode with Rhea as active Pal. Do not claim an independent subagent ran.


