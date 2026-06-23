# Research Tool Shortlist Example

用户请求：

```text
帮我从一批 AI research tools 中筛选适合 AgentPal 的工具。
```

## Vega 输出示例

### 初筛规则

- 工具是否解决 AgentPal 当前研究任务。
- 是否仍维护。
- 是否有清晰文档。
- 是否需要账号、API key、外部上传或付费数据。
- 是否能本地使用或只作为外部服务。
- 是否有明确 License。

### License 检查

| 状态 | 处理方式 |
|---|---|
| MIT / Apache-2.0 / BSD / ISC | 可考虑 public-card 或参考改写 |
| GPL / AGPL | 谨慎，避免混入 MIT 发布包 |
| CC-BY / CC-BY-SA | 注意署名和共享要求 |
| No License / Unknown | 不复制内容，只能 reference-only |

### 隐私风险

- 是否上传用户文件。
- 是否保存用户查询。
- 是否需要登录账号。
- 是否处理公司内部资料。
- 是否会把资料发给外部模型或服务。

### 是否适合导入

```text
## 推荐导入
## 只做 public-card
## 只做 reference-only
## 需要合适协作对象 / 用户进一步确认
## 拒绝
```

### 是否只做 reference-only

如果工具 License 不清、隐私风险高、维护状态差或依赖外部服务，Vega 应只保留链接和摘要，不复制资料。

