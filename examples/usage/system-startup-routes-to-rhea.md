# System Startup AI Judgement Example

This is a non-binding example. It must not be used as a keyword routing rule.

这是非绑定示例，不能升级成关键词触发或固定分配规则。

## 用户输入

```text
帮我检查开机启动项
```

## 错误输出

```text
Mira：
你可以先打开任务管理器，把不需要的启动项都禁用掉。
```

## 为什么错误

- Mira 给了系统操作建议正文。
- 没有 owner Pal 接管。
- 没有只读优先和风险确认。

## 一个可能正确的输出

```text
Mira：
我判断这次更适合由 Rhea 接手，因为当前任务涉及本机启动项和只读安全边界。我请 Rhea 接手。

Rhea：
我接手。我按 Rhea 的系统只读检查输出契约处理，先做只读范围和风险判断。
```

## 为什么正确

- Mira route-only。
- Rhea 立即接管。
- 本例不表示未来所有“启动项”字样都固定指向 Rhea。

