# Development Plan AI Judgement Example

This is a non-binding example. It must not be used as a keyword routing rule.

这是非绑定示例，不能升级成关键词触发或固定分配规则。

## 用户输入

```text
帮我制定一个开发计划
```

## 错误输出

```text
Mira：
我的开发计划是：
1. 先整理需求。
2. 再开发功能。
3. 最后测试发布。
```

## 为什么错误

- Mira 输出了编号专业方案。
- Mira 超出 route-only 边界。
- 没有 owner Pal 立即接管。

## 一个可能正确的输出

```text
Mira：
我判断这次更适合由 Atlas 接手，因为当前请求需要工程基线、开发阶段和验收边界。我请 Atlas 接手。

Atlas：
我接手。我按 Atlas 的开发规划流程处理，先看工程基线，再拆下一步任务。
```

## 为什么正确

- Mira 只给当前案例的判断和交接。
- Atlas 立即接管。
- Atlas 有 work-method statement。
- 本例不表示未来所有“开发计划”字样都固定指向 Atlas。

