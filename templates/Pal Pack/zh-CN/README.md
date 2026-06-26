# PalPack 中文模板

这是 AgentPal Pal Pack 的中文目录模板，用于单独发布、复制、改名并创建新的 Pal。

Pal 是一个可以被 AgentPal / Codex 读取的长期工作伙伴目录。它不是单个 prompt，也不是普通 Skill。一个 Pal Pack 应包含身份、职责、边界、输出契约、知识、技能、流程、学习区和公开安全的占位状态。

## 目录内容

本目录当前包含一个可复制模板：

| 路径 | 用途 |
|---|---|
| `PalName-role-template/` | 新 Pal 的模板目录。复制后改成你的 Pal 目录名，例如 `Luna-designer`。 |
| `README.md` | 本说明文件，介绍 PalPack 模板结构、使用方式、删除方式和维护规则。 |

## Pal 目录结构

模板目录结构如下：

| 路径 | 用途 |
|---|---|
| `PAL.md` | Pal 的主体身份说明：是谁、负责什么、不负责什么、如何协作。 |
| `SKILL.md` | Pal 的入口说明：Codex / AgentPal 读取这个 Pal 时先看什么、适合什么任务。 |
| `AGENTS.md` | Codex 工作区指令：当 Codex 位于这个 Pal 目录内时应遵守的规则。 |
| `pal.json` | 机器可读元数据：id、名称、别名、直接调用命令、协作开关、入口文件等。 |
| `README.md` | 面向用户的 Pal 简介：如何使用、目录说明、边界说明。 |
| `identity/` | 人格、语气、边界等身份资产。 |
| `core/` | 核心协议：输出契约、协作协议、记忆规则、运行时边界等。 |
| `skills/` | 正式 Skill。用户明确要求保存 Skill，或同类任务超过 3 次时，优先沉淀到这里。 |
| `knowledge/` | 可复用知识卡、方法卡、判断原则。 |
| `workflows/` | 多步骤工作流，例如从模糊需求到可交付结果的完整流程。 |
| `runbooks/` | 可重复执行的操作手册或检查步骤。 |
| `learning/` | 候选学习区：知识缺口、重复任务、待晋升为 Skill / Runbook / Workflow 的内容。 |
| `examples/` | 非绑定使用示例。示例不能变成硬编码路由规则。 |
| `evals/` | 自测用例、发布前检查、回归验收。 |
| `memory/` | 运行时记忆占位目录。公开发布包中只放 README 或 `.gitkeep`，不要放私人记忆。 |
| `state/` | 运行时状态占位目录。公开发布包中不要放真实会话状态。 |
| `reports/` | 运行报告占位目录。公开发布包中不要放私人项目报告。 |

## 如何创建新的 Pal

1. 复制模板目录：

```text
PalName-role-template
```

2. 把复制后的目录改名为：

```text
Name-role
```

例如：

```text
Luna-designer
Kai-finance
Momo-study
```

3. 修改这些文件中的占位内容：

| 文件 | 必改内容 |
|---|---|
| `pal.json` | `id`、`name`、`display_name`、`directory_name`、`role`、`direct_call`、`aliases`、`description`。 |
| `PAL.md` | Pal 的身份、职责、边界、工作方式、协作方式。 |
| `SKILL.md` | 这个 Pal 适合在什么任务中被读取，以及读取顺序。 |
| `AGENTS.md` | 目录级运行规则，尤其是边界和输出规则。 |
| `README.md` | 给使用者看的介绍。 |
| `identity/` | 人格、语气、边界。 |
| `core/output-contract.md` | 回答时必须包含什么内容。 |

4. 根据需要补充：

| 目录 | 适合补充的内容 |
|---|---|
| `skills/` | 正式可复用 Skill。 |
| `knowledge/` | 领域知识、判断原则、术语表。 |
| `workflows/` | 多步骤工作流程。 |
| `runbooks/` | 检查清单、处理步骤、复盘方法。 |
| `examples/` | 合格示例和失败示例。 |
| `evals/` | 自测和发布前验收。 |

## 放到什么位置

把新 Pal 目录放到 AgentPal 工作区的：

```text
AgentPal/pals/
```

示例：

```text
AgentPal/pals/Luna-designer/
```

把目录放入 `pals/` 之后，还需要在 AgentPal 工作区执行注册提示词，让 Runtime 检查新 Pal Pack 并更新 contacts / registry。仅复制目录或重启外部项目会话，不应被当成已经完成注册。

注册方式：

- Codex：把 AgentPal 目录作为 Codex 项目打开，复制并粘贴 `prompts/add-pal-to-agentpal.md`。
- Claude Code：在终端进入 AgentPal 工作区目录，运行 `claude`，复制并粘贴 `prompts/add-pal-to-agentpal.md`。
- 其它 CLI Agent：在终端进入 AgentPal 工作区目录，启动对应 CLI Agent，复制并粘贴 `prompts/add-pal-to-agentpal.md`。

如果只是修改已有 Pal 或需要重建索引，可以使用 `prompts/refresh-pal-index.md`。如果你平时是在外部项目目录中使用 AgentPal，注册完成后，外部项目会话仍显示旧 Pal 列表时再重新初始化该会话。

## 如何调用

注册后，用户可以用：

```text
/pal Luna
@Luna
```

普通消息仍默认先交给 Mira。专业任务由 Mira / Brain 根据当前 contacts / registry 和上下文逐案判断 owner Pal。不要在 Pal 内部写死“某类任务必须交给某个 Pal”。

## 如何删除 Pal

删除对应 Pal 目录即可：

```text
AgentPal/pals/Luna-designer/
```

删除后，在 AgentPal 工作区执行 `prompts/refresh-pal-index.md`，让 AgentPal 重新检查 `pals/`，并从通讯录 / 注册表中去除已经不存在的 Pal。

如果某个会话中仍显示旧 Pal，通常是会话尚未刷新。重新初始化 AgentPal 工作区即可。

## 发布注意事项

- 不要把私人用户记忆、真实项目状态、客户资料、密钥、Token、账号、内部开发资料放入公开 Pal Pack。
- `memory/`、`state/`、`reports/` 默认只放 README 或 `.gitkeep`。
- 示例可以提到其它 Pal，但必须标明是非绑定示例。
- Pal Pack 不维护其它 Pal 的固定名单。协作者应从当前 AgentPal `contacts/` / `registry/` 中解析。
- `pal.json` 必须保持合法 JSON。
- 新增 Skill 时，优先放到本 Pal 自己的 `skills/` 目录，并更新 `skills/index.md`。

## 最小可用检查

发布前至少检查：

| 检查项 | 通过条件 |
|---|---|
| JSON | `pal.json` 可以正常解析。 |
| 入口文件 | `PAL.md`、`SKILL.md`、`AGENTS.md`、`README.md` 都存在。 |
| 身份 | Pal 名称、角色、边界清楚。 |
| 直接调用 | `direct_call` 与 `aliases` 可读、可用。 |
| 输出契约 | `core/output-contract.md` 写清楚回答格式和证据要求。 |
| 私密数据 | 没有私人记忆、真实项目状态、密钥或内部记录。 |
