# Resource Ingestion Protocol

外部资源放入 `imports/`。

处理流程必须包含：

1. Detect：识别资源类型。不要只看目录名，要结合 README、SKILL.md、manifest 和文件结构。
2. Inspect：阅读入口文件和依赖说明，确认输入、输出、权限和运行方式。
3. Summarize：用短句说明它能做什么、不能做什么、适合什么任务。
4. Classify：分类到 Skill、Knowledge、Persona、Tool、Pal Pack 候选或 Raw。
5. Index：写入对应 `registry/*.index.md`，必要时更新 `RESOURCE_INDEX.md`。
6. Risk Check：标记危险命令、网络访问、密钥需求、许可证、过期风险和冲突。
7. Promote：如果资源稳定可复用，建议升级为正式 Skill、Runbook、Workflow、Knowledge Card；如果它是标准 Pal Pack，再进入通讯录候选。

默认不修改外部包本体。优先生成 sidecar 索引。

普通 Skill、工具、资料库和人设包不能直接进入 Pal 通讯录。

