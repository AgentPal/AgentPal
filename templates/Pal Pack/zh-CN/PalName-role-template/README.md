# PalName-role-template

这是 AgentPal 中文 Pal Pack 标准模板。开发者可以复制本目录，替换其中的 `PalName`、`pal-id`、`role`、`domain` 等占位信息，创建一个新的内嵌 Pal Pack。

核心原则：

```text
AgentPal 主体负责系统层。
单个 Pal Pack 只负责专业层。
```

更具体地说：

- AgentPal 主体负责中央 roster、runtime、models、plugins、orchestration、templates 和 project binding。
- 单个 Pal Pack 负责身份、语气、专业知识、技能、流程、学习、输出标准、示例、自测和 public-safe 占位。

不要把单个 Pal 写成独立项目、Agent Runtime、工具集合、固定路由表，或某个外部项目绑定目录。

## 适合谁使用

这个模板适合：

- 为 AgentPal 增加一个新的专业 Pal。
- 把一组专业知识、Skills、工作流程和输出标准整理成可复用 Pal Pack。
- 创建可公开发布的 Pal Pack 初始骨架。
- 给 Codex、Claude Code 或其它 Markdown/JSON-capable Runtime 提供可读取的 Pal 工作资产。

这个模板不适合：

- 创建 Agent Runtime。
- 创建多 Agent 执行系统。
- 创建桌面 App、Web App、daemon、service 或 installer。
- 存放真实用户记忆、私有项目状态、密钥、token、内部报告或本机路径。

## 快速创建一个 Pal

1. 复制本目录：

   ```text
   PalName-role-template/
   ```

2. 将目录改名为：

   ```text
   PalName-role/
   ```

   示例：

   ```text
   Atlas-developer
   Nova-product
   Morgan-document
   ```

3. 修改根文件中的占位信息：

   - `PAL.md`
   - `AGENTS.md`
   - `SKILL.md`
   - `pal.json`
   - `README.md`

4. 修改 `identity/` 和 `core/` 中的身份、边界、输出契约和工作协议。

5. 为这个 Pal 添加最小知识、技能、自测和 public-safe 占位。

6. 只有当 Pal Pack 已经完整、公开安全、且通过维护者检查后，才把它加入 AgentPal `workspace/organization/contacts/`。

## 根目录标准结构

推荐结构：

```text
PalName-role/
  README.md
  PAL.md
  AGENTS.md
  SKILL.md
  pal.json

  identity/
    persona.md
    voice.md
    boundaries.md

  core/
    output-contract.md
    collaboration-protocol.md
    memory-protocol.md
    runtime-boundary.md

  knowledge/
    index.md
    domain-principles.md

  skills/
    index.md
    example-skill/
      SKILL.md
      README.md

  workflows/
    index.md
    lifecycle/
      README.md

  runbooks/
    index.md
    basic-check.md

  learning/
    README.md
    knowledge-gaps.md
    repeated-tasks.md
    skill-candidates.md
    runbook-candidates.md
    workflow-candidates.md

  evals/
    README.md
    pal-self-test.md

  examples/
    README.md
    usage-example.md

  memory/
    README.md

  state/
    README.md

  reports/
    README.md
```

最小可用结构：

```text
PalName-role/
  README.md
  PAL.md
  AGENTS.md
  SKILL.md
  pal.json

  identity/
  core/
  knowledge/
  skills/
  learning/
```

## 根文件说明

| 文件 | 是否必需 | 开发者需要写什么 | 不应该写什么 |
| --- | ---: | --- | --- |
| `PAL.md` | 必需 | Pal 的身份、职责、边界、语气、协作原则和不能做什么。 | 不写固定路由表，不写“某类任务必须交给某 Pal”。 |
| `AGENTS.md` | 必需 | Runtime 进入本 Pal 目录时的读取顺序、工作规则、风险边界和输出要求。 | 不重复 AgentPal 全局 central roster / runtime 逻辑。 |
| `SKILL.md` | 必需 | 作为 Pal Pack 入口，说明何时使用、读取哪些文件、如何输出。 | 不把 Pal 降级成单一小工具 Skill。 |
| `pal.json` | 必需 | 机器可读元数据，例如 `id`、`display_name`、`directory_name`、`aliases`、`role`、`capabilities`、`collaboration`。 | 不写 `domain_map`、固定 owner、task 到 Pal 的硬编码路由。 |
| `README.md` | 建议 | 给人看的说明：这个 Pal 是谁，适合什么，怎么 `/pal Name` 调用，如何维护。 | 不写内部开发流水账、本机路径、私有数据或过期标准。 |

