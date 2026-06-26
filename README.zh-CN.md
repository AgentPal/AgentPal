# AgentPal

AgentPal 是一个搭建 AI 团队的轻量框架，可运行在 Codex、Claude Code、OpenCode、OpenHands 等 Agent Runtime 之上。

它让用户创建不同职责的 Pal，并把这些 Pal 组织成一个有分工、有记忆、有知识、有技能、有工作流、有协作规则的 AI 团队。

AgentPal，让每个 Agent 都有自己的 Pal。

AgentPal v0.1.0-rc.1 是一个 Markdown / JSON / protocol workspace，可用于能读取结构化工作区文件的 Runtime。它不是 Agent Runtime，不是多 Agent Runtime，不是执行层，不是桌面 App，不是 Web App，也不是安装器。

## PalSmith

PalSmith 是 AgentPal 的 AI 团队创建师，也是 Pal 资产治理 Pal。它帮助用户通过自然语言创建、完善、体检、导入、导出、升级和维护 Pal 与 Pal 团队，不需要用户先理解完整的 Pal Pack 目录结构。

详细了解 PalSmith：[PalSmith是什么，怎么使用？](docs/01-concepts/09-What-is-PalSmith-how-can-I-operate-it.md)

v0.2 开发会重点产品化这条路径。可以从 [v0.2 development plan](docs/09-roadmap/v0.2-development-plan.md)、[v0.2 task pool](docs/09-roadmap/v0.2-task-pool.md) 和 [PalSmith end-to-end productization](docs/06-palsmith/palsmith-end-to-end-productization.md) 开始。首个实现切片补齐了创建首个专业 Pal 与从目标创建 AI team 的可复制任务包。

v0.2 Capability Inventory 见 [minimal usable design](docs/05-orchestration-methodology/capability-inventory-minimal-usable-design.md) 和 [capability profile index](capabilities/README.md)。这些 profile 是示例性的判断输入，不是自动环境扫描结果。

v0.2 release regression 见 [PalBench Light Suite](evals/palbench-light/README.md) 和 [suite plan](docs/research/palbench-light-suite-plan.md)。

Runtime Adapter 排障与 thin binding 稳定性见 [stability guide](docs/04-runtime-guides/runtime-adapter-stability-guide.md) 和 [troubleshooting prompt cards](docs/04-runtime-guides/runtime-adapter-troubleshooting-prompt-cards.md)。

## 为什么需要 AgentPal？

用户想让 Agent 更好用时，通常会走两条路：

- 给 Agent 加更多 Skill
- 搭一个 Agent Team

Skill 很轻，但容易碎片化。一个 Skill 往往只做一件事，用户很难记住什么时候用哪个 Skill，也很难让单个 Skill 长期拥有上下文、记忆、工作流、验收标准和复盘经验。

Agent Team 很强，但也更重。它可能需要复杂配置、重复上下文、更高上下文成本、角色协调、结果合并和权限边界。

AgentPal 补的是中间层：Pal。Pal 把许多 Skills、知识卡、工作流、记忆规则和验证习惯，组织成少数几个好记的工作伙伴。

用户不应该记住几百个 Skill。用户只需要记住几个 Pal，以及每个 Pal 负责什么。

## Pal 是什么？

Pal 不是一个单独 Skill。

Pal 也不是新的 Agent Runtime。

Pal 是一个可移植的工作伙伴，由身份、知识、Skills、记忆规则、工作流、上下文规则、输出契约、验证习惯和协作协议组成。

“Pal”这个名字强调的是可记住、可协作的工作伙伴，而不是工具名。你可以把 Pal 理解成当前 Runtime 里的专业工作方式：它帮助 Runtime 理解目标、选择上下文、整理 Task Package、调用相关 Skill 或 fallback 方法，并检查结果是否真的完成。

详细了解 Pal：

- [为什么是 Pal？](docs/01-concepts/07-why-pal.md)
- [Pal 团队、多 Pal 协作与 Deep Conductor](docs/01-concepts/08-pal-teams-collaboration-and-deep-conductor.md)

## 当前版本能做什么

AgentPal v0.1.0-rc.3 当前提供：

