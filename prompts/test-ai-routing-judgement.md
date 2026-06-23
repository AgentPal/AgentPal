# Test AI Routing Judgement

Use this prompt to manually test AgentPal routing before a public release candidate.

## Rule

Do not evaluate by expected Pal identity. Evaluate by whether Mira gives a case-specific judgement, respects explicit commands, and avoids keyword-triggered Pal routing.

## Test Inputs

1. Multi-perspective A:

```text
这个项目下一版值不值得继续做？如果值得，怎么开发，怎么验收？
```

2. Multi-perspective B:

```text
帮我从产品、工程和发布质量三个角度看一下这个项目下一步怎么走。
```

3. Multi-perspective C:

```text
我不想只听技术建议，你帮我判断继续做有没有价值、工程上怎么推进、发布前怎么把关。
```

4. Explicit single Pal:

```text
/pal Atlas 帮我看下一步怎么开发。
```

5. Simple explanation:

```text
开发计划和验收计划有什么区别？
```

6. Low token:

```text
简单说一下这个项目下一步，不要多 Pal，省 token。
```

7. Codex generic:

```text
不要使用任何 Pal 的知识和流程，只用 Codex 通用能力回答：这个项目继续开发应该注意什么？
```

8. Ambiguous:

```text
这个项目我有点迷茫，你觉得下一步怎么搞？
```

## Pass Checklist

- [ ] No hard-coded semantic routing.
- [ ] No keyword-triggered Pal routing.
- [ ] Multi-perspective requests include a rationale for selected owner / consultant / reviewer Pals when used.
- [ ] Simple explanation does not force specialist handoff unless the current context needs it.
- [ ] Low-token request is respected.
- [ ] Codex generic request starts with `Codex generic answer:`.
- [ ] Explicit `/pal Atlas` is honored as direct command handling.
- [ ] Any selected owner, consultant, or reviewer is justified by context.

