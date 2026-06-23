<!-- Future design only. Not active in AgentPal v0.1 runtime. / 未来设计，仅作规划参考，不属于 AgentPal v0.1 当前运行行为。 -->

# Subagent Parallel Non-Binding Example

This is a non-binding example. It must not be used as a keyword routing rule.

这是非绑定示例，不能升级成关键词触发或固定分配规则。

## User Input

```text
这个项目下一版值不值得继续做？如果值得，怎么开发，怎么验收？
```

## Mira Judgement

Mira does not use a fixed phrase trigger. Mira decides case-by-case whether independent Pal perspectives and Codex Subagent Mode are useful.

One valid judgement:

```text
Mira：
我判断这次适合多 Pal 并行，因为你同时要取舍、执行拆分和验收证据，而且当前环境支持 Codex Subagent Mode。我会用 Subagent Mode 分别收集几个视角，再汇总。
```

## Possible Subagents

The selected Pal set is non-binding and case-specific. A valid run may include:

- one owner Pal for the main decision
- one consultant Pal for feasibility
- one reviewer Pal for evidence and release risk

## Required Files

Each selected subagent reads its own Pal identity, `SKILL.md`, `pal.json`, Response Fingerprint, and Output Contract.

## Expected Result

- Each selected Pal stays inside its own output contract.
- Mira reports what each Pal concluded, where they agree, where they differ, evidence gaps, and final recommendation.
- Mira records runtime evidence: each `agent_id`, wait status, close status, and whether completed agents were closed.

## Fallback If Unavailable

Use Simple Pal Mode with clearly labeled Pal sections and say the Pals were not independent subagent threads.

Subagent Mode is subagent-first for authorized owned tasks, not keyword-triggered.


