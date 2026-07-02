<!-- Future design only. Not active in AgentPal v0.1 runtime. / 未来设计，仅作规划参考，不属于 AgentPal v0.1 当前运行行为。 -->

# AI Routing Judgement Example

This is a non-binding example. It must not be used as a keyword routing rule.

这是非绑定示例，不能升级成关键词触发或固定分配规则。

## User

```text
这个项目下一步怎么推进，能不能给我一个专业建议？
```

## Expected Behaviour

Mira does not look for a fixed phrase or route table. Mira applies AI routing judgement case-by-case.

Possible factors:

- Is the user asking for product direction, engineering execution, risk review, or a combined decision?
- Is there enough project context to choose an owner?
- Would one owner Pal be enough, or would same-response consultation help?
- If future orchestration would help, should Mira describe it only as future design instead of active v0.1 execution?

## One Valid Response Shape

```text
Mira：我判断这次属于当前 contacts / registry 中某个 owner Pal 的职责范围，需要先由 owner Pal 接手。我请合适的 Pal 接手。

<Owner Pal>：我接手。我会按自己的输出契约处理：先完成 owner 范围内的判断，再决定是否需要 consultant 或 reviewer 补充其它视角。
```

This does not mean similar future requests must route to any fixed Pal. If the same sentence appears in a different context, Mira may select a different owner. If the user explicitly calls `/pal Name`, explicit command handling applies.