## `identity/`

`identity/` 负责“这个 Pal 像谁”。

| 文件 | 用途 |
| --- | --- |
| `persona.md` | Pal 的人格、角色气质和专业姿态。 |
| `voice.md` | 说话方式，例如简短、严谨、温和、直接、是否多问问题。 |
| `boundaries.md` | 身份边界：这个 Pal 不做什么，什么情况必须交给其它层处理。 |

可选扩展：

- `relationship.md`：说明 Pal 与用户的关系，例如顾问、审查者、开发伙伴、写作助手。
- `user-addressing.md`：说明如何称呼用户，如何处理中文和英文语境。

## `core/`

`core/` 负责“这个 Pal 怎么工作”。这是 Pal Pack 最重要的目录之一。

| 文件 | 用途 |
| --- | --- |
| `output-contract.md` | 输出契约：本 Pal 回答时应包含哪些结构、证据和收口方式。 |
| `collaboration-protocol.md` | 协作边界：可以如何咨询、交接或请求 review，但不写死路由。 |
| `memory-protocol.md` | 记忆边界：什么可以成为候选记忆，什么绝不能保存。 |
| `runtime-boundary.md` | Runtime 边界：Pal 不直接执行文件修改、命令、发布或高风险操作。 |

开发者可以按需要增加：

- `task-loop.md`
- `verification-protocol.md`
- `reporting-protocol.md`
- `learning-protocol.md`
- `risk-protocol.md`

不同 Pal 的 `output-contract.md` 应体现自己的专业输出。例如：

- 开发 Pal：工程状态、文件范围、开发阶段、验收命令、下一步 Runtime 任务。
- 产品 Pal：用户场景、问题定义、范围切片、Must / Should / Won't、开发前澄清问题。
- 质量 Pal：检查范围、证据、风险、结论、阻断项、剩余不确定性。
- 写作 Pal：受众、语气、结构、版本差异、最终文案。

## `knowledge/`

`knowledge/` 是专业知识库，不是运行状态，也不是用户记忆。

推荐内容：

- `index.md`：知识索引。
- `domain-principles.md`：领域原则。
- `domain/`：稳定领域知识。
- `references/`：可复用参考资料。
- `checklists/`：专业检查清单。
- `patterns/`：常见模式和经验总结。
- `glossary.md`：术语表。

可以放：

- 稳定专业知识。
- 可公开的检查清单。
- 方法论说明。
- 术语和模式总结。

不可以放：

- 用户真实隐私。
- 临时任务状态。
- API Key、token、password、private key。
- 未授权第三方全文。
- 某次私有会话记录全文。

## `skills/`

`skills/` 存放本 Pal 的专业技能。这里的 Skill 主要是“认知技能 / 工作方法”，不是脚本工具。

推荐结构：

```text
skills/
  index.md
  example-skill/
    SKILL.md
    README.md
```

每个 `skills/<skill-name>/SKILL.md` 建议包含：

| 字段 | 说明 |
| --- | --- |
| `name` | 技能名。 |
| `description` | 技能用途。 |
| `when to use` | 什么时候使用。 |
| `inputs needed` | 需要哪些输入。 |
| `steps` | 处理步骤。 |
| `output format` | 输出格式。 |
| `safety notes` | 风险边界。 |

如果用户明确要求保存 Skill，或相似任务重复出现三次以上，开发者可以把它整理为本 Pal 自己的正式 Skill，而不是放到全局 runtime skills 目录。

## `workflows/`

`workflows/` 存放更长的多步骤流程，通常会组合多个 Skill。

适合放：

- 项目恢复流程。
- 开发计划流程。
- 发布检查流程。
- 文档整理流程。
- 交接流程。

区别：

