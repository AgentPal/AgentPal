# Agent Skill Resource Evaluation Example

用户请求：

```text
帮我判断这个 GitHub Skill 包能不能改造成 AgentPal Pal Pack 的能力。
```

## Vega 输出示例

### 是否是 Skill

检查：

- 是否有 `SKILL.md`。
- 是否有 README、manifest、examples、templates 或 scripts。
- 是否说明触发场景、输入、输出和边界。

### 是否是 Pal Pack

检查：

- 是否有 `PAL.md`。
- 是否有 `pal.json`。
- `pal.json.type` 是否为 `pal-pack`。
- 是否声明协作开关。

如果只是 Skill，不进入 contacts。

### License

- 记录 License 来源。
- 无 License 或协议不明时，不复制内容。
- 第三方内容不会自动继承 AgentPal MIT。

### 安全风险

- 是否有命令、脚本、依赖安装、删除、上传、部署或审批绕过。
- 是否要求 API key、账号、token 或外部服务。
- 是否保存用户资料或发送给外部 Runtime。

### 适合进入哪里

| 判断 | 位置 |
|---|---|
| 外部参考 | `imports/` + `registry/` |
| 来源卡 | `imports/research-cards/` |
| 可复用流程 | `runbooks/` |
| 多步骤流程 | `workflows/` |
| 稳定知识 | `knowledge/` |
| 长期核心能力 | `skills/`，需改写为 Vega 自有表达 |

### 是否不能进入 contacts

普通 Skill、工具、MCP、插件、模型、网页、GitHub 项目和外部 Runtime 不能进入 contacts。只有标准 Pal Pack 才能进入 Pal 通讯录。

