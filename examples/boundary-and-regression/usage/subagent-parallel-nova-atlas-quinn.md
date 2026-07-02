<!-- Future design only. Not active in AgentPal v0.1 runtime. / 未来设计，仅作规划参考，不属于 AgentPal v0.1 当前运行行为。 -->

# Subagent Parallel Non-Binding Example

This is a non-binding example. It must not be used as a keyword routing rule.

这是非绑定示例，不能升级成关键词触发或固定分配规则。

## User Input

```text
这个项目下一版值不值得继续做？如果值得，怎么开发，怎么验收？
```

## Mira Judgement

Mira does not use a fixed phrase trigger. In AgentPal v0.1.0-rc.1, Mira may decide case-by-case whether bounded Simple Pal Mode perspectives or a Task Package are useful. Codex Subagent Mode is future design only.

One valid judgement:

```text
Mira：
我判断这次需要多个视角，但 v0.1 当前不启动 Subagent Mode。我会用 Simple Pal Mode 组织 owner / consultant / reviewer 视角，或整理成未来可执行的任务包。
```

## Possible Future Subagents

The selected Pal set is non-binding and case-specific. A future design run may include:

- one owner Pal for the main decision
- one consultant Pal for feasibility
- one reviewer Pal for evidence and release risk

## Required Files

Each selected subagent reads its own Pal identity, `SKILL.md`, `pal.json`, Response Fingerprint, and Output Contract.

## Expected Result

- Each selected Pal stays inside its own output contract.
- Mira reports what each Pal concluded, where they agree, where they differ, evidence gaps, and final recommendation.
- In v0.1, Mira does not record `agent_id`, wait status, or close status because no child workflow is started.

## Fallback If Unavailable

Use Simple Pal Mode with clearly labeled Pal sections and say the Pals were not independent subagent threads.

Future Subagent Mode must never be keyword-triggered. It is not active in AgentPal v0.1.0-rc.1.


