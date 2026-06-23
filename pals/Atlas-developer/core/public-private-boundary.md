# Public / Private Boundary

本文说明 `pal-developer` 公开发布前应保留和排除的内容。

## 可以随公开包发布

- `README.md`、`SKILL.md`、`PAL.md`、`AGENTS.md`、`pal.json`。
- `LICENSE` 和公开说明文档。
- Atlas 自写 `skills/`、`knowledge/`、`core/`、`identity/`。
- Runtime / model / plugin / capability / orchestration 的公开模板和规则。
- `imports/skills/README.md` 与 `.gitkeep`。
- 不含私人数据的示例文件。

## 不应随公开包发布

- 用户私人记忆。
- 真实项目记忆和任务账本。
- 运行时状态、报告、日志和临时输出。
- 真实模型使用记录、外部 Runtime 使用记录和路由决策。
- 内部调研过程资料。
- 未经授权的第三方 Skill、知识包、工具包、MCP、插件或 Pal Pack。

## 内部调研资料

维护者调研、候选评估、License 细评、安全风险细评和导入计划应保存在维护者私有资料中，不放进公开 `pal-developer` 包。

D2 GitHub Skill 调研只保留公开摘要和风险结论；原始设计资料已转化为本 Pal Pack 内容，不要求用户访问维护者私有资料。

## imports/ 发布注意事项

`imports/` 是用户本地放外部资源的位置。官方公开包默认不打包第三方 Skill 源码。

如果用户要发布自己的 Pal Pack，并包含 `imports/` 中的第三方资源，必须先确认：

- 原始 License 允许复制和再分发。
- 已保留版权声明、NOTICE 和 License 文件。
- 没有提交无授权内容。
- 没有提交密钥、日志、账号信息、私人项目资料或真实用户数据。

## memory/ 发布注意事项

`memory/` 下的模板可以公开，真实运行记忆不应公开：

- `memory/user/`：用户偏好和私人记忆，不提交。
- `memory/project/`：真实项目记忆、决策和任务账本，不提交。
- `memory/runtime/`：模型、Runtime、外部 Runtime 使用记录，不提交。

如果需要发布示例，只发布脱敏的模板，不发布真实用户数据。

## reports / state / reasoning

- `reports/`：执行报告和验收记录，默认不提交。
- `state/`：运行时状态，默认不提交。
- `reasoning/solution-log.md`、`reasoning/decision-trace.md`：真实推理和决策日志，默认不提交。

公开包应保留规则和模板，不保留真实运行痕迹。