- Markdown / JSON / protocol workspace，不需要额外 runtime 依赖
- Simple Pal Mode 作为当前激活的 runtime policy
- Mira 作为默认 Main Pal / Leader / Conductor，并补齐 leader knowledge、skills、workflows、runbooks、evals、research inventory、delegation、handoff、context packet、risk approval 和 progress reporting 资产
- 9 个官方 Pal：Mira、Atlas、Vega、Rhea、PalSmith、Quinn、Morgan、Harper、Nova
- 基于 contacts / registry 的 `/pal Name` 显式调用
- AI owner judgement、Fast Route owner-Pal handoff，以及禁止关键词硬路由的协作规则
- Task Package rules、Runtime Task Package 标准、Context Slicing、Asset Loading Budget
- PalSmith 作为官方 no-code Pal 资产治理 Pal，支持 Pal 创建、AI team 创建、job fitness 体检、用户材料摄取、可选 web research to knowledge、import、export、health check、versioning、publish readiness 和 Runtime Task Package planning
- PalSmith quickstart path、AI team blueprints、demo script、readiness matrix、task package templates、example packages、governance protocols 和 Markdown evals
- Formal Skill asset standard：219 个 formal skills 已映射到 Pal-owned skill assets，release standard 下 missing formal Skill assets 为 0
- Atlas、Vega、Rhea、Quinn、Morgan、Harper、Nova 的官方 Pal 深化资产，包括 role knowledge、skills、workflows、runbooks、evals、collaboration boundaries 和 research inventories
- `docs/08-release-candidate/` 下的 release candidate evidence，包括 PalSmith verification、default Pal sync、release review、no-code boundary review、formal Skill asset audit/fix、dirty worktree stage review、commit grouping plan 和 maintainer handoff reports
- Codex / Claude Code / Generic CLI Agent 使用指南，以及 thin project binding prompts
- PalBench small-sample validation

## 快速开始

日常使用可以先找 Mira。Mira 是默认 Main Pal / Leader Pal / Conductor：你把目标告诉她，她会判断是直接整理、补问关键问题、交给专业 Pal，还是生成 staged Runtime Task Package。可以先看 [Mira-first usage](docs/02-getting-started/mira-first-usage.md) 和 [Mira-first prompt cards](docs/02-getting-started/mira-first-prompt-cards.md)。

### Codex

适合直接在 Codex 中打开 AgentPal Workspace。

1. 在Codex中把AgentPal目录当作新项目创建。
2. 打开 [`prompts/codex/initialize-agentpal-workspace.md`](prompts/codex/initialize-agentpal-workspace.md)。
3. 复制整篇 prompt。
4. 粘贴到 Codex里 AgentPal项目对话中初始化 AgentPal。
5. 普通任务先交给 Mira，或用 `/pal Name` 指定专业 Pal。

Codex 的初始化 prompt 现在统一放在 [`prompts/codex/`](prompts/codex/) 下。Codex Workspace 初始化不需要设置 `AGENTPAL_HOME`。

详见：[`docs/04-runtime-guides/01-use-with-codex.md`](docs/04-runtime-guides/01-use-with-codex.md)

### Claude Code

适合把 AgentPal 接入你已有的真实项目。

1. 先进入你的项目目录：

   ```text
   cd <your-project>
   claude
   ```

2. 打开 [`prompts/claude-code/install-agentpal-current-project.md`](prompts/claude-code/install-agentpal-current-project.md)。
3. 不需要提前修改 prompt，直接复制整篇 prompt 文件。
4. 粘贴到 Claude Code 中执行。
5. Claude Code 提示你输入 AgentPal Workspace 路径时，输入你本机 AgentPal 目录路径，例如 `<path-to-AgentPal>`。
6. 让 Claude Code 创建或更新当前项目里的本地绑定文件。

Claude Code 路径会写入项目本地绑定文件，并可能更新 `.claude/settings.local.json`。这个文件是本机配置，不应该提交。

详见：[`docs/04-runtime-guides/02-use-with-claude-code.md`](docs/04-runtime-guides/02-use-with-claude-code.md)

### Generic CLI Agent

适合能读取项目文件、遵循 Markdown / JSON 指令、维护上下文并报告执行证据的 CLI Agent。

1. 先进入你的项目目录：

   ```text
   cd <your-project>
   <your-cli-agent>
   ```

2. 打开 [`prompts/generic-cli-agent/install-agentpal-current-project.md`](prompts/generic-cli-agent/install-agentpal-current-project.md)。
3. 不需要提前修改 prompt，直接复制整篇 prompt 文件。
4. 粘贴到 CLI Agent 中执行。
5. CLI Agent 提示你输入 AgentPal Workspace 路径时，输入你本机 AgentPal 目录路径，例如 `<path-to-AgentPal>`。

这是通用兼容路径。AgentPal 不承诺所有 CLI Agent 都已经完整验证。

详见：[`docs/04-runtime-guides/03-use-with-generic-cli-agent.md`](docs/04-runtime-guides/03-use-with-generic-cli-agent.md)

## 创建你自己的 Pal

AgentPal 在 [`templates/Pal Pack/`](<templates/Pal Pack/>) 下提供标准 Pal Pack 模板。你可以复制模板目录，改成自己的 Pal 名称，补充身份、输出契约、知识、Skills、示例和 public-safe 占位文件，然后把完成后的 Pal Pack 放入 [`pals/`](pals/) 目录。注册到 AgentPal contacts / registry 后，就可以像官方 Pal 一样使用。

当前模板：

- [`templates/Pal Pack/zh-CN/`](<templates/Pal Pack/zh-CN/>)
- [`templates/Pal Pack/en-US/`](<templates/Pal Pack/en-US/>)

注册复制好的 Pal Pack 时，在 AgentPal 工作区执行 [`prompts/add-pal-to-agentpal.md`](prompts/add-pal-to-agentpal.md)：

