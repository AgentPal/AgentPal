# Dispatch Protocol

Pal 应根据任务边界选择执行方式。

## 执行方式

- self：自己执行。
- skill：调用 Skill。
- tool：调用工具。
- agent：委托外部 Runtime 或线程。
- consult-pal：咨询其他 Pal。
- delegate-pal：委托其他 Pal 子任务。
- handoff-pal：转交任务 owner。
- joint-work：共同工作。

## 派发要求

每次派发应包含目标、输入、边界、验收标准、风险和回传格式。
