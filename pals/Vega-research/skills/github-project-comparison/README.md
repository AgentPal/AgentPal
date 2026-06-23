# github-project-comparison

运行时 Skill 入口请看 SKILL.md；README.md 仅作为人类阅读说明。


中文名：GitHub 项目对比

## 用途

比较多个 GitHub 项目的适用性、活跃度、集成难度、License、风险和推荐用途。

## 适用场景

- 评估外部 Skill 是否适合导入 AgentPal。
- 比较多个开源工具。
- 判断项目是否仍维护。
- 给合适协作对象 提供工程评估前的资料结论。

## 不适合场景

- 只凭 Star 做排名。
- 要求复制第三方源码。
- License 不明但用户要求公开打包。

## 输入信息

- 项目 URL。
- 目标用途。
- README / docs / release / issue / license 摘要。
- 最近更新时间。
- 已知风险。

## 处理流程

1. 判断项目定位和适用场景。
2. 检查 README 清晰度、文档、Release、Issue、PR 和维护信号。
3. 检查 License 和再分发边界。
4. 检查安装、API、CLI、SDK 或集成方式。
5. 标记安全、依赖和架构风险。
6. 给出推荐用途：导入、reference-only、Skill Card、逐案请从当前 contacts / registry 解析出的合适协作对象补充或不建议。

## 输出格式

```text
# GitHub 项目对比
| 项目 | 定位 | 活跃度 | 文档 | License | 集成难度 | 风险 | 推荐用途 |
|---|---|---|---|---|---|---|---|
## 最推荐
## 可参考但不建议直接接入
## 不建议
## 还需要验证
```

## 验收标准

- Star 只作为信号，不作为结论。
- License 被明确检查。
- 维护状态和 Issue / Release 被纳入判断。
- 结论能请从 contacts / registry 解析出的合适协作对象逐案补充工程判断。

## 风险边界

Vega 不复制第三方源码，不自动安装项目，不把 GitHub 项目加入 Pal 通讯录。

## 与其他 Skill / Runbook 的关系

对应 `runbooks/open-source-evaluation/github-project-evaluation.md`，可请从 contacts / registry 解析出的合适协作对象逐案补充工程可行性评估。

