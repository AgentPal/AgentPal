# Create A Composite Pal With PalSmith

Copy this prompt into AgentPal when you want PalSmith to design a composite Pal.

```text
/pal PalSmith 请帮我创建一个组合式 Pal。

我希望：
- Pal 名称：
- 岗位职责：
- 想蒸馏的思维方式：
- 想蒸馏的性格和说话风格：
- 行业或任务场景：
- 岗位知识来源：
- 需要会使用的 Skill / 插件 / 外部软件：
- 这个 Pal 是私有、团队内部、公开示例，还是 Marketplace 候选：

如果我没有填完整，请先用不超过 3 个问题追问最关键缺口。

请先输出创建计划，区分：
- 思维方式
- 性格和语气
- 岗位职责
- 岗位知识
- Skill / Agent 使用建议
- 记忆与复盘
- 隐私、授权和公开发布边界
- eval 验证计划

如果我继续要求生成 draft Pal Pack，或者当前任务明确是受控测试 /
fixture 创建，请输出可执行的 draft Pal Pack 文件映射和 Runtime Task
Package。文件映射至少包含：

- `pal.json`
- `PAL.md`
- `SKILL.md`
- `README.md`
- `identity/`
- `knowledge/`
- `workflows/`
- `memory/`
- `prompts/`
- `evals/`
- `metadata-draft.md`

生成的 draft / custom Pal 必须继承 Pal Asset Execution Contract。不要只生成
persona、role 或 voice seed。文件映射和创建计划必须包含：

- `completeness_level`，只能使用 `persona_only`,
  `persona_plus_voice`, `role_plus_knowledge`, `role_plus_workflow`,
  `executable_pal`, `verified_pal`
- Pal Runtime Read Order
- Asset Path Map
- Task Asset Packet 使用规则
- Asset Use Summary 使用规则
- Missing Asset Plan 规则
- No Blind Tool Call Rule
- `tool_vs_pal_asset_boundary`

draft Pal Pack 默认必须是：

- `official: false`
- `status: draft_test_artifact` 或 `draft`
- 不进入 `official/pals/`
- 不进入 `workspace/organization/contacts/`
- 不公开 Marketplace listing
- 不包含 runtime/backend/CLI/scanner/daemon/connector

如果安装为 user custom Pal，需要先使用
`prompts/palsmith/install-draft-as-custom-pal.md` 准备安装计划。user
custom Pal 默认私有、discovery 关闭、delegation 关闭、contacts
registration 关闭、Marketplace public listing 关闭。

不要直接声称已经创建 official Pal。
不要修改 central contacts。
不要把私有资料写成公开示例或公开 Marketplace 商品。
等我确认后，再准备 Pal Pack 创建 Task Package。
```

Notes:

- You can leave fields blank.
- PalSmith should make assumptions and ask only the most important missing questions.
- Host runtime actions still require confirmation and evidence.
