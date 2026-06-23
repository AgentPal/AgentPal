# Architecture Review Checklist

Atlas 架构审查关注责任边界。

## 检查项

- Core 是否被做成 Planner、Router、Executor 或审批者。
- Pal 是否被要求直接执行文件、命令或安装。
- Runtime / Adapter 是否承担了规划、记忆写入或审批。
- 改动是否超出本轮目标。
- 是否引入过度抽象或不可回滚重构。

## 输出

结论必须指出涉及层级、风险、建议调整和验收标准。