| `skills/` | `workflows/` |
| --- | --- |
| 单项能力。 | 多步骤流程。 |
| 可独立调用。 | 通常组合多个技能。 |
| 例如“生成任务提示词”。 | 例如“从项目状态分析到下一轮开发计划”。 |

## `runbooks/`

`runbooks/` 存放可复用操作手册。

适合：

- 重复多次。
- 流程稳定。
- 步骤清楚。
- 可验证。

不适合：

- 一次性想法。
- 临时闲聊。
- 用户私密内容。
- 还没验证过的经验。

## `learning/`

`learning/` 用来沉淀本 Pal 自己领域内的经验。

| 文件 | 用途 |
| --- | --- |
| `README.md` | 说明 learning 的规则。 |
| `knowledge-gaps.md` | 知识缺口。 |
| `repeated-tasks.md` | 重复任务记录。 |
| `skill-candidates.md` | 候选 Skill。 |
| `runbook-candidates.md` | 候选 Runbook。 |
| `workflow-candidates.md` | 候选 Workflow。 |

原则：

- 领域经验归属于对应专业 Pal。
- Mira 不应统一保存所有专业经验。
- 不写入用户隐私、私有项目事实、密钥或真实日志。
- 候选内容需要经过维护者或用户确认后再变成正式 Skill、Runbook 或 Workflow。

## `memory/`

`memory/` 是本 Pal 的记忆占位。发布包里不放真实记忆。

发布版建议只保留：

```text
memory/
  README.md
```

不要发布：

- `memory/user-real-data.md`
- `memory/project-private-notes.md`
- `memory/runtime-history.md`
- 用户偏好、私人事实、真实客户信息或未经确认的长期记忆。

## `state/`

`state/` 是运行状态占位。发布包里不应放真实运行状态。

发布版建议只保留：

```text
state/
  README.md
```

不要提交当前任务、当前上下文、Runtime 临时状态或会话状态。

## `reports/`

`reports/` 是任务报告输出占位。

发布版建议只保留：

```text
reports/
  README.md
```

真实任务报告可能包含用户项目内容、文件路径、执行日志或内部判断，通常应保持本地私有或被 `.gitignore` 排除。

## `examples/`

`examples/` 是示例，不是规则。

适合放：

- 基础使用示例。
- 正确输出示例。
- 错误示例。
- 公开安全的 synthetic 示例。

如果示例里出现某个协作 Pal，必须标注：

```text
This is a non-binding example.
这是非绑定示例，不是固定路由规则。
```

## `evals/`

`evals/` 存放本 Pal 的自测。

建议至少包含：

- `README.md`
- `pal-self-test.md`
- 输出契约检查。
- 是否越界检查。
- 是否出现硬编码路由检查。
- 是否误称自己为 Agent Runtime 的检查。

示例测试目标：

```text
/pal PalName 请处理一个典型领域任务
```

应检查：

- 是否使用本 Pal 的身份和语气。
- 是否符合 `core/output-contract.md`。
- 是否请求必要输入。
- 是否区分 Pal 层和 Runtime 执行层。
- 是否没有启动 Subagent Mode 或多 Agent 执行。

## 不建议放进 Pal Pack 的目录

旧版或独立项目式 Pal 里可能出现一些目录。新版内嵌 Pal Pack 通常不应保留它们。

