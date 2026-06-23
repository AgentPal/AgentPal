# Usage Example: Claude Code non-Pal runtime Research

## User Request

```text
请让 Vega 调研：Claude Code 是否适合接入 AgentPal，作为 the selected implementation collaborator can调度的外部开发 Agent？
```

## Vega Style Answer

### Conclusion

Claude Code 可以作为 AgentPal 的外部开发 Agent / Runtime 候选，但当前不应加入 Pal 通讯录。更合适的方式是：Vega 负责调研来源和边界，合适实现协作对象负责生成有边界的开发 handoff，并在 Claude Code 返回后复验 evidence。

### Evidence

- 官方文档说明 Claude Code 是面向代码库的 agentic coding tool，可读取代码库、编辑文件、运行命令并与开发工具集成。
- 官方文档说明 Claude Code 支持 MCP、Agent SDK、subagents、hooks、skills 和 settings / policy 相关控制面。
- 官方 MCP 文档提醒外部 server 需要信任检查，并存在 prompt injection 风险。

### Source Status

Primary source status: verified from Anthropic official Claude Code documentation on 2026-06-22.

Pending: local version check, account/provider availability, SDK behavior test, target repo permission behavior and one controlled implementation collaborator handoff trial.

### Recommendation

让合适实现协作对象先做一个低风险 Claude Code handoff trial：限制文件范围，明确验收标准，要求变更清单、验证结果、失败说明和未完成项。不要把 Claude Code、MCP、plugin、skill 或外部 Runtime 写入 `contacts/`。

### Next Step

将 `examples/real-research/claude-code-as-external-agent/04-developer-pal-handoff.md` 逐案请从 contacts / registry 解析出的合适协作对象接手生成一份真实开发任务试用包。


