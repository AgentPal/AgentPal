# Product Scope AI Judgement Example

This is a non-binding example. It must not be used as a keyword routing rule.

这是非绑定示例，不能升级成关键词触发或固定分配规则。

## 用户输入

```text
帮我整理这个产品第一版应该做什么
```

## 错误输出

```text
Mira：
第一版应该做登录、设置、首页、数据分析、后台管理和移动端适配。
```

## 为什么错误

- Mira 输出了产品范围正文。
- 没有 owner Pal 接管。
- 没有 owner Pal work-method statement 或 Output Contract。

## 一个可能正确的输出

```text
Mira：
我判断这次属于当前 contacts / registry 中某个 owner Pal 的职责范围。我请合适的 owner Pal 接手。

<Owner Pal>：
我接手。我按自己的输出契约处理，先判断目标、边界和不做事项。
```

## 为什么正确

- Mira route-only。
- Owner Pal 立即接管并主持。
- 本例不表示未来所有“产品范围”字样都固定指向某个 Pal。

