# AgentPal Core Is Not Agent

AgentPal Core 不应成为隐藏的执行器、Router、Planner 或 Brain。

## Core 不做

- 不直接判断任务类型并生成业务结果。
- 不按关键词硬路由任务。
- 不自己选择 Runtime 执行用户任务。
- 不自己创建或批准高风险操作。
- 不直接执行文件操作、shell 命令或依赖安装。
- 不把普通 Skill 当成 Pal。

## Core 可以做

- 承载标准目录和协议。
- 连接 Pal Pack、Runtime、通讯录和资源索引。
- 展示任务、审批、状态和 evidence。
- 回收执行层结果并交给 Pal / Runtime 复验。

Atlas 看到开发方案让 Core 做执行、规划、审批或隐藏路由时，应标记为越界风险。

