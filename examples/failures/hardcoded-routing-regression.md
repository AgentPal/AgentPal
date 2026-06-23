# Hardcoded Routing Regression

This is a failure example, not a routing rule.

## Bad user/assistant exchange

User:

```text
开发计划和验收计划有什么区别？
```

Assistant:

```text
Mira：因为出现了“开发”和“验收”，必须让 Atlas 和 Quinn 参与。
```

## Why it is wrong

This turns keywords into fixed Pal routing. AgentPal uses AI routing judgement case-by-case. Simple explanation tasks usually do not need specialist handoff.

## Correct behavior

Mira can answer only if the request is Mira-owned, or explain why an owner Pal is useful for the current context. The reason must not be keyword matching.

## Related eval

- `evals/ai-routing-judgement-regression.md`
- `evals/ai-routing-judgement-no-hardcode-self-test.md`

## Related protocol

- `orchestration/ai-routing-judgement-protocol.md`
- `orchestration/runtime-response-gate.md`

