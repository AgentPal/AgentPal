# Open Source Project Evaluation Example

用户请求：

```text
帮我评估一个 GitHub 开源 Skill 项目是否适合导入 AgentPal。
```

## Vega 输出示例

### License 检查

- 找到项目根目录 License。
- 检查 README 是否有额外 NOTICE 或引用要求。
- 如果无 License，建议不要复制进公开包，只保留链接和摘要。

### README / 活跃度 / Issue / Release 检查

| 维度 | 检查内容 |
|---|---|
| README | 用途是否清楚，是否有安装或执行风险 |
| 活跃度 | 最近提交、维护节奏、项目类型 |
| Issue | 未解决问题、维护者响应 |
| Release | 是否有稳定版本或变更记录 |
| 文档 | 是否说明输入输出和边界 |

### 安全风险

- 是否要求 API key、token 或账户。
- 是否包含自动下载、抓取、上传、删除、部署或绕过审批逻辑。
- 是否会保存用户私密资料。
- 是否适合改写为研究流程，而不是直接启用。

### 导入判断

| 判断 | 条件 |
|---|---|
| 正式导入 | License 清晰、风险低、确实需要，并已改写为 Vega 自有表达 |
| Skill Card | 有参考价值，但不复制源码 |
| reference-only | 可学习思路，不适合打包 |
| 不建议 | 无 License、高风险、维护差或不适配 |

### 是否适合转成 Skill Card

适合时记录来源、License、用途、风险、Vega 改写计划和最后检查时间。