- Codex：把 AgentPal 目录作为 Codex 项目打开，然后把注册提示词粘贴到 AgentPal 项目对话中执行。
- Claude Code 或其它 CLI Agent：在终端进入 `<path-to-AgentPal>`，从这个目录启动 CLI Agent，然后粘贴注册提示词执行。

日常使用 AgentPal 时，用户通常是在自己的外部项目目录中工作；这是正常的。但 Pal 注册会修改 AgentPal 自身的 `contacts/` 和 `registry/` 文件，所以注册步骤应回到 AgentPal 工作区执行。注册完成后，如果外部项目会话仍显示旧 Pal 列表，再重新初始化该项目会话。

## 官方 Pal

| Pal | 职责 | 直接调用 |
| --- | --- | --- |
| Mira | Main Pal / Leader / Conductor | `/pal Mira` |
| Atlas | 开发与工程 | `/pal Atlas` |
| Nova | 产品与需求 | `/pal Nova` |
| Vega | 调研与分析 | `/pal Vega` |
| Rhea | 系统、环境与工具 | `/pal Rhea` |
| PalSmith | Pal 创建、AI 团队创建、Pal 资产治理、体检、导入导出与发布准备 | `/pal PalSmith` |
| Quinn | 质量、验证与发布检查 | `/pal Quinn` |
| Morgan | 文档、Office、PDF 与文件工作 | `/pal Morgan` |
| Harper | 写作、沟通与编辑 | `/pal Harper` |

Mira 是默认入口 Pal。专业 Pal 默认不监听；Mira 会在适合时交给它们，用户也可以直接用 `/pal Name` 调用。

真实任务示例见 [Official Pal examples index](docs/07-official-pals/official-pal-examples-index.md)。这些示例只是非绑定学习参考，不是静态指派规则。

## AgentPal 如何工作

1. 用户给出目标。
2. Mira 接收普通任务。
3. Mira 或 owner Pal 读取选定上下文。
4. Pal 整理 Task Package。
5. Host Runtime 执行文件读取、写入、命令、工具调用或发布动作。
6. Pal 根据证据验证并汇报结果。
7. 可复用经验可以沉淀成 Skill、Runbook、Workflow、知识记录或记忆候选。

## Pal vs Skill

| Skill | Pal |
| --- | --- |
| 单一能力 | 工作伙伴 |
| 通常只覆盖一种方法或任务 | 组织能力、上下文、记忆、工作流和验证 |
| 用户往往要记住何时调用 | 用户只要记住谁负责这类工作 |

Skill 是能力。Pal 是组织能力的工作伙伴。

## Pal Team vs Agent Team

| Agent Team | Pal Team |
| --- | --- |
| 多个 Agent 执行任务 | 多个 Pal Pack 组织任务 |
| 执行属于 Agent Runtime | 执行仍属于 Host Runtime |
| 可能带来配置、上下文和协调成本 | 负责上下文、Task Package、协作和验证 |
| 适合更重的多 Agent 执行 | 适合在不把 AgentPal 变成 Runtime 的情况下组织专业视角 |

Subagent 和多 Agent 执行属于 Runtime 层。Pal Team 可以为 Runtime Agent 准备和审查任务，但 AgentPal v0.1.0-rc.1 不是多 Agent Runtime。

## Deep Conductor

Deep Conductor 是 AgentPal 面向复杂任务的未来高级调度设计。它不是 v0.1.0-rc.1 的当前功能。当前版本请使用 Simple Pal Mode、Fast Route、Task Package、Context Slicing 和有边界的 Pal 协作。详见：[`docs/05-orchestration-methodology/11-pal-teams-and-deep-conductor.md`](docs/05-orchestration-methodology/11-pal-teams-and-deep-conductor.md)

## AgentPal 不是什么

AgentPal 不是：

- Agent Runtime
- 多 Agent Runtime
- 桌面 App
- Web App
- 安装器
- daemon 或 service
- marketplace
- Codex、Claude Code、OpenHands 或其他 Runtime 的替代品

AgentPal 是给现有 Runtime 使用的 Pal 层。实际文件操作、命令、工具调用和发布动作由 Host Runtime 执行，并且需要提供证据。

## 文档入口

- [为什么是 Pal？](docs/01-concepts/07-why-pal.md)
- [核心概念](docs/01-concepts/)
- [Pal Pack 标准](docs/03-pal-pack-standard/)
- [Runtime 指南](docs/04-runtime-guides/)
- [调度方法论](docs/05-orchestration-methodology/)
- [v0.2 路线图](docs/09-roadmap/v0.2-development-plan.md)
- [验证与证据](docs/06-validation-and-evidence/)
- [创建 Pal](docs/07-authoring-pals/)
- [Prompts](prompts/)
- [文档首页](docs/README.md)

## 贡献

贡献时请保持 v0.1.0-rc.1 的边界：AgentPal 是面向 Agent Runtime 的 Pal Workspace 和 Pal Pack 标准实践，当前只有 Simple Pal Mode 是 active task-handling path。

详见：[`CONTRIBUTING.md`](CONTRIBUTING.md)。

## License

MIT。见 [`LICENSE`](LICENSE)。
