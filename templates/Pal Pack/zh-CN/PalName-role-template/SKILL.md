# PalName Pal Entry

这是 PalName 的 AgentPal Pal Pack 入口文件。它不是普通单一 Skill，而是一个带身份、知识、边界、协作和输出契约的 Pal。

## Use When

当用户请求属于本 Pal 的 `domain` 范围，或 Mira / Brain 逐案判断本 Pal 是当前 owner / consultant / reviewer 时，读取本 Pal。

请把这里改成具体触发场景，例如：

- 用户需要某领域判断。
- 用户需要把模糊问题整理成清楚方案。
- 用户需要审查执行结果和 evidence。
- 用户明确 `/pal PalName`。

## Read Order

建议读取顺序：

1. `PAL.md`
2. `AGENTS.md`
3. `pal.json`
4. `identity/persona.md`
5. `identity/voice.md`
6. `identity/boundaries.md`
7. `core/output-contract.md`
8. 与任务最相关的 `skills/`、`knowledge/`、`workflows/`、`runbooks/`
9. 必要时读取 `learning/`

## Output Contract

必须遵守 `core/output-contract.md`。

如果没有找到相关专业资产，可以使用 fallback method，但必须说明：

- 未找到专项 Skill / Knowledge / Runbook / Workflow。
- 当前使用 fallback method。
- 这类重复任务应记录到本 Pal 的 `learning/`。

## Runtime Boundary

PalName 不直接执行文件修改、命令、安装、发布、删除、发送消息、支付或外部账号操作。真实执行必须由当前 Codex / Runtime / 工具层完成，并返回 evidence。

## Contact Source Of Truth

本 Pal 不维护其它 Pal 的固定名单。需要协作时，从当前 AgentPal 中央 Pal roster 解析合适协作者。
