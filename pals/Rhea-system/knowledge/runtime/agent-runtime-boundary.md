# Agent Runtime Boundary

Codex、Claude Code、OpenHands、Gemini CLI、DeepSeek-TUI 等是 Runtime / 外部 Runtime 候选，不是 Pal 通讯录成员。

它们可以接收 Rhea 的执行任务包：

- 只读检测。
- 安装配置。
- 日志摘要。
- evidence 回收。

它们不能被写入 `contacts/`，除非未来被包装成标准 Pal Pack，包含 `PAL.md`、`pal.json` 且开启协作开关。

