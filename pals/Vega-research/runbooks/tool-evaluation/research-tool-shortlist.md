# Research Tool Shortlist Runbook

这个 Runbook 用于从 awesome list、工具目录、GitHub 搜索结果或用户提供的一批工具中筛选 Research Pal 可参考的候选。

## Key Principle

Awesome list 只能作为候选线索，不等于推荐，不等于安全，也不等于 License 清楚。

## Required Inputs

- 工具列表或来源目录。
- 用户要解决的研究问题。
- 是否准备公开发布。
- 是否涉及用户资料、私密文件、账号、API key 或外部上传。

## Screening Steps

1. 去重并识别工具类型：搜索、文献、引用、PDF、数据分析、知识库、Agent、MCP、插件。
2. 检查项目主页、README、License、更新时间、Release、Issue 和维护状态。
3. 检查是否需要账号、API key、上传资料、联网抓取或外部写入。
4. 检查隐私和数据保留风险。
5. 检查是否适合本地使用，还是只能作为外部服务。
6. 判断是否适合 AgentPal：reference-only、public-card、runbook inspiration、knowledge-card、reject。
7. 写入 `registry/resource-map.md` 的 sidecar 索引。

## Output Format

```text
| 工具 | 类型 | License | 维护状态 | 隐私风险 | 适配方式 | 建议 |
|---|---|---|---|---|---|---|
```

## Decision Labels

- `reference-only`：只保留链接和摘要。
- `public-card`：可创建公开来源卡。
- `convert-to-runbook`：方法可改写为 Vega 自有流程。
- `convert-to-knowledge-card`：方法可沉淀为知识卡。
- `reject`：License、隐私、安全或质量风险不可接受。

## Boundary

Vega 不安装工具，不调用外部服务，不上传用户资料，不把工具或外部 Runtime 加入 contacts。

