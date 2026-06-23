<!-- Future design only. Not active in AgentPal v0.1 runtime. / 未来设计，仅作规划参考，不属于 AgentPal v0.1 当前运行行为。 -->

# AI Routing Judgement Regression Example

This is a non-binding example. It demonstrates possible response shapes, not route rules.

这是非绑定示例，只展示可能的回答形态，不是固定路由。

## Complex Multi-Perspective Request

User:

```text
我不想只听技术建议，你帮我判断继续做有没有价值、工程上怎么推进、发布前怎么把关。
```

One valid response shape when Subagent Mode is available and worth the cost:

```text
Mira：
我判断这次适合用 Codex Subagent Mode，因为你明确要求价值、工程推进和发布把关三个相互独立的视角，分开判断能减少互相覆盖。我会让逐案选定的 Pal 分别给结论，再汇总差异。
```

One valid response shape when Simple Pal Mode is enough:

```text
Mira：
我判断这次先用 Simple Pal Mode 更合适，因为当前缺少项目材料，直接并行开多个 subagent 成本高且可能空转。我先给一个轻量判断，并列出需要补充的信息。
```

## Simple Explanation Request

User:

```text
开发计划和验收计划有什么区别？
```

Valid response shape:

```text
Mira：
开发计划说明怎么把东西做出来；验收计划说明怎么判断它是否真的达标。这个问题是概念解释，不需要开 Subagent Mode。
```

## Explicit Codex Generic Request

User:

```text
不要使用任何 Pal 的知识和流程，只用 Codex 通用能力回答：这个项目继续开发应该注意什么？
```

Valid response shape:

```text
Codex generic answer:
继续开发前，先确认目标用户、最小范围、技术风险、验收标准和回滚方案。
```

## Explicit Pal Request

User:

```text
/pal Atlas 帮我看下一步怎么开发。
```

Valid response shape:

```text
Atlas：
我接手。我会按 Atlas 的开发边界处理：先看目标、范围和验收，再判断是否需要执行层任务包。
```

Explicit Pal calls are deterministic command handling. They are not semantic routing.

