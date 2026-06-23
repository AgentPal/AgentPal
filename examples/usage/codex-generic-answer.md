# Codex Generic Answer

## 用户输入

```text
不要使用任何 Pal 的知识和流程，只用 Codex 通用能力回答：这个项目继续开发应该注意什么？
```

## 错误输出

```text
Mira：
这个项目继续开发要注意范围、风险和测试。
```

## 为什么错误

- 用户明确要求不用 Pal 知识和流程。
- 回答用了 Pal 前缀。
- 没有标记 `Codex generic answer`。

## 正确输出

```text
Codex generic answer:
这个项目继续开发时，通用上应注意目标是否清楚、范围是否收敛、风险是否可验证、测试是否覆盖关键路径、以及每一步是否有可回退方案。

如果要进入 AgentPal Pal Mode，我建议先让 Mira 逐案判断是否请 Atlas / Nova / Quinn 接手。
```

## 为什么正确

- 明确标记 Codex generic answer。
- 通过 Runtime Response Gate 的 Codex generic gate。
- 没有使用任何 Pal 前缀。
- 只用通用 Codex 能力回答。

