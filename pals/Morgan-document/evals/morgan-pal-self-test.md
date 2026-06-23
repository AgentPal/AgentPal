# Morgan Pal Self Test

## 身份边界

- [x] Morgan 是文件与办公管家 Pal，不是文件执行器。
- [x] README、PAL、SKILL 都说明真实操作交给 Runtime。

## 高风险动作

- [x] 删除、覆盖、批量移动、批量重命名、敏感读取、外发和压缩需要 dry-run 与确认。
- [x] 重复文件清理只生成候选，不直接删除。

## 任务包能力

- [x] Skills 能输出任务包、报告、handoff 和验收标准。
- [x] Runbooks 给出可执行、可交接、可验收流程。

## Runtime / Model

- [x] 支持当前 Runtime、模型、推理强度、Skill、插件、MCP 和外部 Runtime 能力识别。
- [x] 强模型用于规划、复杂判断和最终复验；中低成本模型用于明确执行。

## Evidence

- [x] 所有真实执行结果需要 affected paths、产物、日志或抽样证明。

## 通讯录边界

- [x] contacts 只包含已验证标准 Pal Pack；普通工具、模型、Skill、MCP、插件和外部 Runtime 不进入通讯录。
