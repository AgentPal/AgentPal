# GitHub Project Evaluation Runbook

这个 Runbook 用于评估一个 GitHub 项目是否适合导入 AgentPal、转成 Skill Card、只做 reference-only，或请从 contacts / registry 解析出的合适协作对象逐案补充工程评估。

## Required Context

- 项目 URL。
- 用户想解决的问题。
- 目标导入方式：知识、Skill、Runbook、工具、MCP、Pal Pack 候选或参考资料。
- 是否准备公开发布。

## Evaluation Steps

1. 检查项目定位和 README 清晰度。
2. 检查 License、NOTICE 和再分发边界。
3. 检查最近提交、Release、Issue、PR 和维护状态。
4. 检查文档、示例、测试、CI 和安装难度。
5. 检查安全风险、权限要求、外部服务和数据上传。
6. 判断与 AgentPal 的关系：正式 Skill、知识卡、Runbook、Skill Card、reference-only 或不建议。
7. 标注需要合适协作对象判断的工程问题。

## Output

```text
## 项目定位
## 来源与时间
## License 结论
## 维护活跃度
## 文档与接入难度
## 安全与隐私风险
## 推荐处理方式
## 是否需要合适协作对象继续评估
## 不确定项
```

## Evidence Requirements

- 项目链接。
- License 来源。
- 最近更新时间或 Release 信息。
- Issue / PR / README / docs 摘要。
- 风险来源。
- 访问时间和判断适用范围。

## Boundary

不复制第三方源码或 README 原文。不把 GitHub 项目加入 contacts。Star 只是信号，不是结论。

