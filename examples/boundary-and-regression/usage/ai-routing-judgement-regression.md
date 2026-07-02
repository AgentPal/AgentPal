<!-- Future design only. Not active in AgentPal v0.1 runtime. / 未来设计，仅作规划参考，不属于 AgentPal v0.1 当前运行行为。 -->

# AI Routing Judgement Regression Example

This is a non-binding example. It demonstrates possible response shapes, not route rules.

这是非绑定示例，只展示可能的回答形态，不是固定路由。

## Complex Multi-Perspective Request

User:

```text
我不想只听技术建议，你帮我判断继续做有没有价值、工程上怎么推进、发布前怎么把关。
```

Future-design response shape only, not active in AgentPal v0.1:

```text
Mira：
如果未来启用 Deep Conductor 或外部多 Agent 编排，这类任务可以拆成价值、工程推进和发布把关三个独立视角。当前 v0.1 使用 Simple Pal Mode only，所以我会先选择一个 owner Pal 接手，必要时在同一回复中标注需要哪些补充视角。
```

One valid response shape when Simple Pal Mode is enough:

```text
Mira：
我判断这次先用 Simple Pal Mode 处理，因为当前缺少项目材料。我先选择一个 owner Pal 接手，并列出需要补充的信息。
```

## Simple Explanation Request

User:

```text
开发计划和验收计划有什么区别？
```

Valid response shape:

```text
Mira：
开发计划说明怎么把东西做出来；验收计划说明怎么判断它是否真的达标。这个问题是概念解释，直接由当前 Pal 回答即可。
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