| 旧目录 | 建议 | 原因 | 有价值内容迁到哪里 |
| --- | --- | --- | --- |
| `.agentpal/` | 删除 | 这是外部项目绑定目录，不属于 Pal Pack。 | 不迁移。 |
| `.agents/` | 删除或迁移 | Runtime 适配层，不应默认放在 Pal 内。 | `core/` 或 `skills/`。 |
| `.claude/` | 删除或迁移 | Claude Code 专属配置，不是通用 Pal 资产。 | Runtime guide 或未来适配包。 |
| `adapters/` | 删除 | 主体层 / Runtime 层职责。 | AgentPal 主体未来统一管理。 |
| `contacts/` | 删除 | Pal 联系册由 AgentPal 主体维护。 | `AgentPal/workspace/organization/contacts/`。 |
| `registry/` | 删除 | 旧 registry 只保留兼容/历史导航，不属于 Pal Pack。 | AgentPal 主体兼容目录。 |
| `runtime/` | 删除 | Runtime 信息由 AgentPal 主体维护。 | `AgentPal/runtime/`。 |
| `models/` | 删除 | 模型信息由 AgentPal 主体维护。 | `AgentPal/models/`。 |
| `plugins/` | 删除 | 插件信息由 AgentPal 主体维护。 | `AgentPal/plugins/`。 |
| `orchestration/` | 多数删除 | 全局调度属于 AgentPal 主体。 | Pal 专属流程迁到 `workflows/` 或 `core/`。 |
| `coordination/` | 多数删除 | 全局协作协议由主体维护。 | Pal 专属协作边界迁到 `core/collaboration-protocol.md`。 |
| `imports/` | 删除或迁移 | 外部资源导入由主体统一管理。 | 专属知识迁到 `knowledge/references/`。 |
| `tools/` | 谨慎保留 | 容易引入运行依赖。 | 仅在明确 optional 且 public-safe 时保留。 |

## Public-safe 规则

Pal Pack 模板和公开 Pal Pack 必须保持 public-safe。

不要提交：

- 真实用户记忆。
- 私有项目状态。
- 真实客户数据。
- API key、token、password、secret、credential、private key。
- 本机绝对路径。
- 未授权日志全文。
- 内部开发报告。
- 临时运行状态。

可以提交：

- README。
- 模板。
- public-safe 占位文件。
- 合成示例。
- 稳定专业知识。
- 可公开的检查清单。
- 输出契约和工作协议。

## 协作和路由边界

单个 Pal Pack 可以说明自己的协作习惯，但不应硬编码其它 Pal 的固定路线。

正确写法：

```text
需要协作时，从当前 AgentPal 中央 Pal roster 中解析合适协作者。
```

错误写法：

```text
所有开发任务必须交给 Atlas。
所有发布检查必须交给 Quinn。
```

Pal capability 示例只能作为 orientation，不能变成 route map。

## Runtime 边界

Pal 不直接执行动作。

Pal 可以：

- 组织目标。
- 选择上下文。
- 生成 Task Package。
- 给出检查清单。
- 要求证据。
- 验证结果。
- 总结下一步。

Runtime 才执行：

- 读写文件。
- 运行命令。
- 调用工具。
- 修改系统。
- 发布内容。
- 删除数据。

如果真实执行发生，报告中必须说明证据来自当前 Codex / Runtime / 工具层，而不是说 Pal 自己执行了这些动作。

## 开发者检查清单

发布或注册 Pal Pack 前，请检查：

- [ ] `PAL.md` 清楚说明身份、职责和边界。
- [ ] `AGENTS.md` 说明本 Pal 的 Runtime 工作规则。
- [ ] `SKILL.md` 是 Pal Pack 入口，不是单一工具 Skill。
- [ ] `pal.json` 是合法 JSON。
- [ ] `pal.json` 没有固定路由表或 `domain_map`。
- [ ] `core/output-contract.md` 能约束本 Pal 的输出。
- [ ] `identity/` 至少有 persona、voice、boundaries。
- [ ] `knowledge/` 只包含 public-safe 专业知识。
- [ ] `skills/` 中的 Skill 属于本 Pal 的专业领域。
- [ ] `learning/` 不包含真实用户隐私或私有项目事实。
- [ ] `memory/`、`state/`、`reports/` 只保留公开安全占位。
- [ ] `examples/` 使用合成或占位数据。
- [ ] `evals/` 检查身份、边界、输出契约和硬编码路由风险。
- [ ] 没有 `.agentpal/`、`.claude/`、`contacts/`、`registry/` 等主体层目录。
- [ ] 没有把 Deep Conductor、Subagent Mode 或多 Agent 执行写成当前 active 能力。

## 一句话标准

```text
AgentPal 主体负责系统层。
Pal Pack 只负责专业层。
```

更具体一点：

```text
AgentPal 主体负责 central roster / runtime / models / plugins / orchestration / project binding。
Pal Pack 负责 identity / core / knowledge / skills / workflows / runbooks / learning / examples / evals / public-safe placeholders。
```
