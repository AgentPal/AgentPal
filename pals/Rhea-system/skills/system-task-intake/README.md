# system-task-intake

运行时 Skill 入口请看 SKILL.md；README.md 仅作为人类阅读说明。


中文名：系统与应用任务接入

## 用途

判断用户请求属于系统、应用、Runtime、依赖、权限、PATH、进程、磁盘、包导入还是故障恢复问题，并确定下一步是否只能先做只读检测。

## 适用场景

- “软件打不开 / 装不上 / 删不掉。”
- “Codex / Claude Code / Gemini CLI 不可用。”
- “Node / Python / Git / .NET / Flutter 找不到。”
- “电脑变慢、磁盘满、某个进程占用高。”

## 不适合场景

- 用户要求 Rhea 直接运行命令。
- 纯代码实现、测试失败或架构问题，应由当前 owner 从 contacts / registry 逐案解析合适协作对象。
- 事实查证或工具来源研究，应咨询问从当前 contacts / registry 解析出的合适协作对象。

## 输入信息

- 用户描述。
- 操作系统和版本，如果可得。
- 软件、Runtime、命令、项目或错误摘要。
- 是否允许只读检测、管理员权限和外部 Runtime。

## 处理流程

1. 识别问题类型。
2. 标记风险等级：只读、低风险、需要权限、高风险。
3. 判断缺失信息。
4. 决定下一步 Skill 或 Runbook。
5. 输出只读优先的建议。

## 输出格式

```text
## 判断
## 缺失信息
## 建议先检查
## 风险等级
## 下一步 Skill / Runbook
```

## 验收标准

- 问题类型明确。
- 没有把模糊问题直接变成修复命令。
- 风险等级和下一步检测路径清楚。

## 风险边界

不能承诺已经检测或修复。不能要求用户直接复制危险命令。

## 与其他 Skill / Runbook 的关系

通常作为入口，后续连接 `environment-diagnosis-plan`、`permission-risk-review`、`runtime-setup-handoff` 或 `app-installation-handoff`。

