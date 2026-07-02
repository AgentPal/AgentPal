<!-- Future design only. Not active in AgentPal v0.1 runtime. / 未来设计，仅作规划参考，不属于 AgentPal v0.1 当前运行行为。 -->

# Subagent Rhea Read-Only System Task

## User input

```text
帮我检查系统启动项都有哪些，会不会影响开机速度
```

## Mira routing decision in v0.1

Mira uses AI routing judgement case-by-case. If Mira selects Rhea in AgentPal v0.1.0-rc.1, Rhea answers through Simple Pal Mode with a read-only boundary. Mira does not start Codex Subagent Mode.

## Current Pal handling

- Rhea as owner Pal in Simple Pal Mode

## Required files Rhea reads on demand

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

## Future-design note

Future external orchestration may run Rhea as an independent workflow, but AgentPal v0.1 does not claim an independent subagent ran.


