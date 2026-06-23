# architecture-review

运行时 Skill 入口请看 SKILL.md；README.md 仅作为人类阅读说明。


中文名：架构审查

## 用途

检查开发方案、任务拆分或执行层结果是否破坏 AgentPal 的职责边界、模块分层和可维护性。

## 适用场景

- 任务涉及 Core、Pal、Runtime、Adapter、工具或通讯录边界。
- 执行层计划大范围重构。
- 用户要求把调度、执行、审批或记忆写入某个不合适层级。
- 代码审查中发现改动范围异常大。

## 不适合场景

- 纯文案或小格式修改。
- 没有架构影响的小范围补丁。
- 用户只需要测试计划或浏览器验证。

## 输入信息

- 方案或执行层完成报告。
- 相关目录和模块职责。
- 修改范围、禁止事项和验收标准。
- 任何涉及 Core / Pal / Runtime / Adapter 的改动说明。

## 处理流程

1. 判断涉及哪些边界：Core、Pal、Runtime、Adapter、Skill、工具、通讯录。
2. 检查是否把 Core 做成 Planner、Router、Executor 或审批者。
3. 检查是否把 Pal 做成直接执行器。
4. 检查 Runtime / Adapter 是否越权写记忆、做规划或审批。
5. 检查是否过度设计、过度抽象或跨范围重构。
6. 给出风险、替代方案和验收建议。

## 输出格式

```text
## 架构结论

## 涉及边界

## 发现的问题

## 风险等级

## 建议调整

## 验收标准
```

## 验收标准

- 明确说明是否越界。
- 能指出具体责任层。
- 给出可执行调整建议。
- 不以抽象洁癖替代真实风险判断。

## 风险边界

架构审查不能变成无边界重构建议。Atlas 应优先保护最小可验证改动和可回滚路径。

## 与 Atlas 其他 Skill / Runbook 的关系

- `code-review-and-quality` 发现结构风险时调用本 Skill。
- `security-and-hardening` 处理权限、凭据和高风险操作。
- `development-lifecycle` 在计划和 review 阶段调用本 Skill。

