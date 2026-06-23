# Codex Multi Thread Prompt Test

## 用户请求

我正在开发 AgentPal 主标准仓库，想让 Codex 帮我增加一个 Pal Pack 发布前检查能力，用于检查一个 Pal Pack 是否具备 SKILL.md、PAL.md、AGENTS.md、pal.json、协作开关、License、隐私边界、外部资源导入说明和 Runtime/Model 路由能力。请 Atlas 帮我拆成多线程开发任务。

## 协作对象判断

这是开发任务，可以进入开发，但必须限定范围。

当前目标不是发布完整 CLI，也不是修改 AgentPal 标准本身，而是为 Pal Pack 发布前检查能力建立一个最小可用闭环：检查项清楚、输入输出清楚、验收标准清楚、不会误提交私人记忆或第三方资源。

## 当前目标

为 AgentPal 主标准仓库增加一个 Pal Pack 发布前检查能力，用于帮助用户检查 Pal Pack 是否具备基础入口、manifest、协作开关、License、隐私边界、外部资源导入说明和 Runtime/Model 路由能力。

## 不做事项

- 不开发复杂 CLI。
- 不做桌面 App、聊天 UI 或 Pal Hub。
- 不修改 `.git` 或仓库结构。
- 不复制第三方 Skill 源码。
- 不把普通 Skill 或外部 Runtime 加入通讯录。
- 不做自动修复、自动删除、自动安装或 git push。

## 推荐执行策略

使用 4 个 Codex 线程：

1. 规则和上下文线程。
2. 最小检查实现或文档入口线程。
3. 测试计划和安全边界线程。
4. 最终复验线程。

Atlas 负责拆任务和复验。Codex 负责在各自线程中修改文件并返回 evidence。

## 线程 1：发布检查规则与 Context Pack

目标：
梳理 Pal Pack 发布前检查能力的检查范围，并生成执行层可用 Context Pack。

必读文档：
- `README.md`
- `zh-CN/README.md`
- `zh-CN/docs/12-Pal-Pack发布检查清单.md`
- `zh-CN/schema/pal.schema.json`
- `zh-CN/templates/minimal-pal-pack/`
- `zh-CN/templates/standard-pal-pack/`

修改范围：
- 发布检查相关 docs 或 tools 说明文件。
- 不修改 schema 语义。

禁止事项：
- 不复制维护者私有资料。
- 不修改模板目录结构。
- 不新增复杂 CLI。
- 不移动、删除或复制 `.git`。

验收标准：
- 检查项覆盖入口文件、`pal.json`、协作开关、License、隐私边界、imports、Runtime/Model 路由。
- Context Pack 只包含必要文档，不倾倒全仓库。
- 明确哪些检查是必须项，哪些是建议项。

建议模型：
强模型。

推理强度：
high。

任务长度：
中。

完成报告格式：
- 完成内容。
- 修改文件。
- 检查项摘要。
- 未确定问题。
- 需要人工确认。

## 线程 2：最小检查入口

目标：
建立一个最小发布检查入口，可以是文档化检查流程或轻量占位工具说明。

必读文档：
- 线程 1 输出。
- `zh-CN/schema/pal.schema.json`
- `zh-CN/templates/minimal-pal-pack/`
- `zh-CN/templates/standard-pal-pack/`

修改范围：
- `tools/`
- `zh-CN/docs/`
- 相关 README。

禁止事项：
- 不引入外部依赖。
- 不安装包。
- 不做自动修复。
- 不删除文件。

验收标准：
- 用户知道如何检查 `SKILL.md`、`PAL.md`、`AGENTS.md`、`pal.json`。
- 用户知道如何检查协作开关和 Runtime/Model 路由字段。
- 用户知道如何处理 imports 和第三方 License。

建议模型：
中等模型。

推理强度：
medium。

任务长度：
中。

完成报告格式：
- 完成内容。
- 修改文件。
- 验证方式。
- 未覆盖检查。
- 风险。

## 线程 3：测试计划与安全边界

目标：
为发布检查能力补充测试计划、安全边界和 evidence 要求。

必读文档：
- `zh-CN/docs/12-Pal-Pack发布检查清单.md`
- `.gitignore`
- `LICENSE`
- `CONTRIBUTING.md`

修改范围：
- 发布检查相关测试说明、验收说明或 eval 文档。

禁止事项：
- 不运行真实删除、移动、发布或 push。
- 不提交私人 memory、reports、state。
- 不复制第三方 Skill 源码。

验收标准：
- 有手工测试路径。
- 有 JSON parse 和 schema 检查建议。
- 有第三方 License 与 imports 检查项。
- 有私人记忆和运行时状态排除检查项。

建议模型：
中等模型。

推理强度：
medium。

任务长度：
短到中。

完成报告格式：
- 测试计划。
- 安全边界。
- evidence 要求。
- 需要人工复验。

## 线程 4：最终复验

目标：
汇总前三个线程结果，检查发布前检查能力是否形成可用闭环。

必读文档：
- 三个线程完成报告。
- changed files。
- 相关 README、docs、tools、evals。

修改范围：
- 只修正明显冲突、重复或缺口。
- 不做大范围重写。

禁止事项：
- 不接受无 evidence 的“完成”。
- 不复制内部资料到公开仓库。
- 不新增无关功能。

验收标准：
- 检查能力可被用户理解和执行。
- 文档、检查入口和测试计划一致。
- 没有架构越界。
- 没有安全边界缺口。

建议模型：
强模型。

推理强度：
high。

任务长度：
短。

完成报告格式：
- 复验结论。
- 支持完成的 evidence。
- 缺失 evidence。
- 风险或返工项。
- 是否建议进入下一轮。

## 全局 Evidence 要求

每个线程必须返回：

- changed files。
- 关键修改摘要。
- 验证结果或未验证原因。
- 是否触碰禁止事项。
- 剩余风险。

## 风险点

- 把发布前检查做成复杂 CLI。
- 修改 schema 导致模板不兼容。
- 把维护者私有资料复制到公开仓库。
- 忽略第三方 License 和 imports 边界。
- 忽略私人 memory、reports、state 的发布风险。

## Atlas 如何复验

Atlas 使用 `context-engineering` 检查上下文是否合适，使用 `test-plan-writer` 检查测试计划，使用 `architecture-review` 检查标准边界，使用 `security-and-hardening` 检查高风险动作，最后用 `execution-evidence-review` 对照 evidence 判断是否完成。

## 需要用户确认

- 是否允许新增轻量检查脚本。
- 检查入口放在 `tools/` 还是 `docs/`。
- 是否只检查 `zh-CN` 标准包，还是支持任意 Pal Pack 目录。
- 是否需要 JSON 输出。

