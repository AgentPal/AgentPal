# Claude Code Handoff

Claude Code 适合长上下文理解、项目级修改和复杂架构判断。

交接给 Claude Code 时，Atlas 应提供：

- 项目路径。
- 当前目标。
- 必读文档。
- 关键文件范围。
- 不允许修改的区域。
- 项目约束和架构边界。
- 验收标准。
- evidence 返回格式。

如果任务涉及大范围重构，Atlas 应先要求 Claude Code 输出计划和影响范围，再进入执行。

